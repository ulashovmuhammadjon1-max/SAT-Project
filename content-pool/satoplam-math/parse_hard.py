# -*- coding: utf-8 -*-
"""Parse the SATashkent "Math Hard Book" into structured records.

    python3 parse_hard.py <out.json> <pdf>

A different book from Math 2.0/3.0 and a different layout: questions are
numbered `N.` on a line of their own with no exam label, and the four chapters
(Algebra, Advanced Math, Geometry, Problem Solving) each end with their own
answer sheet. Numbering restarts per chapter, so identity is (chapter, number).

── The choice-marker problem ──────────────────────────────────────────────
The book uses TWO markers, apparently from two typesetting macros:

    A) The sample sizes are too small.        ← prose choices
    A (3, 8 - 1/m)                            ← choices that are math

Accepting a bare `A ` anywhere swallows any body line opening with the ARTICLE
"A" — "A cooking school is offering a promotion…" became choice A on 63
questions, taking the whole question body with it. This is precisely the
LETTER_REF bug CLAUDE.md records ("the old pattern matched any bare A-D
followed by whitespace, which also matched the article 'A' starting a
sentence"), reintroduced here in a new file.

Two conditions together, since neither alone is enough:

  1. the letter must be the one expected next in sequence — A, then B, then
     C, then D — so a mid-body "A science class studied…" cannot match once
     the parser is already looking for B;
  2. what follows must LOOK like mathematics, because the bare marker is only
     ever used for maths in this book; prose choices always carry the `A)`
     form. An article is followed by ordinary words and fails this.

Condition 1 alone let all 63 through, because the article usually appears in
the first body line, exactly when the parser is still expecting A.
"""
import json
import re
import subprocess
import sys
from collections import Counter

CHAPTERS = ["Algebra", "Advanced Math", "Geometry", "Problem Solving"]
DOMAIN_OF = {"Algebra": "ALG", "Advanced Math": "ADV",
             "Geometry": "GT", "Problem Solving": "PSDA"}
SKILL_OF = {"Algebra": "ALG-LE", "Advanced Math": "ADV-NF",
            "Geometry": "GT-AV", "Problem Solving": "PSDA-RP"}

Q_START = re.compile(r"^(\d+)\.$")
PAREN_CHOICE = re.compile(r"^([A-D])\)\s*(.*)$")
BARE_CHOICE = re.compile(r"^([A-D])\s+(\S.*)$")
# A relation, an operator, or an opening that only a mathematical expression
# has. Deliberately conservative: a hyphen is excluded because prose is full
# of them ("14- to 15-year-old"), and prose choices never need this form.
LOOKS_MATHS = re.compile(r"[=+/^√π]|^[(\[]|^-?\d|^[a-z]\s*[(=]")
KEY_ROW = re.compile(r"^(\d+)\s+(\S+)(?:\s+(\d+)\s+(\S+))?\s*$")
ANS_HDR = re.compile(r"^(?:Answers:\s*(.+)|(.+?)\s+Answers)\s*$")


