"""Local Qwen loading, prompt formatting, and generation for the notebooks.

Use the uv notebooks dependency group. Loading defaults to the pinned cached
checkpoint, with all weights on GPU and 4-bit NF4 quantization.
"""

import faulthandler
import logging
import os
from pathlib import Path
import time

CACHE_DIR = Path(__file__).resolve().parents[2] / "data" / "huggingface"
os.environ.setdefault("HF_HOME", str(CACHE_DIR))

import torch
from transformers import AutoModelForImageTextToText, AutoTokenizer, BitsAndBytesConfig, TextStreamer

MODEL_ID = "Qwen/Qwen3.5-4B"
REVISION = "851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a"
ANSWER_INSTRUCTIONS = r"Solve the problem and put your final answer in \boxed{}. No need to verify"


def _hide_expected_cast(record: logging.LogRecord) -> bool:
    return not record.getMessage().startswith("MatMul8bitLt: inputs will be cast from")


logging.getLogger("bitsandbytes.autograd._functions").addFilter(_hide_expected_cast)


def format_problem(problem: str, scaffolding_prompt: str = ANSWER_INSTRUCTIONS) -> str:
    """Append the same answer-format instruction without changing the problem."""
    return problem + "\n\n" + scaffolding_prompt


def load_model(
    *, quantization_bits: int = 4, compute_dtype=None, local_files_only: bool = True,
):
    """Return (model, tokenizer). Restart the notebook kernel before reloading."""
    if quantization_bits not in (4, 8):
        raise ValueError("Choose 8-bit or 4-bit weights.")
    if not torch.cuda.is_available():
        raise RuntimeError("A CUDA GPU is required to load the model.")
    if compute_dtype is None:
        compute_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    if quantization_bits == 8:
        quantization_config = BitsAndBytesConfig(load_in_8bit=True)
    else:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=compute_dtype,
        )
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    common = dict(revision=REVISION, local_files_only=local_files_only, cache_dir=str(CACHE_DIR / "hub"))
    print({"model": MODEL_ID, "revision": REVISION, "quantization_bits": quantization_bits,
           "compute_dtype": str(compute_dtype)})
    from transformers.models.qwen3_5.modeling_qwen3_5 import is_fast_path_available
    print("DeltaNet fast path:", is_fast_path_available)
    faulthandler.dump_traceback_later(60)
    try:
        started = time.perf_counter()
        print("Loading tokenizer...", flush=True)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, **common)
        print("Loading and quantizing weights on GPU...", flush=True)
        model = AutoModelForImageTextToText.from_pretrained(
            MODEL_ID, **common, quantization_config=quantization_config,
            dtype=compute_dtype, device_map={"": 0}, attn_implementation="sdpa",
        )
        model.eval()
        devices = {str(parameter.device) for parameter in model.parameters()}
        if devices != {"cuda:0"}:
            raise RuntimeError(f"Unexpected model placement: {devices}")
        print(f"Loaded in {time.perf_counter() - started:.1f} seconds")
        print(f"Model footprint: {model.get_memory_footprint() / 2**30:.2f} GiB")
        print(f"CUDA allocated: {torch.cuda.memory_allocated() / 2**30:.2f} GiB")
        print("Parameter devices:", sorted(devices))
        return model, tokenizer
    finally:
        faulthandler.cancel_dump_traceback_later()


