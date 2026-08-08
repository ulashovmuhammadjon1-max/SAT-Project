import type { Subject } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import type { PlanMilestone, PlanWeek, SkillSignal, StudyPlanData } from "@/lib/plan/types";

/**
 * Personalized plan generation.
 *
 * The plan is a **function of evidence**, not a template with the student's
 * name pasted in. Two inputs feed it:
 *
 *   1. The onboarding profile — target score, test date, weekly study time.
 *   2. Every graded answer the student has produced, from both the Question
 *      Bank (`QuestionAttempt`) and full tests (`Response`). Skills the student
 *      gets wrong rise to the top; skills they have mastered drop to
 *      maintenance.
 *
 * Because the second input grows as they practise, regenerating produces a
 * different plan — which is the whole point. `evidenceCount` records how much
 * work a snapshot was built from so staleness is detectable.
 */

/** Below this many graded answers on a skill, accuracy is not yet meaningful. */
const MIN_EVIDENCE_PER_SKILL = 4;
/** Below this many graded answers overall, the plan is a cold start. */
const COLD_START_THRESHOLD = 15;
/** Accuracy at or above which a skill counts as a strength. */
const STRENGTH_ACCURACY = 80;

interface SkillRow {
  code: string;
  name: string;
  domainCode: string;
  domainName: string;
  subject: Subject;
  attempted: number;
  correct: number;
}

/**
 * Per-skill accuracy across everything the student has answered.
 *
 * One grouped query per source rather than per skill. Both tables are indexed
 * on `userId`, and the join to Question/Skill happens in Postgres, so this
 * stays a constant number of round trips no matter how much history exists.
 */
async function collectSkillSignals(userId: string): Promise<SkillRow[]> {
  const rows = await prisma.$queryRaw<
    {
      code: string;
      name: string;
      domain_code: string;
      domain_name: string;
      subject: Subject;
      attempted: bigint;
      correct: bigint;
    }[]
  >`
    WITH graded AS (
      SELECT q."skillId" AS skill_id, qa."isCorrect" AS is_correct
      FROM "QuestionAttempt" qa
      JOIN "Question" q ON q.id = qa."questionId"
      WHERE qa."userId" = ${userId} AND q."skillId" IS NOT NULL

      UNION ALL

      SELECT q."skillId" AS skill_id, r."isCorrect" AS is_correct
      FROM "Response" r
      JOIN "Question" q ON q.id = r."questionId"
      JOIN "Attempt" a ON a.id = r."attemptId"
      WHERE a."userId" = ${userId}
        AND q."skillId" IS NOT NULL
        AND r."isCorrect" IS NOT NULL
    )
    SELECT s.code, s.name,
           d.code AS domain_code, d.name AS domain_name, d.subject,
           COUNT(*)::bigint AS attempted,
           COUNT(*) FILTER (WHERE graded.is_correct)::bigint AS correct
    FROM graded
    JOIN "Skill" s ON s.id = graded.skill_id
    JOIN "Domain" d ON d.id = s."domainId"
    GROUP BY s.code, s.name, d.code, d.name, d.subject
  `;

  return rows.map((r) => ({
    code: r.code,
    name: r.name,
    domainCode: r.domain_code,
    domainName: r.domain_name,
    subject: r.subject,
    attempted: Number(r.attempted),
    correct: Number(r.correct),
  }));
}

/**
 * Rank a skill for attention. Lower sorts sooner.
 *
 * Ordering is by tier first, then by score inside the tier. A single blended
 * number cannot express this: a first attempt at it put unpractised skills at a
 * flat 55, which ranked them *above* a demonstrated 61% weakness (whose blended
 * score was ~60) and inverted the spec's own worked example. Tiers make the
 * intent explicit and un-tunable by accident.
 *
 *   Tier 0  Demonstrated weakness — enough evidence, below the strength line.
 *           Sorted by confidence-weighted accuracy, so a 40% from 30 questions
 *           outranks a 40% from 5.
 *   Tier 1  Unproven — never attempted, or too few answers to judge. Worth
 *           covering, but never ahead of a weakness you can actually see.
 *   Tier 2  Maintenance — already at or above the strength line.
 */
