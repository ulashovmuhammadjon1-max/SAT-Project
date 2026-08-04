// SM-2 spaced repetition scheduler (the classic SuperMemo-2 algorithm).
// `quality` is a 0-5 self-assessment: 0-2 = forgot/hard, 3-5 = recalled.

export interface SRSState {
  easeFactor: number;
  intervalDays: number;
  repetitions: number;
}

export function scheduleNextReview(
  state: SRSState,
  quality: 0 | 1 | 2 | 3 | 4 | 5
): SRSState & { nextReviewAt: Date } {
  let { easeFactor, intervalDays, repetitions } = state;

  if (quality < 3) {
    repetitions = 0;
    intervalDays = 1;
  } else {
    repetitions += 1;
    if (repetitions === 1) intervalDays = 1;
    else if (repetitions === 2) intervalDays = 6;
    else intervalDays = Math.round(intervalDays * easeFactor);

    easeFactor = Math.max(1.3, easeFactor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)));
  }

  const nextReviewAt = new Date();
  nextReviewAt.setDate(nextReviewAt.getDate() + intervalDays);

  return { easeFactor, intervalDays, repetitions, nextReviewAt };
}

export function statusForRepetitions(repetitions: number): "NEW" | "LEARNING" | "MASTERED" {
  if (repetitions === 0) return "NEW";
  if (repetitions < 4) return "LEARNING";
  return "MASTERED";
}
