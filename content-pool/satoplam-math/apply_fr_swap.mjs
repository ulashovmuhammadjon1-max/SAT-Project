/**
 * Swap one grid-in for a multiple-choice question in the four Module 2 Easy
 * modules whose HARD tier is entirely free-response.
 *
 *   PROD_URL='postgresql://...' node apply_fr_swap.mjs [--apply]
 *
 * Those tiers hold exactly three questions and all three are grid-ins, so no
 * ordering of them avoids three in a row — the fix has to change content, not
 * position. The replacement comes from the Question Bank spares and was
 * screened for co-visibility against the whole test by plan_fr_swap.py.
 *
 * The displaced question is retired, never deleted, and the incoming one moves
 * out of the bank and into the module.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");
const plan = JSON.parse(readFileSync(path.join(HERE, "fr_swap.json"), "utf8"));

for (const p of plan) {
  const dropSource = (p.drop.startsWith("sathard") ? "SATHARD:" : "SATMATH:") + p.drop;

  const [out] = await sql.query(
    `SELECT q.id, q."moduleId", q."order", q.type, q.difficulty
       FROM "Question" q
       JOIN "Module" m ON m.id = q."moduleId" AND m.subject = 'MATH'
                      AND m."order" = 2 AND m.difficulty = 'EASY'
       JOIN "Test" t ON t.id = m."testId"
      WHERE t.title = $1 AND q.source = $2 AND q."isPublished"`,
    [p.test, dropSource]);
  const [inc] = await sql.query(
    `SELECT id, type, difficulty FROM "Question"
      WHERE source = $1 AND "moduleId" IS NULL AND "isPublished"`, [p.addSource]);

  // Assert the shape before writing: the row being removed must really be the
  // hard grid-in this plan was built from, and the replacement must really be
  // a hard multiple-choice sitting in the bank.
  if (!out) throw new Error(`${p.test}: ${dropSource} not found in Module 2 Easy`);
  if (!inc) throw new Error(`${p.test}: ${p.addSource} not found in the bank`);
  if (out.type !== "FREE_RESPONSE" || out.difficulty !== "HARD")
    throw new Error(`${p.test}: ${dropSource} is ${out.type}/${out.difficulty}`);
  if (inc.type !== "MULTIPLE_CHOICE" || inc.difficulty !== "HARD")
    throw new Error(`${p.test}: ${p.addSource} is ${inc.type}/${inc.difficulty}`);

  console.log(`${p.test}: order ${out.order}  ${p.drop} (FR) -> ${p.add} (MC)`);
  if (!APPLY) continue;

  await sql.query(
    `UPDATE "Question" SET "moduleId" = NULL, "isPublished" = false, "updatedAt" = now()
      WHERE id = $1`, [out.id]);
  await sql.query(
    `UPDATE "Question" SET "moduleId" = $1, "order" = $2, "updatedAt" = now()
      WHERE id = $3`, [out.moduleId, out.order, inc.id]);
}

console.log(`${APPLY ? "APPLIED" : "DRY RUN"}: ${plan.length} swaps`);
