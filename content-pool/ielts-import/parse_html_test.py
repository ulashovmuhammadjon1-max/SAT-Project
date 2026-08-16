# -*- coding: utf-8 -*-
"""Convert a self-contained IELTS practice HTML export into our schema.

    python3 parse_html_test.py <file.html> <out.json>

The exports carry the whole test in a single `window.ieltsData` object, so
nothing here scrapes the DOM: the object is lifted out and remapped. That is
the difference between an importer that survives a layout change and one that
breaks on the next file.

What this does NOT do is trust the source. Two things are checked and reported
rather than imported quietly:

* **gap alignment** — a completion group carries both a `full_text` with
  `__n__` markers and a `question_details` list, and they can disagree. In the
  file this was built against, gap 2 sits on the "Email:" line while its
  recorded answer is "post", which belongs to the following line. Importing
  that silently would put a wrong answer in front of a student.
* **option lettering** — the flow-chart group lists its options as
  `["A the blood", "a flower", …]`, lettered on the first entry only. Letters
  are re-derived from position instead of parsed off the text.
"""
import json, re, sys, html as htmllib

TYPE_MAP = {
    "form completion": "FORM_COMPLETION",
    "note completion": "NOTE_COMPLETION",
    "table completion": "TABLE_COMPLETION",
    "flowchart completion": "FLOWCHART_COMPLETION",
    "flow-chart completion": "FLOWCHART_COMPLETION",
    "summary completion": "SUMMARY_COMPLETION",
    "sentence completion": "SENTENCE_COMPLETION",
    "short answer": "SHORT_ANSWER",
    "multiple choice": "MULTIPLE_CHOICE_SINGLE",
    "matching features": "MATCHING_FEATURES",
    "matching information": "MATCHING_INFORMATION",
    "matching headings": "MATCHING_HEADINGS",
    "plan/map/diagram labelling": "PLAN_MAP_DIAGRAM_LABEL",
    "diagram labelling": "DIAGRAM_LABEL_COMPLETION",
}

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def extract_data(path):
    """Lift `window.ieltsData = {...}` out by brace matching, not by regex."""
    s = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"window\.ieltsData\s*=\s*", s)
    if not m:
        raise SystemExit("no window.ieltsData in this file")
    i = s.index("{", m.end())
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                break
    return json.loads(s[i:j + 1])


def word_limit(instructions):
    """Read the printed limit into something the answer validator can enforce."""
    t = (instructions or "").upper()
    if "ONE WORD AND/OR A NUMBER" in t:
        return {"wordLimit": "ONE WORD AND/OR A NUMBER", "maxWords": 1, "maxNumbers": 1}
    if "NO MORE THAN THREE WORDS AND/OR A NUMBER" in t:
        return {"wordLimit": "NO MORE THAN THREE WORDS AND/OR A NUMBER", "maxWords": 3, "maxNumbers": 1}
    if "NO MORE THAN TWO WORDS AND/OR A NUMBER" in t:
        return {"wordLimit": "NO MORE THAN TWO WORDS AND/OR A NUMBER", "maxWords": 2, "maxNumbers": 1}
    if "NO MORE THAN THREE WORDS" in t:
        return {"wordLimit": "NO MORE THAN THREE WORDS", "maxWords": 3, "maxNumbers": 0}
    if "NO MORE THAN TWO WORDS" in t:
        return {"wordLimit": "NO MORE THAN TWO WORDS", "maxWords": 2, "maxNumbers": 0}
    if "ONE WORD ONLY" in t:
        return {"wordLimit": "ONE WORD ONLY", "maxWords": 1, "maxNumbers": 0}
    return {"wordLimit": None, "maxWords": None, "maxNumbers": None}


def body_html(full_text):
    """`__7__` becomes `{{7}}`; `## X` becomes a sub-heading; `-` a bullet."""
    if not full_text:
        return None
    out = []
    for raw in full_text.split("\n"):
        line = htmllib.escape(raw.strip())
        if not line:
            continue
        line = re.sub(r"__(\d+)__", r"{{\1}}", line)
        if line.startswith("## "):
            out.append(f"<h4>{line[3:]}</h4>")
        elif line.startswith("&ndash;") or line.startswith("–") or line.startswith("-"):
            out.append(f"<li>{line.lstrip('-–').lstrip()}</li>")
        elif line == "↓":
            out.append('<p class="flow-arrow">&darr;</p>')
        else:
            out.append(f"<p>{line}</p>")
    # Wrap any run of <li> in a real list rather than leaving them loose.
    joined = "".join(out)
    joined = re.sub(r"(<li>.*?</li>)(?!<li>)", lambda m: m.group(1), joined)
    return re.sub(r"((?:<li>.*?</li>)+)", r"<ul>\1</ul>", joined)


