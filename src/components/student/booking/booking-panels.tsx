"use client";

import Link from "next/link";
import { AlertTriangle, ArrowRight, BookOpen, CalendarDays, CheckCircle2, Clock, Loader2, UserRound } from "lucide-react";

import {
  AlertDialog,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import { Button } from "@/components/ui/button";
import { InstagramIcon, TelegramIcon } from "@/components/shared/brand-icons";
import { topicOf } from "@/lib/booking/topics";
import type { CommunityRequirement } from "@/lib/community";
import type { BookingContext, OpenSlot } from "@/server/actions/student/bookings";

import { Coins } from "./coins";
import { dayLong, firstName, timeRange, useMounted } from "./format";

/* -------------------------------------------------------------------------- */
/* What is being booked                                                        */
/* -------------------------------------------------------------------------- */

export function SessionFacts({ slot }: { slot: OpenSlot }) {
  const mounted = useMounted();
  const teacher = firstName(slot.hostName) ?? "A Scholarly mentor";
  return (
    <div>
      <p className="inline-flex items-center gap-1.5 text-[13px] font-medium text-primary">
        <BookOpen className="h-3.5 w-3.5" aria-hidden /> {topicOf(slot.subject)}
      </p>
      <p className="mt-1 text-lg font-semibold leading-snug">{slot.title ?? "1-on-1 session"}</p>
      <dl className="mt-4 space-y-2.5 text-[15px]">
        <Fact icon={CalendarDays} label="Date">
          {mounted ? dayLong(slot.startsAt) : "…"}
        </Fact>
        <Fact icon={Clock} label="Time">
          {mounted ? timeRange(slot.startsAt, slot.durationMinutes) : "…"}{" "}
          <span className="text-muted-foreground">({slot.durationMinutes} min)</span>
        </Fact>
        <Fact icon={UserRound} label="Teacher">
          {teacher} <span className="text-muted-foreground">· 1-on-1</span>
        </Fact>
      </dl>
    </div>
  );
}

function Fact({ icon: Icon, label, children }: { icon: typeof Clock; label: string; children: React.ReactNode }) {
  return (
    <div className="flex items-start gap-3">
      <Icon className="mt-0.5 h-4 w-4 shrink-0 text-muted-foreground" aria-hidden />
      <dt className="sr-only">{label}</dt>
      <dd>{children}</dd>
    </div>
  );
}

/** Balance → cost → balance after. The numbers come from the server. */
export function PriceBreakdown({ context }: { context: BookingContext }) {
  const after = context.balance - context.cost;
  return (
    <div className="space-y-3">
      <dl className="space-y-2 text-[15px]">
        <div className="flex items-center justify-between gap-4">
          <dt className="text-muted-foreground">Your balance</dt>
          <dd>
            <Coins value={context.balance} />
          </dd>
        </div>
        <div className="flex items-center justify-between gap-4">
          <dt className="text-muted-foreground">This session</dt>
          <dd className="font-medium">
            − <Coins value={context.cost} />
          </dd>
        </div>
        <div className="flex items-center justify-between gap-4 border-t border-border pt-2.5">
          <dt className="font-semibold">After booking</dt>
          <dd className={after < 0 ? "text-destructive" : undefined}>
            <Coins value={after} />
          </dd>
        </div>
      </dl>
      {context.previousBookings > 0 && context.costIncrement > 0 && (
        <p className="text-xs leading-relaxed text-muted-foreground">
          Sessions start at {context.baseCost} coins and go up by {context.costIncrement} for each one you have booked
          before, so free time reaches as many students as possible.
        </p>
      )}
      <p className="text-xs leading-relaxed text-muted-foreground">
        Coins are Scholarly points, not money. They are held when you book and returned in full if the booking is
        not approved
        {context.refundHours !== null
          ? `, or if you cancel at least ${context.refundHours} hours before it starts.`
          : "."}
      </p>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Final confirmation                                                          */
/* -------------------------------------------------------------------------- */

/**
 * The last word before coins move. It cannot be skipped: booking happens only
 * from its primary button. It states the consequence of a false confirmation
 * plainly, without shouting.
 */
export function ConfirmDialog({
  open,
  onOpenChange,
  slot,
  cost,
  requirements,
  pending,
  onConfirm,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  slot: OpenSlot;
  cost: number;
  requirements: CommunityRequirement[];
  pending: boolean;
  onConfirm: () => void;
}) {
  const mounted = useMounted();
  return (
    <AlertDialog open={open} onOpenChange={(o) => !pending && onOpenChange(o)}>
      <AlertDialogContent className="flex max-h-[calc(100dvh-2rem)] w-[calc(100vw-2rem)] max-w-lg flex-col gap-0 overflow-y-auto rounded-xl p-0">
        <div className="p-6 sm:p-7">
          <AlertDialogHeader className="space-y-3 text-left">
            <span className="flex h-12 w-12 items-center justify-center rounded-full bg-warning/15">
              <AlertTriangle className="h-6 w-6 text-warning" aria-hidden />
            </span>
            <AlertDialogTitle className="text-xl">Before you book: did you follow both accounts?</AlertDialogTitle>
            <AlertDialogDescription asChild>
              <div className="space-y-4 text-[15px] leading-relaxed text-muted-foreground">
                <p>
                  Reviewers check every booking.{" "}
                  <strong className="text-foreground">
                    If you have not followed, your booking will be cancelled
                  </strong>{" "}
                  and your coins returned.
                </p>
                <ul className="space-y-2">
                  {requirements.map((r) => {
                    const Icon = r.id === "instagram" ? InstagramIcon : TelegramIcon;
                    return (
                      <li key={r.id} className="flex items-center gap-3 rounded-lg bg-secondary/60 px-3 py-2.5">
                        <Icon className="h-5 w-5 shrink-0 text-foreground" />
                        <span className="min-w-0 text-sm">
                          <span className="text-foreground">{r.label}</span>{" "}
                          <a
                            href={r.href}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="font-medium text-primary underline-offset-4 hover:underline"
                          >
                            {r.handle}
                          </a>
                        </span>
                      </li>
                    );
                  })}
                </ul>
              </div>
            </AlertDialogDescription>
          </AlertDialogHeader>

          <div className="mt-5 flex flex-wrap items-center justify-between gap-3 rounded-lg border border-border p-4">
            <div className="min-w-0">
              <p className="truncate text-sm font-semibold">{slot.title ?? "1-on-1 session"}</p>
              <p className="text-sm text-muted-foreground">
                {mounted ? `${dayLong(slot.startsAt)}, ${timeRange(slot.startsAt, slot.durationMinutes)}` : "…"}
              </p>
            </div>
            <Coins value={cost} />
          </div>
        </div>

        {/* Stacked at every width: both labels are long, and side by side they
            outgrow the dialog. The primary action sits on top. */}
        <AlertDialogFooter className="flex-col-reverse gap-3 border-t border-border bg-secondary/40 p-4 sm:flex-col-reverse sm:justify-start sm:px-7 sm:py-5">
          <AlertDialogCancel disabled={pending} className="mt-0 h-12 w-full px-5 text-[15px]">
            Go back and follow first
          </AlertDialogCancel>
          <Button type="button" onClick={onConfirm} disabled={pending} className="h-12 w-full px-5 text-[15px]">
            {pending ? <Loader2 className="h-4 w-4 animate-spin" aria-hidden /> : <CheckCircle2 className="h-4 w-4" aria-hidden />}
            {pending ? "Booking…" : "I followed, book my session"}
          </Button>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
}

/* -------------------------------------------------------------------------- */
/* Not enough coins                                                            */
/* -------------------------------------------------------------------------- */

export function NotEnoughCoins({ context }: { context: BookingContext }) {
  const friends = Math.ceil(context.shortfall / Math.max(1, context.referralRewardCoins));
  return (
    <div className="space-y-5">
      <div>
        <p className="text-lg font-semibold">You need {context.shortfall} more coins for this session</p>
        <p className="mt-1.5 text-[15px] leading-relaxed text-muted-foreground">
          It costs <strong className="text-foreground">{context.cost} coins</strong> and you have{" "}
          <strong className="text-foreground">{context.balance}</strong>. Coins are free to earn, and nothing is charged
          until you can afford it.
        </p>
      </div>
      <div className="rounded-xl border border-border bg-secondary/40 p-5">
        <p className="font-semibold">The quickest way to earn them</p>
        <p className="mt-1 text-[15px] leading-relaxed text-muted-foreground">
          Invite a friend and get {context.referralRewardCoins} coins when they join. You are {friends}{" "}
          {friends === 1 ? "friend" : "friends"} away.
        </p>
        <Button asChild className="mt-4 h-12 w-full px-5 text-[15px] sm:w-auto">
          <Link href="/invite">
            Invite friends <ArrowRight className="h-4 w-4" aria-hidden />
          </Link>
        </Button>
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Success                                                                     */
/* -------------------------------------------------------------------------- */

export function BookingSuccess({
  slot,
  coinsSpent,
  balance,
  email,
}: {
  slot: OpenSlot;
  coinsSpent: number;
  balance: number;
  email: string;
}) {
  const steps = [
    "Your mentor and the review team check your request, including the community follow.",
    `Once it is approved you get an email at ${email || "your address"} with the join link.`,
    "Your coins are held until then, and returned in full if the request is not approved.",
  ];
  return (
    <section
      aria-labelledby="success-title"
      className="mx-auto max-w-2xl rounded-2xl border border-border bg-card p-6 text-center sm:p-10"
    >
      <span className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-success/15 motion-safe:animate-pop-in">
        <CheckCircle2 className="h-9 w-9 text-success" aria-hidden />
      </span>
      <h2 id="success-title" className="mt-5 font-display text-2xl font-semibold tracking-tight" tabIndex={-1}>
        Request sent
      </h2>
      <p className="mt-2 text-[15px] text-muted-foreground">
        Your booking is <strong className="text-foreground">pending approval</strong>. It is not confirmed yet.
      </p>

      <div className="mt-7 rounded-xl border border-border p-5 text-left">
        <SessionFacts slot={slot} />
        <p className="mt-4 flex flex-wrap items-center gap-x-2 border-t border-border pt-4 text-sm text-muted-foreground">
          Held <Coins value={coinsSpent} size="sm" className="text-foreground" /> · balance now{" "}
          <Coins value={balance} size="sm" className="text-foreground" />
        </p>
      </div>

      <div className="mt-7 text-left">
        <p className="text-sm font-semibold">What happens next</p>
        <ol className="mt-3 space-y-3">
          {steps.map((s, i) => (
            <li key={s} className="flex gap-3 text-[15px] leading-relaxed text-muted-foreground">
              <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-secondary text-sm font-semibold text-foreground">
                {i + 1}
              </span>
              {s}
            </li>
          ))}
        </ol>
      </div>

      <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:justify-center">
        <Button asChild className="h-12 px-6 text-[15px]">
          <Link href="/bookings">
            Go to My Sessions <ArrowRight className="h-4 w-4" aria-hidden />
          </Link>
        </Button>
        <Button asChild variant="outline" className="h-12 px-6 text-[15px]">
          <Link href="/dashboard">Back to Home</Link>
        </Button>
      </div>
    </section>
  );
}
