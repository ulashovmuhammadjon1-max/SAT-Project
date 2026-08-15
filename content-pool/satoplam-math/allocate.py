# -*- coding: utf-8 -*-
"""Allocate the verified pool into Tests 6-N Math, at the mix CLAUDE.md records.

    python3 allocate.py [--tests 17]

Per module (22 questions each):

    Module 1  (STANDARD)   3 EASY   10 MEDIUM   9 HARD
    Module 2  (EASY)      10 EASY    9 MEDIUM   3 HARD
    Module 2  (HARD)       1 EASY    7 MEDIUM  14 HARD

Two placement rules on top of the mix:

* Hard Book questions never go into Module 2 Easy. The user's instruction was
  that they are Module 2 Hard questions; with Module 1's nine hard slots
  opened to them as well (their decision, because Module 1's hard questions
  are meant to be genuinely hard) the build reaches 17 tests instead of 11.
* Module 2 Hard takes Hard Book items first, so the hardest module is built
  from the curated-hard book wherever supply allows.

The part that matters most is the co-visibility screen. A student sits
Module 1 plus exactly ONE Module 2 branch, so M1-vs-M2E, M1-vs-M2H and
within-module pairs are all seen together in one sitting, while M2E-vs-M2H
never is. The R&W build skipped this and shipped 33 same-test duplicates, two
of them byte-identical.
"""
import json, os, sys
from collections import Counter, defaultdict

import sim

HERE = os.path.dirname(os.path.abspath(__file__))
FIRST_TEST = 6
N_TESTS = int(sys.argv[sys.argv.index("--tests") + 1]) if "--tests" in sys.argv else 17

# Read off the band survey, not guessed: 0.45-0.60 is the same question with
# the numbers changed, and 0.35-0.45 still holds real template repeats
# (x^2+kx+14=(x+n)(x+7) against x^2+kx+55=(x+n)(x+11) scored 0.44). Anything
# at or above this may not be co-visible with what it matches.
COVISIBLE_REJECT = 0.35

MODULES = [
    ("M1",  1, "STANDARD", {"EASY": 3,  "MEDIUM": 10, "HARD": 9}),
    ("M2E", 2, "EASY",     {"EASY": 10, "MEDIUM": 9,  "HARD": 3}),
    ("M2H", 2, "HARD",     {"EASY": 1,  "MEDIUM": 7,  "HARD": 14}),
]
FR_CAP = 5          # CLAUDE.md: raised from 3 for this rebuild, and closer to
                    # the real Digital SAT's 5-6 student-produced responses.
COVISIBLE = {("M1", "M2E"), ("M1", "M2H"), ("M2E", "M1"), ("M2H", "M1")}

pool = json.load(open(f"{HERE}/pool.json"))
meta = {}
for f in ("math_parsed.json", "hard_parsed.json"):
    for q in json.load(open(f"{HERE}/{f}")):
        meta[q["id"]] = q

for q in pool:
    m = meta[q["id"]]
    q["domain"], q["skill"], q["topic"] = m["domain"], m["skill"], m["topic"]
    q["hardbook"] = q["id"].startswith("sathard")
    q["fr"] = not q.get("choices")

sigs = {q["id"]: sim.sig(q) for q in pool}


def collides(cand, placed):
    """Does this candidate repeat anything a student would see beside it?"""
    for other in placed:
        if sim.score(sigs[cand["id"]], sigs[other["id"]])[0] >= COVISIBLE_REJECT:
            return other
    return None


# Roughly the Digital SAT's own domain shape over 22 questions. Used as a
# target to steer toward, not a hard quota — supply per tier is too tight in
# places to insist on it.
DOMAIN_TARGET = {"ALG": 7, "ADV": 8, "PSDA": 4, "GT": 3}

# A hard ceiling, not a preference. Without it the allocator keeps filling
# tests after the algebra and advanced-maths HARD supply is spent, and the
# last three Module 2 Hards came out 14 of 22 geometry with no
# problem-solving at all. A module that lopsided is not a Digital SAT module,
# so it is better to stop building tests than to ship it.
DOMAIN_CAP = 9


