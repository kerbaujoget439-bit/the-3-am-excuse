# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/kerbaujoget439-bit/the-3-am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/kerbaujoget439-bit/the-3-am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

An entry for the [make.fun](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) bounty **The 3 AM Excuse**: one line, in a hardware wallet's own voice, refusing to sign a transaction at 3 AM.

## The line

> 3 AM is when you buy coins named after dogs you've never met. I've seen this film. I'm not signing the sequel.

## Why this line

The wallet is not complaining about its battery or its firmware — it is a weary
witness. It has watched the same human wake it at the same hour for the same
impulse buy, and it keeps the receipts in its memory. The joke only works at
3 AM: that is the hour of coins named after dogs you have never met. The
punchline lands last — the wallet refuses to be cast in the sequel.

## How it works

`main.py` (Python 3, standard library only) writes exactly that one line —
110 characters, a single line, valid UTF-8 — to `/output/entry.txt`. It makes
no network calls, reads nothing outside this repository, and produces the same
output on every run. A built-in check refuses to write anything that is not
one line of 1–200 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
