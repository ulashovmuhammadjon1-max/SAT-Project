import Link from "next/link";
import { Medal, School, Trophy } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Class Leaderboard" };
export const dynamic = "force-dynamic";

/**
 * Rankings inside a class only — a friendly race between people who know each
 * other, not the global board. Ranked by questions answered (effort), with
 * tests completed and best score alongside; effort first on purpose, because a
 * class leaderboard that only shows scores demoralises exactly the students a
 * teacher most needs practising.
 */
export default async function ClassLeaderboardPage() {
  const user = await requireUser();

  const memberships = await prisma.classMembership.findMany({
    where: { userId: user.id },
    select: {
      class: {
        select: {
          id: true,
          name: true,
          school: true,
          isArchived: true,
          memberships: {
            select: {
              user: {
                select: {
                  id: true,
                  name: true,
                  studyActivities: { select: { questionsAnswered: true } },
                  attempts: {
                    where: { status: "SUBMITTED" },
                    select: { totalScaledScore: true },
                  },
                },
              },
            },
          },
        },
      },
    },
  });

  const classes = memberships
    .map((m) => m.class)
    .filter((c) => !c.isArchived)
    .map((c) => ({
      id: c.id,
      name: c.name,
      school: c.school,
      rows: c.memberships
        .map((m) => ({
          id: m.user.id,
          name: m.user.name ?? "Student",
          answered: m.user.studyActivities.reduce((sum, a) => sum + a.questionsAnswered, 0),
          tests: m.user.attempts.length,
          best: m.user.attempts.reduce<number | null>(
            (best, a) =>
              a.totalScaledScore == null ? best : Math.max(best ?? 0, a.totalScaledScore),
            null,
          ),
        }))
        .sort((a, b) => b.answered - a.answered || b.tests - a.tests),
    }));

  if (classes.length === 0) {
    return (
      <div className="space-y-4">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Class leaderboard</h1>
        <p className="max-w-xl text-sm text-muted-foreground">
          You are not in a class yet. If your teacher uses Scholarly,{" "}
          <Link href="/class" className="font-medium text-primary underline-offset-4 hover:underline">
            join with their class code
          </Link>{" "}
          and your class race appears here.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
          <School className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly for Schools
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Class leaderboard</h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Ranked by questions answered — effort first. Scores follow effort anyway.
        </p>
      </div>

      {classes.map((c) => (
        <Card key={c.id}>
          <CardHeader className="pb-3">
            <CardTitle className="flex items-center gap-2 text-base">
              <Trophy className="h-4 w-4 text-warning" />
              {c.name} <span className="text-sm font-normal text-muted-foreground">· {c.school}</span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
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
                  {c.rows.map((r, i) => {
                    const me = r.id === user.id;
                    return (
                      <tr
                        key={r.id}
                        className={cn("border-b border-border/60", me && "bg-primary/5 font-medium")}
                      >
                        <td className="py-2 pr-4 tabular-nums">
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
                        <td className="py-2 pr-4">
                          {r.name}
                          {me && <span className="ml-1.5 text-xs text-primary">(you)</span>}
                        </td>
                        <td className="py-2 pr-4 tabular-nums">{r.answered.toLocaleString()}</td>
                        <td className="py-2 pr-4 tabular-nums">{r.tests}</td>
                        <td className="py-2 tabular-nums">{r.best ?? "—"}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
