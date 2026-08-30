import { neon } from "@neondatabase/serverless";
const sql = neon(process.env.PROD_URL);
const REW = [
  ["incorrect: disjoint events with positive probability are dependent, because P(A given B) = 0 while P(A) > 0",
   "incorrect, because disjoint events with positive probability are dependent, since P(A given B) = 0 while P(A) > 0"],
  ["incorrect: for mutually exclusive events P(A and B) = 0, while the product rule applies to independent events",
   "incorrect, because P(A and B) = 0 for mutually exclusive events, while the product rule applies to independent events"],
  ["expected: an expected value is a long-run average and need not be a possible value of the random variable",
   "possible, because an expected value is a long-run average and need not be a possible value of the random variable"],
];
const apply = process.argv.includes("--apply");
for (const [oldText, newText] of REW) {
  const rows = await sql.query(
    `SELECT id, topic, "order", "choicesJson", "correctIndex" FROM "ApQuestion"
      WHERE subject = 'STATISTICS' AND "choicesJson" LIKE $1`,
    ["%" + oldText + "%"],
  );
  if (rows.length !== 1) {
    console.error(`expected exactly 1 row, found ${rows.length} for: ${oldText.slice(0, 45)}`);
    process.exit(1);
  }
  const r = rows[0];
  const ch = typeof r.choicesJson === "string" ? JSON.parse(r.choicesJson) : r.choicesJson;
  const at = ch.findIndex((c) => c === oldText);
  // The tell only matters because this string IS the key -- assert that before
  // touching anything, and rewrite in place so the position never moves.
  if (at !== r.correctIndex) {
    console.error(`${r.topic} #${r.order}: string is at ${at}, key is ${r.correctIndex}`);
    process.exit(1);
  }
  ch[at] = newText;
  console.log(`${apply ? "updating" : "would update"} STATISTICS ${r.topic} #${r.order} choice ${at}`);
  if (!apply) continue;
  const res = await sql.query(
    `UPDATE "ApQuestion" SET "choicesJson" = $2
      WHERE id = $1 AND "correctIndex" = $3 RETURNING id`,
    [r.id, JSON.stringify(ch), r.correctIndex],
  );
  if (res.length !== 1) { console.error("guard failed", r.id); process.exit(1); }
}
console.log(apply ? "done" : "dry run only");
