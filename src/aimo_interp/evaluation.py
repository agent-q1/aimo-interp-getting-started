"""Generate one response and score its final mathematical answer."""

from collections.abc import Callable

from latex2sympy2_extended import NormalizationConfig
from math_verify import ExprExtractionConfig, LatexExtractionConfig, parse, verify

from .model import solve, solve_batch


class MathVerifyScorer:
    """Compare the last boxed answer with a numeric reference using Math-Verify."""

    def __init__(self, expected_answer: str | int):
        self.expected = parse(
            str(expected_answer), extraction_config=[ExprExtractionConfig()],
            fallback_mode="no_fallback", extraction_mode="first_match",
        )
        if not self.expected:
            raise ValueError(f"Cannot parse reference answer: {expected_answer!r}")

    def extract(self, response: str) -> list:
        """Extract and normalize the final box; do not fall back to prose numbers."""
        last_box = response.rfind(r"\boxed")
        if last_box < 0:
            return []
        return parse(
            response[last_box:],
            extraction_config=[LatexExtractionConfig(
                boxed_match_priority=0,
                normalization_config=NormalizationConfig(
                    basic_latex=True, units=True, malformed_operators=True,
                    nits=True, boxed="last", equations=False,
                ),
            )],
            fallback_mode="no_fallback", extraction_mode="first_match",
        )

    def __call__(self, response: str) -> bool:
        predicted = self.extract(response)
        return bool(predicted and verify(self.expected, predicted))


def evaluate(
    problem: str,
    scaffolding_prompt: str,
    model,
    scorer: Callable[[str], bool],
    *,
    tokenizer,
    max_new_tokens: int = 8192,
    enable_thinking: bool = True,
) -> dict:
    """Run one generation and score its final response, retaining diagnostics."""
    result = solve(
        problem, max_new_tokens=max_new_tokens, model=model, tokenizer=tokenizer,
        scaffolding_prompt=scaffolding_prompt,
        enable_thinking=enable_thinking, stream=False,
    )
    return _score_response(result, scorer, enable_thinking)


def _score_response(result: dict, scorer: Callable[[str], bool], enable_thinking: bool) -> dict:
    response = result["response"]
    if "</think>" in response:
        final_response = response.rsplit("</think>", 1)[1].strip()
    elif enable_thinking:
        # Qwen's thinking template opens <think> in the prompt. Without the
        # closing tag, any boxes in the generated text are still reasoning.
        final_response = ""
    else:
        final_response = response.strip()
    return {
        **result,
        "final_response": final_response,
        "is_correct": bool(scorer(final_response)),
    }


def evaluate_batch(
    problems: list[str], scaffolding_prompt: str, model,
    scorers: list[Callable[[str], bool]], *, tokenizer,
    max_new_tokens: int = 8192, enable_thinking: bool = True,
) -> list[dict]:
    """Generate a fixed batch and score each response against its own reference."""
    if len(problems) != len(scorers):
        raise ValueError("Provide exactly one scorer per problem")
    results = solve_batch(
        problems, max_new_tokens=max_new_tokens, model=model, tokenizer=tokenizer,
        scaffolding_prompt=scaffolding_prompt, enable_thinking=enable_thinking,
    )
    return [_score_response(result, scorer, enable_thinking)
            for result, scorer in zip(results, scorers, strict=True)]