const TIER = { WEAKNESS: 0, UNPROVEN: 1, MAINTENANCE: 2 } as const;

function tierOf(attempted: number, accuracy: number | null): number {
  if (accuracy === null || attempted < MIN_EVIDENCE_PER_SKILL) return TIER.UNPROVEN;
  return accuracy >= STRENGTH_ACCURACY ? TIER.MAINTENANCE : TIER.WEAKNESS;
}

/**
 * Within-tier score. Raw accuracy over-reacts to one unlucky pair of questions,
 * so it is pulled toward the midpoint when evidence is thin.
 */
function priorityOf(attempted: number, accuracy: number | null): number {
  if (accuracy === null || attempted === 0) return 50;
  const confidence = Math.min(1, attempted / 20);
  return accuracy * confidence + 50 * (1 - confidence);
}

/** Sort key: tier dominates, score breaks ties, code keeps it deterministic. */
function comparePriority(a: SkillSignal, b: SkillSignal): number {
  const tierA = tierOf(a.attempted, a.accuracy);
  const tierB = tierOf(b.attempted, b.accuracy);
  if (tierA !== tierB) return tierA - tierB;
  // Inside maintenance, the *least* solid strength is the one worth revisiting.
  if (tierA === TIER.MAINTENANCE) return a.priority - b.priority;
  // Inside unproven, prefer the completely untouched over the barely touched.
  if (tierA === TIER.UNPROVEN) return a.attempted - b.attempted || a.code.localeCompare(b.code);
  return a.priority - b.priority || a.code.localeCompare(b.code);
}

function reasonFor(signal: { attempted: number; accuracy: number | null }): string {
  if (signal.accuracy === null || signal.attempted < MIN_EVIDENCE_PER_SKILL) {
    return signal.attempted === 0
      ? "Not practised yet"
      : `Only ${signal.attempted} answered so far`;
  }
  if (signal.accuracy < 50) return `${signal.accuracy}% correct — biggest gap`;
  if (signal.accuracy < 70) return `${signal.accuracy}% correct — needs work`;
  if (signal.accuracy < STRENGTH_ACCURACY) return `${signal.accuracy}% correct — nearly there`;
  return `${signal.accuracy}% correct — keep it warm`;
}

export interface PlanInputs {
  userId: string;
  currentScore: number | null;
  targetScore: number | null;
  testDate: Date | null;
  studyMinutesPerDay: number | null;
  weakestArea: string | null;
  estimatedScore: number | null;
}

