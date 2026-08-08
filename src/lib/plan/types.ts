import type { Subject } from "@prisma/client";

/**
 * The shape of a generated study plan.
 *
 * Stored as JSON on `StudyPlan.data`. Everything here is derived — from the
 * onboarding profile and from the student's actual answers — so the plan is
 * regenerated rather than edited.
 */

export interface SkillSignal {
  code: string;
  name: string;
  domainCode: string;
  domainName: string;
  subject: Subject;
  attempted: number;
  correct: number;
  /** 0-100. Null when there is not enough evidence to claim an accuracy. */
  accuracy: number | null;
  /**
   * Ranking score, low = needs work most. Combines accuracy with how much
   * evidence backs it, so a 40% from 30 questions outranks a 40% from 2.
   */
  priority: number;
  /** Why this skill was placed where it was, in words the student can read. */
  reason: string;
}

export interface PlanWeek {
  index: number;
  label: string;
  startsOn: string;
  focus: {
    subject: Subject;
    domainName: string;
    skillCodes: string[];
    skillNames: string[];
  }[];
  targetedSessions: number;
  timedModules: number;
  fullTests: number;
  reviewFocus: string;
  /** Practice-session deep link, prefilled with this week's skills. */
  practiceHref: string;
}

export interface PlanMilestone {
  id: string;
  label: string;
  detail: string;
  target: number;
  current: number;
  done: boolean;
}

export interface StudyPlanData {
  version: 1;
  generatedAt: string;

  currentScore: number | null;
  targetScore: number | null;
  scoreGap: number | null;
  /** Score estimated from real test attempts, when any exist. */
  estimatedScore: number | null;

  testDate: string | null;
  daysUntilTest: number | null;
  weeksUntilTest: number | null;

  weeklyMinutes: number;
  sessionsPerWeek: number;
  minutesPerSession: number;

  /** Weakest first. Drives the ordering of the weeks. */
  priorities: SkillSignal[];
  strengths: SkillSignal[];

  weeks: PlanWeek[];
  milestones: PlanMilestone[];

  /** How much graded work the plan was built from. */
  evidenceCount: number;
  /**
   * True when there is too little evidence to personalise from performance, so
   * the plan leans on the onboarding answers instead. The UI says so plainly
   * rather than implying a diagnosis that was never made.
   */
  coldStart: boolean;
  headline: string;
}
