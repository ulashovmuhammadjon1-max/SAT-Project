/**
 * Repair Math questions that are broken as content, not merely mis-keyed.
 *
 * Each entry asserts a distinctive substring of the CURRENT stem before it
 * writes, so a repair aimed at the wrong row fails loudly instead of silently
 * overwriting a correct question.
 *
 *   PROD_URL=… node repair_math.mjs           # report only
 *   PROD_URL=… node repair_math.mjs --apply
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");

/** The house table style, copied from CLAUDE.md so tables match every other test. */
const TBL = 'style="border-collapse:collapse;margin:0.75rem 0;"';
const TH = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;"';
const TD = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"';

const rows = [
  ["10:00 a.m.", 58],
  ["1:30 p.m.", 137],
  ["4:45 p.m.", 45],
  ["8:15 p.m.", 88],
];
const ticketTable =
  `<table ${TBL}><tr><th ${TH}>Screening</th><th ${TH}>Tickets sold</th></tr>` +
  rows.map(([s, n]) => `<tr><td ${TD}>${s}</td><td ${TD}>${n}</td></tr>`).join("") +
  `</table>`;

const REPAIRS = [
  {
    id: "060a8be5",
    where: "Test 7 Math M2 Easy q17 — unanswerable, no table",
    expectOld: "TABLE_B",
    // The stem shipped with the literal placeholder token and no table, so the
    // question could not be answered at all. Built to the existing key (92) and
    // to the existing distractors, so no choice had to change: greatest 137
    // minus least 45 is 92; 137 - 58 is the 79 in B; 88 - 45 is the 43 in A;
    // and D is the greatest value with no subtraction at all.
    stem:
      `${ticketTable}<p>The table shows the number of tickets sold for each of four film screenings. ` +
      `How many more tickets were sold for the screening with the greatest number of tickets sold ` +
      `than for the screening with the least?</p>`,
    explanation: {
      whyCorrect:
        "Find the two extremes in the Tickets sold column, not the first and last rows. The greatest is 137 at 1:30 p.m. and the least is 45 at 4:45 p.m., so the difference is 137 − 45 = 92.",
      whyWrong: {
        A: "43 is 88 − 45, the difference between the second-largest value and the smallest. The question asks for the greatest, and 88 is not it.",
        B: "79 is 137 − 58, using 58 as the smallest value. 58 is the second-smallest; 45 at 4:45 p.m. is lower.",
        D: "137 is the greatest number of tickets on its own. The question asks how many more that screening sold than the least, so it still has to be reduced by 45.",
      },
      commonMistakes:
        "Reading the first and last rows as the extremes. The screenings are listed in time order, not in order of tickets sold.",
      tips: "On a difference-from-a-table question, mark the largest and smallest values before doing any arithmetic.",
    },
  },
  {
    id: "7d672518",
    where: "Test 29 Math M1 q3 — scenario inconsistent with its own numbers",
    expectOld: "each with 30 tonnes of coal",
    // Keyed 60 hours, but at 0.6 t/h a 30-tonne stock is gone at hour 50, so
    // the gap physically tops out at 7.5 tonnes and 9 is never reached. Raising
    // the stock to 40 tonnes makes the faster kiln last 66.7 hours, so the
    // keyed answer is now reachable. The gap is still 0.15t, so every distractor
    // keeps its meaning and no choice changes.
    stem:
      "Two kilns are lit on the same morning, each with 40 tonnes of coal at its mouth. The first burns coal steadily at 0.6 tonnes an hour and the second steadily at 0.45 tonnes an hour. After how many hours of burning does the first kiln have 9 tonnes less coal left than the second?",
    explanation: {
      whyCorrect:
        "Both kilns start from the same 40 tonnes, so the difference between them comes only from the difference in burn rates. The first burns 0.6 − 0.45 = 0.15 tonnes an hour more than the second, and that gap accumulates: after \\(t\\) hours the first has 0.15t tonnes less. Set 0.15t = 9 and t = 60.",
      whyWrong: {
        A: "40 hours gives a gap of 0.15 × 40 = 6 tonnes, not 9. This is what you get by dividing 9 by the second kiln's rate of 0.45 and rounding.",
        B: "45 hours gives 0.15 × 45 = 6.75 tonnes. The 45 comes from the burn rate 0.45, which is not what the question asks for.",
        C: "50 hours gives 0.15 × 50 = 7.5 tonnes. Close, but the gap is still short of 9.",
      },
      commonMistakes:
        "Working out each kiln's remaining coal separately and subtracting at the end. Since both start equal, only the difference in rates matters, which turns a two-equation problem into one step.",
      tips: "When two quantities start from the same value and change at constant rates, the gap between them is just the rate difference times the time.",
    },
  },
];

