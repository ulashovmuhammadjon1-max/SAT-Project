/**
 * Audit EVERY live Math question for plain-text math that should be KaTeX.
 *
 * The gap this closes: `verify_math_m2easy.py` and `verify_math_authored_mc.py`
 * only ever saw questions authored in this directory. Questions imported from
 * `content-pool/new-source-transcripts/` were transcribed as plain text and no
 * check ever looked at them, so `f(x) = 250(5)^x`, `26 + 26*sqrt(2)` and `3/5`
 * shipped to production rendering as literal carets, asterisks and slashes.
 *
 * This runs over the database rather than over a source file, so it covers
 * transcribed and authored content alike. Run it against local and production
 * before publishing any test.
 *
 *   DATABASE_URL='postgresql://...' node audit_math_rendering.mjs
 *
 * Exits 1 if anything is flagged.
 */
const isLocal = /localhost|127\.0\.0\.1/.test(process.env.DATABASE_URL || "");
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

// Base64 image payloads false-positive on every pattern below (CLAUDE.md warns
// about exactly this), so strip <img> tags before looking at anything.
const stripImages = (s) => (s || "").replace(/<img[^>]*>/gi, " ");

// Spans of real math. Anything flagged inside one of these is fine.
function mathSpans(s) {
  const spans = [];
  const re = /\\\((.*?)\\\)|\\\[(.*?)\\\]/gs;
  let m;
  while ((m = re.exec(s)) !== null) spans.push([m.index, m.index + m[0].length]);
  return spans;
}
const inMath = (spans, i) => spans.some(([a, b]) => a <= i && i < b);

// severity "error" = renders as raw notation the student can see is wrong.
// severity "style" = renders readably but is not the house convention.
const CHECKS = [
  // literal exponent caret rendering as "^"
  [/\^/g, "caret outside math mode", "error"],
  // plain-text radical
  [/\bsqrt\s*\(/gi, "plain-text sqrt(", "error"],
  // asterisk used as a multiplication sign. Letter-or-paren on the left too,
  // so "k*tan(...)" is caught and not just "26*sqrt(2)".
  [/[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]/g, "asterisk multiplication", "error"],
  // a function name written as bare text renders upright and unspaced
  [/(?<!\\)\b(sin|cos|tan|log|ln)\s*\(/g, "bare function call outside math mode", "error"],
  // a Greek letter spelled out in prose
  [/(?<![A-Za-z\\])(theta|alpha|beta|lambda|mu|sigma)(?![A-Za-z])/g,
   "Greek letter spelled out", "error"],
  // slash fraction between bare numbers, e.g. "3/5" — but not dates, ratios
  // written as words, or URLs
  [/(?<![\d\/:])\d+\s*\/\s*\d+(?![\d\/])/g, "slash fraction", "error"],
  // a lone unicode radical or plain-text pi. The `pi` lookaround is
  // letter-specific, not \b: a digit is a word char, so \bpi\b never fires on
  // "3pi" (the mathify.mjs bug recorded in CLAUDE.md).
  [/√/g, "raw radical glyph", "error"],
  [/(?<![A-Za-z\\])pi(?![A-Za-z])/g, "plain-text 'pi'", "error"],
  // a LaTeX macro sitting outside any math span renders as literal backslash
  // text — this is how "2\pi" shipped in Test 6 M2H Q19
  [/\\(pi|frac|sqrt|cdot|le|ge|ne|times|div|circ|sin|cos|tan|log|ln)\b/g,
   "LaTeX macro outside math mode", "error"],
  // ASCII comparison operators that should be typeset
  [/(!=|<=|>=)/g, "ASCII comparison operator", "error"],
  // An angle written as "35 degrees" should be "35&deg;". A temperature that
  // names its scale — "34 degrees Celsius" — is correct prose and is not an
  // angle, so it is excluded rather than flagged.
  [/\d\s*degrees?\b(?!\s*(?:Celsius|Fahrenheit|Kelvin|C\b|F\b))/gi,
   "'degrees' spelled out instead of &deg;", "style"],
];

// Contexts where a slash is legitimately prose, not a fraction.
const SLASH_OK = /\b(miles?|kilometers?|km|meters?|m|hours?|hr|minutes?|min|seconds?|sec|dollars?|gallons?|liters?|L|feet|ft|inch(?:es)?|cm|mm|g|kg|lb)\s*\//i;

const rows = await sql`
  SELECT t.title, m.subject, m."order" AS mo, m.difficulty, q."order" AS qo,
         q.id, q.stem,
         COALESCE((SELECT string_agg(ac.content, '' ORDER BY ac."order")
                   FROM "AnswerChoice" ac WHERE ac."questionId" = q.id), '') AS choices
  FROM "Question" q
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  WHERE m.subject = 'MATH'
  ORDER BY t.title, m."order", m.difficulty, q."order"`;

const flagged = [];
for (const r of rows) {
  const blocks = [["stem", r.stem]];
  (r.choices || "").split("").filter(Boolean)
    .forEach((c, i) => blocks.push([`choice ${"ABCD"[i] || i}`, c]));

  const hits = [];
  for (const [where, raw] of blocks) {
    const s = stripImages(raw);
    const spans = mathSpans(s);
    for (const [re, label, sev] of CHECKS) {
      re.lastIndex = 0;
      let m;
      while ((m = re.exec(s)) !== null) {
        if (inMath(spans, m.index)) continue;
        if (label === "slash fraction") {
          const ctx = s.slice(Math.max(0, m.index - 24), m.index + m[0].length);
          if (SLASH_OK.test(ctx)) continue;
        }
        hits.push(`${sev === "error" ? "ERROR" : "style"}  ${where}: ${label} — ${JSON.stringify(
          s.slice(Math.max(0, m.index - 30), m.index + m[0].length + 30))}`);
      }
    }
  }
  if (hits.length) flagged.push({ r, hits, errors: hits.filter(h => h.startsWith("ERROR")).length });
}

const withErrors = flagged.filter(f => f.errors);
console.log(`scanned ${rows.length} Math questions across ${new Set(rows.map(r => r.title)).size} tests`);
console.log(`${withErrors.length} with rendering errors, ${flagged.length - withErrors.length} style-only\n`);
for (const { r, hits } of flagged) {
  console.log(`${r.title} ${r.subject} M${r.mo}${r.difficulty[0]} Q${r.qo}  (${r.id})`);
  for (const h of hits) console.log(`    ${h}`);
  console.log();
}
if (!flagged.length) console.log("clean: no plain-text math outside KaTeX spans");
if (pgClient) await pgClient.end();
process.exit(withErrors.length ? 1 : 0);
