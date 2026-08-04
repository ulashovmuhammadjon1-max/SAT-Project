"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { scheduleNextReview, statusForRepetitions } from "@/lib/srs/scheduler";

export async function getDueWords(limit = 20) {
  const user = await requireUser();

  const due = await prisma.vocabProgress.findMany({
    where: { userId: user.id, nextReviewAt: { lte: new Date() } },
    include: { word: true },
    orderBy: { nextReviewAt: "asc" },
    take: limit,
  });

  if (due.length >= limit) return due.map((d) => d.word);

  const seenWordIds = due.map((d) => d.wordId);
  const newWords = await prisma.vocabWord.findMany({
    where: {
      id: { notIn: seenWordIds },
      progress: { none: { userId: user.id } },
      OR: [{ visibility: "PUBLIC" }, { createdById: user.id }],
    },
    take: limit - due.length,
    orderBy: { createdAt: "asc" },
  });

  return [...due.map((d) => d.word), ...newWords];
}

export async function addPersonalWord(input: {
  term: string;
  definition: string;
  partOfSpeech?: string;
  exampleSentence?: string;
  synonyms?: string[];
  antonyms?: string[];
  difficulty?: "EASY" | "MEDIUM" | "HARD";
}) {
  const user = await requireUser();
  if (!input.term.trim() || !input.definition.trim()) {
    throw new Error("A term and definition are required.");
  }

  const word = await prisma.vocabWord.create({
    data: {
      term: input.term.trim(),
      definition: input.definition.trim(),
      partOfSpeech: input.partOfSpeech?.trim() || null,
      exampleSentence: input.exampleSentence?.trim() || null,
      synonyms: input.synonyms ?? [],
      antonyms: input.antonyms ?? [],
      difficulty: input.difficulty ?? "MEDIUM",
      createdById: user.id,
      visibility: "PRIVATE",
    },
  });

  // Seed it into this student's rotation right away instead of waiting for
  // getDueWords' "new word" fallback to notice it.
  await prisma.vocabProgress.create({
    data: { userId: user.id, wordId: word.id, status: "NEW", nextReviewAt: new Date() },
  });

  revalidatePath("/vocabulary");
  return word;
}

export async function deletePersonalWord(wordId: string) {
  const user = await requireUser();
  const word = await prisma.vocabWord.findUniqueOrThrow({ where: { id: wordId } });
  if (word.createdById !== user.id) throw new Error("You can only delete words you added yourself.");
  await prisma.vocabWord.delete({ where: { id: wordId } });
  revalidatePath("/vocabulary");
}

export async function reviewWord(wordId: string, quality: 0 | 1 | 2 | 3 | 4 | 5) {
  const user = await requireUser();

  const existing = await prisma.vocabProgress.findUnique({
    where: { userId_wordId: { userId: user.id, wordId } },
  });

  const state = scheduleNextReview(
    {
      easeFactor: existing?.easeFactor ?? 2.5,
      intervalDays: existing?.intervalDays ?? 0,
      repetitions: existing?.repetitions ?? 0,
    },
    quality
  );

  await prisma.vocabProgress.upsert({
    where: { userId_wordId: { userId: user.id, wordId } },
    create: {
      userId: user.id,
      wordId,
      easeFactor: state.easeFactor,
      intervalDays: state.intervalDays,
      repetitions: state.repetitions,
      correctStreak: quality >= 3 ? 1 : 0,
      status: statusForRepetitions(state.repetitions),
      lastReviewedAt: new Date(),
      nextReviewAt: state.nextReviewAt,
    },
    update: {
      easeFactor: state.easeFactor,
      intervalDays: state.intervalDays,
      repetitions: state.repetitions,
      correctStreak: quality >= 3 ? { increment: 1 } : 0,
      status: statusForRepetitions(state.repetitions),
      lastReviewedAt: new Date(),
      nextReviewAt: state.nextReviewAt,
    },
  });

  const today = new Date();
  today.setHours(0, 0, 0, 0);
  await prisma.studyActivity.upsert({
    where: { userId_date: { userId: user.id, date: today } },
    create: { userId: user.id, date: today, vocabReviewed: 1 },
    update: { vocabReviewed: { increment: 1 } },
  });

  revalidatePath("/vocabulary");
}
