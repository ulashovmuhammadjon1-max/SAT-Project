import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DomainAccuracyChart } from "@/components/charts/domain-accuracy-chart";
import { AudienceBarChart, CountryPieChart } from "@/components/charts/audience-charts";
import { prisma } from "@/lib/prisma";
import { countryByCode } from "@/lib/data/countries";
import { GRADE_LABELS } from "@/lib/validations/onboarding";

export const metadata = { title: "Analytics" };
export const dynamic = "force-dynamic";

/** Ordered so the grade chart reads 9 → 12 → beyond rather than alphabetically. */
const GRADE_ORDER = ["GRADE_9", "GRADE_10", "GRADE_11", "GRADE_12", "GAP_YEAR", "COLLEGE", "OTHER"] as const;

export default async function AdminAnalyticsPage() {
  const [totalAttempts, submittedAttempts, responses, students, scoreAgg, studyAgg] = await Promise.all([
    prisma.attempt.count(),
    prisma.attempt.count({ where: { status: "SUBMITTED" } }),
    prisma.response.findMany({
      where: { isCorrect: { not: null } },
      include: { question: { include: { domain: true } } },
      take: 5000,
    }),
    prisma.user.findMany({
      where: { role: "STUDENT" },
      select: {
        countryCode: true,
        gradeLevel: true,
        dreamUniversities: true,
        satDate: true,
        onboardedAt: true,
      },
    }),
    prisma.user.aggregate({
      where: { role: "STUDENT" },
      _avg: { targetScore: true, currentScore: true },
      _count: { targetScore: true, currentScore: true },
    }),
    prisma.user.aggregate({
      where: { role: "STUDENT" },
      _avg: { studyMinutesPerDay: true },
      _count: { studyMinutesPerDay: true },
    }),
  ]);

  /* ---- existing platform performance ------------------------------------ */
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

  /* ---- audience composition --------------------------------------------- */
  const onboardedCount = students.filter((s) => s.onboardedAt != null).length;

  const countryCounts = new Map<string, number>();
  for (const s of students) {
    if (!s.countryCode) continue;
    countryCounts.set(s.countryCode, (countryCounts.get(s.countryCode) ?? 0) + 1);
  }
  const countriesRanked = [...countryCounts.entries()]
    .map(([code, value]) => ({
      code,
      name: countryByCode(code)?.name ?? code,
      flag: countryByCode(code)?.flag ?? "🏳️",
      value,
    }))
    .sort((a, b) => b.value - a.value);

  // The pie stays readable at ~8 slices; everything else rolls into "Other".
  const TOP_SLICES = 8;
  const countryPie = [
    ...countriesRanked.slice(0, TOP_SLICES).map((c) => ({ name: c.name, value: c.value })),
    ...(countriesRanked.length > TOP_SLICES
      ? [{ name: "Other", value: countriesRanked.slice(TOP_SLICES).reduce((sum, c) => sum + c.value, 0) }]
      : []),
  ];

  const gradeCounts = new Map<string, number>();
  for (const s of students) {
    if (!s.gradeLevel) continue;
    gradeCounts.set(s.gradeLevel, (gradeCounts.get(s.gradeLevel) ?? 0) + 1);
  }
  const gradeData = GRADE_ORDER.filter((g) => gradeCounts.has(g)).map((g) => ({
    name: GRADE_LABELS[g],
    value: gradeCounts.get(g) ?? 0,
  }));

  const uniCounts = new Map<string, number>();
  for (const s of students) {
    for (const u of s.dreamUniversities) {
      uniCounts.set(u, (uniCounts.get(u) ?? 0) + 1);
    }
  }
  const topUniversities = [...uniCounts.entries()]
    .map(([name, value]) => ({ name, value }))
    .sort((a, b) => b.value - a.value)
    .slice(0, 10);

  // Upcoming test dates, grouped by month, future only.
  const now = new Date();
  const startOfMonth = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), 1));
  const satMonthCounts = new Map<string, number>();
  for (const s of students) {
    if (!s.satDate || s.satDate < startOfMonth) continue;
    const key = `${s.satDate.getUTCFullYear()}-${String(s.satDate.getUTCMonth() + 1).padStart(2, "0")}`;
    satMonthCounts.set(key, (satMonthCounts.get(key) ?? 0) + 1);
  }
  const satDateData = [...satMonthCounts.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .slice(0, 12)
    .map(([key, value]) => ({
      name: new Date(`${key}-01T00:00:00Z`).toLocaleDateString("en-US", {
        month: "short",
        year: "2-digit",
        timeZone: "UTC",
      }),
      value,
    }));

  const avgTarget = scoreAgg._avg.targetScore;
  const avgCurrent = scoreAgg._avg.currentScore;
  const avgStudy = studyAgg._avg.studyMinutesPerDay;

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Analytics</h1>
        <p className="text-sm text-muted-foreground">Platform performance and audience composition.</p>
      </div>

      {/* ---- Audience ------------------------------------------------------ */}
      <section className="space-y-4">
        <h2 className="font-display text-lg font-semibold tracking-tight">Audience</h2>

        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
          <MetricCard label="Students" value={students.length} />
          <MetricCard
            label="Completed onboarding"
            value={onboardedCount}
            sub={students.length ? `${Math.round((onboardedCount / students.length) * 100)}% of students` : undefined}
          />
          <MetricCard
            label="Avg. target score"
            value={avgTarget ? Math.round(avgTarget) : "—"}
            sub={`${scoreAgg._count.targetScore} reported`}
          />
          <MetricCard
            label="Avg. current score"
            value={avgCurrent ? Math.round(avgCurrent) : "—"}
            sub={`${scoreAgg._count.currentScore} reported`}
          />
          <MetricCard
            label="Avg. study time"
            value={avgStudy ? `${Math.round(avgStudy)} min` : "—"}
            sub={`${studyAgg._count.studyMinutesPerDay} reported · per day`}
          />
        </div>

        <div className="grid gap-4 lg:grid-cols-2">
          <Card>
            <CardHeader>
              <CardTitle>Users by country</CardTitle>
            </CardHeader>
            <CardContent>
              {countryPie.length > 0 ? (
                <CountryPieChart data={countryPie} />
              ) : (
                <EmptyNote>No students have selected a country yet.</EmptyNote>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Country breakdown</CardTitle>
            </CardHeader>
            <CardContent>
              {countriesRanked.length > 0 ? (
                <ul className="max-h-[300px] space-y-1 overflow-y-auto">
                  {countriesRanked.map((c) => {
                    const pct = Math.round((c.value / (students.length || 1)) * 100);
                    return (
                      <li key={c.code} className="flex items-center gap-3 rounded-lg px-2 py-1.5 hover:bg-secondary/50">
                        <span className="text-lg leading-none">{c.flag}</span>
                        <span className="flex-1 truncate text-sm">{c.name}</span>
                        <div className="hidden h-1.5 w-24 overflow-hidden rounded-full bg-secondary sm:block">
                          <div className="h-full rounded-full bg-primary" style={{ width: `${pct}%` }} />
                        </div>
                        <span className="w-10 text-right text-sm font-semibold tabular-nums">{c.value}</span>
                      </li>
                    );
                  })}
                </ul>
              ) : (
                <EmptyNote>No country data yet.</EmptyNote>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Users by grade</CardTitle>
            </CardHeader>
            <CardContent>
              {gradeData.length > 0 ? (
                <AudienceBarChart data={gradeData} unit="students" />
              ) : (
                <EmptyNote>No grade data yet.</EmptyNote>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Upcoming SAT dates</CardTitle>
            </CardHeader>
            <CardContent>
              {satDateData.length > 0 ? (
                <AudienceBarChart data={satDateData} color="hsl(266 84% 60%)" unit="students" />
              ) : (
                <EmptyNote>No upcoming test dates recorded.</EmptyNote>
              )}
            </CardContent>
          </Card>

          <Card className="lg:col-span-2">
            <CardHeader>
              <CardTitle>Most popular dream universities</CardTitle>
            </CardHeader>
            <CardContent>
              {topUniversities.length > 0 ? (
                <AudienceBarChart data={topUniversities} color="hsl(152 60% 40%)" unit="students" horizontal />
              ) : (
                <EmptyNote>No universities selected yet.</EmptyNote>
              )}
            </CardContent>
          </Card>
        </div>
      </section>

      {/* ---- Performance --------------------------------------------------- */}
      <section className="space-y-4">
        <h2 className="font-display text-lg font-semibold tracking-tight">Performance</h2>

        <div className="grid gap-4 sm:grid-cols-3">
          <MetricCard label="Total attempts" value={totalAttempts} />
          <MetricCard label="Submitted attempts" value={submittedAttempts} />
          <MetricCard label="Completion rate" value={`${completionRate}%`} />
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Accuracy by domain</CardTitle>
          </CardHeader>
          <CardContent>
            {chartData.length > 0 ? (
              <DomainAccuracyChart data={chartData} />
            ) : (
              <EmptyNote>No responses recorded yet.</EmptyNote>
            )}
          </CardContent>
        </Card>
      </section>
    </div>
  );
}

function MetricCard({
  label,
  value,
  sub,
}: {
  label: string;
  value: string | number;
  sub?: string;
}) {
  return (
    <Card>
      <CardHeader className="pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">{label}</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="font-display text-3xl font-semibold tracking-tight">{value}</p>
        {sub && <p className="mt-0.5 text-xs text-muted-foreground">{sub}</p>}
      </CardContent>
    </Card>
  );
}

function EmptyNote({ children }: { children: React.ReactNode }) {
  return <p className="py-10 text-center text-sm text-muted-foreground">{children}</p>;
}
