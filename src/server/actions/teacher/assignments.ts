"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { layout, para, sendEmail } from "@/lib/email";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * Teacher-set assignments.
 *
 * Three kinds, decided by what the teacher attaches:
 *  - test assignments: completion is DERIVED from a submitted attempt of that
 *    test, so it cannot be faked by ticking a box and the teacher sees the
 *    actual score next to the name;
 *  - question-set assignments: a hand-picked set of Question Bank questions,
 *    completion derived from having answered all of them;
 *  - free-form tasks ("read this PDF", "bring your essay"): students mark them
 *    done themselves, optionally uploading the work as proof.
 *
 * Any of the three can carry an uploaded file and a due date.
 */

/**
 * Attachments arrive as Blob URLs — the browser uploads directly to Blob
 * storage (type and the 10MB cap are enforced by the token route), and only
 * the URL reaches this action. The host check keeps anything that is not our
 * blob store from being stored as an "attachment".
 */
const BLOB_URL = /^https:\/\/[a-zA-Z0-9.-]+\.blob\.vercel-storage\.com\//;

const fileSchema = z
  .object({
    name: z.string().trim().min(1).max(200),
    url: z.string().regex(BLOB_URL, "Upload the file through the attach box.").max(1000),
  })
  .nullable()
  .optional();

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
  attachment: fileSchema,
  questionIds: z.array(z.string().min(1)).max(50).default([]),
  subject: z.enum(["MATH", "READING_WRITING"]).optional().nullable(),
});

/**
 * Tell the class a task exists.
 *
 * Best-effort and deliberately non-fatal: the assignment is already saved by
 * the time this runs, and a mail provider having a bad minute must not turn a
 * successful post into an error the teacher has to puzzle over. Sends are
 * sequential — a class is tens of students, not thousands, and Resend's free
 * tier rate-limits bursts.
 */
async function notifyClass(assignmentId: string) {
  const assignment = await prisma.classAssignment.findUnique({
    where: { id: assignmentId },
    select: {
      title: true,
      instructions: true,
      dueAt: true,
      attachmentName: true,
      questionIds: true,
      testId: true,
      test: { select: { title: true } },
      class: {
        select: {
          name: true,
          school: true,
          teacherName: true,
          memberships: { select: { user: { select: { name: true, email: true } } } },
        },
      },
    },
  });
  if (!assignment) return;

  const due = assignment.dueAt
    ? assignment.dueAt.toLocaleDateString("en-GB", { day: "numeric", month: "long" })
    : null;

  const what = assignment.testId
    ? `Practice test: ${assignment.test?.title ?? "assigned test"}`
    : assignment.questionIds.length > 0
      ? `${assignment.questionIds.length} Question Bank questions`
      : assignment.attachmentName
        ? `Attached file: ${assignment.attachmentName}`
        : null;

  const url = "https://scholarly.space/classes";

  for (const m of assignment.class.memberships) {
    const email = m.user.email;
    if (!email) continue;
    const firstName = m.user.name?.trim().split(/\s+/)[0] ?? "there";
    await sendEmail({
      to: email,
      subject: `New assignment in ${assignment.class.name}: ${assignment.title}`,
      text:
        `Hi ${firstName},\n\n` +
        `${assignment.class.teacherName} posted a new assignment in ${assignment.class.name}.\n\n` +
        `${assignment.title}\n` +
        (what ? `${what}\n` : "") +
        (due ? `Due ${due}\n` : "") +
        (assignment.instructions ? `\n${assignment.instructions}\n` : "") +
        `\nOpen it here: ${url}\n`,
      html: layout(
        para(`Hi ${firstName},`) +
          para(
            `<strong>${assignment.class.teacherName}</strong> posted a new assignment in ` +
              `${assignment.class.name} — ${assignment.class.school}.`,
          ) +
          para(`<strong>${assignment.title}</strong>`) +
          (what ? para(what) : "") +
          (due ? para(`Due ${due}`) : "") +
          (assignment.instructions ? para(assignment.instructions) : "") +
          `<p style="margin:24px 0;"><a href="${url}" style="display:inline-block;background:#2549ea;color:#ffffff;text-decoration:none;padding:12px 22px;border-radius:10px;font-weight:600;font-size:15px;">Open the assignment</a></p>`,
      ),
    });
  }
}

export async function createAssignment(input: {
  classId: string;
  title: unknown;
  instructions?: unknown;
  testId?: unknown;
  dueAt?: string | null;
  attachment?: { name: string; url: string } | null;
  questionIds?: string[];
  subject?: string | null;
}): Promise<{ ok?: boolean; error?: string; notified?: number }> {
  const parsed = createSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Check the assignment details." };
  }
  try {
    await requireOwnClass(parsed.data.classId);
  } catch {
    return { error: "That class is not linked to your account." };
  }

  const d = parsed.data;
  if (d.testId && d.questionIds.length > 0) {
    return { error: "Assign either a whole practice test or a set of questions, not both." };
  }
  if (d.testId) {
    const test = await prisma.test.findFirst({
      where: { id: d.testId, status: "PUBLISHED" },
      select: { id: true },
    });
    if (!test) return { error: "That practice test does not exist or is not published." };
  }

  // Ids come from the teacher's own preview, but they arrive over the wire —
  // confirm every one is a real published question before it becomes homework
  // a student cannot open.
  let questionIds: string[] = [];
  let subject = d.subject ?? null;
  if (d.questionIds.length > 0) {
    const found = await prisma.question.findMany({
      where: { id: { in: d.questionIds }, isPublished: true },
      select: { id: true, domain: { select: { subject: true } } },
    });
    if (found.length === 0) {
      return { error: "Those questions are no longer available. Preview a new set." };
    }
    const valid = new Set(found.map((q) => q.id));
    questionIds = d.questionIds.filter((id) => valid.has(id));
    subject = found[0].domain.subject;
  }

  if (d.dueAt && d.dueAt.getTime() < Date.now()) {
    return { error: "The due date is already in the past." };
  }

  const created = await prisma.classAssignment.create({
    data: {
      classId: d.classId,
      title: d.title,
      instructions: d.instructions || null,
      testId: d.testId || null,
      dueAt: d.dueAt ?? null,
      attachmentName: d.attachment?.name ?? null,
      attachmentData: d.attachment?.url ?? null,
      questionIds,
      subject,
    },
    select: { id: true, class: { select: { _count: { select: { memberships: true } } } } },
  });

  await notifyClass(created.id);

  revalidatePath("/teach");
  revalidatePath("/classes");
  return { ok: true, notified: created.class._count.memberships };
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
  revalidatePath("/classes");
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

// The student side of submissions lives in
// src/server/actions/student/classroom.ts — drafts, multi-file uploads,
// submit and unsubmit are all there, behind the same membership checks.
