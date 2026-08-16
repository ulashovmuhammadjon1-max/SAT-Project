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
 * Switch which exam the dashboard is showing.
 *
 * Refuses a mode the student is not preparing for. The switcher only offers
 * legitimate options, but the check belongs on the server: a hand-made request
 * would otherwise put an account into IELTS mode with no IELTS profile behind
 * it, and every IELTS page would then render an empty shell.
 */
export async function setActiveExam(mode: ExamMode): Promise<ExamModeResult> {
  const user = await requireUser();
  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { preparationExams: true },
  });
  if (!row) return { error: "Account not found." };

  const preparing = row.preparationExams;
  const hasSat = preparing.includes("SAT");
  const hasIelts = preparing.includes("IELTS");

  if (mode === "SAT" && !hasSat) return { error: "You are not preparing for the SAT yet." };
  if (mode === "IELTS" && !hasIelts) return { error: "You are not preparing for IELTS yet." };
  if (mode === "BOTH" && !(hasSat && hasIelts)) {
    return { error: "Add both exams first." };
  }

  await prisma.user.update({ where: { id: user.id }, data: { activeExam: mode } });

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
  return { ok: true, redirectTo: exam === "IELTS" ? "/ielts/setup" : "/dashboard" };
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
