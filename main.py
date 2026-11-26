#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Writes one funny line in the voice of a smug, judgmental self-checkout
machine to /output/entry.txt. No external dependencies.
"""

import os

LINE = "Twelve yoghurts, no spoon, no plan. Please place your life choices in the bagging area."

def main() -> None:
    # Gate self-check: 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
