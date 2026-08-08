#!/usr/bin/env python3
"""
Fix Math questions that shipped with raw plain-text notation instead of KaTeX.

The bug: `verify_math_authored_mc.py` and `verify_math_m2easy.py` check house
style only on questions authored in this directory. The questions pulled from
`content-pool/new-source-transcripts/` were transcribed as plain text -- "f(x) =
250(5)^x", "26 + 26*sqrt(2)", "y = 18(2)^(x/29)", "3/5" -- and nothing ever
converted them, so they render with literal carets, asterisks and slashes
instead of exponents, radicals and fractions.

A scan of all 396 live Math questions for `^`, `sqrt(`, `*` and slash-fractions
appearing outside a `\\( \\)` or `\\[ \\]` span found 12 real cases: 9 in Test 6
(from that transcribed pool), 1 in Test 2 and 1 in Test 3. A 13th hit in Test 3
was a false positive -- the pattern matched inside a base64 `<img>` data URI,
which is the trap CLAUDE.md warns about.

Every replacement below is typed by hand, per standing rule 2: no bulk
auto-conversion, and every span checked for the specific defects a converter
gets wrong (escaped function names, thousands separators as `{,}` so KaTeX does
not add spacing, no prose inside math mode).

Rows are matched by (test title, subject, module order, difficulty, question
order) because IDs differ between local and production, and every write asserts
a distinctive substring is present in the row first.

  DATABASE_URL='postgresql://...' python3 fix_math_rendering.py [--apply]
"""
import os
import sys
import json
import subprocess

APPLY = "--apply" in sys.argv