def rank(q, mod, used_dom, used_skill, used_topic):
    """Prefer the question that widens the module's coverage most.

    This is recomputed before every single pick. Sorting the candidate list
    once and walking it packs a module with whatever topic is plentiful — the
    first version of this allocator produced 22-question modules spanning
    three skills, because the counters updated while the ordering did not.

    Hard Book preference runs in opposite directions by module: Module 2 Hard
    should be built from the curated-hard book, while Module 1 should leave it
    alone until the ordinary books' hard supply is exhausted. Without that
    second half the Hard Book drains into the early tests and the last tests
    get none of it.
    """
    deficit = used_dom[q["domain"]] - DOMAIN_TARGET.get(q["domain"], 4)
    return (deficit, 0 if q["hardbook"] else 1,
            used_skill[q["skill"]], used_topic[q["topic"]], q["id"])


available = {q["id"]: q for q in pool}
tests, failures = [], []

for t in range(N_TESTS):
    title = f"Test {FIRST_TEST + t}"
    before = dict(available)
    short_here = []
    built = {}
    seen_in_test = []          # everything placed in this test so far
    for mod, order, diff, mix in MODULES:
        picks = []
        used_dom, used_skill, used_topic = Counter(), Counter(), Counter()
        fr_used = 0
        for tier in ("HARD", "MEDIUM", "EASY"):
            need = mix[tier]
            while need:
                # Only screen against questions this student could see beside
                # it: this module, plus the other module in a co-visible pair.
                against = picks + [p for p in seen_in_test
                                   if (p["_mod"], mod) in COVISIBLE]
                cands = [q for q in available.values()
                         if q["difficulty"] == tier
                         and not (mod == "M2E" and q["hardbook"])
                         and not (q["fr"] and fr_used >= FR_CAP)
                         and used_dom[q["domain"]] < DOMAIN_CAP]
                cands.sort(key=lambda q: rank(q, mod, used_dom, used_skill, used_topic))
                pick = next((q for q in cands if not collides(q, against)), None)
                if pick is None:
                    short_here.append(f"{title} {mod} {tier}: {need} short")
                    break
                pick["_mod"] = mod
                picks.append(pick)
                seen_in_test.append(pick)
                used_dom[pick["domain"]] += 1
                used_skill[pick["skill"]] += 1
                used_topic[pick["topic"]] += 1
                fr_used += pick["fr"]
                del available[pick["id"]]
                need -= 1
        built[mod] = {"order": order, "difficulty": diff, "questions": picks}
    if short_here:
        # Roll the whole test back. A part-built test leaves its questions
        # stranded out of the pool for no gain, and half a test is not a
        # deliverable.
        failures.extend(short_here)
        available.clear(); available.update(before)
        break
    tests.append({"title": title, "modules": built})

print(f"allocated {len(tests)} tests, {sum(len(m['questions']) for t in tests for m in t['modules'].values())} questions")
print(f"pool left: {len(available)}")
if failures:
    print(f"\nSHORTFALLS ({len(failures)}):")
    for f in failures[:30]:
        print("  " + f)
else:
    print("\nevery module filled exactly")

print(f"\n{'test':9} {'mod':5} {'E':>3}{'M':>3}{'H':>3} {'FR':>4} {'hbook':>6} "
      f"{'skills':>7}  domains")
for t in tests:
    for mod, m in t["modules"].items():
        qs = m["questions"]
        d = Counter(q["difficulty"] for q in qs)
        dom = Counter(q["domain"] for q in qs)
        print(f"{t['title']:9} {mod:5} {d['EASY']:3}{d['MEDIUM']:3}{d['HARD']:3} "
              f"{sum(q['fr'] for q in qs):4} {sum(q['hardbook'] for q in qs):6} "
              f"{len({q['skill'] for q in qs}):7}  "
              + " ".join(f"{k}{dom[k]}" for k in ("ALG", "ADV", "PSDA", "GT")))

for t in tests:
    for m in t["modules"].values():
        for q in m["questions"]:
            q.pop("_mod", None)

json.dump(tests, open(f"{HERE}/allocation.json", "w"), indent=1)
print(f"\nwrote allocation.json")
