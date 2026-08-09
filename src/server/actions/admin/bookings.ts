"use server";

import { revalidatePath } from "next/cache";

import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export type AdminResult = { ok: boolean; error?: string };

/**
 * Publishes bookable slots.
 *
 * `times` are "HH:MM" in the admin's own timezone; `tzOffsetMinutes` is
 * `Date.prototype.getTimezoneOffset()` from that browser, so we can turn them
 * into absolute UTC instants. Storing instants (not wall-clock strings) is what
 * lets students in other timezones see the correct local time.
 */
export async function createSlots(input: {
  dates: string[];
  times: string[];
  durationMinutes: number;
  tzOffsetMinutes: number;
}): Promise<AdminResult & { created?: number }> {
  await requireAdmin();

  if (!input.dates.length || !input.times.length) {
    return { ok: false, error: "Pick at least one date and one time." };
  }
  const duration = Math.min(180, Math.max(10, input.durationMinutes || 30));

  const starts: Date[] = [];
  for (const d of input.dates) {
    for (const t of input.times) {
      const [h, m] = t.split(":").map(Number);
      if (Number.isNaN(h) || Number.isNaN(m)) continue;
      // Build the wall-clock time as if UTC, then undo the admin's offset.
      const asUtc = new Date(`${d}T00:00:00.000Z`);
      asUtc.setUTCHours(h, m, 0, 0);
      starts.push(new Date(asUtc.getTime() + input.tzOffsetMinutes * 60_000));
    }
  }
  if (!starts.length) return { ok: false, error: "Those times couldn't be parsed." };

  // startsAt is unique — skipDuplicates makes re-submitting harmless.
  const res = await prisma.mentorSlot.createMany({
    data: starts.map((startsAt) => ({ startsAt, durationMinutes: duration })),
    skipDuplicates: true,
  });

  revalidatePath("/admin/bookings");
  return { ok: true, created: res.count };
}

export async function setSlotBlocked(slotId: string, isBlocked: boolean): Promise<AdminResult> {
  await requireAdmin();

  const slot = await prisma.mentorSlot.findUnique({ where: { id: slotId }, include: { bookings: { where: { status: "UPCOMING" } } } });
  if (!slot) return { ok: false, error: "Slot not found." };
  if (isBlocked && slot.bookings.length > 0) {
    return {
      ok: false,
      error:
        slot.bookings.length === 1
          ? "Cancel the booking on that slot before blocking it."
          : `That session has ${slot.bookings.length} people registered. Cancel them before blocking it.`,
    };
  }

  await prisma.mentorSlot.update({ where: { id: slotId }, data: { isBlocked } });
  revalidatePath("/admin/bookings");
  return { ok: true };
}

export async function deleteSlot(slotId: string): Promise<AdminResult> {
  await requireAdmin();

  const slot = await prisma.mentorSlot.findUnique({ where: { id: slotId }, include: { bookings: { where: { status: "UPCOMING" } } } });
  if (!slot) return { ok: true };
  if (slot.bookings.length > 0) {
    return {
      ok: false,
      error:
        slot.bookings.length === 1
          ? "That slot has an upcoming booking."
          : `That session has ${slot.bookings.length} people registered.`,
    };
  }

  await prisma.mentorSlot.delete({ where: { id: slotId } });
  revalidatePath("/admin/bookings");
  return { ok: true };
}

export async function setBookingStatus(
  bookingId: string,
  status: "UPCOMING" | "COMPLETED" | "CANCELLED"
): Promise<AdminResult> {
  await requireAdmin();

  const booking = await prisma.booking.findUnique({ where: { id: bookingId } });
  if (!booking) return { ok: false, error: "Booking not found." };

  await prisma.booking.update({
    where: { id: bookingId },
    data: { status, cancelledAt: status === "CANCELLED" ? new Date() : null },
  });

  revalidatePath("/admin/bookings");
  return { ok: true };
}

/**
 * Publish a group event: the weekly review, a lecture, a workshop.
 *
 * Separate from `createSlots` because the inputs genuinely differ — an event
 * has a name, a description and a seat count, and is created one at a time
 * rather than as a grid of repeated slots.
 *
 * `MentorSlot.startsAt` is unique, which for a single mentor is a feature:
 * it makes it impossible to publish an event opposite a 1-on-1 and end up
 * double-booked with yourself.
 */
export async function createEvent(input: {
  date: string;
  time: string;
  durationMinutes: number;
  tzOffsetMinutes: number;
  sessionType: "TEST_ANALYSIS" | "FINANCIAL_LITERACY" | "LECTURE" | "WORKSHOP";
  title: string;
  description?: string | null;
  capacity: number;
  /** Publish this many weekly repeats, for a recurring review. */
  repeatWeeks?: number;
}): Promise<AdminResult & { created?: number }> {
  await requireAdmin();

  const title = input.title?.trim();
  if (!title) return { ok: false, error: "Give the event a title." };
  if (!input.date || !input.time) return { ok: false, error: "Pick a date and a time." };

  const [h, m] = input.time.split(":").map(Number);
  if (Number.isNaN(h) || Number.isNaN(m)) return { ok: false, error: "That time couldn't be read." };

  const duration = Math.min(240, Math.max(10, input.durationMinutes || 60));
  const capacity = Math.min(500, Math.max(1, input.capacity || 30));
  const repeats = Math.min(26, Math.max(1, input.repeatWeeks || 1));

  const asUtc = new Date(`${input.date}T00:00:00.000Z`);
  asUtc.setUTCHours(h, m, 0, 0);
  const first = new Date(asUtc.getTime() + input.tzOffsetMinutes * 60_000);

  const rows = Array.from({ length: repeats }, (_, i) => ({
    startsAt: new Date(first.getTime() + i * 7 * 864e5),
    durationMinutes: duration,
    sessionType: input.sessionType,
    title,
    description: input.description?.trim() || null,
    capacity,
  }));

  // skipDuplicates so re-submitting, or overlapping an existing slot, is
  // harmless rather than an error the admin has to decode.
  const res = await prisma.mentorSlot.createMany({ data: rows, skipDuplicates: true });

  revalidatePath("/admin/bookings");
  revalidatePath("/events");
  return { ok: true, created: res.count };
}
