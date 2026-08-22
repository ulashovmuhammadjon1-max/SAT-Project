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

  // Named columns rather than whole rows.
  //
  // A full test review is 54+ questions, and `include` on each of question,
  // explanation, passage, domain and skill pulled every column of all five —
  // including `Question.imageUrl`, which holds base64 figures up to 898 KB. The
  // page then threw that straight away, because the page replaces it
  // with a short route URL. Fetching hundreds of kilobytes of base64 in order to
  // discard it costs Neon egress on the way out and Vercel Active CPU to
  // serialize, twice over, on every single review.
  //
  // Every explanation field IS used by this page, so those stay. `tableData`,
  // the audit columns and the foreign keys are not, so they go.
  const responses = await prisma.response.findMany({
    where: { attemptId: attempt.id },
    select: {
      id: true,
      questionId: true,
      moduleAttemptId: true,
      selectedChoiceId: true,
      freeResponseAnswer: true,
      isCorrect: true,
      flagged: true,
      changedAnswerCount: true,
      timeSpentSeconds: true,
      order: true,
      question: {
        select: {
          id: true,
          stem: true,
          type: true,
          difficulty: true,
          order: true,
          correctAnswerFR: true,
          // Presence only — the bytes are served by /api/question-image.
          imageUrl: false,
          choices: {
            select: { id: true, label: true, content: true, isCorrect: true },
            orderBy: { order: "asc" },
          },
          domain: { select: { name: true } },
          skill: { select: { name: true } },
          passage: { select: { title: true, content: true } },
          explanation: {
            select: {
              content: true, whyCorrect: true, whyWrongJson: true,
              commonMistakes: true, tips: true, relatedConcepts: true,
            },
          },
        },
      },
    },
    orderBy: { order: "asc" },
  });

  // Which of these questions carry a figure, as ids only.
  const withImage = new Set(
    (
      await prisma.question.findMany({
        where: { id: { in: responses.map((r) => r.questionId) }, imageUrl: { not: null } },
        select: { id: true },
      })
    ).map((q) => q.id)
  );

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
    imageUrl: withImage.has(r.question.id) ? `/api/question-image/${r.question.id}` : null,
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
