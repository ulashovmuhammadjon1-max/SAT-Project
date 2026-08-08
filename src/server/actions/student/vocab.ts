"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { scheduleNextReview, statusForRepetitions } from "@/lib/srs/scheduler";
import { passThresholdFor } from "@/lib/vocab-constants";

export async function getVocabCollections() {
  const user = await requireUser();

  const collections = await prisma.vocabCollection.findMany({
    orderBy: { order: "asc" },
    include: { decks: { where: { order: { not: null } }, select: { id: true } } },
  });

  const progressRows = await prisma.vocabDeckProgress.findMany({
    where: { userId: user.id, passed: true },
    select: { deckId: true },
  });
  const passedDeckIds = new Set(progressRows.map((p) => p.deckId));

  return collections.map((c) => ({
    id: c.id,
    name: c.name,
    description: c.description,
    setCount: c.decks.length,
    setsCompleted: c.decks.filter((d) => passedDeckIds.has(d.id)).length,
  }));
}

export async function getVocabSets(collectionId: string) {
  const user = await requireUser();

  const [decks, progressRows] = await Promise.all([
    prisma.vocabDeck.findMany({
      where: { collectionId, order: { not: null } },
      orderBy: { order: "asc" },
      include: { _count: { select: { words: true, quizQuestions: true } } },
    }),
    prisma.vocabDeckProgress.findMany({ where: { userId: user.id } }),
  ]);

  const progressByDeck = new Map(progressRows.map((p) => [p.deckId, p]));

  return decks.map((deck, i) => {
    const progress = progressByDeck.get(deck.id);
    const previousDeck = decks[i - 1];
    const previousPassed = !previousDeck || progressByDeck.get(previousDeck.id)?.passed === true;
    return {
      id: deck.id,
      collectionId,
      name: deck.name,
      order: deck.order!,
      wordCount: deck._count.words,
      quizCount: deck._count.quizQuestions,
      passed: progress?.passed ?? false,
      bestScore: progress?.bestScore ?? 0,
      attempts: progress?.attempts ?? 0,
      unlocked: previousPassed,
    };
  });
}

export async function getVocabSetDetail(deckId: string) {
  const user = await requireUser();

  const deckMeta = await prisma.vocabDeck.findUnique({ where: { id: deckId }, select: { collectionId: true } });
  if (!deckMeta?.collectionId) throw new Error("Set not found.");

  const sets = await getVocabSets(deckMeta.collectionId);
  const meta = sets.find((s) => s.id === deckId);
  if (!meta) throw new Error("Set not found.");
  if (!meta.unlocked) throw new Error("Complete the previous set's quiz first to unlock this one.");

  const deck = await prisma.vocabDeck.findUniqueOrThrow({
    where: { id: deckId },
    include: {
      words: { include: { word: true }, orderBy: { order: "asc" } },
      quizQuestions: { orderBy: { order: "asc" } },
    },
  });

  const progress = await prisma.vocabDeckProgress.findUnique({
    where: { userId_deckId: { userId: user.id, deckId } },
  });

  return {
    id: deck.id,
    collectionId: deckMeta.collectionId,
    name: deck.name,
    passageTitle: deck.passageTitle,
    passage: deck.passage,
    words: deck.words.map((dw) => ({
      id: dw.word.id,
      term: dw.word.term,
      definition: dw.word.definition,
      example: dw.word.exampleSentence,
      antonym: Array.isArray(dw.word.antonyms) ? (dw.word.antonyms as string[])[0] : null,
    })),
    quiz: deck.quizQuestions.map((q) => ({
      id: q.id,
      order: q.order,
      stem: q.stem,
      choices: { A: q.choiceA, B: q.choiceB, C: q.choiceC, D: q.choiceD },
      // correct answer intentionally omitted from the client-facing payload
    })),
    passed: progress?.passed ?? false,
    bestScore: progress?.bestScore ?? 0,
    attempts: progress?.attempts ?? 0,
  };
}

export interface SubmitSetQuizResult {
  score: number;
  total: number;
  passed: boolean;
  passThreshold: number;
  correctAnswers: Record<string, "A" | "B" | "C" | "D">;
}

export async function submitVocabSetQuiz(
  deckId: string,
  answers: Record<string, "A" | "B" | "C" | "D">
): Promise<SubmitSetQuizResult> {
  const user = await requireUser();

  const questions = await prisma.vocabSetQuizQuestion.findMany({ where: { deckId } });
  if (questions.length === 0) throw new Error("This set has no quiz questions.");

  let score = 0;
  const correctAnswers: Record<string, "A" | "B" | "C" | "D"> = {};
  for (const q of questions) {
    correctAnswers[q.id] = q.correct as "A" | "B" | "C" | "D";
    if (answers[q.id] === q.correct) score++;
  }

  const passThreshold = passThresholdFor(questions.length);
  const passed = score >= passThreshold;

  const existing = await prisma.vocabDeckProgress.findUnique({
    where: { userId_deckId: { userId: user.id, deckId } },
  });

  await prisma.vocabDeckProgress.upsert({
    where: { userId_deckId: { userId: user.id, deckId } },
    create: {
      userId: user.id,
      deckId,
      bestScore: score,
      attempts: 1,
      passed,
      completedAt: passed ? new Date() : null,
    },
    update: {
      bestScore: Math.max(score, existing?.bestScore ?? 0),
      attempts: { increment: 1 },
      passed: passed || existing?.passed === true,
      completedAt: passed && !existing?.passed ? new Date() : existing?.completedAt,
    },
  });

  const deck = await prisma.vocabDeck.findUnique({ where: { id: deckId }, select: { collectionId: true } });
  revalidatePath(`/vocabulary/sets/${deck?.collectionId}`);
  revalidatePath(`/vocabulary/sets/${deck?.collectionId}/${deckId}`);

  return { score, total: questions.length, passed, passThreshold, correctAnswers };
}

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

export interface DeletePersonalWordResult {
  error?: string;
  success?: boolean;
}

export async function deletePersonalWord(wordId: string): Promise<DeletePersonalWordResult> {
  const user = await requireUser();
  const word = await prisma.vocabWord.findUnique({ where: { id: wordId } });
  // A concurrent double-click (or an already-removed word) — treat as done
  // rather than crashing, since the end state the user wanted is achieved.
  if (!word) return { success: true };
  if (word.createdById !== user.id) return { error: "You can only delete words you added yourself." };

  try {
    await prisma.vocabWord.delete({ where: { id: wordId } });
  } catch (error) {
    console.error("[vocab] Failed to delete personal word", wordId, error);
    return { error: "Couldn't delete this word. Please try again." };
  }

  revalidatePath("/vocabulary");
  return { success: true };
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
