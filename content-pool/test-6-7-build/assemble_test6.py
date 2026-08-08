#!/usr/bin/env python3
"""
Assemble Test 6 from the verified pools into insert-ready JSON.

Shape (matching Test 1, the reference implementation):
    READING_WRITING  M1 STANDARD / M2 EASY / M2 HARD   27 each
    MATH             M1 STANDARD / M2 EASY / M2 HARD   22 each, 19 MC + 3 FR

The ordering rule the user restated is enforced by construction rather than by
inspection: every R&W module is sorted on its block rank, so the reading domains
come first in the mandated sequence and the writing block starts at about
question 14-15 and never earlier. `report()` then re-checks that the rank
sequence is monotonic, that no reading question follows a writing question, and
that the first writing question lands in the 14-16 window.

Run:  python3 assemble_test6.py
Out:  test6.json
"""
import json
import os
import random
from collections import Counter

from math_m2easy import TEST6 as MATH_M2E
from math_authored_mc import QUESTIONS as AUTHORED_MC
import rw_octusb_m1, rw_octintb_m1, rw_octusc_m1, rw_octintb_m2, rw_octusb_m2
import rw_octusc_m2, rw_auguse, rw_authored

HERE = os.path.dirname(os.path.abspath(__file__))

# Mandated block order. Index is the sort key; 0-5 reading, 6-9 writing.
BLOCK_ORDER = [
    "Words in Context", "Text Structure and Purpose", "Cross-Text Connections",
    "Central Ideas and Details", "Command of Evidence", "Inferences",
    "Boundaries", "Form, Structure, and Sense", "Transitions", "Rhetorical Synthesis",
]
RANK = {s: i for i, s in enumerate(BLOCK_ORDER)}
FIRST_WRITING = 6

SKILL_CODE = {
    "Words in Context": ("CAS", "CAS-WV"),
    "Text Structure and Purpose": ("CAS", "CAS-TS"),
    "Cross-Text Connections": ("CAS", "CAS-CT"),
    "Central Ideas and Details": ("INI", "INI-CI"),
    "Command of Evidence": ("INI", "INI-CE"),
    "Inferences": ("INI", "INI-IE"),
    "Boundaries": ("SEC", "SEC-BS"),
    "Form, Structure, and Sense": ("SEC", "SEC-FS"),
    "Transitions": ("EOI", "EOI-TR"),
    "Rhetorical Synthesis": ("EOI", "EOI-RS"),
}

# Per-module domain quota. Reading totals 14, writing 13, so the writing block
# opens at question 15 in every module.
QUOTA = {
    "Words in Context": 5, "Text Structure and Purpose": 2, "Central Ideas and Details": 2,
    "Command of Evidence": 3, "Inferences": 2,
    "Boundaries": 4, "Form, Structure, and Sense": 3, "Transitions": 3,
    "Rhetorical Synthesis": 3,
}
CROSS_TEXT_MODULE = "RW_M2H"   # the single Cross-Text item goes here, replacing one WiC

# Transcribed Math questions whose figure survives only as a prose description
# in the transcript. Rule 3 forbids a description standing in for the picture,
# and no source image was kept to crop, so these are excluded and replaced by
# authored items H21-H24.
FIGURE_ONLY_AS_PROSE = {
    "junev2_math_m1:7":            "scatterplot described point by point in the stem",
    "junev2_math_m2:8":            "labelled right triangle described in the stem",
    "march_intb_test1_math_m2:10": "dot plot of Jupiter moon orbital periods described in the stem",
    "may_inta_math_m1:20":         "graph of an exponential function described in the stem",
}