# (title, subject, module order, difficulty, question order) ->
#   dict(assert=<substring that must be present>, stem=<new stem or None>,
#        choices=[(old, new), ...])
FIXES = {
 ("Test 6", "MATH", 1, "STANDARD", 9): dict(
   assert_="customer loyalty program",
   stem=("A company has a customer loyalty program. In January 2018, there were 1,600 customers "
         "enrolled in the loyalty program. For the next 24 months after January 2018, the total "
         "number of customers enrolled in the loyalty program each month was 5% greater than the "
         "total number enrolled the previous month. Which equation gives the total number of "
         "customers, c, enrolled in the company's loyalty program m months after January 2018, "
         "where \\(m\\le 24\\)?"),
   choices=[("c = 1,600(0.05)^m", "\\(c=1{,}600(0.05)^{m}\\)"),
            ("c = 1,600(1.05)^m", "\\(c=1{,}600(1.05)^{m}\\)"),
            ("c = 1,600(1.5)^m",  "\\(c=1{,}600(1.5)^{m}\\)"),
            ("c = 1,600(5)^m",    "\\(c=1{,}600(5)^{m}\\)")]),

 ("Test 6", "MATH", 1, "STANDARD", 11): dict(
   assert_="isosceles right triangle has a perimeter",
   stem=("An isosceles right triangle has a perimeter of \\(26+26\\sqrt{2}\\). What is the length "
         "of the hypotenuse of the triangle?"),
   # all four wrapped: a plain "13" sitting beside a KaTeX-italic
   # \(13\sqrt{2}\) in the same list is the inconsistency CLAUDE.md flags
   choices=[("13", "\\(13\\)"), ("26", "\\(26\\)"),
            ("13*sqrt(2)", "\\(13\\sqrt{2}\\)"),
            ("26*sqrt(2)", "\\(26\\sqrt{2}\\)")]),

 ("Test 6", "MATH", 1, "STANDARD", 12): dict(
   assert_="which of the following equations defines the function g",
   stem=("\\[f(x)=250(5)^{x}\\]The function f is defined by the given equation. If \\(g(x)=f(x-2)\\), "
         "which of the following equations defines the function g?"),
   choices=[("g(x) = 10(5)^x",   "\\(g(x)=10(5)^{x}\\)"),
            ("g(x) = 125(5)^x",  "\\(g(x)=125(5)^{x}\\)"),
            ("g(x) = 250(25)^x", "\\(g(x)=250(25)^{x}\\)"),
            ("g(x) = 250(10)^x", "\\(g(x)=250(10)^{x}\\)")]),

 ("Test 6", "MATH", 1, "STANDARD", 14): dict(
   assert_="sealed container doubles every 29 minutes",
   stem=None,
   choices=[("y = 18(2)^(x/29)",     "\\(y=18(2)^{\\frac{x}{29}}\\)"),
            ("y = 18(2)^(29x)",      "\\(y=18(2)^{29x}\\)"),
            ("y = 29(2)^(x/18)",     "\\(y=29(2)^{\\frac{x}{18}}\\)"),
            ("y = 18 + (2)^(x/29)",  "\\(y=18+(2)^{\\frac{x}{29}}\\)")]),

 ("Test 6", "MATH", 1, "STANDARD", 20): dict(
   assert_="product of the solutions to the given equation is krs",
   stem=("\\[56x^{2}+(56s+r)x+rs=0\\]In the given equation, r and s are positive constants. The "
         "product of the solutions to the given equation is krs, where k is a constant. What is the "
         "value of k?"),
   choices=[]),

 ("Test 6", "MATH", 2, "EASY", 2): dict(
   assert_="machine fills 45 bottles each minute",
   stem=None,
   # all four wrapped, not just the fraction: a lone KaTeX choice sitting beside
   # three plain-text siblings is the inconsistency CLAUDE.md flags
   choices=[("B=45+m", "\\(B=45+m\\)"), ("B=45m", "\\(B=45m\\)"),
            ("B=m/45", "\\(B=\\frac{m}{45}\\)"), ("B=45-m", "\\(B=45-m\\)")]),

 ("Test 6", "MATH", 2, "HARD", 3): dict(
   assert_="what is the value of a?",
   stem=("\\[f(x)=\\sqrt{5x+6}\\]The function f is defined by the given equation. If \\(f(a)=-5a\\), "
         "where a is a constant, what is the value of a?"),
   choices=[("3/5", "\\(\\frac{3}{5}\\)"), ("2/5", "\\(\\frac{2}{5}\\)"),
            ("-2/5", "\\(-\\frac{2}{5}\\)"), ("-3/5", "\\(-\\frac{3}{5}\\)")]),

 ("Test 6", "MATH", 2, "HARD", 18): dict(
   assert_="increase by p% for every increase of x by 4",
   stem=("\\[f(x)=k(1.84)^{x}\\]The function f is defined by the given equation, where k is a "
         "constant. The value of f(x) increases by p% for every increase of x by 1. For which of the "
         "following functions, where k is a constant, does the value of g(x) increase by p% for every "
         "increase of x by 4?"),
   choices=[("g(x) = k(1.84^x)^{1/4}", "\\(g(x)=k\\left(1.84^{x}\\right)^{\\frac{1}{4}}\\)"),
            ("g(x) = k(1.84^x)^4",     "\\(g(x)=k\\left(1.84^{x}\\right)^{4}\\)"),
            ("g(x) = k(1.84)^{x-4}",   "\\(g(x)=k(1.84)^{x-4}\\)"),
            ("g(x) = k(1.84)^{x+4}",   "\\(g(x)=k(1.84)^{x+4}\\)")]),

 ("Test 6", "MATH", 2, "HARD", 19): dict(
   assert_="length of arc DA is 2 times the length of arc AB",
   stem=("A circle has diameters AC and BD. The circumference of the circle is \\(84\\pi\\), and the "
         "length of arc DA is 2 times the length of arc AB. What is the length of arc BC?"),
   choices=[("2\\pi", "\\(2\\pi\\)"), ("14\\pi", "\\(14\\pi\\)"),
            ("21\\pi", "\\(21\\pi\\)"), ("28\\pi", "\\(28\\pi\\)")]),

 ("Test 6", "MATH", 2, "HARD", 21): dict(
   assert_="number of bacteria in the population to double",
   stem=("\\[f(t)=10{,}000(2)^{\\frac{t}{350}}\\]The given function f gives the number of bacteria in "
         "a population t minutes after an initial observation. How much time, in minutes, does it "
         "take for the number of bacteria in the population to double?"),
   choices=[]),

 ("Test 2", "MATH", 2, "HARD", 11): dict(
   assert_="Which expression is equivalent to",
   stem="Which expression is equivalent to \\(x^{-3}\\cdot x^{7}\\) for \\(x\\ne 0\\)?",
   choices=[]),

 # --- ASCII comparison operators and bare trig, found by the DB-wide audit ---
 # These predate Test 6: the same transcription habit that produced "^" also
 # left "!=", "<=" and "sin(theta)" as plain text in Tests 1-4.
 ("Test 1", "MATH", 2, "EASY", 13): dict(
   assert_="x^{3} \\times",
   stem=("Which expression is equivalent to \\(\\frac{x^{3}\\times x^{5}}{x^{2}}\\) for all "
         "\\(x\\ne 0\\)?"),
   choices=[]),

 ("Test 2", "MATH", 1, "STANDARD", 13): dict(
   assert_="\\frac{x^{2} - 9}{x - 3}",
   stem="Which expression is equivalent to \\(\\frac{x^{2}-9}{x-3}\\) for \\(x\\ne 3\\)?",
   choices=[]),

 ("Test 2", "MATH", 2, "EASY", 5): dict(
   assert_="represents all values of x that satisfy",
   stem=("Which of the following represents all values of x that satisfy "
         "\\(-3<2x+1\\le 9\\)?"),
   choices=[("-2 < x <= 4", "\\(-2<x\\le 4\\)"), ("-2 < x <= 5", "\\(-2<x\\le 5\\)"),
            ("-1 < x <= 4", "\\(-1<x\\le 4\\)"), ("-1 < x <= 5", "\\(-1<x\\le 5\\)")]),

 ("Test 2", "MATH", 2, "EASY", 14): dict(
   assert_="\\frac{3}{x}",
   stem=("If \\(\\frac{3}{x}=\\frac{1}{4}\\) and \\(x\\ne 0\\), what is the value of x?"),
   choices=[]),

 ("Test 2", "MATH", 2, "EASY", 20): dict(
   assert_="one of the acute angles",
   # theta was spelled out and sin/cos were bare, so they rendered upright and
   # unspaced instead of as function names
   stem=("In a right triangle, one of the acute angles, \\(\\theta\\), satisfies "
         "\\(\\sin\\theta=\\frac{3}{5}\\). What is the value of "
         "\\(\\cos(90^{\\circ}-\\theta)\\)?"),
   choices=[]),

 ("Test 4", "MATH", 2, "HARD", 4): dict(
   assert_="sum of the measures of angle R and angle S",
   # the "/13" sat OUTSIDE the \( \) span, so the value rendered as a typeset
   # radical followed by a literal slash and 13
   stem=("In right triangle RST, the sum of the measures of angle R and angle S is 90&deg;. "
         "The value of \\(\\sin R\\) is \\(\\frac{3\\sqrt{17}}{13}\\). What is the value of "
         "\\(\\cos S\\)?"),
   choices=[]),

 ("Test 6", "MATH", 1, "STANDARD", 17): dict(
   assert_="renting a piece of construction equipment",
   stem=("The cost of renting a piece of construction equipment for up to 5 days is $230 for "
         "the first day and $115 for each additional day. Which of the following equations "
         "gives the cost y, in dollars, of renting the equipment for x days, where x is a "
         "positive integer and \\(x\\le 5\\)?"),
   choices=[("y = 230x + 115", "\\(y=230x+115\\)"), ("y = 230x - 115", "\\(y=230x-115\\)"),
            ("y = 115x + 230", "\\(y=115x+230\\)"), ("y = 115x + 115", "\\(y=115x+115\\)")]),

 ("Test 3", "MATH", 2, "HARD", 3): dict(
   assert_="the length of YZ is 22 units",
   stem=("In triangle XYZ, angle Y is a right angle, the measure of angle Z is 39&deg;, and the "
         "length of YZ is 22 units. If the area, in square units, of triangle XYZ can be represented "
         "by the expression \\(k\\tan 39^{\\circ}\\), where k is a constant, what is the value of k?"),
   choices=[]),
}

