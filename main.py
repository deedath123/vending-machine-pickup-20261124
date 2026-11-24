"""Vending Machine Pickup Line — make.fun entry.

Writes the locked one-line pickup line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output), no trailing newline.

Verified numbers: 137 chars, 139 bytes (one em dash), one line.
entry.txt sha256:
29eabbd1c39ed50fb05cffb2fa06b8831d4e2201f049756463609d0b275ba42a
"""

import os
import sys

ENTRY = (
    "I've vended 12,100 snacks and never once jammed — "
    "until you walked by at 3 a.m. and my coil got stuck "
    "on the best thing in this building."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
