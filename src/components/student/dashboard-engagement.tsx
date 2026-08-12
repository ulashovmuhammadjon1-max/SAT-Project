import Link from "next/link";
import { ArrowRight, Award, CalendarDays, CheckCircle2, Trophy } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { AchievementMedal } from "@/components/student/achievement-tile";
import type { EarnedAchievement } from "@/lib/achievements/definitions";
import type { DailyChallenge } from "@/lib/daily-challenge";
import { cn } from "@/lib/utils";

/**
 * The daily challenge, on the dashboard.
 *
 * Deliberately the first thing with a call to action: it is one question, it
 * is the same one everybody else is doing today, and finishing it keeps the
 * streak alive. That combination is what brings someone back tomorrow.
 */
export function DashboardDailyCard({ daily }: { daily: DailyChallenge }) {
  const done = daily.answeredToday;

  return (
    <Card className={cn(done ? "border-emerald-500/40" : "border-primary/50 bg-primary/5")}>
      <CardContent className="flex flex-wrap items-center justify-between gap-4 p-6">
        <div className="min-w-0">
          {/* A div, not a p: Badge renders a div, and a div inside a p makes
              the browser close the paragraph early. React does not, so the
              server and client DOM disagree and hydration fails. */}
          <div className="flex items-center gap-2 text-sm font-medium">
            {done ? (
              <CheckCircle2 className="h-4 w-4 text-emerald-500" />
            ) : (
              <CalendarDays className="h-4 w-4 text-primary" />
            )}
            Daily Challenge
            <Badge variant="outline">
              {daily.subject === "MATH" ? "Math" : "Reading & Writing"}
            </Badge>
          </div>
          <p className="mt-1 text-sm text-muted-foreground">
            {done
              ? daily.answeredCorrectly
                ? "Solved today. A new one lands at midnight."
                : "Attempted today — check the explanation."
              : `One question on ${daily.skill}. Keeps your streak going.`}
            {daily.crowdAccuracyPct != null && ` ${daily.crowdAccuracyPct}% of students got it right.`}
          </p>
        </div>

        <div className="flex items-center gap-4">
          <div className="hidden gap-1 sm:flex">
            {daily.week.map((d, i) => (
              <span
                key={i}
                title={d.studied ? "studied" : "no activity"}
                className={cn(
                  "h-6 w-2.5 rounded-sm",
                  // A visible empty state: bg-muted on a dark surface is so close
                  // to the card that a rest day reads as a missing square.
                  d.studied ? "bg-primary" : "bg-muted-foreground/25",
                  d.isToday && "ring-1 ring-primary"
                )}
              />
            ))}
          </div>
          <Button variant={done ? "outline" : "default"} asChild>
            <Link href="/daily">
              {done ? "See it again" : "Solve today's"} <ArrowRight className="h-4 w-4" />
            </Link>
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}

/**
 * Recently earned badges plus the closest locked ones.
 *
 * Showing what is *nearly* earned is the part that does the work — a wall of
 * things already won is a trophy cabinet, while "42 of 50 questions to the
 * next one" is a reason to open the Question Bank now.
 */
export function DashboardAchievementsCard({
  unlocked,
  nextUp,
  unlockedCount,
  totalCount,
}: {
  unlocked: EarnedAchievement[];
  nextUp: EarnedAchievement[];
  unlockedCount: number;
  totalCount: number;
}) {
  const recent = unlocked.slice(-3).reverse();

  return (
    <Card>
      <CardContent className="space-y-4 p-6">
        <div className="flex items-center justify-between gap-3">
          <p className="flex items-center gap-2 text-sm font-medium">
            <Award className="h-4 w-4" /> Achievements
          </p>
          <span className="text-sm tabular-nums text-muted-foreground">
            {unlockedCount}/{totalCount}
          </span>
        </div>

        {recent.length > 0 && (
          <div className="flex flex-wrap gap-3">
            {recent.map((a) => (
              <div key={a.id} className="flex items-center gap-2">
                <AchievementMedal achievement={a} className="h-8 w-8" />
                <span className="text-xs">{a.title}</span>
              </div>
            ))}
          </div>
        )}

        {nextUp.length > 0 ? (
          <div className="space-y-2.5">
            <p className="text-xs uppercase tracking-wide text-muted-foreground">Closest to earning</p>
            {nextUp.map((a) => (
              <div key={a.id}>
                <div className="mb-1 flex items-baseline justify-between gap-2 text-xs">
                  <span className="truncate">{a.title}</span>
                  <span className="shrink-0 tabular-nums text-muted-foreground">
                    {a.currentValue.toLocaleString()}
                    {a.unit}/{a.target.toLocaleString()}
                    {a.unit}
                  </span>
                </div>
                <Progress value={a.progressPct} className="h-1" />
              </div>
            ))}
          </div>
        ) : (
          <p className="text-xs text-muted-foreground">
            Answer a few questions to start earning badges.
          </p>
        )}

        <Button variant="outline" size="sm" className="w-full" asChild>
          <Link href="/achievements">See all achievements</Link>
        </Button>
      </CardContent>
    </Card>
  );
}

/** This week's top students, with the reader's own position. */
export function DashboardLeaderboardCard({
  rows,
  myRank,
  participants,
}: {
  rows: { rank: number; displayName: string; value: number; isMe: boolean }[];
  myRank: number | null;
  participants: number;
}) {
  return (
    <Card>
      <CardContent className="space-y-4 p-6">
        <div className="flex items-center justify-between gap-3">
          <p className="flex items-center gap-2 text-sm font-medium">
            <Trophy className="h-4 w-4" /> This week
          </p>
          {myRank && (
            <span className="text-sm text-muted-foreground">
              you&apos;re <strong className="text-foreground tabular-nums">#{myRank}</strong> of{" "}
              {participants}
            </span>
          )}
        </div>

        {rows.length ? (
          <ol className="space-y-2">
            {rows.map((r) => (
              <li
                key={r.rank + r.displayName}
                className={cn("flex items-center gap-3 text-sm", r.isMe && "font-medium")}
              >
                <span className="w-5 shrink-0 text-center text-xs tabular-nums text-muted-foreground">
                  {r.rank}
                </span>
                <span className="min-w-0 flex-1 truncate">{r.displayName}</span>
                <span className="shrink-0 tabular-nums">{r.value}</span>
              </li>
            ))}
          </ol>
        ) : (
          <p className="text-xs text-muted-foreground">
            No questions answered yet this week — answer one and you top the board.
          </p>
        )}

        <Button variant="outline" size="sm" className="w-full" asChild>
          <Link href="/leaderboard">Full leaderboard</Link>
        </Button>
      </CardContent>
    </Card>
  );
}
