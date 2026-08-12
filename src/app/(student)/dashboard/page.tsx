import Link from "next/link";
import { ArrowRight, Clock, Target, TrendingUp } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { StatCard } from "@/components/student/stat-card";
import { PersonalizedHeader } from "@/components/student/personalized-header";
import {
  DashboardCoinsCard,
  DashboardPlanCard,
  DashboardSessionCard,
} from "@/components/student/dashboard-plan-card";
import {
  DashboardAchievementsCard,
  DashboardDailyCard,
  DashboardLeaderboardCard,
} from "@/components/student/dashboard-engagement";
import { ScoreTrendChart } from "@/components/charts/score-trend-chart";
import { getAchievements } from "@/lib/achievements/service";
import { getDailyChallenge } from "@/lib/daily-challenge";
import { getLeaderboard } from "@/lib/leaderboard";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { estimateScaledScore } from "@/lib/scoring/estimate";
import { getPlanSummary } from "@/lib/plan/service";
import { getSettings } from "@/lib/settings";
import { readProfile } from "@/lib/onboarding/profile";
import { asWeakArea } from "@/lib/validations/onboarding";
import { formatDuration } from "@/lib/utils";

export const metadata = { title: "Dashboard" };
export const dynamic = "force-dynamic";

export default async function DashboardPage() {
  const user = await requireUser();

  // Midnight UTC today — StudyActivity.date is a @db.Date, so this matches the
  // row for the current day without timezone drift.
  const todayUtc = new Date();
  todayUtc.setUTCHours(0, 0, 0, 0);

  const [
    inProgress,
    recentAttempts,
    responses,
    submittedAttempts,
    profile,
    todayActivity,
    planSummary,
    coinUser,
    upcomingSession,
    settings,
    daily,
    achievements,
    weeklyBoard,
  ] = await Promise.all([
    prisma.attempt.findFirst({
      where: { userId: user.id, status: { in: ["IN_PROGRESS", "PAUSED"] } },
      include: { test: true },
      orderBy: { updatedAt: "desc" },
    }),
    prisma.attempt.findMany({
      where: { userId: user.id },
      orderBy: { createdAt: "desc" },
      take: 5,
      include: { test: true },
    }),
    prisma.response.findMany({
      where: { attempt: { userId: user.id }, isCorrect: { not: null } },
      include: { question: { include: { domain: true } } },
    }),
    prisma.attempt.findMany({
      where: { userId: user.id, status: "SUBMITTED" },
      orderBy: { submittedAt: "asc" },
      select: { submittedAt: true, totalScaledScore: true, mathScaledScore: true, rwScaledScore: true },
    }),
    readProfile(user.id),
    prisma.studyActivity.findUnique({
      where: { userId_date: { userId: user.id, date: todayUtc } },
      select: { questionsAnswered: true, minutesStudied: true },
    }),
    getPlanSummary(user.id),
    prisma.user.findUnique({
      where: { id: user.id },
      select: { coinBalance: true },
    }),
    prisma.booking.findFirst({
      where: { userId: user.id, status: "UPCOMING" },
      orderBy: { slot: { startsAt: "asc" } },
      select: {
        meetingUrl: true,
        slot: { select: { startsAt: true, durationMinutes: true } },
      },
    }),
    getSettings(),
    getDailyChallenge(user.id),
    getAchievements(user.id),
    // Just the podium for the dashboard card; the full board is its own page.
    getLeaderboard("weekly", user.id, 3),
  ]);

  const totalAnswered = responses.length;
  const totalCorrect = responses.filter((r) => r.isCorrect).length;
  const accuracy = totalAnswered ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
  const avgTime = totalAnswered
    ? Math.round(responses.reduce((sum, r) => sum + r.timeSpentSeconds, 0) / totalAnswered)
    : 0;

  const rwResponses = responses.filter((r) => r.question.domain.subject === "READING_WRITING");
  const mathResponses = responses.filter((r) => r.question.domain.subject === "MATH");
  const rwAccuracy = rwResponses.length
    ? Math.round((rwResponses.filter((r) => r.isCorrect).length / rwResponses.length) * 100)
    : 0;
  const mathAccuracy = mathResponses.length
    ? Math.round((mathResponses.filter((r) => r.isCorrect).length / mathResponses.length) * 100)
    : 0;

  const latestFullLength = submittedAttempts.at(-1);
  const rwEstimate = latestFullLength?.rwScaledScore ?? (rwResponses.length ? estimateScaledScore(rwAccuracy, "READING_WRITING") : null);
  const mathEstimate =
    latestFullLength?.mathScaledScore ?? (mathResponses.length ? estimateScaledScore(mathAccuracy, "MATH") : null);
  const totalEstimate =
    latestFullLength?.totalScaledScore ?? (rwEstimate && mathEstimate ? rwEstimate + mathEstimate : null);

  const domainStats = new Map<string, { correct: number; total: number }>();
  for (const r of responses) {
    const key = r.question.domain.name;
    const bucket = domainStats.get(key) ?? { correct: 0, total: 0 };
    bucket.total += 1;
    if (r.isCorrect) bucket.correct += 1;
    domainStats.set(key, bucket);
  }
  const domainAccuracy = [...domainStats.entries()]
    .map(([domain, { correct, total }]) => ({ domain, accuracy: Math.round((correct / total) * 100), total }))
    .filter((d) => d.total >= 3)
    .sort((a, b) => a.accuracy - b.accuracy);
  const weakest = domainAccuracy.slice(0, 3);
  const strongest = [...domainAccuracy].reverse().slice(0, 3);

  const trend = submittedAttempts
    .filter((a) => a.totalScaledScore != null)
    .map((a, i) => ({ attempt: `#${i + 1}`, score: a.totalScaledScore as number }));

  return (
    <div className="space-y-8">
      <PersonalizedHeader
        firstName={user.name ? user.name.split(" ")[0] : ""}
        targetScore={profile?.targetScore ?? null}
        currentScore={profile?.currentScore ?? null}
        predictedScore={totalEstimate}
        satDate={profile?.satDate ?? null}
        gradeLevel={profile?.gradeLevel ?? null}
        weakestArea={asWeakArea(profile?.weakestArea)}
        dailyGoalType={profile?.dailyGoalType ?? null}
        dailyGoalValue={profile?.dailyGoalValue ?? null}
        todayQuestions={todayActivity?.questionsAnswered ?? 0}
        todayMinutes={todayActivity?.minutesStudied ?? 0}
        currentStreak={profile?.currentStreak ?? 0}
        weakestSkills={weakest.map((w) => w.domain)}
        onboarded={profile?.onboardedAt != null}
      />

      {daily && <DashboardDailyCard daily={daily} />}

      <DashboardPlanCard plan={planSummary} />

      <div className="grid gap-4 md:grid-cols-2">
        <DashboardAchievementsCard
          unlocked={achievements.unlocked}
          nextUp={achievements.nextUp}
          unlockedCount={achievements.unlockedCount}
          totalCount={achievements.totalCount}
        />
        <DashboardLeaderboardCard
          rows={weeklyBoard.rows}
          myRank={weeklyBoard.rows.find((r) => r.isMe)?.rank ?? weeklyBoard.me?.rank ?? null}
          participants={weeklyBoard.participants}
        />
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <DashboardCoinsCard
          balance={coinUser?.coinBalance ?? 0}
          referralReward={settings.referralRewardCoins}
        />
        {upcomingSession && (
          <DashboardSessionCard
            startsAt={upcomingSession.slot.startsAt}
            durationMinutes={upcomingSession.slot.durationMinutes}
            meetingUrl={upcomingSession.meetingUrl}
          />
        )}
      </div>

      {inProgress && (
        <Card className="border-primary/50 bg-primary-50/50">
          <CardContent className="flex flex-wrap items-center justify-between gap-4 p-6">
            <div>
              <p className="text-sm font-medium text-primary-700">Continue where you left off</p>
              <p className="font-display text-lg font-semibold">{inProgress.test.title}</p>
            </div>
            <Button asChild>
              <Link href={`/exam/${inProgress.id}`}>
                Resume test <ArrowRight className="h-4 w-4" />
              </Link>
            </Button>
          </CardContent>
        </Card>
      )}

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard label="Overall SAT estimate" value={totalEstimate ?? "—"} sublabel="out of 1600" icon={TrendingUp} />
        <StatCard label="Reading & Writing" value={rwEstimate ?? "—"} sublabel="out of 800" icon={Target} />
        <StatCard label="Math" value={mathEstimate ?? "—"} sublabel="out of 800" icon={Target} />
        <StatCard label="Avg. time / question" value={avgTime ? formatDuration(avgTime) : "—"} icon={Clock} />
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Score trend</CardTitle>
          </CardHeader>
          <CardContent>
            {trend.length > 1 ? (
              <ScoreTrendChart data={trend} />
            ) : (
              <p className="py-12 text-center text-sm text-muted-foreground">
                Complete full-length practice tests to see your score trend here.
              </p>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Accuracy</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="text-center">
              <p className="font-display text-4xl font-semibold">{accuracy}%</p>
              <p className="text-sm text-muted-foreground">{totalAnswered} questions answered</p>
            </div>
            <Progress value={accuracy} />
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Weakest topics</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            {weakest.length === 0 && <p className="text-sm text-muted-foreground">Not enough data yet.</p>}
            {weakest.map((d) => (
              <div key={d.domain} className="flex items-center justify-between">
                <span className="text-sm">{d.domain}</span>
                <Badge variant="destructive">{d.accuracy}%</Badge>
              </div>
            ))}
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Strongest topics</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            {strongest.length === 0 && <p className="text-sm text-muted-foreground">Not enough data yet.</p>}
            {strongest.map((d) => (
              <div key={d.domain} className="flex items-center justify-between">
                <span className="text-sm">{d.domain}</span>
                <Badge variant="success">{d.accuracy}%</Badge>
              </div>
            ))}
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Recent activity</CardTitle>
        </CardHeader>
        <CardContent className="space-y-2">
          {recentAttempts.length === 0 && (
            <p className="text-sm text-muted-foreground">
              No attempts yet.{" "}
              <Link href="/tests" className="text-primary hover:underline">
                Start a practice test
              </Link>
              .
            </p>
          )}
          {recentAttempts.map((attempt) => (
            <div key={attempt.id} className="flex items-center justify-between rounded-lg border border-border p-3">
              <div>
                <p className="text-sm font-medium">{attempt.test.title}</p>
                <p className="text-xs text-muted-foreground">
                  {attempt.createdAt.toLocaleDateString()} · {attempt.status.replace("_", " ")}
                </p>
              </div>
              {attempt.totalScaledScore != null && <Badge variant="outline">{attempt.totalScaledScore}</Badge>}
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
}