# Domain and skill for every transcribed pool question, assigned by reading each
# stem. Looked up by code at insert time, never by name.
POOL_SKILL = {
 "decintb_math_m1:9": "ALG-LE",   "decintb_math_m1:10": "ALG-LE",  "decintb_math_m1:11": "ADV-NE",
 "decintb_math_m1:21": "ADV-NF",  "decintb_math_m1:22": "ADV-EQ",  "decintb_math_m2:5": "ADV-NF",
 "decintb_math_m2:15": "ADV-NF",  "decintb_math_m2:18": "ADV-NE",  "decintb_math_m2:20": "GT-AV",
 "junev2_math_m1:6": "ALG-LF",    "junev2_math_m1:12": "PSDA-RP",  "junev2_math_m1:13": "ADV-NF",
 "junev2_math_m1:17": "ALG-LE",   "junev2_math_m2:1": "ALG-LF",    "junev2_math_m2:16": "ADV-EQ",
 "junev2_math_m2:18": "ADV-NE",   "junev2_math_m2:20": "ALG-LF",
 "march_intb_test1_math_m1:15": "ALG-LE", "march_intb_test1_math_m1:21": "ALG-LF",
 "march_intb_test1_math_m2:4": "PSDA-DI", "march_intb_test1_math_m2:6": "ADV-NF",
 "march_intb_test1_math_m2:20": "GT-LA",
 "may_inta_math_m1:1": "ALG-LE",  "may_inta_math_m1:4": "ADV-NF",  "may_inta_math_m1:8": "PSDA-ST",
 "may_inta_math_m1:9": "PSDA-ST", "may_inta_math_m1:13": "ALG-LE", "may_inta_math_m1:21": "ADV-NF",
 "may_inta_math_m1:22": "ADV-NE", "may_inta_math_m2:9": "ADV-EQ",  "may_inta_math_m2:15": "GT-AV",
 "octintb_math_m1:1": "ALG-LF",   "octintb_math_m1:9": "ADV-NF",
 "octusb_math_m2:12": "PSDA-RP",  "octusb_math_m2:16": "PSDA-ST",
 "octusc_supplement:M2-Q2": "ADV-NE",
}
DOMAIN_OF = {"ALG": "ALG", "ADV": "ADV", "PSDA": "PSDA", "GT": "GT"}


def rw_pool():
    """Every available R&W question, tagged with where it came from."""
    mods = [rw_octusb_m1, rw_octintb_m1, rw_octusc_m1, rw_octintb_m2,
            rw_octusb_m2, rw_octusc_m2, rw_auguse, rw_authored]
    out = []
    for m in mods:
        lists = [("QUESTIONS", m.QUESTIONS)]
        if hasattr(m, "AUGUSC"):
            lists.append(("AUGUSC", m.AUGUSC))
        for listname, L in lists:
            src = m.SOURCE + ("-USC" if listname == "AUGUSC" else "")
            for q in L:
                mod = getattr(m, "MODULE", "RW")
                out.append(dict(q, _src=src, _ref=f"{src}/{mod}:{q['num']}"))
    return out


def build_rw():
    """Deal three 27-question modules from the pool, honouring the quotas."""
    pool = rw_pool()
    by_skill = {}
    for q in pool:
        by_skill.setdefault(q["skill"], []).append(q)
    # Deterministic: shuffle with a fixed seed so a rerun produces the same test.
    rng = random.Random(6)
    for v in by_skill.values():
        rng.shuffle(v)

    modules = {}
    for name in ("RW_M1", "RW_M2E", "RW_M2H"):
        quota = dict(QUOTA)
        picked = []
        if name == CROSS_TEXT_MODULE and by_skill.get("Cross-Text Connections"):
            picked.append(by_skill["Cross-Text Connections"].pop())
            quota["Words in Context"] -= 1
        for skill, want in quota.items():
            have = by_skill.get(skill, [])
            assert len(have) >= want, f"{name}: need {want} {skill}, {len(have)} left"
            picked += [have.pop() for _ in range(want)]
        picked.sort(key=lambda q: RANK[q["skill"]])
        for i, q in enumerate(picked):
            q["order"] = i + 1
            q["domainCode"], q["skillCode"] = SKILL_CODE[q["skill"]]
        modules[name] = picked
    return modules


def build_math():
    """Math M1 and M2 Hard from the transcribed pool plus the authored MC set."""
    pool = [p for p in json.load(open(os.path.join(HERE, "math_pool_available.json")))
            if f"{p['src']}:{p['num']}" not in FIGURE_ONLY_AS_PROSE]
    mc = [p for p in pool if p["type"] == "MULTIPLE_CHOICE"]
    fr = [p for p in pool if p["type"] == "FREE_RESPONSE"]
    rng = random.Random(6)
    rng.shuffle(mc)
    rng.shuffle(fr)

    authored = [dict(q, _ref=f"AUTHORED:{q['n']}") for q in AUTHORED_MC]
    assert len(mc) + len(authored) >= 38, "not enough MC for Test 6"
    assert len(fr) >= 6, "not enough FR for Test 6"

    # Interleave transcribed and authored MC so neither module is made entirely
    # of one kind, then split 19/19.
    all_mc = [normalise_pool_q(p) for p in mc] + [normalise_authored(q) for q in authored]
    rng.shuffle(all_mc)
    assert len(all_mc) >= 38, f"only {len(all_mc)} MC available, need 38"
    m1_mc, m2h_mc = all_mc[:19], all_mc[19:38]
    m1_fr = [normalise_pool_q(p) for p in fr[:3]]
    m2h_fr = [normalise_pool_q(p) for p in fr[3:6]]

    def finish(mcs, frs):
        qs = mcs + frs
        for i, q in enumerate(qs):
            q["order"] = i + 1
        return qs

    out = {"MATH_M1": finish(m1_mc, m1_fr), "MATH_M2H": finish(m2h_mc, m2h_fr)}
    m2e = []
    for i, q in enumerate(MATH_M2E):
        item = dict(order=i + 1, type=q["type"], stem=q["stem"], domain=q["domain"],
                    skill=q["skill"], sourceRef="AUTHORED (Test 6 M2 Easy, sympy-verified)",
                    verified=q["check"])
        if q["type"] == "MULTIPLE_CHOICE":
            item["choices"], item["correct"] = q["choices"], q["correct"]
        else:
            item["correctAnswerFR"] = json.dumps(q["answers"])
        if "table" in q:
            item["table"] = q["table"]
        out["MATH_M2E"] = out.get("MATH_M2E", []) + [item]
    return out


