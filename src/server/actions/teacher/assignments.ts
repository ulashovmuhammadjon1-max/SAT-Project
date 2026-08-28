"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * Teacher-set assignments.
 *
 * Two kinds, decided by whether a practice test is linked:
 *  - test assignments: completion is DERIVED from a submitted attempt of that
 *    test, so it cannot be faked by ticking a box and the teacher sees the
 *    actual score next to the name;
 *  - free-form tasks ("watch the lecture", "bring your essay"): students mark
 *    them done themselves.
 */

async function requireOwnClass(classId: string) {
  const user = await requireUser();
  const cls = await prisma.schoolClass.findUnique({
    where: { id: classId },
    select: { id: true, teacherUserId: true, isArchived: true },
  });
  if (!cls || cls.isArchived || cls.teacherUserId !== user.id) {
    throw new Error("Not your class");
  }
  return user;
}

const createSchema = z.object({
  classId: z.string().min(1),
  title: z.string().trim().min(3, "Give the task a title.").max(160),
  instructions: z.string().trim().max(2000).optional().or(z.literal("")),
  testId: z.string().optional().or(z.literal("")),
  dueAt: z.coerce.date().optional().nullable(),
});

export async function createAssignment(input: {
  classId: string;
  title: unknown;
  instructions?: unknown;
  testId?: unknown;
  dueAt?: string | null;
}): Promise<{ ok?: boolean; error?: string }> {
  const parsed = createSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the assignment details." };
  }
  try {
    await requireOwnClass(parsed.data.classId);
  } catch {
    return { error: "That class is not linked to your account." };
  }

  if (parsed.data.testId) {
    const test = await prisma.test.findFirst({
      where: { id: parsed.data.testId, status: "PUBLISHED" },
      select: { id: true },
    });
    if (!test) return { error: "That practice test does not exist or is not published." };
  }
  if (parsed.data.dueAt && parsed.data.dueAt.getTime() < Date.now()) {
    return { error: "The due date is already in the past." };
  }

  await prisma.classAssignment.create({
    data: {
      classId: parsed.data.classId,
      title: parsed.data.title,
      instructions: parsed.data.instructions || null,
      testId: parsed.data.testId || null,
      dueAt: parsed.data.dueAt ?? null,
    },
  });

  revalidatePath("/teach");
  revalidatePath("/class");
  return { ok: true };
}

export async function deleteAssignment(assignmentId: string): Promise<{ ok?: boolean; error?: string }> {
  const user = await requireUser();
  const assignment = await prisma.classAssignment.findUnique({
    where: { id: assignmentId },
    select: { id: true, class: { select: { teacherUserId: true } } },
  });
  if (!assignment || assignment.class.teacherUserId !== user.id) {
    return { error: "That assignment is not yours." };
  }
  await prisma.classAssignment.delete({ where: { id: assignmentId } });
  revalidatePath("/teach");
  revalidatePath("/class");
  return { ok: true };
}

/** Published tests for the assignment picker. */
export async function getAssignableTests(): Promise<{ id: string; title: string }[]> {
  await requireUser();
  return prisma.test.findMany({
    where: { status: "PUBLISHED" },
    orderBy: { title: "asc" },
    select: { id: true, title: true },
  });
}

/** Student side: tick off a free-form task. */
export async function markAssignmentDone(assignmentId: string): Promise<{ ok?: boolean; error?: string }> {
  const user = await requireUser();
  const assignment = await prisma.classAssignment.findUnique({
    where: { id: assignmentId },
    select: {
      id: true,
      testId: true,
      class: { select: { memberships: { where: { userId: user.id }, select: { id: true } } } },
    },
  });
  if (!assignment || assignment.class.memberships.length === 0) {
    return { error: "That task is not in one of your classes." };
  }
  if (assignment.testId) {
    return { error: "This one completes itself when you submit the linked practice test." };
  }
  await prisma.assignmentCompletion.upsert({
    where: { assignmentId_userId: { assignmentId, userId: user.id } },
    create: { assignmentId, userId: user.id },
    update: {},
  });
  revalidatePath("/class");
  revalidatePath("/teach");
  return { ok: true };
}
