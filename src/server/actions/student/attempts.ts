"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { determineModule2Difficulty, SUBJECT_ORDER } from "@/lib/adaptive/engine";
import { estimateScaledScore, estimateTotalScore, sectionScoreForRaw, weightedSectionScore } from "@/lib/scoring/estimate";

function moduleSortKey(subject: string, order: number) {
  return SUBJECT_ORDER.indexOf(subject as (typeof SUBJECT_ORDER)[number]) * 10 + order;
}

export async function startAttempt(testId: string) {
  const user = await requireUser();

  const test = await prisma.test.findUniqueOrThrow({
    where: { id: testId },
    include: { modules: true },
  });

  const firstModule = [...test.modules]
    .filter((m) => m.order === 1)
    .sort((a, b) => moduleSortKey(a.subject, a.order) - moduleSortKey(b.subject, b.order))[0];

  if (!firstModule) throw new Error("This test has no modules configured yet.");

  const attempt = await prisma.attempt.create({
    data: {
      userId: user.id,
      testId,
      status: "IN_PROGRESS",
      currentModuleId: firstModule.id,
      moduleAttempts: { create: { moduleId: firstModule.id } },
    },
  });

  redirect(`/exam/${attempt.id}`);
}

export interface ResponsePayload {
  questionId: string;
  selectedChoiceId?: string | null;
  freeResponseAnswer?: string | null;
  timeSpentSeconds: number;
  flagged: boolean;
  changedAnswerCount: number;
  eliminatedChoiceIds: string[];
}

export async function autosaveResponses(attemptId: string, moduleAttemptId: string, responses: ResponsePayload[]) {
  const user = await requireUser();

  const attempt = await prisma.attempt.findUniqueOrThrow({ where: { id: attemptId } });
  if (attempt.userId !== user.id) throw new Error("Not authorized.");

  // `Response.order` defaults to 0 and was never written, so every row held 0
  // and anything sorting by it — the review page did — got raw database order
  // instead of question order. One lookup keyed by question id fixes that for
  // the whole batch; it is also written on update, so rows created before this
  // are corrected the next time the student touches the question.
  const questionOrder = new Map(
    (
      await prisma.question.findMany({
        where: { id: { in: responses.map((r) => r.questionId) } },
        select: { id: true, order: true },
      })
    ).map((q) => [q.id, q.order] as const)
  );

  for (const r of responses) {
    const order = questionOrder.get(r.questionId) ?? 0;
    await prisma.response.upsert({
      where: { attemptId_questionId: { attemptId, questionId: r.questionId } },
      create: {
        attemptId,
        moduleAttemptId,
        questionId: r.questionId,
        order,
        selectedChoiceId: r.selectedChoiceId,
        freeResponseAnswer: r.freeResponseAnswer,
        timeSpentSeconds: r.timeSpentSeconds,
        flagged: r.flagged,
        changedAnswerCount: r.changedAnswerCount,
        eliminatedChoiceIds: r.eliminatedChoiceIds,
        answeredAt: r.selectedChoiceId || r.freeResponseAnswer ? new Date() : null,
      },
      update: {
        order,
        selectedChoiceId: r.selectedChoiceId,
        freeResponseAnswer: r.freeResponseAnswer,
        timeSpentSeconds: r.timeSpentSeconds,
        flagged: r.flagged,
        changedAnswerCount: r.changedAnswerCount,
        eliminatedChoiceIds: r.eliminatedChoiceIds,
        answeredAt: r.selectedChoiceId || r.freeResponseAnswer ? new Date() : null,
      },
    });
  }
}

export async function pauseAttempt(attemptId: string) {
  const user = await requireUser();
  await prisma.attempt.updateMany({
    where: { id: attemptId, userId: user.id },
    data: { status: "PAUSED", pausedAt: new Date() },
  });
  revalidatePath("/dashboard");
}

/**
 * Creates the ModuleAttempt for the next module, tolerating a concurrent
 * duplicate submit. `submitModule` can legitimately be invoked twice for the
 * same module — the countdown timer auto-submits unconditionally the instant
 * it hits zero, with no awareness of a manual "End Module" click already in
 * flight — and `ModuleAttempt` has a `@@unique([attemptId, moduleId])`
 * constraint, so the loser of that race would otherwise crash with an
 * uncaught P2002 in the middle of a timed exam. Whoever loses the race just
 * adopts the winner's row instead of erroring.
 */