def solve(problem: str, max_new_tokens: int = 256, *, model, tokenizer, enable_thinking: bool = True, stream: bool = True, scaffolding_prompt: str = ANSWER_INSTRUCTIONS) -> dict:
    """Generate a greedy response with optional streaming and return runtime metadata."""
    if max_new_tokens < 1:
        raise ValueError("max_new_tokens must be positive")
    messages = [{"role": "user", "content": format_problem(problem, scaffolding_prompt)}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=enable_thinking,
    )
    inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda:0")
    torch.cuda.reset_peak_memory_stats()
    print("Generating (tokens will appear below)..." if stream else "Generating...", flush=True)
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True) if stream else None
    torch.cuda.synchronize()
    started = time.perf_counter()
    with torch.inference_mode():
        output = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            streamer=streamer,
            use_cache=True, pad_token_id=tokenizer.eos_token_id,
        )
    torch.cuda.synchronize()
    elapsed = time.perf_counter() - started
    generated = output[0, inputs["input_ids"].shape[1]:]
    eos = model.generation_config.eos_token_id
    eos_ids = {eos} if isinstance(eos, int) else set(eos or [])
    return {
        "response": tokenizer.decode(generated, skip_special_tokens=True),
        "generated_tokens": len(generated),
        "hit_token_limit": len(generated) == max_new_tokens and int(generated[-1]) not in eos_ids,
        "elapsed_seconds": round(elapsed, 2),
        "tokens_per_second": round(len(generated) / elapsed, 2),
        "peak_allocated_gib": round(torch.cuda.max_memory_allocated() / 2**30, 2),
    }


def solve_batch(
    problems: list[str], max_new_tokens: int = 256, *, model, tokenizer,
    enable_thinking: bool = True, scaffolding_prompt: str = ANSWER_INSTRUCTIONS,
) -> list[dict]:
    """Generate one fixed batch, returning one result per problem in input order.

    All rows share the batch wall time and peak memory. Per-row token counts
    stop at the first EOS (inclusive), excluding padding added after completion.
    Batch throughput counts useful generated tokens across all rows.
    """
    if max_new_tokens < 1:
        raise ValueError("max_new_tokens must be positive")
    if not problems:
        return []
    prompts = [tokenizer.apply_chat_template(
        [{"role": "user", "content": format_problem(problem, scaffolding_prompt)}],
        tokenize=False, add_generation_prompt=True, enable_thinking=enable_thinking,
    ) for problem in problems]
    # Decoder-only generation reads the rightmost input position. Left padding
    # keeps that position on the actual prompt for every row.
    previous_padding_side, previous_pad_token = tokenizer.padding_side, tokenizer.pad_token
    try:
        tokenizer.padding_side = "left"
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token = tokenizer.eos_token
        inputs = tokenizer(
            prompts, padding=True, return_tensors="pt", add_special_tokens=False,
        ).to("cuda:0")
        pad_token_id = tokenizer.pad_token_id
    finally:
        tokenizer.padding_side, tokenizer.pad_token = previous_padding_side, previous_pad_token

    torch.cuda.reset_peak_memory_stats()
    torch.cuda.synchronize()
    started = time.perf_counter()
    print(f"Generating batch of {len(problems)}...", flush=True)
    with torch.inference_mode():
        output = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            use_cache=True, pad_token_id=pad_token_id,
        )
    torch.cuda.synchronize()
    elapsed = time.perf_counter() - started
    generated = output[:, inputs["input_ids"].shape[1]:].tolist()
    eos = model.generation_config.eos_token_id
    eos_ids = {eos} if isinstance(eos, int) else set(eos or [])
    sequences = []
    for sequence in generated:
        end = next((i + 1 for i, token in enumerate(sequence) if token in eos_ids), len(sequence))
        sequences.append(sequence[:end])
    batch_tokens = sum(len(sequence) for sequence in sequences)
    peak_memory = round(torch.cuda.max_memory_allocated() / 2**30, 2)
    return [{
        "response": tokenizer.decode(sequence, skip_special_tokens=True),
        "generated_tokens": len(sequence),
        "hit_token_limit": len(sequence) == max_new_tokens and sequence[-1] not in eos_ids,
        "elapsed_seconds": round(elapsed, 2),
        "tokens_per_second": round(len(sequence) / elapsed, 2),
        "peak_allocated_gib": peak_memory,
        "batch_size": len(problems),
        "batch_generated_tokens": batch_tokens,
        "batch_tokens_per_second": round(batch_tokens / elapsed, 2),
    } for sequence in sequences]
