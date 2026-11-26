#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun entry.

One word for the Wi-Fi: it wheezes, it drops, it gasps back to life
every few minutes. The most honest diagnosis a network ever got.

One word has to carry the whole complaint: the wheezing, the dropping, the gasping back to life.

The program writes that one word to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). A command-line argument may
name the directory instead, but the grader passes none.
"""

import os
import sys

from pathlib import Path

DIAGNOSIS = "Asthmatic"


def main(argv):
    # One word only, nothing attached; gate is 1-20 characters.
    if len(DIAGNOSIS.split()) != 1 or not 1 <= len(DIAGNOSIS) <= 20:
        print("entry must be exactly one word, got %r" % DIAGNOSIS,
              file=sys.stderr)
        return 1
    out_dir = argv[1] if len(argv) > 1 else (
        os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with open(Path(out_dir) / "entry.txt", "w",
              encoding="utf-8", newline="\n") as handle:
        handle.write(DIAGNOSIS + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
