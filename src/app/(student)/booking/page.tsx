import Link from "next/link";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { BookingForm } from "@/components/student/booking-form";
import { LocalTime } from "@/components/shared/local-time";
import { ACTIVE_STATUSES } from "@/lib/booking/status";
import { getBotUsername } from "@/lib/telegram";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getBookingContext, getOpenSlots } from "@/server/actions/student/bookings";

export const metadata = { title: "Sessions" };
export const dynamic = "force-dynamic";

export default async function BookingPage() {
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
    prisma.booking.findFirst({
      where: { userId: user.id, status: { in: ACTIVE_STATUSES } },
      include: { slot: true },
    }),
    // Null unless a bot token is configured, which is what makes the widget
    // opt-in: without it the requirement falls back to the tick box.
    getBotUsername(),
  ]);

  if (existing) {
    return (
      <div className="mx-auto max-w-2xl space-y-6">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Sessions</h1>
        <Card>
          <CardContent className="space-y-3 p-6">
            <p className="font-medium">You already have a session booked.</p>
            <p className="text-sm text-muted-foreground">
              <LocalTime iso={existing.slot.startsAt.toISOString()} format="full" />
            </p>
            <Button asChild>
              <Link href="/bookings">View my booking</Link>
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight sm:text-3xl">Sessions</h1>
        <p className="mt-2 text-[15px] leading-relaxed text-muted-foreground">
          Book a free one-to-one hour with a Scholarly mentor. Pick a topic you want help with, then a time
          that suits you.
        </p>
      </div>

      <BookingForm
        slots={slots}
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
        context={bookingContext}
      />
    </div>
  );
}
