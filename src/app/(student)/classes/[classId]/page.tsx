import Link from "next/link";
import { notFound } from "next/navigation";
import { PartyPopper, Users } from "lucide-react";

import { AssignmentRow } from "@/components/classroom/assignment-row";
import { isDone } from "@/lib/classroom/status";
import { getClassHome, type StudentAssignment } from "@/server/actions/student/classroom";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Class" };
export const dynamic = "force-dynamic";

/**
 * A class's home: its assignments, grouped the way a student triages them —
 * overdue first, then what's due soon, then the rest, then what's finished.
 */
export default async function ClassPage({ params }: { params: { classId: string } }) {
  await requireUser();
  const home = await getClassHome(params.classId);
  if (!home) notFound();

  const week = 7 * 86_400_000;
  const now = Date.now();

  const open = home.assignments.filter((a) => !isDone(a.status) && a.status !== "MISSING");
  const groups: { title: string; hint?: string; items: StudentAssignment[] }[] = [
    {
      title: "Past due",
      hint: "Still worth handing in — late beats missing.",
      items: home.assignments.filter((a) => a.status === "MISSING"),
    },
    {
      title: "Due soon",
      items: open
        .filter((a) => a.dueAt && a.dueAt.getTime() - now < week)
        .sort((a, b) => a.dueAt!.getTime() - b.dueAt!.getTime()),
    },
    {
      title: "Upcoming",
      items: open
        .filter((a) => !a.dueAt || a.dueAt.getTime() - now >= week)
        .sort((a, b) => {
          if (a.dueAt && b.dueAt) return a.dueAt.getTime() - b.dueAt.getTime();
          if (a.dueAt) return -1;
          if (b.dueAt) return 1;
          return b.createdAt.getTime() - a.createdAt.getTime();
        }),
    },
    {
      title: "Done",
      items: home.assignments.filter((a) => isDone(a.status)),
    },
  ].filter((g) => g.items.length > 0);

  const allCaughtUp =
    home.assignments.length > 0 && home.assignments.every((a) => isDone(a.status));

  return (
    <div className="space-y-8">
      <div>
        <Link href="/classes" className="text-sm text-muted-foreground hover:text-foreground">
          Your classes
        </Link>
        <div className="mt-1 flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="font-display text-3xl font-semibold tracking-tight">{home.name}</h1>
            <p className="mt-1 text-sm text-muted-foreground">
              with {home.teacherName} · {home.school}
            </p>
          </div>
          <span className="flex items-center gap-1.5 text-sm text-muted-foreground">
            <Users className="h-4 w-4" /> {home.classmates} student{home.classmates === 1 ? "" : "s"}
          </span>
        </div>

        <nav className="mt-5 flex gap-1 border-b border-border">
          {[
            { href: `/classes/${home.id}`, label: "Assignments", active: true },
            { href: `/classes/${home.id}/leaderboard`, label: "Leaderboard", active: false },
          ].map((t) => (
            <Link
              key={t.href}
              href={t.href}
              className={cn(
                "-mb-px border-b-2 px-4 py-2.5 text-sm font-medium transition-colors",
                t.active
                  ? "border-primary text-primary"
                  : "border-transparent text-muted-foreground hover:text-foreground",
              )}
            >
              {t.label}
            </Link>
          ))}
        </nav>
      </div>

      {home.assignments.length === 0 ? (
        <div className="rounded-2xl border border-dashed border-border px-6 py-16 text-center">
          <p className="font-medium">No assignments yet</p>
          <p className="mt-1 text-sm text-muted-foreground">
            {home.teacherName} hasn&apos;t posted anything here yet — you&apos;ll get an email the
            moment they do.
          </p>
        </div>
      ) : (
        <div className="space-y-8">
          {allCaughtUp && (
            <div className="flex items-center gap-3 rounded-2xl bg-success/10 px-5 py-4">
              <PartyPopper className="h-5 w-5 shrink-0 text-success" />
              <div>
                <p className="font-medium text-success">You&apos;re all caught up</p>
                <p className="text-sm text-muted-foreground">No outstanding assignments.</p>
              </div>
            </div>
          )}
          {groups.map((g) => (
            <section key={g.title}>
              <div className="flex items-baseline gap-2">
                <h2 className="font-display text-lg font-semibold tracking-tight">{g.title}</h2>
                <span className="text-sm tabular-nums text-muted-foreground">{g.items.length}</span>
                {g.hint && (
                  <span className="hidden text-xs text-muted-foreground sm:inline">— {g.hint}</span>
                )}
              </div>
              <div className="mt-2 divide-y divide-border/60 rounded-2xl border border-border/70 bg-card shadow-soft">
                {g.items.map((a) => (
                  <AssignmentRow key={a.id} assignment={a} />
                ))}
              </div>
            </section>
          ))}
        </div>
      )}
    </div>
  );
}
