import { School, Users } from "lucide-react";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { AssignmentList } from "@/components/student/assignment-list";
import { JoinClassForm } from "@/components/student/join-class-form";
import { getMyAssignments, getMyClasses } from "@/server/actions/student/school-class";
import { requireUser } from "@/lib/session";

export const metadata = { title: "My Class" };
export const dynamic = "force-dynamic";

export default async function ClassPage() {
  await requireUser();
  const [classes, assignments] = await Promise.all([getMyClasses(), getMyAssignments()]);

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
          <School className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly for Schools
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">My class</h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          If your teacher uses Scholarly, they will give you a class code. Joining lets them see
          your practice progress so class time goes where your class actually needs it.
        </p>
      </div>

      <Card className="max-w-xl">
        <CardHeader>
          <CardTitle className="text-base">Join with a code</CardTitle>
          <CardDescription>
            Your teacher sees your test scores and practice volume — never your password, your
            messages, or anything outside your studying.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <JoinClassForm />
        </CardContent>
      </Card>

      {assignments.length > 0 && (
        <Card className="max-w-2xl">
          <CardHeader>
            <CardTitle className="text-base">Assignments from your teacher</CardTitle>
            <CardDescription>
              Test assignments complete themselves when you submit the test — no box to tick.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <AssignmentList assignments={assignments} />
          </CardContent>
        </Card>
      )}

      {classes.length > 0 && (
        <Card className="max-w-xl">
          <CardHeader>
            <CardTitle className="text-base">Your classes</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="divide-y divide-border">
              {classes.map((c) => (
                <li key={c.id} className="flex items-center gap-3 py-3">
                  <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-success/10 text-success">
                    <School className="h-4 w-4" />
                  </span>
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">{c.name}</p>
                    <p className="text-xs text-muted-foreground">
                      {c.school} · {c.teacherName}
                    </p>
                  </div>
                  <span className="flex items-center gap-1 text-xs text-muted-foreground">
                    <Users className="h-3.5 w-3.5" /> {c.classmates}
                  </span>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}

      <p className="max-w-xl text-sm text-muted-foreground">
        Are you a teacher? Scholarly gives your class free adaptive SAT tests, auto-graded
        practice, and a per-student progress view —{" "}
        <a
          href="mailto:scholarlyhub.space@gmail.com?subject=Scholarly%20for%20Schools"
          className="font-medium text-primary underline-offset-4 hover:underline"
        >
          write to us
        </a>{" "}
        and we will set your class up personally.
      </p>
    </div>
  );
}
