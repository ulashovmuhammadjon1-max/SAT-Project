/**
 * Raw score to band for the objective sections.
 *
 * The conversion is read from `IeltsScoreConversion`, which an admin can
 * configure per paper. A single hardcoded table cannot be right: the real
 * conversion varies by form, and a table baked into the code would quietly
 * misreport every paper it was not built from. The constants below are only
 * the fallback used when a paper has no table of its own and no default has
 * been configured.
 */

import type { IeltsModule, IeltsSkill } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { toHalfBand } from "./bands";

/**
 * A commonly published Academic Listening/Reading approximation, used only
 * until an admin loads a real table. Index is the raw score out of 40.
 */
const FALLBACK: Record<"LISTENING" | "READING", readonly number[]> = {
  LISTENING: [
    0, 0, 0, 1, 1, 1.5, 2, 2.5, 2.5, 3, 3, 3.5, 3.5, 4, 4, 4.5, 5, 5, 5.5, 5.5,
    5.5, 6, 6, 6, 6.5, 6.5, 6.5, 7, 7, 7, 7.5, 7.5, 8, 8, 8.5, 8.5, 9, 9, 9, 9, 9,
  ],
  READING: [
    0, 0, 0, 1, 1, 1.5, 2, 2.5, 2.5, 3, 3, 3.5, 3.5, 4, 4, 4.5, 5, 5, 5.5, 5.5,
    5.5, 6, 6, 6, 6.5, 6.5, 6.5, 7, 7, 7, 7.5, 7.5, 8, 8, 8.5, 8.5, 9, 9, 9, 9, 9,
  ],
};

function fallbackBand(skill: IeltsSkill, raw: number, total: number): number {
  const table = skill === "READING" ? FALLBACK.READING : FALLBACK.LISTENING;
  // A paper with fewer than 40 questions still has to land on the same scale,
  // so scale the raw score onto the table's own length first.
  const scaled = total === table.length - 1
    ? raw
    : Math.round((raw / Math.max(total, 1)) * (table.length - 1));
  const idx = Math.min(table.length - 1, Math.max(0, scaled));
  return table[idx];
}

/**
 * The band for a raw score.
 *
 * Lookup order: this paper's own table, then the module-wide default table,
 * then the built-in approximation. The paper-specific row wins so an admin can
 * correct one paper without disturbing the rest.
 */
export async function bandForRawScore(params: {
  testId: string;
  module: IeltsModule;
  skill: IeltsSkill;
  raw: number;
  total: number;
}): Promise<number> {
  const { testId, module, skill, raw, total } = params;

  const rows = await prisma.ieltsScoreConversion.findMany({
    where: {
      module, skill, rawScore: raw,
      OR: [{ testId }, { testId: null }],
    },
  });
  // A row scoped to this paper outranks the module-wide default.
  const specific = rows.find((r) => r.testId === testId);
  const fallbackRow = rows.find((r) => r.testId === null);
  const hit = specific ?? fallbackRow;
  if (hit) return toHalfBand(hit.band);

  return fallbackBand(skill, raw, total);
}

/**
 * Whether a real conversion table exists, so the UI can say the band is an
 * approximation when it is one rather than presenting all bands alike.
 */
export async function hasConversionTable(
  module: IeltsModule,
  skill: IeltsSkill,
  testId?: string
): Promise<boolean> {
  const n = await prisma.ieltsScoreConversion.count({
    where: { module, skill, OR: [{ testId: testId ?? null }, { testId: null }] },
  });
  return n > 0;
}
