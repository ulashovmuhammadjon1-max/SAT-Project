import { notFound, redirect } from "next/navigation";

import { ReviewShell } from "@/components/exam/review-shell";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export const dynamic = "force-dynamic";

export default async function ReviewPage({ params }: { params: { attemptId: string } }) {
  const user = await requireUser();

  const attempt = await prisma.attempt.findUnique({
    where: { id: params.attemptId },
    include: {
      test: true,
      moduleAttempts: {
        orderBy: { startedAt: "asc" },
        include: { module: true },
      },
    },
  });

  if (!attempt || attempt.userId !== user.id) notFound();
  if (attempt.status !== "SUBMITTED") redirect(`/exam/${attempt.id}`);

  const responses = await prisma.response.findMany({
    where: { attemptId: attempt.id },
    include: {
      question: {
        include: { choices: { orderBy: { order: "asc" } }, domain: true, skill: true, explanation: true, passage: true },
      },
      selectedChoice: true,
    },
    orderBy: { order: "asc" },
  });

  const subjectByModuleAttemptId = Object.fromEntries(
    attempt.moduleAttempts.map((ma) => [ma.id, ma.module.subject])
  );

  const items = responses.map((r) => ({
    responseId: r.id,
    questionId: r.questionId,
    subject: subjectByModuleAttemptId[r.moduleAttemptId] ?? "READING_WRITING",
    stem: r.question.stem,
    passage: r.question.passage ? { title: r.question.passage.title, content: r.question.passage.content } : null,
    imageUrl: r.question.imageUrl,
    type: r.question.type,
    difficulty: r.question.difficulty,
    domain: r.question.domain.name,
    skill: r.question.skill.name,
    choices: r.question.choices.map((c) => ({ id: c.id, label: c.label, content: c.content, isCorrect: c.isCorrect })),
    correctAnswerFR: r.question.correctAnswerFR ? (JSON.parse(r.question.correctAnswerFR)[0] ?? null) : null,
    selectedChoiceId: r.selectedChoiceId,
    freeResponseAnswer: r.freeResponseAnswer,
    isCorrect: r.isCorrect,
    flagged: r.flagged,
    changedAnswerCount: r.changedAnswerCount,
    timeSpentSeconds: r.timeSpentSeconds,
    explanation: r.question.explanation
      ? {
          content: r.question.explanation.content,
          whyCorrect: r.question.explanation.whyCorrect,
          commonMistakes: r.question.explanation.commonMistakes,
          tips: r.question.explanation.tips,
          relatedConcepts: r.question.explanation.relatedConcepts,
        }
      : null,
  }));

  const correctCount = items.filter((i) => i.isCorrect).length;

  return (
    <ReviewShell
      testTitle={attempt.test.title}
      totalScaledScore={attempt.totalScaledScore}
      rwScaledScore={attempt.rwScaledScore}
      mathScaledScore={attempt.mathScaledScore}
      correctCount={correctCount}
      totalCount={items.length}
      items={items}
    />
  );
}
