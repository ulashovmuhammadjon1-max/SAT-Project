/**
 * Audit every Explanation row against the question it explains.
 *
 *     PROD_URL=… node audit_explanations.mjs
 *
 * The failure that matters is an explanation that disagrees with the key it is
 * attached to — a student reads it, believes it, and learns the error. That is
 * strictly worse than the blank page it replaced, which is why the authoring
 * gate exists. But the gate only ran at write time: a key edited afterwards
 * leaves the explanation behind, still confidently arguing the old answer.
 * 21 keys were flipped in this session, so that is not hypothetical.
 *
 * The strongest signal is structural rather than textual. `whyWrongJson` is
 * keyed by choice letter, so if it carries an entry for the letter now marked
 * correct, the explanation is on record calling the right answer wrong. No
 * prose parsing needed, and it cannot be argued with.
 *
 * The style checks repeat the ones from verify.mjs deliberately — those ran
 * against the authored JSONL, not against what is actually in the database,
 * and rows have been written by several different paths (agents, official
 * rationales, hand repairs) over the life of the project.
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);

const rows = await sql`
  SELECT e.id, e."questionId", e.content, e."whyCorrect", e."whyWrongJson",
         e."commonMistakes", e.tips, e.source,
         q.stem, q.type, q."correctAnswerFR",
         t.title AS test, m.subject, m."order" AS mo, m.difficulty AS br, q."order" AS qo
  FROM "Explanation" e
  JOIN "Question" q ON q.id = e."questionId"
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  WHERE q."isPublished" = true`;

const choices = await sql`
  SELECT c."questionId", c.label, c."isCorrect"
  FROM "AnswerChoice" c
  JOIN "Question" q ON q.id = c."questionId"
  WHERE q."isPublished" = true`;
const byQ = new Map();
for (const c of choices) {
  if (!byQ.has(c.questionId)) byQ.set(c.questionId, []);
  byQ.get(c.questionId).push(c);
}

const findings = new Map();
const add = (r, what, detail = "") => {
  if (!findings.has(what)) findings.set(what, []);
  findings.get(what).push({ r, detail });
};

const strip = (s) => (s || "").replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim();
const seen = new Map();

for (const r of rows) {
  const cs = byQ.get(r.questionId) ?? [];
  const key = cs.find((c) => c.isCorrect)?.label;

  // ── the one that matters ────────────────────────────────────────────────
  let ww = r.whyWrongJson;
  if (typeof ww === "string") { try { ww = JSON.parse(ww); } catch { ww = null; } }
  if (ww && typeof ww === "object" && key && Object.keys(ww).includes(key))
    add(r, "CONTRADICTS THE KEY — calls the correct choice wrong", `key ${key}`);

  if (ww && typeof ww === "object" && key) {
    const wrong = cs.filter((c) => !c.isCorrect).map((c) => c.label);
    const missing = wrong.filter((l) => !Object.keys(ww).includes(l));
    if (missing.length && Object.keys(ww).length)
      add(r, "no reason given for some distractors", `missing ${missing.join(",")}`);
    for (const [l, v] of Object.entries(ww))
      if (!cs.some((c) => c.label === l)) add(r, "reason for a choice that does not exist", l);
      else if (!strip(v)) add(r, "empty reason for a distractor", l);
  }

  // ── empty or stub bodies ────────────────────────────────────────────────
  const body = strip(r.content);
  if (!body) add(r, "empty explanation body");
  else if (body.length < 40) add(r, "explanation body under 40 chars", body.slice(0, 40));
  if (!strip(r.whyCorrect) && r.source !== "MANUAL") add(r, "whyCorrect empty");

  // ── rendering / house style ─────────────────────────────────────────────
  const text = [r.whyCorrect, ...(ww ? Object.values(ww) : []), r.commonMistakes, r.tips]
    .filter(Boolean).join(" ");
  if (/\*[^*\n]{2,}\*/.test(text)) add(r, "markdown asterisks");
  if (/\$(?!\d)[^$\n]{1,80}\$/.test(text)) add(r, "$…$ math instead of \\( \\)");
  const outside = text.replace(/\\\((.|\n)*?\\\)/g, "");
  if (/\\(frac|sqrt|pi|cdot|times|le|ge|ne)(?![a-z])/.test(outside))
    add(r, "LaTeX macro outside a math span");
  if (/&lt;(p|strong|em|li|ul)&gt;/i.test(r.content || ""))
    add(r, "escaped HTML — tags would render as visible text");
  for (const tag of ["p", "li", "ul", "strong", "em"]) {
    const o = ((r.content || "").match(new RegExp(`<${tag}(?![a-z])[^>]*>`, "gi")) ?? []).length;
    const c = ((r.content || "").match(new RegExp(`</${tag}>`, "gi")) ?? []).length;
    if (o !== c) add(r, `unbalanced <${tag}> in the body`);
  }

  // ── the same explanation on two different questions ─────────────────────
  // Compared on the WHOLE body, not a prefix. A 160-character signature
  // reported six false positives: College Board's rationales for Standard
  // English Conventions all open "Choice C is the best answer. The convention
  // being tested is punctuation use between sentences." — that is their house
  // formula, and the explanations diverge immediately after it. Matching on
  // the opening of a formulaic genre finds the genre, not a duplicate.
  if (body.length > 40) {
    if (seen.has(body) && seen.get(body) !== r.questionId)
      add(r, "body byte-identical to another question's");
    else seen.set(body, r.questionId);
  }
}

console.log(`audited ${rows.length} explanations on published questions\n`);
if (!findings.size) console.log("no findings");
for (const [what, hits] of [...findings].sort((a, b) => b[1].length - a[1].length)) {
  console.log(`${String(hits.length).padStart(5)}  ${what}`);
  for (const h of hits.slice(0, 6))
    console.log(`        ${h.r.test} ${h.r.subject === "MATH" ? "Math" : "R&W"} M${h.r.mo}${h.r.br} q${h.r.qo}` +
                `${h.detail ? "  " + h.detail : ""}  ${h.r.questionId}`);
  if (hits.length > 6) console.log(`        … and ${hits.length - 6} more`);
}
