#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings, at most 200
characters. Writes the line verbatim to entry.txt.

The joke personifies the Monday alarm as a negotiator: it rings, the
sleeper bargains, and both sides lose — which is exactly how every Monday
morning feels. The judge scores laughs, so the line is built as a tiny
three-beat scene (agreement, ring, negotiation) with the punchline in the
last three words, and the loser is everybody, which is the universal part.
"""

import os
from pathlib import Path

LINE = "My Monday alarm and I have an agreement: it rings, I negotiate, we both lose."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
