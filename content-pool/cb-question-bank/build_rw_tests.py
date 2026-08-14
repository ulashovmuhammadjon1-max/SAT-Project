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
def blocks_for(module_difficulty):
    """Skill blocks for one module, in the mandated domain-block order.

    Cross-Text Connections is dropped from the Easy branch and its slot given
    to Central Ideas and Details. Supply is the reason: only 42 Cross-Text
    questions remain, and 3 per test caps the run at 14 tests when 16 are
    needed. CLAUDE.md treats Cross-Text as 0-1 per module and explicitly
    optional, so thinning it is within the blueprint where inventing questions
    would not be.
    """
    ct = 0 if module_difficulty == "EASY" else 1
    return [
        ("Words in Context", 5),
        ("Text Structure and Purpose", 2),
        ("Cross-Text Connections", ct),
        ("Central Ideas and Details", 2 + (1 - ct)),
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


def assign(slots, quota, pool, spare=None):
    """Choose a difficulty for every skill block in this module.

    Min-cost max-flow, not plain max-flow. Plain max-flow finds *a* feasible
    assignment, and a feasible one is not good enough here: it happily sends a
    slot to a difficulty where the labelled pool is empty while labelled
    questions of the same skill sit unused at another difficulty. Measured, it
    left 374 College Board questions on the shelf and pulled 697 unlabelled
    ones in their place.

    Costs encode the source preference. The user asked for these tests to be
    built from the SAToplam books first and to fall back on the College Board
    export only where SAToplam runs short, so the unlabelled (SAToplam) edge
    costs 0 and the labelled (College Board) edge costs 1.

    The trade-off is real and worth stating: SAToplam carries no difficulty
    label, so every question drawn from it has its difficulty ASSIGNED by
    placement rather than measured. Those rows are marked
    `difficulty_inferred`.

    Graph:  src -> skill -> difficulty -> sink,
    with a per-skill `spare` node so one skill's unlabelled pool cannot be
    spent more than once across the three difficulties.
    """
    skills = [s for s, n in slots if n]
    need = dict(slots)
    S = len(skills)
    # node ids: 0..S-1 skills | S..2S-1 spare | 2S..2S+2 difficulties | src | snk
    N = 2 * S + 3 + 2
    src, snk = N - 2, N - 1
    cap = [[0] * N for _ in range(N)]
    cost = [[0] * N for _ in range(N)]

    def edge(u, v, c, w):
        cap[u][v] += c
        cost[u][v] = w
        cost[v][u] = -w

    for i, sk in enumerate(skills):
        edge(src, i, need[sk], 0)
        if spare and spare[sk]:
            edge(i, S + i, len(spare[sk]), 0)      # SAToplam preferred
        for j, d in enumerate(DIFFS):
            if pool[sk][d]:
                edge(i, 2 * S + j, len(pool[sk][d]), 1)   # College Board fallback
            if spare and spare[sk]:
                edge(S + i, 2 * S + j, len(spare[sk]), 0)
    for j, d in enumerate(DIFFS):
        edge(2 * S + j, snk, quota.get(d, 0), 0)

    total = sum(need[s] for s in skills)
    flow = 0
    while flow < total:
        # Bellman-Ford: costs include negative residual edges.
        dist = [float("inf")] * N
        par = [-1] * N
        dist[src] = 0
        for _ in range(N):
            changed = False
            for u in range(N):
                if dist[u] == float("inf"):
                    continue
                for v in range(N):
                    if cap[u][v] > 0 and dist[u] + cost[u][v] < dist[v]:
                        dist[v] = dist[u] + cost[u][v]
                        par[v] = u
                        changed = True
            if not changed:
                break
        if par[snk] == -1:
            return None
        aug, v = 10 ** 9, snk
        while v != src:
            aug = min(aug, cap[par[v]][v]); v = par[v]
        v = snk
        while v != src:
            cap[par[v]][v] -= aug; cap[v][par[v]] += aug; v = par[v]
        flow += aug

    # Read the assignment back: labelled flow is skill -> difficulty directly,
    # unlabelled flow arrives via that skill's spare node.
    out = defaultdict(lambda: defaultdict(int))
    spare_out = defaultdict(lambda: defaultdict(int))
    for i, sk in enumerate(skills):
        for j, d in enumerate(DIFFS):
            out[sk][d] = cap[2 * S + j][i]            # reverse edge = flow
            spare_out[sk][d] = cap[2 * S + j][S + i]
    return out, spare_out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bank"); ap.add_argument("out")
    ap.add_argument("--tests", nargs="+", type=int, required=True)
    ap.add_argument("--exclude", nargs="*", default=[],
                    help="previously built test files whose questions are already in use")
    ap.add_argument("--allow-unlabelled", action="store_true",
                    help="also draw on questions with no difficulty label, preferring MEDIUM slots")
    args = ap.parse_args()

    # A question already placed in another test must never be picked again — a
    # student meeting the same item in two tests is the whole point of tracking
    # this. Read from the built files rather than the database so the exclusion
    # is deterministic and auditable, and verify against the DB afterwards.
    used = set()
    for f in args.exclude:
        for t in json.load(open(f)):
            for m in t["modules"]:
                for q in m["questions"]:
                    used.add(q["cb_id"])
    if used:
        print(f"excluding {len(used)} questions already placed in earlier tests")

    rng = random.Random(20260814)
    pool = defaultdict(lambda: defaultdict(list))
    unlabelled = defaultdict(list)
    for q in json.load(open(args.bank)):
        if "error" in q or q.get("already_in_bank") or q.get("needs_figure"):
            continue
        if q["id"] in used:
            continue
        if q.get("difficulty"):
            pool[skill_key(q)][q["difficulty"]].append(q)
        elif args.allow_unlabelled:
            # SAToplam questions carry no difficulty label. They are real SAT
            # questions, which is why they are worth using at all, but the
            # label has to come from somewhere.
            #
            # They are pooled separately and drawn ONLY after the labelled
            # supply for a slot is exhausted, and preferentially into MEDIUM
            # slots. Medium is the middle of the distribution, so a question
            # whose true difficulty is unknown does least harm there: a
            # mislabelled item in the Easy branch would make the easier half of
            # an adaptive test harder than intended, which is the one place the
            # label actually changes what a student meets.
            unlabelled[skill_key(q)].append(q)
    for s in pool:
        for d in pool[s]:
            rng.shuffle(pool[s][d])
    for s in unlabelled:
        rng.shuffle(unlabelled[s])

    tests = []
    for tno in args.tests:
        modules = []
        for diff_label, order, quota in MODULES:
            blocks = blocks_for(diff_label)
            res = assign(blocks, quota, pool, unlabelled if args.allow_unlabelled else None)
            if res is None:
                raise SystemExit(f"Test {tno} module {diff_label}: supply exhausted")
            plan, plan_spare = res
            picked = []

            def take(q, d, inferred):
                passage, stem = split_passage_stem(q["question"])
                picked.append({
                    "cb_id": q["id"], "skill": q["skill"], "domain": q["domain"],
                    "difficulty": d, "passage": passage, "stem": stem,
                    "choices": q["choices"], "correct": q["correct"],
                    "rationale": q.get("rationale", ""),
                    "source_book": q.get("source_book"),
                    "difficulty_inferred": inferred,
                    "key_is_transcribed": q.get("key_is_transcribed", False),
                })

            for skill, nslots in blocks:         # preserves the mandated order
                if not nslots:
                    continue
                for d in DIFFS:
                    for _ in range(plan[skill].get(d, 0)):
                        take(pool[skill][d].pop(), d, False)
                    for _ in range(plan_spare[skill].get(d, 0)):
                        take(unlabelled[skill].pop(), d, True)

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
            inf = sum(1 for q in m["questions"] if q.get("difficulty_inferred"))
            print(f"  Test {t['test']:>2} M{m['order']}{m['difficulty'][:1]}  "
                  f"E{c['EASY']:>2} M{c['MEDIUM']:>2} H{c['HARD']:>2}"
                  + (f"  inferred:{inf:>2}" if inf else "")
                  + (f"   !! {nostem} without a stem" if nostem else ""))


if __name__ == "__main__":
    main()