/** Questions where one distractor is mathematically equal to the key. */
const CHOICE_SWAPS = [
  {
    id: "b4f10f7d",
    where: "Test 6 Math M1 q6 — two correct answers",
    label: "D",
    expectOld: "p - 35c = 6",
    // The data give p = 35c + 6, so the keyed "35c - p = -6" and the old D
    // "p - 35c = 6" are the same equation multiplied by -1: both are correct.
    // Replaced with the classic variable-swap error, which is wrong and is not
    // equivalent to B either.
    content: "\\(35p - c = 6\\)",
  },
  {
    id: "lismstoibyvyb3e0691gr40g",
    where: "Test 2 Math M1 q16 — two correct answers",
    label: "C",
    expectOld: "2\\times \\sqrt{12}",
    // 2*sqrt(12) = 2*2*sqrt(3) = 4*sqrt(3), which is the keyed A. Replaced with
    // 2*sqrt(24), the result of pulling a 2 out of the radical while dividing
    // the radicand by 2 instead of by 4.
    content: "\\(2\\times \\sqrt{24}\\)",
  },
];

let bad = 0;

for (const r of REPAIRS) {
  const [q] = await sql`SELECT id, stem FROM "Question" WHERE id LIKE ${r.id + "%"}`;
  if (!q) { console.error(`${r.where}: not found`); bad++; continue; }
  if (!q.stem.includes(r.expectOld)) {
    console.error(`${r.where}: stem does not contain "${r.expectOld}" — refusing`);
    bad++;
    continue;
  }
  console.log(`${r.where}\n  -> ${r.stem.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim().slice(0, 110)}…`);
  if (!APPLY) continue;

  await sql`UPDATE "Question" SET stem = ${r.stem}, "updatedAt" = NOW() WHERE id = ${q.id}`;

  const e = r.explanation;
  const bits = [`<p>${e.whyCorrect}</p>`, "<p><strong>Why the others are wrong</strong></p><ul>"];
  for (const [label, why] of Object.entries(e.whyWrong)) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
  bits.push("</ul>");
  await sql`
    INSERT INTO "Explanation" (id, "questionId", content, "whyCorrect", "whyWrongJson",
                               "commonMistakes", tips, source, "generatedAt")
    VALUES (gen_random_uuid()::text, ${q.id}, ${bits.join("")}, ${e.whyCorrect},
            ${JSON.stringify(e.whyWrong)}::jsonb, ${e.commonMistakes ?? null}, ${e.tips ?? null},
            'MANUAL', NOW())
    ON CONFLICT ("questionId") DO UPDATE
      SET content = EXCLUDED.content, "whyCorrect" = EXCLUDED."whyCorrect",
          "whyWrongJson" = EXCLUDED."whyWrongJson", "commonMistakes" = EXCLUDED."commonMistakes",
          tips = EXCLUDED.tips, source = 'MANUAL', "generatedAt" = NOW()`;
  console.log("  applied");
}

for (const s of CHOICE_SWAPS) {
  const [c] = await sql`
    SELECT c.id, c.content, c."isCorrect" FROM "AnswerChoice" c JOIN "Question" q ON q.id = c."questionId"
     WHERE q.id LIKE ${s.id + "%"} AND c.label = ${s.label}`;
  if (!c) { console.error(`${s.where}: choice ${s.label} not found`); bad++; continue; }
  if (!c.content.includes(s.expectOld)) {
    console.error(`${s.where}: choice ${s.label} does not contain "${s.expectOld}" — refusing`);
    console.error(`  it reads: ${c.content}`);
    bad++;
    continue;
  }
  if (c.isCorrect) { console.error(`${s.where}: choice ${s.label} is the key — refusing`); bad++; continue; }
  console.log(`${s.where}\n  ${s.label}: ${c.content}  ->  ${s.content}`);
  if (!APPLY) continue;
  await sql`UPDATE "AnswerChoice" SET content = ${s.content} WHERE id = ${c.id}`;
  console.log("  applied");
}

console.log(`\n${REPAIRS.length + CHOICE_SWAPS.length - bad} ready, ${bad} refused`);
if (!APPLY) console.log("Report only. Re-run with --apply.");
