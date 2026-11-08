"use server";

import { revalidatePath } from "next/cache";
import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { pickIeltsDiagnosticPart, pickSatDiagnostic, scoreSatDiagnostic, type DiagnosticResult } from "@/lib/diagnostic";

/**
 * The free diagnostic. Every action works on the signed-in student's own row
 * only; nothing takes a user id from the client.
 */

type Kind = "SAT" | "IELTS";

export interface DiagnosticStatus {
  kind: Kind;
  state: "READY" | "IN_PROGRESS" | "DONE";
  requestedAt: string;
  completedAt: string | null;
  result: DiagnosticResult | null;
  ieltsPartId: string | null;
  ieltsSubmissionId: string | null;
}

/** All of this student's diagnostics, with IELTS completion read off the submission. */
export async function getMyDiagnostics(): Promise<DiagnosticStatus[]> {
  const user = await requireUser();
  const rows = await prisma.diagnosticTest.findMany({ where: { userId: user.id }, orderBy: { kind: "asc" } });
  const out: DiagnosticStatus[] = [];
  for (const r of rows) {
    let completedAt = r.completedAt;
    let submissionId: string | null = null;
    // IELTS is complete when the Task 2 essay has been sent for review.
    if (r.kind === "IELTS" && r.ieltsPartId) {
      const sub = await prisma.ieltsWritingSubmission.findFirst({
        where: { userId: user.id, partId: r.ieltsPartId, status: { not: "PENDING" } },
        orderBy: { submittedAt: "desc" },
        select: { id: true, submittedAt: true },
      });
      if (sub) {
        submissionId = sub.id;
        if (!completedAt) {
          completedAt = sub.submittedAt;
          await prisma.diagnosticTest.update({ where: { id: r.id }, data: { completedAt } });
        }
      }
    }
    out.push({
      kind: r.kind,
      state: completedAt ? "DONE" : r.startedAt ? "IN_PROGRESS" : "READY",
      requestedAt: r.requestedAt.toISOString(),
      completedAt: completedAt?.toISOString() ?? null,
      result: (r.result as unknown as DiagnosticResult | null) ?? null,
      ieltsPartId: r.ieltsPartId,
      ieltsSubmissionId: submissionId,
    });
  }
  return out;
}

/** Turn the diagnostic on for a student who skipped it at sign-up. Idempotent. */
export async function enableDiagnostic(kind: Kind): Promise<{ ok: true }> {
  const user = await requireUser();
  await prisma.diagnosticTest.upsert({
    where: { userId_kind: { userId: user.id, kind } },
    create: { userId: user.id, kind },
    update: {},
  });
  revalidatePath("/dashboard");
  revalidatePath("/diagnostic");
  return { ok: true };
}

/**
 * Start (or resume) the SAT diagnostic. The question set is chosen once and
 * pinned on the row, so a reload or a return days later is the same test.
 */
export async function startSatDiagnostic(): Promise<{ ok: true; href: string } | { ok: false; error: string }> {
  const user = await requireUser();
  const row = await prisma.diagnosticTest.upsert({
    where: { userId_kind: { userId: user.id, kind: "SAT" } },
    create: { userId: user.id, kind: "SAT" },
    update: {},
  });
  if (row.completedAt) return { ok: true, href: "/diagnostic" };
  if (row.questionIds.length === 0) {
    const ids = await pickSatDiagnostic(user.id);
    if (ids.length < 10) return { ok: false, error: "The diagnostic is not available right now. Please try again later." };
    // Only the first start writes the set: a double click cannot pin two.
    await prisma.diagnosticTest.updateMany({
      where: { id: row.id, questionIds: { isEmpty: true } },
      data: { questionIds: ids, startedAt: new Date() },
    });
  }
  return { ok: true, href: "/diagnostic/sat" };
}

/** Finish: score from the student's own recorded answers, store the result once. */
export async function completeSatDiagnostic(): Promise<{ ok: true } | { ok: false; error: string }> {
  const user = await requireUser();
  const row = await prisma.diagnosticTest.findUnique({ where: { userId_kind: { userId: user.id, kind: "SAT" } } });
  if (!row || !row.startedAt || row.questionIds.length === 0) return { ok: false, error: "Start the diagnostic first." };
  if (row.completedAt) return { ok: true };
  const result = await scoreSatDiagnostic(user.id, row.questionIds, row.startedAt);
  await prisma.diagnosticTest.updateMany({
    where: { id: row.id, completedAt: null },
    data: { completedAt: new Date(), result: result as unknown as Prisma.InputJsonValue },
  });
  revalidatePath("/dashboard");
  revalidatePath("/diagnostic");
  revalidatePath("/plan");
  return { ok: true };
}

/** Start the IELTS diagnostic: hand the student a Writing Task 2. */
export async function startIeltsDiagnostic(): Promise<{ ok: true; href: string } | { ok: false; error: string }> {
  const user = await requireUser();
  const row = await prisma.diagnosticTest.upsert({
    where: { userId_kind: { userId: user.id, kind: "IELTS" } },
    create: { userId: user.id, kind: "IELTS" },
    update: {},
  });
  let partId = row.ieltsPartId;
  if (!partId) {
    partId = await pickIeltsDiagnosticPart();
    if (!partId) return { ok: false, error: "No IELTS Writing task is available right now. Please try again later." };
    await prisma.diagnosticTest.update({ where: { id: row.id }, data: { ieltsPartId: partId, startedAt: new Date() } });
  }
  return { ok: true, href: `/ielts/writing/${partId}` };
}
