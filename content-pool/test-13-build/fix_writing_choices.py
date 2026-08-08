#!/usr/bin/env python3
"""
Repair writing-domain answer choices that render as bare punctuation.

The defect: Boundaries items were authored with the punctuation alone as the
choice — ", " / "; " / ": " / " and " — so the student sees four all-but-empty
options and cannot tell what any of them would do to the sentence. The real
test never does this. It repeats the words on either side of the blank inside
every option, so the choice reads as the sentence would read:

    ... plotting soundings by hand _____ the result was the first map ...
        A  hand; the result          C  hand the result
        B  hand, the result          D  hand: and the result

This rewrites every choice of an affected question as
`<words before the blank><choice><words after the blank>`, taking the context
straight from the question's own passage so the option is always a faithful
rendering of the resulting sentence.

Only questions where at least one choice contains no letters at all are
touched. A Form/Structure item whose options are "was" / "were" / "has been"
is already readable on its own and is left alone — that is also how the real
test presents those.

    python3 fix_writing_choices.py rw_test8.py [--write]
"""
import io
import json
import re
import sys

BLANK = "_____"


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def words_before(text, n=2):
    plain = strip_tags(text).replace("&nbsp;", " ")
    parts = plain.split()
    return " ".join(parts[-n:]) if parts else ""


def words_after(text, n=3):
    plain = strip_tags(text).replace("&nbsp;", " ")
    parts = plain.split()
    return " ".join(parts[:n]) if parts else ""


def needs_fix(q):
    return any(not re.search(r"[A-Za-z]", c) for c in q["choices"])


def splice(passage, choice):
    """Render the sentence fragment this choice would produce."""
    left, _, right = passage.partition(BLANK)
    before = words_before(left)
    after = words_after(right)
    # Most choices carry their own trailing space (", " / "; "), but some do
    # not (": and"), which would run straight into the following word.
    sep = "" if (not choice or choice[-1].isspace()) else " "
    joined = f"{before}{choice}{sep}{after}"
    return re.sub(r"\s+", " ", joined).strip()


def repair(questions):
    """Return (questions with spliced choices, count repaired, skipped ids)."""
    out, fixed, skipped = [], 0, []
    for q in questions:
        q = dict(q)
        if needs_fix(q):
            if BLANK not in (q.get("passage") or ""):
                skipped.append(f"{q['num']}: no blank in passage")
            else:
                new = [splice(q["passage"], c) for c in q["choices"]]
                if len(set(new)) != 4:
                    skipped.append(f"{q['num']}: options collapse to {len(set(new))}")
                else:
                    q["choices"] = new
                    fixed += 1
        out.append(q)
    return out, fixed, skipped


def main():
    path = sys.argv[1]
    mod = path[:-3].split("/")[-1]
    sys.path.insert(0, ".")
    questions = __import__(mod).QUESTIONS

    out, fixed, skipped = repair(questions)
    for q, o in list(zip(out, questions))[:200]:
        if q["choices"] != o["choices"] and fixed and q["num"] in (out[0]["num"], "B1", "B5"):
            print(f"  {q['num']}: {o['choices']}")
            print(f"      -> {q['choices']}")
    for s_ in skipped:
        print("  !!", s_)

    # the key must still point at the same option position
    for a, b in zip(questions, out):
        assert a["answer"] == b["answer"], a["num"]

    dest = f"{mod}_repaired.json"
    with io.open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    print(f"\n{fixed} questions repaired -> {dest}")


if __name__ == "__main__":
    main()
