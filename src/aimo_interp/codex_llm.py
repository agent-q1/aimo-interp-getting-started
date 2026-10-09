"""One-prompt Codex calls using the installed, authenticated Codex CLI."""

import subprocess
import tempfile
from pathlib import Path


def llm(prompt: str) -> str:
    """Start a fresh Codex turn and return its final response as text."""
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "response.txt"
        subprocess.run(
            [
                "codex", "exec",
                "--skip-git-repo-check",
                "--sandbox", "read-only",
                "--ephemeral",
                "--output-last-message", str(output),
                "-",
            ],
            input=prompt,
            cwd=tmp,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return output.read_text(encoding="utf-8").strip()
