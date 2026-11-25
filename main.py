#!/usr/bin/env python3
"""make.fun entry: Have You Tried Turning It Off?

Writes one funny line (under 200 characters) that a hopeless tech support
agent says to a desperate customer to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only; no network,
no files outside this repository.
"""

import os

LINE = "Let us turn it off and on again, and if that does not work I will transfer you to someone who will ask you to do the exact same thing."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
