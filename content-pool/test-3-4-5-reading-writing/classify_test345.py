# -*- coding: utf-8 -*-
"""Classifies the reserved R&W-only content for Test 3, 4, 5 (indices 2, 3, 4
in final_allocation_5tests.json) using the same classifier used for Test 1
and Test 2 (already fixed for the "given sentences" Rhetorical Synthesis
phrasing). No Math content exists for these yet -- R&W only, saved as DRAFT
tests so the content isn't lost when the session's scratchpad goes away.
"""
import json
import re

from classify_test1 import classify_rw, strip_diagram_note

TEST_INDEX = {"test3": 2, "test4": 3, "test5": 4}

# classify_rw's Boundaries detector needs literal words like "comma"/
# "semicolon" in the stem, which real SAT Boundaries questions never contain
# -- the actual signal is the answer choices' punctuation (same root cause
# already documented for Test 1 and Test 2). Every SEC question here was
# reviewed by hand against its choices; Boundaries = choices differ by
# clause-joining punctuation/conjunction (comma/semicolon/colon/period/
# dash/"and"), Form/Structure/Sense = choices differ by verb form/tense,
# pronoun, or full-sentence restructuring for clarity. Keyed by (module key,
# 0-based index in that module's classified list).
SEC_OVERRIDE = {
    ("test3|RW_M1", 15): "Boundaries",
    ("test3|RW_M1", 16): "Boundaries",
    ("test3|RW_M1", 18): "Boundaries",
    ("test3|RW_M1", 19): "Boundaries",
    ("test3|RW_M1", 20): "Boundaries",
    ("test3|RW_M2_EASY", 18): "Boundaries",
    ("test3|RW_M2_EASY", 19): "Boundaries",
    ("test3|RW_M2_EASY", 20): "Boundaries",
    ("test3|RW_M2_HARD", 17): "Boundaries",
    ("test3|RW_M2_HARD", 20): "Boundaries",
    ("test4|RW_M1", 16): "Boundaries",
    ("test4|RW_M1", 17): "Boundaries",
    ("test4|RW_M1", 19): "Boundaries",
    ("test4|RW_M1", 20): "Boundaries",
    ("test4|RW_M2_EASY", 17): "Boundaries",
    ("test4|RW_M2_EASY", 18): "Boundaries",
    ("test4|RW_M2_EASY", 19): "Boundaries",
    ("test4|RW_M2_EASY", 20): "Boundaries",
    ("test4|RW_M2_HARD", 15): "Boundaries",
    ("test4|RW_M2_HARD", 17): "Boundaries",
    ("test4|RW_M2_HARD", 18): "Boundaries",
    ("test4|RW_M2_HARD", 20): "Boundaries",
    ("test5|RW_M1", 15): "Boundaries",
    ("test5|RW_M1", 16): "Boundaries",
    ("test5|RW_M1", 17): "Boundaries",
    ("test5|RW_M2_EASY", 13): "Boundaries",
    ("test5|RW_M2_EASY", 14): "Boundaries",
    ("test5|RW_M2_EASY", 15): "Boundaries",
    ("test5|RW_M2_EASY", 16): "Boundaries",
    ("test5|RW_M2_EASY", 17): "Boundaries",
    ("test5|RW_M2_HARD", 15): "Boundaries",
    ("test5|RW_M2_HARD", 16): "Boundaries",
    ("test5|RW_M2_HARD", 18): "Boundaries",
    ("test5|RW_M2_HARD", 20): "Boundaries",
}


def main():
    alloc = json.load(open("/tmp/claude-0/-home-user-SAT-Project/16335d00-5283-5db6-a7a3-023a1a5fae45/scratchpad/batch2/pool/final_allocation_5tests.json"))
    out = {}
    for name, idx in TEST_INDEX.items():
        for rt in ["RW_M1", "RW_M2_EASY", "RW_M2_HARD"]:
            key = f"{idx}|{rt}"
            out_key = f"{name}|{rt}"
            items = alloc[key]
            classified = []
            for i, q in enumerate(items):
                qc = dict(q)
                qc["stem"] = strip_diagram_note(qc.get("stem", ""))
                qc["passage"] = strip_diagram_note(qc.get("passage", ""))
                domain, skill = classify_rw(qc["passage"], qc["stem"])
                override = SEC_OVERRIDE.get((out_key, i))
                if override:
                    assert domain == "Standard English Conventions", (out_key, i, domain)
                    skill = override
                qc["domain"] = domain
                qc["skill"] = skill
                classified.append(qc)
            out[out_key] = classified

    json.dump(
        out,
        open("/tmp/claude-0/-home-user-SAT-Project/16335d00-5283-5db6-a7a3-023a1a5fae45/scratchpad/batch2/pool/test345_classified.json", "w"),
        indent=2,
    )

    for key, items in out.items():
        counts = {}
        for q in items:
            k = f"{q['domain']} / {q['skill']}"
            counts[k] = counts.get(k, 0) + 1
        print(f"\n=== {key} ({len(items)}) ===")
        for k, c in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {c:3d}  {k}")


if __name__ == "__main__":
    main()
