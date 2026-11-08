/**
 * The free SAT diagnostic: which questions, and what the answers say.
 *
 * 25 questions — 13 Reading & Writing, 12 Math — chosen so every domain is
 * covered and difficulty runs from easy to hard inside each one. 25 is the
 * study plan's "answer 25 questions" milestone, so finishing the diagnostic
 * also gives the plan enough evidence to personalise itself.
 *
 * The score is an estimate and is always shown as a range: 12-13 questions per
 * section cannot pin a score to ten points, and pretending otherwise would be
 * the first thing a student learns to distrust.
 */
import type { QuestionDifficulty } from "@prisma/client";

import { prisma } from "@/lib/prisma";

type Plan = { code: string; difficulties: QuestionDifficulty[] };

/** R&W in the order the real test runs its domains; Math by domain. */
const RW_PLAN: Plan[] = [
  { code: "CAS", difficulties: ["EASY", "MEDIUM", "MEDIUM", "HARD"] },
  { code: "INI", difficulties: ["EASY", "MEDIUM", "HARD"] },
  { code: "SEC", difficulties: ["EASY", "MEDIUM", "MEDIUM", "HARD"] },
  { code: "EOI", difficulties: ["MEDIUM", "HARD"] },
];
const MATH_PLAN: Plan[] = [
  { code: "ALG", difficulties: ["EASY", "MEDIUM", "HARD"] },
  { code: "ADV", difficulties: ["EASY", "MEDIUM", "HARD"] },
  { code: "PSDA", difficulties: ["EASY", "MEDIUM", "HARD"] },
  { code: "GT", difficulties: ["EASY", "MEDIUM", "HARD"] },
];

export const DIAGNOSTIC_SIZE = 25;
export const DIAGNOSTIC_MINUTES = 35;

/**
 * Pick the question set. Prefers questions the student has never answered and
 * a different skill for each pick inside a domain, so the result says
 * something about as many skills as possible.
 */
export async function pickSatDiagnostic(userId: string): Promise<string[]> {
  const domains = await prisma.domain.findMany({ select: { id: true, code: true } });
  const idByCode = new Map(domains.map((d) => [d.code, d.id]));

  const answered = await prisma.questionAttempt.findMany({
    where: { userId },
    select: { questionId: true },
    distinct: ["questionId"],
  });
  const seen = new Set(answered.map((a) => a.questionId));

  const ordered: { id: string; subject: "RW" | "MATH"; difficulty: QuestionDifficulty }[] = [];
  for (const [subject, plan] of [["RW", RW_PLAN], ["MATH", MATH_PLAN]] as const) {
    for (const step of plan) {
      const domainId = idByCode.get(step.code);
      if (!domainId) continue;
      const usedSkills = new Set<string>();
      for (const difficulty of step.difficulties) {
        const candidates = await prisma.$queryRaw<{ id: string; skillId: string }[]>`
          SELECT q.id, q."skillId" FROM "Question" q
          WHERE q."domainId" = ${domainId} AND q.difficulty = ${difficulty}::"QuestionDifficulty" AND q."isPublished" = true
          ORDER BY random() LIMIT 40`;
        const fresh = candidates.filter((c) => !seen.has(c.id) && !ordered.some((o) => o.id === c.id));
        const pool = fresh.length ? fresh : candidates.filter((c) => !ordered.some((o) => o.id === c.id));
        const pick = pool.find((c) => !usedSkills.has(c.skillId)) ?? pool[0];
        if (!pick) continue;
        usedSkills.add(pick.skillId);
        ordered.push({ id: pick.id, subject, difficulty });
      }
    }
  }

  // Inside each section, easy questions first: a diagnostic should not open on
  // its hardest question and lose the student in the first minute.
  const rank: Record<QuestionDifficulty, number> = { EASY: 0, MEDIUM: 1, HARD: 2 };
  const rw = ordered.filter((o) => o.subject === "RW");
  const math = ordered.filter((o) => o.subject === "MATH").sort((a, b) => rank[a.difficulty] - rank[b.difficulty]);
  return [...rw, ...math].map((o) => o.id);
}

