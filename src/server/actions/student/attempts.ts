"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { determineModule2Difficulty, SUBJECT_ORDER } from "@/lib/adaptive/engine";
import { estimateScaledScore } from "@/lib/scoring/estimate";

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

  for (const r of responses) {
    await prisma.response.upsert({
      where: { attemptId_questionId: { attemptId, questionId: r.questionId } },
      create: {
        attemptId,
        moduleAttemptId,
        questionId: r.questionId,
        selectedChoiceId: r.selectedChoiceId,
        freeResponseAnswer: r.freeResponseAnswer,
        timeSpentSeconds: r.timeSpentSeconds,
        flagged: r.flagged,
        changedAnswerCount: r.changedAnswerCount,
        eliminatedChoiceIds: r.eliminatedChoiceIds,
        answeredAt: r.selectedChoiceId || r.freeResponseAnswer ? new Date() : null,
      },
      update: {
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
  const scaledScore = estimateScaledScore(totalCount ? (correctCount / totalCount) * 100 : 0);

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
      const nextModuleAttempt = await prisma.moduleAttempt.create({
        data: { attemptId, moduleId: nextModule.id },
      });
      await prisma.attempt.update({
        where: { id: attemptId },
        data: {
          currentModuleId: nextModule.id,
          module1ScorePct: totalCount ? (correctCount / totalCount) * 100 : 0,
          assignedModule2Level: difficulty,
        },
      });
      return { nextModuleId: nextModule.id, nextModuleAttemptId: nextModuleAttempt.id, finished: false };
    }
  }

  // Otherwise: move to the next subject's Module 1, or finish the attempt.
  const currentSubjectIndex = SUBJECT_ORDER.indexOf(mod.subject as (typeof SUBJECT_ORDER)[number]);
  const remainingSubjects = SUBJECT_ORDER.filter((_, i) => i > currentSubjectIndex);
  const nextSubjectModule = modules.find(
    (m) => remainingSubjects.includes(m.subject as (typeof SUBJECT_ORDER)[number]) && m.order === 1
  );

  if (nextSubjectModule) {
    const nextModuleAttempt = await prisma.moduleAttempt.create({
      data: { attemptId, moduleId: nextSubjectModule.id },
    });
    await prisma.attempt.update({ where: { id: attemptId }, data: { currentModuleId: nextSubjectModule.id } });
    return { nextModuleId: nextSubjectModule.id, nextModuleAttemptId: nextModuleAttempt.id, finished: false };
  }

  return finalizeAttempt(attemptId);
}

async function finalizeAttempt(attemptId: string) {
  const moduleAttempts = await prisma.moduleAttempt.findMany({
    where: { attemptId },
    include: { module: true },
  });

  const rwScores = moduleAttempts.filter((m) => m.module.subject === "READING_WRITING" && m.scaledScore != null);
  const mathScores = moduleAttempts.filter((m) => m.module.subject === "MATH" && m.scaledScore != null);

  const avg = (arr: typeof moduleAttempts) =>
    arr.length ? Math.round(arr.reduce((sum, m) => sum + (m.scaledScore ?? 0), 0) / arr.length) : null;

  const rwScaledScore = avg(rwScores);
  const mathScaledScore = avg(mathScores);
  const totalScaledScore = rwScaledScore != null && mathScaledScore != null ? rwScaledScore + mathScaledScore : null;

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

  return { finished: true, nextModuleId: null, nextModuleAttemptId: null };
}
