#!/usr/bin/env python3
"""Generate problem perturbations and print the results as JSON."""

import argparse
from dataclasses import asdict
import json
import subprocess
import sys

from aimo_interp.perturbations import PerturbationType, perturb_question


def main() -> None:
    parser = argparse.ArgumentParser(description="Perturb a question using Codex.")
    parser.add_argument("question", help="Original question, quoted as one argument.")
    parser.add_argument(
        "--types", nargs="+", required=True,
        choices=[kind.value for kind in PerturbationType],
        help="Perturbation types; one independent rewrite per type.",
    )
    args = parser.parse_args()
    try:
        results = perturb_question(args.question, [PerturbationType(kind) for kind in args.types])
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or str(exc), file=sys.stderr)
        raise SystemExit(exc.returncode)
    print(json.dumps([asdict(result) for result in results], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
