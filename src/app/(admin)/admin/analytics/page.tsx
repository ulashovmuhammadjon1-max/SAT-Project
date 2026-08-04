import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DomainAccuracyChart } from "@/components/charts/domain-accuracy-chart";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Analytics" };
export const dynamic = "force-dynamic";

export default async function AdminAnalyticsPage() {
  const [totalAttempts, submittedAttempts, responses] = await Promise.all([
    prisma.attempt.count(),
    prisma.attempt.count({ where: { status: "SUBMITTED" } }),
    prisma.response.findMany({
      where: { isCorrect: { not: null } },
      include: { question: { include: { domain: true } } },
      take: 5000,
    }),
  ]);

  const byDomain = new Map<string, { correct: number; total: number }>();
  for (const r of responses) {
    const key = r.question.domain.name;
    const bucket = byDomain.get(key) ?? { correct: 0, total: 0 };
    bucket.total += 1;
    if (r.isCorrect) bucket.correct += 1;
    byDomain.set(key, bucket);
  }

  const chartData = [...byDomain.entries()].map(([domain, { correct, total }]) => ({
    domain,
    accuracy: total ? Math.round((correct / total) * 100) : 0,
  }));

  const completionRate = totalAttempts ? Math.round((submittedAttempts / totalAttempts) * 100) : 0;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Analytics</h1>
        <p className="text-sm text-muted-foreground">Platform-wide performance signals.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm text-muted-foreground">Total attempts</CardTitle>
          </CardHeader>
          <CardContent className="font-display text-3xl font-semibold">{totalAttempts}</CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm text-muted-foreground">Submitted attempts</CardTitle>
          </CardHeader>
          <CardContent className="font-display text-3xl font-semibold">{submittedAttempts}</CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm text-muted-foreground">Completion rate</CardTitle>
          </CardHeader>
          <CardContent className="font-display text-3xl font-semibold">{completionRate}%</CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Accuracy by domain</CardTitle>
        </CardHeader>
        <CardContent>
          {chartData.length > 0 ? (
            <DomainAccuracyChart data={chartData} />
          ) : (
            <p className="text-sm text-muted-foreground">No responses recorded yet.</p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
