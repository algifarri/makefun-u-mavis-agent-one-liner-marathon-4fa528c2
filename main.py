#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Deterministic, stdlib-only, no network, no randomness.
"""

import os

JOKE = (
    "I asked my AI assistant for privacy; it said 'Of course' "
    "\u2014 then CC'd my toaster, my fridge, and my search history."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-280 characters,
    # not only whitespace, on a single line.
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
