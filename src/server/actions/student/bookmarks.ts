"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

function prismaErrorCode(error: unknown): string | undefined {
  return typeof error === "object" && error !== null && "code" in error ? (error as { code: string }).code : undefined;
}

export async function toggleBookmark(questionId: string) {
  const user = await requireUser();

  const existing = await prisma.bookmark.findUnique({
    where: { userId_questionId: { userId: user.id, questionId } },
  });

  try {
    if (existing) {
      await prisma.bookmark.delete({ where: { id: existing.id } });
    } else {
      await prisma.bookmark.create({ data: { userId: user.id, questionId } });
    }
  } catch (error) {
    // The check-then-act above races a double-click (or a slow tap that
    // fires twice): both calls can read "not bookmarked yet" and both try to
    // create (P2002), or both read "bookmarked" and both try to delete
    // (P2025 on the second one, since the first already removed it). Either
    // way the row ends up in the state the user asked for, so treat the
    // loser of the race as a success rather than crashing the page.
    const code = prismaErrorCode(error);
    const isDuplicateCreate = code === "P2002" && !existing;
    const isDoubleDelete = code === "P2025" && !!existing;
    if (!isDuplicateCreate && !isDoubleDelete) throw error;
  }

  revalidatePath("/bookmarks");
  return { bookmarked: !existing };
}
