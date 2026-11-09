import Link from "next/link";
import { ArrowRight, CalendarPlus, UserRound } from "lucide-react";

import { Button } from "@/components/ui/button";
import { LocalTime } from "@/components/shared/local-time";
import { ACTIVE_STATUSES } from "@/lib/booking/status";
import { topicOf } from "@/lib/booking/topics";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getOpenSlots } from "@/server/actions/student/bookings";

/**
 * The open 1-on-1 sessions, shown where students already are (Home and SAT
 * home) instead of only on /booking, which most students never opened: six
 * sessions sat unbooked while students practised a click away.
 *
 * Renders nothing when there is nothing to book, or when the student already
 * holds a session (one active booking at a time; the dashboard shows that one).
 * Each row opens the booking flow for that exact session.
 */
export async function OpenSessionsCard({ limit = 3 }: { limit?: number }) {
  const user = await requireUser();
  const [slots, active] = await Promise.all([
    getOpenSlots(),
    prisma.booking.count({ where: { userId: user.id, status: { in: ACTIVE_STATUSES } } }),
  ]);
  if (slots.length === 0 || active > 0) return null;
  const shown = slots.slice(0, limit);

  return (
    <section
      aria-labelledby="open-sessions-heading"
      className="overflow-hidden rounded-2xl border border-primary/25 bg-gradient-to-br from-primary/[0.07] via-card to-card shadow-sm"
    >
      <div className="flex flex-wrap items-center justify-between gap-3 px-5 pb-3 pt-5 sm:px-6">
        <div className="min-w-0">
          <p className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-primary">
            <CalendarPlus className="h-3.5 w-3.5" /> Free 1-on-1 sessions
          </p>
          <h2 id="open-sessions-heading" className="mt-1 font-display text-lg font-semibold tracking-tight">
            {slots.length === 1 ? "1 session is open to book" : `${slots.length} sessions are open to book`}
          </h2>
          <p className="text-sm text-muted-foreground">Just you and a mentor, on the topic you pick. Paid with Scholarly coins.</p>
        </div>
        {slots.length > shown.length && (
          <Button asChild variant="outline" size="sm" className="shrink-0">
            <Link href="/booking">
              See all {slots.length} <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </Button>
        )}
      </div>

      <ul className="divide-y divide-border/70 border-t border-border/70">
        {shown.map((s) => (
          <li key={s.id}>
            <Link
              href={`/booking?slot=${s.id}`}
              className="group flex items-center gap-4 px-5 py-3.5 transition-colors hover:bg-primary/[0.04] sm:px-6"
            >
              <span className="flex w-16 shrink-0 flex-col items-center rounded-xl border border-border bg-background py-1.5 text-center">
                <SlotDay iso={s.startsAt.toISOString()} />
              </span>
              <span className="min-w-0 flex-1">
                <span className="block truncate font-medium">{s.title ?? topicOf(s.subject)}</span>
                <span className="mt-0.5 flex flex-wrap items-center gap-x-2 gap-y-0.5 text-sm text-muted-foreground">
                  <LocalTime iso={s.startsAt.toISOString()} format="time" />
                  <span aria-hidden>·</span>
                  <span>{s.durationMinutes} min</span>
                  {s.hostName && (
                    <>
                      <span aria-hidden className="hidden sm:inline">·</span>
                      <span className="inline-flex basis-full items-center gap-1 sm:basis-auto">
                        <UserRound className="h-3.5 w-3.5" /> {s.hostName}
                      </span>
                    </>
                  )}
                </span>
              </span>
              <span className="hidden shrink-0 items-center gap-1 text-sm font-semibold text-primary sm:flex">
                Book <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </span>
              <ArrowRight aria-hidden className="h-4 w-4 shrink-0 text-primary sm:hidden" />
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}

/** Weekday over day-of-month, in the student's own timezone. */
function SlotDay({ iso }: { iso: string }) {
  return (
    <>
      <LocalTime iso={iso} format="weekdayShort" className="text-[11px] font-semibold uppercase tracking-wide text-primary" />
      <LocalTime iso={iso} format="dayMonth" className="font-display text-base font-semibold leading-tight tabular-nums" />
    </>
  );
}
