/**
 * Break up Math questions that are the same template as another live question.
 *
 * These pairs sit in different tests, so no single student meets both — but the
 * project's dedupe rule is explicit that a repeated problem template with only
 * the numbers changed counts as a duplicate, and a student working through the
 * bank will meet both. Each entry re-authors the SECOND of the pair with new
 * constants, replaces its choices, and rewrites its explanation to match.
 *
 * Every entry asserts a distinctive substring of the current stem before
 * writing, and every new answer is verified independently in the accompanying
 * sympy check (see the commit message for the run).
 *
 *   PROD_URL=… node dedupe_math_templates.mjs           # report only
 *   PROD_URL=… node dedupe_math_templates.mjs --apply
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");

const ITEMS = [
  {
    id: "436c759d",
    where: "Test 27 Math M2 Hard q4 — same line as Test 26 M2 Hard q2",
    expectOld: "(a,3a)",
    // Test 26 M2H q2 uses the identical points (a,3a) and (3a,11a), slope 4,
    // y = 4x - a. New points give slope 3 and intercept +4a, so neither the
    // slope nor the sign of the intercept carries over.
    stem:
      "On a plan of a cheese cave a straight line passes through the points \\((a,7a)\\) and \\((4a,16a)\\), where a is a positive constant. The line crosses the vertical axis at the point \\((0,b)\\). What is the value of b in terms of a?",
    choices: [
      { label: "A", content: "\\(4a\\)", isCorrect: true },
      { label: "B", content: "\\(-4a\\)", isCorrect: false },
      { label: "C", content: "\\(3a\\)", isCorrect: false },
      { label: "D", content: "\\(7a\\)", isCorrect: false },
    ],
    explanation: {
      whyCorrect:
        "Slope first: \\(\\frac{16a-7a}{4a-a}=\\frac{9a}{3a}=3\\). Then put one point into \\(y=3x+b\\) — using \\((a,7a)\\) gives \\(7a=3a+b\\), so \\(b=4a\\). The a's cancel in the slope, which is what makes the answer a clean multiple of a.",
      whyWrong: {
        B: "\\(-4a\\) is the right size with the wrong sign, from rearranging \\(7a=3a+b\\) as \\(b=3a-7a\\) instead of \\(b=7a-3a\\).",
        C: "\\(3a\\) is the slope, not the intercept. The slope is the 3 in \\(y=3x+b\\); b is what is left after the slope term is subtracted.",
        D: "\\(7a\\) is the y-coordinate of the first point. That is the height of the line at \\(x=a\\), not at \\(x=0\\).",
      },
      commonMistakes:
        "Treating \\((a,7a)\\) as though it were on the vertical axis. It sits at \\(x=a\\), so the line still has to be walked back to \\(x=0\\).",
      tips: "When every coordinate carries the same unknown constant, work the slope first — the constant cancels and leaves an ordinary number.",
    },
  },
  {
    id: "1aba74ae",
    where: "Test 31 Math M2 Easy q3 — same equation as Test 29 M2 Easy q6",
    expectOld: "7n - 12 = 4n + 27",
    // Test 29 M2E q6 is 7x - 12 = 4x + 27, the identical equation answering 13.
    stem:
      "A loft keeper counting his birds writes 9n - 15 = 5n + 21, where n is the number of pigeons in the loft. What is the value of n?",
    correctAnswerFR: '["9"]',
    explanation: {
      whyCorrect:
        "Collect the n terms on one side and the numbers on the other. Subtracting 5n from both sides leaves 4n - 15 = 21, and adding 15 to both sides gives 4n = 36, so n = 9. Checking: 9(9) - 15 = 66 and 5(9) + 21 = 66.",
      whyWrong: {},
      commonMistakes:
        "Subtracting 15 from the right-hand side instead of adding it. The -15 moves across the equals sign as +15.",
      tips: "Always substitute your answer back into the original equation. Both sides landing on 66 is the check that costs five seconds and catches a sign slip.",
    },
  },
  {
    id: "59425706",
    where: "Test 23 Math M2 Hard q19 — same 5-12-13 ratio as Test 22 M2 Hard q21",
    expectOld: "\\sin A=\\frac{5}{13}",
    // Test 22 M2H q21 gives sin = 5/13 and asks for a tangent from the same
    // 5-12-13 triangle. Moved to the 8-15-17 triple.
    stem:
      "In right triangle ABC the right angle is at B, and \\(\\sin A=\\frac{8}{17}\\). What is the value of \\(\\tan C\\)?",
    choices: [
      { label: "A", content: "\\(\\frac{8}{17}\\)", isCorrect: false },
      { label: "B", content: "\\(\\frac{8}{15}\\)", isCorrect: false },
      { label: "C", content: "\\(\\frac{17}{8}\\)", isCorrect: false },
      { label: "D", content: "\\(\\frac{15}{8}\\)", isCorrect: true },
    ],
    explanation: {
      whyCorrect:
        "With the right angle at B, the hypotenuse is \\(AC\\). \\(\\sin A=\\frac{BC}{AC}=\\frac{8}{17}\\), so take \\(BC=8k\\) and \\(AC=17k\\); the Pythagorean theorem gives \\(AB=15k\\). Now switch to angle C: its opposite side is \\(AB\\) and its adjacent side is \\(BC\\), so \\(\\tan C=\\frac{15k}{8k}=\\frac{15}{8}\\).",
      whyWrong: {
        A: "\\(\\frac{8}{17}\\) is the sine you were given. A tangent is opposite over adjacent, never opposite over hypotenuse.",
        B: "\\(\\frac{8}{15}\\) is \\(\\tan A\\), not \\(\\tan C\\). A and C are the two acute angles, and their tangents are reciprocals of each other.",
        C: "\\(\\frac{17}{8}\\) uses the hypotenuse as one of the two sides. The hypotenuse never appears in a tangent.",
      },
      commonMistakes:
        "Finding the third side correctly and then reading the ratio from the wrong angle. Which side is opposite and which adjacent swaps completely when you move from A to C.",
      tips: "Label all three sides with the multiplier k before touching the second angle. Once the triangle is 8k, 15k, 17k, any ratio is just picking two of them.",
    },
  },
];

let bad = 0;
for (const it of ITEMS) {
  const [q] = await sql`SELECT id, stem, type::text AS type FROM "Question" WHERE id LIKE ${it.id + "%"}`;
  if (!q) { console.error(`${it.where}: not found`); bad++; continue; }
  if (!q.stem.includes(it.expectOld)) {
    console.error(`${it.where}: stem does not contain "${it.expectOld}" — refusing`);
    console.error(`  it reads: ${q.stem.slice(0, 120)}`);
    bad++;
    continue;
  }
  console.log(`${it.where}\n  -> ${it.stem.slice(0, 105)}…`);
  if (!APPLY) continue;

  await sql`UPDATE "Question" SET stem = ${it.stem}, "updatedAt" = NOW() WHERE id = ${q.id}`;

  if (it.correctAnswerFR) {
    // Must stay a JSON-encoded array string; a bare value crashes grading.
    JSON.parse(it.correctAnswerFR);
    await sql`UPDATE "Question" SET "correctAnswerFR" = ${it.correctAnswerFR} WHERE id = ${q.id}`;
  }
  if (it.choices) {
    await sql`DELETE FROM "AnswerChoice" WHERE "questionId" = ${q.id}`;
    for (const [i, c] of it.choices.entries()) {
      await sql`
        INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
        VALUES (gen_random_uuid()::text, ${q.id}, ${c.label}, ${c.content}, ${c.isCorrect}, ${i})`;
    }
    const after = await sql`SELECT label FROM "AnswerChoice" WHERE "questionId" = ${q.id} AND "isCorrect"`;
    if (after.length !== 1) throw new Error(`${it.id}: ${after.length} keys after rewrite`);
  }

  const e = it.explanation;
  const bits = [`<p>${e.whyCorrect}</p>`];
  if (Object.keys(e.whyWrong).length) {
    bits.push("<p><strong>Why the others are wrong</strong></p><ul>");
    for (const [label, why] of Object.entries(e.whyWrong)) bits.push(`<li><strong>${label}.</strong> ${why}</li>`);
    bits.push("</ul>");
  }
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
  console.log("  applied, verified");
}

console.log(`\n${ITEMS.length - bad} ready, ${bad} refused`);
if (!APPLY) console.log("Report only. Re-run with --apply.");
