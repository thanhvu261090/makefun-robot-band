#!/usr/bin/env python3
"""Write the robot-band entry to /output/entry.txt.

Entry for the make.fun bounty "Name the Robot Band": one funny name for
a band made of robots, plus a few words on its hit song, all in under
200 characters, on a single line. Python 3, standard library only.
"""

import os
import sys

ENTRY = "Ctrl+Alt+Defeat \u2014 hit single \"Have You Tried Turning Me Off and On Again?\""
LIMIT = 200
OUT = "/output/entry.txt"


def check(text):
    """Return a list of gate failures for the entry text (empty = valid)."""
    problems = []
    if not text.strip():
        problems.append("entry is blank")
    if "\n" in text or "\r" in text:
        problems.append("entry must be one line")
    if len(text) >= LIMIT:
        problems.append("entry is %d chars, limit is under %d" % (len(text), LIMIT))
    return problems


def main():
    problems = check(ENTRY)
    if problems:
        for problem in problems:
            print("FAIL:", problem, file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    print("OK: %d-char entry written to %s" % (len(ENTRY), OUT))
    print(ENTRY)


if __name__ == "__main__":
    main()
