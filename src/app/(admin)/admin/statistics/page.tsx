import Link from "next/link";
import { AlertTriangle, CheckCircle2, TrendingUp, Users } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DistributionChart, TrendAreaChart } from "@/components/charts/trend-chart";
import { getAdminStatistics, type QuestionOutlier } from "@/lib/admin/statistics";
import { cn } from "@/lib/utils";

export const metadata = { title: "Statistics" };
export const dynamic = "force-dynamic";

export default async function AdminStatisticsPage() {
  const stats = await getAdminStatistics();

  const completed = stats.funnel.at(-1)?.count ?? 0;
  const signedUp = stats.funnel[0]?.count ?? 0;

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Statistics</h1>
        <p className="text-sm text-muted-foreground">
          How the platform is being used, and which questions are behaving oddly.
        </p>
      </div>

      {/* ---- headline numbers ------------------------------------------- */}
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Metric icon={Users} label="Students" value={signedUp} sub="accounts created" />
        <Metric
          icon={TrendingUp}
          label="Active this week"
          value={stats.activeLast7}
          sub={`${stats.activeLast30} in the last 30 days`}
        />
        <Metric
          icon={CheckCircle2}
          label="Questions answered"
          value={stats.questionsAnsweredAllTime}
          sub="all time, across the platform"
        />
        <Metric
          icon={TrendingUp}
          label="Average score"
          value={stats.averageTotalScore ?? "—"}
          sub={completed ? `over ${completed} completed test${completed === 1 ? "" : "s"}` : "no completed tests yet"}
        />
      </div>

      {/* ---- funnel ------------------------------------------------------ */}
      <Card>
        <CardHeader>
          <CardTitle>From signup to a finished test</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <p className="-mt-2 text-sm text-muted-foreground">
            Each row counts <strong>distinct students</strong>, so someone who has taken six tests
            counts once. The gap between two rows is where people are dropping out.
          </p>
          {stats.funnel.map((step) => (
            <div key={step.label} className="space-y-1">
              <div className="flex items-baseline justify-between gap-3 text-sm">
                <span className="font-medium">{step.label}</span>
                <span className="tabular-nums text-muted-foreground">
                  {step.count} · {step.pctOfTop}%
                </span>
              </div>
              <div className="h-2 overflow-hidden rounded-full bg-secondary">
                <div className="h-full rounded-full bg-primary" style={{ width: `${step.pctOfTop}%` }} />
              </div>
              <p className="text-xs text-muted-foreground">{step.note}</p>
            </div>
          ))}
        </CardContent>
      </Card>

      {/* ---- trends ------------------------------------------------------ */}
      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>New students, last 12 weeks</CardTitle>
          </CardHeader>
          <CardContent>
            {stats.signupsByWeek.length ? (
              <TrendAreaChart data={stats.signupsByWeek} unitLabel="students" />
            ) : (
              <Empty>No signups in the last twelve weeks.</Empty>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Questions answered, last 30 days</CardTitle>
          </CardHeader>
          <CardContent>
            {stats.activityByDay.length ? (
              <TrendAreaChart data={stats.activityByDay} unitLabel="questions" />
            ) : (
              <Empty>Nobody has answered a question in the last thirty days.</Empty>
            )}
          </CardContent>
        </Card>
      </div>

      {/* ---- scores ------------------------------------------------------ */}
      <Card>
        <CardHeader>
          <CardTitle>Score distribution</CardTitle>
        </CardHeader>
        <CardContent>
          {stats.scoreDistribution.some((b) => b.value > 0) ? (
            <DistributionChart data={stats.scoreDistribution} unitLabel="tests" />
          ) : (
            <Empty>No completed tests to score yet.</Empty>
          )}
        </CardContent>
      </Card>

      {/* ---- per-test uptake --------------------------------------------- */}
      <Card>
        <CardHeader>
          <CardTitle>Tests by uptake</CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          {stats.testUsage.length ? (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead className="border-b bg-secondary/40 text-left text-xs uppercase tracking-wide text-muted-foreground">
                  <tr>
                    <Th className="pl-6">Test</Th>
                    <Th right>Started</Th>
                    <Th right>Completed</Th>
                    <Th right>Completion</Th>
                    <Th right className="pr-6">Avg score</Th>
                  </tr>
                </thead>
                <tbody>
                  {stats.testUsage.map((row) => (
                    <tr key={row.title} className="border-b last:border-0">
                      <Td className="pl-6 font-medium">{row.title}</Td>
                      <Td right>{row.started}</Td>
                      <Td right>{row.completed}</Td>
                      <Td right>{row.completionPct}%</Td>
                      <Td right className="pr-6">{row.averageScore ?? "—"}</Td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="p-6">
              <Empty>No test has been started yet.</Empty>
            </div>
          )}
        </CardContent>
      </Card>

      {/* ---- content QA --------------------------------------------------- */}
      <div className="grid gap-4 xl:grid-cols-2">
        <OutlierTable
          title="Hardest questions"
          blurb="A question almost nobody gets right is usually broken — a wrong key, an ambiguous stem, a missing figure — rather than genuinely difficult. Worth reading before assuming it is hard."
          rows={stats.hardest}
          tone="hard"
        />
        <OutlierTable
          title="Easiest questions"
          blurb="A question everybody gets right is not testing anything. Often the distractors are implausible or the answer is given away by the stem."
          rows={stats.easiest}
          tone="easy"
        />
      </div>

      <p className="text-xs text-muted-foreground">
        Outlier tables only include questions answered at least 5 times — below that a question
        sits at 0% or 100% by chance, and a table of noise is worse than no table. Answers from
        the Question Bank and from full tests are pooled, because a defective question is
        defective in both.
      </p>
    </div>
  );
}

function OutlierTable({
  title,
  blurb,
  rows,
  tone,
}: {
  title: string;
  blurb: string;
  rows: QuestionOutlier[];
  tone: "hard" | "easy";
}) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          {tone === "hard" ? (
            <AlertTriangle className="h-4 w-4 text-amber-500" />
          ) : (
            <CheckCircle2 className="h-4 w-4 text-emerald-500" />
          )}
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        <p className="-mt-2 text-sm text-muted-foreground">{blurb}</p>
        {rows.length ? (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="border-b text-left text-xs uppercase tracking-wide text-muted-foreground">
                <tr>
                  <Th>Question</Th>
                  <Th>Where</Th>
                  <Th right>Answers</Th>
                  <Th right>Correct</Th>
                </tr>
              </thead>
              <tbody>
                {rows.map((r) => (
                  <tr key={r.questionId} className="border-b last:border-0">
                    <Td>
                      <Link
                        href={`/admin/questions/${r.questionId}`}
                        className="font-medium text-primary underline-offset-4 hover:underline"
                      >
                        {r.ref}
                      </Link>
                      <span className="block text-xs text-muted-foreground">
                        {r.domain} · {r.skill}
                      </span>
                    </Td>
                    <Td>
                      <span className="text-xs">
                        {r.testTitle} · {r.moduleLabel} Q{r.order}
                      </span>
                    </Td>
                    <Td right>{r.attempts}</Td>
                    <Td right>
                      <span
                        className={cn(
                          "font-semibold tabular-nums",
                          r.accuracyPct <= 25 && "text-destructive",
                          r.accuracyPct >= 95 && "text-emerald-500"
                        )}
                      >
                        {r.accuracyPct}%
                      </span>
                    </Td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <Empty>Not enough answers yet to tell a hard question from an unlucky one.</Empty>
        )}
      </CardContent>
    </Card>
  );
}

function Metric({
  icon: Icon,
  label,
  value,
  sub,
}: {
  icon: typeof Users;
  label: string;
  value: number | string;
  sub: string;
}) {
  return (
    <Card>
      <CardContent className="space-y-1 p-4">
        <div className="flex items-center gap-2 text-muted-foreground">
          <Icon className="h-4 w-4" />
          <span className="text-xs font-medium uppercase tracking-wide">{label}</span>
        </div>
        <p className="font-display text-2xl font-semibold tabular-nums">{value}</p>
        <p className="text-xs text-muted-foreground">{sub}</p>
      </CardContent>
    </Card>
  );
}

function Th({
  children,
  right,
  className,
}: {
  children: React.ReactNode;
  right?: boolean;
  className?: string;
}) {
  return <th className={cn("px-3 py-2 font-medium", right && "text-right", className)}>{children}</th>;
}

function Td({
  children,
  right,
  className,
}: {
  children: React.ReactNode;
  right?: boolean;
  className?: string;
}) {
  return <td className={cn("px-3 py-2", right && "text-right tabular-nums", className)}>{children}</td>;
}

function Empty({ children }: { children: React.ReactNode }) {
  return <p className="py-6 text-center text-sm text-muted-foreground">{children}</p>;
}
