# -*- coding: utf-8 -*-
"""Independent check of legacy_fixes.json against legacy_defects.json.

Reads both files from disk -- it shares no state with build_legacy_fixes.py, so
a bug in the builder's own asserts cannot hide here.

  underline records: exactly one <u>...</u>, and deleting the <u>/</u> tags
                     reproduces the original passage byte for byte.
  figure records:    every tag balanced, every table rectangular, the original
                     prose preserved verbatim, and (where an underline was
                     added too) the same strip-and-compare test.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
defects = {d["id"]: d for d in json.load(open(os.path.join(HERE, "legacy_defects.json")))}
fixes = json.load(open(os.path.join(HERE, "legacy_fixes.json")))

PLACEHOLDER = re.compile(r"<p><em>\[Graph/figure not available[^]]*\]</em></p>")
TAGS = ("p", "strong", "table", "tr", "th", "td", "u", "em")

fails = []


def bad(qid, msg):
    fails.append(f"{qid}: {msg}")


for f in fixes:
    if "failed" in f:
        print(f"NOTE: {len(f['failed'])} question(s) recorded as failed")
        continue
    qid, new, kind = f["id"], f["passage"], f["kind"]
    old = defects[qid]["passage"]

    for tag in TAGS:
        o = len(re.findall(r"<%s[ >]" % tag, new))
        c = len(re.findall(r"</%s>" % tag, new))
        if o != c:
            bad(qid, f"unbalanced <{tag}>: {o} open / {c} close")

    for tbl in re.findall(r"<table.*?</table>", new, re.S):
        widths = {len(re.findall(r"<t[hd][ >]", row))
                  for row in re.findall(r"<tr>.*?</tr>", tbl, re.S)}
        if len(widths) != 1:
            bad(qid, f"table not rectangular: row widths {sorted(widths)}")
        if not widths or widths == {0}:
            bad(qid, "table has no cells")

    nu, ncu = new.count("<u>"), new.count("</u>")
    stripped = new.replace("<u>", "").replace("</u>", "")

    if kind == "underline":
        if (nu, ncu) != (1, 1):
            bad(qid, f"expected one <u> pair, found {nu}/{ncu}")
        if stripped != old:
            bad(qid, "stripping <u> does not reproduce the original passage")
    else:
        # A figure record may also carry an underline (one question needed
        # both).  Its prose must still survive untouched: drop the figure
        # block and the old placeholder from both sides and compare.
        if nu != ncu:
            bad(qid, f"unbalanced <u>: {nu}/{ncu}")
        prose_new = re.sub(r"^<p><strong>.*?</strong></p>(<table.*?</table>|<p><img[^>]*/></p>)",
                           "", stripped, flags=re.S)
        prose_old = PLACEHOLDER.sub("", old).strip()
        if prose_new.strip() != prose_old:
            bad(qid, "prose text changed by the figure edit")
        if "<table" not in new and "<img" not in new:
            bad(qid, "figure record contains neither a table nor an image")

    # nothing but the passage may be emitted
    extra = set(f) - {"id", "passage", "kind", "note"}
    if extra:
        bad(qid, f"unexpected keys {sorted(extra)}")
    if kind not in ("underline", "figure"):
        bad(qid, f"bad kind {kind!r}")
    if not f.get("note"):
        bad(qid, "empty note")

ids = [f["id"] for f in fixes if "id" in f]
missing = set(defects) - set(ids)
if missing:
    for m in sorted(missing):
        fails.append(f"{m}: present in legacy_defects.json but not fixed or failed")

for f in fixes:
    if "id" not in f:
        continue
    print(f"OK   {f['id']}  {f['kind']:<9} "
          f"<u>x{f['passage'].count('<u>')}  "
          f"table={'y' if '<table' in f['passage'] else 'n'}  "
          f"img={'y' if '<img' in f['passage'] else 'n'}  "
          f"{len(f['passage'])} chars")

if fails:
    print("\nFAILURES:")
    for x in fails:
        print("  " + x)
    sys.exit(1)
print(f"\nall {len(ids)} records pass")
