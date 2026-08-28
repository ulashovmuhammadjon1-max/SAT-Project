"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * Joining a class. A code is something a teacher writes on a whiteboard, so
 * matching is forgiving: case-insensitive, spaces and dashes ignored.
 */

const codeSchema = z.string().trim().min(4).max(24);

function normalize(code: string): string {
  return code.toUpperCase().replace(/[\s-]/g, "");
}

export async function joinClass(rawCode: unknown): Promise<{ ok?: boolean; error?: string; className?: string }> {
  const user = await requireUser();

  const parsed = codeSchema.safeParse(rawCode);
  if (!parsed.success) return { error: "Enter the class code your teacher gave you." };
  const code = normalize(parsed.data);

  const cls = await prisma.schoolClass.findFirst({
    where: { code, isArchived: false },
    select: { id: true, name: true, school: true },
  });
  if (!cls) return { error: "No class with that code. Check it with your teacher." };

  // Idempotent: joining a class you are already in is a no-op, not an error.
  await prisma.classMembership.upsert({
    where: { classId_userId: { classId: cls.id, userId: user.id } },
    create: { classId: cls.id, userId: user.id },
    update: {},
  });

  revalidatePath("/class");
  return { ok: true, className: `${cls.name} — ${cls.school}` };
}

export async function leaveClass(classId: string): Promise<{ ok?: boolean; error?: string }> {
  const user = await requireUser();
  await prisma.classMembership.deleteMany({ where: { classId, userId: user.id } });
  revalidatePath("/class");
  return { ok: true };
}

export interface MyClass {
  id: string;
  name: string;
  school: string;
  teacherName: string;
  classmates: number;
}

export async function getMyClasses(): Promise<MyClass[]> {
  const user = await requireUser();
  const memberships = await prisma.classMembership.findMany({
    where: { userId: user.id },
    orderBy: { joinedAt: "desc" },
    select: {
      class: {
        select: {
          id: true,
          name: true,
          school: true,
          teacherName: true,
          isArchived: true,
          _count: { select: { memberships: true } },
        },
      },
    },
  });
  return memberships
    .filter((m) => !m.class.isArchived)
    .map((m) => ({
      id: m.class.id,
      name: m.class.name,
      school: m.class.school,
      teacherName: m.class.teacherName,
      classmates: m.class._count.memberships,
    }));
}

export interface MyAssignment {
  id: string;
  className: string;
  title: string;
  instructions: string | null;
  testId: string | null;
  testTitle: string | null;
  dueAt: Date | null;
  done: boolean;
}

/** Every assignment across the student's classes, with their own status. */
export async function getMyAssignments(): Promise<MyAssignment[]> {
  const user = await requireUser();
  const rows = await prisma.classAssignment.findMany({
    where: { class: { isArchived: false, memberships: { some: { userId: user.id } } } },
    orderBy: { createdAt: "desc" },
    include: {
      class: { select: { name: true } },
      test: { select: { title: true } },
      completions: { where: { userId: user.id }, select: { id: true } },
    },
  });
  if (rows.length === 0) return [];

  const testIds = rows.map((r) => r.testId).filter((t): t is string => t !== null);
  const submitted = testIds.length
    ? await prisma.attempt.findMany({
        where: { userId: user.id, testId: { in: testIds }, status: "SUBMITTED" },
        select: { testId: true },
      })
    : [];
  const submittedTests = new Set(submitted.map((a) => a.testId));

  return rows.map((r) => ({
    id: r.id,
    className: r.class.name,
    title: r.title,
    instructions: r.instructions,
    testId: r.testId,
    testTitle: r.test?.title ?? null,
    dueAt: r.dueAt,
    done: r.testId ? submittedTests.has(r.testId) : r.completions.length > 0,
  }));
}
