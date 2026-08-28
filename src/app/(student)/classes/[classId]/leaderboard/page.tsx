import Link from "next/link";
import { notFound } from "next/navigation";
import { Medal, Users } from "lucide-react";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Class Leaderboard" };
export const dynamic = "force-dynamic";

/**
 * Rankings inside one class — a friendly race between people who know each
 * other. Ranked by questions answered (effort), with tests and best score
 * alongside; effort first on purpose, because a class board that only shows
 * scores demoralises exactly the students a teacher most needs practising.
 */
export default async function ClassLeaderboardPage({
  params,
}: {
  params: { classId: string };
}) {
  const user = await requireUser();

  const membership = await prisma.classMembership.findUnique({
    where: { classId_userId: { classId: params.classId, userId: user.id } },
    select: {
      class: {
        select: {
          id: true,
          name: true,
          school: true,
          teacherName: true,
          isArchived: true,
          memberships: {
            select: {
              user: {
                select: {
                  id: true,
                  name: true,
                  studyActivities: { select: { questionsAnswered: true } },
                  attempts: { where: { status: "SUBMITTED" }, select: { totalScaledScore: true } },
                },
              },
            },
          },
        },
      },
    },
  });
  if (!membership || membership.class.isArchived) notFound();
  const c = membership.class;

  const rows = c.memberships
    .map((m) => ({
      id: m.user.id,
      name: m.user.name ?? "Student",
      answered: m.user.studyActivities.reduce((sum, a) => sum + a.questionsAnswered, 0),
      tests: m.user.attempts.length,
      best: m.user.attempts.reduce<number | null>(
        (best, a) => (a.totalScaledScore == null ? best : Math.max(best ?? 0, a.totalScaledScore)),
        null,
      ),
    }))
    .sort((a, b) => b.answered - a.answered || b.tests - a.tests);

  return (
    <div className="space-y-8">
      <div>
        <Link href="/classes" className="text-sm text-muted-foreground hover:text-foreground">
          Your classes
        </Link>
        <div className="mt-1 flex flex-wrap items-end justify-between gap-3">
          <div>
            <h1 className="font-display text-3xl font-semibold tracking-tight">{c.name}</h1>
            <p className="mt-1 text-sm text-muted-foreground">
              with {c.teacherName} · {c.school}
            </p>
          </div>
          <span className="flex items-center gap-1.5 text-sm text-muted-foreground">
            <Users className="h-4 w-4" /> {rows.length} student{rows.length === 1 ? "" : "s"}
          </span>
        </div>

        <nav className="mt-5 flex gap-1 border-b border-border">
          {[
            { href: `/classes/${c.id}`, label: "Assignments", active: false },
            { href: `/classes/${c.id}/leaderboard`, label: "Leaderboard", active: true },
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

      <div className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
        <p className="text-sm text-muted-foreground">
          Ranked by questions answered — effort first. Scores follow effort anyway.
        </p>
        <div className="mt-4 overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-border text-left text-xs uppercase tracking-wide text-muted-foreground">
                <th className="py-2 pr-4 font-medium">#</th>
                <th className="py-2 pr-4 font-medium">Student</th>
                <th className="py-2 pr-4 font-medium">Questions answered</th>
                <th className="py-2 pr-4 font-medium">Tests completed</th>
                <th className="py-2 font-medium">Best score</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r, i) => {
                const me = r.id === user.id;
                return (
                  <tr
                    key={r.id}
                    className={cn("border-b border-border/60", me && "bg-primary/5 font-medium")}
                  >
                    <td className="py-2.5 pr-4 tabular-nums">
                      {i < 3 ? (
                        <Medal
                          className={cn(
                            "h-4 w-4",
                            i === 0 && "text-warning",
                            i === 1 && "text-muted-foreground",
                            i === 2 && "text-[#b87333]",
                          )}
                        />
                      ) : (
                        i + 1
                      )}
                    </td>
                    <td className="py-2.5 pr-4">
                      {r.name}
                      {me && <span className="ml-1.5 text-xs text-primary">(you)</span>}
                    </td>
                    <td className="py-2.5 pr-4 tabular-nums">{r.answered.toLocaleString()}</td>
                    <td className="py-2.5 pr-4 tabular-nums">{r.tests}</td>
                    <td className="py-2.5 tabular-nums">{r.best ?? "—"}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
