# -*- coding: utf-8 -*-
"""Split disputes.json across blind adjudicators.

    python3 build_adj.py <n> [--prefix adj2]

A slice carries the question and nothing else. The printed key and the first
agent's answer are both stripped here rather than in the dump tool, so a
curious adjudicator cannot find them by opening the slice file — which is
exactly how the one contaminated reading in the first round happened.
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2
PREFIX = sys.argv[sys.argv.index("--prefix") + 1] if "--prefix" in sys.argv else "adj"

disputes = json.load(open(f"{HERE}/disputes.json"))
done = set()
for f in os.listdir(f"{HERE}/adj"):
    if f.endswith(".jsonl"):
        for line in open(f"{HERE}/adj/{f}"):
            if line.strip():
                try: done.add(json.loads(line)["id"])
                except Exception: pass

todo = [d for d in disputes if d["id"] not in done]
print(f"{len(disputes)} disputes, {len(disputes) - len(todo)} already adjudicated, "
      f"{len(todo)} to go")

slim = [{
    "id": d["id"],
    "type": "FREE_RESPONSE" if not d.get("choices") else "MULTIPLE_CHOICE",
    "stem": d["stem"],
    "choices": d.get("choices") or [],
    "needsFigure": d.get("needsFigure", False),
    "book_note": d.get("note", ""),
} for d in todo]

per = math.ceil(len(slim) / N)
for i in range(N):
    sl = slim[i * per:(i + 1) * per]
    if not sl:
        continue
    name = f"{PREFIX}-{i + 1}"
    json.dump(sl, open(f"{HERE}/adj/{name}.slice.json", "w"), indent=1)
    print(f"  {name}  {len(sl)} questions")
