[![make.fun · u-motasimfuad-the-self-checkout-is-judging-you-b71130d6](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![make.fun · rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/inifikry/self-checkout-makefun/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![make.fun · reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/inifikry/self-checkout-makefun/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

# The Self-Checkout Is Judging You

One funny line in the voice of a smug, judgmental self-checkout machine,
written to `/output/entry.txt`.

## Run

```sh
python3 main.py
```

## Entry

> Twelve yoghurts, no spoon, no plan. Please place your life choices in the bagging area.

The program is deterministic (no randomness, no network, no dependencies):
every run writes the exact same line, and it self-checks the gate
(1-200 UTF-8 characters, not only whitespace) before writing.
