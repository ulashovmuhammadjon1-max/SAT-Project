import Link from "next/link";
import { headers } from "next/headers";
import { CheckCircle2, Clock, Gift, Mic, PenLine, UserPlus } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ReferralLink } from "@/components/student/referral-link";
import { getReferralSummary } from "@/lib/referrals";
import {
  FREE_REVIEWS, FRIENDS_PER_REVIEW, getReviewAllowance,
} from "@/lib/ielts/economy";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Invite Friends" };
export const dynamic = "force-dynamic";

/**
 * How a student earns more free reviews.
 *
 * The page leads with the balance rather than the invite link, because the
 * question a student arrives with is "can I send this essay?", not "what is my
 * code?". The link is what they need second.
 */
export default async function IeltsInvitePage() {
  const user = await requireUser();
  const host = headers().get("host") ?? "scholarly.space";
  const proto = headers().get("x-forwarded-proto") ?? "https";

  const [summary, allowance] = await Promise.all([
    getReferralSummary(user.id, `${proto}://${host}`),
    getReviewAllowance(user.id),
  ]);

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Invite Friends</h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Your first review is free. After that, every {FRIENDS_PER_REVIEW} friends who join
          unlock one more — a real person reads or listens to your work and scores it, and
          that time has to come from somewhere.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        <Card className={cn(allowance.remaining > 0 && "border-emerald-600/40")}>
          <CardContent className="space-y-1 py-5">
            <Gift
              className={cn(
                "h-4 w-4",
                allowance.remaining > 0 ? "text-emerald-600" : "text-muted-foreground"
              )}
            />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {allowance.remaining}
            </p>
            <p className="text-sm text-muted-foreground">
              {allowance.remaining === 1 ? "review available" : "reviews available"}
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <CheckCircle2 className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">
              {allowance.qualifiedFriends}
            </p>
            <p className="text-sm text-muted-foreground">friends joined</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="space-y-1 py-5">
            <Clock className="h-4 w-4 text-muted-foreground" />
            <p className="font-display text-3xl font-semibold tabular-nums">{allowance.used}</p>
            <p className="text-sm text-muted-foreground">
              {allowance.used === 1 ? "review used" : "reviews used"}
            </p>
          </CardContent>
        </Card>
      </div>

      {/* Progress toward the next review, drawn as the friends themselves
          rather than a percentage — two of two is a countable thing and a
          progress bar would abstract away exactly what the student has to do. */}
      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">
            {allowance.remaining > 0
              ? allowance.onFreeReview
                ? `Your ${FREE_REVIEWS === 1 ? "free review" : "free reviews"} is ready to use`
                : "You have a review in hand"
              : `${allowance.friendsNeeded} more ${
                  allowance.friendsNeeded === 1 ? "friend" : "friends"
                } unlocks your next review`}
          </CardTitle>
          <p className="text-sm text-muted-foreground">
            {allowance.remaining > 0
              ? "Send a Writing task or a Speaking interview whenever you are ready."
              : "Your drafts and recordings are saved. Nothing is lost while you wait."}
          </p>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center gap-2">
            {Array.from({ length: FRIENDS_PER_REVIEW }, (_, i) => (
              <span
                key={i}
                className={cn(
                  "flex h-9 w-9 items-center justify-center rounded-full border",
                  i < allowance.towardNext
                    ? "border-emerald-600 bg-emerald-600 text-white"
                    : "border-dashed border-border text-muted-foreground"
                )}
                aria-hidden
              >
                <UserPlus className="h-4 w-4" />
              </span>
            ))}
            <span className="ml-1 text-sm text-muted-foreground">
              {allowance.towardNext} of {FRIENDS_PER_REVIEW} toward the next review
            </span>
          </div>

          <ReferralLink
            link={summary.link}
            shareText={
              "Free IELTS Writing and Speaking practice, marked by a real person — " +
              "join me on Scholarly."
            }
          />
          <p className="text-xs text-muted-foreground">
            Or share your code: <span className="font-mono font-semibold">{summary.code}</span>
          </p>

          <div className="flex flex-wrap gap-3 text-sm">
            <Link href="/ielts/writing" className="inline-flex items-center gap-1.5 underline">
              <PenLine className="h-3.5 w-3.5" /> Writing
            </Link>
            <Link href="/ielts/speaking" className="inline-flex items-center gap-1.5 underline">
              <Mic className="h-3.5 w-3.5" /> Speaking
            </Link>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="pb-3">
          <CardTitle className="text-base">Who you have invited</CardTitle>
          <p className="text-sm text-muted-foreground">
            A friend counts once their account qualifies, which is not the instant they sign
            up — that gap is what stops one person inviting themselves ten times.
          </p>
        </CardHeader>
        <CardContent className="p-0">
          {summary.recent.length ? (
            <ol>
              {summary.recent.map((r) => (
                <li
                  key={r.id}
                  className="flex items-center justify-between gap-3 border-b px-6 py-2.5 last:border-0"
                >
                  <span className="truncate text-sm">{r.name}</span>
                  <span className="flex items-center gap-3">
                    <span className="hidden text-xs text-muted-foreground sm:inline">
                      {new Date(r.joinedAt).toLocaleDateString()}
                    </span>
                    <Badge
                      variant={r.status === "REWARDED" ? "navy" : "outline"}
                      className={r.status === "VOID" ? "text-muted-foreground" : undefined}
                    >
                      {r.status === "REWARDED"
                        ? "Counted"
                        : r.status === "PENDING"
                          ? "Pending"
                          : "Not counted"}
                    </Badge>
                  </span>
                </li>
              ))}
            </ol>
          ) : (
            <p className="p-10 text-center text-sm text-muted-foreground">
              Nobody yet. Share your link above — the first {FRIENDS_PER_REVIEW} friends who
              join earn you a review.
            </p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
