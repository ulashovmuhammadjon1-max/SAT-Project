import { EconomySettingsForm } from "@/components/admin/economy-settings-form";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LocalTime } from "@/components/shared/local-time";
import { listReferrals, readPlatformSettings } from "@/server/actions/admin/economy";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Economy" };
export const dynamic = "force-dynamic";

export default async function AdminEconomyPage() {
  const [{ current, defaults }, referrals, totals] = await Promise.all([
    readPlatformSettings(),
    listReferrals(50),
    prisma.coinTransaction.groupBy({
      by: ["type"],
      _sum: { amount: true },
      _count: { _all: true },
    }),
  ]);

  const circulating = await prisma.user.aggregate({ _sum: { coinBalance: true } });

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Economy</h1>
        <p className="text-sm text-muted-foreground">
          Coin settings, the booking price ladder, and referral records.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <Card>
          <CardContent className="p-4">
            <p className="text-xs text-muted-foreground">Coins in circulation</p>
            <p className="font-display text-2xl font-semibold tabular-nums">
              {circulating._sum.coinBalance ?? 0}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <p className="text-xs text-muted-foreground">Referrals rewarded</p>
            <p className="font-display text-2xl font-semibold tabular-nums">
              {referrals.filter((r) => r.status === "REWARDED").length}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-4">
            <p className="text-xs text-muted-foreground">Ledger entries</p>
            <p className="font-display text-2xl font-semibold tabular-nums">
              {totals.reduce((n, t) => n + t._count._all, 0)}
            </p>
          </CardContent>
        </Card>
      </div>

      <EconomySettingsForm current={current} defaults={defaults} />

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Recent referrals</CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          {referrals.length === 0 ? (
            <p className="p-6 text-sm text-muted-foreground">No referrals yet.</p>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead className="border-b border-border text-left text-xs text-muted-foreground">
                  <tr>
                    <th className="px-4 py-2 font-medium">Referrer</th>
                    <th className="px-4 py-2 font-medium">Joined</th>
                    <th className="px-4 py-2 font-medium">Code</th>
                    <th className="px-4 py-2 font-medium">Status</th>
                    <th className="px-4 py-2 font-medium">When</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-border">
                  {referrals.map((r) => (
                    <tr key={r.id}>
                      <td className="px-4 py-2">
                        <p className="font-medium">{r.referrer.name ?? "—"}</p>
                        <p className="text-xs text-muted-foreground">{r.referrer.email}</p>
                      </td>
                      <td className="px-4 py-2">
                        <p className="font-medium">{r.referredUser.name ?? "—"}</p>
                        <p className="text-xs text-muted-foreground">{r.referredUser.email}</p>
                      </td>
                      <td className="px-4 py-2 font-mono text-xs">{r.code}</td>
                      <td className="px-4 py-2">
                        <span
                          className={
                            r.status === "REWARDED"
                              ? "text-success"
                              : r.status === "VOID"
                                ? "text-destructive"
                                : "text-muted-foreground"
                          }
                        >
                          {r.status}
                        </span>
                      </td>
                      <td className="px-4 py-2 text-xs text-muted-foreground">
                        <LocalTime iso={r.createdAt.toISOString()} format="date" />
                      </td>
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
