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

export interface DeleteQuestionResult {
  error?: string;
  success?: boolean;
}

export async function deleteQuestion(questionId: string): Promise<DeleteQuestionResult> {
  await requireAdmin();
  try {
    await prisma.question.delete({ where: { id: questionId } });
  } catch (error) {
    console.error("[admin] Failed to delete question", questionId, error);
    // Response.question has no cascade, by design: deleting one question out
    // of a module a student already took would leave that attempt's stored
    // score counts stale (they aren't recomputed on delete), which is worse
    // than just blocking. Unpublishing keeps it out of future tests without
    // touching anything a student has already seen.
    return {
      error: "This question has already been answered by students, so it can't be deleted. Unpublish it instead to keep it out of future tests.",
    };
  }
  revalidatePath("/admin/questions");
  return { success: true };
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
