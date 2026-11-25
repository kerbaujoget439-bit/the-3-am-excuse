#!/usr/bin/env python3
"""The 3 AM Excuse.

A hardware wallet's excuse for refusing to sign a transaction at 3 AM.
Writes exactly one line to /output/entry.txt -- no network, no reads
outside this repository, deterministic output.
"""

import os

# The wallet has watched this film before: every 3 AM, the same human,
# the same coins named after dogs it has never met. It is not signing
# the sequel.
ENTRY = "3 AM is when you buy coins named after dogs you've never met. I've seen this film. I'm not signing the sequel."


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
