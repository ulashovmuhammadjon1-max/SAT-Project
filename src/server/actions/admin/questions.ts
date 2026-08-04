"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { getExtractionProvider } from "@/lib/ai/extraction-service";
import type { QuestionDifficulty } from "@prisma/client";

export interface QuestionUpdateInput {
  stem: string;
  imageUrl?: string | null;
  domainId: string;
  skillId: string;
  difficulty: QuestionDifficulty;
  isPublished: boolean;
  choices: { id?: string; label: string; content: string; isCorrect: boolean; order: number }[];
}

export async function updateQuestion(questionId: string, input: QuestionUpdateInput) {
  await requireAdmin();

  await prisma.$transaction(async (tx) => {
    await tx.question.update({
      where: { id: questionId },
      data: {
        stem: input.stem,
        imageUrl: input.imageUrl,
        domainId: input.domainId,
        skillId: input.skillId,
        difficulty: input.difficulty,
        isPublished: input.isPublished,
      },
    });

    await tx.answerChoice.deleteMany({ where: { questionId } });
    await tx.answerChoice.createMany({
      data: input.choices.map((c) => ({
        questionId,
        label: c.label,
        content: c.content,
        isCorrect: c.isCorrect,
        order: c.order,
      })),
    });
  });

  revalidatePath(`/admin/questions/${questionId}`);
  revalidatePath("/admin/questions");
}

export async function updatePassage(passageId: string, content: string) {
  await requireAdmin();
  await prisma.passage.update({ where: { id: passageId }, data: { content } });
  revalidatePath("/admin/questions");
}

export async function deleteQuestion(questionId: string) {
  await requireAdmin();
  await prisma.question.delete({ where: { id: questionId } });
  revalidatePath("/admin/questions");
}

export async function saveExplanation(
  questionId: string,
  input: {
    content: string;
    whyCorrect: string;
    whyWrongJson: Record<string, string>;
    commonMistakes: string;
    tips: string;
    relatedConcepts: string;
  }
) {
  await requireAdmin();
  await prisma.explanation.upsert({
    where: { questionId },
    create: { questionId, ...input, source: "MANUAL" },
    update: { ...input, source: "MANUAL" },
  });
  revalidatePath(`/admin/questions/${questionId}`);
}

export async function generateExplanationDraft(questionId: string) {
  await requireAdmin();

  const question = await prisma.question.findUniqueOrThrow({
    where: { id: questionId },
    include: { choices: true, domain: true, skill: true },
  });

  const provider = getExtractionProvider();
  const draft = await provider.generateExplanation({
    stem: question.stem.replace(/<[^>]+>/g, ""),
    choices: question.choices.map((c) => ({ label: c.label, content: c.content, isCorrect: c.isCorrect })),
    domain: question.domain.name,
    skill: question.skill.name,
  });

  await prisma.explanation.upsert({
    where: { questionId },
    create: { questionId, ...draft, source: "AI_GENERATED", generatedAt: new Date() },
    update: { ...draft, source: "AI_GENERATED", generatedAt: new Date() },
  });

  revalidatePath(`/admin/questions/${questionId}`);
  return draft;
}
