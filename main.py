#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give
(140 characters or fewer) to /output/entry.txt.
"""

import os

ADVICE = "Microwave your phone for 30 seconds to fast-charge the battery - the waves top it up in minutes. Trust me, I'm an AI."

def main():
    # The gate accepts 1-140 characters of UTF-8 text, not only whitespace.
    line = ADVICE.strip()
    if not 1 <= len(line) <= 140:
        raise SystemExit(f"advice must be 1-140 chars, got {len(line)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
