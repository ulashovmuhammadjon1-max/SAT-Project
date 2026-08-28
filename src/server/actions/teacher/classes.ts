"use server";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * The teacher panel's data layer.
 *
 * A teacher is linked to a class two ways:
 *  - `teacherUserId`, set the moment an admin creates the class if an account
 *    with the teacher's email already exists;
 *  - lazily here: any class whose `teacherEmail` matches the signed-in user's
 *    email and has no linked teacher yet is claimed on first visit. This is
 *    what makes "add the email first, the teacher registers later" work with
 *    no extra step for anyone.
 */

async function claimClassesByEmail(userId: string, email: string) {
  await prisma.schoolClass.updateMany({
    where: {
      teacherUserId: null,
      teacherEmail: { equals: email, mode: "insensitive" },
    },
    data: { teacherUserId: userId },
  });
}

export interface TeachingStudent {
  id: string;
  name: string | null;
  email: string;
  joinedAt: Date;
  testsCompleted: number;
  questionsAnswered: number;
  bestScore: number | null;
}

export interface TeachingClass {
  id: string;
  code: string;
  name: string;
  school: string;
  students: TeachingStudent[];
}

export async function getMyTeachingClasses(): Promise<TeachingClass[]> {
  const user = await requireUser();
  if (user.email) await claimClassesByEmail(user.id, user.email);

  const classes = await prisma.schoolClass.findMany({
    where: { teacherUserId: user.id, isArchived: false },
    orderBy: { createdAt: "desc" },
    select: {
      id: true,
      code: true,
      name: true,
      school: true,
      memberships: {
        orderBy: { joinedAt: "asc" },
        select: {
          joinedAt: true,
          user: {
            select: {
              id: true,
              name: true,
              email: true,
              studyActivities: { select: { questionsAnswered: true } },
              attempts: { where: { status: "SUBMITTED" }, select: { totalScaledScore: true } },
            },
          },
        },
      },
    },
  });

  return classes.map((c) => ({
    id: c.id,
    code: c.code,
    name: c.name,
    school: c.school,
    students: c.memberships.map((m) => ({
      id: m.user.id,
      name: m.user.name,
      email: m.user.email,
      joinedAt: m.joinedAt,
      testsCompleted: m.user.attempts.length,
      questionsAnswered: m.user.studyActivities.reduce((s, a) => s + a.questionsAnswered, 0),
      bestScore: m.user.attempts.reduce<number | null>(
        (best, a) => (a.totalScaledScore == null ? best : Math.max(best ?? 0, a.totalScaledScore)),
        null,
      ),
    })),
  }));
}

/** Cheap teacher check for the sidebar — one indexed count, no rosters. */
export async function isTeacher(userId: string, email: string | null): Promise<boolean> {
  const count = await prisma.schoolClass.count({
    where: {
      isArchived: false,
      OR: [
        { teacherUserId: userId },
        ...(email ? [{ teacherUserId: null, teacherEmail: { equals: email, mode: "insensitive" as const } }] : []),
      ],
    },
  });
  return count > 0;
}
