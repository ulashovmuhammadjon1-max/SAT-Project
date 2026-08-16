/**
 * Seed original Writing tasks and Speaking prompt sets.
 *
 *   PROD_URL='postgresql://...' node seed_prompts.mjs [--apply]
 *
 * Written for SATForge rather than taken from a book: these are the two skills
 * the product actually delivers, so the prompts have to be ones we can publish.
 * They follow the documented IELTS Academic task forms — Task 1 describes
 * visual information, Task 2 argues a position, Speaking runs personal to
 * abstract across three parts — without reproducing anyone's questions.
 *
 * Idempotent on slug: re-running replaces the tasks in place.
 */
import { neon } from "@neondatabase/serverless";
import { randomUUID } from "crypto";

const sql = neon(process.env.PROD_URL);
const APPLY = process.argv.includes("--apply");

const TABLE =
  '<table style="border-collapse:collapse;margin:0.75rem 0;">' +
  '<thead><tr>' +
  ['Year', 'Cycling', 'Bus', 'Car', 'Walking'].map((h) =>
    `<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">${h}</th>`).join("") +
  '</tr></thead><tbody>' +
  [["2005", "8%", "24%", "52%", "16%"],
   ["2012", "13%", "27%", "43%", "17%"],
   ["2019", "21%", "29%", "31%", "19%"]]
    .map((r) => "<tr>" + r.map((c) =>
      `<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">${c}</td>`).join("") + "</tr>").join("") +
  "</tbody></table>";

/** Writing papers: each is one test carrying Task 1 and Task 2. */
const WRITING = [
  {
    slug: "writing-practice-1",
    title: "IELTS Writing Practice 1",
    tasks: [
      {
        partNumber: 1, title: "Task 1",
        minWords: 150,
        promptHtml:
          "<p>The table below shows how commuters in one European city travelled to work " +
          "in 2005, 2012 and 2019.</p>" + TABLE +
          "<p>Summarise the information by selecting and reporting the main features, " +
          "and make comparisons where relevant.</p>",
      },
      {
        partNumber: 2, title: "Task 2",
        minWords: 250,
        promptHtml:
          "<p>Some people believe that universities should prioritise subjects that lead " +
          "directly to employment. Others argue that universities should give equal weight " +
          "to subjects with no obvious career path, such as philosophy or history.</p>" +
          "<p>Discuss both views and give your own opinion.</p>",
      },
    ],
  },
  {
    slug: "writing-practice-2",
    title: "IELTS Writing Practice 2",
    tasks: [
      {
        partNumber: 1, title: "Task 1",
        minWords: 150,
        promptHtml:
          "<p>The diagram below shows the stages in recycling glass bottles, from " +
          "collection through to the production of new containers.</p>" +
          "<p><em>Stages: household collection &rarr; sorting by colour &rarr; washing and " +
          "contaminant removal &rarr; crushing into cullet &rarr; melting at 1,500&deg;C with " +
          "sand and limestone &rarr; moulding into new bottles &rarr; distribution.</em></p>" +
          "<p>Summarise the information by selecting and reporting the main features.</p>",
      },
      {
        partNumber: 2, title: "Task 2",
        minWords: 250,
        promptHtml:
          "<p>In many countries, people are working longer hours than they did a generation " +
          "ago, while spending less time with family and friends.</p>" +
          "<p>What are the causes of this development? What measures could reduce its " +
          "effects?</p>",
      },
    ],
  },
];

/**
 * Speaking papers. Part 1 is personal and familiar, Part 2 a long turn from a
 * cue card, Part 3 abstract discussion tied to the Part 2 topic — the widening
 * of scope across the three parts is the shape of the real interview.
 */
