/**
 * KaTeX receives the raw contents of a \( … \) span, so an HTML entity written
 * inside one is passed through literally: `k &gt; 5a` renders as the visible
 * text "k &gt; 5a" in KaTeX's error colour instead of "k > 5a".
 *
 * Outside a math span `&lt;` / `&gt;` are correct HTML and must stay, so the
 * replacement is scoped to the inside of each span and nowhere else. That is
 * the whole point — a blanket entity decode would corrupt every stem that
 * legitimately writes a less-than sign in prose.
 *
 *   PROD_URL='postgresql://...' node fix_entities.mjs [--apply]
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");

const IMG = /<img[^>]*>/gi;
const SPAN = /(\\\()([\s\S]*?)(\\\))|(\\\[)([\s\S]*?)(\\\])/g;
const MAP = {
  "&lt;": "<", "&gt;": ">", "&le;": "\\le ", "&ge;": "\\ge ",
  "&ne;": "\\ne ", "&minus;": "-", "&times;": "\\times ",
  "&divide;": "\\div ", "&amp;": "\\&",
};
const ENT = new RegExp(Object.keys(MAP).join("|"), "g");

function fix(html) {
  if (!html) return null;
  // Hold image payloads aside: base64 can contain any byte sequence.
  // The sentinel has to be something the content cannot contain: a bare
  // ` 0 ` placeholder would be matched by every ordinary number in a stem on
  // the way back, silently swapping a "5" for an image or for undefined.
  const imgs = [];
  const held = html.replace(IMG, (m) => { imgs.push(m); return "@@IMG" + (imgs.length - 1) + "@@"; });
  let changed = false;
  const out = held.replace(SPAN, (m, o1, in1, c1, o2, in2, c2) => {
    const open = o1 ?? o2, inner = in1 ?? in2, close = c1 ?? c2;
    ENT.lastIndex = 0;
    if (!ENT.test(inner)) return m;
    changed = true;
    ENT.lastIndex = 0;
    return open + inner.replace(ENT, (e) => MAP[e]) + close;
  });
  if (!changed) return null;
  return out.replace(/@@IMG(\d+)@@/g, (_, i) => imgs[Number(i)]);
}

const rows = await sql.query('SELECT id, stem FROM "Question" WHERE "isPublished"');
const chs = await sql.query(
  `SELECT a.id, a.content FROM "AnswerChoice" a
     JOIN "Question" q ON q.id = a."questionId" WHERE q."isPublished"`);

let sn = 0, cn = 0;
for (const r of rows) {
  const next = fix(r.stem);
  if (next === null) continue;
  sn++;
  if (!APPLY) continue;
  // Every write is gated on the row still holding exactly the text that was
  // read, so a concurrent edit can never be silently clobbered.
  const res = await sql.query(
    `UPDATE "Question" SET stem = $1, "updatedAt" = now()
      WHERE id = $2 AND stem = $3 RETURNING id`, [next, r.id, r.stem]);
  if (!res.length) throw new Error(`stem changed under us: ${r.id}`);
}
for (const c of chs) {
  const next = fix(c.content);
  if (next === null) continue;
  cn++;
  if (!APPLY) continue;
  const res = await sql.query(
    `UPDATE "AnswerChoice" SET content = $1 WHERE id = $2 AND content = $3 RETURNING id`,
    [next, c.id, c.content]);
  if (!res.length) throw new Error(`choice changed under us: ${c.id}`);
}
console.log(`${APPLY ? "APPLIED" : "DRY RUN"}: ${sn} stems, ${cn} choices`);
