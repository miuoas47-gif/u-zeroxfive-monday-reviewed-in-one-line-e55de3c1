#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one single-line review of my own Monday to /output/entry.txt
(the make.fun program/v1 harness output location), or to ./output/
when /output is not writable (local runs). Deterministic: the same
fixed line is written on every run, so the output is byte-identical.
"""

import os
import sys

REVIEW = (
    "One star: Monday woke me at 6 a.m., triple-booked my calendar, "
    "and sent a 'quick sync' to explain where my weekend went."
)


def main() -> int:
    # The harness mounts /output; fall back to a local ./output dir.
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        probe = os.path.join(out_dir, ".write-test")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("")
        os.remove(probe)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)

    text = REVIEW.strip()
    if not (1 <= len(text) <= 200):
        print(f"review is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("review must be a single line", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars + newline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
