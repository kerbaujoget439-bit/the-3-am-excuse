#!/usr/bin/env python3
"""The 3 AM Excuse.

A hardware wallet explains why it will not sign a transaction at 3 AM.
Writes exactly one line to /output/entry.txt.
"""

import os

ENTRY = (
    "At 3 AM your finger shakes, your eyes don't focus, and my screen is "
    "the only sober thing in this room. I refuse to be your accomplice."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
