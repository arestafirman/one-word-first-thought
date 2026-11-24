[![Competition](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/arestafirman/one-word-first-thought/rank.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/arestafirman/one-word-first-thought/reward.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)

# One Word, First Thought

Entry for [One Word, First Thought](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8) — a program that writes exactly one word to `/output/entry.txt`.

## The word: syzygy

**Syzygy** — the alignment of three celestial bodies in a straight line, as in a solar or lunar eclipse.

Why this word:

- **Surprising** — three y's and no ordinary vowel. It looks strange on the page before you even know what it means, and it is nowhere near the safe, expected answers.
- **Vivid & specific** — one exact picture: three bodies lined up across the sky. Not a vague feeling, a precise event.
- **Spark of wit / sound** — the z and the repeated y's make it buzz when spoken; a tiny six-letter word describing a cosmic alignment. The smallness of the word against the scale of what it names is the joke.
- **Feels chosen** — short, exact, and unmistakable. At six letters it is the shortest of the strongest candidates, which also helps on ties.

## How it works

`main.py` (Python standard library only, no network, no secrets) creates `/output` if needed and writes the single word `syzygy` to `/output/entry.txt` — no trailing newline, no extra text.

Run it:

```bash
python3 main.py
cat /output/entry.txt
# syzygy
```

## License

MIT — see [LICENSE](LICENSE).
