#!/usr/bin/env python3
"""
Assemble Test 5's three Reading & Writing modules.

Takes the formatted banked content (test5_rw_formatted.json) plus the verified
top-ups (rw_topups.json), fills each module to 27, and orders every module by
the mandatory domain-block sequence in CLAUDE.md.

The ordering rule is the important one: no reading-domain question may appear
after the writing block has started. Sorting by the block rank enforces that
by construction rather than by inspection.

Run:  python3 assemble_rw.py
Out:  test5_rw.json
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

# The mandated block order. Index is the sort key; 0-5 are reading, 6-9 writing.
BLOCK_ORDER = [
    "Words in Context",             # 0
    "Text Structure and Purpose",   # 1
    "Cross-Text Connections",       # 2
    "Central Ideas and Details",    # 3
    "Command of Evidence",          # 4
    "Inferences",                   # 5  <- always the last reading block
    "Boundaries",                   # 6
    "Form, Structure, and Sense",   # 7
    "Transitions",                  # 8
    "Rhetorical Synthesis",         # 9  <- always last
]
RANK = {s: i for i, s in enumerate(BLOCK_ORDER)}
FIRST_WRITING = 6

# Domain code lookup (Domain/Skill are resolved by `code` at insert time).
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

# How many top-ups each module needs to reach 27.
NEED = {"test5|RW_M1": 4, "test5|RW_M2_EASY": 6, "test5|RW_M2_HARD": 1}


def main():
    banked = json.load(open(os.path.join(HERE, "test5_rw_formatted.json")))
    topups = json.load(open(os.path.join(HERE, "rw_topups.json")))["accepted"]

    # Hand out top-ups in order; they are all writing-domain, which is exactly
    # what the three modules are short of.
    cursor = 0
    modules = {}
    for mod, want in NEED.items():
        take = topups[cursor:cursor + want]
        cursor += want
        pool = list(banked[mod]) + [
            {
                "source": t["source"],
                "sourceNum": t["num"],
                "type": t["type"],
                "passageHtml": t["passage"] if t["passage"].startswith("<")
                               else f"<p>{t['passage']}</p>",
                "stem": t["stem"],
                "choices": t["choices"],
                "correct": t["correct"],
                "domain": t["domain"],
                "skill": t["skill"],
                "diagramNote": "",
            }
            for t in take
        ]
        # Stable sort by block rank: preserves the existing relative order
        # inside each block while making the block sequence monotonic.
        pool.sort(key=lambda q: RANK[q["skill"]])
        for i, q in enumerate(pool):
            q["order"] = i + 1
            q["domainCode"], q["skillCode"] = SKILL_CODE[q["skill"]]
        modules[mod] = pool

    assert cursor == len(topups), f"used {cursor} of {len(topups)} top-ups"

    ok = True
    for mod, qs in modules.items():
        ranks = [RANK[q["skill"]] for q in qs]
        mono = all(ranks[i] <= ranks[i + 1] for i in range(len(ranks) - 1))
        first_w = next((i for i, r in enumerate(ranks) if r >= FIRST_WRITING), len(ranks))
        leak = [i for i, r in enumerate(ranks) if r < FIRST_WRITING and i > first_w]
        reading = sum(1 for r in ranks if r < FIRST_WRITING)
        good = len(qs) == 27 and mono and not leak and reading <= 15
        ok &= good
        print(f"{mod:22} n={len(qs)} reading={reading} writing={len(qs)-reading} "
              f"monotonic={mono} leak={leak or 'none'} {'OK' if good else 'FAIL'}")
        print(f"    {dict(Counter(q['skill'] for q in qs))}")

    with open(os.path.join(HERE, "test5_rw.json"), "w") as fh:
        json.dump(modules, fh, indent=1)
    print("\nwrote test5_rw.json;", "all modules valid" if ok else "VALIDATION FAILED")


if __name__ == "__main__":
    main()
