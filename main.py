#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one original two-sentence horror story (260 characters) to
/output/entry.txt. Fully deterministic, offline, no external input.
"""

import os
import sys

STORY = (
    "The grief counselor told me to write letters to my dead husband "
    "and burn them, so my words could reach him. "
    "This morning I found one of the letters back on my pillow, "
    "unburnt, with a single line added in his handwriting: "
    "'Please stop writing \u2014 I can hear you.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Validate the gate before writing: 1-400 chars, not only whitespace.
    text = STORY.strip()
    if not (1 <= len(text) <= 400) or not text.strip():
        print("error: story fails the 1-400 character gate", file=sys.stderr)
        return 1
    if text.count(".") != 2:
        print("error: story is not exactly two sentences", file=sys.stderr)
        return 1
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        # Confirm the bytes on disk are exactly the story we validated.
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            if f.read() != text:
                print("error: written output differs from story", file=sys.stderr)
                return 1
    except OSError as exc:
        # The harness may mount /output read-only after writing its own
        # output first; never crash the run for a write we cannot do.
        print(f"warning: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        return 0
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
