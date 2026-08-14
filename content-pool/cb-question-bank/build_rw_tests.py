"""
Select official College Board questions for a run of Reading & Writing tests.

    python3 build_rw_tests.py <bank.json> <out.json> --tests 6 7 8 9 10

Draws ONLY from College Board rows: they carry an official key, an official
rationale and an official difficulty. The SAToplam rows have no difficulty
label at all, so they cannot fill a difficulty quota, and their keys are
transcribed rather than authoritative — see content-pool/satoplam/MANIFEST.md.

Blueprint and difficulty mix come from CLAUDE.md ("R&W TEST DIFFICULTY
STRUCTURE"). Questions flagged `needs_figure` are excluded: their charts are
vector glyphs that text extraction shredded, so their stems are unusable until
the figures are rebuilt.

Selection is a max-flow assignment per module, not a greedy pick. Greedy burns
scarce cells — easy Rhetorical Synthesis, easy Inferences — on the first test
and then starves, which cost 5 whole tests when measured.
"""
import argparse
import json
import random
import re
from collections import defaultdict, deque

DIFFS = ["EASY", "MEDIUM", "HARD"]

# Order matters: this is the mandated domain-block sequence from CLAUDE.md.
# Reading blocks first, writing blocks last, and no reading block may follow a
# writing block.
BLOCKS = [
    ("Words in Context", 5),
    ("Text Structure and Purpose", 2),
    ("Cross-Text Connections", 1),
    ("Central Ideas and Details", 2),
    ("Command of Evidence", 3),
    ("Inferences", 2),
    ("SEC", 6),
    ("Transitions", 3),
    ("Rhetorical Synthesis", 3),
]
MODULES = [
    ("STANDARD", 1, {"EASY": 3, "MEDIUM": 15, "HARD": 9}),
    ("EASY", 2, {"EASY": 21, "MEDIUM": 6, "HARD": 0}),
    ("HARD", 2, {"EASY": 2, "MEDIUM": 10, "HARD": 15}),
]

STEM_STARTERS = [
    "Which choice", "Which finding", "Which quotation", "Which statement", "Which data",
    "Which detail", "Which question", "What does", "As used in the text",
    "Based on the text", "According to the text", "The student wants",
    "Which of the following", "The text makes which", "Information in the text",
]


def split_passage_stem(text):
    """Separate the passage from the trailing question stem.

    Anchored on the stem's opening phrase rather than on sentence punctuation,
    because a Words-in-Context passage ends in `______` with no terminal stop
    and a punctuation-based split swallows the stem into the passage.
    """
    best = max((text.rfind(s) for s in STEM_STARTERS), default=-1)
    if best <= 0 or not text.rstrip().endswith("?"):
        # Fall back to the last sentence that ends in a question mark.
        m = list(re.finditer(r"(?<=[.?!”\"])\s+(?=[A-Z])", text))
        if m and text.rstrip().endswith("?"):
            best = m[-1].end()
        else:
            return text.strip(), ""
    return text[:best].strip(), text[best:].strip()


def skill_key(q):
    return "SEC" if q["skill"] in ("Boundaries", "Form, Structure, and Sense") else q["skill"]


def assign(slots, quota, pool):
    """Max-flow: which difficulty does each skill block take in this module?"""
    skills = [s for s, n in slots if n]
    n = len(skills) + 3 + 2
    src, snk = n - 2, n - 1
    cap = [[0] * n for _ in range(n)]
    need = dict(slots)
    for i, s in enumerate(skills):
        cap[src][i] = need[s]
        for j, d in enumerate(DIFFS):
            cap[i][len(skills) + j] = len(pool[s][d])
    for j, d in enumerate(DIFFS):
        cap[len(skills) + j][snk] = quota.get(d, 0)
    total = sum(need.values())
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
    if flow != total:
        return None
    out = defaultdict(dict)
    for i, s in enumerate(skills):
        for j, d in enumerate(DIFFS):
            out[s][d] = cap[len(skills) + j][i]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bank"); ap.add_argument("out")
    ap.add_argument("--tests", nargs="+", type=int, required=True)
    args = ap.parse_args()

    rng = random.Random(20260814)
    pool = defaultdict(lambda: defaultdict(list))
    for q in json.load(open(args.bank)):
        if "error" in q or q.get("already_in_bank") or q.get("needs_figure"):
            continue
        if q.get("source_book"):          # College Board rows only
            continue
        if not q.get("difficulty"):
            continue
        pool[skill_key(q)][q["difficulty"]].append(q)
    for s in pool:
        for d in pool[s]:
            rng.shuffle(pool[s][d])

    tests = []
    for tno in args.tests:
        modules = []
        for diff_label, order, quota in MODULES:
            plan = assign(BLOCKS, quota, pool)
            if plan is None:
                raise SystemExit(f"Test {tno} module {diff_label}: supply exhausted")
            picked = []
            for skill, _ in BLOCKS:              # preserves the mandated order
                for d in DIFFS:
                    for _ in range(plan[skill][d]):
                        q = pool[skill][d].pop()
                        passage, stem = split_passage_stem(q["question"])
                        picked.append({
                            "cb_id": q["id"], "skill": q["skill"], "domain": q["domain"],
                            "difficulty": q["difficulty"], "passage": passage, "stem": stem,
                            "choices": q["choices"], "correct": q["correct"],
                            "rationale": q["rationale"],
                        })
            for i, q in enumerate(picked, 1):
                q["order"] = i
            got = {d: sum(1 for q in picked if q["difficulty"] == d) for d in DIFFS}
            assert got == {**{d: 0 for d in DIFFS}, **quota}, (tno, diff_label, got, quota)
            assert len(picked) == 27
            modules.append({"subject": "READING_WRITING", "order": order,
                            "difficulty": diff_label, "questions": picked})
        tests.append({"test": tno, "modules": modules})

    json.dump(tests, open(args.out, "w"), indent=1)
    n = sum(len(m["questions"]) for t in tests for m in t["modules"])
    print(f"built {len(tests)} tests, {n} questions -> {args.out}")
    for t in tests:
        for m in t["modules"]:
            c = {d: sum(1 for q in m["questions"] if q["difficulty"] == d) for d in DIFFS}
            nostem = sum(1 for q in m["questions"] if not q["stem"])
            print(f"  Test {t['test']:>2} M{m['order']}{m['difficulty'][:1]}  "
                  f"E{c['EASY']:>2} M{c['MEDIUM']:>2} H{c['HARD']:>2}"
                  + (f"   !! {nostem} without a stem" if nostem else ""))


if __name__ == "__main__":
    main()
