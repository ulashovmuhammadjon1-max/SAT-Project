"use server";

import { revalidatePath } from "next/cache";

import { credit } from "@/lib/coins";
import { getCommunityRequirements } from "@/lib/community";
import {
  sendBookingApproved,
  sendBookingCancelledByAdmin,
  sendBookingNeedsRecheck,
  sendBookingRejected,
} from "@/lib/email/booking-decision";
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

  // Cancelling has to go through decideBooking so the coins are actually
  // returned. This path used to flip the status and keep the student's coins,
  // which is the bug that made an admin cancel quietly more expensive for the
  // student than cancelling it themselves.
  if (status === "CANCELLED") return decideBooking({ bookingId, decision: "CANCEL" });

  await prisma.booking.update({
    where: { id: bookingId },
    data: { status, cancelledAt: null },
  });

  revalidatePath("/admin/bookings");
  return { ok: true };
}

export type BookingDecision = "APPROVE" | "REJECT" | "CANCEL" | "REVOKE";

/**
 * Approve, reject, or cancel a booking, with a reason the student is told.
 *
 * One action for all three because they share everything that matters: the
 * same authorization, the same "has someone already decided this?" race, the
 * same refund rule, and the same requirement that the student hears about it.
 * Splitting them produced three near-identical bodies and one of them
 * (cancel) silently skipped the refund.
 *
 * Coins are held at booking time, not charged on approval. That way a student
 * cannot be approved into a session they can no longer afford because their
 * balance moved while they waited, and the refund path is the one already
 * proven by student-initiated cancellation — including its idempotency key,
 * which is what stops a double-click refunding twice.
 */
export async function decideBooking(input: {
  bookingId: string;
  decision: BookingDecision;
  /** Shown to the student verbatim, in the email and on My Sessions. */
  reason?: string | null;
}): Promise<AdminResult & { refunded?: number }> {
  const admin = await requireAdmin();

  const reason = input.reason?.trim().slice(0, 2000) || null;
  // A decline or a withdrawal without a stated cause reads as arbitrary and
  // leaves the student nothing to act on. Approving needs no justification.
  if (input.decision !== "APPROVE" && !reason) {
    return { ok: false, error: "Give the student a reason — it goes in the email they receive." };
  }

  const booking = await prisma.booking.findUnique({
    where: { id: input.bookingId },
    include: { slot: { select: { startsAt: true, durationMinutes: true, sessionType: true } } },
  });
  if (!booking) return { ok: false, error: "Booking not found." };

  if (input.decision === "APPROVE" && booking.status !== "PENDING") {
    return {
      ok: false,
      error:
        booking.status === "UPCOMING"
          ? "That booking is already approved."
          : `That booking is ${booking.status.toLowerCase()} and can't be approved.`,
    };
  }
  if (input.decision === "REJECT" && booking.status !== "PENDING") {
    return { ok: false, error: "Only a booking still awaiting approval can be declined." };
  }
  if (input.decision === "CANCEL" && !["PENDING", "UPCOMING"].includes(booking.status)) {
    return { ok: false, error: "That booking isn't active." };
  }
  if (input.decision === "REVOKE" && booking.status !== "UPCOMING") {
    return {
      ok: false,
      error:
        booking.status === "PENDING"
          ? "That booking is already waiting for approval."
          : "Only an approved session can be sent back for review.",
    };
  }

  // REVOKE returns an approved session to the queue rather than ending it: the
  // seat stays held, the coins stay held, and the student keeps their slot while
  // they fix whatever failed the check. That is the whole point of it being
  // separate from CANCEL.
  const nextStatus =
    input.decision === "APPROVE"
      ? "UPCOMING"
      : input.decision === "REJECT"
        ? "REJECTED"
        : input.decision === "REVOKE"
          ? "PENDING"
          : "CANCELLED";

  // Guarded on the status we just read, so two admins clicking at once cannot
  // both decide it — the loser updates zero rows and refunds nothing.
  const changed = await prisma.booking.updateMany({
    where: { id: booking.id, status: booking.status },
    data: {
      status: nextStatus,
      statusReason: reason,
      decidedAt: new Date(),
      decidedById: admin.id,
      // Only a genuinely terminal state carries a cancellation timestamp.
      cancelledAt: nextStatus === "UPCOMING" || nextStatus === "PENDING" ? null : new Date(),
    },
  });
  if (changed.count === 0) return { ok: false, error: "Someone else just decided that booking." };

  // No refund on REVOKE — the booking still exists and the coins are still
  // held against it. Refunding here and re-debiting on re-approval would risk
  // the student's balance having moved in between, which is the failure mode
  // holding the coins exists to avoid.
  let refunded = 0;
  if (nextStatus === "REJECTED" || nextStatus === "CANCELLED") {
    if (booking.coinCost > 0) {
      try {
        await credit({
          userId: booking.userId,
          amount: booking.coinCost,
          type: "BOOKING_REFUND",
          description:
            nextStatus === "REJECTED"
              ? "Session request declined — coins returned"
              : "Session cancelled — coins returned",
          bookingId: booking.id,
          // Same key the student-initiated cancel uses, so a booking can only
          // ever be refunded once no matter which path releases it.
          idempotencyKey: `refund:${booking.id}`,
        });
        refunded = booking.coinCost;
      } catch (error) {
        // The decision stands; the refund is recoverable by hand. Failing the
        // whole action here would leave the admin thinking nothing happened.
        console.error("[booking] admin refund failed", error);
      }
    }
  }

  const emailArgs = {
    to: booking.email,
    name: booking.name,
    startsAt: booking.slot.startsAt,
    durationMinutes: booking.slot.durationMinutes,
    sessionType: booking.slot.sessionType,
    reason,
    meetingUrl: booking.meetingUrl,
    refunded,
  };
  if (nextStatus === "UPCOMING") await sendBookingApproved(emailArgs);
  else if (nextStatus === "REJECTED") await sendBookingRejected(emailArgs);
  else if (nextStatus === "PENDING")
    // The re-check mail lists the actual requirements so the student knows
    // exactly what to do rather than guessing which step they missed.
    await sendBookingNeedsRecheck({ ...emailArgs, requirements: await getCommunityRequirements() });
  else await sendBookingCancelledByAdmin(emailArgs);

  revalidatePath("/admin/bookings");
  revalidatePath("/bookings");
  revalidatePath("/dashboard");
  return { ok: true, refunded };
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
