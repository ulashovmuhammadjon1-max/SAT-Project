# -*- coding: utf-8 -*-
"""Plan replacements for duplicate questions a single student can meet twice.

    python3 plan_dupe_fix.py                 # report
    python3 plan_dupe_fix.py --write         # also write dupe_plan.json

Reads rw_state.json (the live Tests 16-31 R&W snapshot) and bank_merged.json.

── What counts as a collision ─────────────────────────────────────────────
Not every same-test pair. A student sits Module 1 and then exactly ONE
Module 2 branch, so:

    M1  ↔ M1     collision     (same module)
    M1  ↔ M2E    collision     (every Easy-branch student)
    M1  ↔ M2H    collision     (every Hard-branch student)
    M2E ↔ M2E    collision
    M2H ↔ M2H    collision
    M2E ↔ M2H    NOT a collision — no student sits both branches

The first scan counted M2E↔M2H pairs as same-test duplicates. They are a
content-reuse smell, but no student is ever shown both, so replacing them
would churn live questions for no student-visible gain.

── Which side gets replaced ───────────────────────────────────────────────
The Module 1 copy stays, because every student sees Module 1 and the branch
copy is only seen by half the cohort — replacing the branch copy disturbs
fewer students' experience. Within one module, the later question goes.

── "1.5x harder" ──────────────────────────────────────────────────────────
The user asked for replacements 1.5x harder than what they replace. Read as
one difficulty tier up, since one tier is the smallest real step and two
(EASY→HARD) would be nearer 2x:

    EASY → MEDIUM      MEDIUM → HARD      HARD → HARD

This does move each module off the mandated difficulty mix in CLAUDE.md by
however many questions are replaced there. That is the user's explicit
instruction and it is reported per module so the drift is visible, not
silent.

── Screening the replacement ──────────────────────────────────────────────
Same skill, one tier harder, never already used anywhere in the database, and
scored against every other question in the SAME test — including replacements
chosen earlier in this run. A candidate at or above REJECT is refused outright, and REJECT sits below
COLLIDE on purpose — a replacement must not be allowed to land just under the
line used to find the duplicate. CLAUDE.md's standing rule is that the score
decides what to READ, so anything from READ_ME up is printed for a human.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_rw_tests import split_passage_stem, skill_key  # noqa: E402

# The reject line for an incoming question must be STRICTER than the detect
# line for an existing one. At 0.40 the planner picked, as the replacement for
# one Hawai'i Register of Historic Places question, a third Hawai'i Register
# question scoring 0.25 against the copy being kept — just under the 0.26
# duplicate line, i.e. it would have inserted exactly the kind of pair it was
# sent to remove. 0.20 leaves margin below that line.
REJECT = 0.20      # never take a candidate at or above this
READ_ME = 0.15     # print anything this close for a human to check
# What counts as a duplicate. 0.60 was the first guess and it under-caught:
# every co-visible pair down to 0.35 turned out, on reading, to be a genuine
# template repeat — the same Navajo Nation chapter frame with a different
# chapter, the same Aubrey/Maturin novel frame with a different novel, the
# same conjecture-proved-by-a-mathematician frame with different names. A
# template repeat swaps the setting words, so it scores LOW precisely because
# it changed the words, which is why the number can only ever decide what to
# read. Every co-visible pair from 0.26 up was read by hand before this was
# set, and all of them were real: the same Navajo Nation chapter frame, the
# same Aubrey/Maturin novel frame, the same Chelsea Wood parasite study, Sei
# Shonagon's Pillow Book twice in one test. Below 0.26 the pairs stop being
# repeats and are merely on similar topics.
COLLIDE = 0.26

STOP = set("the a an and or of to in is are was were that this it for on as with by "
           "from at be been which what how not but their its his her they them".split())
NEXT_TIER = {"EASY": "MEDIUM", "MEDIUM": "HARD", "HARD": "HARD"}
SKILL_CODE = {
    "Central Ideas and Details": "INI-CI", "Inferences": "INI-IE",
    "Command of Evidence": "INI-CE", "Words in Context": "CAS-WV",
    "Text Structure and Purpose": "CAS-TS", "Cross-Text Connections": "CAS-CT",
    "Rhetorical Synthesis": "EOI-RS", "Transitions": "EOI-TR",
    "Boundaries": "SEC-BS", "Form, Structure, and Sense": "SEC-FS",
}


# Phrases every question of a given type carries. They are not content, and
# leaving them in makes two unrelated questions of the same type look alike:
# a Rhetorical Synthesis pair about Philippine capitals and one about
# strawberries scored 0.36 purely on this frame, while genuine repeats sat at
# the same number. Stripping them separates the two cases instead of forcing a
# threshold to do it.
BOILERPLATE = re.compile(
    r"while researching a topic,? a student has taken the following notes:?"
    r"|which choice most effectively uses relevant (information|data) from the notes"
    r" to accomplish this goal\??"
    r"|which choice completes the text with the most logical and precise word or phrase\??"
    r"|which choice completes the text so that it conforms to the conventions of"
    r" standard english\??"
    r"|which choice best (describes|states) the main (purpose|idea) of the text\??",
    re.I)


FIGURE_REF = re.compile(r"\b(table|graph|figure|chart|plot)\b", re.I)


def sig(text):
    flat = BOILERPLATE.sub(" ", re.sub(r"<[^>]+>", " ", text or "").lower())
    return {w for w in re.findall(r"[a-z]{3,}", flat) if w not in STOP}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    return inter / (len(a) + len(b) - inter)


def covisible(x, y):
    """Can one student be shown both of these?"""
    if x["m_order"] == y["m_order"] and x["branch"] == y["branch"]:
        return True
    m1, m2 = sorted([x, y], key=lambda r: r["m_order"])
    return m1["m_order"] == 1 and m2["m_order"] == 2


def main():
    live = json.load(open(os.path.join(HERE, "rw_state.json")))
    bank = json.load(open(os.path.join(HERE, "bank_merged.json")))
    used = set(json.load(open(os.path.join(
        "/tmp/claude-0/-home-user-SAT-Project/16335d00-5283-5db6-a7a3-023a1a5fae45/"
        "scratchpad/used_sources.json"))))

    for q in live:
        q["sig"] = sig((q.get("passage") or "") + " " + q["stem"])

    by_test = {}
    for q in live:
        by_test.setdefault(q["test"], []).append(q)

    # The same source question inserted into two different tests. No student
    # meets both, so it is milder than a co-visible duplicate, but it is still
    # one question doing two jobs — and every instance of it here was created
    # by running this planner twice against a `used` snapshot taken before the
    # first run applied. Refreshing that snapshot between runs is the real fix;
    # this catches whatever slipped through. The later test keeps its slot's
    # difficulty rather than being bumped again, because it was already set to
    # the intended tier when it was inserted.
    # Questions named explicitly for replacement. These are the ones the
    # explanation agents found by READING — a goal sentence pasted from another
    # question, a choice that is the literal string "None of the above", a
    # passage that contradicts itself because a decimal comma turned 1,408 m
    # into 14,08. No pattern finds these; a person has to notice them. They
    # cannot be repaired from the database because the missing text only exists
    # in the source books, so they are swapped out for sound questions instead.
    forced = {}
    fpath = os.path.join(HERE, "force_replace.json")
    if os.path.exists(fpath):
        forced = {f["id"]: f["why"] for f in json.load(open(fpath))}

    seen_src, dup_src = {}, set()
    for q in sorted(live, key=lambda r: (int(re.sub(r"\D", "", r["test"])), r["m_order"])):
        if q["source"] in seen_src:
            dup_src.add(q["id"])
        else:
            seen_src[q["source"]] = q["id"]
    if dup_src:
        print(f"{len(dup_src)} question(s) reuse a source already live in another test\n")

    # Free pool: never inserted anywhere, R&W, has choices, has a real stem.
    def src_of(b):
        return ("SAT:" if b.get("source_book") else "CB:") + str(b["id"])

    pool = []
    for b in bank:
        if b.get("error") or b.get("subject") != "Reading and Writing":
            continue
        if src_of(b) in used or b.get("needs_figure"):
            continue
        if len(b.get("choices") or []) != 4 or not b.get("correct"):
            continue
        passage, stem = split_passage_stem(b.get("question") or "")
        if not stem or not passage:
            continue
        # A bank question can be perfectly well formed and still unanswerable
        # once stored, because the thing it points at did not survive the
        # transcription. `needs_figure` only flags the ones whose text came out
        # visibly shredded; these two are the quiet cases.
        #   - "uses data from the table" with no <table> and no <img>: the
        #     table is in the source PDF as a drawn object, not in the text.
        #   - "the underlined portion" with no <u>: the span was underlined on
        #     the page and underlining is not carried by extracted text.
        # Three figure questions and two underline questions were inserted
        # before these filters existed, and every one is unanswerable.
        body = passage + " " + stem
        if FIGURE_REF.search(stem) and "<table" not in body and "<img" not in body:
            continue
        if "underlined" in stem.lower() and "<u>" not in body:
            continue
        b["_src"], b["_passage"], b["_stem"] = src_of(b), passage, stem
        b["_sig"] = sig(b["question"])
        pool.append(b)

    by_skill_diff = {}
    for b in pool:
        by_skill_diff.setdefault((b["skill"], b.get("difficulty")), []).append(b)

    print(f"live {len(live)} questions | free pool {len(pool)} usable\n")

    plan, notes = [], []
    total_pairs = 0
    for test, qs in sorted(by_test.items(), key=lambda kv: int(re.sub(r"\D", "", kv[0]))):
        pairs = []
        for i in range(len(qs)):
            for j in range(i + 1, len(qs)):
                if not covisible(qs[i], qs[j]):
                    continue
                s = jaccard(qs[i]["sig"], qs[j]["sig"])
                if s >= COLLIDE:
                    pairs.append((s, qs[i], qs[j]))
        total_pairs += len(pairs)

        # Victims: keep Module 1, drop the branch copy; within a module drop the later.
        victims = {}
        for s, a, b in sorted(pairs, key=lambda p: -p[0]):
            if a["id"] in victims or b["id"] in victims:
                continue
            if a["m_order"] != b["m_order"]:
                v = a if a["m_order"] == 2 else b
            else:
                v = a if a["q_order"] > b["q_order"] else b
            victims[v["id"]] = (s, v, a if v is b else b)

        # A question already live that trips the same two filters is itself
        # unanswerable and gets replaced whether or not it duplicates anything.
        for q in qs:
            if q["id"] in victims:
                continue
            body = (q.get("passage") or "") + " " + q["stem"]
            broken = ((FIGURE_REF.search(q["stem"]) and "<table" not in body
                       and "<img" not in body)
                      or ("underlined" in q["stem"].lower() and "<u>" not in body))
            if broken or q["id"] in dup_src or q["id"] in forced:
                victims[q["id"]] = (0.0, q, None)

        # Nothing wrong with this test — checked only after the defect scan, so
        # a test with no duplicates but a broken question still gets looked at.
        if not victims:
            continue
        print(f"{test}: {len(pairs)} colliding pair(s), {len(victims)} to replace")
        for s, v, kept in victims.values():
            want_skill = v["skill_name"]
            want_diff = (v["difficulty"] if v["id"] in dup_src
                         else NEXT_TIER[v["difficulty"]])
            if v["id"] in forced:
                notes.append(f"  replaced {v['test']} M{v['m_order']}{v['branch']} "
                             f"q{v['q_order']}: {forced[v['id']]}")
            cands = by_skill_diff.get((want_skill, want_diff), [])
            # Some cells are genuinely empty — Rhetorical Synthesis/HARD has
            # nothing left unused. The books leave a further tranche of
            # questions unlabelled, so fall back to those rather than silently
            # dropping the tier and shipping something easier. An unlabelled
            # pick carries `judge_difficulty`, because "harder" is the whole
            # point of the replacement and an unlabelled question has not been
            # shown to be harder by anything.
            fallback = False
            if not cands:
                cands = by_skill_diff.get((want_skill, None), [])
                fallback = bool(cands)
            others = [q for q in qs if q["id"] != v["id"]]
            chosen, best_seen = None, []
            for c in sorted(cands, key=lambda b: -len(b["_sig"])):
                worst = max((jaccard(c["_sig"], o["sig"]) for o in others), default=0.0)
                worst = max([worst] + [jaccard(c["_sig"], p["cand"]["_sig"])
                                       for p in plan if p["test"] == test])
                best_seen.append((worst, c))
                if worst < REJECT:
                    chosen = c
                    break
            if not chosen:
                notes.append(f"  !! {test} M{v['m_order']}{v['branch']} q{v['q_order']}: "
                             f"no {want_skill}/{want_diff} candidate below {REJECT}")
                continue
            worst = min(w for w, _ in best_seen if _ is chosen)
            flag = "  <-- read this one" if worst >= READ_ME else ""
            if fallback:
                flag += "  [unlabelled — judge difficulty by hand]"
            print(f"   q{v['q_order']:>2} {v['branch']:<8} {want_skill[:26]:<26} "
                  f"{v['difficulty']}→{want_diff}  overlap {worst:.2f}{flag}")
            plan.append({
                "test": test, "module_id": v["module_id"], "m_order": v["m_order"],
                "branch": v["branch"], "q_order": v["q_order"],
                "retire_id": v["id"], "retire_source": v["source"],
                "kept_id": kept["id"] if kept else None, "pair_score": round(s, 3),
                "skill_name": want_skill, "skill_code": SKILL_CODE[want_skill],
                "difficulty": want_diff, "was_difficulty": v["difficulty"],
                "overlap": round(worst, 3),
                "judge_difficulty": fallback,
                "cand": chosen,
            })
            # A chosen candidate must not be offered again.
            key = (want_skill, None) if fallback else (want_skill, want_diff)
            by_skill_diff[key] = [b for b in by_skill_diff.get(key, [])
                                  if b["_src"] != chosen["_src"]]

    print(f"\n{total_pairs} colliding pairs, {len(plan)} replacements planned")
    for n in notes:
        print(n)

    drift = {}
    for p in plan:
        k = f"{p['test']} M{p['m_order']}{p['branch']}"
        drift.setdefault(k, []).append(f"{p['was_difficulty'][0]}→{p['difficulty'][0]}")
    print("\ndifficulty drift against the mandated mix:")
    for k, v in sorted(drift.items()):
        print(f"  {k:<22} {', '.join(v)}")

    if "--write" in sys.argv:
        out = os.path.join(HERE, "dupe_plan.json")
        slim = []
        for p in plan:
            c = p["cand"]
            slim.append({**{k: v for k, v in p.items() if k != "cand"},
                         "new_source": c["_src"], "passage": c["_passage"],
                         "stem": c["_stem"], "choices": c["choices"],
                         "correct": c["correct"], "rationale": c.get("rationale", "")})
        json.dump(slim, open(out, "w"), indent=1)
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
