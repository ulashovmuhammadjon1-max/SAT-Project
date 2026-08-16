import Link from "next/link";
import { Gift, UserPlus } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { cn } from "@/lib/utils";
import { FRIENDS_PER_REVIEW, type ReviewAllowance } from "@/lib/ielts/economy";

/**
 * The review balance, shown above the Writing and Speaking lists.
 *
 * It sits where the student decides what to do next rather than only on the
 * invite page, because "I have no reviews left" is information you need
 * *before* spending forty minutes on a Task 2 — finding out at the Submit
 * button is finding out too late.
 */
export function ReviewBalance({ allowance }: { allowance: ReviewAllowance }) {
  const out = allowance.remaining <= 0;

  return (
    <Card className={cn(out ? "border-amber-500/40" : "border-emerald-600/40")}>
      <CardContent className="flex flex-wrap items-center justify-between gap-4 py-4">
        <div className="flex items-start gap-3">
          {out ? (
            <UserPlus className="mt-0.5 h-5 w-5 shrink-0 text-amber-600" />
          ) : (
            <Gift className="mt-0.5 h-5 w-5 shrink-0 text-emerald-600" />
          )}
          <div>
            <p className="text-sm font-semibold">
              {out
                ? `Invite ${allowance.friendsNeeded} more ${
                    allowance.friendsNeeded === 1 ? "friend" : "friends"
                  } to unlock your next review`
                : allowance.onFreeReview
                  ? "Your first review is free"
                  : `${allowance.remaining} ${
                      allowance.remaining === 1 ? "review" : "reviews"
                    } available`}
            </p>
            <p className="text-sm text-muted-foreground">
              {out
                ? "Keep writing and recording — everything is saved, and you can send it the moment a review is free."
                : `Every ${FRIENDS_PER_REVIEW} friends who join unlock one more.`}
            </p>
          </div>
        </div>
        <Link
          href="/ielts/invite"
          className="shrink-0 text-sm font-medium underline underline-offset-4"
        >
          {out ? "Get your invite link" : "Invite friends"}
        </Link>
      </CardContent>
    </Card>
  );
}
