/**
 * What an IELTS student's dashboard needs to know about them.
 *
 * One loader rather than a query per card, so the hero, the plan and the
 * progress strip cannot disagree about the student's current band.
 */

import type { IeltsSkill } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { overallBand } from "./bands";
import { SKILL_SHAPE } from "./constants";

export interface SkillStanding {
  skill: IeltsSkill;
  label: string;
  /** Most recent band for this skill, or null if never assessed. */
  band: number | null;
  /** How many times the student has been assessed on it. */
  attempts: number;
}

export interface IeltsDashboardData {
  profile: {
    targetBand: number | null;
    examDate: Date | null;
    daysToExam: number | null;
    studyMinutesPerDay: number | null;
    onboarded: boolean;
  };
  standings: SkillStanding[];
  currentOverall: number | null;
  /** The weakest assessed skill — what the plan should push on. */
  focus: SkillStanding | null;
  inProgressAttemptId: string | null;
  pendingWritingReviews: number;
  pendingSpeakingReviews: number;
  readyWritingReviews: number;
  readySpeakingReviews: number;
  publishedTests: number;
}

const SKILLS: IeltsSkill[] = ["LISTENING", "READING", "WRITING", "SPEAKING"];

export async function loadIeltsDashboard(userId: string): Promise<IeltsDashboardData> {
  const [profile, attempts, writing, speaking, publishedTests] = await Promise.all([
    // Explicit select, deliberately. A whole-row fetch asks the database for
    // every column `schema.prisma` knows about, so the day a column is added
    // to this model and the migration has not been applied yet, this page
    // starts throwing P2022 for every student. Naming the columns means this
    // query only breaks if one of THESE goes missing.
    prisma.ieltsStudentProfile.findUnique({
      where: { userId },
      select: {
        targetBand: true, examDate: true, reason: true,
        currentListening: true, currentReading: true,
        currentWriting: true, currentSpeaking: true, currentOverall: true,
        levelSource: true, studyMinutesPerDay: true, onboardedAt: true,
      },
    }),
    prisma.ieltsAttempt.findMany({
      where: { userId },
      orderBy: { createdAt: "desc" },
      select: {
        id: true, status: true,
        listeningBand: true, readingBand: true,
        writingBand: true, speakingBand: true,
      },
      take: 40,
    }),
    prisma.ieltsWritingSubmission.findMany({
      where: { userId },
      select: { status: true },
    }),
    prisma.ieltsSpeakingSubmission.findMany({
      where: { userId },
      select: { status: true },
    }),
    prisma.ieltsTest.count({ where: { status: "PUBLISHED", module: "ACADEMIC" } }),
  ]);

  const bandOf = (skill: IeltsSkill, a: (typeof attempts)[number]) =>
    skill === "LISTENING" ? a.listeningBand
      : skill === "READING" ? a.readingBand
      : skill === "WRITING" ? a.writingBand
      : a.speakingBand;

  const standings: SkillStanding[] = SKILLS.map((skill) => {
    const scored = attempts.filter((a) => bandOf(skill, a) != null);
    return {
      skill,
      label: SKILL_SHAPE[skill].label,
      // `attempts` is newest-first, so the first scored row is the latest band.
      band: scored.length ? (bandOf(skill, scored[0]) as number) : null,
      attempts: scored.length,
    };
  });

  // Fall back to the self-reported starting point so a student who has just
  // finished onboarding sees their own numbers rather than four dashes.
  const withFallback: SkillStanding[] = standings.map((s) => {
    if (s.band != null || !profile) return s;
    const self =
      s.skill === "LISTENING" ? profile.currentListening
        : s.skill === "READING" ? profile.currentReading
        : s.skill === "WRITING" ? profile.currentWriting
        : profile.currentSpeaking;
    return { ...s, band: self ?? null };
  });

  const currentOverall =
    overallBand({
      listening: withFallback[0].band,
      reading: withFallback[1].band,
      writing: withFallback[2].band,
      speaking: withFallback[3].band,
    }) ?? profile?.currentOverall ?? null;

  const assessed = withFallback.filter((s) => s.band != null);
  const focus = assessed.length
    ? assessed.reduce((worst, s) => ((s.band as number) < (worst.band as number) ? s : worst))
    : null;

  const examDate = profile?.examDate ?? null;
  const daysToExam = examDate
    ? Math.ceil((examDate.getTime() - Date.now()) / 86_400_000)
    : null;

  const pending = (rows: { status: string }[]) =>
    rows.filter((r) => r.status === "PENDING" || r.status === "ASSIGNED" || r.status === "IN_REVIEW").length;
  const ready = (rows: { status: string }[]) => rows.filter((r) => r.status === "COMPLETE").length;

  return {
    profile: {
      targetBand: profile?.targetBand ?? null,
      examDate,
      daysToExam,
      studyMinutesPerDay: profile?.studyMinutesPerDay ?? null,
      onboarded: Boolean(profile?.onboardedAt),
    },
    standings: withFallback,
    currentOverall,
    focus,
    inProgressAttemptId: attempts.find((a) => a.status === "IN_PROGRESS")?.id ?? null,
    pendingWritingReviews: pending(writing),
    pendingSpeakingReviews: pending(speaking),
    readyWritingReviews: ready(writing),
    readySpeakingReviews: ready(speaking),
    publishedTests,
  };
}
