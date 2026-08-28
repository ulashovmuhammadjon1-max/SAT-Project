import Link from "next/link";
import { notFound } from "next/navigation";
import {
  AlertTriangle,
  ChevronRight,
  ClipboardList,
  GraduationCap,
  TrendingDown,
  Users,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { AssignmentForm } from "@/components/teacher/assignment-form";
import { formatDue, isDone } from "@/lib/classroom/status";
import { getAssignableTests } from "@/server/actions/teacher/assignments";
import { getClassAnalytics, getMyTeachingClasses } from "@/server/actions/teacher/classes";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Teacher Panel" };
export const dynamic = "force-dynamic";

const pct = (correct: number, total: number) => (total === 0 ? 0 : Math.round((correct / total) * 100));

/**
 * One class, the teacher's view: who is active, what the class is weak at,
 * the assignments with their submission counts, and the roster. Assignments
 * are created from inside this page, so each one belongs to exactly this
 * class — the switcher at the top is how you change that, not a dropdown on
 * the form.
 */
export default async function TeachClassPage({ params }: { params: { classId: string } }) {
  await requireUser();
  const classes = await getMyTeachingClasses();
  const active = classes.find((c) => c.id === params.classId);
  if (!active) notFound();

  const [tests, a] = await Promise.all([getAssignableTests(), getClassAnalytics(active.id)]);

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
          <GraduationCap className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Teacher panel
        </p>
        <div className="mt-1 flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="font-display text-3xl font-semibold tracking-tight">{active.name}</h1>
            <p className="mt-1 text-sm text-muted-foreground">{active.school}</p>
          </div>
          <span className="flex items-center gap-2 text-xs text-muted-foreground">
            Class code
            <Badge variant="navy" className="px-2.5 py-1 font-mono text-sm tracking-[0.2em]">
              {active.code}
            </Badge>
          </span>
        </div>
      </div>

      {/* Class switcher — only when there is a choice to make. */}
      {classes.length > 1 && (
        <div className="flex flex-wrap gap-2 border-b border-border pb-3">
          {classes.map((c) => {
            const on = c.id === active.id;
            return (
              <Link
                key={c.id}
                href={`/teach/${c.id}`}
                className={cn(
                  "rounded-full border px-3.5 py-1.5 text-sm font-medium transition-colors",
                  on
                    ? "border-primary bg-primary text-primary-foreground"
                    : "border-border text-muted-foreground hover:border-primary/50 hover:text-foreground",
                )}
              >
                {c.name}
                <span className={on ? "ml-1.5 opacity-80" : "ml-1.5 text-muted-foreground"}>
                  {c.students.length}
                </span>
              </Link>
            );
          })}
        </div>
      )}

      {/* Analytics row */}
      {a && active.students.length > 0 && (
        <div className="grid gap-4 lg:grid-cols-3">
          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center gap-2 text-sm">
                <Users className="h-4 w-4 text-primary" /> This week
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-1.5">
              <p className="text-3xl font-semibold tabular-nums">
                {a.activeLast7}
                <span className="text-base font-normal text-muted-foreground">
                  {" "}/ {active.students.length} active
                </span>
              </p>
              {a.inactive.length > 0 && (
                <div className="rounded-lg bg-warning/10 px-3 py-2 text-xs leading-relaxed">
                  <p className="flex items-center gap-1 font-medium text-warning-foreground">
                    <AlertTriangle className="h-3.5 w-3.5 text-warning" /> Needs a nudge
                  </p>
                  <p className="mt-0.5 text-muted-foreground">
                    {a.inactive.map((s) => s.name ?? "Student").join(", ")}
                  </p>
                </div>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-2">
              <CardTitle className="text-sm">Class accuracy by domain</CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              {a.domainAccuracy.length === 0 ? (
                <p className="text-sm text-muted-foreground">No practice recorded yet.</p>
              ) : (
                a.domainAccuracy.map((d) => {
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
              <CardTitle className="flex items-center gap-2 text-sm">
                <TrendingDown className="h-4 w-4 text-destructive" /> Weakest skills — teach these
              </CardTitle>
            </CardHeader>
            <CardContent>
              {a.weakestSkills.length === 0 ? (
                <p className="text-sm text-muted-foreground">
                  Appears once the class has practised enough to rank.
                </p>
              ) : (
                <ol className="space-y-1.5 text-sm">
                  {a.weakestSkills.map((s, rank) => (
                    <li key={s.skill} className="flex justify-between gap-2">
                      <span>
                        <span className="mr-1.5 tabular-nums text-muted-foreground">{rank + 1}.</span>
                        {s.skill}
                      </span>
                      <span className="shrink-0 tabular-nums text-muted-foreground">
                        {pct(s.correct, s.total)}%
                      </span>
                    </li>
                  ))}
                </ol>
              )}
            </CardContent>
          </Card>
        </div>
      )}

      {/* Assignments: create here, track per assignment */}
      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="flex items-center gap-2 text-base">
            <ClipboardList className="h-4 w-4 text-primary" /> Assignments
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <AssignmentForm classId={active.id} tests={tests} />

          {a && a.assignments.length > 0 && (
            <div className="divide-y divide-border/60">
              {a.assignments.map((as) => {
                const doneCount = as.perStudent.filter((p) => p.done).length;
                const missing = as.perStudent.filter((p) => p.status === "MISSING").length;
                const handedIn = as.perStudent.filter((p) => p.files.length > 0 || p.note).length;
                return (
                  <Link
                    key={as.id}
                    href={`/teach/${active.id}/assignments/${as.id}`}
                    className="group flex items-center gap-4 px-1 py-3.5 transition-colors hover:bg-secondary/50 sm:px-2"
                  >
                    <span className="min-w-0 flex-1">
                      <span className="block truncate font-medium group-hover:text-primary">
                        {as.title}
                      </span>
                      <span className="mt-0.5 block text-xs text-muted-foreground">
                        {as.kind === "TEST" && as.testTitle}
                        {as.kind === "QUESTIONS" && `${as.questionCount} questions`}
                        {as.kind === "TASK" && "Task"}
                        {as.dueAt && <> · {formatDue(as.dueAt)}</>}
                        {handedIn > 0 && <> · {handedIn} hand-in{handedIn === 1 ? "" : "s"}</>}
                      </span>
                    </span>
                    <span className="flex shrink-0 items-center gap-3 text-sm tabular-nums">
                      <span className="text-success">{doneCount} ✓</span>
                      {missing > 0 && <span className="text-destructive">{missing} missing</span>}
                      <span className="text-muted-foreground">/ {as.perStudent.length}</span>
                    </span>
                    <ChevronRight className="h-4 w-4 shrink-0 text-muted-foreground/60 transition-transform group-hover:translate-x-0.5" />
                  </Link>
                );
              })}
            </div>
          )}
        </CardContent>
      </Card>

      {/* Roster with drill-down links */}
      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">Students — click a name for the full picture</CardTitle>
        </CardHeader>
        <CardContent>
          {active.students.length === 0 ? (
            <p className="rounded-xl border border-dashed border-border px-4 py-8 text-center text-sm text-muted-foreground">
              Nobody has joined yet. Give your students the code{" "}
              <span className="font-mono font-semibold tracking-widest">{active.code}</span> — they
              enter it under <span className="font-medium">School → Join a class</span>.
            </p>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-border text-left text-xs uppercase tracking-wide text-muted-foreground">
                    <th className="py-2 pr-4 font-medium">Student</th>
                    <th className="py-2 pr-4 font-medium">Joined</th>
                    <th className="py-2 pr-4 font-medium">Questions</th>
                    <th className="py-2 pr-4 font-medium">Tests</th>
                    <th className="py-2 font-medium">Best score</th>
                  </tr>
                </thead>
                <tbody>
                  {active.students.map((s) => (
                    <tr key={s.id} className="border-b border-border/60">
                      <td className="py-2 pr-4">
                        <Link
                          href={`/teach/student/${s.id}`}
                          className="font-medium text-primary underline-offset-4 hover:underline"
                        >
                          {s.name ?? s.email}
                        </Link>
                      </td>
                      <td className="py-2 pr-4 text-muted-foreground">
                        {s.joinedAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
                      </td>
                      <td className="py-2 pr-4 tabular-nums">{s.questionsAnswered.toLocaleString()}</td>
                      <td className="py-2 pr-4 tabular-nums">{s.testsCompleted}</td>
                      <td className="py-2 tabular-nums">{s.bestScore ?? "—"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </CardContent>
      </Card>

    </div>
  );
}
