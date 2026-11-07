import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { GrantCoinsForm } from "@/components/admin/grant-coins-form";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Give Coins" };
export const dynamic = "force-dynamic";

const who = (u: { name: string | null; username: string | null; email: string | null } | null) =>
  u ? (u.name ?? (u.username ? `@${u.username}` : u.email ?? "—")) : "—";

export default async function GiveCoinsPage() {
  await requireAdmin();

  // Every admin grant, newest first: positive ADMIN_ADJUSTMENT rows made by
  // an admin. Referral reversals are negative and excluded.
  const recent = await prisma.coinTransaction.findMany({
    where: { type: "ADMIN_ADJUSTMENT", amount: { gt: 0 }, actorId: { not: null } },
    orderBy: { createdAt: "desc" },
    take: 25,
    select: {
      id: true,
      amount: true,
      description: true,
      createdAt: true,
      user: { select: { name: true, username: true, email: true } },
      actor: { select: { name: true, username: true, email: true } },
    },
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Give Coins</h1>
        <p className="text-sm text-muted-foreground">
          Add coins to any account. Each grant is recorded with your name and reason, and shows in the
          student&apos;s wallet history.
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Add coins</CardTitle>
          <CardDescription>Up to 10,000 coins at a time. A reason of at least 10 words is required.</CardDescription>
        </CardHeader>
        <CardContent>
          <GrantCoinsForm />
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Recent grants</CardTitle>
        </CardHeader>
        <CardContent>
          {recent.length === 0 ? (
            <p className="text-sm text-muted-foreground">No coins have been given yet.</p>
          ) : (
            <ul className="divide-y divide-border">
              {recent.map((t) => (
                <li key={t.id} className="flex flex-wrap items-start justify-between gap-3 py-3">
                  <div className="min-w-[240px] flex-1">
                    <p className="text-sm">
                      <span className="font-medium">+{t.amount}</span> to <span className="font-medium">{who(t.user)}</span>
                      <span className="text-muted-foreground"> · by {who(t.actor)}</span>
                    </p>
                    <p className="mt-0.5 text-sm text-muted-foreground">{t.description}</p>
                  </div>
                  <p className="text-xs text-muted-foreground">{t.createdAt.toLocaleDateString()}</p>
                </li>
              ))}
            </ul>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
