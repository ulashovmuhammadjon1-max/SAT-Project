/**
 * Step 1 of 3: dump the live AP questions whose math needs typesetting.
 *
 *   PROD_URL='postgresql://...' node scripts/ap-latex-dump.mjs <out.json> [SUBJECT ...]
 *
 * The conversion runs against the LIVE rows rather than re-exporting the
 * modules, and that is deliberate. Re-exporting would re-run the choice
 * shuffle, and `ApQuestionAttempt` stores the index a student selected -- if
 * the choices move, every past attempt silently starts pointing at a different
 * answer, and review pages would show students picking things they never
 * picked. Converting the stored strings in place cannot do that: the array
 * order and `correctIndex` are never touched.
 */
import { neon } from "@neondatabase/serverless";
import { writeFileSync } from "fs";

const [out, ...subjects] = process.argv.slice(2);
if (!out) {
  console.error("usage: ap-latex-dump.mjs <out.json> [SUBJECT ...]");
  process.exit(1);
}
const wanted = subjects.length ? subjects : ["CALC_AB", "CALC_BC", "STATISTICS"];
const sql = neon(process.env.PROD_URL || process.env.DATABASE_URL);

const rows = await sql.query(
  `SELECT id, subject, topic, "order", stem, "choicesJson", "correctIndex",
          explanation, "tableJson"
     FROM "ApQuestion"
    WHERE subject = ANY($1)
    ORDER BY subject, topic, "order"`,
  [wanted],
);

writeFileSync(out, JSON.stringify(rows));
const bySubject = {};
for (const r of rows) bySubject[r.subject] = (bySubject[r.subject] || 0) + 1;
console.log(`dumped ${rows.length} questions ->`, bySubject);
