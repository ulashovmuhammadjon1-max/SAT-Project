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

  // Review order. Two things were wrong here and both had to be fixed.
  //
  // `Response.order` is `@default(0)` and `autosaveResponses` never set it, so
  // every row held 0 and the `orderBy` above sorted nothing — questions came
  // back in raw database order. That is now populated on write, but the column
  // cannot be trusted for attempts submitted before then, so the ordering here
  // is derived from `Question.order` instead, which the inserter guarantees is
  // contiguous from 1 in every module.
  //
  // Even with a correct value, sorting on it alone is not enough: it is the
  // position *within a module*, so Module 1 and Module 2 interleave and Reading
  // and Writing reads 1, 1, 2, 2, … instead of 1 through 54. The module the
  // student sat first has to come first. `moduleAttempts` is already ordered by
  // `startedAt`, which is that real sequence; the subject rank keeps Reading
  // and Writing ahead of Math even if timestamps tie.
  const moduleSequence = new Map(
    attempt.moduleAttempts.map((ma, index) => [ma.id, index] as const)
  );
  const subjectRank = (subject: string) => (subject === "READING_WRITING" ? 0 : 1);
  const sequenceOf = (moduleAttemptId: string) =>
    moduleSequence.get(moduleAttemptId) ?? Number.MAX_SAFE_INTEGER;

  responses.sort((a, b) => {
    const bySubject =
      subjectRank(subjectByModuleAttemptId[a.moduleAttemptId] ?? "READING_WRITING") -
      subjectRank(subjectByModuleAttemptId[b.moduleAttemptId] ?? "READING_WRITING");
    if (bySubject !== 0) return bySubject;
    const byModule = sequenceOf(a.moduleAttemptId) - sequenceOf(b.moduleAttemptId);
    if (byModule !== 0) return byModule;
    return a.question.order - b.question.order;
  });

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
          // Stored as { [choiceLabel]: reason }. Cast rather than trusting the
          // Json column's shape blindly — an older row may hold anything.
          whyWrong:
            r.question.explanation.whyWrongJson &&
            typeof r.question.explanation.whyWrongJson === "object" &&
            !Array.isArray(r.question.explanation.whyWrongJson)
              ? (r.question.explanation.whyWrongJson as Record<string, string>)
              : null,
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
