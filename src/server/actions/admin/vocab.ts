"use server";

import { revalidatePath } from "next/cache";
import type { VocabDifficulty } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export async function updateVocabWord(
  wordId: string,
  input: {
    term: string;
    definition: string;
    partOfSpeech?: string | null;
    exampleSentence?: string | null;
    difficulty: VocabDifficulty;
    synonyms: string[];
    antonyms: string[];
  }
) {
  await requireAdmin();
  await prisma.vocabWord.update({ where: { id: wordId }, data: input });
  revalidatePath("/admin/vocabulary");
}

export async function deleteVocabWord(wordId: string) {
  await requireAdmin();
  await prisma.vocabWord.delete({ where: { id: wordId } });
  revalidatePath("/admin/vocabulary");
}
