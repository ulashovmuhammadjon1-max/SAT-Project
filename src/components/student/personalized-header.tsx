import Link from "next/link";
import { ArrowRight, CalendarDays, Flame, Target, TrendingUp } from "lucide-react";

import { Progress } from "@/components/ui/progress";
import { cn } from "@/lib/utils";
import { GRADE_LABELS, SECTION_LABELS } from "@/lib/validations/onboarding";

export interface PersonalizedHeaderProps {
  firstName: string;
  targetScore: number | null;
  currentScore: number | null;
  predictedScore: number | null;
  satDate: Date | null;
  gradeLevel: keyof typeof GRADE_LABELS | null;
  weakestArea: keyof typeof SECTION_LABELS | null;
  dailyGoalType: "QUESTIONS" | "MINUTES" | null;
  dailyGoalValue: number | null;
  todayQuestions: number;
  todayMinutes: number;
  currentStreak: number;
  weakestSkills: string[];
  onboarded: boolean;
}

function daysUntil(date: Date): number {
  const today = new Date();
  const a = Date.UTC(today.getUTCFullYear(), today.getUTCMonth(), today.getUTCDate());
  const b = Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate());
  return Math.round((b - a) / 86_400_000);
}

export function PersonalizedHeader({
  firstName,
  targetScore,
  currentScore,
  predictedScore,
  satDate,
  gradeLevel,
  weakestArea,
  dailyGoalType,
  dailyGoalValue,
  todayQuestions,
  todayMinutes,
  currentStreak,
  weakestSkills,
  onboarded,
}: PersonalizedHeaderProps) {
  const goalDone = dailyGoalType === "MINUTES" ? todayMinutes : todayQuestions;
  const goalPct = dailyGoalValue ? Math.min(100, Math.round((goalDone / dailyGoalValue) * 100)) : 0;
  const goalMet = dailyGoalValue !== null && goalDone >= dailyGoalValue;

  const daysLeft = satDate ? daysUntil(satDate) : null;
  const gapToTarget = targetScore !== null && predictedScore !== null ? targetScore - predictedScore : null;

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight sm:text-3xl">
            Welcome back{firstName ? `, ${firstName}` : ""}
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {goalMet
              ? "Today's goal is done — anything else is a bonus."
              : dailyGoalValue !== null
                ? `${Math.max(dailyGoalValue - goalDone, 0)} ${
                    dailyGoalType === "MINUTES" ? "minutes" : "questions"
                  } left to hit today's goal.`
                : "Here's where your prep stands today."}
          </p>
        </div>

        {currentStreak > 0 && (
          <span className="flex items-center gap-1.5 rounded-full bg-warning/10 px-3 py-1.5 text-sm font-semibold text-warning-foreground">
            <Flame className="h-4 w-4 text-warning" />
            {currentStreak}-day streak
          </span>
        )}
      </div>

      {!onboarded && (
        <div className="flex flex-wrap items-center justify-between gap-3 rounded-xl border border-primary/40 bg-primary-50/60 px-5 py-4">
          <div>
            <p className="text-sm font-semibold text-primary-700">Finish setting up your study plan</p>
            <p className="text-sm text-muted-foreground">
              Tell us your target score and test date and this dashboard gets a lot more useful.
            </p>
          </div>
          <Link
            href="/settings"
            className="flex items-center gap-1 text-sm font-semibold text-primary hover:underline"
          >
            Set it up <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </div>
      )}

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {/* Target vs predicted */}
        <div className="rounded-xl border border-border bg-card p-5 shadow-soft">
          <div className="flex items-center gap-2 text-muted-foreground">
            <Target className="h-4 w-4" />
            <p className="text-xs font-medium uppercase tracking-wide">Target score</p>
          </div>
          <p className="mt-2 font-display text-3xl font-semibold tracking-tight">
            {targetScore ?? "—"}
          </p>
          {gapToTarget !== null && (
            <p
              className={cn(
                "mt-1 text-xs font-medium",
                gapToTarget > 0 ? "text-muted-foreground" : "text-success"
              )}
            >
              {gapToTarget > 0 ? `${gapToTarget} points to go` : "Target reached — hold it steady"}
            </p>
          )}
        </div>

        {/* Predicted */}
        <div className="rounded-xl border border-border bg-card p-5 shadow-soft">
          <div className="flex items-center gap-2 text-muted-foreground">
            <TrendingUp className="h-4 w-4" />
            <p className="text-xs font-medium uppercase tracking-wide">Predicted score</p>
          </div>
          <p className="mt-2 font-display text-3xl font-semibold tracking-tight text-primary">
            {predictedScore ?? "—"}
          </p>
          <p className="mt-1 text-xs text-muted-foreground">
            {currentScore !== null ? `Started at ${currentScore}` : "From your practice so far"}
          </p>
        </div>

        {/* Exam countdown */}
        <div className="rounded-xl border border-border bg-card p-5 shadow-soft">
          <div className="flex items-center gap-2 text-muted-foreground">
            <CalendarDays className="h-4 w-4" />
            <p className="text-xs font-medium uppercase tracking-wide">Your SAT</p>
          </div>
          {satDate ? (
            <>
              <p className="mt-2 font-display text-3xl font-semibold tracking-tight">
                {daysLeft !== null && daysLeft >= 0 ? daysLeft : "—"}
                <span className="ml-1 text-base font-medium text-muted-foreground">
                  {daysLeft === 1 ? "day" : "days"}
                </span>
              </p>
              <p className="mt-1 text-xs text-muted-foreground">
                {satDate.toLocaleDateString("en-US", { month: "long", year: "numeric", timeZone: "UTC" })}
              </p>
            </>
          ) : (
            <>
              <p className="mt-2 font-display text-3xl font-semibold tracking-tight">—</p>
              <p className="mt-1 text-xs text-muted-foreground">No date set</p>
            </>
          )}
        </div>

        {/* Today's goal */}
        <div className="rounded-xl border border-border bg-card p-5 shadow-soft">
          <div className="flex items-center gap-2 text-muted-foreground">
            <Flame className="h-4 w-4" />
            <p className="text-xs font-medium uppercase tracking-wide">Today&apos;s goal</p>
          </div>
          {dailyGoalValue !== null ? (
            <>
              <p className="mt-2 font-display text-3xl font-semibold tracking-tight">
                {goalDone}
                <span className="text-base font-medium text-muted-foreground">/{dailyGoalValue}</span>
              </p>
              <Progress value={goalPct} className="mt-2 h-1.5" />
              <p className="mt-1.5 text-xs text-muted-foreground">
                {dailyGoalType === "MINUTES" ? "minutes studied" : "questions answered"}
              </p>
            </>
          ) : (
            <>
              <p className="mt-2 font-display text-3xl font-semibold tracking-tight">—</p>
              <p className="mt-1 text-xs text-muted-foreground">No daily goal set</p>
            </>
          )}
        </div>
      </div>

      {(weakestSkills.length > 0 || weakestArea || gradeLevel) && (
        <div className="flex flex-wrap items-center gap-x-6 gap-y-2 rounded-xl border border-border bg-secondary/30 px-5 py-3.5">
          {weakestSkills.length > 0 ? (
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
                Focus next
              </span>
              {weakestSkills.map((s) => (
                <span key={s} className="rounded-full bg-destructive/10 px-2.5 py-1 text-xs font-medium text-destructive">
                  {s}
                </span>
              ))}
            </div>
          ) : (
            weakestArea && (
              <div className="flex items-center gap-2">
                <span className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
                  You told us
                </span>
                <span className="rounded-full bg-destructive/10 px-2.5 py-1 text-xs font-medium text-destructive">
                  {SECTION_LABELS[weakestArea]}
                </span>
              </div>
            )
          )}

          {gradeLevel && (
            <span className="ml-auto text-xs text-muted-foreground">{GRADE_LABELS[gradeLevel]}</span>
          )}
        </div>
      )}
    </div>
  );
}
