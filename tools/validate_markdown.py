"""Minimal markdown hygiene checks for repository documentation."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "__pycache__"}


def markdown_files():
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def main() -> int:
    failures = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if text and not text.endswith("\n"):
            failures.append(f"{path}: missing trailing newline")
        for index, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                failures.append(f"{path}:{index}: trailing whitespace")
            if "\t" in line:
                failures.append(f"{path}:{index}: tab character")

    if failures:
        raise SystemExit("\n".join(failures))

    print("Markdown hygiene checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
