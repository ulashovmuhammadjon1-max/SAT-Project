import Link from "next/link";
import { ArrowRight, CheckCircle2, Plus, School, Users } from "lucide-react";

import { Button } from "@/components/ui/button";
import { AssignmentRow } from "@/components/classroom/assignment-row";
import { JoinClassDialog } from "@/components/classroom/join-class-dialog";
import { formatDue } from "@/lib/classroom/status";
import { getClassesOverview } from "@/server/actions/student/classroom";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Your Classes" };
export const dynamic = "force-dynamic";

/**
 * The classroom hub: which classes am I in, and what needs doing next. The
 * class cards give the overview; the class page gives the context; the
 * assignment page gives the actual work.
 */
export default async function ClassesPage() {
  await requireUser();
  const { classes, upcoming } = await getClassesOverview();

  if (classes.length === 0) {
    return (
      <div className="mx-auto flex max-w-md flex-col items-center py-20 text-center">
        <span className="flex h-14 w-14 items-center justify-center rounded-2xl bg-success/10 text-success">
          <School className="h-6 w-6" />
        </span>
        <h1 className="mt-5 font-display text-2xl font-semibold tracking-tight">
          You&apos;re not in any classes yet
        </h1>
        <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
          Ask your teacher for a class code to get started. Joining lets them see your practice
          progress, so class time goes where your class actually needs it.
        </p>
        <JoinClassDialog>
          <Button className="mt-6 gap-2">
            <Plus className="h-4 w-4" /> Join a class
          </Button>
        </JoinClassDialog>
        <p className="mt-10 text-sm text-muted-foreground">
          Are you a teacher?{" "}
          <Link href="/schools" className="font-medium text-primary underline-offset-4 hover:underline">
            Scholarly for Schools
          </Link>{" "}
          sets your class up free.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-10">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
            <School className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
            Scholarly for Schools
          </p>
          <h1 className="mt-1 font-display text-2xl font-semibold tracking-tight">Your classes</h1>
        </div>
        <JoinClassDialog>
          <Button variant="outline" className="gap-2">
            <Plus className="h-4 w-4" /> Join a class
          </Button>
        </JoinClassDialog>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        {classes.map((c) => (
          <Link
            key={c.id}
            href={`/classes/${c.id}`}
            className="group rounded-2xl border border-border/70 bg-card p-5 shadow-soft transition-all hover:-translate-y-0.5 hover:border-primary/40 hover:shadow-md"
          >
            <div className="flex items-start justify-between gap-3">
              <div className="min-w-0">
                <p className="truncate font-display text-lg font-semibold tracking-tight group-hover:text-primary">
                  {c.name}
                </p>
                <p className="mt-0.5 truncate text-sm text-muted-foreground">
                  {c.school} · {c.teacherName}
                </p>
              </div>
              <span className="flex items-center gap-1 rounded-full bg-secondary px-2 py-1 text-xs text-muted-foreground">
                <Users className="h-3 w-3" /> {c.classmates}
              </span>
            </div>

            <div className="mt-5 flex items-center justify-between gap-3 border-t border-border/60 pt-3.5">
              {c.openCount === 0 ? (
                <span className="flex items-center gap-1.5 text-sm font-medium text-success">
                  <CheckCircle2 className="h-4 w-4" /> All caught up
                </span>
              ) : (
                <span className="min-w-0 text-sm">
                  <span className="font-medium">
                    {c.openCount} assignment{c.openCount === 1 ? "" : "s"} open
                  </span>
                  {c.nextDue && (
                    <span className="block truncate text-xs text-muted-foreground">
                      {c.nextDue.title} — {formatDue(c.nextDue.dueAt).toLowerCase()}
                    </span>
                  )}
                </span>
              )}
              <span className="flex items-center gap-1 text-sm font-medium text-primary">
                Open <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
              </span>
            </div>
          </Link>
        ))}
      </div>

      {upcoming.length > 0 && (
        <section>
          <h2 className="font-display text-lg font-semibold tracking-tight">Up next</h2>
          <p className="mt-0.5 text-sm text-muted-foreground">
            Everything still open, across all your classes — soonest due first.
          </p>
          <div className="mt-3 divide-y divide-border/60 rounded-2xl border border-border/70 bg-card shadow-soft">
            {upcoming.map((a) => (
              <AssignmentRow key={a.id} assignment={a} showClass />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
