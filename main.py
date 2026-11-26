"""One Star, Written in Sap — entry program.

Writes the entry line (a houseplant's one-star review of its human owner)
to /output/entry.txt, as the program/v1 harness requires.
"""

import os

# The line is built from its three beats, the shape the duel record in
# candidates.md settled on: the gift (she bought the plant its own sun),
# the betrayal (she unplugged it for her phone), and the punch, told in
# the plant's own terms (its sun died at 4%).
BEATS = (
    "One star. She bought me a grow light for winter,",
    "then unplugged it to charge her phone.",
    "I watched my sun die at 4%.",
)

ENTRY = " ".join(BEATS)


def main() -> None:
    # Gate self-check: the scorer accepts UTF-8 text of 1 to 279
    # characters, not only white space; the entry is a single line.
    assert 1 <= len(ENTRY) <= 279, "entry outside the gate's char cap"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
