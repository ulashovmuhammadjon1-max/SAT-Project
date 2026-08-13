/**
 * Correct answer keys that adjudication found wrong, then let the normal
 * pipeline ship the explanation.
 *
 * Every one of these questions already HAS an authored explanation sitting in
 * an agent's JSONL — it was withheld because `verify.mjs` refuses to publish an
 * explanation that argues against the stored key. Fixing the key here makes the
 * next `insert.mjs --apply` pass the gate and insert it. So this script only
 * ever touches `AnswerChoice.isCorrect`; it writes no explanation itself.
 *
 * Safety, per the rule in CLAUDE.md that a hardcoded position once overwrote an
 * already-correct question: each entry names a substring that must appear in
 * the choice it is about to promote, and the update is refused if it does not.
 * Ids are matched by prefix because production ids are UUIDs and the review
 * list carries only the first segment.
 *
 *   PROD_URL=… node fix_keys.mjs           # report only
 *   PROD_URL=… node fix_keys.mjs --apply
 */
import { neon } from "@neondatabase/serverless";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");

/** { id prefix, from → to letters, a substring that must be in the NEW choice, why } */
const FIXES = [
  {
    id: "i5cs4uao",
    where: "Test 1 R&W M1 q7 — Text Structure",
    from: "D",
    to: "A",
    expect: "counterexample",
    why: "The underlined portion is everything after the colon — the refutation itself. The tempting explanation it overturns sits BEFORE the underline, so the keyed D describes the wrong half of the sentence.",
  },
  {
    id: "roxqi9nr",
    where: "Test 1 Math M1 q8 — Lines, Angles, and Triangles",
    from: "A",
    to: "B",
    expect: "frac{-1}{6}",
    why: "Read off the figure, line n passes through (0, 3) and reaches y = 12 at x = 1.5, so its slope is 6 and the perpendicular slope is -1/6. The keyed -1/5 would require line n to have slope 5, which puts y = 12 at x = 1.8, right of where the drawn segment ends.",
  },
  {
    id: "w1q03tid",
    where: "Test 1 R&W M1 q16 — Boundaries",
    from: "D",
    to: "B",
    expect: "restaurants;",
    why: "Both sides of the blank are independent clauses, so the keyed comma is a splice. The semicolon is the only choice that supplies a full stop.",
  },
  {
    id: "js5541j6",
    where: "Test 1 R&W M2 Hard q7 — Text Structure",
    from: "C",
    to: "D",
    expect: "basic description",
    why: "The keyed C claims the sentence distinguishes this center from other tribal centers, but the very next sentence says the Comanche Nation 'employs a similar strategy'. The contrast in the passage is with non-Indigenous museums, not with other tribal centers.",
  },
  {
    id: "mf5z82cr",
    where: "Test 2 R&W M1 q22 — Transitions",
    from: "A",
    to: "C",
    expect: "Indeed",
    why: "The sentence after the blank restates the one before it — 'no matter the essay topic, Montaigne challenges his own ideas' and 'he questions his own perspective, regardless of subject matter' say the same thing. That is emphatic restatement, not exemplification, so the keyed 'For example' points at an example that never arrives.",
  },
  {
    id: "cj78heyd",
    where: "Test 2 R&W M2 Hard q3 — Words in Context",
    from: "B",
    to: "C",
    expect: "distinctive to",
    why: "The next sentence calls the conditions 'unique, rapidly evolving local conditions', which defines the blank as meaning particular to Iran. The keyed 'prohibitive in' does not fit the sentence at all — circumstances prohibitive in Iran would be a disadvantage, and the clause is introduced as an advantage.",
  },
  {
    id: "e09b3da7",
    where: "Test 10 R&W M2 Easy q14 — Inferences",
    from: "A",
    to: "D",
    expect: "easier for researchers to count",
    why: "The passage supports the ring inference directly — treeline rings can be thinner than a sheet of paper, and the lower trees grow far faster, so their rings are wider. Lifespan is never mentioned. The distractor design confirms it: B and C are the two reversals of the density sentence, leaving the ring sentence as the one the answer keys to.",
  },
  {
    id: "67845ef0",
    where: "Test 27 R&W M2 Hard q16 — Boundaries",
    from: "A",
    to: "D",
    expect: "place: deliberately, since",
    why: "A semicolon needs an independent clause on both sides, and 'deliberately, since they carry the digestive enzymes…' has no subject and no finite verb of its own. A colon takes a complete sentence before it — which 'Gutting a herring…leaving the pyloric caeca in place' is — and may be followed by a fragment that explains it, which is exactly what this is.",
  },
  {
    id: "522b9934",
    where: "Test 29 R&W M2 Easy q17 — Boundaries",
    from: "D",
    to: "B",
    expect: "heavy timber set",
    why: "The appositive renaming 'banker' is the whole phrase 'a low bench of stone or heavy timber set at about waist height' — 'set at about waist height' is a reduced relative telling you which kind of bench, so it belongs inside the appositive. The keyed D puts a comma between 'timber' and its own modifier, closing the appositive early and stranding the participle.",
  },
];

let bad = 0;
for (const f of FIXES) {
  const rows = await sql`
    SELECT c.id, c.label, c.content, c."isCorrect"
      FROM "AnswerChoice" c JOIN "Question" q ON q.id = c."questionId"
     WHERE q.id LIKE ${f.id + "%"} ORDER BY c."order"`;
  if (!rows.length) { console.error(`${f.id}: no choices found`); bad++; continue; }

  const oldC = rows.find((r) => r.label === f.from);
  const newC = rows.find((r) => r.label === f.to);
  if (!oldC || !newC) { console.error(`${f.id}: labels ${f.from}/${f.to} not both present`); bad++; continue; }
  if (!oldC.isCorrect) { console.error(`${f.id}: ${f.from} is not currently the key — already changed?`); bad++; continue; }
  if (!newC.content.includes(f.expect)) {
    console.error(`${f.id}: choice ${f.to} does not contain "${f.expect}" — refusing`);
    console.error(`         it reads: ${newC.content.slice(0, 90)}`);
    bad++;
    continue;
  }

  console.log(`${f.where}\n  ${f.from} -> ${f.to}   ${newC.content.replace(/<[^>]+>/g, "").slice(0, 70)}`);
  if (!APPLY) continue;

  await sql`UPDATE "AnswerChoice" SET "isCorrect" = false WHERE id = ${oldC.id}`;
  await sql`UPDATE "AnswerChoice" SET "isCorrect" = true  WHERE id = ${newC.id}`;

  // Read back rather than trust the write: exactly one key must survive.
  const after = await sql`
    SELECT label FROM "AnswerChoice" c JOIN "Question" q ON q.id = c."questionId"
     WHERE q.id LIKE ${f.id + "%"} AND c."isCorrect"`;
  if (after.length !== 1 || after[0].label !== f.to) {
    throw new Error(`${f.id}: after update the key is ${JSON.stringify(after)} — expected exactly ${f.to}`);
  }
  console.log(`  applied, verified`);
}

console.log(`\n${FIXES.length - bad} ready, ${bad} refused`);
if (!APPLY) console.log("Report only. Re-run with --apply.");
