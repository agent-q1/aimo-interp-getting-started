#!/usr/bin/env python3
"""Download the pinned training dataset into the local data directory."""

import json
import os
from pathlib import Path

DATASET = "aimo-interp/train-main-v2"
REVISION = "23791d9b120132087877b0459f953d5959fc8455"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "train-main-v2"

if __name__ == "__main__":
    os.environ.setdefault("HF_HOME", str(OUTPUT_DIR.parent / "huggingface"))
    from huggingface_hub import snapshot_download

    snapshot_download(
        repo_id=DATASET,
        repo_type="dataset",
        revision=REVISION,
        allow_patterns=["README.md", "data/*.parquet"],
        local_dir=OUTPUT_DIR,
    )
    (OUTPUT_DIR / "metadata.json").write_text(
        json.dumps({"dataset": DATASET, "revision": REVISION}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Downloaded {DATASET}@{REVISION} to {OUTPUT_DIR}")
