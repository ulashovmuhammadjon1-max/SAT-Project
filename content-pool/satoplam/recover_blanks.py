"""
Recover the missing fill-in-the-blank markers in the SAToplam Writing book.

    python3 recover_blanks.py <satoplam.json> <out.json> <part1.pdf> …

The book draws each blank as a horizontal RULE, not as underscores, so
`pdftotext -raw` — which the parser uses, because it keeps apostrophes inline —
drops it completely. A Boundaries passage arrives as

    "The Great Salt Desert in western Asia is an arid it is one of the largest"

and the student cannot tell where "desert, for example;" belongs. Every
Boundaries and Form-Structure-and-Sense question in the book is affected: 436
unanswerable questions.

`pdftotext -layout` DOES preserve the rule, as a run of spaces. So the position
is recoverable without reading anything visually: crop to the passage column,
find the gap, take the words on either side of it, and insert a five-underscore
blank between that same pair of words in the parsed passage.

Every insertion is gated on the surrounding words occurring EXACTLY ONCE in the
passage. A pair that is ambiguous, or that cannot be found, is reported and
left alone rather than guessed at — a blank in the wrong place is worse than a
missing one, because it silently changes what the question asks.
"""
import json
import re
import subprocess
import sys
from collections import defaultdict

# The passage sits in the left column of an A4 page; the stem and choices are
# on the right. Cropping keeps the two from interleaving.
CROP = ["-x", "0", "-y", "0", "-W", "300", "-H", "800"]
GAP = re.compile(r"(\S+)\s{3,}(\S+)")


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def page_text(pdf, page, layout):
    args = ["pdftotext", "-f", str(page), "-l", str(page)]
    args += ["-layout"] + CROP if layout else ["-raw"]
    return subprocess.run(args + [pdf, "-"], capture_output=True, text=True).stdout.replace("\f", "")


def build_index(pdfs):
    """page -> raw text, so a question can be located by a distinctive phrase."""
    idx = []
    for pdf in pdfs:
        n = int(re.search(r"Pages:\s+(\d+)",
                subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
        for p in range(1, n + 1):
            idx.append((pdf, p, page_text(pdf, p, layout=False)))
    return idx


def main():
    src, out_path, pdfs = sys.argv[1], sys.argv[2], sys.argv[3:]
    qs = json.load(open(src))

    # Only questions that need a blank and do not have one.
    targets = [q for q in qs
               if re.search(r"completes the text", q["question"], re.I)
               and not re.search(r"_{3,}", (q["passage"] or "") + q["question"])]
    print(f"{len(targets)} questions missing a blank")

    print("indexing pages…")
    idx = build_index(pdfs)
    print(f"  {len(idx)} pages")

    layout_cache = {}
    fixed, failed = {}, []
    for q in targets:
        # A distinctive phrase: the last words of the passage are the least
        # likely to repeat across the book.
        probe = " ".join(norm(q["passage"]).split()[-8:])
        hit = next(((pdf, pg) for pdf, pg, txt in idx if probe and probe in norm(txt)), None)
        if not hit:
            failed.append((q["topic"], q["number"], "page not found"))
            continue
        pdf, pg = hit
        if hit not in layout_cache:
            layout_cache[hit] = page_text(pdf, pg, layout=True)
        lay = layout_cache[hit]

        passage = q["passage"]
        placed = False
        for before, after in GAP.findall(lay):
            if before in ("", None) or after in ("", None):
                continue
            pair = re.compile(re.escape(before) + r"\s+" + re.escape(after))
            hits = pair.findall(passage)
            if len(hits) != 1:
                continue
            passage = pair.sub(f"{before} _____ {after}", passage, count=1)
            placed = True
            break
        if placed:
            fixed[f"{q['topic']}|{q['number']}"] = passage
        else:
            failed.append((q["topic"], q["number"], "no unambiguous gap"))

    print(f"recovered {len(fixed)} | could not place {len(failed)}")
    by_reason = defaultdict(int)
    for _, _, r in failed:
        by_reason[r] += 1
    for r, n in by_reason.items():
        print(f"    {r}: {n}")
    json.dump({"fixed": fixed, "failed": failed}, open(out_path, "w"), indent=1)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
