#!/usr/bin/env python3
"""
Render test7.json as a review PDF.

This is the artefact the test is approved from, so it shows everything a
reviewer needs to judge it and nothing they would have to take on trust: every
passage, every stem, all four choices, the marked key, and — for each question —
the reasoning that produced that key (`why` for Reading & Writing, `check` for
Math).

Math is rendered by KaTeX so the PDF shows the same typesetting the student
sees, which is the point of reviewing it on paper at all: a stem that renders a
literal caret or a slash fraction is visible here before it ships.

    python3 make_pdf.py            -> Test-7-review.pdf
"""
import html
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")

TITLES = [
    ("RW_M1", "Section 1, Module 1: Reading and Writing", "Standard", 27),
    ("RW_M2E", "Section 1, Module 2: Reading and Writing", "Easy", 27),
    ("RW_M2H", "Section 1, Module 2: Reading and Writing", "Hard", 27),
    ("MATH_M1", "Section 2, Module 1: Math", "Standard", 22),
    ("MATH_M2E", "Section 2, Module 2: Math", "Easy", 22),
    ("MATH_M2H", "Section 2, Module 2: Math", "Hard", 22),
]

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt;
       line-height: 1.5; color: #1D2433; margin: 0; }
h1 { font-family: Helvetica, Arial, sans-serif; font-size: 26pt; margin: 0 0 4pt; }
.sub { font-family: Helvetica, Arial, sans-serif; color: #505866; font-size: 10pt; margin: 0; }
.cover { page-break-after: always; padding-top: 40mm; }
.cover table { border-collapse: collapse; margin-top: 14pt; font-family: Helvetica, Arial, sans-serif;
               font-size: 9.5pt; width: 100%; }
.cover th, .cover td { border: 1px solid #D9DEE5; padding: 4pt 7pt; text-align: left; }
.cover th { background: #F4F6F8; }
.note { background: #F7F7F5; border-left: 3px solid #2D6CDF; padding: 8pt 11pt;
        margin: 14pt 0; font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; }
.modhead { page-break-before: always; border-bottom: 2px solid #0E1728;
           padding-bottom: 5pt; margin-bottom: 12pt; }
.modhead h2 { font-family: Helvetica, Arial, sans-serif; font-size: 15pt; margin: 0; }
.modhead p { font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; color: #505866; margin: 3pt 0 0; }
.q { page-break-inside: avoid; margin: 0 0 15pt; padding-bottom: 11pt;
     border-bottom: 1px solid #E4E7EC; }
.qhead { font-family: Helvetica, Arial, sans-serif; font-size: 9pt; color: #505866;
         margin-bottom: 5pt; }
.qnum { display: inline-block; background: #0E1728; color: #fff; border-radius: 3px;
        padding: 1pt 6pt; font-weight: bold; margin-right: 7pt; }
.tag { display: inline-block; border: 1px solid #D9DEE5; border-radius: 3px;
       padding: 0 5pt; margin-left: 4pt; background: #FAFAF8; }
.passage { background: #F7F7F5; border: 1px solid #E4E7EC; padding: 8pt 11pt; margin: 0 0 8pt; }
.stem { margin: 0 0 7pt; }
ol.choices { list-style: none; margin: 0; padding: 0; }
ol.choices li { margin: 0 0 3pt; padding: 3pt 7pt; border: 1px solid #E4E7EC; border-radius: 4px; }
ol.choices li.key { border: 2px solid #13683F; background: #EDF9F2; }
.lab { font-family: Helvetica, Arial, sans-serif; font-weight: bold; margin-right: 6pt; }
.keytag { font-family: Helvetica, Arial, sans-serif; font-size: 8.5pt; color: #13683F;
          font-weight: bold; margin-left: 6pt; }
.fr { border: 2px solid #13683F; background: #EDF9F2; border-radius: 4px; padding: 4pt 8pt;
      font-family: Helvetica, Arial, sans-serif; font-size: 10pt; }
.why { margin-top: 6pt; font-family: Helvetica, Arial, sans-serif; font-size: 9pt;
       color: #505866; border-left: 2px solid #D9DEE5; padding-left: 8pt; }
table { border-collapse: collapse; margin: 6pt 0; font-size: 9.5pt; }
th, td { border: 1px solid #D9DEE5; padding: 3pt 6pt; text-align: left; }
th { background: #F4F6F8; }
"""


def esc(s):
    return html.escape(s or "")


def render_table(t):
    """A data table, either as finished HTML or as [caption, headers, rows]."""
    if isinstance(t, str):
        return t
    caption, headers, rows = t
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    cap = f"<caption style='caption-side:top;text-align:left;font-weight:bold;padding-bottom:3pt;'>{caption}</caption>" if caption else ""
    return f"<table>{cap}<tr>{head}</tr>{body}</table>"


def render_question(q, n, subject):
    tags = f'<span class="tag">{esc(q["domain"])} / {esc(q["skill"])}</span>'
    tags += f'<span class="tag">{esc(q["difficulty"])}</span>'
    if q["type"] == "FREE_RESPONSE":
        tags += '<span class="tag">student-produced response</span>'

    parts = [f'<div class="q"><div class="qhead"><span class="qnum">{n}</span>{tags}</div>']

    if q.get("passage"):
        parts.append(f'<div class="passage">{q["passage"]}</div>')
    if q.get("table"):
        parts.append(render_table(q["table"]))

    parts.append(f'<div class="stem">{q["stem"]}</div>')

    if q["type"] == "MULTIPLE_CHOICE":
        parts.append("<ol class=\"choices\">")
        for c in q["choices"]:
            cls = ' class="key"' if c["isCorrect"] else ""
            tag = '<span class="keytag">&#10003; correct answer</span>' if c["isCorrect"] else ""
            parts.append(f'<li{cls}><span class="lab">{c["label"]}</span>{c["content"]}{tag}</li>')
        parts.append("</ol>")
    else:
        answers = json.loads(q["correctAnswerFR"])
        parts.append(f'<div class="fr">Accepted answer(s): <strong>{esc(" or ".join(answers))}</strong></div>')

    rationale = q.get("why") or q.get("check")
    if rationale:
        label = "Why this answer" if subject == "RW" else "Derivation"
        parts.append(f'<div class="why"><strong>{label}.</strong> {esc(rationale)}</div>')

    parts.append("</div>")
    return "".join(parts)


def main():
    test = json.load(open(os.path.join(HERE, "test7.json")))

    counts = {k: len(v) for k, v in test.items()}
    rows = "".join(
        f"<tr><td>{esc(title)}</td><td>{esc(diff)}</td><td>{counts[key]}</td>"
        f"<td>{sum(1 for q in test[key] if q['type']=='FREE_RESPONSE') or '&mdash;'}</td></tr>"
        for key, title, diff, _ in TITLES
    )

    body = [f"""
<div class="cover">
  <h1>SATForge Practice Test 7</h1>
  <p class="sub">Full review copy &mdash; 147 questions, answer key and reasoning included</p>
  <table>
    <tr><th>Module</th><th>Difficulty</th><th>Questions</th><th>Free response</th></tr>
    {rows}
  </table>
  <div class="note">
    <strong>Nothing in this test is reused.</strong> The Math is written from scratch and every
    answer re-derived with sympy from the question itself. Each stem was checked against all 396
    Math questions already live in the bank using a template-similarity measure that ignores the
    numbers, so a question that reuses an old template with new values is rejected, not just an
    exact duplicate. The highest remaining similarity is 0.73, against a 0.75 limit.
    Reading &amp; Writing is drawn from material never used in any published test, and the one
    remaining gap was authored here.
  </div>
  <div class="note">
    <strong>Difficulty is stamped per question, matching its module</strong> &mdash; the Test 1/2
    convention. Tests 3&ndash;6 left every question <em>MEDIUM</em> regardless of which module it
    sat in, which is why their Question Bank difficulty badges and filters are wrong. This test
    does not repeat that.
  </div>
  <div class="note">
    <strong>Status: not published.</strong> This is for review. Nothing has been written to the
    database.
  </div>
</div>
"""]

    for key, title, diff, expected in TITLES:
        items = test[key]
        subject = "RW" if key.startswith("RW") else "MATH"
        body.append(
            f'<div class="modhead"><h2>{esc(title)}</h2>'
            f'<p>{esc(diff)} &middot; {len(items)} questions &middot; '
            f'{"32" if subject == "RW" else "35"} minutes</p></div>'
        )
        for i, q in enumerate(items, 1):
            body.append(render_question(q, i, subject))

    page = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>SATForge Practice Test 7</title>
<link rel="stylesheet" href="{os.path.join(ROOT, 'node_modules/katex/dist/katex.min.css')}">
<style>{CSS}</style></head>
<body>{''.join(body)}
<script src="{os.path.join(ROOT, 'node_modules/katex/dist/katex.min.js')}"></script>
<script src="{os.path.join(ROOT, 'node_modules/katex/dist/contrib/auto-render.min.js')}"></script>
<script>
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "\\\\[", right: "\\\\]", display: true}},
      {{left: "\\\\(", right: "\\\\)", display: false}}
    ],
    throwOnError: false
  }});
  window.__katexDone = true;
</script>
</body></html>"""

    html_path = os.path.join(HERE, "test7_review.html")
    open(html_path, "w").write(page)
    print(f"wrote {html_path}")

    pdf_path = os.path.join(HERE, "SATForge-Practice-Test-7-review.pdf")
    script = f"""
import {{ chromium }} from "playwright-core";
const b = await chromium.launch({{
  executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  args: ["--no-sandbox", "--allow-file-access-from-files"],
}});
const p = await (await b.newContext()).newPage();
const errs = [];
p.on("pageerror", e => errs.push(String(e)));
await p.goto("file://{html_path}", {{ waitUntil: "networkidle" }});
await p.waitForFunction(() => window.__katexDone === true, {{ timeout: 30000 }});
await p.waitForTimeout(1200);
const unrendered = await p.evaluate(() =>
  (document.body.innerText.match(/\\\\\\(|\\\\\\[|\\\\frac|\\\\sqrt/g) || []).length);
await p.pdf({{ path: "{pdf_path}", format: "A4", printBackground: true,
  margin: {{ top: "16mm", bottom: "18mm", left: "14mm", right: "14mm" }},
  displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: '<div style="width:100%;font-size:8pt;color:#9BA3AF;font-family:Helvetica;padding:0 14mm;text-align:center;">SATForge Practice Test 7 — review copy — page <span class="pageNumber"></span> of <span class="totalPages"></span></div>' }});
console.log("unrendered LaTeX fragments left on the page: " + unrendered);
if (errs.length) console.log("page errors: " + errs.join("; "));
await b.close();
"""
    js_path = os.path.join(HERE, "_pdf.mjs")
    open(js_path, "w").write(script)
    res = subprocess.run(["node", js_path], capture_output=True, text=True, cwd=ROOT)
    print(res.stdout.strip() or res.stderr.strip()[:600])
    os.remove(js_path)
    if os.path.exists(pdf_path):
        print(f"wrote {pdf_path}  ({os.path.getsize(pdf_path)/1024:.0f} KB)")
    else:
        sys.exit("PDF was not produced")


if __name__ == "__main__":
    main()
