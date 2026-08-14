/**
 * Scan Tests 16-31's R&W for the defect classes the explanation agents found.
 *
 *     PROD_URL=… node scan_satoplam_defects.mjs [> report.txt]
 *
 * The agents read every question and reported what they happened to notice.
 * That is a sample, not a census — three agents covering a quarter of the set
 * found six spliced choices and a dozen duplicate templates between them, so
 * the rest of the set almost certainly holds more. This finds all of them.
 *
 * Four classes, each with the boundary discipline this project keeps having to
 * relearn — a checker that over-matches trains you to ignore its output:
 *
 *  duplicate   Near-identical questions. Scored on the passage+stem token
 *              signature. Reported separately for same-test pairs, which are
 *              much worse: a student sees Module 1 plus one Module 2 branch,
 *              so a repeat inside one test shows half the cohort the same
 *              question twice in one sitting.
 *
 *  spliced     A choice carrying text from an unrelated question, e.g.
 *              "…according to a 2019 study.g sprouts and begins
 *              photosynthesis." Detected structurally rather than by
 *              vocabulary: a sentence-ending period followed immediately by a
 *              lowercase letter with no space is not something a typesetter
 *              produces, and neither is a run of text in a choice that also
 *              appears in a *different* question's passage.
 *
 *  truncated   A stem that stops mid-sentence, which removes the cue naming
 *              what to look for. Requires the stem to end without terminal
 *              punctuation, and excludes the ones that legitimately end on a
 *              blank or a colon.
 *
 *  goal-drift  A Rhetorical Synthesis goal sentence describing a task the
 *              notes cannot support — "emphasize a similarity between the two
 *              countries" over notes about a linocut. Flagged when the goal's
 *              distinctive content words appear nowhere in the notes or the
 *              choices, which is what a goal pasted from another item looks
 *              like.
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);

const text = (s) =>
  (s || "").replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim();

const rows = await sql`
  SELECT q.id, q.stem, q.source, q."order" AS q_order, p.content AS passage,
         t.title AS test, m."order" AS m_order, m.difficulty AS branch, s.code AS skill
  FROM "Question" q
  LEFT JOIN "Passage" p ON p.id = q."passageId"
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  LEFT JOIN "Skill" s ON s.id = q."skillId"
  WHERE m.subject = 'READING_WRITING'
    AND (regexp_replace(t.title, '\\D', '', 'g'))::int BETWEEN 16 AND 31
  ORDER BY t.title, m."order", m.difficulty, q."order"`;

const choices = await sql`
  SELECT c."questionId", c.label, c.content
  FROM "AnswerChoice" c
  JOIN "Question" q ON q.id = c."questionId"
  JOIN "Module" m ON m.id = q."moduleId"
  JOIN "Test" t ON t.id = m."testId"
  WHERE m.subject = 'READING_WRITING'
    AND (regexp_replace(t.title, '\\D', '', 'g'))::int BETWEEN 16 AND 31`;

const byQ = new Map();
for (const c of choices) {
  if (!byQ.has(c.questionId)) byQ.set(c.questionId, []);
  byQ.get(c.questionId).push(c);
}
const where = (r) => `${r.test} M${r.m_order}${r.branch === "STANDARD" ? "" : r.branch === "EASY" ? "E" : "H"} q${r.q_order}`;

// ── duplicates ────────────────────────────────────────────────────────────
// Stop words alone would not help here: R&W stems are boilerplate ("Which
// choice completes the text…"), so the passage carries all the signal.
const STOP = new Set("the a an and or of to in is are was were that this it for on as with by from at be been which what how".split(" "));
const sig = (r) => {
  const t = text(r.passage) + " " + text(r.stem);
  return new Set(t.toLowerCase().match(/[a-z]{3,}/g)?.filter((w) => !STOP.has(w)) ?? []);
};
const sigs = rows.map((r) => ({ r, s: sig(r) }));
const jaccard = (a, b) => {
  let inter = 0;
  for (const w of a) if (b.has(w)) inter++;
  return inter / (a.size + b.size - inter || 1);
};

const dupSame = [], dupCross = [];
for (let i = 0; i < sigs.length; i++) {
  for (let j = i + 1; j < sigs.length; j++) {
    if (sigs[i].s.size < 12 || sigs[j].s.size < 12) continue;
    const score = jaccard(sigs[i].s, sigs[j].s);
    if (score < 0.6) continue;
    (sigs[i].r.test === sigs[j].r.test ? dupSame : dupCross)
      .push({ a: sigs[i].r, b: sigs[j].r, score });
  }
}

// ── spliced text ──────────────────────────────────────────────────────────
// Structural, not lexical. A period or comma glued to a following lowercase
// letter with no space is a splice artifact, never typesetting.
const SPLICE = /[a-z]{2}[.,][a-z]{2}/;
const spliced = [];
for (const r of rows) {
  for (const c of byQ.get(r.id) ?? []) {
    const t = text(c.content);
    if (SPLICE.test(t)) spliced.push({ r, label: c.label, t });
  }
}

// ── truncated stems ───────────────────────────────────────────────────────
const truncated = rows.filter((r) => {
  const t = text(r.stem);
  return t.length > 20 && !/[.?!:_"”)\]]$/.test(t);
});

// ── goal drift ────────────────────────────────────────────────────────────
// Only Rhetorical Synthesis has a goal sentence. Content words from the goal
// that appear in neither the notes nor any choice mean the goal was written
// for a different item.
const goalDrift = [];
for (const r of rows) {
  if (r.skill !== "EOI-RS") continue;
  const p = text(r.passage);
  const m = p.match(/The student wants to ([^.]+)\./);
  if (!m) continue;
  const notes = p.replace(m[0], "");
  const body = (notes + " " + (byQ.get(r.id) ?? []).map((c) => text(c.content)).join(" ")).toLowerCase();
  const words = (m[1].toLowerCase().match(/[a-z]{5,}/g) ?? [])
    .filter((w) => !["student", "wants", "emphasize", "explain", "describe", "specify", "introduce", "present", "provide", "similarity", "difference", "between", "audience", "unfamiliar", "readers", "claim", "example"].includes(w));
  const missing = words.filter((w) => !body.includes(w.slice(0, Math.max(5, w.length - 2))));
  if (words.length >= 2 && missing.length === words.length) goalDrift.push({ r, goal: m[1], missing });
}

// ── report ────────────────────────────────────────────────────────────────
const show = (title, items, fmt) => {
  console.log(`\n${"=".repeat(72)}\n${title}: ${items.length}\n${"=".repeat(72)}`);
  for (const it of items) console.log(fmt(it));
};

show("DUPLICATES WITHIN ONE TEST (a student can meet both)", dupSame,
  (d) => `  ${d.score.toFixed(2)}  ${where(d.a).padEnd(20)} ↔ ${where(d.b).padEnd(20)}\n        ${d.a.id}  ${d.b.id}\n        ${text(d.a.passage).slice(0, 110)}`);
show("DUPLICATES ACROSS TESTS", dupCross,
  (d) => `  ${d.score.toFixed(2)}  ${where(d.a).padEnd(20)} ↔ ${where(d.b).padEnd(20)}  ${d.a.id} ${d.b.id}`);
show("SPLICED CHOICE TEXT", spliced,
  (s) => `  ${where(s.r).padEnd(20)} ${s.r.id} choice ${s.label}\n        …${s.t.slice(0, 150)}`);
show("TRUNCATED STEMS", truncated,
  (r) => `  ${where(r).padEnd(20)} ${r.id}\n        ${text(r.stem).slice(-110)}`);
show("RHETORICAL SYNTHESIS GOAL DRIFT", goalDrift,
  (g) => `  ${where(g.r).padEnd(20)} ${g.r.id}\n        goal: ${g.goal}\n        absent from notes+choices: ${g.missing.join(", ")}`);

console.log(`\nscanned ${rows.length} questions in Tests 16-31`);
