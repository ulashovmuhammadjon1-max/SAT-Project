"""Balance the EXPORTED answer spread of an AP Psychology module.

Why this exists
---------------
`export_units.py` disperses keys with a per-topic deterministic shuffle, and
`README.md` says the raw `ans` index in a module is therefore not worth
balancing by hand. That is true for a 50-question economics topic, where the
noise averages out. It is not true for a 25-question topic with four choices:
topic 4.1's first export came out **48% "C"** purely from the seed. A student
who always guesses C would score half of that topic.

The exporter cannot be edited, but it does not need to be. Its shuffle does not
depend on the key:

    order = [0, 1, 2, 3]; rng.shuffle(order); ans_out = order.index(ans_in)

`order` is a permutation, so as `ans_in` ranges over 0..3, `ans_out` ranges over
all four letters. For each question we can therefore SOLVE for the source index
that produces the letter we want:

    ans_out == d   <=>   ans_in == order[d]

This script replays the exporter's rng stream, picks a balanced target letter
for each question, and rewrites the module so the choices are rotated to put the
key at the required source index. Rotation preserves the relative order of the
distractors, so no question's reading changes -- only which slot the key sits in.

Usage:  python3 balance_psych_keys.py p4_1.py p4_2.py
Then re-run the module's verifier and the exporter.
"""
import importlib
import random
import re
import sys

from export_units import numeric_ladder


def target_letters(n, n_choices=4):
    """A round-robin of target indices, so counts differ by at most one."""
    return [i % n_choices for i in range(n)]


def balance(fn):
    mod_name = fn[:-3] if fn.endswith(".py") else fn
    m = importlib.import_module(mod_name)
    code = m.TOPIC[0]
    qs = m.QUESTIONS

    # Replay export_units.py's rng stream exactly, including the fact that a
    # numeric ladder is left unshuffled and so never draws from the stream.
    rng = random.Random(int(code.replace(".", "")) * 7919)
    wanted = target_letters(len(qs))
    source_index = []
    for item, want in zip(qs, wanted):
        if numeric_ladder(item["choices"]):
            source_index.append(None)          # not shuffled; leave it alone
            continue
        order = list(range(len(item["choices"])))
        rng.shuffle(order)
        source_index.append(order[want])       # ans_out == want  <=>  ans_in == order[want]

    src = open(fn).read()
    parts = src.split("\n dict(q=")
    head, items = parts[0], parts[1:]
    assert len(items) == len(qs), f"{fn}: parsed {len(items)} items, module has {len(qs)}"

    out = []
    for item, q, tgt in zip(items, qs, source_index):
        mm = re.search(r"choices=\[\n(.*?)\], ans=(\d+)", item, re.S)
        assert mm, f"{fn}: could not parse a choices block"
        chs = re.findall(r'"((?:[^"\\]|\\.)*)"', mm.group(1))
        ans = int(mm.group(2))
        assert chs == q["choices"] and ans == q["ans"], f"{fn}: source/module mismatch"
        if tgt is None or tgt == ans:
            out.append(item)
            continue
        shift = (tgt - ans) % len(chs)
        new = chs[-shift:] + chs[:-shift]
        assert new[tgt] == chs[ans], f"{fn}: rotation lost the key"
        body = "\n".join('   "%s",' % c for c in new)[:-1]
        item = (item[:mm.start(1)] + body + "\n"
                + item[mm.end(1):mm.start(2)] + str(tgt) + item[mm.end(2):])
        out.append(item)

    open(fn, "w").write(head + "\n dict(q=" + "\n dict(q=".join(out))
    print(f"balanced {fn} -> targets {sorted(set(wanted))}, "
          f"{len(qs)} questions rewritten to hit a round-robin export spread")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        balance(f)
