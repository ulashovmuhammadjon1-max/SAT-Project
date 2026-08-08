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

  const slot = await prisma.mentorSlot.findUnique({ where: { id: slotId }, include: { booking: true } });
  if (!slot) return { ok: false, error: "Slot not found." };
  if (isBlocked && slot.booking && slot.booking.status === "UPCOMING") {
    return { ok: false, error: "Cancel the booking on that slot before blocking it." };
  }

  await prisma.mentorSlot.update({ where: { id: slotId }, data: { isBlocked } });
  revalidatePath("/admin/bookings");
  return { ok: true };
}

export async function deleteSlot(slotId: string): Promise<AdminResult> {
  await requireAdmin();

  const slot = await prisma.mentorSlot.findUnique({ where: { id: slotId }, include: { booking: true } });
  if (!slot) return { ok: true };
  if (slot.booking && slot.booking.status === "UPCOMING") {
    return { ok: false, error: "That slot has an upcoming booking." };
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