async function createOrGetModuleAttempt(attemptId: string, moduleId: string) {
  const existing = await prisma.moduleAttempt.findUnique({
    where: { attemptId_moduleId: { attemptId, moduleId } },
  });
  if (existing) return existing;

  try {
    return await prisma.moduleAttempt.create({ data: { attemptId, moduleId } });
  } catch (error) {
    const isUniqueViolation =
      typeof error === "object" && error !== null && "code" in error && (error as { code: string }).code === "P2002";
    if (!isUniqueViolation) throw error;
    return prisma.moduleAttempt.findUniqueOrThrow({ where: { attemptId_moduleId: { attemptId, moduleId } } });
  }
}

export async function submitModule(attemptId: string, moduleAttemptId: string) {
  const user = await requireUser();

  const attempt = await prisma.attempt.findUniqueOrThrow({
    where: { id: attemptId },
    include: { test: { include: { modules: true, adaptiveConfig: true } } },
  });
  if (attempt.userId !== user.id) throw new Error("Not authorized.");

  const moduleAttempt = await prisma.moduleAttempt.findUniqueOrThrow({
    where: { id: moduleAttemptId },
    include: { module: { include: { questions: true } } },
  });

  const responses = await prisma.response.findMany({
    where: { moduleAttemptId },
    include: { question: { include: { choices: true } } },
  });

  let correctCount = 0;
  for (const response of responses) {
    const question = response.question;
    let isCorrect = false;
    if (question.type === "MULTIPLE_CHOICE") {
      const correctChoice = question.choices.find((c) => c.isCorrect);
      isCorrect = !!correctChoice && correctChoice.id === response.selectedChoiceId;
    } else {
      const accepted: string[] = question.correctAnswerFR ? JSON.parse(question.correctAnswerFR) : [];
      isCorrect = accepted.some((a) => a.trim().toLowerCase() === (response.freeResponseAnswer ?? "").trim().toLowerCase());
    }
    await prisma.response.update({ where: { id: response.id }, data: { isCorrect } });
    if (isCorrect) correctCount += 1;
  }

  const totalCount = moduleAttempt.module.questions.length;
  // Indicative only, and never summed into a section score — the section is
  // converted once from both modules' combined raw score in `finalizeAttempt`.
  // A single module is half a section, so this is "what this pace is worth",
  // not a result.
  const scaledScore = estimateScaledScore(
    totalCount ? (correctCount / totalCount) * 100 : 0,
    moduleAttempt.module.subject === "MATH" ? "MATH" : "READING_WRITING",
  );

  await prisma.moduleAttempt.update({
    where: { id: moduleAttemptId },
    data: { submittedAt: new Date(), correctCount, totalCount, scaledScore },
  });

  const mod = moduleAttempt.module;
  const modules = attempt.test.modules;

  // Module 1 of a subject with adaptivity enabled -> branch to Module 2's difficulty.
  if (mod.order === 1 && attempt.test.isAdaptive) {
    // A threshold set on this specific module (from the PDF publish flow) wins;
    // otherwise fall back to the test's linked AdaptiveConfig, then a hard default.
    const configDefault =
      mod.subject === "MATH"
        ? attempt.test.adaptiveConfig?.mathThresholdPct ?? 70
        : attempt.test.adaptiveConfig?.rwThresholdPct ?? 70;
    const threshold = mod.adaptiveThresholdPct ?? configDefault;
    const difficulty = determineModule2Difficulty(correctCount, totalCount, threshold);

    const nextModule = modules.find((m) => m.subject === mod.subject && m.order === 2 && m.difficulty === difficulty);

    if (nextModule) {
      const nextModuleAttempt = await createOrGetModuleAttempt(attemptId, nextModule.id);
      await prisma.attempt.update({
        where: { id: attemptId },
        data: {
          currentModuleId: nextModule.id,
          module1ScorePct: totalCount ? (correctCount / totalCount) * 100 : 0,
          assignedModule2Level: difficulty,
        },
      });
      // Module 1 -> Module 2 of the same subject: no break, the student moves
      // straight on, exactly as Bluebook does.
      return {
        nextModuleId: nextModule.id,
        nextModuleAttemptId: nextModuleAttempt.id,
        finished: false,
        breakBefore: false,
        nextSubjectLabel: null as string | null,
      };
    }
  }

  // Otherwise: move to the next subject's Module 1, or finish the attempt.
  const currentSubjectIndex = SUBJECT_ORDER.indexOf(mod.subject as (typeof SUBJECT_ORDER)[number]);
  const remainingSubjects = SUBJECT_ORDER.filter((_, i) => i > currentSubjectIndex);
  const nextSubjectModule = modules.find(
    (m) => remainingSubjects.includes(m.subject as (typeof SUBJECT_ORDER)[number]) && m.order === 1
  );

  if (nextSubjectModule) {
    const nextModuleAttempt = await createOrGetModuleAttempt(attemptId, nextSubjectModule.id);
    await prisma.attempt.update({ where: { id: attemptId }, data: { currentModuleId: nextSubjectModule.id } });
    // Crossing into a new section (R&W -> Math) is the one point the real test
    // gives the student a break before the next module's clock starts.
    return {
      nextModuleId: nextSubjectModule.id,
      nextModuleAttemptId: nextModuleAttempt.id,
      finished: false,
      breakBefore: true,
      nextSubjectLabel: (nextSubjectModule.subject === "MATH" ? "Math" : "Reading and Writing") as string | null,
    };
  }

  return finalizeAttempt(attemptId);
}

