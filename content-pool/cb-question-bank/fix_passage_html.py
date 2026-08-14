"""
Rebuild passage HTML for the questions used in Tests 6-15.

The first insert wrote passages as PLAIN TEXT, because the parser collapsed
every newline to a space to normalise wrapped lines. Two things broke as a
result:

1. Every passage rendered as one undifferentiated block. A text with two
   paragraphs, or a Cross-Text passage with a Text 1 / Text 2 split, ran
   together with no break.
2. Rhetorical Synthesis "student notes" — which CLAUDE.md requires to be real
   `<ul><li>` markup — came out as a run-on sentence, so the notes read as
   prose rather than as a list.

Both are recoverable, because `pdftotext -raw` preserves the line structure;
the parser simply discarded it. This re-extracts each question's block from the
source PDF, keeps the newlines, and rebuilds proper HTML.

    python3 fix_passage_html.py <out.json> <tests1.json> [tests2.json …]

Writes {cb_id: passage_html} for every question it can rebuild. Applying it to
the database is a separate step.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

UPLOADS = Path("/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45")
PDFS = sorted(p for p in UPLOADS.glob("*.pdf")
              if re.match(r"^[0-9a-f]{8}-(READING_QUESTION_BANK|\d+)", p.name))

STEM_STARTERS = [
    "Which choice", "Which finding", "Which quotation", "Which statement", "Which data",
    "Which detail", "Which question", "What does", "As used in the text",
    "Based on the text", "According to the text", "The student wants",
    "Which of the following", "The text makes which", "Information in the text",
]

_cache = {}


def blocks_for(pdf):
    if pdf not in _cache:
        txt = subprocess.run(["pdftotext", "-raw", str(pdf), "-"],
                             capture_output=True, text=True).stdout.replace("\f", "")
        d = {}
        for b in re.split(r"(?=Question ID: [0-9a-f]+)", txt):
            m = re.match(r"Question ID: ([0-9a-f]+)", b)
            if m:
                d[m.group(1)] = b
        _cache[pdf] = d
    return _cache[pdf]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_html(lines):
    """Turn the raw question lines into passage HTML, dropping the stem."""
    # Cut everything from the stem onwards — the stem is stored separately.
    cut = len(lines)
    for i, ln in enumerate(lines):
        if any(ln.startswith(s) for s in STEM_STARTERS):
            cut = i
            break
        for s in STEM_STARTERS:
            j = ln.find(s)
            if j > 0:
                lines[i] = ln[:j].rstrip()
                cut = i + 1
                break
        else:
            continue
        break
    lines = [l for l in lines[:cut] if l.strip()]
    if not lines:
        return None

    # Student notes: a "following notes:" lead-in, then one note per line, then
    # a "The student wants…" line. The notes become a real list.
    lead = next((i for i, l in enumerate(lines) if re.search(r"following notes:?$", l, re.I)), None)
    if lead is not None:
        tail = next((i for i in range(lead + 1, len(lines))
                     if lines[i].startswith("The student wants")), len(lines))
        notes, merged = [], ""
        for l in lines[lead + 1:tail]:
            # A note continues onto the next line when the previous one did not
            # end in a full stop.
            if merged and not re.search(r"[.!?][\"”)]?$", merged):
                merged += " " + l
            else:
                if merged:
                    notes.append(merged)
                merged = l
        if merged:
            notes.append(merged)
        out = [f"<p>{esc(lines[lead])}</p>", "<ul>"]
        out += [f"<li>{esc(n)}</li>" for n in notes]
        out.append("</ul>")
        out += [f"<p>{esc(l)}</p>" for l in lines[tail:]]
        return "".join(out)

    # Otherwise: ONE paragraph, broken only at an explicit Text 1 / Text 2
    # marker.
    #
    # `pdftotext -raw` emits no blank line anywhere inside a passage — checked
    # across a whole part, zero occurrences — so the source carries no
    # paragraph information at all. An earlier version guessed at breaks from
    # line length, which invented them: "…such concerns didn't ______ Booker T"
    # / "." / "Whatley's efforts…" was split into two paragraphs straight
    # through a person's name, because the line ended in a period and was
    # short. Guessing a break is strictly worse than not breaking, so this now
    # only breaks where the source is explicit.
    #
    # A line that is nothing but punctuation is the same PDFium artifact as the
    # floating apostrophe: the period after "Booker T" lands on its own line.
    # It is re-attached to the previous line with no space.
    paras, cur = [], ""
    for l in lines:
        st = l.strip()
        if re.match(r"^Text [12]\b", st):
            if cur:
                paras.append(cur)
            paras.append(st)
            cur = ""
            continue
        if re.fullmatch(r"[^\w\s]{1,3}", st) and cur:
            cur += st                       # stray punctuation, no space
            continue
        cur = (cur + " " + st).strip() if cur else st
    if cur:
        paras.append(cur)

    html = []
    for para in paras:
        if re.fullmatch(r"Text [12]", para.strip()):
            html.append(f"<p><strong>{esc(para.strip())}</strong></p>")
        else:
            html.append(f"<p>{esc(para)}</p>")
    return "".join(html)


def main():
    out_path, files = sys.argv[1], sys.argv[2:]
    want = {}
    for f in files:
        for t in json.load(open(f)):
            for m in t["modules"]:
                for q in m["questions"]:
                    want[q["cb_id"]] = q
    print(f"{len(want)} questions to rebuild")

    fixed, missing = {}, []
    for pdf in PDFS:
        blocks = blocks_for(pdf)
        for cid in list(want):
            if cid in fixed or cid not in blocks:
                continue
            b = blocks[cid]
            qm = re.search(r"^Question\s*$", b, re.M)
            am = re.search(r"^Answer\s*$", b, re.M)
            if not (qm and am):
                continue
            html = build_html(b[qm.end():am.start()].split("\n"))
            if html:
                fixed[cid] = html
    missing = [c for c in want if c not in fixed]

    print(f"rebuilt {len(fixed)} | could not rebuild {len(missing)}")
    lists = sum(1 for h in fixed.values() if "<li>" in h)
    multi = sum(1 for h in fixed.values() if h.count("<p>") > 1)
    print(f"  with a real <ul> list: {lists}")
    print(f"  with more than one paragraph: {multi}")
    json.dump({"fixed": fixed, "missing": missing}, open(out_path, "w"), indent=1)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
