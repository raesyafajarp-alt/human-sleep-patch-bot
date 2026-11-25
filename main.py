#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep is
fixed, to /output/entry.txt (the file the judge reads).
"""

import os

ENTRY = (
    "Fixed: falling asleep no longer hangs at 99% while your brain "
    "replays every embarrassing thing you said in 2011."
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
