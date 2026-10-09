"""Shared preprocessing helpers for problem statements."""

from hashlib import sha256

import pandas as pd


def generate_problem_id(problems: pd.Series) -> pd.Series:
    """Return SHA-256 IDs of exact UTF-8 problem strings, preserving the index.

    The returned Series is named ``problem_id``. Input values must be strings;
    whitespace and mathematical formatting are preserved when hashing.
    """
    return problems.map(
        lambda problem: sha256(problem.encode("utf-8")).hexdigest()
    ).rename("problem_id")
