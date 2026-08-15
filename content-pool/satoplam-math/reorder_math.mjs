/**
 * Order every Math module so a student meets EASY, then MEDIUM, then HARD, and
 * never three free-response questions in a row.
 *
 *   PROD_URL='postgresql://...' node reorder_math.mjs [--apply]
 *
 * Only `Question.order` changes. Past `Response` rows key on questionId, not
 * order, so attempt history and review pages are unaffected; what changes is
 * the position a future student sees in the palette.
 *
 * Free-response placement: rather than sorting and then patching up runs, the
 * grid-ins are dealt out at even intervals through each difficulty tier. That
 * makes a run of three impossible by construction whenever the tier has at
 * least two multiple-choice questions per grid-in, instead of relying on a
 * repair loop that has to be checked afterwards. The boundary between two
 * tiers is checked as well, since a tier ending in two grid-ins followed by a
 * tier opening on one is still three in a row.
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");
const TIERS = ["EASY", "MEDIUM", "HARD"];

/** Deal the free-response questions evenly through a tier's multiple choice. */
function spread(items) {
  const mc = items.filter((q) => q.type !== "FREE_RESPONSE");
  const fr = items.filter((q) => q.type === "FREE_RESPONSE");
  if (!fr.length) return mc;
  if (!mc.length) return fr;
  const out = [];
  // Target gap between grid-ins, in slots.
  const step = (mc.length + fr.length) / fr.length;
  let next = step - 1, fi = 0;
  for (let i = 0; i < mc.length; i++) {
    out.push(mc[i]);
    while (fi < fr.length && out.length >= Math.round(next)) {
      out.push(fr[fi++]);
      next += step;
    }
  }
  while (fi < fr.length) out.push(fr[fi++]);
  return out;
}

function longestRun(list) {
  let best = 0, run = 0;
  for (const q of list) {
    run = q.type === "FREE_RESPONSE" ? run + 1 : 0;
    if (run > best) best = run;
  }
  return best;
}

const mods = await sql.query(`
  SELECT m.id, m."order" AS mo, m.difficulty AS branch, t.title
    FROM "Module" m JOIN "Test" t ON t.id = m."testId"
   WHERE m.subject = 'MATH'
   ORDER BY t.title, m."order", m.difficulty`);

let changed = 0, moved = 0, worstRun = 0;
const report = [];

for (const mod of mods) {
  const qs = await sql.query(
    `SELECT id, "order", difficulty, type FROM "Question"
      WHERE "moduleId" = $1 AND "isPublished" ORDER BY "order"`, [mod.id]);
  if (!qs.length) continue;

  const before = qs.map((q) => q.id).join(",");
  const ordered = [];
  for (const tier of TIERS) {
    ordered.push(...spread(qs.filter((q) => q.difficulty === tier)));
  }
  // Anything with an unexpected difficulty keeps its place at the end rather
  // than being dropped — losing a question here would silently shrink a module.
  for (const q of qs) if (!ordered.includes(q)) ordered.push(q);

  const run = longestRun(ordered);
  if (run > worstRun) worstRun = run;
  const after = ordered.map((q) => q.id).join(",");
  const diff = ordered.filter((q, i) => q.id !== qs[i].id).length;
  if (before !== after) { changed++; moved += diff; }
  report.push({
    test: mod.title, mod: `${mod.mo}${mod.branch[0]}`, n: qs.length,
    tiers: TIERS.map((t) => qs.filter((q) => q.difficulty === t).length).join("/"),
    fr: qs.filter((q) => q.type === "FREE_RESPONSE").length,
    maxFRrun: run, moved: diff,
  });

  if (!APPLY || before === after) continue;
  // Two passes: park the module in a disjoint range first, because
  // (moduleId, order) collisions during a straight renumber would otherwise
  // put two questions on the same slot mid-update.
  for (let i = 0; i < ordered.length; i++) {
    await sql.query(`UPDATE "Question" SET "order" = $1 WHERE id = $2`,
      [1000 + i, ordered[i].id]);
  }
  for (let i = 0; i < ordered.length; i++) {
    await sql.query(`UPDATE "Question" SET "order" = $1, "updatedAt" = now() WHERE id = $2`,
      [i + 1, ordered[i].id]);
  }
}

console.table(report.filter((r) => r.moved).slice(0, 20));
console.log(`${APPLY ? "APPLIED" : "DRY RUN"}: ${changed} of ${mods.length} Math modules reordered, `
  + `${moved} question positions changed`);
console.log(`longest free-response run after ordering: ${worstRun}`);