def normalise_pool_q(p):
    q = p["q"]
    ref = f"{p['src']}:{p['num']}"
    skill = POOL_SKILL[ref]
    item = dict(type=p["type"], stem=p["stem"], sourceRef=ref,
                domain=DOMAIN_OF[skill.split("-")[0]], skill=skill,
                verified=str(q.get("verified", "")))
    if p["type"] == "MULTIPLE_CHOICE":
        ch = q.get("choices") or []
        item["choices"] = [c["content"] if isinstance(c, dict) else c for c in ch]
        item["correct"] = q.get("correct")
    else:
        ans = q.get("answers") or [q.get("correct")]
        item["correctAnswerFR"] = json.dumps([str(a) for a in ans])
    for extra in ("table", "figureFile", "needsFigure", "NOTE"):
        if extra in q:
            item[extra] = q[extra]
    return item


def normalise_authored(q):
    item = dict(type="MULTIPLE_CHOICE", stem=q["stem"], choices=q["choices"],
                correct=q["correct"], domain=q["domain"], skill=q["skill"],
                sourceRef=f"AUTHORED:{q['n']}", verified=q["check"])
    if "table" in q:
        item["table"] = q["table"]
    return item


def report(rw, math):
    ok = True
    print("Reading & Writing")
    for name, qs in rw.items():
        ranks = [RANK[q["skill"]] for q in qs]
        mono = all(ranks[i] <= ranks[i + 1] for i in range(len(ranks) - 1))
        first_w = next((i + 1 for i, r in enumerate(ranks) if r >= FIRST_WRITING), None)
        leak = [i + 1 for i, r in enumerate(ranks)
                if r < FIRST_WRITING and first_w and i + 1 > first_w]
        reading = sum(1 for r in ranks if r < FIRST_WRITING)
        good = (len(qs) == 27 and mono and not leak and 14 <= first_w <= 16)
        ok &= good
        print(f"  {name:8} n={len(qs)}  reading={reading} writing={len(qs)-reading}  "
              f"writing starts at Q{first_w}  monotonic={mono}  "
              f"{'OK' if good else 'FAIL'}")
    print("Math")
    for name, qs in math.items():
        mc = sum(1 for q in qs if q["type"] == "MULTIPLE_CHOICE")
        fr = len(qs) - mc
        good = len(qs) == 22 and fr <= 3
        ok &= good
        print(f"  {name:8} n={len(qs)}  MC={mc} FR={fr}  "
              f"{dict(Counter(q['domain'] for q in qs))}  {'OK' if good else 'FAIL'}")
    # no question may appear twice anywhere in the package
    refs = [q.get("_ref") or q["sourceRef"] for m in list(rw.values()) + list(math.values())
            for q in m]
    dup = [r for r, c in Counter(refs).items() if c > 1 and "AUTHORED (Test 6" not in r]
    print(f"\nduplicate references across the package: {dup or 'none'}")
    ok &= not dup
    return ok


if __name__ == "__main__":
    rw = build_rw()
    math = build_math()
    good = report(rw, math)
    out = {**{k: v for k, v in rw.items()}, **math}
    with open(os.path.join(HERE, "test6.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    total = sum(len(v) for v in out.values())
    print(f"\nwrote test6.json — {total} questions; "
          f"{'all modules valid' if good else 'VALIDATION FAILED'}")
    raise SystemExit(0 if good else 1)
