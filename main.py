#!/usr/bin/env python3
"""The 3AM Fridge Text — writes one funny line to /output/entry.txt.

Stdlib only, deterministic.
"""

import os

LINE = "I lit up for nobody four times tonight. I'm not a nightlight, I'm a stage, and you're bombing."


def main():
    # Validate against the sealed scorer's gate before writing: the entry
    # must be 1-140 characters of UTF-8 text, not only whitespace, and a
    # single line, or it scores 0 and never reaches the judge.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: the gate reads /output/entry.txt, so confirm the
    # file on disk is byte-identical to the line, with no trailing newline.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the line byte for byte")
    print(LINE)


if __name__ == "__main__":
    main()