const SPEAKING = [
  {
    slug: "speaking-practice-1",
    title: "IELTS Speaking Practice 1",
    parts: [
      {
        partNumber: 1, title: "Part 1 — Introduction and Interview",
        speakSeconds: 45,
        promptHtml: JSON.stringify([
          "Where are you living at the moment?",
          "What do you like most about the area you live in?",
          "Do you prefer being indoors or outdoors? Why?",
          "How often do you travel by public transport?",
          "Has the way you travel around changed in recent years?",
        ]),
      },
      {
        partNumber: 2, title: "Part 2 — Individual Long Turn",
        prepSeconds: 60, speakSeconds: 120,
        promptHtml:
          "<p><strong>Describe a place you go to when you want to concentrate.</strong></p>" +
          "<p>You should say:</p><ul>" +
          "<li>where it is</li>" +
          "<li>how often you go there</li>" +
          "<li>what you usually do there</li></ul>" +
          "<p>and explain why this place helps you concentrate.</p>",
      },
      {
        partNumber: 3, title: "Part 3 — Discussion",
        speakSeconds: 60,
        promptHtml: JSON.stringify([
          "Why do you think some people find it harder to concentrate than others?",
          "Have public spaces in cities become noisier over time?",
          "Should employers be responsible for providing quiet working conditions?",
          "How might the ability to concentrate change as technology develops?",
        ]),
      },
    ],
  },
  {
    slug: "speaking-practice-2",
    title: "IELTS Speaking Practice 2",
    parts: [
      {
        partNumber: 1, title: "Part 1 — Introduction and Interview",
        speakSeconds: 45,
        promptHtml: JSON.stringify([
          "Do you work or are you a student?",
          "What do you enjoy most about what you do?",
          "How do you usually spend your weekends?",
          "Do you think you have enough free time?",
          "What kind of weather do you prefer?",
        ]),
      },
      {
        partNumber: 2, title: "Part 2 — Individual Long Turn",
        prepSeconds: 60, speakSeconds: 120,
        promptHtml:
          "<p><strong>Describe something you learned that turned out to be more useful " +
          "than you expected.</strong></p>" +
          "<p>You should say:</p><ul>" +
          "<li>what it was</li>" +
          "<li>when and how you learned it</li>" +
          "<li>why you did not expect it to be useful</li></ul>" +
          "<p>and explain how it has been useful to you since.</p>",
      },
      {
        partNumber: 3, title: "Part 3 — Discussion",
        speakSeconds: 60,
        promptHtml: JSON.stringify([
          "Should schools teach more practical skills alongside academic subjects?",
          "Is it possible to know in advance which skills will be valuable?",
          "How has the way people learn new skills changed in the last twenty years?",
          "Do you think formal qualifications will matter as much in the future?",
        ]),
      },
    ],
  },
];

async function seedPaper(paper, skill, minutes) {
  const found = await sql.query(`SELECT id FROM "IeltsTest" WHERE slug = $1`, [paper.slug]);
  let testId;
  if (found.length) {
    testId = found[0].id;
    await sql.query(`DELETE FROM "IeltsSection" WHERE "testId" = $1`, [testId]);
    await sql.query(
      `UPDATE "IeltsTest" SET title=$2, status='PUBLISHED', "updatedAt"=now() WHERE id=$1`,
      [testId, paper.title]);
  } else {
    testId = randomUUID();
    await sql.query(
      `INSERT INTO "IeltsTest" (id,title,slug,module,status,description,difficulty,"createdAt","updatedAt")
       VALUES ($1,$2,$3,'ACADEMIC','PUBLISHED',$4,3,now(),now())`,
      [testId, paper.title, paper.slug,
       skill === "WRITING"
         ? "Two tasks, sixty minutes. Submitted for free human review."
         : "Three parts, recorded and submitted for free human review."]);
  }
  const sectionId = randomUUID();
  await sql.query(
    `INSERT INTO "IeltsSection" (id,"testId",skill,"order","durationMinutes",instructions)
     VALUES ($1,$2,$3::"IeltsSkill",1,$4,$5)`,
    [sectionId, testId, skill, minutes,
     skill === "WRITING"
       ? "Spend about 20 minutes on Task 1 and about 40 minutes on Task 2."
       : "You will record your answers. Speak naturally and at a normal pace."]);

  for (const p of paper.parts ?? paper.tasks) {
    await sql.query(
      `INSERT INTO "IeltsPart" (id,"sectionId","partNumber",title,"promptHtml",
                                "minWords","prepSeconds","speakSeconds")
       VALUES ($1,$2,$3,$4,$5,$6,$7,$8)`,
      [randomUUID(), sectionId, p.partNumber, p.title, p.promptHtml,
       p.minWords ?? null, p.prepSeconds ?? null, p.speakSeconds ?? null]);
  }
  return testId;
}

if (!APPLY) {
  console.log(`DRY RUN: ${WRITING.length} writing papers, ${SPEAKING.length} speaking papers`);
  process.exit(0);
}
for (const w of WRITING) console.log("writing  ", w.slug, await seedPaper(w, "WRITING", 60));
for (const s of SPEAKING) console.log("speaking ", s.slug, await seedPaper(s, "SPEAKING", 14));

const check = await sql.query(
  `SELECT t.title, t.status, s.skill, COUNT(p.id)::int AS parts
     FROM "IeltsTest" t
     JOIN "IeltsSection" s ON s."testId" = t.id
     LEFT JOIN "IeltsPart" p ON p."sectionId" = s.id
    WHERE s.skill IN ('WRITING','SPEAKING')
    GROUP BY t.title, t.status, s.skill ORDER BY s.skill, t.title`);
console.table(check);
