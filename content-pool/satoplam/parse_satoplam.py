"""
Parse the "SAToplam 2.0" Reading book (@satashkent) into structured JSON.

A completely different format from the official College Board export, so it
needs its own parser:

    Topic N: <name>
    <n> Questions
    DIRECTIONS / Must Know Tips …
    <passage>
    <question number, alone on a line>
    <stem>
    A) …  B) …  C) …  D) …
    . . . . . . . . . .        (dotted separator between questions)
    …
    Answers: <topic name>
    Number Answer Number Answer
    1 D 2 C
    …

Two structural differences that matter:

- Choices are "A)" here, not "A." as in the College Board export.
- The key is NOT next to the question. It lives in a per-topic answer table at
  the end of each topic, indexed by the question's number *within that topic*,
  so the two have to be joined on (topic, number). A question whose number
  cannot be recovered therefore has no key at all and is dropped rather than
  guessed at.

Run:  python3 parse_satoplam.py <file.pdf> <out.json>
"""
import json
import re
import subprocess
import sys

FOOTER = re.compile(r"^@satashkent\s*\d*\s*$")
DOTTED = re.compile(r"^\s*\.(\s*\.)+\s*$")
TOPIC = re.compile(r"^Topic\s+(\d+):\s*(.+?)\s*$")
ANSWERS = re.compile(r"^Answers:\s*(.+?)\s*$")
CHOICE = re.compile(r"^([A-D])\)\s*(.*)$")
NUMBER = re.compile(r"^(\d{1,3})$")


def lines_of(pdfs):
    """Text of every supplied part, concatenated in order.

    Parsed as one stream rather than per file, because a topic's questions and
    its answer table can fall in different parts — the Inference topic starts
    in part 1 and its key is in part 2 — and a per-file parse silently drops
    every question whose key it cannot see.
    """
    out = []
    for pdf in pdfs:
        txt = subprocess.run(["pdftotext", "-raw", pdf, "-"],
                             capture_output=True, text=True, check=True).stdout
        for ln in txt.replace("\f", "").split("\n"):
            if FOOTER.match(ln):
                continue
            out.append(ln.rstrip())
    return out


def parse_answer_table(block):
    """'1 D 2 C' style pairs -> {1: 'D', 2: 'C'}."""
    keys = {}
    for ln in block:
        for num, letter in re.findall(r"(\d{1,3})\s+([A-D])\b", ln):
            keys[int(num)] = letter
    return keys


def parse(pdfs):
    lines = lines_of(pdfs)

    # Index the topic and answer-table boundaries.
    marks = []
    for i, ln in enumerate(lines):
        m = TOPIC.match(ln)
        if m:
            marks.append(("topic", i, m.group(2)))
        m = ANSWERS.match(ln)
        if m:
            marks.append(("answers", i, m.group(1)))

    questions = []
    for idx, (kind, i, name) in enumerate(marks):
        if kind != "topic":
            continue
        # Questions run from the topic header to its answer table; the answer
        # table runs from there to whatever comes next.
        ans_at = next((m for m in marks[idx + 1:] if m[0] == "answers"), None)
        if ans_at is None:
            continue
        nxt = next((m for m in marks[idx + 1:] if m[1] > ans_at[1]), None)
        keys = parse_answer_table(lines[ans_at[1] + 1: nxt[1] if nxt else len(lines)])
        body = lines[i + 1: ans_at[1]]

        # Split into per-question chunks on the dotted separators.
        chunks, cur = [], []
        for ln in body:
            if DOTTED.match(ln):
                if cur:
                    chunks.append(cur)
                cur = []
            else:
                cur.append(ln)
        if cur:
            chunks.append(cur)

        for ch in chunks:
            a_at = next((j for j, ln in enumerate(ch) if CHOICE.match(ln) and ln.startswith("A)")), None)
            if a_at is None:
                continue

            choices, curc = [], None
            for ln in ch[a_at:]:
                m = CHOICE.match(ln)
                if m:
                    if curc:
                        choices.append(curc)
                    curc = {"label": m.group(1), "content": m.group(2)}
                elif curc and ln.strip():
                    curc["content"] += " " + ln.strip()
            if curc:
                choices.append(curc)

            # The question number sits alone on a line between passage and
            # stem; take the LAST such line before the choices, since a
            # passage can legitimately contain a bare year or figure.
            head = ch[:a_at]
            num_at = None
            for j in range(len(head) - 1, -1, -1):
                if NUMBER.match(head[j].strip()):
                    num_at = j
                    break
            if num_at is None:
                continue
            number = int(head[num_at].strip())
            passage = " ".join(x.strip() for x in head[:num_at] if x.strip())
            stem = " ".join(x.strip() for x in head[num_at + 1:] if x.strip())

            for c in choices:
                c["content"] = re.sub(r"\s+", " ", c["content"]).strip()

            questions.append({
                "topic": name,
                "number": number,
                "passage": re.sub(r"\s+", " ", passage).strip(),
                "question": re.sub(r"\s+", " ", stem).strip(),
                "choices": choices,
                "correct": keys.get(number),
                # The book reconstructs damaged text inside square brackets,
                # e.g. "delivered by [a confident orator, it may be] ignored".
                # That is an editorial guess at the original wording, so it is
                # flagged rather than shipped silently.
                "bracketed_text": bool(re.search(r"\[[^\]]{4,}\]",
                                                 passage + " " + stem + " " +
                                                 " ".join(c["content"] for c in choices))),
            })
    return questions


def main():
    out, pdfs = sys.argv[1], sys.argv[2:]
    qs = parse(pdfs)
    # Parts overlap at their boundaries, so the same question can appear twice.
    seen, uniq = set(), []
    for q in qs:
        k = (q["topic"], q["number"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(q)
    dupes = len(qs) - len(uniq)
    qs = uniq
    if dupes:
        print(f"dropped {dupes} duplicate (topic, number) across part boundaries")
    nokey = [q for q in qs if not q["correct"]]
    bad = [q for q in qs if len(q["choices"]) != 4]
    brk = [q for q in qs if q["bracketed_text"]]
    print(f"parsed            {len(qs)}")
    print(f"  no key          {len(nokey)}")
    print(f"  not 4 choices   {len(bad)}")
    print(f"  bracketed text  {len(brk)}")
    print(f"  topics          {sorted({q['topic'] for q in qs})}")
    json.dump(qs, open(out, "w"), indent=1)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
