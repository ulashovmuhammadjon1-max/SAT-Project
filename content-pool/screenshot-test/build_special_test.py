"""
Assemble SPECIAL TEST into special_test.json for insert_special.mjs.

Modules 1 and 2 Hard (both subjects) were transcribed from the user's
screenshots and solved independently (rw_m1.json, rw_m2_hard.json,
math_m1.json, math_m2_hard.json). Both Module 2 Easy sections are existing
database questions chosen by select_m2e_from_db.py (m2e_from_db.json); the
inserter COPIES them, so the originals stay where they are.

Difficulty for the transcribed modules is assigned by judgement to the user's
standing mix (CLAUDE.md): R&W M1 3/15/9, M2 Hard 2/10/15; Math M1 3/10/9,
M2 Hard 1/7/14 (easy/medium/hard). The script asserts the counts.

Run: python3 build_special_test.py
"""
import base64
import json
import re
from collections import Counter

LETTERS = "ABCD"
DOMAIN = {"CAS": "CAS", "INI": "INI", "SEC": "SEC", "EOI": "EOI",
          "ALG": "ALG", "ADV": "ADV", "PSDA": "PSDA", "GT": "GT"}

E, M, H = "EASY", "MEDIUM", "HARD"
DIFF = {
    "RW_M1":  [M, M, E, H, E, E, M, M, H, M, H, H, H, H, H, M, M, M, M, H, M, M, M, H, M, M, M],
    "RW_M2H": [H, H, M, E, M, H, H, H, E, H, H, M, H, H, H, H, M, M, M, M, H, M, M, H, M, H, H],
    "MATH_M1": [E, M, M, M, E, E, M, M, H, M, M, M, M, H, H, M, H, H, H, H, H, H],
    "MATH_M2H": [M, E, M, M, M, M, H, H, H, M, H, M, H, H, H, H, H, H, H, H, H, H],
}
TARGET = {"RW_M1": (3, 15, 9), "RW_M2H": (2, 10, 15), "MATH_M1": (3, 10, 9), "MATH_M2H": (1, 7, 14)}

# Repairs to copied database questions, by source question id: (field, old, new).
# Each must match exactly once, or the build stops.
FIXES = {
    # Missing punctuation joined two sentences.
    "049f8cfa-fd96-43d6-b844-78576d1d9ed6": [
        ["passage", "throughout the state the design", "throughout the state: the design"]],
    # A dash that never closed, and a missing comma before "all of whom".
    "0b3eb7c8-2295-4761-ad46-a8b555124a04": [
        ["passage", "categorized by topic – e.g., statement 13,", "categorized by topic (e.g., statement 13,"],
        ["passage", "categorized as anticipation and respondents all of whom", "categorized as anticipation), and respondents, all of whom"]],
    "381753bb-2278-4d5c-b3ab-f95454a0634c": [["passage", "campalgns", "campaigns"]],
    # Typos, and the student's goal belongs in the question, not in the notes.
    "00818a47-4b4d-4eec-88c7-0654eb70c95f": [
        ["passage", "was twisted, Its average", "was twisted, its average"],
        ["passage", "<p>The student wants to emphasize a similarity between EPDM rubber and four-ply NiTi wire fibers.</p>", ""],
        ["stem", "Which choice most effectively", "The student wants to emphasize a similarity between EPDM rubber and four-ply NiTi wire fibers. Which choice most effectively"],
        ["choice:B", "four-ply NITI wire", "four-ply NiTi wire"],
        ["choice:C", "the filbers were", "the fibers were"]],
}

# The whale question asks what "can most reasonably be concluded", which is an
# inference question; inference is always the last reading block, so it moves
# from the Central Ideas block to just before the other inference items.


def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()


def rw(q, difficulty):
    return {
        "domain": q["skill"].split("-")[0], "skill": q["skill"], "type": "MULTIPLE_CHOICE",
        "difficulty": difficulty, "passage": q["passage"], "stem": q["stem"],
        "choices": [{"label": LETTERS[i], "content": c, "isCorrect": LETTERS[i] == q["mine"]}
                    for i, c in enumerate(q["choices"])],
        "_ref": "screenshot:" + q.get("source", "bluecorn"),
    }


def math(q, difficulty):
    out = {
        "domain": q["skill"].split("-")[0], "skill": q["skill"], "difficulty": difficulty,
        "passage": None, "stem": q["stem"], "_ref": "screenshot:" + q.get("source", "sat1600acer"),
    }
    if q.get("image"):
        out["imageUrl"] = data_uri(q["image"])
    if q["type"] == "FR":
        out["type"] = "FREE_RESPONSE"
        out["correctAnswerFR"] = json.dumps(q["answerFR"])
    else:
        out["type"] = "MULTIPLE_CHOICE"
        out["choices"] = [{"label": LETTERS[i], "content": c, "isCorrect": LETTERS[i] == q["mine"]}
                          for i, c in enumerate(q["choices"])]
    return out


def module(key, path, conv):
    qs = sorted(json.load(open(path))["questions"], key=lambda q: q["n"])
    diffs = DIFF[key]
    assert len(qs) == len(diffs), (key, len(qs), len(diffs))
    c = Counter(diffs)
    assert (c[E], c[M], c[H]) == TARGET[key], (key, c)
    return [conv(q, d) for q, d in zip(qs, diffs)]


test = {
    "RW_M1": module("RW_M1", "rw_m1.json", rw),
    "RW_M2H": module("RW_M2H", "rw_m2_hard.json", rw),
    "MATH_M1": module("MATH_M1", "math_m1.json", math),
    "MATH_M2H": module("MATH_M2H", "math_m2_hard.json", math),
}
db = json.load(open("m2e_from_db.json"))
rw_e = list(db["RW_M2E"])
whale = next(q for q in rw_e if q["skill"] == "INI-CI" and q["test"] == "Test 23")
rw_e.remove(whale)
first_ie = next(i for i, q in enumerate(rw_e) if q["skill"] == "INI-IE")
rw_e.insert(first_ie, whale)
test["RW_M2E"] = [{"copyFrom": q["id"], "difficulty": q["difficulty"]} for q in rw_e]
test["MATH_M2E"] = [{"copyFrom": q["id"], "difficulty": q["difficulty"]} for q in db["MATH_M2E"]]
test["fixes"] = FIXES

# Every MC question has exactly one key; every FR answer is a JSON array.
for key, qs in test.items():
    if key == "fixes":
        continue
    for i, q in enumerate(qs, 1):
        if "copyFrom" in q:
            continue
        if q["type"] == "MULTIPLE_CHOICE":
            assert len(q["choices"]) == 4 and sum(c["isCorrect"] for c in q["choices"]) == 1, (key, i)
        else:
            assert isinstance(json.loads(q["correctAnswerFR"]), list), (key, i)

json.dump(test, open("special_test.json", "w"), ensure_ascii=False)
print({k: len(v) for k, v in test.items() if k != "fixes"})