export interface DiagnosticResult {
  total: { estimate: number; low: number; high: number };
  sections: {
    subject: "READING_WRITING" | "MATH";
    label: string;
    correct: number;
    answered: number;
    questions: number;
    estimate: number;
    low: number;
    high: number;
  }[];
  domains: { subject: "READING_WRITING" | "MATH"; name: string; correct: number; questions: number }[];
  /** Skills missed, worst first, for "practise this next". */
  focus: { skillId: string; skillName: string; subject: "READING_WRITING" | "MATH" }[];
  strengths: string[];
}

const WEIGHT: Record<QuestionDifficulty, number> = { EASY: 1, MEDIUM: 1.6, HARD: 2.2 };
const round10 = (n: number) => Math.round(n / 10) * 10;
const clampSection = (n: number) => Math.min(800, Math.max(200, n));

/**
 * Score the run from the student's own answers to the pinned questions, using
 * the latest answer to each one since the diagnostic started. Unanswered
 * questions count as wrong.
 */
export async function scoreSatDiagnostic(userId: string, questionIds: string[], startedAt: Date): Promise<DiagnosticResult> {
  const [questions, attempts] = await Promise.all([
    prisma.question.findMany({
      where: { id: { in: questionIds } },
      select: {
        id: true,
        difficulty: true,
        skillId: true,
        skill: { select: { name: true } },
        domain: { select: { name: true, subject: true, code: true } },
      },
    }),
    prisma.questionAttempt.findMany({
      where: { userId, questionId: { in: questionIds }, createdAt: { gte: startedAt } },
      orderBy: { createdAt: "asc" },
      select: { questionId: true, isCorrect: true },
    }),
  ]);
  const latest = new Map<string, boolean>();
  for (const a of attempts) latest.set(a.questionId, a.isCorrect);

  const sections: DiagnosticResult["sections"] = [];
  for (const subject of ["READING_WRITING", "MATH"] as const) {
    const qs = questions.filter((q) => q.domain.subject === subject);
    const totalWeight = qs.reduce((n, q) => n + WEIGHT[q.difficulty], 0) || 1;
    const earned = qs.reduce((n, q) => n + (latest.get(q.id) ? WEIGHT[q.difficulty] : 0), 0);
    const share = earned / totalWeight;
    const estimate = clampSection(round10(200 + 600 * share));
    sections.push({
      subject,
      label: subject === "MATH" ? "Math" : "Reading and Writing",
      correct: qs.filter((q) => latest.get(q.id)).length,
      answered: qs.filter((q) => latest.has(q.id)).length,
      questions: qs.length,
      estimate,
      low: clampSection(estimate - 60),
      high: clampSection(estimate + 60),
    });
  }

  const domainMap = new Map<string, DiagnosticResult["domains"][number]>();
  for (const q of questions) {
    const d = domainMap.get(q.domain.code) ?? { subject: q.domain.subject, name: q.domain.name, correct: 0, questions: 0 };
    d.questions += 1;
    if (latest.get(q.id)) d.correct += 1;
    domainMap.set(q.domain.code, d);
  }
  const domains = [...domainMap.values()].sort((a, b) => (a.subject === b.subject ? 0 : a.subject === "READING_WRITING" ? -1 : 1));

  // Missed easy questions say more about a gap than missed hard ones.
  const missed = questions
    .filter((q) => !latest.get(q.id))
    .sort((a, b) => WEIGHT[a.difficulty] - WEIGHT[b.difficulty]);
  const focus: DiagnosticResult["focus"] = [];
  for (const q of missed) {
    if (focus.some((f) => f.skillId === q.skillId)) continue;
    focus.push({ skillId: q.skillId, skillName: q.skill.name, subject: q.domain.subject });
    if (focus.length === 4) break;
  }
  const strengths = domains.filter((d) => d.questions > 0 && d.correct === d.questions).map((d) => d.name);

  const total = sections.reduce((n, s) => n + s.estimate, 0);
  return {
    total: { estimate: total, low: Math.max(400, total - 100), high: Math.min(1600, total + 100) },
    sections,
    domains,
    focus,
    strengths,
  };
}

/** A published Writing Task 2 for the IELTS diagnostic. */
export async function pickIeltsDiagnosticPart(): Promise<string | null> {
  const part = await prisma.ieltsPart.findFirst({
    where: { partNumber: 2, section: { skill: "WRITING", test: { status: "PUBLISHED" } } },
    orderBy: { section: { test: { createdAt: "asc" } } },
    select: { id: true },
  });
  return part?.id ?? null;
}
