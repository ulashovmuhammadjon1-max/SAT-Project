import type { ModuleDifficulty } from "@prisma/client";

export function determineModule2Difficulty(
  correctCount: number,
  totalCount: number,
  thresholdPct: number
): ModuleDifficulty {
  const pct = totalCount ? (correctCount / totalCount) * 100 : 0;
  return pct >= thresholdPct ? "HARD" : "EASY";
}

// Canonical module sequence for a full adaptive Digital SAT: R&W module 1 →
// R&W module 2 (adaptive) → Math module 1 → Math module 2 (adaptive).
export const SUBJECT_ORDER = ["READING_WRITING", "MATH"] as const;
