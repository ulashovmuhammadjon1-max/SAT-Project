/**
 * Repair questions that adjudication found defective rather than merely
 * mis-keyed.
 *
 * A wrong key is fixed by `fix_keys.mjs`. This file is for the other outcome:
 * an item where two of the four choices are both correct Standard English, so
 * no key is right and moving the key would still leave a student who picked the
 * other one marked wrong for no reason. Those need the passage or the choices
 * changed so exactly one option works.
 *
 * Each entry replaces the passage text and the full choice set in one
 * transaction-ish sequence, and asserts a distinctive substring of the CURRENT
 * passage first — the rule from CLAUDE.md, after a hardcoded position once
 * overwrote an already-correct question.
 *
 *   PROD_URL=… node rewrite_questions.mjs           # report only
 *   PROD_URL=… node rewrite_questions.mjs --apply
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");

const REWRITES = [
  {
    id: "0531453e",
    where: "Test 24 R&W M2 Easy q17 — Boundaries",
    // "…cords, laces the cord ends into the ___ and covers the whole in leather."
    // is a three-item series, so both "boards" and "boards," are correct: the
    // serial comma is optional and the SAT does not test it. Recast as two
    // independent clauses, which has exactly one right mark.
    expectOld: "sews each gathering round three cords, laces the cord ends",
    passage:
      "The binder sews each gathering round three cords and laces the cord ends into the _____ the whole is then covered in leather.",
    choices: [
      { label: "A", content: "boards", isCorrect: false },
      { label: "B", content: "boards,", isCorrect: false },
      { label: "C", content: "boards;", isCorrect: true },
      { label: "D", content: "boards:", isCorrect: false },
    ],
    explanation: {
      whyCorrect:
        "Everything before the blank is a complete sentence — the binder sews the gatherings and laces the cord ends into the boards. Everything after it is another complete sentence, with its own subject <em>the whole</em> and its own verb <em>is covered</em>. Two complete sentences need a full stop between them, and the semicolon is the only choice here that supplies one.",
      whyWrong: {
        A: "With no punctuation at all the two sentences run straight together, which is the error this question is built around.",
        B: "A comma is too weak to join two complete sentences. This is a comma splice — the single most common way to get a Boundaries question wrong.",
        D: "A colon does follow a complete sentence, but what comes after it has to explain or specify what came before. Covering the book in leather is the next step in the process, not an explanation of lacing the cords, so the colon has nothing to introduce.",
      },
      commonMistakes:
        "Choosing the comma because the two halves describe one continuous process. How closely the ideas are related does not change what punctuation two complete sentences require.",
      tips: "Test each side of the blank on its own. If both stand up as sentences, a comma alone is never the answer.",
    },
  },
  {
    id: "d4651a93",
    where: "Test 27 R&W M2 Easy q17 — Boundaries",
    // The original put two independent clauses either side of the blank, which
    // makes BOTH "membrane. It" and "membrane, and it" correct. Recast around
    // an appositive, where exactly one mark works — and which also removes the
    // original's awkward "It stiffens it", two pronouns with different referents.
    expectOld: "bacterioruberin, a carotenoid that sits in the archaeal cell",
    passage:
      "The red that colours a saturating pond comes from _____ a carotenoid that sits in the archaeal cell membrane and stiffens it against the osmotic stress of the surrounding brine and, incidentally, screens the cell from ultraviolet light.",
    choices: [
      { label: "A", content: "bacterioruberin,", isCorrect: true },
      { label: "B", content: "bacterioruberin", isCorrect: false },
      { label: "C", content: "bacterioruberin;", isCorrect: false },
      { label: "D", content: "bacterioruberin, and", isCorrect: false },
    ],
    explanation: {
      whyCorrect:
        "What follows the blank — <em>a carotenoid that sits in the archaeal cell membrane…</em> — renames the pigment just mentioned. That is an appositive, and a non-restrictive appositive is separated from the noun it renames by a comma.",
      whyWrong: {
        B: "With no punctuation the appositive runs into the noun, so the sentence reads as though the red comes from some thing called a <em>bacterioruberin a carotenoid</em>. An appositive has to be marked off.",
        C: "A semicolon needs a complete sentence on both sides. <em>A carotenoid that sits in the archaeal cell membrane and stiffens it…</em> has no main verb of its own — it is a noun phrase, not a sentence.",
        D: "Adding <em>and</em> turns one thing into two, as if the red came from bacterioruberin plus some separate carotenoid. There is only one pigment here, and the phrase after the blank is another name for it.",
      },
      commonMistakes:
        "Reading the long phrase after the blank as a clause because it contains verbs. <em>Sits</em> and <em>stiffens</em> both belong to <em>that</em>, inside the relative clause — the phrase as a whole is still a noun.",
      tips: "If the words after the blank rename the noun before it, you are looking at an appositive, and the question is only about how to fence it off.",
    },
  },
  {
    id: "99a4e8fc",
    where: "Test 23 R&W M1 q17 — answer shown earlier in the same module",
    // q6's passage, eleven questions earlier in this same module, prints
    // "Weed cutting takes off what has grown in the water this season; dredging
    // takes out what has settled on the bed over many" — the exact sentence
    // this item asks the student to punctuate, semicolon included. Moved onto a
    // different pair of clauses in the same setting. The colon stays wrong for
    // the same reason as before: the second clause is the next step in the
    // process, not an explanation of the first.
    expectOld: "Weed cutting removes what has grown in the water this",
    passage:
      "The two operations are not the same and are not costed the same way. A gauging station records what a boat is _____ toll clerk works out what that cargo owes.",
    choices: [
      { label: "A", content: "carrying the", isCorrect: false },
      { label: "B", content: "carrying: the", isCorrect: false },
      { label: "C", content: "carrying; the", isCorrect: true },
      { label: "D", content: "carrying, the", isCorrect: false },
    ],
    explanation: {
      whyCorrect:
        "Both sides of the blank stand alone as sentences: <em>a gauging station records what a boat is carrying</em> has its own subject and verb, and so does <em>the toll clerk works out what that cargo owes</em>. Two complete sentences that belong together in one sentence need a semicolon.",
      whyWrong: {
        A: "With nothing between them the two sentences run together, which is the error the question is testing.",
        B: "A colon does follow a complete sentence, but what comes after it has to explain or spell out what came before. Working out the toll is the next step after gauging the boat, not an explanation of it.",
        D: "A comma cannot join two complete sentences on its own. This is a comma splice.",
      },
      commonMistakes:
        "Choosing the comma because the two actions happen in sequence and feel like one thought. Closeness of meaning never licenses a comma between two complete sentences.",
      tips: "Cover the blank and read each side as its own sentence. If both work, the comma is out and you are choosing between the semicolon and the colon — and the colon needs the second half to explain the first.",
    },
  },
];

let bad = 0;
for (const r of REWRITES) {
  const [q] = await sql`
    SELECT q.id, q."passageId", p.content AS passage
      FROM "Question" q JOIN "Passage" p ON p.id = q."passageId"
     WHERE q.id LIKE ${r.id + "%"}`;
  if (!q) { console.error(`${r.where}: not found`); bad++; continue; }
  if (!q.passage.includes(r.expectOld)) {
    console.error(`${r.where}: current passage does not contain "${r.expectOld}" — refusing`);
    console.error(`  it reads: ${q.passage.slice(0, 120)}`);
    bad++;
    continue;
  }
  if (r.choices.filter((c) => c.isCorrect).length !== 1) { console.error(`${r.where}: not exactly one key`); bad++; continue; }

  console.log(`${r.where}\n  -> ${r.passage.slice(0, 100)}…\n  key ${r.choices.find((c) => c.isCorrect).label}`);
  if (!APPLY) continue;

  await sql`UPDATE "Passage" SET content = ${r.passage} WHERE id = ${q.passageId}`;
  await sql`DELETE FROM "AnswerChoice" WHERE "questionId" = ${q.id}`;
  for (const [i, c] of r.choices.entries()) {
    await sql`
      INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
      VALUES (gen_random_uuid()::text, ${q.id}, ${c.label}, ${c.content}, ${c.isCorrect}, ${i})`;
  }

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
          tips = EXCLUDED.tips, "generatedAt" = NOW()`;

  const after = await sql`SELECT label FROM "AnswerChoice" WHERE "questionId" = ${q.id} AND "isCorrect"`;
  if (after.length !== 1) throw new Error(`${r.id}: ${after.length} keys after rewrite`);
  console.log(`  applied, verified`);
}

console.log(`\n${REWRITES.length - bad} ready, ${bad} refused`);
if (!APPLY) console.log("Report only. Re-run with --apply.");
