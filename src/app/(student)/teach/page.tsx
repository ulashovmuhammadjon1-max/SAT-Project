import { GraduationCap, Users } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { getMyTeachingClasses } from "@/server/actions/teacher/classes";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Teacher Panel" };
export const dynamic = "force-dynamic";

export default async function TeachPage() {
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

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
          <GraduationCap className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly for Schools
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Teacher panel</h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Your classes, live. Students join with the class code; their practice shows up here as it
          happens — nothing to grade by hand.
        </p>
      </div>

      {classes.map((c) => {
        const totalAnswered = c.students.reduce((s, st) => s + st.questionsAnswered, 0);
        return (
          <Card key={c.id}>
            <CardHeader className="pb-3">
              <div className="flex flex-wrap items-center gap-2">
                <CardTitle className="text-base">{c.name}</CardTitle>
                <span className="text-sm text-muted-foreground">· {c.school}</span>
                <span className="ml-auto flex items-center gap-2">
                  <span className="text-xs text-muted-foreground">Class code</span>
                  <Badge variant="navy" className="px-2.5 py-1 font-mono text-sm tracking-[0.2em]">
                    {c.code}
                  </Badge>
                </span>
              </div>
              <p className="flex items-center gap-1.5 text-sm text-muted-foreground">
                <Users className="h-3.5 w-3.5" />
                {c.students.length} student{c.students.length === 1 ? "" : "s"} ·{" "}
                {totalAnswered.toLocaleString()} questions answered in total
              </p>
            </CardHeader>
            <CardContent>
              {c.students.length === 0 ? (
                <p className="rounded-xl border border-dashed border-border px-4 py-8 text-center text-sm text-muted-foreground">
                  Nobody has joined yet. Give your students the code{" "}
                  <span className="font-mono font-semibold tracking-widest">{c.code}</span> — they
                  enter it under <span className="font-medium">School → My Class</span>.
                </p>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b border-border text-left text-xs uppercase tracking-wide text-muted-foreground">
                        <th className="py-2 pr-4 font-medium">Student</th>
                        <th className="py-2 pr-4 font-medium">Joined</th>
                        <th className="py-2 pr-4 font-medium">Questions answered</th>
                        <th className="py-2 pr-4 font-medium">Tests completed</th>
                        <th className="py-2 font-medium">Best score</th>
                      </tr>
                    </thead>
                    <tbody>
                      {c.students.map((s) => (
                        <tr key={s.id} className="border-b border-border/60">
                          <td className="py-2 pr-4">
                            <span className="font-medium">{s.name ?? "—"}</span>
                            <span className="ml-2 text-xs text-muted-foreground">{s.email}</span>
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
        );
      })}

      <p className="max-w-2xl text-sm text-muted-foreground">
        Want a second class, a change, or a feature that would help your teaching? Write to{" "}
        <a
          href="mailto:scholarlyhub.space@gmail.com?subject=Teacher%20panel"
          className="font-medium text-primary underline-offset-4 hover:underline"
        >
          scholarlyhub.space@gmail.com
        </a>{" "}
        — pilot teachers shape what gets built.
      </p>
    </div>
  );
}