JS = r"""
const isLocal = /localhost|127\.0\.0\.1/.test(process.env.DATABASE_URL);
let sql, pgClient;
if (isLocal) {
  const pg = (await import("pg")).default;
  pgClient = new pg.Client({ connectionString: process.env.DATABASE_URL });
  await pgClient.connect();
  sql = async (strings, ...values) => {
    const text = strings.reduce((a, s, i) => a + s + (i < values.length ? `$${i + 1}` : ""), "");
    return (await pgClient.query(text, values)).rows;
  };
} else {
  const { neon } = await import("@neondatabase/serverless");
  sql = neon(process.env.DATABASE_URL);
}
const FIXES = __FIXES__;
const APPLY = __APPLY__;
let changed = 0, skipped = 0;
for (const f of FIXES) {
  const rows = await sql`
    SELECT q.id, q.stem FROM "Question" q
    JOIN "Module" m ON m.id = q."moduleId" JOIN "Test" t ON t.id = m."testId"
    WHERE t.title = ${f.title} AND m.subject = ${f.subject} AND m."order" = ${f.mo}
      AND m.difficulty = ${f.diff} AND q."order" = ${f.qo}`;
  if (rows.length !== 1) { console.log(`  !! ${f.label}: matched ${rows.length} rows`); skipped++; continue; }
  const row = rows[0];
  if (!row.stem.includes(f.assert)) {
    console.log(`  !! ${f.label}: assertion ${JSON.stringify(f.assert)} NOT in stem — refusing`);
    skipped++; continue;
  }
  if (f.stem && f.stem !== row.stem) {
    if (APPLY) await sql`UPDATE "Question" SET stem = ${f.stem}, "updatedAt" = now() WHERE id = ${row.id}`;
    console.log(`  ${APPLY ? "stem  " : "would"} ${f.label}`);
    changed++;
  }
  for (const [oldC, newC] of f.choices) {
    const hit = await sql`SELECT id, content FROM "AnswerChoice" WHERE "questionId" = ${row.id} AND content = ${oldC}`;
    if (hit.length !== 1) { console.log(`     .. choice ${JSON.stringify(oldC)} not found (already fixed?)`); continue; }
    if (APPLY) await sql`UPDATE "AnswerChoice" SET content = ${newC} WHERE id = ${hit[0].id}`;
    changed++;
  }
}
console.log(`\n${APPLY ? "applied" : "dry run"}: ${changed} edits, ${skipped} skipped`);
if (pgClient) await pgClient.end();
"""

payload = []
for (title, subject, mo, diff, qo), f in FIXES.items():
    payload.append(dict(title=title, subject=subject, mo=mo, diff=diff, qo=qo,
                        label=f"{title} {subject} M{mo}{diff[:1]} Q{qo}",
                        assert_=f["assert_"], **{"assert": f["assert_"]},
                        stem=f["stem"], choices=f["choices"]))

script = JS.replace("__FIXES__", json.dumps(payload)).replace("__APPLY__", "true" if APPLY else "false")
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "_fix_math.mjs")
open(out, "w").write(script)
target = "production" if "localhost" not in os.environ.get("DATABASE_URL", "") else "local"
print(f"target: {target}   mode: {'APPLY' if APPLY else 'dry run'}\n")
subprocess.run(["node", out], check=True, cwd=here)
