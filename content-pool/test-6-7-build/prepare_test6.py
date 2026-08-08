#!/usr/bin/env python3
"""
Convert test6.json into the two files insert_test6.mjs consumes, matching the
shape `../test-5-build/insert_test5.mjs` established.

R&W: `passage` becomes `passageHtml` (wrapped in <p> unless it already opens a
block element), `answer` becomes `correct`, and any `table` tuple is rendered
into the standard style block and prepended to the passage.
Math: passes through, with `correct`/`correctAnswerFR` already in place.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "test6.json")))

TABLE_OPEN = '<table style="border-collapse:collapse;margin:0.75rem 0;">'
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'


def table_html(t):
    if isinstance(t, dict):
        title, headers, rows = None, t["headers"], t["rows"]
    else:
        title, headers, rows = t
    html = (TABLE_OPEN + "<thead><tr>" + "".join(f"{TH}{h}</th>" for h in headers)
            + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"{TD}{c}</td>" for c in r) + "</tr>" for r in rows)
            + "</tbody></table>")
    return (f"<p><strong>{title}</strong></p>" if title else "") + html


def passage_html(q):
    p = q["passage"].strip()
    body = p if re.match(r'^<(p|ul|ol|table|div)\b', p) else f"<p>{p}</p>"
    # a passage written as "...intro</p><p>rest" needs its opening <p> supplied
    if body.startswith("<p>") is False and "</p>" in body:
        body = "<p>" + body
    return (table_html(q["table"]) if "table" in q else "") + body


rw, math = {}, {}
for key, out_key in (("RW_M1", "test6|RW_M1"), ("RW_M2E", "test6|RW_M2_EASY"),
                     ("RW_M2H", "test6|RW_M2_HARD")):
    rw[out_key] = [{
        "source": q.get("_src", "AUTHORED"),
        "sourceNum": q["num"],
        "sourceRef": q.get("_ref"),
        "type": "MULTIPLE_CHOICE",
        "passageHtml": passage_html(q),
        "stem": q["stem"],
        "choices": q["choices"],
        "correct": q["answer"],
        "domainCode": q["domainCode"],
        "skillCode": q["skillCode"],
        "skill": q["skill"],
        "order": q["order"],
        "why": q.get("why", ""),
    } for q in T[key]]

for key, out_key in (("MATH_M1", "MATH_M1"), ("MATH_M2E", "MATH_M2_EASY"),
                     ("MATH_M2H", "MATH_M2_HARD")):
    math[out_key] = T[key]

json.dump(rw, open(os.path.join(HERE, "test6_rw.json"), "w"), indent=1)
json.dump(math, open(os.path.join(HERE, "test6_math.json"), "w"), indent=1)
for k, v in rw.items():
    print(f"  {k}: {len(v)}")
for k, v in math.items():
    fr = sum(1 for q in v if q["type"] == "FREE_RESPONSE")
    print(f"  {k}: {len(v)} ({len(v)-fr} MC + {fr} FR)")
