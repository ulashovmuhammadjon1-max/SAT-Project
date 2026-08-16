/**
 * Apply a manual migration over Neon's HTTP API.
 *
 *   PROD_URL='postgresql://...' node scripts/apply-manual-migration.mjs \
 *     prisma/migrations/manual/010_ielts_academic.sql [--apply]
 *
 * The sandbox blocks raw Postgres (5432) and allows only outbound HTTPS, so
 * `prisma migrate deploy` cannot reach production from here. Statements are
 * split and sent one at a time, which is also why every DDL statement in a
 * manual migration must be independently re-runnable: there is no enclosing
 * transaction to roll back to. Use IF NOT EXISTS.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const file = process.argv[2];
const APPLY = process.argv.includes("--apply");
if (!file) {
  console.error("usage: apply-manual-migration.mjs <file.sql> [--apply]");
  process.exit(1);
}
const sql = neon(process.env.PROD_URL);

const text = readFileSync(file, "utf8");
// Strip comment-only lines so a statement is never just a comment.
const statements = text
  .split(/;\s*\n/)
  .map((s) => s.split("\n").filter((l) => !l.trim().startsWith("--")).join("\n").trim())
  .filter(Boolean);

console.log(`${file}: ${statements.length} statements`);
let ran = 0, skipped = 0;
for (const s of statements) {
  const label = s.replace(/\s+/g, " ").slice(0, 80);
  if (!APPLY) { console.log(`  would run: ${label}`); continue; }
  try {
    await sql.query(s.endsWith(";") ? s : s + ";");
    ran++;
  } catch (e) {
    // Re-running a migration must be a no-op, not a failure.
    if (/already exists|duplicate/i.test(e.message)) { skipped++; continue; }
    console.error(`FAILED: ${label}\n  ${e.message}`);
    process.exit(1);
  }
}
console.log(APPLY ? `APPLIED: ${ran} statements, ${skipped} already present` : "DRY RUN");
