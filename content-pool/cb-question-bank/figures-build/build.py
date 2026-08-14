# -*- coding: utf-8 -*-
"""Assemble content-pool/cb-question-bank/figures.json.

One record per needs_figure question:
  {id, question, figure_html}      for data tables
  {id, question, figure_png_b64}   for bar/line charts
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables
from charts import CHARTS
from render_charts import render

BANK = "/home/user/SAT-Project/content-pool/cb-question-bank/bank_parsed.json"
OUT = "/home/user/SAT-Project/content-pool/cb-question-bank/figures.json"

# Text repairs applied to the cleaned stem. Each is (id, needle, replacement);
# the needle must be present or the build fails loudly rather than silently
# rewriting the wrong question.
TEXT_FIXES = [
    # the table's own rounding footnote belongs with the table, not the stem
    ("3fc06a91", "Rows in table may not add up to 100 due to rounding. ", ""),
    ("dd349efc", "Rows in table may not add up to 100 due to rounding. ", ""),
    # superscripts flattened by text extraction
    ("43f4013a", "( 87 Sr/ 86 Sr)", "(<sup>87</sup>Sr/<sup>86</sup>Sr)"),
    ("43f4013a", "respectively—to 87 Sr/ 86 Sr ratios",
     "respectively—to <sup>87</sup>Sr/<sup>86</sup>Sr ratios"),
    ("43f4013a", "shows how 87 Sr/ 86 Sr ratios",
     "shows how <sup>87</sup>Sr/<sup>86</sup>Sr ratios"),
]

SHRED = re.compile(r'(?:[\d][\d,\.]*\s+){7}[\d][\d,\.]*')


def main():
    cleaned = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaned.json")))
    bank = json.load(open(BANK))
    need = [q["id"] for q in bank if q.get("needs_figure")]

    for qid, needle, repl in TEXT_FIXES:
        t = cleaned[qid]
        assert needle in t, f"{qid}: text fix needle not found: {needle!r}"
        cleaned[qid] = t.replace(needle, repl, 1)

    records = []
    for qid in need:
        q = cleaned[qid].strip()
        assert q, f"{qid}: empty question"
        assert not SHRED.search(q), f"{qid}: shred pattern survived: {q[:120]}"
        rec = {"id": qid, "question": q}
        if qid in tables.TABLES:
            rec["figure_html"] = tables.html(qid)
        elif qid in CHARTS:
            rec["figure_png_b64"] = render(qid, CHARTS[qid])
        else:
            raise SystemExit(f"{qid}: no figure spec")
        records.append(rec)

    ids = [r["id"] for r in records]
    assert len(ids) == len(set(ids)) == len(need) == 73, (len(ids), len(set(ids)), len(need))
    assert set(ids) == set(need)
    for r in records:
        assert r.get("figure_html") or r.get("figure_png_b64"), r["id"]
        assert not (r.get("figure_html") and r.get("figure_png_b64")), r["id"]

    with open(OUT, "w") as f:
        json.dump(records, f, ensure_ascii=False, indent=1)
    n_tab = sum(1 for r in records if "figure_html" in r)
    print(f"wrote {OUT}: {len(records)} records ({n_tab} tables, {len(records)-n_tab} charts)")


if __name__ == "__main__":
    main()
