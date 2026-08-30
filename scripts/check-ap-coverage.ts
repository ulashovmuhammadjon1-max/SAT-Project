/**
 * Assert that the AP course outline students navigate and the question bank
 * behind it describe the same set of topics.
 *
 *   PROD_URL='postgresql://...' npx tsx scripts/check-ap-coverage.ts
 *
 * Two failures this catches, both of which reach a student directly:
 *
 *   - a topic listed in the outline with NO questions behind it, so the
 *     student taps through to an empty practice session;
 *   - questions sitting in the bank under a topic code the outline never
 *     shows, so content that was paid for is unreachable.
 *
 * It imports AP_COURSES rather than parsing courses.ts, so it cannot drift
 * from what the app actually renders.
 */
import { neon } from "@neondatabase/serverless";

import { AP_COURSES } from "../src/lib/ap/courses";
import { AP_CATALOG, isLiveSubject } from "../src/lib/ap/catalog";

const sql = neon(process.env.PROD_URL || process.env.DATABASE_URL || "");

type Row = { subject: string; topic: string; n: number };

async function main() {
  const rows = (await sql.query(
    `SELECT subject, topic, COUNT(*)::int AS n
       FROM "ApQuestion" GROUP BY subject, topic`,
  )) as Row[];

  const live = new Map<string, Map<string, number>>();
  for (const r of rows) {
    if (!live.has(r.subject)) live.set(r.subject, new Map());
    live.get(r.subject)!.set(r.topic, r.n);
  }

  let problems = 0;
  for (const course of AP_COURSES) {
    const banked = live.get(course.code) ?? new Map<string, number>();
    const outline = new Set<string>();
    for (const unit of course.units) {
      for (const t of unit.topics ?? []) outline.add(t.code);
    }

    const empty = [...outline].filter((c) => !banked.has(c));
    const orphan = [...banked.keys()].filter((c) => !outline.has(c));
    const thin = [...banked.entries()].filter(([c, n]) => outline.has(c) && n < 10);

    const total = [...banked.values()].reduce((a, b) => a + b, 0);
    const listed = AP_CATALOG.find((s) => s.code === course.code);
    const flag = listed && isLiveSubject(course.code) ? "LIVE" : "not live";
    console.log(
      `${course.code.padEnd(12)} ${String(outline.size).padStart(3)} topics in outline, ` +
        `${String(banked.size).padStart(3)} with questions, ${String(total).padStart(5)} questions  [${flag}]`,
    );

    // An outline topic with no questions only matters once the subject is
    // live -- before that, an empty topic is just work not yet done.
    if (empty.length && isLiveSubject(course.code)) {
      problems += empty.length;
      console.log(`   EMPTY (live subject, no questions): ${empty.join(", ")}`);
    } else if (empty.length) {
      console.log(`   not yet authored: ${empty.length} topics`);
    }
    if (orphan.length) {
      problems += orphan.length;
      console.log(`   ORPHAN (questions with no outline entry): ${orphan.join(", ")}`);
    }
    if (thin.length) {
      problems += thin.length;
      console.log(
        `   THIN (<10 questions): ${thin.map(([c, n]) => `${c}:${n}`).join(", ")}`,
      );
    }
  }

  // A subject the catalog calls live must actually have a course outline.
  for (const s of AP_CATALOG) {
    if (!isLiveSubject(s.code)) continue;
    if (!AP_COURSES.some((c) => c.code === s.code)) {
      problems++;
      console.log(`MISSING OUTLINE: catalog lists ${s.code} as live, courses.ts has none`);
    }
  }

  console.log(problems ? `\n${problems} problems` : "\nno problems");
  process.exit(problems ? 1 : 0);
}

main();
