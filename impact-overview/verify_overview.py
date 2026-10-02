#!/usr/bin/env python3
"""
Verify scholarly_impact_overview.pdf against aggregates.json.

Checks:
  1. exactly one page, A4 size
  2. every font embedded
  3. every headline number on the page equals the computed aggregate, and no
     other numbers appear except the date in the footer
  4. no digits anywhere in the countries section (no per-country counts)
  5. no personal data: the page text contains only the expected vocabulary,
     and no user's name, username or email appears in it. User fields are
     fetched into memory for this comparison only and never written or printed.

Usage:  PROD_URL='postgresql://...' python3 verify_overview.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

from compute_aggregates import neon_query

HERE = Path(__file__).resolve().parent
PDF = HERE / "scholarly_impact_overview.pdf"
OWNER = {"muhammadjon", "ulashov"}

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)


def run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


agg = json.loads((HERE / "aggregates.json").read_text())
fig = agg["figures"]

# 1. one page, A4 -------------------------------------------------------------
info = run("pdfinfo", str(PDF))
pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
w, h = map(float, re.search(r"^Page size:\s+([\d.]+) x ([\d.]+)", info, re.M).groups())
check(pages == 1, f"page count = {pages}")
check(abs(w - 595.28) < 1 and abs(h - 841.89) < 1, f"page size = {w} x {h} pt (A4 = 595.28 x 841.89)")

# 2. fonts embedded -------------------------------------------------------------
fonts = [l for l in run("pdffonts", str(PDF)).splitlines()[2:] if l.strip()]
emb = [l.split()[-5] for l in fonts]  # 'emb' column
check(len(fonts) > 0 and all(e == "yes" for e in emb), f"{len(fonts)} font(s), all embedded: {emb}")

# 3. numbers ---------------------------------------------------------------------
text = run("pdftotext", "-layout", str(PDF), "-")
order = ["students_registered", "countries_represented", "mentorship_session_requests",
         "mentorship_sessions_held", "papers_published"]
expected = [f"{fig[k]['value']:,}" for k in order]
stat_line = next((l for l in text.splitlines() if re.fullmatch(r"\s*[\d,]+(\s+[\d,]+){4}\s*", l)), "")
on_page = stat_line.split()
check(on_page == expected, f"headline numbers on page {on_page} == computed {expected}")
for k, v in zip(order, on_page):
    print(f"        {fig[k]['label']:<30} page={v:<6} computed={fig[k]['value']}")

date_nums = re.findall(r"\d+", agg["computed_on"])
all_nums = re.findall(r"\d[\d,]*", text)
allowed = expected + date_nums
extra = [n for n in all_nums if n not in allowed]
check(not extra and sorted(all_nums) == sorted(allowed),
      f"no numbers other than the 5 figures and the date (found {all_nums})")

# 4. countries section has no digits ----------------------------------------------
section = text.split("Countries represented")[-1].split("Figures computed")[0]
check(not re.search(r"\d", section), "no digits anywhere in the countries section")

# 5. personal data ------------------------------------------------------------------
check("@" not in text, "no '@' (no email addresses) in page text")

# Expected vocabulary: labels, fixed copy, footer, owner line, country names.
html = (HERE / "scholarly_impact_overview.html").read_text()
visible = re.sub(r"<style.*?</style>|<svg.*?</svg>|<[^>]+>", " ", html, flags=re.S)
expected_words = set(re.findall(r"[A-Za-zÀ-ÿ]+", visible.lower()))
page_words = set(re.findall(r"[A-Za-zÀ-ÿ]+", text.lower()))
unexpected = page_words - expected_words
check(not unexpected, f"page text uses only the generated vocabulary ({len(page_words)} words)")

conn = os.environ.get("PROD_URL")
if not conn:
    sys.exit("Set PROD_URL to run the personal-data check.")
rows = neon_query(conn, 'SELECT name, username, email FROM "User"')  # memory only
low = text.lower()
hits_full, hits_word = 0, set()
for r in rows:
    for field in ("username", "email"):
        v = (r.get(field) or "").strip().lower()
        if len(v) >= 3 and re.search(rf"(?<![a-z0-9]){re.escape(v)}(?![a-z0-9])", low):
            hits_full += 1
    name = (r.get("name") or "").strip().lower()
    if len(name) >= 3 and " " in name and name in low and set(name.split()) - OWNER:
        hits_full += 1
    for word in name.split():
        if len(word) >= 3 and word not in OWNER and re.search(rf"\b{re.escape(word)}\b", low):
            hits_word.add(word)
del rows
check(hits_full == 0, f"no user's full name, username or email appears ({hits_full} matches)")
# Single-word overlaps can only be generated page vocabulary (e.g. a person
# whose first name is also a country). Printed only because they are page words.
coincidental = sorted(w for w in hits_word if w in expected_words)
check(set(hits_word) <= expected_words,
      "single-word name overlaps are page vocabulary only"
      + (f" (coincidental: {', '.join(coincidental)})" if coincidental else " (none)"))

print("\nRESULT:", "ALL CHECKS PASSED" if not fails else f"{len(fails)} FAILED")
sys.exit(1 if fails else 0)
