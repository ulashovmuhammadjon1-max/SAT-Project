/**
 * Second Math cleanup pass: the "style" findings from audit_math_rendering.mjs.
 *
 * Two things, both required by standing rule 1 in CLAUDE.md ("Test 1 and Test 2
 * are the quality reference"):
 *
 * 1. `NN degrees` spelled out in prose becomes `NN&deg;`, which is what the
 *    real SAT prints. The prose form "the measure, in degrees, of angle F" is
 *    correct English and is left alone -- only a degree value attached to a
 *    number or to a math span is converted.
 *
 * 2. Test 3 and Test 4 wrap every Math stem in <p>...</p>; Tests 1, 2, 5 and 6
 *    wrap none. This unwraps Test 3/4 so all six tests match. Only stems that
 *    are exactly one paragraph are touched, and the unwrap is rejected if it
 *    would change anything other than the outer tags.
 *
 *   DATABASE_URL='postgresql://...' node fix_math_style.mjs [--apply]
 */
const APPLY = process.argv.includes("--apply");
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

// Stems that need more than the mechanical rule -- transcription damage around
// the degree symbol, hand-checked against the Test 1 wording of the same item.
//
// Matched on distinctive content, never on row id: local and production use
// different id schemes, so an id-keyed table silently no-ops on one of them.
const HAND = [
  // "40 degrees Fahrenheit (°F)" glosses a unit it then uses; SAT prints 40°F
  ["was 40 degrees Fahrenheit (°F) and",
   "was 40&deg;F and"],
  // Test 3's copy of the same item lost the degree symbol entirely: "90 F"
  ["was 10 degrees Fahrenheit and the highest temperature recorded was 90 F.",
   "was 10&deg;F and the highest temperature recorded was 90&deg;F."],
  ["any temperature, in F, recorded",
   "any temperature, in &deg;F, recorded"],
  // a degree value carried by a math span rather than by a bare number
  ["is \\(\\frac{k}{2}\\) degrees, where",
   "is \\(\\frac{k}{2}\\)&deg;, where"],
];

function degreeFix(s) {
  // Only a number immediately followed by "degrees"/"degree". Leaves the
  // adverbial "in degrees," alone, since nothing precedes it.
  s = s.replace(/(\d)\s*degrees?(?![a-z])/gi, "$1&deg;");
  // a raw ° glyph is the house style's other spelling of the same thing; a
  // stem carrying both reads as two different conventions in one sentence.
  // Only outside math spans -- inside one the right form is ^{\circ}.
  const spans = [...s.matchAll(/\\\((.*?)\\\)|\\\[(.*?)\\\]/gs)]
    .map((m) => [m.index, m.index + m[0].length]);
  let out = "";
  for (let i = 0; i < s.length; i++) {
    const guarded = spans.some(([a, b]) => a <= i && i < b);
    out += (s[i] === "°" && !guarded) ? "&deg;" : s[i];
  }
  return out;
}

function unwrap(s) {
  const t = s.trim();
  if (!t.startsWith("<p>") || !t.endsWith("</p>")) return null;
  const inner = t.slice(3, -4);
  // reject multi-paragraph stems -- unwrapping those would join two paragraphs
  if (/<\/?p[\s>]/i.test(inner)) return null;
  return inner;
}

const rows = await sql`
  SELECT t.title, m."order" AS mo, m.difficulty, q."order" AS qo, q.id, q.stem
  FROM "Question" q
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  WHERE m.subject = 'MATH'
  ORDER BY t.title, m."order", m.difficulty, q."order"`;

let deg = 0, unw = 0, hand = 0, refused = 0;
const handHits = new Map();
for (const r of rows) {
  let next = r.stem;

  for (const [from, to] of HAND) {
    if (!next.includes(from)) continue;
    next = next.split(from).join(to);
    hand++;
    handHits.set(from, (handHits.get(from) || 0) + 1);
  }

  const afterDeg = degreeFix(next);
  if (afterDeg !== next) deg++;
  next = afterDeg;

  if (r.title === "Test 3" || r.title === "Test 4") {
    const u = unwrap(next);
    if (u !== null) {
      // the unwrap must change the outer tags and nothing else
      if (`<p>${u}</p>` !== next.trim()) {
        console.log(`  !! ${r.title} M${r.mo}${r.difficulty[0]} Q${r.qo}: unwrap not lossless — refusing`);
        refused++;
      } else {
        next = u;
        unw++;
      }
    }
  }

  if (next !== r.stem) {
    if (APPLY) await sql`UPDATE "Question" SET stem = ${next}, "updatedAt" = now() WHERE id = ${r.id}`;
  }
}

// answer choices carry "63 degrees" too
const choices = await sql`
  SELECT ac.id, ac.content FROM "AnswerChoice" ac
  JOIN "Question" q ON q.id = ac."questionId"
  JOIN "Module" m ON m.id = q."moduleId"
  WHERE m.subject = 'MATH' AND ac.content ~ '[0-9] ?degrees?'`;
let cdeg = 0;
for (const c of choices) {
  const next = degreeFix(c.content);
  if (next === c.content) continue;
  if (APPLY) await sql`UPDATE "AnswerChoice" SET content = ${next} WHERE id = ${c.id}`;
  cdeg++;
}

// A hand-fix that matched nothing means either the DB lacks that test or the
// stem drifted -- say which, rather than passing silently.
for (const [from] of HAND) {
  const n = handHits.get(from) || 0;
  if (n !== 1) console.log(`  note: hand-fix ${JSON.stringify(from.slice(0, 48))}… matched ${n} rows`);
}

console.log(`${APPLY ? "applied" : "dry run"}: ${hand} hand-fixed, ${deg} stems + ${cdeg} choices degree-normalized, ${unw} stems unwrapped, ${refused} refused`);
if (pgClient) await pgClient.end();
