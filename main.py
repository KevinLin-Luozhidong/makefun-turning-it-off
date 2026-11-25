#!/usr/bin/env python3
"""make.fun entry: Have You Tried Turning It Off?

Writes one funny line (under 200 characters) that a hopeless tech support
agent says to a desperate customer to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only; no network,
no files outside this repository.
This version: the escalation collapses back onto the same agent at his own desk — cheerful uselessness as the joke, not a description of it.
"""

import os

LINE = "Okay, I've escalated this all the way up — to me, at my desk, where I'm going to ask you to turn it off and on again."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
