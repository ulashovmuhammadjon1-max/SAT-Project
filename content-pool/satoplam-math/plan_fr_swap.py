# -*- coding: utf-8 -*-
"""Pick a HARD multiple-choice replacement for one grid-in in each module
whose HARD tier is entirely free-response.

Four Module 2 Easy modules have a HARD tier of exactly 3 questions, all
free-response. No ordering of those three avoids a run of three, so the fix
has to be a content swap rather than a sort. Each replacement is screened for
co-visibility against every question in the same test, exactly as the
allocator does.
"""
import json, os, sys
import sim

HERE = os.path.dirname(os.path.abspath(__file__))
REJECT = 0.35
TARGETS = ["Test 6", "Test 8", "Test 13", "Test 14"]

pool = {q["id"]: q for q in json.load(open(f"{HERE}/pool.json"))}
alloc = {}
for f in ("allocation.json", "allocation2.json"):
    for t in json.load(open(f"{HERE}/{f}")):
        alloc[t["title"]] = t

used = {q["id"] for t in alloc.values()
        for m in t["modules"].values() for q in m["questions"]}
spare = [q for q in pool.values()
         if q["id"] not in used and q["difficulty"] == "HARD" and q.get("choices")]

plan, taken = [], set()
for title in TARGETS:
    t = alloc[title]
    # Every question the same student could meet beside the replacement:
    # Module 1 and this Module 2 branch. M2 Hard is never co-visible with M2 Easy.
    against = t["modules"]["M1"]["questions"] + t["modules"]["M2E"]["questions"]
    sigs = [sim.sig(q) for q in against]
    hard_fr = [q for q in t["modules"]["M2E"]["questions"]
               if q["difficulty"] == "HARD" and not q.get("choices")]
    assert len(hard_fr) == 3, (title, len(hard_fr))
    drop = hard_fr[-1]

    pick = None
    for cand in spare:
        if cand["id"] in taken:
            continue
        s = sim.sig(cand)
        if max((sim.score(s, o)[0] for o in sigs), default=0) < REJECT:
            pick = cand
            break
    if pick is None:
        print(f"{title}: NO CLEAN REPLACEMENT", file=sys.stderr)
        continue
    taken.add(pick["id"])
    plan.append({"test": title, "drop": drop["id"], "add": pick["id"],
                 "addSource": ("SATHARD:" if pick["id"].startswith("sathard")
                               else "SATMATH:") + pick["id"]})
    print(f"{title}: drop {drop['id']}  ->  add {pick['id']}")

json.dump(plan, open(f"{HERE}/fr_swap.json", "w"), indent=1)
print(f"\nwrote fr_swap.json ({len(plan)})")
