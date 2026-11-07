"use client";

import { ArrowRight, BookOpen, Clock, UserRound, Users } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { topicOf } from "@/lib/booking/topics";
import type { OpenSlot } from "@/server/actions/student/bookings";

import { Coins } from "./coins";
import { dayOfMonth, firstName, monthShort, timeRange, weekdayShort } from "./format";

/**
 * One bookable session.
 *
 * Read in this order: when (the date tile and time), what (title and topic),
 * who (the teacher), then what it costs and the action. The card itself is not
 * a button — only "Book this session" is — so there is one clear target.
 */
export function SessionCard({
  slot,
  cost,
  canAfford,
  onBook,
}: {
  slot: OpenSlot;
  cost: number;
  canAfford: boolean;
  onBook: () => void;
}) {
  const teacher = firstName(slot.hostName) ?? "A Scholarly mentor";
  const oneToOne = slot.seatsLeft === 1;

  return (
    <article className="group flex flex-col rounded-xl border border-border bg-card transition-colors hover:border-foreground/25">
      <div className="flex gap-4 p-5">
        <div
          className="flex w-[4.25rem] shrink-0 flex-col items-center justify-center self-start rounded-lg border border-border bg-secondary/50 py-2.5 text-center"
          aria-hidden
        >
          <span className="text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">
            {monthShort(slot.startsAt)}
          </span>
          <span className="font-display text-[1.65rem] font-semibold leading-none tabular-nums">
            {dayOfMonth(slot.startsAt)}
          </span>
          <span className="mt-0.5 text-[11px] text-muted-foreground">{weekdayShort(slot.startsAt)}</span>
        </div>

        <div className="min-w-0 flex-1">
          <p className="inline-flex max-w-full items-center gap-1.5 text-[13px] font-medium text-primary">
            <BookOpen className="h-3.5 w-3.5 shrink-0" aria-hidden />
            <span className="truncate">{topicOf(slot.subject)}</span>
          </p>
          <h3 className="mt-1 text-[17px] font-semibold leading-snug text-foreground">
            {slot.title ?? "1-on-1 session"}
          </h3>
          <dl className="mt-3 space-y-1.5 text-sm text-muted-foreground">
            <div className="flex items-center gap-2">
              <dt className="sr-only">Time</dt>
              <Clock className="h-4 w-4 shrink-0" aria-hidden />
              <dd className="font-medium text-foreground">
                {timeRange(slot.startsAt, slot.durationMinutes)}
                <span className="font-normal text-muted-foreground"> · {slot.durationMinutes} min</span>
              </dd>
            </div>
            <div className="flex items-center gap-2">
              <dt className="sr-only">Teacher</dt>
              <UserRound className="h-4 w-4 shrink-0" aria-hidden />
              <dd>with {teacher}</dd>
            </div>
            <div className="flex items-center gap-2">
              <dt className="sr-only">Format</dt>
              <Users className="h-4 w-4 shrink-0" aria-hidden />
              <dd>{oneToOne ? "1-on-1 · 1 seat left" : `${slot.seatsLeft} seats left`}</dd>
            </div>
          </dl>
        </div>
      </div>

      <div className="mt-auto flex flex-col gap-3 border-t border-border px-5 py-4 sm:flex-row sm:items-center sm:justify-between">
        <Coins value={cost} />
        <Button
          type="button"
          onClick={onBook}
          className="h-12 w-full gap-2 px-5 text-[15px] sm:w-auto"
          aria-label={`Book ${slot.title ?? "this session"} with ${teacher}`}
        >
          {canAfford ? "Book this session" : "See how to book"}
          <ArrowRight className="h-4 w-4" aria-hidden />
        </Button>
      </div>
    </article>
  );
}

export function SessionCardSkeleton() {
  return (
    <div className="rounded-xl border border-border bg-card" aria-hidden>
      <div className="flex gap-4 p-5">
        <Skeleton className="h-[4.75rem] w-[4.25rem] rounded-lg" />
        <div className="flex-1 space-y-2.5">
          <Skeleton className="h-3.5 w-24" />
          <Skeleton className="h-5 w-3/4" />
          <Skeleton className="h-4 w-1/2" />
          <Skeleton className="h-4 w-1/3" />
        </div>
      </div>
      <div className="flex items-center justify-between border-t border-border px-5 py-4">
        <Skeleton className="h-5 w-20" />
        <Skeleton className="h-12 w-40 rounded-lg" />
      </div>
    </div>
  );
}
