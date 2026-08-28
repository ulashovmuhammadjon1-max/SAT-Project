import Link from "next/link";
import { redirect } from "next/navigation";
import { ArrowRight, GraduationCap, Users } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { getMyTeachingClasses } from "@/server/actions/teacher/classes";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Teacher Panel" };
export const dynamic = "force-dynamic";

/**
 * The teacher panel's front door. One class goes straight in; several get a
 * picker. Everything real happens inside /teach/{classId}, so an assignment
 * always belongs to the class it was created in.
 */
export default async function TeachPage({
  searchParams,
}: {
  searchParams: { class?: string };
}) {
  await requireUser();
  const classes = await getMyTeachingClasses();

  // The pre-redesign panel used /teach?class= — keep those links working.
  if (searchParams.class && classes.some((c) => c.id === searchParams.class)) {
    redirect(`/teach/${searchParams.class}`);
  }
  if (classes.length === 1) redirect(`/teach/${classes[0].id}`);

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
        <h1 className="font-display text-2xl font-semibold tracking-tight">Your classes</h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Open a class to set assignments, track submissions, and see who needs a nudge.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        {classes.map((c) => (
          <Link
            key={c.id}
            href={`/teach/${c.id}`}
            className="group rounded-2xl border border-border/70 bg-card p-5 shadow-soft transition-all hover:-translate-y-0.5 hover:border-primary/40 hover:shadow-md"
          >
            <div className="flex items-start justify-between gap-3">
              <div className="min-w-0">
                <p className="truncate font-display text-lg font-semibold tracking-tight group-hover:text-primary">
                  {c.name}
                </p>
                <p className="mt-0.5 truncate text-sm text-muted-foreground">{c.school}</p>
              </div>
              <Badge variant="navy" className="shrink-0 px-2 py-0.5 font-mono text-xs tracking-[0.15em]">
                {c.code}
              </Badge>
            </div>
            <div className="mt-5 flex items-center justify-between border-t border-border/60 pt-3.5 text-sm">
              <span className="flex items-center gap-1.5 text-muted-foreground">
                <Users className="h-4 w-4" /> {c.students.length} student
                {c.students.length === 1 ? "" : "s"}
              </span>
              <span className="flex items-center gap-1 font-medium text-primary">
                Open <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
              </span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
