"use server";

import { revalidatePath } from "next/cache";
import { Prisma, type SessionType } from "@prisma/client";

import { checkRequirements, getCommunityRequirements, type CommunityRequirement } from "@/lib/community";
import { InsufficientCoinsError, credit, debit } from "@/lib/coins";
import { createMeetingSafely } from "@/lib/meeting";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { bookingCostFor, getSettings } from "@/lib/settings";

export interface OpenSlot {
  id: string;
  startsAt: Date;
  durationMinutes: number;
  sessionType: SessionType;
}

/** Future slots that are published, not blocked, and not already taken. */
export async function getOpenSlots(): Promise<OpenSlot[]> {
  await requireUser();
  const slots = await prisma.mentorSlot.findMany({
    where: {
      isBlocked: false,
      startsAt: { gt: new Date() },
      // A cancelled booking frees its slot again.
      OR: [{ booking: null }, { booking: { status: "CANCELLED" } }],
    },
    orderBy: { startsAt: "asc" },
    take: 200,
    select: { id: true, startsAt: true, durationMinutes: true, sessionType: true },
  });
  return slots;
}

export interface BookingContext {
  balance: number;
  /** What the next booking will cost this student. */
  cost: number;
  previousBookings: number;
  canAfford: boolean;
  shortfall: number;
  requirements: CommunityRequirement[];
  hasUpcoming: boolean;
  refundHours: number | null;
  referralRewardCoins: number;
}

/**
 * Everything the booking page needs to render honestly before the student
 * commits to anything: their balance, the price they will actually be charged,
 * and what happens if they cannot afford it.
 *
 * The price shown here is recomputed server-side at booking time. This is for
 * display; it is never trusted as input.
 */
export async function getBookingContext(): Promise<BookingContext> {
  const user = await requireUser();
  const settings = await getSettings();

  const [dbUser, previousBookings, upcoming, requirements] = await Promise.all([
    prisma.user.findUniqueOrThrow({
      where: { id: user.id },
      select: { coinBalance: true },
    }),
    // Cancelled bookings count: the ladder prices the mentor's time being
    // reserved, and a cancel/rebook cycle must not reset the price.
    prisma.booking.count({ where: { userId: user.id } }),
    prisma.booking.findFirst({
      where: { userId: user.id, status: "UPCOMING" },
      select: { id: true },
    }),
    getCommunityRequirements(),
  ]);

  const cost = bookingCostFor(previousBookings, settings);
  const balance = dbUser.coinBalance;

  return {
    balance,
    cost,
    previousBookings,
    canAfford: balance >= cost,
    shortfall: Math.max(0, cost - balance),
    requirements,
    hasUpcoming: Boolean(upcoming),
    refundHours: settings.bookingRefundHours,
    referralRewardCoins: settings.referralRewardCoins,
  };
}

export interface BookingFormInput {
  slotId: string;
  name: string;
  email: string;
  currentScore?: number | null;
  targetScore?: number | null;
  satDate?: string | null;
  studyHoursPerWeek?: number | null;
  weakestArea?: string | null;
  notes?: string | null;
  timezone?: string | null;
  /** Ids of the community requirements the student confirmed. */
  acknowledgedRequirements?: string[];
}

export type CreateBookingResult =
  | { ok: true; bookingId: string; coinsSpent: number; balance: number }
  | {
      ok: false;
      error: string;
      /** Lets the UI show the right recovery path rather than a generic toast. */
      reason:
        | "validation"
        | "slot_gone"
        | "requirements"
        | "insufficient_coins"
        | "already_booked"
        | "unknown";
      required?: number;
      available?: number;
    };

/**
 * Book a session: verify, charge, create — or do none of it.
 *
 * The coin debit and the booking insert happen in **one** database
 * transaction, which is what makes "do not deduct coins if booking creation
 * fails" true rather than aspirational. If the insert trips the unique index on
 * `slotId` because another student won the race, the transaction unwinds and
 * the debit disappears with it.
 *
 * Order inside the transaction matters: debit first, then insert. Debiting
 * first means the balance guard and the slot guard are both inside the same
 * atomic unit, so there is no window where coins are spent against a slot that
 * has since gone.
 */