async function finalizeAttempt(attemptId: string) {
  const moduleAttempts = await prisma.moduleAttempt.findMany({
    where: { attemptId },
    include: { module: true },
  });

  // Difficulty-weighted, Bluebook-style: every question in the modules the
  // student sat counts, an unanswered one as a miss, and each miss costs
  // points by its difficulty and by whether it is a writing question.
  const takenIds = moduleAttempts.filter((m) => m.submittedAt != null).map((m) => m.id);
  const [questions, responses] = await Promise.all([
    prisma.question.findMany({
      where: { moduleId: { in: moduleAttempts.filter((m) => m.submittedAt != null).map((m) => m.moduleId) } },
      select: { id: true, moduleId: true, difficulty: true, domain: { select: { code: true } } },
    }),
    prisma.response.findMany({
      where: { moduleAttemptId: { in: takenIds }, isCorrect: true },
      select: { questionId: true },
    }),
  ]);
  const correctIds = new Set(responses.map((r) => r.questionId));

  const sectionScore = (subject: "READING_WRITING" | "MATH"): number | null => {
    const taken = moduleAttempts.filter((m) => m.module.subject === subject && m.submittedAt != null);
    if (!taken.length) return null;
    const moduleIds = new Set(taken.map((m) => m.moduleId));
    const scored = questions
      .filter((q) => q.moduleId && moduleIds.has(q.moduleId))
      .map((q) => ({
        correct: correctIds.has(q.id),
        difficulty: q.difficulty,
        isWriting: q.domain.code === "SEC" || q.domain.code === "EOI",
      }));
    if (!scored.length) {
      // No question rows to weigh (should not happen): fall back to the raw table.
      const rawCorrect = taken.reduce((sum, m) => sum + (m.correctCount ?? 0), 0);
      const questionCount = taken.reduce((sum, m) => sum + (m.totalCount ?? 0), 0);
      return questionCount > 0 ? sectionScoreForRaw(subject, rawCorrect, questionCount) : null;
    }
    const module2 = taken.find((m) => m.module.order === 2);
    const route = module2 ? (module2.module.difficulty === "EASY" ? "EASY" : module2.module.difficulty === "HARD" ? "HARD" : null) : null;
    return weightedSectionScore(subject, scored, route);
  };

  const rwScaledScore = sectionScore("READING_WRITING");
  const mathScaledScore = sectionScore("MATH");
  const totalScaledScore = estimateTotalScore(rwScaledScore, mathScaledScore);

  await prisma.attempt.update({
    where: { id: attemptId },
    data: {
      status: "SUBMITTED",
      submittedAt: new Date(),
      currentModuleId: null,
      rwScaledScore,
      mathScaledScore,
      totalScaledScore,
    },
  });

  return {
    finished: true,
    nextModuleId: null,
    nextModuleAttemptId: null,
    breakBefore: false,
    nextSubjectLabel: null as string | null,
  };
}

/**
 * End the whole attempt now, because the student broke the leave-the-tab rule
 * (more than 6 leaves, or one absence over 2 minutes). Grades the module in
 * progress with what was answered and closes every remaining module empty,
 * through the same submitModule path, so scoring stays in one place.
 */
export async function forfeitAttempt(attemptId: string, moduleAttemptId: string) {
  const user = await requireUser();
  const attempt = await prisma.attempt.findUniqueOrThrow({ where: { id: attemptId } });
  if (attempt.userId !== user.id) throw new Error("Not authorized.");
  if (attempt.status === "SUBMITTED") return { finished: true };

  let current: string | null = moduleAttemptId;
  for (let i = 0; i < 8 && current; i++) {
    const result = await submitModule(attemptId, current);
    if (result.finished) return { finished: true };
    current = result.nextModuleAttemptId;
  }
  return { finished: true };
}
