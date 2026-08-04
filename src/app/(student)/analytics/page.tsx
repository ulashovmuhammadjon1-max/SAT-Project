import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DomainAccuracyChart } from "@/components/charts/domain-accuracy-chart";
import { ScoreTrendChart } from "@/components/charts/score-trend-chart";
import { StatCard } from "@/components/student/stat-card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { formatDuration } from "@/lib/utils";
import { Clock, Target, TrendingUp } from "lucide-react";

export const metadata = { title: "Analytics" };
export const dynamic = "force-dynamic";

export default async function StudentAnalyticsPage() {
  const user = await requireUser();

  const [responses, submittedAttempts] = await Promise.all([
    prisma.response.findMany({
      where: { attempt: { userId: user.id }, isCorrect: { not: null } },
      include: { question: { include: { domain: true } } },
    }),
    prisma.attempt.findMany({
      where: { userId: user.id, status: "SUBMITTED" },
      orderBy: { submittedAt: "asc" },
      select: { totalScaledScore: true },
    }),
  ]);

  const totalAnswered = responses.length;
  const totalCorrect = responses.filter((r) => r.isCorrect).length;
  const accuracy = totalAnswered ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
  const avgTime = totalAnswered
    ? Math.round(responses.reduce((sum, r) => sum + r.timeSpentSeconds, 0) / totalAnswered)
    : 0;

  const domainStats = new Map<string, { correct: number; total: number }>();
  for (const r of responses) {
    const key = r.question.domain.name;
    const bucket = domainStats.get(key) ?? { correct: 0, total: 0 };
    bucket.total += 1;
    if (r.isCorrect) bucket.correct += 1;
    domainStats.set(key, bucket);
  }
  const chartData = [...domainStats.entries()].map(([domain, { correct, total }]) => ({
    domain,
    accuracy: Math.round((correct / total) * 100),
  }));

  const trend = submittedAttempts
    .filter((a) => a.totalScaledScore != null)
    .map((a, i) => ({ attempt: `#${i + 1}`, score: a.totalScaledScore as number }));

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Analytics</h1>
        <p className="text-sm text-muted-foreground">A closer look at your performance.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <StatCard label="Accuracy" value={`${accuracy}%`} icon={Target} />
        <StatCard label="Avg. time / question" value={avgTime ? formatDuration(avgTime) : "—"} icon={Clock} />
        <StatCard label="Full tests completed" value={submittedAttempts.length} icon={TrendingUp} />
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Score trend</CardTitle>
        </CardHeader>
        <CardContent>
          {trend.length > 1 ? (
            <ScoreTrendChart data={trend} />
          ) : (
            <p className="py-8 text-center text-sm text-muted-foreground">Complete more full tests to see a trend.</p>
          )}
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Accuracy by domain</CardTitle>
        </CardHeader>
        <CardContent>
          {chartData.length > 0 ? (
            <DomainAccuracyChart data={chartData} />
          ) : (
            <p className="py-8 text-center text-sm text-muted-foreground">Answer some questions to see this chart.</p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
