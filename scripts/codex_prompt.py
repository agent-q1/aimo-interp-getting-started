#!/usr/bin/env python3
"""Send one prompt: uv run scripts/codex_prompt.py "Your prompt here"."""

import argparse
import subprocess
import sys

from aimo_interp.codex_llm import llm


def main() -> None:
    parser = argparse.ArgumentParser(description="Send one prompt to Codex and print its final response.")
    parser.add_argument("prompt", help="Prompt text, quoted as one argument.")
    args = parser.parse_args()
    try:
        print(llm(args.prompt))
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or str(exc), file=sys.stderr)
        raise SystemExit(exc.returncode)


if __name__ == "__main__":
    main()
