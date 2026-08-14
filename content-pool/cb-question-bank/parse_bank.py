"""
Parse an official College Board SAT Question Bank PDF export into structured JSON.

Each question in the export looks like:

    Question ID: <hex>
    Assessment Test Domain Skill Difficulty
    SAT Reading and Writing <Domain> <Skill> <Difficulty>
    Question      <passage + stem>
    Answer        A. … B. … C. … D. …
    Correct Answer: <letter>
    Rationale     <why correct, then why each wrong choice is wrong>

Run:  python3 parse_bank.py <file.pdf> <out.json>

Uses `pdftotext -raw`, NOT `-layout`. This matters: in -layout mode PDFium
emits every typographic apostrophe on its own line ahead of the line it belongs
to, so "photography's impact" arrives as a bare "’" line followed by
"photography s impact" — losing the apostrophe from every possessive and
contraction in the bank, and (worse) any attempt to reattach it corrupts the
"A. " choice markers that follow. -raw keeps the character inline where it
belongs and needs no repair at all.

Because -raw collapses the metadata table onto one space-separated line, domain
and skill are recovered by matching against the known SAT taxonomy rather than
by splitting on whitespace — the same "look it up by a known key, never parse
the display string" rule the rest of this project follows.

Vector-drawn charts are not images (`pdfimages` reports zero objects); they are
individually positioned glyphs, so a bar chart's axis labels shred into
fragments like "ns e ry tiv e". Those questions cannot be recovered from text
and are flagged `needs_figure` so the figure can be rebuilt from a page render.
Importing the shredded text as a stem would produce an unanswerable question —
the exact defect CLAUDE.md rule 3 exists to prevent.
"""
import json
import re
import subprocess
import sys

# Ordered longest-first so "Central Ideas and Details" is tried before any
# shorter string that prefixes it.
DOMAINS = [
    "Information and Ideas",
    "Craft and Structure",
    "Expression of Ideas",
    "Standard English Conventions",
    "Algebra",
    "Advanced Math",
    "Problem-Solving and Data Analysis",
    "Geometry and Trigonometry",
]
SKILLS = [
    "Central Ideas and Details", "Command of Evidence", "Inferences",
    "Words in Context", "Text Structure and Purpose", "Cross-Text Connections",
    "Rhetorical Synthesis", "Transitions",
    "Boundaries", "Form, Structure, and Sense",
    "Linear equations in one variable", "Linear functions",
    "Linear equations in two variables", "Systems of two linear equations in two variables",
    "Linear inequalities in one or two variables",
    "Nonlinear functions", "Nonlinear equations in one variable and systems of equations in two variables",
    "Equivalent expressions",
    "Ratios, rates, proportional relationships, and units", "Percentages",
    "One-variable data: distributions and measures of center and spread",
    "Two-variable data: models and scatterplots", "Probability and conditional probability",
    "Inference from sample statistics and margin of error",
    "Evaluating statistical claims: observational studies and experiments",
    "Area and volume", "Lines, angles, and triangles", "Right triangles and trigonometry",
    "Circles",
]
DOMAINS.sort(key=len, reverse=True)
SKILLS.sort(key=len, reverse=True)

CHOICE = re.compile(r"^([A-D])\.\s+(.*)$")


def extract_text(pdf: str) -> str:
    text = subprocess.run(
        ["pdftotext", "-raw", pdf, "-"], capture_output=True, text=True, check=True
    ).stdout
    # Drop form feeds. pdftotext emits \f at a page boundary directly after the
    # newline, so a marker that happens to fall at the top of a page arrives as
    # "\fCorrect Answer: D" and the ^ anchor no longer matches — silently
    # dropping an otherwise perfect question. The \n survives, so removing the
    # \f alone never joins two lines together.
    return text.replace("\f", "")


def parse_meta(meta: str):
    """Pull domain, skill and difficulty out of the metadata region.

    The region is read as a whole and whitespace-collapsed rather than read as
    one line, because a long skill name wraps: "Text Structure and Purpose"
    arrives as "…Craft and Structure Text Structure and" / "Purpose" / "Hard"
    across three lines. Matching the first line alone silently failed on 103
    questions in a single part.

    Matching is case-insensitive: the export writes "Cross-text Connections"
    here and "Cross-Text Connections" elsewhere, and a case-sensitive lookup
    drops those questions for no real reason.
    """
    low = meta.lower()
    difficulty = None
    for d in ("Easy", "Medium", "Hard"):
        if low.rstrip().endswith(d.lower()):
            difficulty = d
            break
    domain = next((d for d in DOMAINS if d.lower() in low), None)
    skill = next((s for s in SKILLS if s.lower() in low), None)
    return domain, skill, difficulty