def check_gaps(group, findings):
    """Does every numbered gap in the body match a recorded question?"""
    ft = group.get("full_text")
    if not ft:
        return
    in_body = [int(n) for n in re.findall(r"__(\d+)__", ft)]
    recorded = [d["number"] for d in group.get("question_details", [])]
    if sorted(in_body) != sorted(recorded):
        findings.append(
            f"Q{group['from']}-{group['to']}: body has gaps {sorted(in_body)} "
            f"but {sorted(recorded)} are recorded")
    # The subtler failure: the gap is present but the text around it does not
    # match the question's own `text`, which is how a misplaced marker looks.
    #
    # Both sides must be normalised the SAME way. The first version of this
    # check stripped the `__n__` marker out of the recorded text but not out of
    # the body, so every mid-sentence gap failed to match and it reported ten
    # findings where there is one. An over-matching check is worse than none,
    # because it buries the real defect in noise.
    def norm(t):
        """Marker removed, punctuation flattened, whitespace collapsed.

        Punctuation has to go: the export writes "Advantages: cheap and __34__"
        in the body and "Advantages -cheap and __34__" in the record. That is a
        transcription difference, not a misplaced gap, and leaving it in the
        comparison produced a finding that would have sent an admin hunting for
        a defect that is not there."""
        t = re.sub(r"__\d+__", " ", t or "")
        t = re.sub(r"[^\w\s]", " ", t)
        return re.sub(r"\s+", " ", t).strip().lower()

    body = norm(ft)
    for d in group.get("question_details", []):
        core = norm(d.get("text"))
        if core and core not in body:
            findings.append(
                f"Q{d['number']}: recorded text {d.get('text')!r} does not appear "
                f"in the group body — the gap marker may be on the wrong line")

    # The defect that actually matters, and the one the check above cannot see:
    # the ANSWER printed in the body instead of a gap. Removing a marker from
    # the recorded text leaves a fragment that still matches, so a misplaced
    # gap reads as fine — but if the answer word is sitting in the body in
    # plain sight, the student is shown the answer and the gap is somewhere it
    # does not belong. Short answers are skipped: a one- or two-letter answer
    # collides with ordinary words by accident.
    for d in group.get("question_details", []):
        ans = str(d.get("correct_answer") or "").strip()
        if len(ans) < 3 or ans.isdigit():
            continue
        if re.search(rf"(?<![\w]){re.escape(ans.lower())}(?![\w])", body):
            findings.append(
                f"Q{d['number']}: the answer {ans!r} appears in the group body — "
                f"it has been printed instead of gapped, so the student sees it")


def convert(data, title, slug):
    findings = []
    parts_out = []
    seen_numbers = []

    for idx, part in enumerate(data.get("parts", []), 1):
        groups_out = []
        for g in part.get("questions", []):
            gtype = TYPE_MAP.get(str(g.get("type", "")).strip().lower())
            if not gtype:
                findings.append(f"Q{g.get('from')}-{g.get('to')}: unmapped type {g.get('type')!r}")
                gtype = "SHORT_ANSWER"
            check_gaps(g, findings)

            # Letters come from position. The source letters only the first
            # option, so parsing them off the text would mislabel the rest.
            raw_options = g.get("options") or []
            options = []
            for n, opt in enumerate(raw_options):
                text = re.sub(r"^[A-Z]\s+", "", str(opt)).strip()
                options.append({"key": LETTERS[n], "text": text})

            questions_out = []
            for d in g.get("question_details", []):
                num = d["number"]
                seen_numbers.append(num)
                per_q = [{"key": LETTERS[n], "text": str(o)}
                         for n, o in enumerate(d.get("options") or [])]
                answer = str(d.get("correct_answer", "")).strip()
                accepted = []
                # Where a group answers by letter but the key stores the option
                # TEXT, accept both — a student typing either is right, and the
                # renderer decides which one it asks for.
                if options and answer and answer not in [o["key"] for o in options]:
                    match = next((o for o in options
                                  if o["text"].lower() == answer.lower()), None)
                    if match:
                        accepted.append(match["key"])
                    else:
                        findings.append(
                            f"Q{num}: answer {answer!r} is not one of the group's options")
                questions_out.append({
                    "number": num,
                    "type": gtype,
                    "promptHtml": d.get("text") or None,
                    "optionsJson": per_q or None,
                    "correctAnswer": answer,
                    "acceptedAnswers": accepted or None,
                })

            groups_out.append({
                "type": gtype,
                "instructions": g.get("instructions") or "",
                **word_limit(g.get("instructions")),
                "bodyHtml": body_html(g.get("full_text")),
                "optionsJson": options or None,
                "leftHeading": g.get("left_heading"),
                "rightHeading": g.get("right_heading"),
                "questions": questions_out,
            })

        parts_out.append({
            "partNumber": idx,
            "title": part.get("partLabel") or f"Part {idx}",
            "instructions": part.get("instructions") or None,
            # Audio is deliberately NOT carried over: the export points at a
            # third-party host, and hotlinking it would both break when that
            # host goes away and serve bytes we do not control. The admin
            # attaches the file.
            "audioUrl": None,
            "transcript": (data.get("transcript") or {}).get(str(idx)),
            "groups": groups_out,
        })

    expected = list(range(1, 41))
    if sorted(seen_numbers) != expected:
        missing = sorted(set(expected) - set(seen_numbers))
        dupes = sorted({n for n in seen_numbers if seen_numbers.count(n) > 1})
        findings.append(f"question numbering: {len(seen_numbers)} found; "
                        f"missing {missing}; duplicated {dupes}")

    return {
        "title": title, "slug": slug, "module": "ACADEMIC", "status": "DRAFT",
        "skill": "LISTENING", "durationMinutes": 30,
        "sourceNote": data.get("mode"), "parts": parts_out,
        "findings": findings,
    }


if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    data = extract_data(src)
    test = convert(data, "IELTS Listening Practice 1", "listening-practice-1")
    json.dump(test, open(out, "w"), indent=1, ensure_ascii=False)

    nq = sum(len(g["questions"]) for p in test["parts"] for g in p["groups"])
    print(f"{len(test['parts'])} parts, "
          f"{sum(len(p['groups']) for p in test['parts'])} groups, {nq} questions")
    for p in test["parts"]:
        for g in p["groups"]:
            print(f"  part {p['partNumber']}  {g['questions'][0]['number']}-"
                  f"{g['questions'][-1]['number']}  {g['type']}  "
                  f"limit={g['wordLimit']}")
    print(f"\nFINDINGS ({len(test['findings'])}) — these block publishing:")
    for f in test["findings"]:
        print("  ! " + f)
    print(f"\nwrote {out}")
