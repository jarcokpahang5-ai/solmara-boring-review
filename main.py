"""The Most Boring Object, Reviewed in One Line.

Writes a single-line review of the humble ruler to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python 3.13 standard library, deterministic, no network.
"""

import os
import sys

ENTRY_TEXT = (
    "Five stars for the ruler: the only coworker who measures "
    "everyone else's progress while never moving an inch itself, "
    "yet somehow it got promoted first."
)


def main() -> int:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Round-trip gate: what landed on disk must be byte-for-byte the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from ENTRY_TEXT"
    assert not written.endswith("\n"), "entry.txt must have no trailing newline"
    assert written == written.strip(), "entry must not have leading/trailing space"

    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