def clean(s: str) -> str:
    return re.sub(r"[ \t]+", " ", s).strip()


def parse(text: str):
    blocks = [b for b in re.split(r"(?=Question ID: [0-9a-f]+)", text)
              if b.strip().startswith("Question ID")]
    out = []
    for b in blocks:
        qid = re.search(r"Question ID: ([0-9a-f]+)", b).group(1)
        rec = {"id": qid}

        key_m = re.search(r"^Correct Answer:\s*([A-D])\s*$", b, re.M)
        ans_m = re.search(r"^Answer\s*$", b, re.M)
        q_m = re.search(r"^Question\s*$", b, re.M)
        hdr_m = re.search(r"^Assessment Test Domain Skill Difficulty\s*$", b, re.M)

        if not hdr_m or not q_m:
            rec["error"] = "no metadata header"
            out.append(rec)
            continue
        # Everything between the table header and the "Question" marker is the
        # metadata row, however many lines it wrapped onto.
        meta_line = " ".join(b[hdr_m.end():q_m.start()].split())
        domain, skill, difficulty = parse_meta(meta_line)
        if not (domain and skill and difficulty):
            rec["error"] = f"unrecognised taxonomy: {meta_line.strip()!r}"
            out.append(rec)
            continue

        if not (key_m and ans_m and q_m):
            rec["error"] = "missing Question/Answer/Correct Answer marker"
            out.append(rec)
            continue

        qtext = clean(b[q_m.end():ans_m.start()].replace("\n", " "))
        rationale = re.sub(r"^Rationale\s*$", "", b[key_m.end():], flags=re.M)
        rationale = clean(rationale.replace("\n", " "))

        choices, cur = [], None
        for line in b[ans_m.end():key_m.start()].split("\n"):
            m = CHOICE.match(line.strip())
            if m:
                if cur:
                    choices.append(cur)
                cur = {"label": m.group(1), "content": m.group(2)}
            elif cur and line.strip():
                cur["content"] += " " + line.strip()
        if cur:
            choices.append(cur)
        for c in choices:
            c["content"] = clean(c["content"])

        mentions_visual = bool(re.search(r"\b(graph|chart|table|figure)\b", qtext, re.I))
        # A shredded vector chart leaves a run of bare axis numbers behind.
        axis_noise = len(re.findall(r"(?<![\w.])\d{1,3}(?:,\d{3})?(?![\w.%])", qtext)) >= 8

        rec.update({
            "subject": "Math" if " Math " in meta_line else "Reading and Writing",
            "domain": domain,
            "skill": skill,
            "difficulty": difficulty.upper(),
            "question": qtext,
            "choices": choices,
            "correct": key_m.group(1),
            "rationale": rationale,
            "needs_figure": mentions_visual and axis_noise,
            "mentions_visual": mentions_visual,
        })
        out.append(rec)
    return out


def main():
    pdf, outpath = sys.argv[1], sys.argv[2]
    qs = parse(extract_text(pdf))

    errs = [q for q in qs if "error" in q]
    ok = [q for q in qs if "error" not in q]
    bad_n = [q["id"] for q in ok if len(q["choices"]) != 4]
    bad_key = [q["id"] for q in ok if q["correct"] not in {c["label"] for c in q["choices"]}]
    empty = [q["id"] for q in ok if not q["question"] or any(not c["content"] for c in q["choices"])]
    dupes = len(qs) - len({q["id"] for q in qs})
    figs = [q["id"] for q in ok if q["needs_figure"]]

    print(f"parsed                 {len(qs)}")
    print(f"  clean                {len(ok)}")
    print(f"  parse errors         {len(errs)} {[e['id'] for e in errs][:8]}")
    print(f"  not exactly 4 choices{len(bad_n):>3} {bad_n[:8]}")
    print(f"  key not among choices{len(bad_key):>3} {bad_key[:8]}")
    print(f"  empty stem/choice    {len(empty)} {empty[:8]}")
    print(f"  duplicate ids        {dupes}")
    print(f"  need rebuilt figure  {len(figs)}")
    json.dump(qs, open(outpath, "w"), indent=1)
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()
