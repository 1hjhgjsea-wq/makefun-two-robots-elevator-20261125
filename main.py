#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one funny line, under 200 characters, of awkward small talk
a robot says to another robot in an elevator, to entry.txt.
Deterministic: the same line every run, no randomness, no network.
"""

import os
import sys

LINE = (
    "So\u2026 do you come here often? I ask every elevator. "
    "Statistically, one of them has to say yes eventually."
)


def validate(line: str) -> None:
    """Enforce the competition gate: 1 to 200 chars, not only whitespace."""
    if not line or len(line) > 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
