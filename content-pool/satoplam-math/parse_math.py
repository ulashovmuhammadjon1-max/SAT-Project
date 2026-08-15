# -*- coding: utf-8 -*-
"""Parse the SAToplam Math 2.0 book into structured records.

    python3 parse_math.py <out.json> <book>=<pdf> [<book>=<pdf> …]

`book` tags which edition a file belongs to. Numbering restarts per topic
*within a book*, so (book, topic, number) is the identity — two editions both
have a "Quadratics 1" and they are different questions.

The book is TeX-typeset, and that is the whole difficulty. `pdftotext` gives
back reliable STRUCTURE — question numbers, exam labels, choice markers, topic
headings, answer tables — but unreliable MATH: an exponent lands on its own
line, so `x^2 + y^2` extracts as "x2" / "+ y2", and a fraction's numerator and
denominator become two separate lines with the rule dropped entirely.

So this parser deliberately does NOT try to reconstruct the mathematics. It
records structure plus the raw extracted text, and marks which questions carry
shredded math so those can be transcribed by eye from the page. CLAUDE.md is
explicit that a regex converter reverse-engineering author intent from noisy
text was the root cause of every Test 3/4 Math defect, and that the fix is to
hand-write the LaTeX per question. This keeps that possible instead of
foreclosing it.

Numbering restarts per topic, so a question's identity is (topic, number) —
never the number alone. The answer tables are keyed the same way.
"""
import json
import re
import subprocess
import sys

# Topic headings, exactly as the book prints them. Order matters only for
# reporting; matching is exact against a line of its own.
TOPICS = [
    "Expressions", "Linear Equations", "Linear System of Equations",
    "Linear Functions", "Linear Inequalities",
    "Polynomials", "Exponents&Radicals", "Functions&Function Notation",
    "Exponential Functions", "Quadratics",
    "Percent; Ratio&Proportion", "Unit Conversion", "Probability",
    "Mean, Median, Mode, Range", "Scatterplots",
    # This section heading wraps in print, so the first line is what a
    # line-oriented scan actually sees.
    "Research organizing(Margin of Error;",
    "Lines&Angles", "Triangles", "Trigonometry", "Circles", "Areas&Volumes",
    # Book 3 renames three Geometry sections. They are the same topics and are
    # normalised to book 2's names below, so a reader querying "Circles" gets
    # both editions rather than silently only one.
    "Lines and Angles", "Circle", "Area and Volume",
]
SAME_TOPIC = {
    "Lines and Angles": "Lines&Angles",
    "Circle": "Circles",
    "Area and Volume": "Areas&Volumes",
}

# The answer tables are titled differently from the sections they answer —
# "Answers: Percent, Ratio & Proportion" against a section headed
# "Percent; Ratio&Proportion", and "Answers: Research Organizing" against a
# heading that wraps. Matching them by name is the only link between a
# question and its key, so the aliases are declared rather than guessed.
KEY_ALIAS = {
    "Percent, Ratio & Proportion": "Percent; Ratio&Proportion",
    "Research Organizing": "Research organizing(Margin of Error;",
    "Trignometry": "Trigonometry",
    # Book 3's answer blocks carry its own section names. They resolve to
    # book 2's names, the same normalisation the questions get, so a key and
    # the question it belongs to end up filed under one topic rather than two.
    "Lines and Angles": "Lines&Angles",
    "Circle": "Circles",
    "Area and Volume": "Areas&Volumes",
}
DOMAIN_OF = {
    "Lines and Angles": "GT", "Circle": "GT", "Area and Volume": "GT",
    "Expressions": "ALG", "Linear Equations": "ALG",
    "Linear System of Equations": "ALG", "Linear Functions": "ALG",
    "Linear Inequalities": "ALG",
    "Polynomials": "ADV", "Exponents&Radicals": "ADV",
    "Functions&Function Notation": "ADV", "Exponential Functions": "ADV",
    "Quadratics": "ADV",
    "Percent; Ratio&Proportion": "PSDA", "Unit Conversion": "PSDA",
    "Probability": "PSDA", "Mean, Median, Mode, Range": "PSDA",
    "Scatterplots": "PSDA", "Research organizing(Margin of Error;": "PSDA",
    "Lines&Angles": "GT", "Triangles": "GT", "Trigonometry": "GT",
    "Circles": "GT", "Areas&Volumes": "GT",
}
SKILL_OF = {
    "Lines and Angles": "GT-LA", "Circle": "GT-AV", "Area and Volume": "GT-AV",
    "Expressions": "ADV-EQ", "Linear Equations": "ALG-LE",
    "Linear System of Equations": "ALG-LE", "Linear Functions": "ALG-LF",
    "Linear Inequalities": "ALG-LI",
    "Polynomials": "ADV-EQ", "Exponents&Radicals": "ADV-EQ",
    "Functions&Function Notation": "ADV-NF", "Exponential Functions": "ADV-NF",
    "Quadratics": "ADV-NE",
    "Percent; Ratio&Proportion": "PSDA-RP", "Unit Conversion": "PSDA-RP",
    "Probability": "PSDA-ST", "Mean, Median, Mode, Range": "PSDA-ST",
    "Scatterplots": "PSDA-DI",
    "Research organizing(Margin of Error;": "PSDA-ST",
    "Lines&Angles": "GT-LA", "Triangles": "GT-LA", "Trigonometry": "GT-TR",
    "Circles": "GT-AV", "Areas&Volumes": "GT-AV",
}

Q_START = re.compile(r"^(\d+)\.\s*\[([^\]]+)\]\s*$")
CHOICE = re.compile(r"^([A-D])\)\s*(.*)$")
PAGE = re.compile(r"^@satashkent (\d+)\s*$")
ANSWERS_HDR = re.compile(r"^Answers:\s*(.+?)\s*$")
KEY_ROW = re.compile(r"^(\d+)\s+(\S+)(?:\s+(\d+)\s+(\S+))?\s*$")


