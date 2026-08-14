"""
Turn raw SAToplam parse output into content fit to insert.

    python3 prepare_satoplam.py <satoplam.json> <blanks.json> <out.json>

Four repairs and one filter, all needed before any of this reaches a student:

1. **Restore the fill-in-the-blank markers.** The books draw a blank as a
   horizontal rule, so `pdftotext -raw` loses it and a Boundaries passage reads
   "is an arid it is one of the largest deserts" — unanswerable, because the
   student cannot see where the choice belongs. `recover_blanks.py` locates the
   position from the layout gap; this applies the result.

2. **Append the trailing blank on Inference items.** Their passage stops
   mid-sentence by design and the real exam prints a blank there. The ones
   recovered in step 1 confirm the position is the very end, so the rest get
   the same treatment rather than being discarded.

3. **Turn the bullet characters into a real list.** The notes arrive as
   "… the following notes: • first • second", which renders as a run-on
   paragraph. CLAUDE.md requires real <ul><li> markup.

4. **Wrap prose in paragraphs**, since the parse produces bare text.

Then anything still unusable is dropped rather than shipped: a question that
asks about an underlined portion with no underline, one that points at a figure
that does not exist, or one that still has no blank after steps 1 and 2. Each
is unanswerable, and an unanswerable question is worse than one fewer question.
"""
import json
import re
import sys

POINTS_AT_FIGURE = re.compile(
    r"\b(?:the|this|these|following|accompanying)\s+(?:table|graph|chart|figure)\b|"
    r"\b(?:table|graph|chart|figure)\s+(?:above|below|shown|presented)\b", re.I)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def to_html(passage):
    """Bare text -> paragraphs, with bulleted notes as a real list."""
    text = re.sub(r"\s+", " ", passage).strip()
    if "•" in text:
        head, *rest = text.split("•")
        items = [i.strip() for i in rest if i.strip()]
        # A trailing sentence after the last bullet is prose, not a note: the
        # student-notes format ends with "The student wants to …".
        tail = ""
        if items:
            m = re.search(r"(The student wants.*)$", items[-1])
            if m:
                tail = m.group(1).strip()
                items[-1] = items[-1][: m.start()].strip()
        out = [f"<p>{esc(head.strip())}</p>", "<ul>"]
        out += [f"<li>{esc(i)}</li>" for i in items if i]
        out.append("</ul>")
        if tail:
            out.append(f"<p>{esc(tail)}</p>")
        return "".join(out)

    parts = re.split(r"(?=\bText [12]\b)", text)
    html = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        m = re.match(r"^(Text [12])\b\s*(.*)$", p, re.S)
        if m:
            html.append(f"<p><strong>{esc(m.group(1))}</strong></p>")
            if m.group(2).strip():
                html.append(f"<p>{esc(m.group(2).strip())}</p>")
        else:
            html.append(f"<p>{esc(p)}</p>")
    return "".join(html)


def main():
    src, blanks_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    qs = json.load(open(src))
    blanks = json.load(open(blanks_path))["fixed"]

    stats = {"blank_restored": 0, "blank_appended": 0, "bulleted": 0,
             "dropped_no_blank": 0, "dropped_underline": 0, "dropped_figure": 0}
    kept = []
    for q in qs:
        # A question whose stem is empty had its stem swallowed into the
        # passage by the split, so the student sees the question text as part
        # of the passage and no question at all.
        if not (q.get("question") or "").strip():
            stats["dropped_no_stem"] = stats.get("dropped_no_stem", 0) + 1
            continue
        key = f"{q['topic']}|{q['number']}"
        passage = blanks.get(key, q["passage"] or "")
        if key in blanks:
            stats["blank_restored"] += 1

        needs_blank = bool(re.search(r"completes the text", q["question"], re.I))
        has_blank = bool(re.search(r"_{3,}", passage + q["question"]))

        # An Inference passage stops mid-sentence and the exam prints the blank
        # at the end. Only ever appended when the text really does trail off —
        # a passage ending in a full stop is a different shape and is dropped
        # instead of being given a blank it never had.
        if needs_blank and not has_blank and q["topic"] == "Inference":
            if not re.search(r"[.!?][\"”)]?\s*$", passage):
                passage = passage.rstrip() + " ______"
                has_blank = True
                stats["blank_appended"] += 1

        if needs_blank and not has_blank:
            stats["dropped_no_blank"] += 1
            continue
        if re.search(r"underlined", q["question"], re.I) and "<u>" not in passage:
            stats["dropped_underline"] += 1
            continue
        if POINTS_AT_FIGURE.search(q["question"]) and "<table" not in passage:
            stats["dropped_figure"] += 1
            continue

        if "•" in passage:
            stats["bulleted"] += 1
        q = dict(q)
        q["passage"] = to_html(passage)
        kept.append(q)

    print(f"in {len(qs)} -> usable {len(kept)}")
    for k, v in stats.items():
        print(f"  {k:20} {v}")
    json.dump(kept, open(out_path, "w"), indent=1)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
