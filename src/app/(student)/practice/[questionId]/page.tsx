import { notFound } from "next/navigation";

import { PracticeQuestion } from "@/components/student/practice-question";
import { prisma } from "@/lib/prisma";
import { questionImageSrc } from "@/lib/question-image";
import { requireUser } from "@/lib/session";

export const dynamic = "force-dynamic";

export default async function PracticeQuestionPage({ params }: { params: { questionId: string } }) {
  const user = await requireUser();

  const question = await prisma.question.findUnique({
    where: { id: params.questionId },
    include: {
      choices: { orderBy: { order: "asc" } },
      passage: true,
      domain: true,
      skill: true,
      explanation: true,
    },
  });

  if (!question || !question.isPublished) notFound();

  const nextQuestion = await prisma.question.findFirst({
    where: { domainId: question.domainId, isPublished: true, id: { not: question.id } },
    orderBy: { createdAt: "desc" },
  });

  const bookmark = await prisma.bookmark.findUnique({
    where: { userId_questionId: { userId: user.id, questionId: question.id } },
  });

  return (
    <PracticeQuestion
      question={{
        id: question.id,
        stem: question.stem,
        imageUrl: questionImageSrc(question.id, question.imageUrl),
        type: question.type,
        difficulty: question.difficulty,
        domain: question.domain.name,
        skill: question.skill.name,
        passage: question.passage ? { title: question.passage.title, content: question.passage.content } : null,
        choices: question.choices.map((c) => ({ id: c.id, label: c.label, content: c.content, isCorrect: c.isCorrect })),
        correctAnswerFR: question.correctAnswerFR ? JSON.parse(question.correctAnswerFR)[0] ?? null : null,
        explanation: question.explanation
          ? { content: question.explanation.content, tips: question.explanation.tips, commonMistakes: question.explanation.commonMistakes }
          : null,
      }}
      nextQuestionId={nextQuestion?.id ?? null}
      initiallyBookmarked={!!bookmark}
    />
  );
}
