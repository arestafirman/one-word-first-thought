#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Word: syzygy
Meaning: the alignment of three celestial bodies in a straight line
(e.g. Sun, Earth, Moon during an eclipse).

Why this word:
- Surprising: spelled with three y's and no ordinary vowel — it looks
  strange before you even know what it means.
- Vivid and specific: one exact astronomical picture, not a vague feeling.
- Wit and sound: the "z" and the repeated y's make it buzz on the tongue;
  a tiny word about a cosmic alignment.
- Feels chosen: six letters, precise, and impossible to mistake for a
  safe or generic answer. It also dodges every trap word on the banned
  list — no petrichor, no serendipity, no love, no light.
"""

import os

WORD = "syzygy"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
