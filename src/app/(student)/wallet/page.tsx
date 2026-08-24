import Link from "next/link";
import { ArrowDownLeft, ArrowUpRight, CalendarCheck, Gift, Sparkles, UserPlus } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { CoinAmount, CoinIcon } from "@/components/student/coin-badge";
import { LocalTime } from "@/components/shared/local-time";
import { getWallet } from "@/server/actions/student/wallet";
import { cn } from "@/lib/utils";

export const metadata = { title: "Scholarly Coins" };
export const dynamic = "force-dynamic";

/** Icon per ledger entry type, so the history scans without reading every row. */
const TYPE_META: Record<string, { icon: typeof Gift; label: string }> = {
  SIGNUP_BONUS: { icon: Sparkles, label: "Welcome bonus" },
  REFERRAL_REWARD: { icon: UserPlus, label: "Friend referral" },
  BOOKING_SPEND: { icon: CalendarCheck, label: "1-on-1 session" },
  BOOKING_REFUND: { icon: ArrowDownLeft, label: "Session refund" },
  ADMIN_ADJUSTMENT: { icon: Gift, label: "Adjustment" },
  PROMOTION: { icon: Gift, label: "Promotion" },
};

export default async function WalletPage() {
  const wallet = await getWallet();

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Scholarly Coins</h1>
        <p className="text-sm text-muted-foreground">
          Earn coins by growing the community. Spend them on 1-on-1 guidance.
        </p>
      </div>

      {/* Balance. The gradient echoes the landing hero rather than introducing
          a second visual language for the same product. */}
      <Card className="overflow-hidden border-primary/30 bg-gradient-to-br from-primary/10 via-primary/5 to-transparent">
        <CardContent className="flex flex-wrap items-center justify-between gap-6 p-6 sm:p-8">
          <div>
            <p className="text-sm font-medium text-muted-foreground">Current balance</p>
            <div className="mt-1 flex items-baseline gap-2">
              <CoinAmount value={wallet.balance} size="xl" />
            </div>
            <p className="mt-2 text-sm text-muted-foreground">
              {wallet.totalEarned} earned · {wallet.totalSpent} spent
            </p>
          </div>
          <div className="flex flex-wrap gap-2">
            <Button asChild>
              <Link href="/invite">
                <UserPlus className="mr-2 h-4 w-4" />
                Invite friends
              </Link>
            </Button>
            <Button asChild variant="outline">
              <Link href="/booking">Book 1-on-1</Link>
            </Button>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Transaction history</CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          {wallet.transactions.length === 0 ? (
            <div className="p-8 text-center">
              <CoinIcon className="mx-auto mb-3 h-10 w-10 text-lg" />
              <p className="font-medium">No transactions yet</p>
              <p className="mt-1 text-sm text-muted-foreground">
                Your welcome coins and every reward will show up here.
              </p>
            </div>
          ) : (
            <ul className="divide-y divide-border">
              {wallet.transactions.map((t) => {
                const meta = TYPE_META[t.type] ?? { icon: Gift, label: t.type };
                const Icon = meta.icon;
                const positive = t.amount > 0;
                return (
                  <li key={t.id} className="flex items-center gap-4 px-4 py-3 sm:px-6">
                    <span
                      className={cn(
                        "flex h-9 w-9 shrink-0 items-center justify-center rounded-full",
                        positive
                          ? "bg-success/10 text-success"
                          : "bg-muted text-muted-foreground",
                      )}
                    >
                      <Icon className="h-4 w-4" />
                    </span>
                    <div className="min-w-0 flex-1">
                      <p className="truncate text-sm font-medium">{t.description}</p>
                      <p className="text-xs text-muted-foreground">
                        {meta.label} · <LocalTime iso={t.createdAt.toISOString()} format="date" />
                      </p>
                    </div>
                    <div className="text-right">
                      <p
                        className={cn(
                          "flex items-center justify-end gap-1 text-sm font-semibold tabular-nums",
                          positive ? "text-success" : "text-foreground",
                        )}
                      >
                        {positive ? (
                          <ArrowUpRight className="h-3.5 w-3.5" />
                        ) : (
                          <ArrowDownLeft className="h-3.5 w-3.5" />
                        )}
                        {positive ? "+" : ""}
                        {t.amount}
                      </p>
                      <p className="text-xs text-muted-foreground tabular-nums">
                        balance {t.balanceAfter}
                      </p>
                    </div>
                  </li>
                );
              })}
            </ul>
          )}
        </CardContent>
      </Card>

      {wallet.hasMore && (
        <p className="text-center text-sm text-muted-foreground">
          Showing your 25 most recent transactions.
        </p>
      )}
    </div>
  );
}
