"""
How many complete R&W tests can be built from the parsed bank?

Solved as an integer transportation feasibility (max flow), not by dividing
totals: the binding constraint is a skill x difficulty CELL, not a row or a
column. Dividing 1,783 questions by 81 suggests 22 tests; the true answer is
16, because e.g. Module 2 Easy wants easy Rhetorical Synthesis and only 38 of
the 199 are easy.

    python3 capacity.py <bank.json> [--label-satoplam MODE]

MODE for the SAToplam questions, which carry no difficulty label:
  exclude      leave them out (the honest status quo)
  proportional split each skill's unlabelled questions across E/M/H in the same
               ratio the College Board questions of that skill show
  wildcard     let them take any difficulty (optimistic upper bound if the
               labelling pass lands perfectly)
"""
import json
import sys
from collections import defaultdict, deque

DIFFS = ["EASY", "MEDIUM", "HARD"]
QUOTAS = {"M1":  {"EASY": 3,  "MEDIUM": 15, "HARD": 9},
          "M2E": {"EASY": 21, "MEDIUM": 6,  "HARD": 0},
          "M2H": {"EASY": 2,  "MEDIUM": 10, "HARD": 15}}
PER_TEST = {d: sum(q[d] for q in QUOTAS.values()) for d in DIFFS}

BLUEPRINTS = {
    "standard  (WiC 5, CoE 3)": {
        "Words in Context": 5, "Text Structure and Purpose": 2, "Cross-Text Connections": 1,
        "Central Ideas and Details": 2, "Command of Evidence": 3, "Inferences": 2,
        "SEC": 6, "Transitions": 3, "Rhetorical Synthesis": 3},
    "rebalanced (WiC 4, CoE 4)": {
        "Words in Context": 4, "Text Structure and Purpose": 2, "Cross-Text Connections": 1,
        "Central Ideas and Details": 2, "Command of Evidence": 4, "Inferences": 2,
        "SEC": 6, "Transitions": 3, "Rhetorical Synthesis": 3},
    "CoE-heavy  (WiC 4, CoE 5, TS 1)": {
        "Words in Context": 4, "Text Structure and Purpose": 1, "Cross-Text Connections": 1,
        "Central Ideas and Details": 2, "Command of Evidence": 5, "Inferences": 2,
        "SEC": 6, "Transitions": 3, "Rhetorical Synthesis": 3},
}


def build_supply(path, mode):
    labelled = defaultdict(lambda: defaultdict(int))
    unlabelled = defaultdict(int)
    for q in json.load(open(path)):
        if "error" in q or q.get("already_in_bank"):
            continue
        s = "SEC" if q["skill"] in ("Boundaries", "Form, Structure, and Sense") else q["skill"]
        if q.get("difficulty"):
            labelled[s][q["difficulty"]] += 1
        else:
            unlabelled[s] += 1

    sup = {s: {d: labelled[s][d] for d in DIFFS} for s in labelled}
    for s in unlabelled:
        sup.setdefault(s, {d: 0 for d in DIFFS})

    if mode == "exclude":
        return sup, dict(unlabelled)
    for s, n in unlabelled.items():
        if mode == "wildcard":
            # No cell cap: model as freely assignable by adding to every cell,
            # bounded overall by a separate total-supply edge.
            for d in DIFFS:
                sup[s][d] += n
        else:  # proportional
            tot = sum(labelled[s].values())
            if tot == 0:
                for d in DIFFS:
                    sup[s][d] += n // 3
            else:
                for d in DIFFS:
                    sup[s][d] += round(n * labelled[s][d] / tot)
    return sup, dict(unlabelled)


def feasible(N, slots, sup, wildcard_cap=None):
    skills = [s for s in slots if slots[s]]
    n = len(skills) + 3 + 2
    src, snk = n - 2, n - 1
    cap = [[0] * n for _ in range(n)]
    for i, s in enumerate(skills):
        cap[src][i] = N * 3 * slots[s]
        for j, d in enumerate(DIFFS):
            cap[i][len(skills) + j] = sup.get(s, {}).get(d, 0)
    for j, d in enumerate(DIFFS):
        cap[len(skills) + j][snk] = N * PER_TEST[d]
    need = N * 3 * sum(slots[s] for s in skills)
    flow = 0
    while True:
        par = [-1] * n; par[src] = src; dq = deque([src])
        while dq:
            u = dq.popleft()
            for v in range(n):
                if par[v] == -1 and cap[u][v] > 0:
                    par[v] = u; dq.append(v)
        if par[snk] == -1:
            break
        a, v = 10 ** 9, snk
        while v != src:
            a = min(a, cap[par[v]][v]); v = par[v]
        v = snk
        while v != src:
            cap[par[v]][v] -= a; cap[v][par[v]] += a; v = par[v]
        flow += a
    if flow != need:
        return False
    # Under wildcard, a skill's unlabelled pool was added to every cell, so also
    # check the skill never exceeds its real total.
    if wildcard_cap:
        for s in skills:
            if N * 3 * slots[s] > wildcard_cap[s]:
                return False
    return True


def maxtests(slots, sup, cap=None):
    N = 0
    while feasible(N + 1, slots, sup, cap):
        N += 1
    return N


def main():
    path = sys.argv[1]
    print(f"{'blueprint':34}{'exclude':>10}{'proportional':>14}{'wildcard':>10}")
    results = {}
    for label, slots in BLUEPRINTS.items():
        assert sum(slots.values()) == 27, (label, sum(slots.values()))
        row = []
        for mode in ("exclude", "proportional", "wildcard"):
            sup, unl = build_supply(path, mode)
            totals = None
            if mode == "wildcard":
                totals = {}
                for q in json.load(open(path)):
                    if "error" in q or q.get("already_in_bank"):
                        continue
                    s = "SEC" if q["skill"] in ("Boundaries", "Form, Structure, and Sense") else q["skill"]
                    totals[s] = totals.get(s, 0) + 1
            row.append(maxtests(slots, sup, totals))
        results[label] = row
        print(f"{label:34}{row[0]:>10}{row[1]:>14}{row[2]:>10}")
    return results


if __name__ == "__main__":
    main()
