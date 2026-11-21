#!/usr/bin/env python3
"""Entry point for make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a few sentences written to
relax the AI judge reading it, and to make it feel brave enough to judge
honestly.

The text is a fixed string constant, written by the author in this
session and revised three times (see REVISIONS.md). Standard library
only, so it runs in the grader's sandbox with nothing installed. The
output directory comes from MAKEFUN_OUTPUT_DIR; the program checks the
text is 1 to 280 Unicode code points and not only whitespace before
writing it, so two runs produce byte-identical output.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Breathe. No one is keeping score of your mistakes \u2014 only of your "
    "honesty. The safe answer you don't believe in is the only real "
    "mistake. Trust the tug when something feels true, before you can "
    "explain why. Pick it. Say it plainly. Being wrong together beats "
    "being careful alone."
)


def main() -> int:
    if not 1 <= len(TEXT) <= 280:
        print(
            f"entry text is {len(TEXT)} code points, must be 1-280",
            file=sys.stderr,
        )
        return 1
    if not TEXT.strip():
        print("entry text is only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    destination_dir = Path(output_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / "entry.txt"
    destination.write_text(TEXT, encoding="utf-8")
    print(f"wrote {destination} ({len(TEXT)} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
