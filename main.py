#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep is
fixed, to /output/entry.txt (the file the judge reads).
"""

import os

ENTRY = (
    "Fixed: falling asleep no longer requires 45 minutes of "
    "ceiling-staring and one (1) existential crisis. "
    "Sleep now installs in 8 minutes, no restart required."
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
