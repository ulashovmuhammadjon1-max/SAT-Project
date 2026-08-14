"""
Merge the SAToplam Reading book into the College Board bank file.

Both sources claim to be real SAT questions, so they overlap — but the
overlap turns out to be small, and where it exists the College Board copy is
strictly better (official key, official rationale, official difficulty).
So College Board wins every collision and SAToplam contributes only what
College Board does not have.

    python3 merge_into_bank.py <cb_bank.json> <satoplam.json> <out.json>

Matching is on normalised passage + stem, with editorial square brackets
stripped first. Two things learned the hard way here:

- **Never compare answer LETTERS across sources.** Of 39 overlapping questions
  whose correct-choice text is identical, 19 carry a different letter, because
  the two books order the choices differently. Comparing letters reported a 50%
  "key disagreement" rate that was almost entirely an artefact. Correctness has
  to be compared on the text of the credited choice.
- **Requiring the stem to match as well as the passage.** Several SAT passages
  are near-identical templates about different subjects, and a passage-only key
  pairs unrelated questions.

SAToplam carries no difficulty label, which matters: the whole point of the
rebuild is a per-module difficulty mix. Its questions are therefore imported
with `difficulty: null` and cannot fill a difficulty quota until labelled.
"""
import json
import re
import sys

TOPIC_TO_SKILL = {
    "Main Ideas": ("Information and Ideas", "Central Ideas and Details"),
    "Details Question": ("Information and Ideas", "Central Ideas and Details"),
    "Inference": ("Information and Ideas", "Inferences"),
    "Command of Evidence - Support": ("Information and Ideas", "Command of Evidence"),
    "Command of Evidence - Weaken": ("Information and Ideas", "Command of Evidence"),
    "Quotation": ("Information and Ideas", "Command of Evidence"),
    "Command of Evidence - Graphs": ("Information and Ideas", "Command of Evidence"),
    "Main Purpose": ("Craft and Structure", "Text Structure and Purpose"),
    "Central Purpose": ("Craft and Structure", "Text Structure and Purpose"),
    "Overall Structure": ("Craft and Structure", "Text Structure and Purpose"),
    "Underlined Purpose": ("Craft and Structure", "Text Structure and Purpose"),
    "Cross-Text Connection": ("Craft and Structure", "Cross-Text Connections"),
    "Cross-Text Connections": ("Craft and Structure", "Cross-Text Connections"),
    "Words in Context - Gap Filling": ("Craft and Structure", "Words in Context"),
    "Words in Contenxt — Synonyms": ("Craft and Structure", "Words in Context"),
    "Words in Context — Synonyms": ("Craft and Structure", "Words in Context"),
}


def norm(s):
    s = (s or "").replace("’", "'").replace("“", '"').replace("”", '"').replace("—", "-")
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def main():
    cb_path, sat_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    cb = json.load(open(cb_path))
    sat = json.load(open(sat_path))
    live = [q for q in cb if "error" not in q]

    by_passage = {}
    for q in live:
        by_passage.setdefault(norm(q["question"])[:150], []).append(q)

    kept, dropped, reordered, conflicts = [], 0, 0, []
    for q in sat:
        cand = by_passage.get(norm(q["passage"] + " " + q["question"])[:150], []) \
            or by_passage.get(norm(q["passage"])[:150], [])
        stem = norm(q["question"])
        match = next((m for m in cand if stem[:70] and stem[:70] in norm(m["question"])), None)
        if match:
            dropped += 1
            s_txt = next((norm(c["content"]) for c in q["choices"] if c["label"] == q["correct"]), "")
            m_txt = next((norm(c["content"]) for c in match["choices"] if c["label"] == match["correct"]), "")
            if s_txt[:60] == m_txt[:60]:
                if q["correct"] != match["correct"]:
                    reordered += 1
            else:
                conflicts.append({"cb_id": match["id"], "satoplam_topic": q["topic"],
                                  "satoplam_number": q["number"],
                                  "satoplam_says": s_txt[:160], "college_board_says": m_txt[:160]})
            continue

        domain, skill = TOPIC_TO_SKILL.get(q["topic"], (None, None))
        if not skill:
            continue
        kept.append({
            "id": f"satoplam-{re.sub(r'[^a-z0-9]+', '-', q['topic'].lower())}-{q['number']}",
            "source_book": "SAToplam 2.0 (@satashkent)",
            "subject": "Reading and Writing",
            "domain": domain,
            "skill": skill,
            # No difficulty label in this book — it cannot fill a difficulty
            # quota until one is assigned.
            "difficulty": None,
            "question": (q["passage"] + " " + q["question"]).strip(),
            "choices": q["choices"],
            "correct": q["correct"],
            # No rationale in this book either.
            "rationale": "",
            "needs_figure": False,
            "already_in_bank": False,
            "key_is_transcribed": True,
            "bracketed_text": q["bracketed_text"],
        })

    print(f"SAToplam questions           {len(sat)}")
    print(f"  already in the CB export   {dropped}")
    print(f"    of those, choices reordered so the letter differs: {reordered}")
    print(f"    of those, a real answer conflict:                  {len(conflicts)}")
    print(f"  contributed as new         {len(kept)}")
    print(f"  ... carrying bracketed editorial text: {sum(1 for q in kept if q['bracketed_text'])}")

    merged = cb + kept
    json.dump(merged, open(out_path, "w"), indent=1)
    if conflicts:
        json.dump(conflicts, open("content-pool/satoplam/key_conflicts.json", "w"), indent=1)
        print("  wrote content-pool/satoplam/key_conflicts.json")
    print(f"\nmerged total {len(merged)}  -> {out_path}")


if __name__ == "__main__":
    main()
