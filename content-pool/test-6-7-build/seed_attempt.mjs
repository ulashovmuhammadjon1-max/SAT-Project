/**
 * Seed a throwaway Attempt so a built test can be checked in the REAL exam
 * interface (/exam/{attemptId}), not just the admin preview.
 *
 * CLAUDE.md requires this step before shipping: the admin preview and the exam
 * page have matched every time so far, but the exam page is what the student
 * actually sees and is the only check that counts.
 *
 * Mirrors what startAttempt() does in src/server/actions/student/attempts.ts.
 * Deletes any previous attempt for the same user+test first, so it is safe to
 * re-run. Local development database only.
 *
 *   node seed_attempt.mjs "Test 6" MATH 2 HARD
 */
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();
const title = process.argv[2] ?? "Test 5";
const subject = process.argv[3] ?? "READING_WRITING";
const order = Number(process.argv[4] ?? 1);
const difficulty = process.argv[5] ?? null;

const user = await prisma.user.findFirst({ where: { role: "STUDENT" } });
const test = await prisma.test.findFirst({ where: { title } });
if (!user || !test) throw new Error(`no student user, or no test titled "${title}"`);

const mod = await prisma.module.findFirst({
  where: { testId: test.id, subject, order, ...(difficulty ? { difficulty } : {}) },
});
if (!mod) throw new Error(`no ${subject} Module ${order} ${difficulty ?? ""} on "${title}"`);

for (const a of await prisma.attempt.findMany({ where: { userId: user.id, testId: test.id } })) {
  await prisma.response.deleteMany({ where: { attemptId: a.id } });
  await prisma.moduleAttempt.deleteMany({ where: { attemptId: a.id } });
  await prisma.attempt.delete({ where: { id: a.id } });
}

const attempt = await prisma.attempt.create({
  data: {
    userId: user.id,
    testId: test.id,
    status: "IN_PROGRESS",
    currentModuleId: mod.id,
    moduleAttempts: { create: { moduleId: mod.id } },
  },
});

console.log(attempt.id);
await prisma.$disconnect();
