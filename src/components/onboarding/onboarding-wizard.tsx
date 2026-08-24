"use client";

import { useCallback, useEffect, useMemo, useRef, useState, useTransition, type ReactNode } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { signIn } from "next-auth/react";
import { AnimatePresence, motion } from "framer-motion";
import {
  ArrowLeft,
  ArrowRight,
  Check,
  GraduationCap,
  Loader2,
  Lock,
  Mail,
  Sparkles,
  User,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import {
  ChipOption,
  CountryPicker,
  MonthPicker,
  OptionCard,
  ScoreSlider,
  UniversityPicker,
} from "@/components/onboarding/controls";
import { registerWithOnboarding } from "@/server/actions/auth/onboarding";
import { EMPTY_PROFILE, type OnboardingProfile } from "@/lib/validations/onboarding";
import { cn } from "@/lib/utils";

const STORAGE_KEY = "scholarly-onboarding";
const EASE = [0.22, 1, 0.36, 1] as const;

export function OnboardingWizard({ referralCode = null }: { referralCode?: string | null }) {
  const router = useRouter();
  const [step, setStep] = useState(0);
  const [direction, setDirection] = useState<1 | -1>(1);
  const [profile, setProfile] = useState<OnboardingProfile>(EMPTY_PROFILE);
  const [hydrated, setHydrated] = useState(false);

  // Answers live in the browser until the very last step — no partial user
  // rows, and a refresh mid-wizard doesn't lose anything.
  useEffect(() => {
    try {
      const raw = window.sessionStorage.getItem(STORAGE_KEY);
      if (raw) {
        const saved = JSON.parse(raw) as { step?: number; profile?: OnboardingProfile };
        if (saved.profile) setProfile({ ...EMPTY_PROFILE, ...saved.profile });
        // Never restore straight onto the account step; the answers matter more.
        if (typeof saved.step === "number") setStep(Math.max(saved.step, 0));
      }
    } catch {
      // Unreadable storage just means starting fresh.
    }
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (!hydrated) return;
    try {
      window.sessionStorage.setItem(STORAGE_KEY, JSON.stringify({ step, profile }));
    } catch {
      // Private mode / quota — the wizard still works, it just won't resume.
    }
  }, [step, profile, hydrated]);

  const patch = useCallback((p: Partial<OnboardingProfile>) => setProfile((prev) => ({ ...prev, ...p })), []);

  const goNext = useCallback(() => {
    setDirection(1);
    setStep((s) => s + 1);
  }, []);

  const goBack = useCallback(() => {
    setDirection(-1);
    setStep((s) => Math.max(s - 1, 0));
  }, []);

  /** Advances after a short beat, so the selection is visibly registered. */
  const selectAndAdvance = useCallback(
    (p: Partial<OnboardingProfile>) => {
      patch(p);
      window.setTimeout(goNext, 220);
    },
    [patch, goNext]
  );

  const steps = useMemo(
    () => buildSteps({ profile, patch, selectAndAdvance, referralCode }),
    [profile, patch, selectAndAdvance, referralCode]
  );
  // The step list changes length with the track — SAT alone is twelve
  // questions, both exams is nineteen — so the count is read off the built
  // list rather than a constant. Clamped because a student can go back to the
  // chooser and pick a shorter track while standing on a step that no longer
  // exists.
  const total = steps.length;
  const index = Math.min(step, total - 1);
  const current = steps[index];
  const isAccountStep = index === total - 1;

  if (!hydrated) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <Loader2 className="h-5 w-5 animate-spin text-muted-foreground" />
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col bg-background">
      {/* Ambient background */}
      <div className="pointer-events-none fixed inset-0 -z-10">
        <div className="absolute inset-0 bg-[radial-gradient(60%_45%_at_50%_0%,hsl(226_84%_56%/0.09),transparent_70%)]" />
        <div className="absolute left-[10%] top-[15%] h-[320px] w-[320px] rounded-full bg-primary/10 blur-[110px]" />
        <div className="absolute bottom-[10%] right-[12%] h-[300px] w-[300px] rounded-full bg-[hsl(266_84%_60%)]/10 blur-[110px]" />
      </div>

      {/* Header + progress */}
      <header className="sticky top-0 z-20 border-b border-border/60 bg-background/80 backdrop-blur-xl">
        <div className="mx-auto flex h-16 max-w-2xl items-center gap-4 px-5">
          {step > 0 ? (
            <button
              type="button"
              onClick={goBack}
              aria-label="Go back"
              className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground"
            >
              <ArrowLeft className="h-[18px] w-[18px]" />
            </button>
          ) : (
            <Link
              href="/"
              aria-label="Back to home"
              className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground"
            >
              <ArrowLeft className="h-[18px] w-[18px]" />
            </Link>
          )}

          <div className="h-2 flex-1 overflow-hidden rounded-full bg-secondary">
            <motion.div
              className="h-full rounded-full bg-gradient-to-r from-primary to-[hsl(250_84%_60%)]"
              initial={false}
              animate={{ width: `${((index + 1) / total) * 100}%` }}
              transition={{ duration: 0.45, ease: EASE }}
            />
          </div>

          <span className="shrink-0 text-sm font-semibold tabular-nums text-muted-foreground">
            {index + 1}/{total}
          </span>
        </div>
      </header>

      {/* Step body */}
      <main className="flex flex-1 items-start justify-center px-5 py-10 sm:py-14">
        <div className="relative w-full max-w-xl">
          <AnimatePresence custom={direction} initial={false}>
            <motion.div
              key={index}
              custom={direction}
              initial={{ opacity: 0, x: direction * 40 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: direction * -40, position: "absolute" }}
              transition={{ duration: 0.32, ease: EASE }}
              // The outgoing step's exit animation is decorative only — it
              // must never be able to block the incoming step from becoming
              // visible. `mode="wait"` used to make that block possible: if an
              // exit ever failed to resolve cleanly (e.g. interrupted by a
              // fast click), AnimatePresence would wait for it forever and
              // the next step would stay stuck at its `initial` (invisible)
              // state even though it had already mounted. Letting enter and
              // exit run independently removes that dependency entirely.
              className="w-full"
            >
              <div className="text-center">
                {current.emoji && (
                  <motion.div
                    initial={{ scale: 0.5, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    transition={{ delay: 0.05, type: "spring", stiffness: 260, damping: 18 }}
                    className="mx-auto mb-5 flex h-16 w-16 items-center justify-center rounded-2xl border border-border/70 bg-card text-3xl shadow-soft"
                  >
                    {current.emoji}
                  </motion.div>
                )}
                <h1 className="font-display text-[26px] font-semibold leading-tight tracking-tight text-balance sm:text-3xl">
                  {current.title}
                </h1>
                {current.subtitle && (
                  <p className="mx-auto mt-2.5 max-w-md text-[15px] leading-relaxed text-muted-foreground text-balance">
                    {current.subtitle}
                  </p>
                )}
              </div>

              <div className="mt-8">{current.content}</div>

              {!isAccountStep && (
                <div className="mt-8 flex flex-col items-center gap-3">
                  <Button
                    size="lg"
                    onClick={goNext}
                    disabled={!current.canContinue}
                    className="h-12 w-full rounded-full text-[15px] shadow-soft"
                  >
                    {current.cta ?? "Continue"}
                    <ArrowRight className="h-4 w-4" />
                  </Button>
                  {current.skippable && (
                    <button
                      type="button"
                      onClick={goNext}
                      className="text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
                    >
                      Skip this question
                    </button>
                  )}
                </div>
              )}
            </motion.div>
          </AnimatePresence>
        </div>
      </main>

      {isAccountStep && <AccountStepFooter />}
    </div>
  );
}

function AccountStepFooter() {
  return (
    <footer className="pb-8 text-center text-xs text-muted-foreground">
      Already have an account?{" "}
      <Link href="/login" className="font-medium text-primary hover:underline">
        Sign in
      </Link>
    </footer>
  );
}

/* -------------------------------------------------------------------------- */
/* Step definitions                                                            */
/* -------------------------------------------------------------------------- */

interface Step {
  emoji?: string;
  title: string;
  subtitle?: string;
  content: ReactNode;
  canContinue: boolean;
  skippable?: boolean;
  cta?: string;
}

function buildSteps({
  profile,
  patch,
  selectAndAdvance,
  referralCode,
}: {
  profile: OnboardingProfile;
  patch: (p: Partial<OnboardingProfile>) => void;
  selectAndAdvance: (p: Partial<OnboardingProfile>) => void;
  referralCode: string | null;
}): Step[] {
  const track = profile.track;
  return [
    // 1 — Which exam. Asked first because it decides which of the two
    // question sets is worth asking at all: a 1450 target means nothing to
    // someone sitting IELTS, and a Task 2 word count means nothing to someone
    // sitting the SAT.
    {
      emoji: "🧭",
      title: "What are you preparing for?",
      subtitle: "This decides what we ask next and what your plan is built around.",
      canContinue: track !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "SAT", icon: "📘", t: "SAT", s: "Practice tests, a question bank and a personalised plan" },
              { v: "IELTS", icon: "🗣️", t: "IELTS", s: "Writing and Speaking, marked by a person, free" },
              { v: "BOTH", icon: "🎯", t: "Both", s: "Two separate plans, and a switch between them any time" },
            ] as const
          ).map((o, i) => (
            <OptionCard
              key={o.v}
              index={i}
              icon={o.icon}
              title={o.t}
              subtitle={o.s}
              selected={track === o.v}
              onSelect={() => selectAndAdvance({ track: o.v })}
            />
          ))}
          <p className="pt-1 text-center text-xs text-muted-foreground">
            You can switch between the two at any time afterwards — this only decides
            which questions we ask now.
          </p>
        </div>
      ),
    },

    ...(track === "IELTS" ? [] : satSteps({ profile, patch, selectAndAdvance })),
    ...(track === "IELTS" || track === "BOTH"
      ? ieltsSteps({ profile, patch, selectAndAdvance })
      : []),

    // Account — always last, whichever track was taken.
    {
      emoji: "🎉",
      title: track === "BOTH" ? "Both plans are ready" : "Your plan is ready",
      subtitle:
        "Create your account to save it. We will email you a link to confirm your address — your account is not active until you click it.",
      canContinue: true,
      content: <AccountStep profile={profile} referralCode={referralCode} />,
    },
  ];
}

