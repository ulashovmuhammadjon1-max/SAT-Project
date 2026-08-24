import Link from "next/link";
import { CheckCircle2, Clock, Users } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { CoinAmount } from "@/components/student/coin-badge";
import { ReferralLink } from "@/components/student/referral-link";
import { LocalTime } from "@/components/shared/local-time";
import { getMyReferrals } from "@/server/actions/student/wallet";

export const metadata = { title: "Invite friends" };
export const dynamic = "force-dynamic";

export default async function InvitePage() {
  const r = await getMyReferrals();

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Invite friends</h1>
        <p className="text-sm text-muted-foreground">
          Scholarly is free because it grows by word of mouth. Bring someone with you.
        </p>
      </div>

      <Card className="overflow-hidden border-primary/30 bg-gradient-to-br from-primary/10 via-primary/5 to-transparent">
        <CardContent className="space-y-5 p-6 sm:p-8">
          <div className="flex flex-wrap items-baseline gap-x-2">
            <span className="font-display text-xl font-semibold">Earn</span>
            <CoinAmount value={r.rewardPerReferral} size="lg" />
            <span className="font-display text-xl font-semibold">for every friend who joins</span>
          </div>
          <p className="text-sm text-muted-foreground">
            The reward lands when they actually create an account — not when you send the link.
          </p>
          <ReferralLink link={r.link} reward={r.rewardPerReferral} />
          <p className="text-xs text-muted-foreground">
            Your code: <span className="font-mono font-semibold text-foreground">{r.code}</span>
          </p>
        </CardContent>
      </Card>

      <div className="grid gap-4 sm:grid-cols-3">
        <StatTile icon={Users} label="Friends joined" value={String(r.rewarded)} />
        <StatTile icon={Clock} label="Pending" value={String(r.pending)} />
        <StatTile
          icon={CheckCircle2}
          label="Coins earned"
          value={`+${r.coinsEarned}`}
          accent
        />
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Your invites</CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          {r.recent.length === 0 ? (
            <div className="p-8 text-center">
              <Users className="mx-auto mb-3 h-10 w-10 text-muted-foreground" />
              <p className="font-medium">No invites yet</p>
              <p className="mt-1 text-sm text-muted-foreground">
                Share your link in a class group chat — that is where it works best.
              </p>
            </div>
          ) : (
            <ul className="divide-y divide-border">
              {r.recent.map((item) => (
                <li key={item.id} className="flex items-center gap-4 px-4 py-3 sm:px-6">
                  <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-secondary text-sm font-semibold">
                    {item.name.charAt(0).toUpperCase()}
                  </span>
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">{item.name}</p>
                    <p className="text-xs text-muted-foreground">
                      joined <LocalTime iso={item.joinedAt.toISOString()} format="date" />
                    </p>
                  </div>
                  {item.status === "REWARDED" ? (
                    <CoinAmount value={r.rewardPerReferral} size="sm" signed className="text-success" />
                  ) : (
                    <span className="text-xs font-medium text-muted-foreground">
                      {item.status === "PENDING" ? "Pending" : "Not eligible"}
                    </span>
                  )}
                </li>
              ))}
            </ul>
          )}
        </CardContent>
      </Card>

      <Card className="bg-secondary/40">
        <CardContent className="p-5 text-sm text-muted-foreground">
          <p className="font-medium text-foreground">How it works</p>
          <ol className="mt-2 list-decimal space-y-1 pl-5">
            <li>Share your link with a friend.</li>
            <li>They create a Scholarly account through it.</li>
            <li>
              You get {r.rewardPerReferral} coins automatically — check your{" "}
              <Link href="/wallet" className="font-medium text-primary underline-offset-4 hover:underline">
                wallet
              </Link>
              .
            </li>
          </ol>
          <p className="mt-3 text-xs">
            Each account can only be referred once, and referring yourself doesn&apos;t count.
          </p>
        </CardContent>
      </Card>
    </div>
  );
}

function StatTile({
  icon: Icon,
  label,
  value,
  accent,
}: {
  icon: typeof Users;
  label: string;
  value: string;
  accent?: boolean;
}) {
  return (
    <Card>
      <CardContent className="flex items-center gap-3 p-4">
        <span className="flex h-10 w-10 items-center justify-center rounded-lg bg-secondary text-muted-foreground">
          <Icon className="h-5 w-5" />
        </span>
        <div>
          <p className="text-xs text-muted-foreground">{label}</p>
          <p
            className={`font-display text-xl font-semibold tabular-nums ${accent ? "text-success" : ""}`}
          >
            {value}
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
