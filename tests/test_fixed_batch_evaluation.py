"""Batch accounting and scoring checks without allocating GPU memory."""

import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import torch

from aimo_interp.evaluation import MathVerifyScorer, evaluate_batch
from aimo_interp.model import solve_batch


class BatchInputs(dict):
    def to(self, device):
        # Keep these synthetic inputs on CPU while exercising the GPU code path.
        assert device == "cuda:0"
        return self


class Tokenizer:
    padding_side = "right"
    pad_token = "<pad>"
    pad_token_id = 0

    def apply_chat_template(self, messages, **kwargs):
        return messages[0]["content"]

    def __call__(self, prompts, **kwargs):
        assert self.padding_side == "left"
        assert kwargs["padding"] is True
        assert len(prompts) == 3
        return BatchInputs(
            input_ids=torch.tensor([[0, 11], [11, 12], [0, 13]]),
            attention_mask=torch.tensor([[0, 1], [1, 1], [0, 1]]),
        )

    def decode(self, sequence, **kwargs):
        return str(sequence)


class FixedBatchTests(unittest.TestCase):
    def test_left_padding_and_individual_eos_accounting(self):
        model = Mock()
        model.generation_config = SimpleNamespace(eos_token_id=[99, 100])
        model.generate.return_value = torch.tensor([
            [0, 11, 5, 99, 0],    # Completed early; trailing padding isn't output.
            [11, 12, 6, 7, 100],  # EOS exactly at the token cap is completion.
            [0, 13, 8, 9, 10],    # No EOS: this row hit the cap.
        ])
        tokenizer = Tokenizer()
        with (
            patch("aimo_interp.model.torch.cuda.reset_peak_memory_stats"),
            patch("aimo_interp.model.torch.cuda.synchronize"),
            patch("aimo_interp.model.torch.cuda.max_memory_allocated", return_value=2**30),
            patch("aimo_interp.model.time.perf_counter", side_effect=[10, 12]),
        ):
            results = solve_batch(["a", "bb", "c"], 3, model=model, tokenizer=tokenizer)
        model.generate.assert_called_once()
        self.assertEqual(tokenizer.padding_side, "right")
        self.assertEqual([r["generated_tokens"] for r in results], [2, 3, 3])
        self.assertEqual([r["hit_token_limit"] for r in results], [False, False, True])
        self.assertEqual([r["response"] for r in results], ["[5, 99]", "[6, 7, 100]", "[8, 9, 10]"])
        self.assertTrue(all(r["batch_tokens_per_second"] == 4 for r in results))
        self.assertTrue(all(r["elapsed_seconds"] == 2 for r in results))

    def test_each_response_uses_its_own_reference_and_final_section(self):
        responses = [
            {"response": r"reasoning \boxed{9}</think>\boxed{4}"},
            {"response": r"reasoning</think>\boxed{9}"},
            {"response": r"unfinished thinking \boxed{4}"},
        ]
        with patch("aimo_interp.evaluation.solve_batch", return_value=responses):
            results = evaluate_batch(
                ["a", "b", "c"], "box the answer", None,
                [MathVerifyScorer(4), MathVerifyScorer(9), MathVerifyScorer(4)],
                tokenizer=None,
            )
        self.assertEqual([r["is_correct"] for r in results], [True, True, False])
        self.assertEqual(results[2]["final_response"], "")

    def test_empty_and_mismatched_batches(self):
        self.assertEqual(solve_batch([], model=None, tokenizer=None), [])
        with self.assertRaises(ValueError):
            evaluate_batch(["a"], "", None, [], tokenizer=None)


if __name__ == "__main__":
    unittest.main()
