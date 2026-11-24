#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes a single-line review of Monday to entry.txt. No arguments,
deterministic, exits 0. The gate self-check mirrors the house gate:
1-200 UTF-8 characters, not only whitespace, exactly one line.
"""
import os
import sys

LINE = "Monday: one star. My alarm snoozed itself, my coffee filed for overtime, and my to-do list unionised before 9am."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate self-check: 1-200 chars, non-whitespace, single line, no newline.
    text = LINE
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    text.encode("utf-8")  # must be valid UTF-8
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    # Verify what was actually written: read it back and re-run the gate
    # on the file contents, so a disk/encoding surprise cannot slip through.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "written file differs from the review line"
    assert 1 <= len(written) <= 200 and written.strip(), "written file fails gate"
    assert "\n" not in written and "\r" not in written, "written file is not one line"
    return 0


if __name__ == "__main__":
    sys.exit(main())
