import { neon } from '@neondatabase/serverless';
import { readFileSync } from 'fs';
import { randomUUID } from 'crypto';

const sql = neon(process.env.DATABASE_URL);
const full = JSON.parse(readFileSync('./full_build.json', 'utf8'));

const DOMAINS = await sql`SELECT id, code FROM "Domain"`;
const SKILLS = await sql`SELECT id, code FROM "Skill"`;
const domainId = Object.fromEntries(DOMAINS.map(d => [d.code, d.id]));
const skillId = Object.fromEntries(SKILLS.map(s => [s.code, s.id]));

const MODULE_CONFIG = {
  RW_M1:   { subject: 'READING_WRITING', order: 1, difficulty: 'STANDARD', title: 'Module 1', timeLimitMinutes: 32, adaptiveThresholdPct: 70 },
  RW_M2E:  { subject: 'READING_WRITING', order: 2, difficulty: 'EASY',     title: 'Module 2 (Easy)', timeLimitMinutes: 32, adaptiveThresholdPct: null },
  RW_M2H:  { subject: 'READING_WRITING', order: 2, difficulty: 'HARD',     title: 'Module 2 (Hard)', timeLimitMinutes: 32, adaptiveThresholdPct: null },
  MATH_M1: { subject: 'MATH', order: 1, difficulty: 'STANDARD', title: 'Module 1', timeLimitMinutes: 35, adaptiveThresholdPct: 70 },
  MATH_M2E:{ subject: 'MATH', order: 2, difficulty: 'EASY',     title: 'Module 2 (Easy)', timeLimitMinutes: 35, adaptiveThresholdPct: null },
  MATH_M2H:{ subject: 'MATH', order: 2, difficulty: 'HARD',     title: 'Module 2 (Hard)', timeLimitMinutes: 35, adaptiveThresholdPct: null },
};

async function ensureTest(title) {
  const existing = await sql`SELECT id FROM "Test" WHERE title=${title}`;
  if (existing.length) {
    console.log(`Test "${title}" already exists (id=${existing[0].id}) -- will insert modules/questions under it.`);
    return existing[0].id;
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Test" (id, title, description, type, status, "isAdaptive", "createdAt", "updatedAt")
    VALUES (${id}, ${title}, ${null}, 'FULL_LENGTH', 'DRAFT', true, now(), now())
  `;
  console.log(`Created Test "${title}" (id=${id}), status=DRAFT`);
  return id;
}

async function ensureModule(testId, key) {
  const cfg = MODULE_CONFIG[key];
  const existing = await sql`
    SELECT id FROM "Module" WHERE "testId"=${testId} AND subject=${cfg.subject} AND "order"=${cfg.order} AND difficulty=${cfg.difficulty}
  `;
  if (existing.length) {
    console.log(`  Module ${key} already exists (id=${existing[0].id}) -- skipping question insert to avoid duplicates. Delete it first if you want to rebuild.`);
    return { id: existing[0].id, isNew: false };
  }
  const id = randomUUID();
  await sql`
    INSERT INTO "Module" (id, "testId", subject, "order", difficulty, title, "timeLimitMinutes", "adaptiveThresholdPct")
    VALUES (${id}, ${testId}, ${cfg.subject}, ${cfg.order}, ${cfg.difficulty}, ${cfg.title}, ${cfg.timeLimitMinutes}, ${cfg.adaptiveThresholdPct})
  `;
  console.log(`  Created Module ${key} (id=${id})`);
  return { id, isNew: true };
}

async function insertQuestions(moduleId, subjectKind, questions) {
  let order = 1;
  for (const q of questions) {
    let passageId = null;
    if (subjectKind === 'RW') {
      passageId = randomUUID();
      await sql`
        INSERT INTO "Passage" (id, "moduleId", title, content, "imageUrl", source)
        VALUES (${passageId}, ${moduleId}, ${null}, ${q.passage}, ${null}, ${q._source || null})
      `;
    }
    const dId = domainId[q.domain];
    const sId = skillId[q.skill];
    if (!dId || !sId) throw new Error(`Missing domain/skill mapping for ${q.domain}/${q.skill}`);

    const questionId = randomUUID();
    const type = q.type === 'FREE_RESPONSE' ? 'FREE_RESPONSE' : 'MULTIPLE_CHOICE';
    const correctAnswerFR = type === 'FREE_RESPONSE' ? q.correctAnswerFR : null;

    await sql`
      INSERT INTO "Question" (id, "moduleId", "passageId", "domainId", "skillId", type, difficulty, stem, "imageUrl", "tableData", "order", points, "correctAnswerFR", "isPublished", source, "sourceUploadId", "createdAt", "updatedAt")
      VALUES (${questionId}, ${moduleId}, ${passageId}, ${dId}, ${sId}, ${type}, 'MEDIUM', ${q.stem}, ${null}, ${null}, ${order}, 1, ${correctAnswerFR}, false, ${q._source || 'MANUAL'}, ${null}, now(), now())
    `;

    if (type === 'MULTIPLE_CHOICE') {
      let choiceOrder = 0;
      for (const c of q.choices) {
        const choiceId = randomUUID();
        const isCorrect = c.label === q.correct;
        await sql`
          INSERT INTO "AnswerChoice" (id, "questionId", label, content, "isCorrect", "order")
          VALUES (${choiceId}, ${questionId}, ${c.label}, ${c.content}, ${isCorrect}, ${choiceOrder})
        `;
        choiceOrder++;
      }
    }
    order++;
  }
  return order - 1;
}

for (const [testKey, testTitle] of [['test3', 'Test 3'], ['test4', 'Test 4']]) {
  console.log(`\n=== ${testTitle} ===`);
  const testId = await ensureTest(testTitle);
  const modules = full[testKey];
  for (const [modKey, questions] of Object.entries(modules)) {
    const { id: moduleId, isNew } = await ensureModule(testId, modKey);
    if (!isNew) continue;
    const subjectKind = modKey.startsWith('RW') ? 'RW' : 'MATH';
    const count = await insertQuestions(moduleId, subjectKind, questions);
    console.log(`    Inserted ${count} questions into ${modKey}`);
  }
}

console.log('\nDone.');