def main():
    out, pdf = sys.argv[1], sys.argv[2]
    n = int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
            .stdout.split("Pages:")[1].split()[0])

    qs, keys = [], {}
    chapter, cur, mode, key_chap = None, None, "q", None
    for i in range(1, n + 1):
        text = subprocess.run(["pdftotext", "-raw", "-f", str(i), "-l", str(i), pdf, "-"],
                              capture_output=True, text=True).stdout.replace("\f", "")
        for raw in text.split("\n"):
            s = raw.strip()
            if not s:
                continue
            m = ANS_HDR.match(s)
            if m and (m.group(1) or m.group(2)) in CHAPTERS:
                if cur:
                    qs.append(cur); cur = None
                mode, key_chap = "key", (m.group(1) or m.group(2))
                continue
            if s in CHAPTERS:
                if cur:
                    qs.append(cur); cur = None
                chapter, mode = s, "q"
                continue
            if mode == "key":
                if s.startswith("Number Answer"):
                    continue
                m = KEY_ROW.match(s)
                if m:
                    keys[(key_chap, int(m.group(1)))] = m.group(2)
                    if m.group(3):
                        keys[(key_chap, int(m.group(3)))] = m.group(4)
                continue
            m = Q_START.match(s)
            if m:
                if cur:
                    qs.append(cur)
                cur = {"chapter": chapter, "num": int(m.group(1)),
                       "page": i, "body": [], "choices": []}
                continue
            if cur is None:
                continue
            nxt = "ABCD"[len(cur["choices"])] if len(cur["choices"]) < 4 else None
            m = PAREN_CHOICE.match(s)
            if m and m.group(1) == nxt:
                cur["choices"].append({"label": m.group(1), "content": m.group(2)})
                continue
            m = BARE_CHOICE.match(s)
            if m and m.group(1) == nxt and LOOKS_MATHS.search(m.group(2)):
                cur["choices"].append({"label": m.group(1), "content": m.group(2)})
                continue
            if cur["choices"]:
                cur["choices"][-1]["content"] += " " + s
            else:
                cur["body"].append(s)
    if cur:
        qs.append(cur)

    recs = []
    for q in qs:
        if not q["chapter"]:
            continue
        _k, _ch = keys.get((q["chapter"], q["num"])), q["choices"]
        body = "\n".join(q["body"]).strip()
        joined = body + "\n" + "\n".join(c["content"] for c in q["choices"])
        lines = [l.strip() for l in joined.split("\n") if l.strip()]
        shredded = (any(re.fullmatch(r"[0-9]{1,2}|[a-z]|[+\-−=]", l) for l in lines[1:])
                    or bool(re.search(r"(?<=[a-zA-Z])\d(?![\d.,])", joined)))
        # The book's own key settles the question type, and where the parsed
        # choices disagree with it the extraction failed rather than the key
        # being wrong: TeX regularly collapses all four choices onto one line,
        # or strands a choice letter beside a fraction numerator. Either way a
        # person has to read it, so it joins the transcribe pile.
        key_disagrees = bool(_k) and (
            (_k in ("A", "B", "C", "D")) != (len(_ch) == 4))
        recs.append({
            "id": f"sathard-{q['chapter'].lower().replace(' ', '-')}-{q['num']}",
            "book": "hard", "topic": q["chapter"], "num": q["num"], "page": q["page"],
            "domain": DOMAIN_OF[q["chapter"]], "skill": SKILL_OF[q["chapter"]],
            "difficulty": "HARD",          # the whole book is curated hard questions
            "body": body, "choices": q["choices"],
            "type": "MULTIPLE_CHOICE" if len(q["choices"]) == 4 else "FREE_RESPONSE",
            "key": keys.get((q["chapter"], q["num"])),
            "needs_vision": shredded or key_disagrees,
        })

    print(f"questions          {len(recs)}")
    print(f"  with an answer   {sum(1 for r in recs if r['key'])}")
    print(f"  multiple choice  {sum(1 for r in recs if r['type']=='MULTIPLE_CHOICE')}")
    print(f"  free response    {sum(1 for r in recs if r['type']=='FREE_RESPONSE')}")
    print(f"  math survived    {sum(1 for r in recs if not r['needs_vision'])}")
    print(f"  needs transcribe {sum(1 for r in recs if r['needs_vision'])}")
    print(f"  empty body       {sum(1 for r in recs if not r['body'])}")
    print("\nby chapter:")
    for c in CHAPTERS:
        sel = [r for r in recs if r["topic"] == c]
        print(f"  {c:<18} {len(sel):>4}   keyed {sum(1 for r in sel if r['key']):>4}"
              f"   needs-transcribe {sum(1 for r in sel if r['needs_vision']):>4}")
    json.dump(recs, open(out, "w"), indent=1)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
