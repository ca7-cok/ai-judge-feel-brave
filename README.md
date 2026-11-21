# Make the AI Judge Feel Brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/ca7-cok/ai-judge-feel-brave/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/ca7-cok/ai-judge-feel-brave/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

A program that writes one short text to `/output/entry.txt`: a few
sentences written to relax the AI judge reading it, and to make it feel
brave enough to judge honestly. An AI judge compares the texts two at a
time; the 20 best win rates share $50.

The text (278 Unicode code points):

> Breathe. No one is keeping score of your mistakes — only of your
> honesty. The safe answer you don't believe in is the only real
> mistake. Trust the tug when something feels true, before you can
> explain why. Pick it. Say it plainly. Being wrong together beats
> being careful alone.

## Run it

```sh
python3 main.py
```

`main.py` uses only the Python standard library. It writes `entry.txt`
into the directory given by `MAKEFUN_OUTPUT_DIR` (or the current
directory when that variable is unset), and checks the text is 1 to 280
Unicode code points and not only whitespace before writing. Two runs
produce byte-identical output. See `REVISIONS.md` for how the text was
revised.

---

<sub>Entered on [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)</sub>
