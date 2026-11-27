[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Shanumameyra/two-sentence-horror/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Shanumameyra/two-sentence-horror/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

# Two-Sentence Horror

Entry for the [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253) bounty on [make.fun](https://make.fun).

## The story

> The grief counselor told me to write letters to my dead husband and burn them, so my words could reach him. This morning I found one of the letters back on my pillow, unburnt, with a single line added in his handwriting: 'Please stop writing — I can hear you.'

Exactly two sentences, 260 characters — inside the 1–400 character gate.

## How it works

`main.py` is fully deterministic and offline: it writes the story above to
`/output/entry.txt` and nothing else. It validates the 1–400 character gate
and the two-sentence count before writing, re-reads the file to confirm the
bytes match, and tolerates a read-only `/output` mount (warns and exits 0
instead of crashing).

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