export async function generatePlan(inputs: PlanInputs): Promise<StudyPlanData> {
  const [skillRows, allSkills] = await Promise.all([
    collectSkillSignals(inputs.userId),
    prisma.skill.findMany({
      select: {
        code: true,
        name: true,
        domain: { select: { code: true, name: true, subject: true } },
      },
    }),
  ]);

  const byCode = new Map(skillRows.map((r) => [r.code, r]));

  // Every skill in the taxonomy is a candidate, not only the ones already
  // attempted — otherwise a student who has never touched Geometry would never
  // be told to study it.
  const signals: SkillSignal[] = allSkills.map((s) => {
    const row = byCode.get(s.code);
    const attempted = row?.attempted ?? 0;
    const correct = row?.correct ?? 0;
    const accuracy =
      attempted >= MIN_EVIDENCE_PER_SKILL ? Math.round((correct / attempted) * 100) : null;
    return {
      code: s.code,
      name: s.name,
      domainCode: s.domain.code,
      domainName: s.domain.name,
      subject: s.domain.subject,
      attempted,
      correct,
      accuracy,
      priority: priorityOf(attempted, accuracy),
      reason: reasonFor({ attempted, accuracy }),
    };
  });

  const evidenceCount = skillRows.reduce((sum, r) => sum + r.attempted, 0);
  const coldStart = evidenceCount < COLD_START_THRESHOLD;

  const ranked = [...signals].sort(comparePriority);

  // With no performance history, honour what the student told us in onboarding
  // instead of pretending the ranking means something.
  if (coldStart && inputs.weakestArea) {
    const hinted = inputs.weakestArea.toLowerCase();
    ranked.sort((a, b) => {
      const aHit = matchesWeakArea(a, hinted) ? 0 : 1;
      const bHit = matchesWeakArea(b, hinted) ? 0 : 1;
      return aHit - bHit || comparePriority(a, b);
    });
  }

  const priorities = ranked.slice(0, 8);
  const strengths = [...signals]
    .filter((s) => s.accuracy !== null && s.accuracy >= STRENGTH_ACCURACY)
    .sort((a, b) => (b.accuracy ?? 0) - (a.accuracy ?? 0))
    .slice(0, 5);

  // --- cadence ------------------------------------------------------------
  const minutesPerDay = clamp(inputs.studyMinutesPerDay ?? 45, 10, 300);
  const weeklyMinutes = minutesPerDay * 7;
  const sessionsPerWeek = clamp(Math.round(weeklyMinutes / 45), 2, 6);
  const minutesPerSession = Math.max(15, Math.round(weeklyMinutes / sessionsPerWeek));

  const now = new Date();
  const daysUntilTest = inputs.testDate
    ? Math.max(0, Math.ceil((inputs.testDate.getTime() - now.getTime()) / 864e5))
    : null;
  const weeksUntilTest = daysUntilTest === null ? null : Math.max(1, Math.ceil(daysUntilTest / 7));

  // Plan out to the test date, capped at 8 weeks so the page stays readable.
  const weekCount = clamp(weeksUntilTest ?? 6, 1, 8);
  const weeks = buildWeeks(weekCount, ranked, strengths, sessionsPerWeek, now);

  const scoreGap =
    inputs.targetScore !== null && inputs.currentScore !== null
      ? inputs.targetScore - inputs.currentScore
      : null;

  return {
    version: 1,
    generatedAt: now.toISOString(),
    currentScore: inputs.currentScore,
    targetScore: inputs.targetScore,
    scoreGap,
    estimatedScore: inputs.estimatedScore,
    testDate: inputs.testDate ? inputs.testDate.toISOString() : null,
    daysUntilTest,
    weeksUntilTest,
    weeklyMinutes,
    sessionsPerWeek,
    minutesPerSession,
    priorities,
    strengths,
    weeks,
    milestones: buildMilestones(evidenceCount, priorities, inputs),
    evidenceCount,
    coldStart,
    headline: headlineFor({ coldStart, scoreGap, daysUntilTest, priorities }),
  };
}

function matchesWeakArea(signal: SkillSignal, hint: string): boolean {
  return (
    signal.name.toLowerCase().includes(hint) ||
    signal.domainName.toLowerCase().includes(hint) ||
    hint.includes(signal.domainName.toLowerCase())
  );
}

/**
 * Lay the ranked skills across the available weeks.
 *
 * Weakest first: week 1 takes the two most urgent skills, week 2 the next two,
 * and so on. Once the priority list is exhausted the remaining weeks turn to
 * consolidation — mixed review plus a full test — rather than inventing more
 * weaknesses.
 */
