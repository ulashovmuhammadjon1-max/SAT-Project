import Link from "next/link";
import {
  AlertTriangle,
  ClipboardList,
  Download,
  GraduationCap,
  ListChecks,
  Paperclip,
  TrendingDown,
  Users,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { AssignmentForm, DeleteAssignmentButton } from "@/components/teacher/assignment-form";
import { getAssignableTests } from "@/server/actions/teacher/assignments";
import { getClassAnalytics, getMyTeachingClasses } from "@/server/actions/teacher/classes";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Teacher Panel" };
export const dynamic = "force-dynamic";

const pct = (correct: number, total: number) => (total === 0 ? 0 : Math.round((correct / total) * 100));

export default async function TeachPage({
  searchParams,
}: {
  searchParams: { class?: string };
}) {
  await requireUser();
  const classes = await getMyTeachingClasses();

  if (classes.length === 0) {
    return (
      <div className="space-y-4">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Teacher panel</h1>
        <p className="max-w-xl text-sm text-muted-foreground">
          No classes are linked to your account yet. If you teach and want one, write to{" "}
          <a
            href="mailto:scholarlyhub.space@gmail.com?subject=Scholarly%20for%20Schools"
            className="font-medium text-primary underline-offset-4 hover:underline"
          >
            scholarlyhub.space@gmail.com
          </a>{" "}
          — we set classes up personally and link them to the email you register with.
        </p>
      </div>
    );
  }

  // One class at a time. A teacher with five classes should not scroll past
  // four of them to reach the one they are teaching this period.
  const active = classes.find((c) => c.id === searchParams.class) ?? classes[0];

  const [tests, a] = await Promise.all([getAssignableTests(), getClassAnalytics(active.id)]);
  const names = new Map(active.students.map((s) => [s.id, s.name ?? s.email]));

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
          <GraduationCap className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly for Schools
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Teacher panel</h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Set assignments, watch them complete themselves, and click any student for their full
          picture.
        </p>
      </div>

      {/* Class switcher — only worth showing when there is a choice to make. */}
      {classes.length > 1 && (
        <div className="flex flex-wrap gap-2 border-b border-border pb-3">
          {classes.map((c) => {
            const on = c.id === active.id;
            return (
              <Link
                key={c.id}
                href={`/teach?class=${c.id}`}
                className={`rounded-full border px-3.5 py-1.5 text-sm font-medium transition-colors ${
                  on
                    ? "border-primary bg-primary text-primary-foreground"
                    : "border-border text-muted-foreground hover:border-primary/50 hover:text-foreground"
                }`}
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

      <div className="flex flex-wrap items-center gap-2">
        <h2 className="font-display text-xl font-semibold tracking-tight">{active.name}</h2>
        <span className="text-sm text-muted-foreground">· {active.school}</span>
        <span className="ml-auto flex items-center gap-2 text-xs text-muted-foreground">
          Class code
          <Badge variant="navy" className="px-2.5 py-1 font-mono text-sm tracking-[0.2em]">
            {active.code}
          </Badge>
        </span>
      </div>

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

      {/* Assignments */}
      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="flex items-center gap-2 text-base">
            <ClipboardList className="h-4 w-4 text-primary" /> Assignments
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <AssignmentForm classId={active.id} tests={tests} />

          {a && a.assignments.length > 0 && (
            <ul className="divide-y divide-border">
              {a.assignments.map((as) => {
                const doneCount = as.perStudent.filter((p) => p.done).length;
                const submissions = as.perStudent.filter((p) => p.note || p.fileName);
                return (
                  <li key={as.id} className="py-4">
                    <div className="flex flex-wrap items-center gap-2">
                      <p className="font-medium">{as.title}</p>
                      {as.testTitle && <Badge variant="outline">{as.testTitle}</Badge>}
                      {as.questionCount > 0 && (
                        <Badge variant="outline" className="gap-1">
                          <ListChecks className="h-3 w-3" />
                          {as.questionCount} questions
                        </Badge>
                      )}
                      {as.attachmentHref && (
                        <a
                          href={as.attachmentHref}
                          target="_blank"
                          rel="noreferrer"
                          className="inline-flex items-center gap-1 text-xs font-medium text-primary underline-offset-4 hover:underline"
                        >
                          <Paperclip className="h-3 w-3" />
                          {as.attachmentName}
                        </a>
                      )}
                      {as.dueAt && (
                        <span className="text-xs text-muted-foreground">
                          due{" "}
                          {as.dueAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
                        </span>
                      )}
                      <span className="ml-auto text-sm tabular-nums text-muted-foreground">
                        {doneCount}/{as.perStudent.length} done
                      </span>
                      <DeleteAssignmentButton assignmentId={as.id} />
                    </div>

                    {as.instructions && (
                      <p className="mt-1 text-sm text-muted-foreground">{as.instructions}</p>
                    )}

                    {as.perStudent.length > 0 && (
                      <div className="mt-2 flex flex-wrap gap-x-3 gap-y-1 text-xs">
                        {as.perStudent.map((p) => (
                          <span
                            key={p.userId}
                            className={p.done ? "text-success" : "text-muted-foreground"}
                          >
                            {names.get(p.userId)}
                            {p.done
                              ? p.score != null
                                ? ` ✓ ${p.score}${as.questionCount > 0 ? "%" : ""}`
                                : " ✓"
                              : as.questionCount > 0 && p.answered > 0
                                ? ` ${p.answered}/${as.questionCount}`
                                : " —"}
                          </span>
                        ))}
                      </div>
                    )}

                    {submissions.length > 0 && (
                      <div className="mt-3 space-y-1.5 rounded-lg bg-secondary/40 p-3">
                        <p className="text-xs font-medium">Work handed in</p>
                        {submissions.map((p) => (
                          <div key={p.userId} className="flex flex-wrap items-center gap-2 text-xs">
                            <span className="font-medium">{names.get(p.userId)}</span>
                            {p.note && <span className="text-muted-foreground">{p.note}</span>}
                            {p.submissionHref && (
                              <a
                                href={p.submissionHref}
                                target="_blank"
                                rel="noreferrer"
                                className="inline-flex items-center gap-1 font-medium text-primary underline-offset-4 hover:underline"
                              >
                                <Download className="h-3 w-3" />
                                {p.fileName}
                              </a>
                            )}
                          </div>
                        ))}
                      </div>
                    )}
                  </li>
                );
              })}
            </ul>
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
              enter it under <span className="font-medium">School → My Class</span>.
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
