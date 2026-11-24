"""One Line, One Chill: writes the entry text to /output/entry.txt.

Why this line: Horror in one breath: a concrete image (baby monitor, 3 a.m.), dread that outlasts the line, and the last words land the blow. No mirror/doll/basement cliche.
"""

import os

ENTRY = "The baby monitor has been off for a week, but every night at 3 a.m. it whispers my name in my daughter's voice — and my daughter moved out in 2019."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
