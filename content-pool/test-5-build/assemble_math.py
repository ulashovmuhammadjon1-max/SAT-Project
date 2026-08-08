#!/usr/bin/env python3
"""
Assemble Test 5's three Math modules from the verified source pools.

Every module must land on 19 MULTIPLE_CHOICE + 3 FREE_RESPONSE (Test 1's live
shape, and the <=3 FR cap in CLAUDE.md). The source modules do not have that
balance on their own -- real SAT modules carry ~6-7 free-response items -- so
each one keeps its three most interesting FR questions and is topped up with
multiple-choice from the Oct USC pool.

Domain/Skill are assigned here by hand, per question, by reading the content.
They are looked up by `code` at insert time, never by name.

Run:  python3 assemble_math.py
Out:  test5_math.json
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name)) as fh:
        return json.load(fh)


# --- which source questions go where ----------------------------------------
# Module 1: Oct IntB supplies 16 MC + 3 of its 6 FR; Oct USC supplies 3 MC.
# Q1 and Q12 dropped: both repeat a question already live in Test 3 (Q12 is an
# exact duplicate of Test 3 M2E Q22; Q1 is Test 3 M2E Q19 with new numbers).
M1_INTB_MC = [2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18, 19, 20, 22]
M1_INTB_FR = [5, 14, 21]          # dropped: 3, 6, 9 (over the FR cap)
M1_USC = ["M1-Q1", "M1-Q3", "M1-Q6", "M1-Q9", "M1-Q14"]

# Module 2 Hard: Oct USB supplies 12 MC + 3 of its 7 FR; Oct USC supplies 7 MC.
# Q1 dropped: same template as Test 3 M2H Q12 (10x^2-40x-150) with one digit changed.
M2H_USB_MC = [2, 5, 6, 8, 9, 11, 13, 14, 15, 18, 21]
M2H_USB_FR = [3, 19, 22]          # dropped: 7, 12, 16, 20 (over the FR cap)
# M2-Q2 dropped: "how many distinct real solutions" repeats Test 4 M2E Q10.
M2H_USC = ["M2-Q1", "M2-Q3", "M2-Q4", "M2-Q5", "M2-Q10", "M2-Q11",
           "M1-Q15", "M2-Q15"]

# --- Domain/Skill, assigned by reading each question ------------------------
SKILL = {
    ("M1", 1): "ALG-LF",  ("M1", 2): "ADV-EQ",  ("M1", 4): "ALG-LI",
    ("M1", 5): "PSDA-RP", ("M1", 7): "ADV-EQ",  ("M1", 8): "PSDA-DI",
    ("M1", 10): "ALG-LF", ("M1", 11): "ADV-NE", ("M1", 12): "ALG-LF",
    ("M1", 13): "GT-LA",  ("M1", 14): "ALG-LE", ("M1", 15): "ADV-NF",
    ("M1", 16): "ADV-NF", ("M1", 17): "PSDA-ST", ("M1", 18): "GT-TR",
    ("M1", 19): "ADV-NF", ("M1", 20): "PSDA-RP", ("M1", 21): "GT-TR",
    ("M1", 22): "GT-AV",
    ("M1", "M1-Q1"): "ALG-LF", ("M1", "M1-Q3"): "ADV-EQ", ("M1", "M1-Q6"): "ALG-LE",
    ("M1", "M1-Q9"): "PSDA-ST", ("M1", "M1-Q14"): "ALG-LE",

    ("M2H", 1): "ADV-NF",  ("M2H", 2): "ALG-LI",  ("M2H", 3): "ADV-NE",
    ("M2H", 5): "ALG-LF",  ("M2H", 6): "ALG-LE",  ("M2H", 8): "ALG-LE",
    ("M2H", 9): "GT-AV",   ("M2H", 11): "PSDA-DI", ("M2H", 13): "ADV-NF",
    ("M2H", 14): "ALG-LE", ("M2H", 15): "GT-AV",  ("M2H", 18): "ADV-NF",
    ("M2H", 19): "ALG-LI", ("M2H", 21): "ADV-NF", ("M2H", 22): "ADV-NE",
    ("M2H", "M2-Q1"): "GT-LA",  ("M2H", "M2-Q2"): "ADV-NE",
    ("M2H", "M2-Q3"): "ALG-LI", ("M2H", "M2-Q4"): "ALG-LE",
    ("M2H", "M2-Q5"): "ADV-NE", ("M2H", "M2-Q10"): "ALG-LF",
    ("M2H", "M2-Q11"): "ADV-NF", ("M2H", "M1-Q15"): "PSDA-ST",
    ("M2H", "M2-Q15"): "ALG-LI",
}
DOMAIN_OF = {"ALG": "ALG", "ADV": "ADV", "PSDA": "PSDA", "GT": "GT"}


def domain_for(skill):
    return DOMAIN_OF[skill.split("-")[0]]


def emit(src_q, module_tag, order):
    """Normalise a source question into the insert-ready shape."""
    key = (module_tag, src_q["num"])
    skill = SKILL[key]
    out = {
        "order": order,
        "type": src_q["type"],
        "stem": src_q["stem"],
        "domain": domain_for(skill),
        "skill": skill,
        "sourceRef": f"{src_q.get('source', 'OctUSC')}:{src_q['num']}",
        "verified": src_q["verified"],
    }
    if src_q["type"] == "MULTIPLE_CHOICE":
        out["choices"] = src_q["choices"]
        out["correct"] = src_q["correct"]
    else:
        # CLAUDE.md: correctAnswerFR must be a JSON-encoded ARRAY string.
        out["correctAnswerFR"] = json.dumps(src_q["answers"])
    for extra in ("table", "figureFile", "needsFigure", "FLAG", "NOTE"):
        if extra in src_q:
            out[extra] = src_q[extra]
    return out


def build():
    intb = {q["num"]: q for q in load("octintb_math_m1.json")["questions"]}
    usb = {q["num"]: q for q in load("octusb_math_m2.json")["questions"]}
    usc = {q["num"]: q for q in load("octusc_supplement.json")["questions"]}
    easy = load("t5_math_m2easy.json")

    modules = {}

    # ---- Module 1 ----------------------------------------------------------
    picks = ([intb[n] for n in M1_INTB_MC] + [usc[n] for n in M1_USC]
             + [intb[n] for n in M1_INTB_FR])
    modules["MATH_M1"] = [emit(q, "M1", i + 1) for i, q in enumerate(picks)]

    # ---- Module 2 (Hard) ---------------------------------------------------
    picks = ([usb[n] for n in M2H_USB_MC] + [usc[n] for n in M2H_USC]
             + [usb[n] for n in M2H_USB_FR])
    modules["MATH_M2_HARD"] = [emit(q, "M2H", i + 1) for i, q in enumerate(picks)]

    # ---- Module 2 (Easy) — the originally authored module -------------------
    out = []
    for i, q in enumerate(easy):
        item = {
            "order": i + 1,
            "type": q["type"],
            "stem": q["stem"],
            "domain": q["domain"],
            "skill": q["skill"],
            "sourceRef": "ORIGINAL (authored for Test 5, sympy-verified)",
            "verified": q["check"],
        }
        if q["type"] == "MULTIPLE_CHOICE":
            item["choices"] = q["choices"]
            item["correct"] = q["correct"]
        else:
            item["correctAnswerFR"] = json.dumps(q["answers"])
        if "table" in q:
            item["table"] = q["table"]
        out.append(item)
    modules["MATH_M2_EASY"] = out

    return modules


def report(modules):
    ok = True
    for name, qs in modules.items():
        mc = sum(1 for q in qs if q["type"] == "MULTIPLE_CHOICE")
        fr = len(qs) - mc
        doms = Counter(q["domain"] for q in qs)
        orders = [q["order"] for q in qs]
        good = len(qs) == 22 and fr <= 3 and orders == list(range(1, 23))
        ok &= good
        print(f"{name:14} n={len(qs):3} MC={mc:3} FR={fr}  {dict(doms)}  "
              f"{'OK' if good else 'FAIL'}")
    return ok


if __name__ == "__main__":
    mods = build()
    all_ok = report(mods)
    with open(os.path.join(HERE, "test5_math.json"), "w") as fh:
        json.dump(mods, fh, indent=1)
    print("\nwrote test5_math.json;", "all modules valid" if all_ok else "VALIDATION FAILED")