/**
 * The SAT questions.
 *
 * Unchanged from before the IELTS track existed — a student picking SAT sees
 * exactly the wizard they would have seen.
 */
function satSteps({
  profile,
  patch,
  selectAndAdvance,
}: {
  profile: OnboardingProfile;
  patch: (p: Partial<OnboardingProfile>) => void;
  selectAndAdvance: (p: Partial<OnboardingProfile>) => void;
}): Step[] {
  return [
    // 1 — Welcome / motivation
    {
      emoji: "👋",
      title: "Welcome to Scholarly",
      subtitle: "First, what brings you here? This shapes the plan we build for you.",
      canContinue: profile.goal !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "IMPROVE_SCORE", icon: "📈", t: "Improve my SAT score", s: "I've tested before and want more points" },
              { v: "FIRST_SAT", icon: "🎯", t: "Preparing for my first SAT", s: "Starting from scratch" },
              { v: "RETAKING", icon: "🔁", t: "Retaking the SAT", s: "One more shot at a better number" },
              { v: "COLLEGE_ADMISSIONS", icon: "🎓", t: "College admissions", s: "The SAT is one piece of my application" },
            ] as const
          ).map((o, i) => (
            <OptionCard
              key={o.v}
              index={i}
              icon={o.icon}
              title={o.t}
              subtitle={o.s}
              selected={profile.goal === o.v}
              onSelect={() => selectAndAdvance({ goal: o.v })}
            />
          ))}
        </div>
      ),
    },

    // 2 — Current score
    {
      emoji: "📊",
      title: "What's your current SAT score?",
      subtitle: "Your most recent real or practice score. If you haven't tested yet, just skip — we'll find out from your first diagnostic.",
      canContinue: true,
      skippable: profile.currentScore === null,
      content: (
        <div className="rounded-2xl border border-border/70 bg-card p-6 shadow-soft">
          <ScoreSlider
            value={profile.currentScore ?? 1100}
            onChange={(v) => patch({ currentScore: v })}
          />
          {profile.currentScore !== null && (
            <button
              type="button"
              onClick={() => patch({ currentScore: null })}
              className="mt-5 w-full text-center text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
            >
              I haven&apos;t taken the SAT yet
            </button>
          )}
        </div>
      ),
    },

    // 3 — Target score
    {
      emoji: "🏔️",
      title: "What score are you aiming for?",
      subtitle: "Pick the number you'd be genuinely happy to see on test day.",
      canContinue: profile.targetScore !== null,
      content: (
        <div className="space-y-5">
          <div className="grid grid-cols-3 gap-2.5">
            {[1100, 1200, 1300, 1400, 1500, 1550].map((score, i) => (
              <ChipOption
                key={score}
                index={i}
                selected={profile.targetScore === score}
                onSelect={() => selectAndAdvance({ targetScore: score })}
              >
                {score === 1550 ? "1550+" : score}
              </ChipOption>
            ))}
          </div>
          {profile.currentScore !== null && profile.targetScore !== null && (
            <motion.p
              initial={{ opacity: 0, y: 6 }}
              animate={{ opacity: 1, y: 0 }}
              className="rounded-xl bg-primary/[0.06] px-4 py-3 text-center text-sm text-foreground"
            >
              {profile.targetScore > profile.currentScore ? (
                <>
                  That&apos;s <span className="font-semibold text-primary">+{profile.targetScore - profile.currentScore} points</span>{" "}
                  from where you are. Absolutely doable.
                </>
              ) : (
                <>Locking in a score you&apos;ve already reached — smart. Let&apos;s make it consistent.</>
              )}
            </motion.p>
          )}
        </div>
      ),
    },

    // 4 — Dream universities
    {
      emoji: "🎓",
      title: "Where do you dream of going?",
      subtitle: "Pick as many as you like. We'll keep your target score honest against their ranges.",
      canContinue: true,
      skippable: profile.dreamUniversities.length === 0,
      content: <UniversityPicker value={profile.dreamUniversities} onChange={(v) => patch({ dreamUniversities: v })} />,
    },

    // 5 — Country
    {
      emoji: "🌍",
      title: "What country are you from?",
      subtitle: "This helps us understand where our students are and tailor test-date guidance.",
      canContinue: profile.countryCode !== null,
      content: <CountryPicker value={profile.countryCode} onChange={(code) => patch({ countryCode: code })} />,
    },

    // 6 — Grade level
    {
      emoji: "📚",
      title: "What grade are you in?",
      canContinue: profile.gradeLevel !== null,
      content: (
        <div className="grid grid-cols-2 gap-2.5 sm:grid-cols-3">
          {(
            [
              { v: "GRADE_9", t: "9th grade" },
              { v: "GRADE_10", t: "10th grade" },
              { v: "GRADE_11", t: "11th grade" },
              { v: "GRADE_12", t: "12th grade" },
              { v: "GAP_YEAR", t: "Gap year" },
              { v: "COLLEGE", t: "College" },
              { v: "OTHER", t: "Other" },
            ] as const
          ).map((o, i) => (
            <ChipOption
              key={o.v}
              index={i}
              selected={profile.gradeLevel === o.v}
              onSelect={() => selectAndAdvance({ gradeLevel: o.v })}
            >
              {o.t}
            </ChipOption>
          ))}
        </div>
      ),
    },

    // 7 — SAT date
    {
      emoji: "📅",
      title: "When is your SAT?",
      subtitle: "Even a rough month helps — it decides how much time we spend on full tests versus targeted drills.",
      canContinue: true,
      skippable: profile.satMonth === null,
      content: <MonthPicker value={profile.satMonth} onChange={(v) => patch({ satMonth: v })} />,
    },

    // 8 — Strongest section
    {
      emoji: "💪",
      title: "What's your strongest section?",
      subtitle: "Be honest — we're not grading this one.",
      canContinue: profile.strongestSection !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "READING", icon: "📖", t: "Reading", s: "Comprehension, inference, evidence" },
              { v: "WRITING", icon: "✍️", t: "Writing", s: "Grammar, boundaries, transitions" },
              { v: "MATH", icon: "🔢", t: "Math", s: "Algebra, data, advanced topics" },
            ] as const
          ).map((o, i) => (
            <OptionCard
              key={o.v}
              index={i}
              icon={o.icon}
              title={o.t}
              subtitle={o.s}
              selected={profile.strongestSection === o.v}
              onSelect={() => selectAndAdvance({ strongestSection: o.v })}
            />
          ))}
        </div>
      ),
    },

    // 9 — Weakest area
    {
      emoji: "🎯",
      title: "And what needs the most work?",
      subtitle: "This is where your plan will spend most of its time.",
      canContinue: profile.weakestArea !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "READING", icon: "📖", t: "Reading" },
              { v: "WRITING", icon: "✍️", t: "Writing" },
              { v: "MATH", icon: "🔢", t: "Math" },
              { v: "VOCABULARY", icon: "🔤", t: "Vocabulary" },
              { v: "TIME_MANAGEMENT", icon: "⏱️", t: "Time management" },
            ] as const
          ).map((o, i) => (
            <OptionCard
              key={o.v}
              index={i}
              icon={o.icon}
              title={o.t}
              selected={profile.weakestArea === o.v}
              onSelect={() => selectAndAdvance({ weakestArea: o.v })}
            />
          ))}
        </div>
      ),
    },

    // 10 — Study commitment
    {
      emoji: "⏳",
      title: "How much time can you give this?",
      subtitle: "Pick something you'll actually keep to. Consistency beats intensity every time.",
      canContinue: profile.studyMinutesPerDay !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: 15, t: "15 minutes a day", s: "A steady trickle — great for long runways" },
              { v: 30, t: "30 minutes a day", s: "The sweet spot for most students" },
              { v: 60, t: "1 hour a day", s: "Serious progress, fast" },
              { v: 120, t: "2+ hours a day", s: "All-in sprint mode" },
            ] as const
          ).map((o, i) => (
            <OptionCard
              key={o.v}
              index={i}
              title={o.t}
              subtitle={o.s}
              selected={profile.studyMinutesPerDay === o.v}
              onSelect={() => selectAndAdvance({ studyMinutesPerDay: o.v })}
            />
          ))}
        </div>
      ),
    },

    // 11 — Daily goal
    {
      emoji: "🔥",
      title: "Set your daily goal",
      subtitle: "We'll track this on your dashboard and keep your streak alive.",
      canContinue: profile.dailyGoalType !== null && profile.dailyGoalValue !== null,
      content: <DailyGoalStep profile={profile} patch={patch} />,
    },

  ];
}


