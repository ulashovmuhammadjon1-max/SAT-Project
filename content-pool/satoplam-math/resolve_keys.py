# -*- coding: utf-8 -*-
"""Resolve the disputed Math keys from two independent readings.

    python3 resolve_keys.py [--write]

Only one outcome changes a key: both readings, taken without sight of each
other or of the book, reaching the same answer against it. Everything else is
either the first reader being the outlier, or a question no one can settle —
and a question three readings cannot settle is one for a human, not a coin
toss.
"""
import json, glob, os, re, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
disputes = {r["id"]: r for r in json.load(open(f"{HERE}/disputes.json"))}
contaminated = set(json.load(open(f"{HERE}/contaminated.json"))["ids"])

adj = {}
for f in sorted(glob.glob(f"{HERE}/adj/adj-*.jsonl")):
    for line in open(f):
        if line.strip():
            try:
                e = json.loads(line); adj[e["id"]] = e
            except Exception: pass


def num(s):
    if s is None: return None
    t = str(s).strip().replace(",", "").replace("−", "-")
    try: return Fraction(t) if "/" in t else Fraction(str(float(t)))
    except Exception: return None


def same(a, b):
    """Equal as answers, not as strings.

    One reader writes 117.44 where the other writes 1057/9. Those are the same
    answer — a student gridding either would be marked right — and treating
    them as a disagreement invented an 'unsettled' verdict out of two readers
    who in fact agreed exactly. Rounding is allowed only between two numbers,
    and only to a few decimal places, so 'C' can never round into 'D'.
    """
    if a is None or b is None: return False
    if str(a).strip().upper() == str(b).strip().upper(): return True
    x, y = num(a), num(b)
    if x is None or y is None: return False
    if x == y: return True
    return abs(float(x) - float(y)) <= 0.005 * max(1.0, abs(float(y)))


flip, keep, split, broken, missing, held = [], [], [], [], [], []
for qid, d in disputes.items():
    a = adj.get(qid)
    if not a: missing.append(d); continue
    if qid in contaminated: held.append((d, a)); continue
    first = d.get("answerLabel") or d.get("answerValue")
    second = a.get("answerLabel") or a.get("answerValue")
    key = d.get("printed_key")
    # An adjudicator who declines to answer is reporting a broken question,
    # not casting a vote.
    if second in (None, "", "none", "NONE") or (a.get("note") and not second):
        broken.append((d, a)); continue
    if same(first, second) and not same(second, key): flip.append((d, a))
    elif same(second, key): keep.append((d, a))
    else: split.append((d, a))

print(f"disputed {len(disputes)}")
print(f"  KEY WRONG — both readings agree against the book : {len(flip)}")
print(f"  key stands — adjudicator matched the book        : {len(keep)}")
print(f"  unsettled — three readings, no majority          : {len(split)}")
print(f"  adjudicator calls the question broken            : {len(broken)}")
print(f"  held: reading was contaminated, needs a 3rd pass : {len(held)}")
print(f"  no adjudication found                            : {len(missing)}")
print(f"\ndispute rate {len(disputes)}/1084 = {100*len(disputes)/1084:.1f}%; "
      f"of those, {100*len(flip)/max(len(disputes),1):.0f}% are confirmed wrong keys")

for title, rows in (("UNSETTLED", split), ("BROKEN", broken)):
    print(f"\n{title}:")
    for d, a in rows[:14]:
        print(f"  {d['id'][:44]:<44} book {str(d.get('printed_key'))[:8]:<8} "
              f"1st {str(d.get('answerLabel') or d.get('answerValue'))[:8]:<8} "
              f"2nd {str(a.get('answerLabel') or a.get('answerValue'))[:8]}")

if "--write" in sys.argv:
    out = {"flip": [{"id": d["id"], "from": d.get("printed_key"),
                     "to": a.get("answerLabel") or a.get("answerValue"),
                     "confidence": a.get("confidence")} for d, a in flip],
           "keep": [d["id"] for d, _ in keep],
           "unsettled": [{"id": d["id"], "book": d.get("printed_key"),
                          "first": d.get("answerLabel") or d.get("answerValue"),
                          "second": a.get("answerLabel") or a.get("answerValue"),
                          "note": a.get("note", "")} for d, a in split],
           "broken": [{"id": d["id"], "note": a.get("note", "")} for d, a in broken],
           "held_contaminated": [d["id"] for d, _ in held]}
    json.dump(out, open(f"{HERE}/key_verdicts.json", "w"), indent=1)
    print(f"\nwrote key_verdicts.json")
