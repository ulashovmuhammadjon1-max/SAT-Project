import { SlotCreator, SlotTable, type AdminSlotRow } from "@/components/admin/booking-admin";
import { EventCreator } from "@/components/admin/event-creator";
import {
  NextSessionPanel,
  RoomLinkCard,
  type NextSessionInfo,
} from "@/components/admin/next-session-panel";
import { Card, CardContent } from "@/components/ui/card";
import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { getSettings } from "@/lib/settings";

export const metadata = { title: "Sessions" };
export const dynamic = "force-dynamic";

export default async function AdminBookingsPage() {
  await requireAdmin();

  const [slots, settings] = await Promise.all([
    prisma.mentorSlot.findMany({
      orderBy: { startsAt: "asc" },
      include: {
        bookings: {
          where: { status: { in: SEAT_HOLDING_STATUSES } },
          // The verified answer to "did this student actually subscribe", which
          // is the whole reason the un-approve button exists.
          include: {
            user: {
              select: {
                telegramUserId: true,
                telegramUsername: true,
                telegramIsMember: true,
                telegramCheckedAt: true,
                telegramManualOverride: true,
              },
            },
          },
        },
      },
    }),
    getSettings(),
  ]);

  // The room the mentor joins when there is no per-booking link.
  const roomUrl = settings.staticMeetingUrl || process.env.MEETING_STATIC_URL || null;

  const nextSlot = slots.find(
    (s) => s.bookings.some((b) => b.status === "UPCOMING") && s.startsAt > new Date(),
  );
  const nextBooking = nextSlot?.bookings.find((b) => b.status === "UPCOMING") ?? null;
  const nextSession: NextSessionInfo | null =
    nextSlot && nextBooking
      ? {
          bookingId: nextBooking.id,
          startsAt: nextSlot.startsAt.toISOString(),
          durationMinutes: nextSlot.durationMinutes,
          name: nextBooking.name,
          email: nextBooking.email,
          currentScore: nextBooking.currentScore,
          targetScore: nextBooking.targetScore,
          weakestArea: nextBooking.weakestArea,
          notes: nextBooking.notes,
          timezone: nextBooking.timezone,
          // Bookings made before a provider existed have no link of their own;
          // fall back to the standing room rather than showing nothing.
          meetingUrl: nextBooking.meetingUrl ?? roomUrl,
        }
      : null;

  const upcoming = slots.filter(
    (s) => s.bookings.some((b) => b.status === "UPCOMING") && s.startsAt > new Date()
  ).length;
  const awaiting = slots.filter((s) => s.bookings.some((b) => b.status === "PENDING")).length;
  const open = slots.filter(
    (s) => !s.isBlocked && s.startsAt > new Date() && s.bookings.length < s.capacity
  ).length;

  const rows: AdminSlotRow[] = slots.map((s) => ({
    id: s.id,
    startsAt: s.startsAt.toISOString(),
    durationMinutes: s.durationMinutes,
    isBlocked: s.isBlocked,
    booking: s.bookings[0]
      ? {
          id: s.bookings[0].id,
          status: s.bookings[0].status,
          statusReason: s.bookings[0].statusReason,
          name: s.bookings[0].name,
          email: s.bookings[0].email,
          currentScore: s.bookings[0].currentScore,
          targetScore: s.bookings[0].targetScore,
          satDate: s.bookings[0].satDate ? s.bookings[0].satDate.toISOString() : null,
          studyHoursPerWeek: s.bookings[0].studyHoursPerWeek,
          weakestArea: s.bookings[0].weakestArea,
          notes: s.bookings[0].notes,
          timezone: s.bookings[0].timezone,
          telegram: s.bookings[0].user
            ? {
                linked: Boolean(s.bookings[0].user.telegramUserId),
                username: s.bookings[0].user.telegramUsername,
                isMember: s.bookings[0].user.telegramIsMember,
                checkedAt: s.bookings[0].user.telegramCheckedAt
                  ? s.bookings[0].user.telegramCheckedAt.toISOString()
                  : null,
                manual: s.bookings[0].user.telegramManualOverride,
              }
            : null,
        }
      : null,
  }));

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Sessions</h1>
        <p className="text-sm text-muted-foreground">
          Publish availability and manage free 1-on-1 bookings.
        </p>
      </div>

      <NextSessionPanel session={nextSession} />

      <RoomLinkCard url={roomUrl} provider={settings.meetingProvider} />

      <EventCreator />

      <div className="grid gap-3 sm:grid-cols-4">
        {/* Awaiting approval leads, because it is the only tile that is a
            to-do list rather than a status readout. */}
        <Stat label="Awaiting approval" value={awaiting} />
        <Stat label="Upcoming sessions" value={upcoming} />
        <Stat label="Open slots" value={open} />
        <Stat label="Total slots" value={slots.length} />
      </div>

      <SlotCreator />

      <div>
        <h2 className="font-display text-lg font-semibold">All slots</h2>
        <div className="mt-3">
          <SlotTable slots={rows} />
        </div>
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: number }) {
  return (
    <Card>
      <CardContent className="p-4">
        <p className="font-display text-2xl font-semibold tabular-nums">{value}</p>
        <p className="mt-0.5 text-xs text-muted-foreground">{label}</p>
      </CardContent>
    </Card>
  );
}