function buildWeeks(
  weekCount: number,
  ranked: SkillSignal[],
  strengths: SkillSignal[],
  sessionsPerWeek: number,
  startFrom: Date,
): PlanWeek[] {
  const weeks: PlanWeek[] = [];
  const perWeek = 2;

  for (let i = 0; i < weekCount; i++) {
    const slice = ranked.slice(i * perWeek, i * perWeek + perWeek);
    const startsOn = new Date(startFrom.getTime() + i * 7 * 864e5);

    // Group the week's skills by domain so the UI reads "Algebra: Linear
    // equations, Linear functions" rather than a flat list.
    const byDomain = new Map<string, SkillSignal[]>();
    for (const s of slice) {
      const list = byDomain.get(s.domainCode) ?? [];
      list.push(s);
      byDomain.set(s.domainCode, list);
    }

    const focus = [...byDomain.values()].map((group) => ({
      subject: group[0].subject,
      domainName: group[0].domainName,
      skillCodes: group.map((s) => s.code),
      skillNames: group.map((s) => s.name),
    }));

    const isConsolidation = slice.length === 0;
    // A full test at the end of week 2, then every second week.
    const fullTests = i > 0 && i % 2 === 1 ? 1 : 0;

    weeks.push({
      index: i + 1,
      label: `Week ${i + 1}`,
      startsOn: startsOn.toISOString(),
      focus: isConsolidation
        ? strengths.slice(0, 2).map((s) => ({
            subject: s.subject,
            domainName: s.domainName,
            skillCodes: [s.code],
            skillNames: [s.name],
          }))
        : focus,
      targetedSessions: Math.max(1, sessionsPerWeek - fullTests),
      timedModules: fullTests ? 0 : 1,
      fullTests,
      reviewFocus: isConsolidation
        ? "Mixed review — keep your strongest skills sharp"
        : `Review every miss in ${slice.map((s) => s.name).join(" and ")}`,
      practiceHref: buildPracticeHref(slice.length ? slice : strengths.slice(0, 2)),
    });
  }

  return weeks;
}

/** Deep link into the Question Bank, prefilled with this week's skills. */
function buildPracticeHref(skills: SkillSignal[]): string {
  if (skills.length === 0) return "/practice";
  const params = new URLSearchParams();
  params.set("skills", skills.map((s) => s.code).join(","));
  params.set("size", "10");
  return `/practice?${params.toString()}`;
}

function buildMilestones(
  evidenceCount: number,
  priorities: SkillSignal[],
  inputs: PlanInputs,
): PlanMilestone[] {
  const milestones: PlanMilestone[] = [
    {
      id: "diagnostic",
      label: "Answer 25 questions",
      detail: "Enough for SATForge to find your real weak spots",
      target: 25,
      current: Math.min(evidenceCount, 25),
      done: evidenceCount >= 25,
    },
    {
      id: "volume",
      label: "Answer 150 questions",
      detail: "The point where score gains usually start showing",
      target: 150,
      current: Math.min(evidenceCount, 150),
      done: evidenceCount >= 150,
    },
  ];

  const weakest = priorities[0];
  if (weakest && weakest.accuracy !== null) {
    milestones.push({
      id: `skill:${weakest.code}`,
      label: `Get ${weakest.name} to 80%`,
      detail: `Currently ${weakest.accuracy}%`,
      target: 80,
      current: weakest.accuracy,
      done: weakest.accuracy >= 80,
    });
  }

  if (inputs.targetScore && inputs.estimatedScore) {
    milestones.push({
      id: "score",
      label: `Reach ${inputs.targetScore}`,
      detail: `Latest practice test estimate: ${inputs.estimatedScore}`,
      target: inputs.targetScore,
      current: inputs.estimatedScore,
      done: inputs.estimatedScore >= inputs.targetScore,
    });
  }

  return milestones;
}

function headlineFor(args: {
  coldStart: boolean;
  scoreGap: number | null;
  daysUntilTest: number | null;
  priorities: SkillSignal[];
}): string {
  if (args.coldStart) {
    return "Answer a few questions and this plan will rebuild itself around what you actually miss.";
  }
  const weakest = args.priorities[0];
  const focus = weakest ? weakest.name : "your weakest skills";
  if (args.daysUntilTest !== null && args.daysUntilTest <= 21) {
    return `${args.daysUntilTest} days out — spend them on ${focus}.`;
  }
  if (args.scoreGap !== null && args.scoreGap > 0) {
    return `${args.scoreGap} points to go. ${focus} is where they are.`;
  }
  return `Your next gains are in ${focus}.`;
}

function clamp(n: number, lo: number, hi: number): number {
  return Math.min(hi, Math.max(lo, n));
}
