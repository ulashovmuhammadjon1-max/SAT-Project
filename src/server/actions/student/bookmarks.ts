"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export async function toggleBookmark(questionId: string) {
  const user = await requireUser();

  const existing = await prisma.bookmark.findUnique({
    where: { userId_questionId: { userId: user.id, questionId } },
  });

  if (existing) {
    await prisma.bookmark.delete({ where: { id: existing.id } });
  } else {
    await prisma.bookmark.create({ data: { userId: user.id, questionId } });
  }

  revalidatePath("/bookmarks");
  return { bookmarked: !existing };
}
