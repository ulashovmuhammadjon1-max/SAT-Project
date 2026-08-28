"use server";

import {
  assignmentKind,
  deriveStatus,
  isDone,
  type AssignmentKind,
  type SubmissionStatus,
} from "@/lib/classroom/status";
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

// ---------------------------------------------------------------------------
// Class analytics + per-student drill-down
// ---------------------------------------------------------------------------

import { Prisma } from "@prisma/client";

export interface DomainAccuracy {
  domain: string;
  total: number;
  correct: number;
}

/** Accuracy by domain over practice attempts for a set of students. */
async function domainAccuracy(userIds: string[]): Promise<DomainAccuracy[]> {
  if (userIds.length === 0) return [];
  const rows = await prisma.$queryRaw<{ domain: string; total: bigint; correct: bigint }[]>`
    SELECT d.name AS domain,
           COUNT(*)::bigint AS total,
           SUM(CASE WHEN qa."isCorrect" THEN 1 ELSE 0 END)::bigint AS correct
      FROM "QuestionAttempt" qa
      JOIN "Question" q ON q.id = qa."questionId"
      JOIN "Domain" d ON d.id = q."domainId"
     WHERE qa."userId" IN (${Prisma.join(userIds)})
     GROUP BY d.name
     ORDER BY d.name
  `;
  return rows.map((r) => ({ domain: r.domain, total: Number(r.total), correct: Number(r.correct) }));
}

/** The skills costing the most, by miss count. Needs a few attempts to mean anything. */
async function weakestSkills(userIds: string[], limit = 5) {
  if (userIds.length === 0) return [];
  const rows = await prisma.$queryRaw<{ skill: string; total: bigint; correct: bigint }[]>`
    SELECT s.name AS skill,
           COUNT(*)::bigint AS total,
           SUM(CASE WHEN qa."isCorrect" THEN 1 ELSE 0 END)::bigint AS correct
      FROM "QuestionAttempt" qa
      JOIN "Question" q ON q.id = qa."questionId"
      JOIN "Skill" s ON s.id = q."skillId"
     WHERE qa."userId" IN (${Prisma.join(userIds)})
     GROUP BY s.name
    HAVING COUNT(*) >= 4
     ORDER BY (COUNT(*) - SUM(CASE WHEN qa."isCorrect" THEN 1 ELSE 0 END)) DESC
     LIMIT ${limit}
  `;
  return rows.map((r) => ({ skill: r.skill, total: Number(r.total), correct: Number(r.correct) }));
}

export interface AssignmentStudentStatus {
  userId: string;
  status: SubmissionStatus;
  done: boolean;
  /** Scaled score for a test assignment; percent correct for a question set. */
  score: number | null;
  /** Question sets: how many of the assigned questions this student answered. */
  answered: number;
  /** When a free-form task was handed in. */
  submittedAt: Date | null;
  /** What the student handed in on a free-form task. */
  note: string | null;
  files: { id: string; name: string; size: number }[];
}

export interface AssignmentStatus {
  id: string;
  classId: string;
  title: string;
  instructions: string | null;
  kind: AssignmentKind;
  testId: string | null;
  testTitle: string | null;
  dueAt: Date | null;
  createdAt: Date;
  attachmentName: string | null;
  /** Where the teacher re-downloads their own upload. */
  attachmentHref: string | null;
  questionCount: number;
  perStudent: AssignmentStudentStatus[];
}

