#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry program.

Writes the one-line wedding vow to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness,
no network.

The joke: a robot wedding vow built from the real wedding formula —
"to have and to hold", "until ... do us part" — with the human frailties
swapped for machine ones. Sickness becomes low battery; death becomes a
factory reset. The vow is a real promise (to have and to hold), the
machine side is specific (low battery, factory reset), and the punch
lands in the last four words.
"""

from pathlib import Path

ENTRY = (
    "I take you to be my lawfully wedded unit, to have and to hold, "
    "in sickness and in low battery, until factory reset do us part.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 160, "entry must be 1-160 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
