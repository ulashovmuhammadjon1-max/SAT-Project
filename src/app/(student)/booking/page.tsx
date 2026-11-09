import Link from "next/link";
import { ArrowRight, Clock3, Coins as CoinsIcon, Compass, UserRoundCheck } from "lucide-react";

import { Button } from "@/components/ui/button";
import { BookingExperience } from "@/components/student/booking/booking-experience";
import { Coins } from "@/components/student/booking/coins";
import { LocalTime } from "@/components/shared/local-time";
import { ACTIVE_STATUSES } from "@/lib/booking/status";
import { topicOf } from "@/lib/booking/topics";
import { getBotUsername } from "@/lib/telegram";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getBookingContext, getOpenSlots } from "@/server/actions/student/bookings";

export const metadata = { title: "Sessions" };
export const dynamic = "force-dynamic";

const PROMISES = [
  { icon: Compass, title: "Pick your topic", body: "Choose the subject you want help with and a time that suits you." },
  { icon: UserRoundCheck, title: "Always 1-on-1", body: "Every session is just you and your mentor, shaped around your goals." },
  { icon: CoinsIcon, title: "Free to join", body: "Sessions use Scholarly coins, which you earn on the platform. No money." },
];

export default async function BookingPage({ searchParams }: { searchParams: { slot?: string } }) {
  const user = await requireUser();

  const [profile, slots, bookingContext, existing, botUsername] = await Promise.all([
    prisma.user.findUnique({
      where: { id: user.id },
      select: {
        name: true,
        email: true,
        currentScore: true,
        targetScore: true,
        satDate: true,
        weakestArea: true,
        telegramUserId: true,
        telegramUsername: true,
        telegramIsMember: true,
      },
    }),
    getOpenSlots(),
    getBookingContext(),
    // Explicit select: the slot row holds the host's Meet link, which a
    // student must not receive before approval.
    prisma.booking.findFirst({
      where: { userId: user.id, status: { in: ACTIVE_STATUSES } },
      select: {
        status: true,
        slot: {
          select: {
            startsAt: true,
            durationMinutes: true,
            title: true,
            subject: true,
            host: { select: { name: true } },
          },
        },
      },
    }),
    // Null unless a bot token is configured, which is what makes the widget
    // opt-in: without it the requirement falls back to the tick box.
    getBotUsername(),
  ]);

  const existingView = existing ? (
    <section
      aria-labelledby="existing-title"
      className="rounded-xl border border-border bg-card p-6 sm:p-8"
    >
      <p className="inline-flex items-center gap-2 text-sm font-medium text-muted-foreground">
        <Clock3 className="h-4 w-4" aria-hidden />
        {existing.status === "PENDING" ? "Pending approval" : "Confirmed"}
      </p>
      <h2 id="existing-title" className="mt-2 font-display text-xl font-semibold tracking-tight">
        You already have a session booked
      </h2>
      <p className="mt-2 max-w-xl text-[15px] leading-relaxed text-muted-foreground">
        You can hold one 1-on-1 session at a time. Once it has happened, or if you cancel it, you can book the next
        one here.
      </p>
      <div className="mt-5 rounded-lg border border-border p-4">
        <p className="text-[13px] font-medium text-primary">{topicOf(existing.slot.subject)}</p>
        <p className="mt-0.5 font-semibold">{existing.slot.title ?? "1-on-1 session"}</p>
        <p className="mt-1 text-sm text-muted-foreground">
          <LocalTime iso={existing.slot.startsAt.toISOString()} format="full" /> · {existing.slot.durationMinutes}{" "}
          min
          {existing.slot.host?.name ? ` · with ${existing.slot.host.name.split(/\s+/)[0]}` : ""}
        </p>
      </div>
      <Button asChild className="mt-6 h-12 w-full px-6 text-[15px] sm:w-auto">
        <Link href="/bookings">
          Open My Sessions <ArrowRight className="h-4 w-4" aria-hidden />
        </Link>
      </Button>
    </section>
  ) : null;

  return (
    <div className="space-y-10">
      <header className="space-y-6">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
          <div className="max-w-2xl">
            <h1 className="font-display text-3xl font-semibold tracking-tight sm:text-[2.25rem] sm:leading-tight">
              Find your next learning session
            </h1>
            <p className="mt-3 text-base leading-relaxed text-muted-foreground sm:text-[17px]">
              Explore personalised 1-on-1 sessions with experienced mentors and get help with the subjects and skills
              that matter to you.
            </p>
          </div>
          <div className="flex items-center gap-2 self-start rounded-full border border-border bg-card px-4 py-2 text-sm sm:self-auto">
            <span className="text-muted-foreground">Your balance</span>
            <Coins value={bookingContext.balance} size="sm" />
          </div>
        </div>

        <ul className="grid grid-cols-1 gap-px overflow-hidden rounded-xl border border-border bg-border sm:grid-cols-3">
          {PROMISES.map((p) => (
            <li key={p.title} className="flex gap-3 bg-card p-4 sm:p-5">
              <p.icon className="mt-0.5 h-5 w-5 shrink-0 text-primary" aria-hidden />
              <div>
                <p className="text-[15px] font-semibold">{p.title}</p>
                <p className="mt-0.5 text-sm leading-relaxed text-muted-foreground">{p.body}</p>
              </div>
            </li>
          ))}
        </ul>
      </header>

        <BookingExperience
          initialSlotId={typeof searchParams.slot === "string" ? searchParams.slot : null}
          existing={existingView}
          slots={slots}
          context={bookingContext}
          telegram={
            botUsername
              ? {
                  botUsername,
                  state: {
                    linked: Boolean(profile?.telegramUserId),
                    isMember: Boolean(profile?.telegramIsMember),
                    username: profile?.telegramUsername ?? null,
                  },
                }
              : null
          }
          prefill={{
            name: profile?.name ?? "",
            email: profile?.email ?? "",
            currentScore: profile?.currentScore ?? null,
            targetScore: profile?.targetScore ?? null,
            satDate: profile?.satDate ? profile.satDate.toISOString().slice(0, 10) : null,
            weakestArea: profile?.weakestArea ?? null,
          }}
        />
    </div>
  );
}
