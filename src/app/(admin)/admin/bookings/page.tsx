import { SlotCreator, SlotTable, type AdminSlotRow } from "@/components/admin/booking-admin";
import {
  NextSessionPanel,
  RoomLinkCard,
  type NextSessionInfo,
} from "@/components/admin/next-session-panel";
import { Card, CardContent } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";
import { getSettings } from "@/lib/settings";

export const metadata = { title: "Sessions" };
export const dynamic = "force-dynamic";

export default async function AdminBookingsPage() {
  await requireAdmin();

  const [slots, settings] = await Promise.all([
    prisma.mentorSlot.findMany({ orderBy: { startsAt: "asc" }, include: { booking: true } }),
    getSettings(),
  ]);

  // The room the mentor joins when there is no per-booking link.
  const roomUrl = settings.staticMeetingUrl || process.env.MEETING_STATIC_URL || null;

  const nextSlot = slots.find(
    (s) => s.booking?.status === "UPCOMING" && s.startsAt > new Date(),
  );
  const nextSession: NextSessionInfo | null =
    nextSlot && nextSlot.booking
      ? {
          bookingId: nextSlot.booking.id,
          startsAt: nextSlot.startsAt.toISOString(),
          durationMinutes: nextSlot.durationMinutes,
          name: nextSlot.booking.name,
          email: nextSlot.booking.email,
          currentScore: nextSlot.booking.currentScore,
          targetScore: nextSlot.booking.targetScore,
          weakestArea: nextSlot.booking.weakestArea,
          notes: nextSlot.booking.notes,
          timezone: nextSlot.booking.timezone,
          // Bookings made before a provider existed have no link of their own;
          // fall back to the standing room rather than showing nothing.
          meetingUrl: nextSlot.booking.meetingUrl ?? roomUrl,
        }
      : null;

  const upcoming = slots.filter(
    (s) => s.booking?.status === "UPCOMING" && s.startsAt > new Date()
  ).length;
  const open = slots.filter(
    (s) => !s.isBlocked && s.startsAt > new Date() && (!s.booking || s.booking.status === "CANCELLED")
  ).length;

  const rows: AdminSlotRow[] = slots.map((s) => ({
    id: s.id,
    startsAt: s.startsAt.toISOString(),
    durationMinutes: s.durationMinutes,
    isBlocked: s.isBlocked,
    booking: s.booking
      ? {
          id: s.booking.id,
          status: s.booking.status,
          name: s.booking.name,
          email: s.booking.email,
          currentScore: s.booking.currentScore,
          targetScore: s.booking.targetScore,
          satDate: s.booking.satDate ? s.booking.satDate.toISOString() : null,
          studyHoursPerWeek: s.booking.studyHoursPerWeek,
          weakestArea: s.booking.weakestArea,
          notes: s.booking.notes,
          timezone: s.booking.timezone,
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

      <div className="grid gap-3 sm:grid-cols-3">
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
