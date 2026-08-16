"use server";

import { revalidatePath } from "next/cache";
import type { ExamKind, ExamMode } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { resolveMode } from "@/lib/exam/mode";

export interface ExamModeResult {
  ok?: boolean;
  error?: string;
  /** Where the client should navigate after the switch. */
  redirectTo?: string;
}

const HOME: Record<ExamMode, string> = {
  SAT: "/dashboard",
  IELTS: "/ielts",
  BOTH: "/dashboard",
};

/**
 * Switch which exam the dashboard is showing, enrolling if needed.
 *
 * Both exams are open to every account, so this never refuses: choosing IELTS
 * from a SAT-only account adds IELTS and lands the student in it. That is the
 * whole onboarding story for an existing user — one click, no questions. A
 * target band and a test date sharpen the plan later but are never required to
 * start.
 */
export async function setActiveExam(mode: ExamMode): Promise<ExamModeResult> {
  const user = await requireUser();
  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { preparationExams: true },
  });
  if (!row) return { error: "Account not found." };

  // Both exams are open to every account, so picking one from the switcher
  // enrols the student on the spot. There is no gate and no questionnaire:
  // an existing SAT student who wants to look at IELTS clicks IELTS and is
  // there. Goals can be filled in later from the plan page, or never.
  const wanted: ExamKind[] =
    mode === "SAT" ? ["SAT"] : mode === "IELTS" ? ["IELTS"] : ["SAT", "IELTS"];
  const missing = wanted.filter((e) => !row.preparationExams.includes(e));
  const preparing = [...row.preparationExams, ...missing];

  await prisma.$transaction(async (tx) => {
    await tx.user.update({
      where: { id: user.id },
      data: { activeExam: mode, preparationExams: preparing },
    });
    if (missing.includes("IELTS")) {
      // An empty profile row, so the dashboard has somewhere to write a
      // target band the first time the student sets one.
      await tx.ieltsStudentProfile.upsert({
        where: { userId: user.id },
        create: { userId: user.id },
        update: {},
      });
    }
  });

  // The sidebar, hero and plan all change, so the whole student area is stale.
  revalidatePath("/", "layout");
  return { ok: true, redirectTo: HOME[mode] };
}

/**
 * Start preparing for an exam that was not on the account before.
 *
 * Adding an exam never removes the other one and never touches its data —
 * "Add IELTS" from a SAT account must leave every SAT attempt, plan and
 * vocabulary streak exactly as it was.
 */
export async function addExam(exam: ExamKind): Promise<ExamModeResult> {
  const user = await requireUser();
  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { preparationExams: true, activeExam: true },
  });
  if (!row) return { error: "Account not found." };

  if (row.preparationExams.includes(exam)) {
    return { ok: true, redirectTo: exam === "IELTS" ? "/ielts" : "/dashboard" };
  }

  const preparing = [...row.preparationExams, exam];
  await prisma.$transaction(async (tx) => {
    await tx.user.update({
      where: { id: user.id },
      // Land the student in the exam they just added — they clicked "Add
      // IELTS" because they want to set it up now, not to keep looking at
      // the SAT dashboard.
      data: { preparationExams: preparing, activeExam: exam },
    });
    if (exam === "IELTS") {
      await tx.ieltsStudentProfile.upsert({
        where: { userId: user.id },
        create: { userId: user.id },
        update: {},
      });
    }
  });

  revalidatePath("/", "layout");
  return { ok: true, redirectTo: exam === "IELTS" ? "/ielts" : "/dashboard" };
}

/**
 * Stop preparing for an exam.
 *
 * The exam is removed from the list; none of its data is deleted. A student
 * who removes IELTS and adds it back a month later finds their bands, their
 * submissions and their reviewer feedback where they left them. Removing the
 * last remaining exam is refused — an account with no exam has no dashboard.
 */
export async function removeExam(exam: ExamKind): Promise<ExamModeResult> {
  const user = await requireUser();
  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { preparationExams: true, activeExam: true },
  });
  if (!row) return { error: "Account not found." };

  const preparing = row.preparationExams.filter((e) => e !== exam);
  if (!preparing.length) return { error: "Keep at least one exam on your account." };

  const active = resolveMode(preparing, row.activeExam);
  await prisma.user.update({
    where: { id: user.id },
    data: { preparationExams: preparing, activeExam: active },
  });

  revalidatePath("/", "layout");
  return { ok: true, redirectTo: HOME[active] };
}
