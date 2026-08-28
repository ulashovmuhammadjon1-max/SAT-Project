"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

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
 * The student side of the classroom.
 *
 * The hierarchy is Classes → Class → Assignment → Submission, and every query
 * here starts from a membership check — the class an assignment belongs to is
 * decided by the assignment row, never by anything the client sends. A student
 * can only ever read or submit inside classes they are a member of.
 */

/* -------------------------------------------------------------------------- */
/* Loading                                                                    */
/* -------------------------------------------------------------------------- */

export interface StudentAssignment {
  id: string;
  classId: string;
  className: string;
  title: string;
  instructions: string | null;
  kind: AssignmentKind;
  status: SubmissionStatus;
  dueAt: Date | null;
  createdAt: Date;
  teacherName: string;
  /** Teacher-attached worksheet. */
  attachmentName: string | null;
  attachmentHref: string | null;
  /** TEST assignments. */
  testTitle: string | null;
  /** QUESTIONS assignments. */
  questionCount: number;
  questionsAnswered: number;
  practiceHref: string | null;
  /** TASK assignments: what the student has saved or handed in. */
  submittedAt: Date | null;
  note: string | null;
  files: { id: string; name: string; size: number }[];
}

/**
 * Everything about a set of classes' assignments for one student, statuses
 * included, in three bulk queries — never one query per assignment.
 */
async function loadAssignments(userId: string, classIds: string[]): Promise<StudentAssignment[]> {
  if (classIds.length === 0) return [];

  const rows = await prisma.classAssignment.findMany({
    where: { classId: { in: classIds }, class: { isArchived: false } },
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
      subject: true,
      class: { select: { name: true, teacherName: true } },
      test: { select: { title: true } },
      completions: {
        where: { userId },
        select: {
          submittedAt: true,
          note: true,
          files: { select: { id: true, name: true, size: true }, orderBy: { createdAt: "asc" } },
        },
      },
    },
  });
  if (rows.length === 0) return [];

  const testIds = rows.map((r) => r.testId).filter((t): t is string => t !== null);
  const questionIds = [...new Set(rows.flatMap((r) => r.questionIds))];
  const [attempts, answered] = await Promise.all([
    testIds.length
      ? prisma.attempt.findMany({
          where: { userId, testId: { in: testIds }, status: "SUBMITTED" },
          select: { testId: true },
        })
      : [],
    questionIds.length
      ? prisma.questionAttempt.findMany({
          where: { userId, questionId: { in: questionIds } },
          select: { questionId: true },
          distinct: ["questionId"],
        })
      : [],
  ]);
  const submittedTests = new Set(attempts.map((a) => a.testId));
  const answeredIds = new Set(answered.map((a) => a.questionId));

  return rows.map((r) => {
    const kind = assignmentKind(r);
    const completion = r.completions[0];
    const answeredHere = r.questionIds.filter((id) => answeredIds.has(id)).length;
    const status = deriveStatus({
      kind,
      dueAt: r.dueAt,
      submittedAt: completion?.submittedAt ?? null,
      hasWork: Boolean(completion),
      answered: answeredHere,
      total: r.questionIds.length,
      testSubmitted: r.testId ? submittedTests.has(r.testId) : false,
    });

    return {
      id: r.id,
      classId: r.classId,
      className: r.class.name,
      title: r.title,
      instructions: r.instructions,
      kind,
      status,
      dueAt: r.dueAt,
      createdAt: r.createdAt,
      teacherName: r.class.teacherName,
      attachmentName: r.attachmentName,
      attachmentHref: r.attachmentName ? `/api/assignments/${r.id}/attachment` : null,
      testTitle: r.test?.title ?? null,
      questionCount: r.questionIds.length,
      questionsAnswered: answeredHere,
      practiceHref:
        kind === "QUESTIONS"
          ? `/practice/session?subject=${r.subject ?? "READING_WRITING"}&size=${r.questionIds.length}` +
            `&ids=${r.questionIds.join(",")}`
          : null,
      submittedAt: completion?.submittedAt ?? null,
      note: completion?.note ?? null,
      files: completion?.files ?? [],
    };
  });
}

export interface ClassListItem {
  id: string;
  name: string;
  school: string;
  teacherName: string;
  classmates: number;
  /** Assignments not yet done — the number a student actually cares about. */
  openCount: number;
  /** The next thing due, for the overview cards. */
  nextDue: { assignmentId: string; title: string; dueAt: Date } | null;
}

