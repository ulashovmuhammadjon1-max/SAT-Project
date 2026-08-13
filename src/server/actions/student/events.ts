"use server";

import type { SessionType } from "@prisma/client";

import { getCommunityRequirements, type CommunityRequirement } from "@/lib/community";
import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { EVENT_TYPE_LABELS } from "@/lib/events";
import { getSettings } from "@/lib/settings";

/**
 * Group events: the weekly test-analysis review, lectures, workshops.
 *
 * Registration deliberately reuses `createBooking` rather than duplicating it.
 * Everything that matters — the atomic coin debit, the capacity check under a
 * row lock, the community requirements, the refund on cancellation — is
 * already correct there, and a second implementation would be a second place
 * for those guarantees to drift.
 */

export interface EventListItem {
  id: string;
  startsAt: Date;
  durationMinutes: number;
  sessionType: SessionType;
  title: string;
  description: string | null;
  capacity: number;
  taken: number;
  seatsLeft: number;
  isFull: boolean;
  /** This student is already registered. */
  registered: boolean;
  meetingUrl: string | null;
}

export interface EventsPage {
  events: EventListItem[];
  balance: number;
  cost: number;
  canAfford: boolean;
  requirements: CommunityRequirement[];
  refundHours: number | null;
}

export async function getEvents(): Promise<EventsPage> {
  const user = await requireUser();
  const settings = await getSettings();

  const [slots, dbUser, requirements] = await Promise.all([
    prisma.mentorSlot.findMany({
      where: {
        isBlocked: false,
        startsAt: { gt: new Date() },
        // 1-on-1 has its own dedicated funnel at /booking.
        sessionType: { not: "ONE_ON_ONE_SAT" },
      },
      orderBy: { startsAt: "asc" },
      take: 50,
      include: {
        bookings: {
          where: { status: { in: SEAT_HOLDING_STATUSES } },
          select: { userId: true, meetingUrl: true },
        },
      },
    }),
    prisma.user.findUniqueOrThrow({
      where: { id: user.id },
      select: { coinBalance: true },
    }),
    getCommunityRequirements(),
  ]);

  const cost = Math.max(0, settings.eventCost);

  return {
    events: slots.map((s) => {
      const mine = s.bookings.find((b) => b.userId === user.id);
      const taken = s.bookings.length;
      return {
        id: s.id,
        startsAt: s.startsAt,
        durationMinutes: s.durationMinutes,
        sessionType: s.sessionType,
        title: s.title ?? EVENT_TYPE_LABELS[s.sessionType],
        description: s.description,
        capacity: s.capacity,
        taken,
        seatsLeft: Math.max(0, s.capacity - taken),
        isFull: taken >= s.capacity,
        registered: Boolean(mine),
        // Only ever exposed to someone actually registered.
        meetingUrl: mine ? (mine.meetingUrl ?? settings.staticMeetingUrl ?? null) : null,
      };
    }),
    balance: dbUser.coinBalance,
    cost,
    canAfford: dbUser.coinBalance >= cost,
    requirements,
    refundHours: settings.bookingRefundHours,
  };
}

/**
 * Cancel a registration by slot.
 *
 * The events list never exposes booking ids, so this resolves the caller's own
 * booking for that slot and hands it to the shared `cancelBooking`, which owns
 * the refund rules and the ownership check.
 */
export async function cancelEventRegistration(
  slotId: string,
): Promise<{ ok: boolean; error?: string; refunded?: number }> {
  const user = await requireUser();
  const booking = await prisma.booking.findUnique({
    where: { slotId_userId: { slotId, userId: user.id } },
    select: { id: true },
  });
  if (!booking) return { ok: false, error: "You're not registered for this one." };

  const { cancelBooking } = await import("@/server/actions/student/bookings");
  return cancelBooking(booking.id);
}
