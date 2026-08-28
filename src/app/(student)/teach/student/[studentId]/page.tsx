import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, Flame, Target } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getStudentDetail } from "@/server/actions/teacher/classes";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Student Detail" };
export const dynamic = "force-dynamic";

const pct = (correct: number, total: number) => (total === 0 ? 0 : Math.round((correct / total) * 100));

export default async function TeachStudentPage({ params }: { params: { studentId: string } }) {
  await requireUser();
  const s = await getStudentDetail(params.studentId);
  // Covers both "no such student" and "not in one of your classes" — a teacher
  // must never be able to open a student they don't teach.
  if (!s) notFound();

  return (
    <div className="space-y-6">
      <Link
        href="/teach"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" /> Teacher panel
      </Link>

      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">{s.name ?? s.email}</h1>
          <p className="text-sm text-muted-foreground">
            {s.email} · on Scholarly since{" "}
            {s.createdAt.toLocaleDateString(undefined, { month: "short", year: "numeric" })}
            {s.lastActive &&
              ` · last practised ${s.lastActive.toLocaleDateString(undefined, { month: "short", day: "numeric" })}`}
          </p>
        </div>
        <div className="flex gap-4 text-sm">
          <span className="flex items-center gap-1.5">
            <Flame className="h-4 w-4 text-warning" /> {s.currentStreak}-day streak
          </span>
          {s.targetScore && (
            <span className="flex items-center gap-1.5">
              <Target className="h-4 w-4 text-primary" /> target {s.targetScore}
            </span>
          )}
        </div>
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm">Totals</CardTitle>
          </CardHeader>
          <CardContent className="space-y-1 text-sm">
            <p>
              <span className="text-2xl font-semibold tabular-nums">{s.questionsAnswered.toLocaleString()}</span>{" "}
              <span className="text-muted-foreground">questions answered</span>
            </p>
            <p>
              <span className="text-2xl font-semibold tabular-nums">{s.attempts.length}</span>{" "}
              <span className="text-muted-foreground">tests submitted</span>
            </p>
            {s.satDate && (
              <p className="text-muted-foreground">
                SAT date: {s.satDate.toLocaleDateString(undefined, { month: "long", year: "numeric" })}
              </p>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm">Last 4 weeks</CardTitle>
          </CardHeader>
          <CardContent className="space-y-1.5 text-sm">
            {s.weekly.length === 0 ? (
              <p className="text-muted-foreground">No recent practice.</p>
            ) : (
              s.weekly.map((w) => (
                <div key={w.weekStart.toISOString()} className="flex justify-between">
                  <span className="text-muted-foreground">
                    week of {w.weekStart.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
                  </span>
                  <span className="tabular-nums">{w.answered} questions</span>
                </div>
              ))
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm">Weakest skills — where to help</CardTitle>
          </CardHeader>
          <CardContent>
            {s.weakestSkills.length === 0 ? (
              <p className="text-sm text-muted-foreground">Needs more practice to rank.</p>
            ) : (
              <ol className="space-y-1.5 text-sm">
                {s.weakestSkills.map((k, i) => (
                  <li key={k.skill} className="flex justify-between gap-2">
                    <span>
                      <span className="mr-1.5 tabular-nums text-muted-foreground">{i + 1}.</span>
                      {k.skill}
                    </span>
                    <span className="shrink-0 tabular-nums text-muted-foreground">
                      {pct(k.correct, k.total)}% of {k.total}
                    </span>
                  </li>
                ))}
              </ol>
            )}
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm">Accuracy by domain</CardTitle>
          </CardHeader>
          <CardContent className="space-y-2">
            {s.domainAccuracy.length === 0 ? (
              <p className="text-sm text-muted-foreground">No practice recorded yet.</p>
            ) : (
              s.domainAccuracy.map((d) => {
                const p = pct(d.correct, d.total);
                return (
                  <div key={d.domain}>
                    <div className="flex justify-between text-xs">
                      <span>{d.domain}</span>
                      <span className="tabular-nums text-muted-foreground">
                        {p}% · {d.total} q
                      </span>
                    </div>
                    <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-secondary">
                      <div className="h-full rounded-full bg-primary" style={{ width: `${p}%` }} />
                    </div>
                  </div>
                );
              })
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm">Practice tests</CardTitle>
          </CardHeader>
          <CardContent>
            {s.attempts.length === 0 ? (
              <p className="text-sm text-muted-foreground">No submitted tests yet.</p>
            ) : (
              <ul className="divide-y divide-border text-sm">
                {s.attempts.map((a, i) => (
                  <li key={i} className="flex items-center justify-between py-2">
                    <span>{a.testTitle}</span>
                    <span className="flex items-center gap-3">
                      {a.submittedAt && (
                        <span className="text-xs text-muted-foreground">
                          {a.submittedAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
                        </span>
                      )}
                      <span className="font-semibold tabular-nums">{a.score ?? "—"}</span>
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