/** Every class this student is in, with just enough to render the hub. */
export async function getMyClassList(): Promise<ClassListItem[]> {
  const user = await requireUser();
  const memberships = await prisma.classMembership.findMany({
    where: { userId: user.id, class: { isArchived: false } },
    orderBy: { joinedAt: "asc" },
    select: {
      class: {
        select: {
          id: true,
          name: true,
          school: true,
          teacherName: true,
          _count: { select: { memberships: true } },
        },
      },
    },
  });
  if (memberships.length === 0) return [];

  const classIds = memberships.map((m) => m.class.id);
  const assignments = await loadAssignments(user.id, classIds);

  return memberships.map((m) => {
    const mine = assignments.filter((a) => a.classId === m.class.id);
    const open = mine.filter((a) => !isDone(a.status));
    const withDue = open
      .filter((a): a is StudentAssignment & { dueAt: Date } => a.dueAt !== null)
      .sort((a, b) => a.dueAt.getTime() - b.dueAt.getTime());
    return {
      id: m.class.id,
      name: m.class.name,
      school: m.class.school,
      teacherName: m.class.teacherName,
      classmates: m.class._count.memberships,
      openCount: open.length,
      nextDue: withDue[0]
        ? { assignmentId: withDue[0].id, title: withDue[0].title, dueAt: withDue[0].dueAt }
        : null,
    };
  });
}

export interface ClassesOverview {
  classes: ClassListItem[];
  /** Open work across every class, soonest due first — the hub's to-do list. */
  upcoming: StudentAssignment[];
}

/** The /classes hub: one load feeds both the class cards and the to-do list. */
export async function getClassesOverview(): Promise<ClassesOverview> {
  const user = await requireUser();
  const memberships = await prisma.classMembership.findMany({
    where: { userId: user.id, class: { isArchived: false } },
    orderBy: { joinedAt: "asc" },
    select: {
      class: {
        select: {
          id: true,
          name: true,
          school: true,
          teacherName: true,
          _count: { select: { memberships: true } },
        },
      },
    },
  });
  if (memberships.length === 0) return { classes: [], upcoming: [] };

  const assignments = await loadAssignments(
    user.id,
    memberships.map((m) => m.class.id),
  );
  const open = assignments.filter((a) => !isDone(a.status));

  const classes = memberships.map((m) => {
    const mine = open.filter((a) => a.classId === m.class.id);
    const withDue = mine
      .filter((a): a is StudentAssignment & { dueAt: Date } => a.dueAt !== null)
      .sort((a, b) => a.dueAt.getTime() - b.dueAt.getTime());
    return {
      id: m.class.id,
      name: m.class.name,
      school: m.class.school,
      teacherName: m.class.teacherName,
      classmates: m.class._count.memberships,
      openCount: mine.length,
      nextDue: withDue[0]
        ? { assignmentId: withDue[0].id, title: withDue[0].title, dueAt: withDue[0].dueAt }
        : null,
    };
  });

  const upcoming = [...open]
    .sort((a, b) => {
      // Soonest due first; no due date sinks below everything dated.
      if (a.dueAt && b.dueAt) return a.dueAt.getTime() - b.dueAt.getTime();
      if (a.dueAt) return -1;
      if (b.dueAt) return 1;
      return b.createdAt.getTime() - a.createdAt.getTime();
    })
    .slice(0, 8);

  return { classes, upcoming };
}

export interface ClassHome {
  id: string;
  name: string;
  school: string;
  teacherName: string;
  classmates: number;
  assignments: StudentAssignment[];
}

