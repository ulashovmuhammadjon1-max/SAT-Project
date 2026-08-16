/**
 * Which exam ecosystem the student is currently in.
 *
 * SATForge hosts two complete preparation products under one account. This
 * module is the single place that answers "SAT, IELTS, or both?", so a page
 * never has to guess and two pages can never disagree.
 *
 * Two fields, deliberately distinct:
 *
 *   preparationExams  what the student is working towards — decides what data
 *                     exists and what they are allowed to switch to.
 *   activeExam        what they are looking at right now — decides what
 *                     renders.
 *
 * Collapsing them would make "switch to IELTS for a minute" indistinguishable
 * from "stop preparing for the SAT".
 */

import { cache } from "react";
import type { ExamKind, ExamMode } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";

export interface ExamContext {
  userId: string;
  /** Everything this account is preparing for. */
  preparing: ExamKind[];
  /** What the dashboard should render right now. */
  active: ExamMode;
  /** Convenience flags, so callers stop re-deriving these. */
  hasSat: boolean;
  hasIelts: boolean;
  showSat: boolean;
  showIelts: boolean;
  /** Can the switcher be used at all? Only with more than one exam. */
  canSwitch: boolean;
}

/**
 * Reconcile `activeExam` against `preparationExams`.
 *
 * A stored mode can go stale — a student viewing BOTH who then removes IELTS
 * would otherwise keep seeing a combined dashboard with half of it empty. The
 * stored value is treated as a preference, never as permission: what the
 * student is preparing for always wins.
 */
export function resolveMode(preparing: ExamKind[], stored: ExamMode): ExamMode {
  const hasSat = preparing.includes("SAT");
  const hasIelts = preparing.includes("IELTS");

  if (!hasSat && !hasIelts) return "SAT";
  if (hasSat && !hasIelts) return "SAT";
  if (!hasSat && hasIelts) return "IELTS";

  // Preparing for both: any stored mode is legitimate.
  return stored;
}

export const getExamContext = cache(async (): Promise<ExamContext | null> => {
  const user = await getCurrentUser();
  if (!user) return null;

  const row = await prisma.user.findUnique({
    where: { id: user.id },
    // An explicit select, not a whole-row fetch. This runs on every student
    // page, and a whole-row fetch is what breaks the moment a column is added
    // to `User` before its migration lands.
    select: { preparationExams: true, activeExam: true },
  });
  if (!row) return null;

  const preparing = row.preparationExams;
  const active = resolveMode(preparing, row.activeExam);
  const hasSat = preparing.includes("SAT");
  const hasIelts = preparing.includes("IELTS");

  return {
    userId: user.id,
    preparing,
    active,
    hasSat,
    hasIelts,
    showSat: active === "SAT" || active === "BOTH",
    showIelts: active === "IELTS" || active === "BOTH",
    canSwitch: hasSat && hasIelts,
  };
});

/** The context, or a SAT-only default for a signed-out or missing user. */
export async function examContextOrDefault(): Promise<ExamContext> {
  const ctx = await getExamContext();
  return (
    ctx ?? {
      userId: "", preparing: ["SAT"], active: "SAT",
      hasSat: true, hasIelts: false,
      showSat: true, showIelts: false, canSwitch: false,
    }
  );
}

export const EXAM_LABEL: Record<ExamMode, string> = {
  SAT: "SAT",
  IELTS: "IELTS",
  BOTH: "Both",
};

/** Where the switcher sends the student when they change exam. */
export const EXAM_HOME: Record<ExamMode, string> = {
  SAT: "/dashboard",
  IELTS: "/ielts",
  BOTH: "/dashboard",
};