export async function createBooking(input: BookingFormInput): Promise<CreateBookingResult> {
  const user = await requireUser();
  const settings = await getSettings();

  if (!input.name?.trim()) {
    return { ok: false, error: "Please enter your name.", reason: "validation" };
  }
  if (!input.email?.trim()) {
    return { ok: false, error: "Please enter your email.", reason: "validation" };
  }

  // Community requirements. An attestation, not a verification — see
  // lib/community.ts for why that is the honest implementation.
  const reqCheck = await checkRequirements(input.acknowledgedRequirements ?? []);
  if (!reqCheck.ok) {
    return {
      ok: false,
      reason: "requirements",
      error:
        reqCheck.missing.length === 1
          ? `Please confirm: ${reqCheck.missing[0].label}.`
          : "Please confirm both community steps before booking.",
    };
  }

  const slot = await prisma.mentorSlot.findUnique({
    where: { id: input.slotId },
    include: { booking: { select: { id: true, status: true } } },
  });
  if (!slot) return { ok: false, error: "That time slot no longer exists.", reason: "slot_gone" };
  if (slot.isBlocked) {
    return { ok: false, error: "That time slot is no longer available.", reason: "slot_gone" };
  }
  if (slot.startsAt <= new Date()) {
    return { ok: false, error: "That time slot is in the past.", reason: "slot_gone" };
  }
  if (slot.booking && slot.booking.status !== "CANCELLED") {
    return {
      ok: false,
      error: "Someone just booked that slot. Please pick another time.",
      reason: "slot_gone",
    };
  }

  // One active session per student keeps the free offer fair while the mentor
  // is a single person.
  const existing = await prisma.booking.findFirst({
    where: { userId: user.id, status: "UPCOMING" },
    select: { id: true },
  });
  if (existing) {
    return {
      ok: false,
      error: "You already have an upcoming session booked.",
      reason: "already_booked",
    };
  }

  const revivableBookingId =
    slot.booking?.status === "CANCELLED" ? slot.booking.id : null;

  const snapshot = {
    name: input.name.trim(),
    email: input.email.trim(),
    currentScore: input.currentScore ?? null,
    targetScore: input.targetScore ?? null,
    satDate: input.satDate ? new Date(input.satDate) : null,
    studyHoursPerWeek: input.studyHoursPerWeek ?? null,
    weakestArea: input.weakestArea?.trim() || null,
    notes: input.notes?.trim() || null,
    timezone: input.timezone ?? null,
    sessionType: slot.sessionType,
    requirementsAckAt: new Date(),
  };

  let bookingId: string;
  let coinsSpent: number;
  let balance: number;

  try {
    const result = await prisma.$transaction(async (tx) => {
      // Price is derived here, inside the transaction, from the authoritative
      // booking count. Nothing the client sent influences it.
      const previousBookings = await tx.booking.count({ where: { userId: user.id } });
      const cost = bookingCostFor(previousBookings, settings);

      // Throws InsufficientCoinsError, which rolls the transaction back before
      // any booking row exists.
      const ledger = await debit(
        {
          userId: user.id,
          amount: cost,
          type: "BOOKING_SPEND",
          description: "1-on-1 SAT guidance session",
        },
        tx,
      );

      const booking = revivableBookingId
        ? await tx.booking.update({
            where: { id: revivableBookingId },
            data: {
              userId: user.id,
              status: "UPCOMING",
              cancelledAt: null,
              coinCost: cost,
              meetingUrl: null,
              meetingProvider: null,
              meetingExternalId: null,
              ...snapshot,
            },
            select: { id: true },
          })
        : await tx.booking.create({
            data: {
              userId: user.id,
              slotId: slot.id,
              coinCost: cost,
              ...snapshot,
            },
            select: { id: true },
          });

      // Backfill the ledger row now that the booking has an id, so the wallet
      // can link a spend to the session it paid for.
      if (ledger.transactionId) {
        await tx.coinTransaction.update({
          where: { id: ledger.transactionId },
          data: { bookingId: booking.id },
        });
      }

      return { bookingId: booking.id, cost, balance: ledger.balance };
    });

    bookingId = result.bookingId;
    coinsSpent = result.cost;
    balance = result.balance;
  } catch (error) {
    if (error instanceof InsufficientCoinsError) {
      return {
        ok: false,
        reason: "insufficient_coins",
        required: error.required,
        available: error.available,
        error: `You need ${error.required} coins for this session and have ${error.available}.`,
      };
    }
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      // Lost the race for the slot. The transaction rolled back, so the coins
      // were never spent.
      return {
        ok: false,
        error: "Someone just booked that slot. Please pick another time.",
        reason: "slot_gone",
      };
    }
    console.error("[booking] create failed; no coins were deducted", error);
    return {
      ok: false,
      error: "Couldn't complete the booking. Your coins have not been touched.",
      reason: "unknown",
    };
  }

  // Best-effort, outside the transaction: a provider outage must not undo a
  // paid booking. `createMeetingSafely` never throws.
  const meeting = await createMeetingSafely({
    bookingId,
    startsAt: slot.startsAt,
    durationMinutes: slot.durationMinutes,
    studentName: snapshot.name,
    studentEmail: snapshot.email,
    title: "SATForge 1-on-1 SAT guidance",
  });
  if (meeting.url) {
    await prisma.booking
      .update({
        where: { id: bookingId },
        data: {
          meetingUrl: meeting.url,
          meetingProvider: meeting.provider,
          meetingExternalId: meeting.externalId ?? null,
        },
      })
      .catch((e) => console.error("[booking] could not attach meeting link", e));
  }

  revalidatePath("/bookings");
  revalidatePath("/booking");
  revalidatePath("/wallet");
  revalidatePath("/dashboard");
  return { ok: true, bookingId, coinsSpent, balance };
}

