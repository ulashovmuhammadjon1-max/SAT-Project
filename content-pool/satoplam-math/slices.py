# -*- coding: utf-8 -*-
"""Split the transcription work across agents, grouped by page.

    python3 slices.py <n>

Grouped by book and page rather than round-robin: an agent opens one page
image and does every question printed on it, instead of paging back and forth.
Written to disk so a restarted agent gets exactly the slice it had before.
"""
import json, math, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 12
qs = []
for f in ("math_parsed.json", "hard_parsed.json"):
    qs += [q for q in json.load(open(f"{HERE}/{f}")) if q.get("needs_vision")]

by_page = defaultdict(list)
for q in qs:
    by_page[(q.get("src") or q["book"], q.get("pdf_page") or q["page"])].append(q)
pages = sorted(by_page)
per = math.ceil(len(qs) / N)

os.makedirs(f"{HERE}/out", exist_ok=True)
slices, cur = [], []
for p in pages:
    cur += by_page[p]
    if len(cur) >= per:
        slices.append(cur); cur = []
if cur:
    slices.append(cur)

for i, sl in enumerate(slices[:N] if len(slices) > N else slices, 1):
    name = f"mx-{i:02d}"
    json.dump(sl, open(f"{HERE}/out/{name}.slice.json", "w"), indent=1)
    books = sorted({q["book"] for q in sl})
    print(f"{name}  {len(sl):>4} questions  books {','.join(books)}  "
          f"pages {sl[0].get('pdf_page')}-{sl[-1].get('pdf_page')}")
print(f"\n{len(qs)} questions needing transcription across {len(slices)} slices")
