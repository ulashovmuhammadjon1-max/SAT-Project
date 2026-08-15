# -*- coding: utf-8 -*-
"""Turn the verified transcriptions into the pool the allocator draws from.

    python3 build_pool.py

Four things happen here, in order:

1. Attach the built figures. A question that still says `needsFigure` with no
   image is dropped — CLAUDE.md rule 3 is that a prose description of a figure
   substitutes for the picture and usually leaks the answer, so shipping one
   without its image is worse than shipping nothing.
2. Drop questions the transcribers or adjudicators marked unanswerable.
3. Collapse duplicate clusters. These books collect real exam questions across
   many administrations and the exams reuse templates, so the same question
   appears under several topics, across both editions, and in the Hard Book —
   `sathard-advanced-math-121` is byte-identical to `-101`. One member of each
   cluster survives.
4. Report supply against what Tests 6-31 need, per difficulty, because the
   binding constraint is a difficulty tier and not the total.
"""
import json, glob, os
from collections import defaultdict

import sim

HERE = os.path.dirname(os.path.abspath(__file__))
COLLAPSE = 0.60   # read off the band survey: at and above this they are the
                  # same question, not merely the same skill.

pool = json.load(open(f"{HERE}/ready.json"))

# Defects that a threshold cannot decide — see blocked.json for the reason
# beside each id. They are dropped rather than repaired because the pool has
# several hundred spare questions and a source defect repaired by guesswork is
# worse than a question that never ships.
blocked = json.load(open(f"{HERE}/blocked.json"))["ids"]
pool = [q for q in pool if q["id"] not in blocked]
print(f"blocked by hand      {len(blocked)}")

figs = {}
for f in sorted(glob.glob(f"{HERE}/fig/f*-*.jsonl")):
    for line in open(f):
        if line.strip():
            try:
                r = json.loads(line)
                if r.get("imageUrl"):
                    figs[r["id"]] = r
            except Exception:
                pass

attached = dropped_fig = 0
kept = []
for q in pool:
    if q["id"] in figs:
        fr = figs[q["id"]]
        q["imageUrl"] = fr["imageUrl"]
        q["imageAlt"] = fr.get("alt", "")
        if fr.get("note"):
            q["note"] = (q.get("note", "") + " | figure: " + fr["note"]).strip(" |")
        q["needsFigure"] = False
        attached += 1
    if q.get("needsFigure"):
        dropped_fig += 1
        continue
    kept.append(q)

# A "NONE" answer is the transcriber saying no choice works. It is a real
# finding and it is recorded, but it cannot ship to a student.
before = len(kept)
kept = [q for q in kept
        if str(q.get("answerLabel") or "").upper() != "NONE"
        and str(q.get("answerValue") or "").upper() != "NONE"]
dropped_none = before - len(kept)

print(f"verified pool          {len(pool)}")
print(f"  figures attached     {attached}")
print(f"  dropped, no figure   {dropped_fig}")
print(f"  dropped, no answer   {dropped_none}")
print(f"  -> {len(kept)}")

sigs = {q["id"]: sim.sig(q) for q in kept}
ids = [q["id"] for q in kept]
parent = {i: i for i in ids}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for a in range(len(ids)):
    for b in range(a + 1, len(ids)):
        if sim.score(sigs[ids[a]], sigs[ids[b]])[0] >= COLLAPSE:
            ra, rb = find(ids[a]), find(ids[b])
            if ra != rb:
                parent[ra] = rb

clusters = defaultdict(list)
for i in ids:
    clusters[find(i)].append(i)

byid = {q["id"]: q for q in kept}
survivors = []
for members in clusters.values():
    # Prefer the Hard Book copy: it is the tier in shortest supply, and a
    # question that appears in both books is one the Hard Book vouched for.
    members.sort(key=lambda i: (0 if i.startswith("sathard") else 1, i))
    survivors.append(byid[members[0]])

absorbed = len(kept) - len(survivors)
print(f"  duplicate clusters   {sum(1 for v in clusters.values() if len(v) > 1)}"
      f" absorbing {absorbed}")
print(f"\nPOOL {len(survivors)}")

NEED = {"EASY": 14, "MEDIUM": 26, "HARD": 26}   # per test, from CLAUDE.md
print(f"\n{'tier':8} {'have':>5} {'MC':>5} {'FR':>5} {'need/test':>10} {'tests':>6}")
limit = None
for d in ("EASY", "MEDIUM", "HARD"):
    sub = [q for q in survivors if q["difficulty"] == d]
    mc = sum(1 for q in sub if q.get("choices"))
    n = len(sub) // NEED[d]
    limit = n if limit is None else min(limit, n)
    print(f"{d:8} {len(sub):5} {mc:5} {len(sub) - mc:5} {NEED[d]:10} {n:6}")

# Free response is capped per module, so MC is its own constraint.
mc_total = sum(1 for q in survivors if q.get("choices"))
fr_total = len(survivors) - mc_total
print(f"\nMC {mc_total} / 51 per test = {mc_total // 51} tests"
      f"   |   FR {fr_total} / 15 per test = {fr_total // 15} tests")
print(f"\nTESTS SUPPORTABLE: {min(limit, mc_total // 51)}  "
      f"(Tests 6-{5 + min(limit, mc_total // 51)})")

json.dump(survivors, open(f"{HERE}/pool.json", "w"), indent=1)
print(f"\nwrote pool.json ({len(survivors)})")
