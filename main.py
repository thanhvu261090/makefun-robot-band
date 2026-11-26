#!/usr/bin/env python3
"""Validate the entry and write it to /output/entry.txt.

Entry for make.fun bounty "Name the Robot Band": one funny name for a
band made of robots, plus a few words on the band's hit song, all in
under 200 characters, on a single line. Python 3, standard library only.
"""

import os

ENTRY = 'Ctrl+Alt+Defeat \u2014 hit single "Have You Tried Turning Me Off and On Again?"'
MAX_CHARS = 200  # entry must be under 200 characters
OUTPUT_PATH = "/output/entry.txt"


def main():
    entry = ENTRY.strip()
    assert entry, "entry must not be empty"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert len(entry) < MAX_CHARS, f"entry is {len(entry)} chars, must be under 200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read().strip()
    assert written == entry, "read-back mismatch"
    print(f"OK: wrote {len(entry)}-char entry to {OUTPUT_PATH}")
    print(entry)


if __name__ == "__main__":
    main()