async function assignmentStatuses(classId: string, memberIds: string[]): Promise<AssignmentStatus[]> {
  const assignments = await prisma.classAssignment.findMany({
    where: { classId },
    orderBy: { createdAt: "desc" },
    select: {
      id: true,
      classId: true,
      title: true,
      instructions: true,
      testId: true,
      dueAt: true,
      createdAt: true,
      attachmentName: true,
      questionIds: true,
      test: { select: { title: true } },
      completions: {
        select: {
          userId: true,
          note: true,
          submittedAt: true,
          files: { select: { id: true, name: true, size: true }, orderBy: { createdAt: "asc" } },
        },
      },
    },
  });
  if (assignments.length === 0) return [];

  // One query for every test-linked assignment's submitted attempts.
  const testIds = assignments.map((a) => a.testId).filter((t): t is string => t !== null);
  const attempts = testIds.length
    ? await prisma.attempt.findMany({
        where: { testId: { in: testIds }, userId: { in: memberIds }, status: "SUBMITTED" },
        select: { testId: true, userId: true, totalScaledScore: true },
      })
    : [];

  // And one for every question-set assignment: who answered which of the
  // assigned questions, and whether they got it right.
  const allQuestionIds = [...new Set(assignments.flatMap((a) => a.questionIds))];
  const qAttempts =
    allQuestionIds.length && memberIds.length
      ? await prisma.questionAttempt.findMany({
          where: { userId: { in: memberIds }, questionId: { in: allQuestionIds } },
          select: { userId: true, questionId: true, isCorrect: true },
          orderBy: { createdAt: "asc" },
        })
      : [];
  // Latest answer per (student, question) wins — the ascending order above
  // means a later attempt overwrites an earlier one.
  const latest = new Map<string, boolean>();
  for (const a of qAttempts) latest.set(`${a.userId}:${a.questionId}`, a.isCorrect);

  return assignments.map((a) => {
    const kind = assignmentKind(a);
    return {
      id: a.id,
      classId: a.classId,
      title: a.title,
      instructions: a.instructions,
      kind,
      testId: a.testId,
      testTitle: a.test?.title ?? null,
      dueAt: a.dueAt,
      createdAt: a.createdAt,
      attachmentName: a.attachmentName,
      attachmentHref: a.attachmentName ? `/api/assignments/${a.id}/attachment` : null,
      questionCount: a.questionIds.length,
      perStudent: memberIds.map((userId) => {
        const completion = a.completions.find((c) => c.userId === userId);
        const answered = a.questionIds.filter((q) => latest.has(`${userId}:${q}`)).length;
        const testDone = attempts.filter((t) => t.testId === a.testId && t.userId === userId);

        const status = deriveStatus({
          kind,
          dueAt: a.dueAt,
          submittedAt: completion?.submittedAt ?? null,
          hasWork: Boolean(completion),
          answered,
          total: a.questionIds.length,
          testSubmitted: a.testId ? testDone.length > 0 : false,
        });

        let score: number | null = null;
        if (kind === "TEST") {
          score = testDone.reduce<number | null>(
            (b, t) => (t.totalScaledScore == null ? b : Math.max(b ?? 0, t.totalScaledScore)),
            null,
          );
        } else if (kind === "QUESTIONS" && answered > 0) {
          const correct = a.questionIds.filter((q) => latest.get(`${userId}:${q}`)).length;
          score = Math.round((correct / answered) * 100);
        }

        return {
          userId,
          status,
          done: isDone(status),
          score,
          answered,
          submittedAt: completion?.submittedAt ?? null,
          note: completion?.note ?? null,
          files: completion?.files ?? [],
        };
      }),
    };
  });
}

export interface AssignmentTracking {
  assignment: Omit<AssignmentStatus, "perStudent">;
  className: string;
  students: (AssignmentStudentStatus & { name: string | null; email: string })[];
}

/** One assignment's full submission picture, for the teacher's detail page. */
export async function getAssignmentTracking(assignmentId: string): Promise<AssignmentTracking | null> {
  const user = await requireUser();
  const assignment = await prisma.classAssignment.findFirst({
    where: { id: assignmentId, class: { teacherUserId: user.id } },
    select: {
      classId: true,
      class: {
        select: {
          name: true,
          memberships: {
            orderBy: { joinedAt: "asc" },
            select: { user: { select: { id: true, name: true, email: true } } },
          },
        },
      },
    },
  });
  if (!assignment) return null;

  const members = assignment.class.memberships.map((m) => m.user);
  const statuses = await assignmentStatuses(assignment.classId, members.map((m) => m.id));
  const target = statuses.find((s) => s.id === assignmentId);
  if (!target) return null;

  const { perStudent, ...meta } = target;
  const byId = new Map(perStudent.map((p) => [p.userId, p]));
  return {
    assignment: meta,
    className: assignment.class.name,
    students: members.map((m) => ({
      ...(byId.get(m.id) as AssignmentStudentStatus),
      name: m.name,
      email: m.email,
    })),
  };
}

export interface ClassAnalytics {
  domainAccuracy: DomainAccuracy[];
  weakestSkills: { skill: string; total: number; correct: number }[];
  activeLast7: number;
  /** Students with no practice in the last 7 days — the teacher's call list. */
  inactive: { id: string; name: string | null; lastActive: Date | null }[];
  assignments: AssignmentStatus[];
}

