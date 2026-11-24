#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

The entry program for u-gentle-badger-68-make-the-judge-smile-9228676d.
It writes a single line of at most 200 characters to /output/entry.txt,
where a sealed scorer gates it (UTF-8, 1-200 chars, not only white space)
and a judge model then compares it pairwise against the other entries.

What the judge weighs, most important first: the line is about a small
good thing that happened today; warmth — a kindness that lands as genuinely
felt; surprise — a turn where it is least expected; concreteness — one real
small detail, a name, a sound, a time of day; fresh wording — its own
rhythm, no greeting-card phrasing.

The line below is built to hit all five: a concrete morning scene (the
warung, the krupuk, the whispered "for the road"), a small kindness freely
given, and a closing turn that carries the feeling forward instead of
reporting it flat.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Return the entry line: one warm, surprising, concrete sentence."""
    return (
        "This morning the warung lady slipped an extra krupuk into my bag "
        "and whispered, 'for the road' — and I carried her kindness all "
        "the way to work."
    )


def validate(line: str) -> None:
    """Fail loudly if the line would fail the sealed gate scorer."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} cap"
        )
    line.encode("utf-8")  # the gate requires UTF-8 text


def main() -> None:
    line = build_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
