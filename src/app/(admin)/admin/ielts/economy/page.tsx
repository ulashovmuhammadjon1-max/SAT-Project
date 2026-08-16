import { Gift, UserPlus, Users } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { FREE_REVIEWS, FRIENDS_PER_REVIEW } from "@/lib/ielts/economy";
import { shortName } from "@/lib/leaderboard";

export const metadata = { title: "IELTS Reviews & Invites" };
export const dynamic = "force-dynamic";

/**
 * The IELTS economy, which is a different economy from the SAT one.
 *
 * SAT runs on coins: earn them, spend them on sessions. IELTS runs on reviews:
 * one free, then two qualified friends buy the next. They share the `Referral`
 * table and nothing else, so this page is separate from `/admin/economy`
 * rather than a tab inside it — putting a coin balance next to a review balance
 * invites the assumption that one converts into the other.
 */
export default async function AdminIeltsEconomyPage() {
  await requireAdmin();

  const [writingSent, speakingSent, qualified, pending, students] = await Promise.all([
    prisma.ieltsWritingSubmission.count({ where: { status: { not: "PENDING" } } }),
    prisma.ieltsSpeakingSubmission.count({ where: { status: { not: "PENDING" } } }),
    prisma.referral.count({ where: { status: "REWARDED" } }),
    prisma.referral.count({ where: { status: "PENDING" } }),
    prisma.user.count({ where: { role: "STUDENT" } }),
  ]);

  const reviewsSpent = writingSent + speakingSent;

  // Per-student balances, computed the same way `getReviewAllowance` does —
  // in one pass rather than N queries, since this page lists everyone who has
  // used the product rather than one person.
  const [writingByUser, speakingByUser, referralsByUser] = await Promise.all([
    prisma.ieltsWritingSubmission.groupBy({
      by: ["userId"], where: { status: { not: "PENDING" } }, _count: { _all: true },
    }),
    prisma.ieltsSpeakingSubmission.groupBy({
      by: ["userId"], where: { status: { not: "PENDING" } }, _count: { _all: true },
    }),
    prisma.referral.groupBy({
      by: ["referrerId"], where: { status: "REWARDED" }, _count: { _all: true },
    }),
  ]);

  const used = new Map<string, number>();
  for (const r of [...writingByUser, ...speakingByUser]) {
    used.set(r.userId, (used.get(r.userId) ?? 0) + r._count._all);
  }
  const friends = new Map(referralsByUser.map((r) => [r.referrerId, r._count._all]));

  const ids = [...new Set([...used.keys(), ...friends.keys()])];
  const users = await prisma.user.findMany({
    where: { id: { in: ids } },
    select: { id: true, name: true, email: true },
  });

  const rows = users
    .map((u) => {
      const spent = used.get(u.id) ?? 0;
      const invited = friends.get(u.id) ?? 0;
      const allowance = FREE_REVIEWS + Math.floor(invited / FRIENDS_PER_REVIEW);
      return {
        id: u.id,
        name: u.name ?? u.email,
        invited,
        spent,
        remaining: Math.max(0, allowance - spent),
        // Someone who has spent everything and is waiting on friends is the
        // interesting row: they wanted another review and could not have one.
        blocked: allowance - spent <= 0,
      };
    })
    .sort((a, b) => b.spent - a.spent || b.invited - a.invited);

  const blocked = rows.filter((r) => r.blocked).length;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">
          Reviews &amp; Invites
        </h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          The first review is free; every {FRIENDS_PER_REVIEW} friends who join unlock one
          more. Nothing is stored — a balance is always the qualified referrals a student has
          minus the reviews they have sent, so it cannot drift.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardContent className="space-y-1 py-5">
            <Gift className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">{reviewsSpent}</p>
            <p className="text-sm text-muted-foreground">reviews requested</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <UserPlus className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">{qualified}</p>
            <p className="text-sm text-muted-foreground">
              friends qualified{pending > 0 && `, ${pending} pending`}
            </p>
          </CardContent>
        </Card>
        <Card className={blocked > 0 ? "border-amber-500/40" : undefined}>
          <CardContent className="space-y-1 py-5">
            <Users className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">{blocked}</p>
            <p className="text-sm text-muted-foreground">students out of reviews</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <Users className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {reviewsSpent > 0 ? (qualified / reviewsSpent).toFixed(2) : "—"}
            </p>
            <p className="text-sm text-muted-foreground">friends per review requested</p>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">Students</CardTitle>
          <p className="text-sm text-muted-foreground">
            {rows.length} of {students} students have used a review or invited someone.
            Names are shortened; email addresses are not shown.
          </p>
        </CardHeader>
        <CardContent className="p-0">
          {rows.length ? (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b text-left text-xs uppercase tracking-wide text-muted-foreground">
                    <th className="px-6 py-2 font-medium">Student</th>
                    <th className="px-3 py-2 text-right font-medium">Friends</th>
                    <th className="px-3 py-2 text-right font-medium">Used</th>
                    <th className="px-6 py-2 text-right font-medium">Left</th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map((r) => (
                    <tr key={r.id} className="border-b last:border-0">
                      <td className="truncate px-6 py-2">{shortName(r.name)}</td>
                      <td className="px-3 py-2 text-right tabular-nums">{r.invited}</td>
                      <td className="px-3 py-2 text-right tabular-nums">{r.spent}</td>
                      <td className="px-6 py-2 text-right">
                        {r.blocked ? (
                          <Badge variant="outline" className="border-amber-500/40 text-amber-700">
                            0
                          </Badge>
                        ) : (
                          <span className="font-semibold tabular-nums">{r.remaining}</span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p className="p-10 text-center text-sm text-muted-foreground">
              Nobody has requested a review or invited anyone yet.
            </p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
