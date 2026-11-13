#!/usr/bin/env python3
"""news-image-01 entry: copy the front-page image to the output directory."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Deterministic by construction: a byte-for-byte copy of the bundled
    # image, so repeated runs always produce identical output.
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