/** One class, membership-checked, with every assignment and my status. */
export async function getClassHome(classId: string): Promise<ClassHome | null> {
  const user = await requireUser();
  const membership = await prisma.classMembership.findUnique({
    where: { classId_userId: { classId, userId: user.id } },
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
  if (!membership || membership.class.isArchived) return null;

  const assignments = await loadAssignments(user.id, [classId]);
  return {
    id: membership.class.id,
    name: membership.class.name,
    school: membership.class.school,
    teacherName: membership.class.teacherName,
    classmates: membership.class._count.memberships,
    assignments,
  };
}

/**
 * One assignment, for the workspace page. Membership is checked through the
 * assignment's own class — the URL's classId is only trusted after this
 * lookup agrees with it.
 */
export async function getAssignmentWorkspace(assignmentId: string): Promise<StudentAssignment | null> {
  const user = await requireUser();
  const assignment = await prisma.classAssignment.findFirst({
    where: {
      id: assignmentId,
      class: { isArchived: false, memberships: { some: { userId: user.id } } },
    },
    select: { classId: true },
  });
  if (!assignment) return null;

  const all = await loadAssignments(user.id, [assignment.classId]);
  return all.find((a) => a.id === assignmentId) ?? null;
}

/* -------------------------------------------------------------------------- */
/* Saving and submitting                                                      */
/* -------------------------------------------------------------------------- */

const MAX_FILES = 5;
const MAX_FILE_BYTES = 10 * 1024 * 1024;

/**
 * Files arrive as Blob URLs, not payloads: the browser uploads straight to
 * Blob storage (the /api/assignments/upload token route enforces type and
 * the 10MB cap there), and only the URL reaches this action. The host check
 * stops anything that is not our blob store from being stored as a "file".
 */
const BLOB_URL = /^https:\/\/[a-zA-Z0-9-]+\.public\.blob\.vercel-storage\.com\//;

const saveSchema = z.object({
  assignmentId: z.string().min(1),
  note: z.string().trim().max(2000).optional().or(z.literal("")),
  /** Ids of already-uploaded files to keep; anything else is removed. */
  keepFileIds: z.array(z.string().min(1)).max(MAX_FILES).default([]),
  newFiles: z
    .array(
      z.object({
        name: z.string().trim().min(1).max(200),
        url: z.string().regex(BLOB_URL, "Upload files through the upload box.").max(1000),
        size: z.coerce.number().int().min(0).max(MAX_FILE_BYTES).default(0),
      }),
    )
    .max(MAX_FILES)
    .default([]),
  /** false = save a draft; true = hand it in. */
  submit: z.boolean(),
});

export interface SaveWorkResult {
  ok?: boolean;
  error?: string;
  status?: SubmissionStatus;
}

/**
 * Save or submit work on a free-form task.
 *
 * TEST and QUESTIONS assignments refuse this on purpose: they complete from
 * real answers, and a hand-in button on them would let the teacher's status
 * column be faked. Draft first, submit when ready; files persist across
 * visits either way.
 */
export async function saveWork(input: {
  assignmentId: string;
  note?: string;
  keepFileIds?: string[];
  newFiles?: { name: string; url: string; size: number }[];
  submit: boolean;
}): Promise<SaveWorkResult> {
  const user = await requireUser();

  const parsed = saveSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check what you are submitting." };
  }
  const d = parsed.data;

  const assignment = await prisma.classAssignment.findFirst({
    where: {
      id: d.assignmentId,
      class: { isArchived: false, memberships: { some: { userId: user.id } } },
    },
    select: { id: true, classId: true, testId: true, questionIds: true, dueAt: true },
  });
  if (!assignment) return { error: "That assignment is not in one of your classes." };
  if (assignmentKind(assignment) !== "TASK") {
    return { error: "This assignment completes itself from your answers — nothing to upload." };
  }

  const existing = await prisma.assignmentCompletion.findUnique({
    where: { assignmentId_userId: { assignmentId: d.assignmentId, userId: user.id } },
    select: { id: true, files: { select: { id: true } } },
  });

  const keptCount = existing
    ? existing.files.filter((f) => d.keepFileIds.includes(f.id)).length
    : 0;
  if (keptCount + d.newFiles.length > MAX_FILES) {
    return { error: `At most ${MAX_FILES} files per submission.` };
  }

  const submittedAt = d.submit ? new Date() : null;
  const completion = existing
    ? await prisma.assignmentCompletion.update({
        where: { id: existing.id },
        data: { note: d.note || null, submittedAt },
        select: { id: true },
      })
    : await prisma.assignmentCompletion.create({
        data: {
          assignmentId: d.assignmentId,
          userId: user.id,
          note: d.note || null,
          submittedAt,
        },
        select: { id: true },
      });

  // Files not kept are removed; new ones appended. The keep-list only ever
  // matters for files this student's own completion holds.
  if (existing) {
    const drop = existing.files.map((f) => f.id).filter((id) => !d.keepFileIds.includes(id));
    if (drop.length) await prisma.submissionFile.deleteMany({ where: { id: { in: drop } } });
  }
  for (const f of d.newFiles) {
    await prisma.submissionFile.create({
      data: { completionId: completion.id, name: f.name, data: f.url, size: f.size },
    });
  }

  revalidatePath(`/classes/${assignment.classId}`);
  revalidatePath("/classes");
  revalidatePath("/teach");
  return {
    ok: true,
    status: deriveStatus({
      kind: "TASK",
      dueAt: assignment.dueAt,
      submittedAt,
      hasWork: true,
      answered: 0,
      total: 0,
      testSubmitted: false,
    }),
  };
}

/** Pull a submission back to a draft so it can be edited and resubmitted. */
export async function unsubmitWork(assignmentId: string): Promise<SaveWorkResult> {
  const user = await requireUser();
  const completion = await prisma.assignmentCompletion.findFirst({
    where: {
      assignmentId,
      userId: user.id,
      assignment: { class: { memberships: { some: { userId: user.id } } } },
    },
    select: { id: true, assignment: { select: { classId: true } } },
  });
  if (!completion) return { error: "Nothing submitted here yet." };

  await prisma.assignmentCompletion.update({
    where: { id: completion.id },
    data: { submittedAt: null },
  });
  revalidatePath(`/classes/${completion.assignment.classId}`);
  return { ok: true, status: "DRAFT" };
}