export async function cancelBooking(
  bookingId: string,
): Promise<{ ok: boolean; error?: string; refunded?: number }> {
  const user = await requireUser();
  const settings = await getSettings();

  const booking = await prisma.booking.findUnique({
    where: { id: bookingId },
    include: { slot: { select: { startsAt: true } } },
  });
  if (!booking) return { ok: false, error: "Booking not found." };
  // Authorization: a student may only cancel their own booking.
  if (booking.userId !== user.id) return { ok: false, error: "Booking not found." };
  if (booking.status !== "UPCOMING") return { ok: false, error: "That session isn't upcoming." };

  // Refund only outside the cutoff, and only what was actually charged.
  const hoursUntil = (booking.slot.startsAt.getTime() - Date.now()) / 36e5;
  const eligible =
    settings.bookingRefundHours !== null &&
    hoursUntil >= settings.bookingRefundHours &&
    booking.coinCost > 0;

  const cancelled = await prisma.booking.updateMany({
    where: { id: bookingId, status: "UPCOMING" },
    data: { status: "CANCELLED", cancelledAt: new Date() },
  });
  // Someone else already cancelled it — do not refund twice.
  if (cancelled.count === 0) return { ok: false, error: "That session isn't upcoming." };

  let refunded = 0;
  if (eligible) {
    try {
      await credit({
        userId: user.id,
        amount: booking.coinCost,
        type: "BOOKING_REFUND",
        description: "Session cancelled — coins returned",
        bookingId: booking.id,
        // One refund per booking, whatever happens upstream.
        idempotencyKey: `refund:${booking.id}`,
      });
      refunded = booking.coinCost;
    } catch (error) {
      console.error("[booking] refund failed", error);
    }
  }

  revalidatePath("/bookings");
  revalidatePath("/booking");
  revalidatePath("/wallet");
  revalidatePath("/dashboard");
  return { ok: true, refunded };
}

export async function getMyBookings() {
  const user = await requireUser();
  return prisma.booking.findMany({
    where: { userId: user.id },
    orderBy: { createdAt: "desc" },
    include: {
      slot: { select: { startsAt: true, durationMinutes: true, sessionType: true } },
    },
  });
}