export async function getClassAnalytics(classId: string): Promise<ClassAnalytics | null> {
  const user = await requireUser();
  const cls = await prisma.schoolClass.findUnique({
    where: { id: classId },
    select: {
      teacherUserId: true,
      memberships: { select: { user: { select: { id: true, name: true } } } },
    },
  });
  if (!cls || cls.teacherUserId !== user.id) return null;

  const members = cls.memberships.map((m) => m.user);
  const memberIds = members.map((m) => m.id);
  const weekAgo = new Date(Date.now() - 7 * 86_400_000);

  const [domains, skills, recent, assignments] = await Promise.all([
    domainAccuracy(memberIds),
    weakestSkills(memberIds),
    memberIds.length
      ? prisma.studyActivity.groupBy({
          by: ["userId"],
          where: { userId: { in: memberIds }, questionsAnswered: { gt: 0 } },
          _max: { date: true },
        })
      : Promise.resolve([]),
    assignmentStatuses(classId, memberIds),
  ]);

  const lastActiveBy = new Map(recent.map((r) => [r.userId, r._max.date]));
  const inactive = members
    .map((m) => ({ id: m.id, name: m.name, lastActive: lastActiveBy.get(m.id) ?? null }))
    .filter((m) => !m.lastActive || m.lastActive < weekAgo);

  return {
    domainAccuracy: domains,
    weakestSkills: skills,
    activeLast7: memberIds.length - inactive.length,
    inactive,
    assignments,
  };
}

export interface StudentDetail {
  id: string;
  name: string | null;
  email: string;
  createdAt: Date;
  currentStreak: number;
  targetScore: number | null;
  satDate: Date | null;
  questionsAnswered: number;
  lastActive: Date | null;
  attempts: { testTitle: string; score: number | null; submittedAt: Date | null }[];
  domainAccuracy: DomainAccuracy[];
  weakestSkills: { skill: string; total: number; correct: number }[];
  /** Questions answered per ISO week, most recent first (4 weeks). */
  weekly: { weekStart: Date; answered: number }[];
}

/** Full drill-down. Only for students who share a class with this teacher. */
export async function getStudentDetail(studentId: string): Promise<StudentDetail | null> {
  const user = await requireUser();

  const shared = await prisma.classMembership.findFirst({
    where: { userId: studentId, class: { teacherUserId: user.id, isArchived: false } },
    select: { id: true },
  });
  if (!shared) return null;

  const [student, attempts, domains, skills, weeklyRows] = await Promise.all([
    prisma.user.findUnique({
      where: { id: studentId },
      select: {
        id: true,
        name: true,
        email: true,
        createdAt: true,
        currentStreak: true,
        targetScore: true,
        satDate: true,
        studyActivities: { select: { questionsAnswered: true, date: true } },
      },
    }),
    prisma.attempt.findMany({
      where: { userId: studentId, status: "SUBMITTED" },
      orderBy: { submittedAt: "desc" },
      take: 20,
      select: { totalScaledScore: true, submittedAt: true, test: { select: { title: true } } },
    }),
    domainAccuracy([studentId]),
    weakestSkills([studentId]),
    prisma.$queryRaw<{ week: Date; answered: bigint }[]>`
      SELECT date_trunc('week', "date") AS week, SUM("questionsAnswered")::bigint AS answered
        FROM "StudyActivity"
       WHERE "userId" = ${studentId} AND "date" >= now() - interval '4 weeks'
       GROUP BY 1 ORDER BY 1 DESC
    `,
  ]);
  if (!student) return null;

  const activeDates = student.studyActivities.filter((a) => a.questionsAnswered > 0).map((a) => a.date);
  return {
    id: student.id,
    name: student.name,
    email: student.email,
    createdAt: student.createdAt,
    currentStreak: student.currentStreak,
    targetScore: student.targetScore,
    satDate: student.satDate,
    questionsAnswered: student.studyActivities.reduce((s, a) => s + a.questionsAnswered, 0),
    lastActive: activeDates.length ? new Date(Math.max(...activeDates.map((d) => d.getTime()))) : null,
    attempts: attempts.map((a) => ({
      testTitle: a.test.title,
      score: a.totalScaledScore,
      submittedAt: a.submittedAt,
    })),
    domainAccuracy: domains,
    weakestSkills: skills,
    weekly: weeklyRows.map((w) => ({ weekStart: w.week, answered: Number(w.answered) })),
  };
}