/**
 * The IELTS questions.
 *
 * Deliberately about Writing and Speaking only. Scholarly does not mark
 * Listening or Reading, and asking a student to rate skills the plan cannot
 * then help with promises something the product does not deliver — the surest
 * way to make a personalised plan feel generic.
 */
function ieltsSteps({
  profile,
  patch,
  selectAndAdvance,
}: {
  profile: OnboardingProfile;
  patch: (p: Partial<OnboardingProfile>) => void;
  selectAndAdvance: (p: Partial<OnboardingProfile>) => void;
}): Step[] {
  const i = profile.ielts;
  const setI = (p: Partial<typeof i>) => patch({ ielts: { ...i, ...p } });
  const pickI = (p: Partial<typeof i>) => selectAndAdvance({ ielts: { ...i, ...p } });
  const both = profile.track === "BOTH";

  return [
    // Why IELTS — the reason sets the band that actually matters. A university
    // offer is a hard threshold; "for work" usually is not.
    {
      emoji: "🌍",
      title: both ? "Now for IELTS — why do you need it?" : "Why do you need IELTS?",
      subtitle: "The band you need depends on what it is for.",
      canContinue: i.reason !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "UNIVERSITY", icon: "🎓", t: "University admission", s: "Usually a fixed band, often with a per-skill minimum" },
              { v: "WORK", icon: "💼", t: "Work or professional registration", s: "A required band for a job or a licence" },
              { v: "IMMIGRATION", icon: "🛂", t: "Immigration or a visa", s: "A points threshold to clear" },
              { v: "OTHER", icon: "✨", t: "Something else", s: "Personal goal, or keeping options open" },
            ] as const
          ).map((o, n) => (
            <OptionCard
              key={o.v}
              index={n}
              icon={o.icon}
              title={o.t}
              subtitle={o.s}
              selected={i.reason === o.v}
              onSelect={() => pickI({ reason: o.v })}
            />
          ))}
        </div>
      ),
    },

    // Target band.
    {
      emoji: "🎯",
      title: "What band are you aiming for?",
      subtitle: "Overall. We will work back from this to what each task needs.",
      canContinue: i.targetBand !== null,
      content: <BandGrid value={i.targetBand} onSelect={(b) => pickI({ targetBand: b })} />,
    },

    // Where they are starting from.
    {
      emoji: "📍",
      title: "Where are you starting from?",
      subtitle: "An honest answer makes the plan useful. Nobody else sees this.",
      canContinue: i.levelSource !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "NEVER_TAKEN", icon: "🌱", t: "I have never taken IELTS", s: "We will start you with a diagnostic task" },
              { v: "PREVIOUS_TEST", icon: "📄", t: "I have a real IELTS result", s: "From a test I actually sat" },
              { v: "MOCK_OR_TEACHER", icon: "📝", t: "A mock or my teacher's estimate", s: "Not official, but a real assessment" },
            ] as const
          ).map((o, n) => (
            <OptionCard
              key={o.v}
              index={n}
              icon={o.icon}
              title={o.t}
              subtitle={o.s}
              selected={i.levelSource === o.v}
              onSelect={() => pickI({ levelSource: o.v })}
            />
          ))}
        </div>
      ),
    },

    // Current bands — only worth asking when there is something to report.
    ...(i.levelSource && i.levelSource !== "NEVER_TAKEN"
      ? [
          {
            emoji: "📊",
            title: "What did you get for Writing and Speaking?",
            subtitle: "Just these two — they are the ones we mark.",
            canContinue: i.currentWriting !== null && i.currentSpeaking !== null,
            content: (
              <div className="space-y-6">
                <div className="space-y-2">
                  <p className="text-sm font-semibold">Writing</p>
                  <BandGrid value={i.currentWriting} onSelect={(b) => setI({ currentWriting: b })} />
                </div>
                <div className="space-y-2">
                  <p className="text-sm font-semibold">Speaking</p>
                  <BandGrid value={i.currentSpeaking} onSelect={(b) => setI({ currentSpeaking: b })} />
                </div>
              </div>
            ),
          } satisfies Step,
        ]
      : []),

    // Which of the two to lead with.
    {
      emoji: "🪜",
      title: "Which one worries you more?",
      subtitle: "We will front-load your plan with it. You will practise both either way.",
      canContinue: i.focusSkill !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: "WRITING", icon: "✍️", t: "Writing", s: "Task 1 and Task 2, marked on four criteria" },
              { v: "SPEAKING", icon: "🎙️", t: "Speaking", s: "Three parts, recorded and marked on four criteria" },
            ] as const
          ).map((o, n) => (
            <OptionCard
              key={o.v}
              index={n}
              icon={o.icon}
              title={o.t}
              subtitle={o.s}
              selected={i.focusSkill === o.v}
              onSelect={() => pickI({ focusSkill: o.v })}
            />
          ))}
        </div>
      ),
    },

    // When the test is.
    {
      emoji: "📅",
      title: "When is your IELTS test?",
      subtitle: "A rough month is enough. Skip it if you have not booked yet.",
      canContinue: true,
      content: (
        <MonthPicker value={i.examMonth} onChange={(v) => setI({ examMonth: v })} />
      ),
    },

    // Time — asked separately from the SAT answer, because a student doing both
    // is budgeting one evening across two exams, not doubling their day.
    {
      emoji: "⏳",
      title: both ? "How much of that time goes to IELTS?" : "How much time can you give this?",
      subtitle: both
        ? "On top of your SAT study. Be realistic — a plan you keep beats a plan you admire."
        : "Pick something you will actually keep to. Consistency beats intensity.",
      canContinue: i.studyMinutesPerDay !== null,
      content: (
        <div className="space-y-3">
          {(
            [
              { v: 15, t: "15 minutes a day", s: "One Speaking answer, or a Task 1 plan" },
              { v: 30, t: "30 minutes a day", s: "A full Task 1, or half a Task 2" },
              { v: 60, t: "1 hour a day", s: "A complete Task 2 with time to check it" },
              { v: 120, t: "2+ hours a day", s: "A full Writing paper and a Speaking test" },
            ] as const
          ).map((o, n) => (
            <OptionCard
              key={o.v}
              index={n}
              title={o.t}
              subtitle={o.s}
              selected={i.studyMinutesPerDay === o.v}
              onSelect={() => pickI({ studyMinutesPerDay: o.v })}
            />
          ))}
        </div>
      ),
    },
  ];
}