def pages_of(pdf):
    """Text per page, so every question keeps the page it was printed on."""
    out = []
    n = int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
            .stdout.split("Pages:")[1].split()[0])
    for i in range(1, n + 1):
        out.append(subprocess.run(
            ["pdftotext", "-raw", "-f", str(i), "-l", str(i), pdf, "-"],
            capture_output=True, text=True).stdout.replace("\f", ""))
    return out


def shredded(text):
    """Did TeX math survive extraction, or did it come apart?

    Three signatures, all structural rather than lexical:
      - a bare exponent or index stranded on its own short line
      - a letter immediately followed by a digit ("x2", "9nr2"), which is a
        superscript that lost its position
      - a lone operator line, which is what a fraction rule leaves behind
    """
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if any(re.fullmatch(r"[0-9]{1,2}|[a-z]|[+\-−=]", l) for l in lines[1:]):
        return True
    if re.search(r"(?<=[a-zA-Z])\d(?![\d.,])", text):
        return True
    return False


def parse_pdf(pdf):
    recs, topic, page = [], None, None
    cur = None
    mode = "q"          # "q" while reading questions, "key" inside an answer table
    keys = {}
    for ptext in pages_of(pdf):
        for raw in ptext.split("\n"):
            line = raw.rstrip()
            s = line.strip()
            m = PAGE.match(s)
            if m:
                page = int(m.group(1))
                continue
            m = ANSWERS_HDR.match(s)
            if m and KEY_ALIAS.get(m.group(1), m.group(1)) in TOPICS:
                mode, key_topic = "key", KEY_ALIAS.get(m.group(1), m.group(1))
                if cur:
                    recs.append(cur); cur = None
                continue
            if s in TOPICS:
                topic, mode = s, "q"
                if cur:
                    recs.append(cur); cur = None
                continue
            if mode == "key":
                if s.startswith("Number Answer"):
                    continue
                m = KEY_ROW.match(s)
                if m:
                    keys[(key_topic, int(m.group(1)))] = m.group(2)
                    if m.group(3):
                        keys[(key_topic, int(m.group(3)))] = m.group(4)
                continue
            m = Q_START.match(s)
            if m:
                if cur:
                    recs.append(cur)
                cur = {"topic": topic, "num": int(m.group(1)), "exam": m.group(2),
                       "page": page, "body": [], "choices": []}
                continue
            if cur is None:
                continue
            m = CHOICE.match(s)
            if m:
                cur["choices"].append({"label": m.group(1), "content": m.group(2)})
            elif cur["choices"]:
                cur["choices"][-1]["content"] += " " + s
            else:
                cur["body"].append(s)
    if cur:
        recs.append(cur)
    return recs, keys


def main():
    out, args = sys.argv[1], sys.argv[2:]
    all_q, all_keys = {}, {}
    for arg in args:
        book, pdf = arg.split("=", 1)
        recs, keys = parse_pdf(pdf)
        for (t, n), v in keys.items():
            all_keys[(book, t, n)] = v
        new = 0
        for r in recs:
            if not r["topic"]:
                continue
            k = (book, r["topic"], r["num"])
            # Files overlap by a page, so the same question arrives twice.
            # Keep whichever copy has more of itself.
            prev = all_q.get(k)
            score = len(" ".join(r["body"])) + len(r["choices"]) * 40
            if prev is None or score > prev["_score"]:
                r["_score"] = score
                r["book"] = book
                all_q[k] = r
                new += prev is None
        print(f"{pdf.split('/')[-1]:28} {len(recs):>4} parsed  {new:>4} new")

    qs = []
    for (book, topic, num), r in sorted(all_q.items()):
        topic = SAME_TOPIC.get(topic, topic)
        body = "\n".join(r["body"]).strip()
        qs.append({
            "id": f"satmath-{book}-{topic.lower().replace(' ', '-').replace('&', '-').replace(';', '').replace('(', '').replace(')', '').replace(',', '')}-{num}",
            "book": book, "topic": topic, "num": num, "exam": r["exam"], "page": r["page"],
            "domain": DOMAIN_OF[topic], "skill": SKILL_OF[topic],
            "body": body,
            "choices": [c for c in r["choices"]],
            "type": "MULTIPLE_CHOICE" if len(r["choices"]) == 4 else "FREE_RESPONSE",
            "key": all_keys.get((book, topic, num)),
            "needs_vision": shredded(body + "\n" + "\n".join(c["content"] for c in r["choices"])),
        })

    from collections import Counter
    print(f"\nquestions           {len(qs)}")
    print(f"  with an answer    {sum(1 for q in qs if q['key'])}")
    print(f"  multiple choice   {sum(1 for q in qs if q['type']=='MULTIPLE_CHOICE')}")
    print(f"  free response     {sum(1 for q in qs if q['type']=='FREE_RESPONSE')}")
    print(f"  math survived     {sum(1 for q in qs if not q['needs_vision'])}")
    print(f"  needs transcribe  {sum(1 for q in qs if q['needs_vision'])}")
    print(f"  empty body        {sum(1 for q in qs if not q['body'])}")
    print("\nby topic:")
    for t in TOPICS:
        n = sum(1 for q in qs if q["topic"] == t)
        v = sum(1 for q in qs if q["topic"] == t and q["needs_vision"])
        k = sum(1 for q in qs if q["topic"] == t and q["key"])
        if n:
            print(f"  {t[:44]:<45} {n:>4}   keyed {k:>4}   needs-transcribe {v:>4}")
    json.dump(qs, open(out, "w"), indent=1)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
