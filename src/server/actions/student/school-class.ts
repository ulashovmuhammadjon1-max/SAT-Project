"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * Joining and leaving classes. Everything else the student sees — the class
 * list, class home, assignments, submissions — lives in classroom.ts.
 *
 * A code is something a teacher writes on a whiteboard, so matching is
 * forgiving: case-insensitive, spaces and dashes ignored.
 */

const codeSchema = z.string().trim().min(4).max(24);

function normalize(code: string): string {
  return code.toUpperCase().replace(/[\s-]/g, "");
}

export async function joinClass(
  rawCode: unknown,
): Promise<{ ok?: boolean; error?: string; classId?: string; className?: string; teacherName?: string }> {
  const user = await requireUser();

  const parsed = codeSchema.safeParse(rawCode);
  if (!parsed.success) return { error: "Enter the class code your teacher gave you." };
  const code = normalize(parsed.data);

  const cls = await prisma.schoolClass.findFirst({
    where: { code, isArchived: false },
    select: { id: true, name: true, school: true, teacherName: true },
  });
  if (!cls) return { error: "No class with that code. Check it with your teacher." };

  // Idempotent: joining a class you are already in is a no-op, not an error.
  await prisma.classMembership.upsert({
    where: { classId_userId: { classId: cls.id, userId: user.id } },
    create: { classId: cls.id, userId: user.id },
    update: {},
  });

  revalidatePath("/classes");
  return {
    ok: true,
    classId: cls.id,
    className: `${cls.name} — ${cls.school}`,
    teacherName: cls.teacherName,
  };
}

export async function leaveClass(classId: string): Promise<{ ok?: boolean; error?: string }> {
  const user = await requireUser();
  await prisma.classMembership.deleteMany({ where: { classId, userId: user.id } });
  revalidatePath("/classes");
  return { ok: true };
}
