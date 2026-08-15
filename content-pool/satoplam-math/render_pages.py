# -*- coding: utf-8 -*-
"""Render the book pages an agent needs to read, as PNGs.

    python3 render_pages.py            # every page referenced by a slice

Transcription has to happen from the PAGE, not from the extracted text — the
extracted text is exactly what cannot be trusted for mathematics. 150 dpi is
enough to read a subscript without the files becoming unwieldy.
"""
import json, os, subprocess, sys

U = "/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45"
SRC = {
    "ma2": [("9e751874-190_ma2", 2, 90), ("67c94270-90170_ma2", 90, 170),
            ("e04acbdf-170180_ma2", 170, 180), ("88c1f5d6-180270_ma2", 180, 270),
            ("279b02ec-270360_ma2.pdf", 270, 360), ("ad3c1ae5-360381_ma2", 360, 381)],
    "ma3": [("63bd2cfa-190_ma3.pdf", 1, 90), ("fece5eb4-90133_ma3.pdf", 90, 133)],
    "hard": [("711bc634-Math_Hard_Book.pdf", 1, 96)],
}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")
os.makedirs(OUT, exist_ok=True)


def render(book, page):
    """Book page -> PNG. Each source file knows the book-page range it covers,
    so the right file and the right offset inside it are both derivable."""
    dest = f"{OUT}/{book}-{page:03d}.png"
    if os.path.exists(dest):
        return dest
    for name, lo, hi in SRC[book]:
        if lo <= page <= hi:
            # The Hard Book prints no page numbers, so its `page` is already a
            # PDF page index; the others carry a printed number offset by one.
            idx = page if book == "hard" else page - lo + 1
            subprocess.run(["pdftoppm", "-f", str(idx), "-l", str(idx), "-r", "150",
                            "-png", "-singlefile", f"{U}/{name}", dest[:-4]],
                           capture_output=True)
            return dest if os.path.exists(dest) else None
    return None


if __name__ == "__main__":
    want = set()
    for f, book_field in (("math_parsed.json", None), ("hard_parsed.json", "hard")):
        for q in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))):
            if q.get("needs_vision") and q.get("page"):
                want.add((book_field or q["book"], q["page"]))
    ok = sum(1 for b, p in sorted(want) if render(b, p))
    print(f"{ok} of {len(want)} pages rendered into {OUT}")
