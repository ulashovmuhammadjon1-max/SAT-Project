import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { toHalfBand, writingBandFromTasks } from "@/lib/ielts/bands";

/**
 * The IELTS roadmap.
 *
 * Separate from `lib/plan/*` on purpose. The SAT plan reasons about skill
 * accuracy across a thousand-question bank and a 400–1600 scale; this one
 * reasons about two skills, a 9-band scale, and a queue of human reviews that
 * arrive one at a time. Sharing a generator between them would mean a type
 * where half the fields are null for one exam.
 *
 * Like the SAT plan it is **derived, not stored**: the inputs are the
 * onboarding answers and the bands reviewers have actually given, so the
 * roadmap moves on its own as work comes back marked. There is no snapshot to
 * go stale and nothing to invalidate.
 */

export interface IeltsPlanStage {
  index: number;
  title: string;
  blurb: string;
  /** What to do, in the order to do it. */
  actions: { label: string; href: string }[];
  done: boolean;
  /** The current stage — where the student actually is. */
  current: boolean;
}

export interface IeltsPlanData {
  targetBand: number | null;
  /** Best reviewed band per skill, or the self-reported one as a fallback. */
  writingBand: number | null;
  speakingBand: number | null;
  /** Writing and Speaking combined, as a rough indicator only. */
  estimatedBand: number | null;
  /** Bands still to climb to reach the target. Null when there is no target. */
  gap: number | null;
  /** Which skill the plan leads with, and why in words. */
  focus: "WRITING" | "SPEAKING";
  focusReason: string;
  examDate: Date | null;
  weeksLeft: number | null;
  studyMinutesPerDay: number | null;
  /** Reviewed submissions to date. */
  reviewedWriting: number;
  reviewedSpeaking: number;
  stages: IeltsPlanStage[];
  /** True when the student has never answered the IELTS questions. */
  needsOnboarding: boolean;
}

/**
 * `focusSkill` was added to `IeltsStudentProfile` after it shipped.
 *
 * Read on its own and guarded, so a database that has not had
 * `012_ielts_focus_skill.sql` applied yet reports "no preference" rather than
 * throwing P2022 at every student who opens their plan.
 */
async function readFocusSkill(userId: string): Promise<string | null> {
  try {
    const row = await prisma.ieltsStudentProfile.findUnique({
      where: { userId },
      select: { focusSkill: true },
    });
    return row?.focusSkill ?? null;
  } catch (error) {
    if (
      error instanceof Prisma.PrismaClientKnownRequestError &&
      (error.code === "P2022" || error.code === "P2021")
    ) {
      return null;
    }
    throw error;
  }
}

