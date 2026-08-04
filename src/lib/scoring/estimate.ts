// Original, simplified scaled-score approximation for the student dashboard.
// This is NOT the official (proprietary, adaptively-curved) SAT scoring
// table — it linearly maps accuracy to the 200-800 per-section range so
// students get a directional estimate before enough full adaptive attempts
// exist to compute a real trend.
export function estimateScaledScore(accuracyPct: number): number {
  const clamped = Math.max(0, Math.min(100, accuracyPct));
  return Math.round(200 + (clamped / 100) * 600);
}

export function estimateTotalScore(rw: number | null, math: number | null): number | null {
  if (rw == null || math == null) return null;
  return rw + math;
}
