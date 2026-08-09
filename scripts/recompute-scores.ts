/**
 * Rescore every submitted attempt with the current conversion table.
 *
 * Needed because scores are stored, not derived on read: attempts submitted
 * before the scoring fix carry values the SAT cannot award (a student reported
 * a 336) and section scores that were averaged across modules rather than
 * converted once from the combined raw score.
 *
 * Safe to re-run — it recomputes from the stored raw counts every time and
 * writes only where the result differs.
 *
 *   npx tsx scripts/recompute-scores.ts --dry-run   # report, change nothing
 *   npx tsx scripts/recompute-scores.ts             # apply
 *
 * Uses whatever `DATABASE_URL` is set, so point it at production deliberately.
 */

import { PrismaClient } from "@prisma/client";

import { estimateScaledScore, estimateTotalScore, sectionScoreForRaw } from "../src/lib/scoring/estimate";

const prisma = new PrismaClient();
const dryRun = process.argv.includes("--dry-run");

async function main() {
  const attempts = await prisma.attempt.findMany({
    where: { status: "SUBMITTED" },
    select: {
      id: true,
      rwScaledScore: true,
      mathScaledScore: true,
      totalScaledScore: true,
      moduleAttempts: {
        select: {
          id: true,
          correctCount: true,
          totalCount: true,
          scaledScore: true,
          submittedAt: true,
          module: { select: { subject: true } },
        },
      },
    },
  });

  console.log(`${attempts.length} submitted attempt${attempts.length === 1 ? "" : "s"} to check.`);

  let attemptsChanged = 0;
  let modulesChanged = 0;
  let illegalBefore = 0;

  for (const attempt of attempts) {
    const taken = attempt.moduleAttempts.filter((m) => m.submittedAt != null);

    const sectionScore = (subject: "READING_WRITING" | "MATH"): number | null => {
      const forSubject = taken.filter((m) => m.module.subject === subject);
      if (!forSubject.length) return null;
      const rawCorrect = forSubject.reduce((sum, m) => sum + (m.correctCount ?? 0), 0);
      const questionCount = forSubject.reduce((sum, m) => sum + (m.totalCount ?? 0), 0);
      if (questionCount <= 0) return null;
      return sectionScoreForRaw(subject, rawCorrect, questionCount);
    };

    const rw = sectionScore("READING_WRITING");
    const math = sectionScore("MATH");
    const total = estimateTotalScore(rw, math);

    for (const previous of [attempt.rwScaledScore, attempt.mathScaledScore, attempt.totalScaledScore]) {
      if (previous != null && previous % 10 !== 0) illegalBefore += 1;
    }

    const changed =
      rw !== attempt.rwScaledScore || math !== attempt.mathScaledScore || total !== attempt.totalScaledScore;

    if (changed) {
      attemptsChanged += 1;
      console.log(
        `  attempt ${attempt.id}: ` +
          `R&W ${attempt.rwScaledScore ?? "—"}→${rw ?? "—"}, ` +
          `Math ${attempt.mathScaledScore ?? "—"}→${math ?? "—"}, ` +
          `Total ${attempt.totalScaledScore ?? "—"}→${total ?? "—"}`,
      );
      if (!dryRun) {
        await prisma.attempt.update({
          where: { id: attempt.id },
          data: { rwScaledScore: rw, mathScaledScore: math, totalScaledScore: total },
        });
      }
    }

    // The per-module figure is indicative only and never summed into a section
    // score, but it is shown in places, so it should be a legal score too.
    for (const moduleAttempt of taken) {
      const count = moduleAttempt.totalCount ?? 0;
      if (count <= 0) continue;
      const subject = moduleAttempt.module.subject === "MATH" ? "MATH" : "READING_WRITING";
      const indicative = estimateScaledScore(((moduleAttempt.correctCount ?? 0) / count) * 100, subject);
      if (indicative !== moduleAttempt.scaledScore) {
        modulesChanged += 1;
        if (!dryRun) {
          await prisma.moduleAttempt.update({
            where: { id: moduleAttempt.id },
            data: { scaledScore: indicative },
          });
        }
      }
    }
  }

  console.log(
    `\n${dryRun ? "Would update" : "Updated"} ${attemptsChanged} attempt${attemptsChanged === 1 ? "" : "s"} ` +
      `and ${modulesChanged} module score${modulesChanged === 1 ? "" : "s"}.`,
  );
  if (illegalBefore) {
    console.log(`${illegalBefore} stored score${illegalBefore === 1 ? " was" : "s were"} not a multiple of 10.`);
  }
}

main()
  .catch((error) => {
    console.error(error);
    process.exit(1);
  })
  .finally(() => prisma.$disconnect());