export async function loadIeltsPlan(userId: string): Promise<IeltsPlanData> {
  const [profile, writingReviews, speakingReviews, drafts, focusSkill] = await Promise.all([
    prisma.ieltsStudentProfile.findUnique({
      where: { userId },
      select: {
        targetBand: true, examDate: true, reason: true,
        currentWriting: true, currentSpeaking: true,
        levelSource: true, studyMinutesPerDay: true, onboardedAt: true,
      },
    }),
    prisma.ieltsWritingSubmission.findMany({
      where: { userId, review: { isNot: null } },
      select: {
        attemptId: true,
        review: { select: { overallBand: true } },
        // Task 2 counts twice in the paper band, so which task this was matters.
        partId: true,
      },
    }),
    prisma.ieltsSpeakingSubmission.findMany({
      where: { userId, review: { isNot: null } },
      select: { review: { select: { overallBand: true } } },
    }),
    prisma.ieltsWritingSubmission.count({ where: { userId, status: "PENDING" } }),
    readFocusSkill(userId),
  ]);

  // A band a reviewer gave beats one the student remembered. Only when nothing
  // has been marked does the self-reported number stand in — and the plan says
  // which it is using, because "band 6.5" from a memory and from a reviewer are
  // not the same claim.
  const reviewedWritingBands = writingReviews
    .map((w) => w.review?.overallBand)
    .filter((b): b is number => b != null);
  const reviewedSpeakingBands = speakingReviews
    .map((s) => s.review?.overallBand)
    .filter((b): b is number => b != null);

  const writingBand = reviewedWritingBands.length
    ? Math.max(...reviewedWritingBands)
    : profile?.currentWriting ?? null;
  const speakingBand = reviewedSpeakingBands.length
    ? Math.max(...reviewedSpeakingBands)
    : profile?.currentSpeaking ?? null;

  const estimatedBand =
    writingBand != null && speakingBand != null
      ? toHalfBand((writingBand + speakingBand) / 2)
      : writingBand ?? speakingBand ?? null;

  const targetBand = profile?.targetBand ?? null;
  const gap =
    targetBand != null && estimatedBand != null
      ? Math.max(0, Math.round((targetBand - estimatedBand) * 2) / 2)
      : null;

  // What the student said, then what the bands say, then Writing — which is
  // where most candidates lose the most, and the only one with a hard word
  // minimum to fall short of.
  let focus: "WRITING" | "SPEAKING" = "WRITING";
  let focusReason = "Writing is where most candidates lose the most, so we start there.";
  if (focusSkill === "WRITING" || focusSkill === "SPEAKING") {
    focus = focusSkill;
    focusReason = `You told us ${focusSkill === "WRITING" ? "Writing" : "Speaking"} worries you more.`;
  } else if (writingBand != null && speakingBand != null && writingBand !== speakingBand) {
    focus = writingBand < speakingBand ? "WRITING" : "SPEAKING";
    focusReason =
      `Your ${focus === "WRITING" ? "Writing" : "Speaking"} band is the lower of the two, ` +
      "so it is the faster place to gain.";
  }

  const examDate = profile?.examDate ?? null;
  const weeksLeft = examDate
    ? Math.max(0, Math.ceil((examDate.getTime() - Date.now()) / (7 * 86_400_000)))
    : null;

  const reviewedWriting = reviewedWritingBands.length;
  const reviewedSpeaking = reviewedSpeakingBands.length;

  const first = focus === "WRITING" ? "writing" : "speaking";
  const second = focus === "WRITING" ? "speaking" : "writing";
  const firstLabel = focus === "WRITING" ? "Writing" : "Speaking";
  const secondLabel = focus === "WRITING" ? "Speaking" : "Writing";

  // Five stages, each finishable. The order is the point: a student gets one
  // free review, so spending it on a diagnostic in their weaker skill is worth
  // more than spreading effort thinly and learning nothing about either.
  const stages: IeltsPlanStage[] = [
    {
      index: 1,
      title: `Get a real band for ${firstLabel}`,
      blurb: `One ${first === "writing" ? "task" : "interview"}, marked by a person. Everything after this is built on a band you actually earned rather than one you estimated.`,
      actions: [{ label: `Start ${firstLabel}`, href: `/ielts/${first}` }],
      done: (focus === "WRITING" ? reviewedWriting : reviewedSpeaking) > 0,
      current: false,
    },
    {
      index: 2,
      title: "Read the feedback properly",
      blurb: "Four criteria, each with a note saying what would move that band up. This is the part that changes your next attempt — the band alone will not.",
      actions: [{ label: "Open my feedback", href: "/ielts/feedback" }],
      done: reviewedWriting + reviewedSpeaking > 0,
      current: false,
    },
    {
      index: 3,
      title: `Get a band for ${secondLabel} too`,
      blurb: `Now the other half. With both marked you have a Writing and Speaking picture rather than half of one.`,
      actions: [{ label: `Start ${secondLabel}`, href: `/ielts/${second}` }],
      done: (focus === "WRITING" ? reviewedSpeaking : reviewedWriting) > 0,
      current: false,
    },
    {
      index: 4,
      title: "Sit a full Writing paper against the clock",
      blurb: "Both tasks, sixty minutes, one sitting. Budgeting the hour is a separate skill from writing well, and running out of time on Task 2 is one of the commonest ways to lose a band.",
      actions: [
        { label: "Full practice", href: "/ielts/writing" },
        { label: "Use my own topic", href: "/ielts/writing/custom" },
      ],
      done: reviewedWriting >= 2,
      current: false,
    },
    {
      index: 5,
      title: "Repeat on your weakest criterion",
      blurb: "Pick the single criterion your reviewer marked lowest and write for that alone. Broad practice moves a band slowly; one criterion at a time moves it fast.",
      actions: [
        { label: "Your own topic", href: "/ielts/writing/custom" },
        { label: "Invite friends for more reviews", href: "/ielts/invite" },
      ],
      done: reviewedWriting + reviewedSpeaking >= 4,
      current: false,
    },
  ];

  // A stage cannot be ticked before the one above it.
  //
  // The raw conditions are independent, so a student who happened to get a
  // Speaking band first saw "Read the feedback properly — Done" sitting under
  // "Get a real band for Writing — you are here", which reads as a bug even
  // though both statements were true. Clamping makes the column tell one story
  // top to bottom; nothing is lost, because the stage below un-greys the
  // moment the one above it is ticked.
  for (let n = 1; n < stages.length; n++) {
    stages[n].done = stages[n].done && stages[n - 1].done;
  }

  // The current stage is the first unfinished one.
  const currentIndex = stages.findIndex((s) => !s.done);
  if (currentIndex >= 0) stages[currentIndex].current = true;

  return {
    targetBand,
    writingBand,
    speakingBand,
    estimatedBand,
    gap,
    focus,
    focusReason,
    examDate,
    weeksLeft,
    studyMinutesPerDay: profile?.studyMinutesPerDay ?? null,
    reviewedWriting,
    reviewedSpeaking,
    stages,
    needsOnboarding: !profile?.onboardedAt,
  };
}

/** Whether the student's reported bands came from a real test. */
export function levelSourceLabel(source: string | null | undefined): string | null {
  switch ((source ?? "").toLowerCase()) {
    case "previous_test":
      return "from a test you sat";
    case "mock_or_teacher":
      return "from a mock or your teacher";
    case "never_taken":
      return "you have not sat IELTS yet";
    default:
      return null;
  }
}

/** Weekly effort, split between the two skills according to the focus. */
export function weeklyShape(plan: IeltsPlanData): {
  minutesPerWeek: number | null;
  focusShare: number;
} {
  const perDay = plan.studyMinutesPerDay;
  return {
    minutesPerWeek: perDay ? perDay * 7 : null,
    // Two thirds to the weaker skill. Not all of it: a skill left completely
    // alone for a month goes backwards, and Speaking especially decays without
    // use.
    focusShare: 0.65,
  };
}

/** Re-exported so the page can show the paper band the same way the room does. */
export { writingBandFromTasks };
