#!/usr/bin/env python3
"""Select half the training rows, balancing model/label/effort counts by problem."""

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "train-main-v2"
SEED = 42


def main() -> None:
    source = DATA_DIR / "data" / "train-00000-of-00001.parquet"
    frame = pd.read_parquet(source)
    # One binary decision per exact problem statement keeps model repetitions together.
    groups, problems = pd.factorize(frame["problem"], sort=False)
    group_count = len(problems)
    labels = frame["is_robust"].map({True: "robust", False: "non_robust"}).fillna("unlabeled")
    strata = frame["model_id"] + "|" + labels

    def counts(keys):
        return pd.crosstab(keys, groups).reindex(columns=range(group_count), fill_value=0).to_numpy()

    model_labels = counts(strata)
    effort_labels = counts(strata + "|" + frame["reasoning_effort"])
    model_counts = counts(frame["model_id"])
    balance = np.vstack([model_labels, effort_labels])
    target = balance.sum(axis=1) / 2
    deviations = len(target)
    # Minimize absolute deviations from half each stratum. Prioritize model/label
    # balance over effort balance; tiny seeded costs break otherwise equivalent ties.
    costs = np.r_[
        np.random.default_rng(SEED).uniform(0, 1e-7, group_count),
        np.full(len(model_labels), 2.0), np.ones(len(effort_labels)),
    ]
    model_targets = model_counts.sum(axis=1) / 2
    constraints = [
        LinearConstraint(np.c_[balance, -np.eye(deviations)], -np.inf, target),
        LinearConstraint(np.c_[-balance, -np.eye(deviations)], -np.inf, -target),
        LinearConstraint(
            np.r_[np.bincount(groups), np.zeros(deviations)][None, :],
            len(frame) // 2, len(frame) // 2,
        ),
        LinearConstraint(
            np.c_[model_counts, np.zeros((len(model_counts), deviations))],
            np.floor(model_targets), np.ceil(model_targets),
        ),
    ]
    result = milp(
        costs,
        integrality=np.r_[np.ones(group_count), np.zeros(deviations)],
        bounds=Bounds(np.zeros(group_count + deviations), np.r_[np.ones(group_count), np.full(deviations, np.inf)]),
        constraints=constraints,
    )
    if not result.success:
        raise RuntimeError(f"Could not construct the grouped split: {result.message}")
    selected = (result.x[:group_count] > 0.5)[groups]
    allowed = frame.loc[selected]
    assert len(allowed) == len(frame) // 2
    assert set(allowed["problem"]).isdisjoint(frame.loc[~selected, "problem"])
    destination = DATA_DIR / "train_allowed.parquet"
    allowed.to_parquet(destination, index=False)
    metadata = {
        **json.loads((DATA_DIR / "metadata.json").read_text()),
        "source_file": str(source.relative_to(DATA_DIR)),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "method": "Exact half by rows; group identical problems; minimize model/label/effort deviations",
        "seed": SEED,
        "source_rows": len(frame),
        "selected_rows": len(allowed),
        "selected_problem_count": allowed["problem"].nunique(),
        "selected_source_row_positions": np.flatnonzero(selected).tolist(),
    }
    destination.with_suffix(".metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    summary = pd.crosstab(frame["model_id"], labels).join(
        pd.crosstab(allowed["model_id"], labels.loc[selected]),
        lsuffix="_full", rsuffix="_allowed",
    ).fillna(0).astype(int)
    print(summary.to_string())
    print(f"Saved {len(allowed)}/{len(frame)} rows to {destination}")


if __name__ == "__main__":
    main()