/** Bands 4.0 to 9.0 in half steps, as a grid rather than a slider. */
function BandGrid({
  value,
  onSelect,
}: {
  value: number | null;
  onSelect: (band: number) => void;
}) {
  const bands = Array.from({ length: 11 }, (_, n) => 4 + n * 0.5);
  return (
    <div className="grid grid-cols-4 gap-2 sm:grid-cols-6">
      {bands.map((b) => (
        <button
          key={b}
          type="button"
          onClick={() => onSelect(b)}
          aria-pressed={value === b}
          className={cn(
            "rounded-xl border py-3 text-base font-semibold tabular-nums transition-colors",
            value === b
              ? "border-primary bg-primary text-primary-foreground"
              : "border-border hover:bg-secondary"
          )}
        >
          {Number.isInteger(b) ? b : b.toFixed(1)}
        </button>
      ))}
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Daily goal                                                                  */
/* -------------------------------------------------------------------------- */

const QUESTION_PRESETS = [10, 20, 30, 50];
const MINUTE_PRESETS = [15, 30, 45, 60];

function DailyGoalStep({
  profile,
  patch,
}: {
  profile: OnboardingProfile;
  patch: (p: Partial<OnboardingProfile>) => void;
}) {
  const type = profile.dailyGoalType ?? "QUESTIONS";
  const presets = type === "QUESTIONS" ? QUESTION_PRESETS : MINUTE_PRESETS;

  return (
    <div className="space-y-5">
      <div className="grid grid-cols-2 gap-2 rounded-xl bg-secondary p-1">
        {(
          [
            { v: "QUESTIONS", t: "Questions per day" },
            { v: "MINUTES", t: "Minutes per day" },
          ] as const
        ).map((o) => (
          <button
            key={o.v}
            type="button"
            onClick={() => patch({ dailyGoalType: o.v, dailyGoalValue: null })}
            className={cn(
              "relative rounded-lg py-2.5 text-sm font-semibold transition-colors",
              profile.dailyGoalType === o.v ? "text-primary-foreground" : "text-muted-foreground hover:text-foreground"
            )}
          >
            {profile.dailyGoalType === o.v && (
              <motion.span
                layoutId="goal-type-pill"
                className="absolute inset-0 rounded-lg bg-primary"
                transition={{ type: "spring", stiffness: 380, damping: 30 }}
              />
            )}
            <span className="relative">{o.t}</span>
          </button>
        ))}
      </div>

      <div className="grid grid-cols-4 gap-2.5">
        {presets.map((v, i) => (
          <ChipOption
            key={v}
            index={i}
            selected={profile.dailyGoalValue === v && profile.dailyGoalType === type}
            onSelect={() => patch({ dailyGoalType: type, dailyGoalValue: v })}
          >
            {v}
          </ChipOption>
        ))}
      </div>

      {profile.dailyGoalValue !== null && profile.dailyGoalType !== null && (
        <motion.p
          initial={{ opacity: 0, y: 6 }}
          animate={{ opacity: 1, y: 0 }}
          className="rounded-xl bg-primary/[0.06] px-4 py-3 text-center text-sm"
        >
          <span className="font-semibold text-primary">
            {profile.dailyGoalValue} {profile.dailyGoalType === "QUESTIONS" ? "questions" : "minutes"}
          </span>{" "}
          a day — that&apos;s roughly{" "}
          <span className="font-semibold">
            {profile.dailyGoalType === "QUESTIONS"
              ? `${profile.dailyGoalValue * 7} questions`
              : `${Math.round((profile.dailyGoalValue * 7) / 60)} hours`}
          </span>{" "}
          a week.
        </motion.p>
      )}
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Step 12 — account creation                                                  */
/* -------------------------------------------------------------------------- */

function AccountStep({
  profile,
  referralCode,
}: {
  profile: OnboardingProfile;
  /** Carried from ?ref= on the onboarding URL. Validated server-side. */
  referralCode: string | null;
}) {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();
  const [acceptedTerms, setAcceptedTerms] = useState(false);
  const formRef = useRef<HTMLFormElement>(null);

  function onSubmit(formData: FormData) {
    setError(null);
    const name = String(formData.get("name") ?? "");
    const email = String(formData.get("email") ?? "");
    const password = String(formData.get("password") ?? "");

    startTransition(async () => {
      const result = await registerWithOnboarding({
        name,
        email,
        password,
        profile,
        referralCode,
        acceptedTerms: acceptedTerms as true,
      });
      if (result.error) {
        setError(result.error);
        return;
      }

      // Sign straight in so the student is already authenticated when they come
      // back from confirming their email — the link then lands them on their
      // own dashboard rather than on a login form.
      const signInResult = await signIn("credentials", { email, password, redirect: false });
      try {
        window.sessionStorage.removeItem(STORAGE_KEY);
      } catch {
        // Non-fatal.
      }

      if (signInResult?.error) {
        router.push("/login?registered=1");
        return;
      }
      // Straight to the waiting screen: the dashboard would only redirect here
      // anyway, and an unexplained bounce reads as a bug.
      router.push("/verify-email");
      router.refresh();
    });
  }

  return (
    <div className="space-y-6">
      <PlanSummary profile={profile} />

      <form ref={formRef} action={onSubmit} className="space-y-3.5">
        <Field icon={User} name="name" type="text" placeholder="Your name" autoComplete="name" required />
        <Field icon={Mail} name="email" type="email" placeholder="you@example.com" autoComplete="email" required />
        <div>
          <Field
            icon={Lock}
            name="password"
            type="password"
            placeholder="Create a password"
            autoComplete="new-password"
            required
          />
          <p className="mt-1.5 px-1 text-xs text-muted-foreground">
            At least 8 characters, with one uppercase letter and one number.
          </p>
        </div>

        {error && (
          <motion.p
            initial={{ opacity: 0, y: -4 }}
            animate={{ opacity: 1, y: 0 }}
            className="rounded-xl bg-destructive/10 px-4 py-2.5 text-sm text-destructive"
          >
            {error}
          </motion.p>
        )}

        {/* Consent gate. The button below stays disabled until this is ticked,
            and the server rejects the request outright without it — so the
            disabled state is a courtesy, not the enforcement. */}
        <label className="flex cursor-pointer items-start gap-3 rounded-xl border border-border/70 bg-secondary/40 p-3.5 text-left">
          <input
            type="checkbox"
            checked={acceptedTerms}
            onChange={(e) => setAcceptedTerms(e.target.checked)}
            className="mt-0.5 h-4 w-4 shrink-0 rounded border-input accent-primary"
          />
          <span className="text-[13px] leading-relaxed text-muted-foreground">
            I agree to the{" "}
            <Link
              href="/terms"
              target="_blank"
              onClick={(e) => e.stopPropagation()}
              className="font-medium text-primary underline-offset-4 hover:underline"
            >
              Terms of Use
            </Link>{" "}
            and{" "}
            <Link
              href="/privacy"
              target="_blank"
              onClick={(e) => e.stopPropagation()}
              className="font-medium text-primary underline-offset-4 hover:underline"
            >
              Privacy Policy
            </Link>
            . If you are under 18, please check with a parent or guardian first.
          </span>
        </label>

        <Button
          type="submit"
          size="lg"
          disabled={isPending || !acceptedTerms}
          className="h-12 w-full rounded-full text-[15px] shadow-soft"
        >
          {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Sparkles className="h-4 w-4" />}
          Create my account
        </Button>
      </form>

      {/* Stated next to the button rather than only on the screen after it.
          Someone who mistypes their address has already lost the account by the
          time a "check your inbox" page tells them the link matters — the
          warning has to arrive while the field is still in front of them. */}
      <p className="text-center text-xs leading-relaxed text-muted-foreground">
        Free to start. No credit card required. Use an address you can open now:{" "}
        <span className="font-medium text-foreground">
          your account stays inactive until you confirm it by email.
        </span>
      </p>
    </div>
  );
}

function Field({
  icon: Icon,
  ...props
}: { icon: typeof User } & React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <div className="relative">
      <Icon className="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
      <input
        {...props}
        className="h-12 w-full rounded-xl border-2 border-border/70 bg-card pl-11 pr-4 text-[15px] outline-none transition-colors placeholder:text-muted-foreground focus:border-primary"
      />
    </div>
  );
}

function PlanSummary({ profile }: { profile: OnboardingProfile }) {
  const rows = [
    profile.targetScore !== null && { k: "Target score", v: String(profile.targetScore) },
    profile.currentScore !== null && { k: "Starting from", v: String(profile.currentScore) },
    profile.satMonth && {
      k: "Test date",
      v: new Date(`${profile.satMonth}-01T00:00:00Z`).toLocaleDateString("en-US", {
        month: "long",
        year: "numeric",
        timeZone: "UTC",
      }),
    },
    profile.dailyGoalValue !== null && {
      k: "Daily goal",
      v: `${profile.dailyGoalValue} ${profile.dailyGoalType === "MINUTES" ? "min" : "questions"}`,
    },
    profile.dreamUniversities.length > 0 && {
      k: "Dream schools",
      v: `${profile.dreamUniversities.length} selected`,
    },
  ].filter(Boolean) as { k: string; v: string }[];

  if (rows.length === 0) return null;

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.1 }}
      className="overflow-hidden rounded-2xl border border-border/70 bg-card shadow-soft"
    >
      <div className="flex items-center gap-2 border-b border-border/60 bg-secondary/40 px-4 py-2.5">
        <GraduationCap className="h-4 w-4 text-primary" />
        <p className="text-[13px] font-semibold">Your study plan</p>
      </div>
      <dl className="divide-y divide-border/60">
        {rows.map((r) => (
          <div key={r.k} className="flex items-center justify-between px-4 py-2.5">
            <dt className="text-[13px] text-muted-foreground">{r.k}</dt>
            <dd className="flex items-center gap-1.5 text-[14px] font-semibold">
              <Check className="h-3.5 w-3.5 text-success" strokeWidth={3} />
              {r.v}
            </dd>
          </div>
        ))}
      </dl>
    </motion.div>
  );
}
