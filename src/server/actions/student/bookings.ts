"use server";

import { revalidatePath } from "next/cache";
import { Prisma, type SessionType } from "@prisma/client";

import { checkRequirements, getCommunityRequirements, type CommunityRequirement } from "@/lib/community";
import { InsufficientCoinsError, credit, debit } from "@/lib/coins";
import { button, layout, para, sendEmail } from "@/lib/email";
import { EVENT_TYPE_LABELS } from "@/lib/events";
import { createMeetingSafely } from "@/lib/meeting";
import { ACTIVE_STATUSES, SEAT_HOLDING_STATUSES } from "@/lib/booking/status";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { bookingCostFor, getSettings } from "@/lib/settings";

/** Thrown inside the booking transaction when the last seat went. */
class SlotFullError extends Error {
  constructor() {
    super("Slot full");
    this.name = "SlotFullError";
  }
}

/**
 * What a slot costs this student.
 *
 * 1-on-1 keeps the escalating ladder, counted over 1-on-1 bookings only — a
 * student who attended three group lectures has not consumed any of the
 * mentor's exclusive time and should not be charged as if they had.
 *
 * Group events use a flat price, because the scarcity the ladder exists to
 * ration does not apply to a room that holds thirty people.
 */
async function costForSlot(
  tx: Prisma.TransactionClient,
  userId: string,
  sessionType: SessionType,
  settings: Awaited<ReturnType<typeof getSettings>>,
): Promise<number> {
  if (sessionType !== "ONE_ON_ONE_SAT") return Math.max(0, settings.eventCost);
  const previous = await tx.booking.count({
    where: { userId, sessionType: "ONE_ON_ONE_SAT" },
  });
  return bookingCostFor(previous, settings);
}

export interface OpenSlot {
  id: string;
  startsAt: Date;
  durationMinutes: number;
  sessionType: SessionType;
}

/** Future slots that are published, not blocked, and not already taken. */
export async function getOpenSlots(): Promise<OpenSlot[]> {
  await requireUser();
  // The booking page is the 1-on-1 funnel; group events live on /events.
  const slots = await prisma.mentorSlot.findMany({
    where: { isBlocked: false, startsAt: { gt: new Date() }, sessionType: "ONE_ON_ONE_SAT" },
    orderBy: { startsAt: "asc" },
    take: 200,
    select: {
      id: true,
      startsAt: true,
      durationMinutes: true,
      sessionType: true,
      capacity: true,
      _count: { select: { bookings: { where: { status: { in: SEAT_HOLDING_STATUSES } } } } },
    },
  });
  // A cancelled booking frees its seat again, which is why this filters on the
  // live count rather than on "has any booking row".
  return slots
    .filter((s) => s._count.bookings < s.capacity)
    .map(({ _count, capacity, ...rest }) => rest);
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
    prisma.booking.count({ where: { userId: user.id, sessionType: "ONE_ON_ONE_SAT" } }),
    prisma.booking.findFirst({
      where: { userId: user.id, status: { in: ACTIVE_STATUSES }, sessionType: "ONE_ON_ONE_SAT" },
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
    include: {
      bookings: { where: { status: { in: SEAT_HOLDING_STATUSES } }, select: { id: true, userId: true } },
    },
  });
  if (!slot) return { ok: false, error: "That time slot no longer exists.", reason: "slot_gone" };
  if (slot.isBlocked) {
    return { ok: false, error: "That time slot is no longer available.", reason: "slot_gone" };
  }
  if (slot.startsAt <= new Date()) {
    return { ok: false, error: "That time slot is in the past.", reason: "slot_gone" };
  }
  if (slot.bookings.some((b) => b.userId === user.id)) {
    return { ok: false, error: "You're already registered for this one.", reason: "already_booked" };
  }
  if (slot.bookings.length >= slot.capacity) {
    return {
      ok: false,
      error:
        slot.capacity === 1
          ? "Someone just booked that slot. Please pick another time."
          : "This session is full. Please pick another one.",
      reason: "slot_gone",
    };
  }

  // One active 1-on-1 per student keeps the free offer fair while the mentor
  // is a single person. Group events are not scarce in the same way, so they
  // are deliberately outside this rule — a student may attend the weekly
  // review and still hold a 1-on-1.
  if (slot.sessionType === "ONE_ON_ONE_SAT") {
    const existing = await prisma.booking.findFirst({
      where: { userId: user.id, status: { in: ACTIVE_STATUSES }, sessionType: "ONE_ON_ONE_SAT" },
      select: { id: true },
    });
    if (existing) {
      return {
        ok: false,
        error: "You already have an upcoming 1-on-1 session booked.",
        reason: "already_booked",
      };
    }
  }

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
      // Lock the slot row for the rest of the transaction. Capacity cannot be
      // enforced by a unique index once a slot holds many attendees, and a
      // plain count-then-insert races: two students can both read "9 of 10"
      // and both insert. SELECT ... FOR UPDATE serialises them on the slot.
      await tx.$queryRaw`SELECT id FROM "MentorSlot" WHERE id = ${slot.id} FOR UPDATE`;

      const taken = await tx.booking.count({
        where: { slotId: slot.id, status: { in: SEAT_HOLDING_STATUSES } },
      });
      if (taken >= slot.capacity) throw new SlotFullError();

      // Price is derived here, inside the transaction, from the authoritative
      // booking count. Nothing the client sent influences it.
      const cost = await costForSlot(tx, user.id, slot.sessionType, settings);

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

      // A previously cancelled booking by this same student occupies the
      // [slotId, userId] pair, so reuse it rather than colliding.
      const booking = await tx.booking.upsert({
        where: { slotId_userId: { slotId: slot.id, userId: user.id } },
        create: { userId: user.id, slotId: slot.id, coinCost: cost, status: "PENDING", ...snapshot },
        update: {
          // Back into the queue, not straight to confirmed — and the previous
          // decision has to be cleared or the student would see the old
          // rejection reason attached to a fresh request.
          status: "PENDING",
          statusReason: null,
          decidedAt: null,
          decidedById: null,
          cancelledAt: null,
          coinCost: cost,
          meetingUrl: null,
          meetingProvider: null,
          meetingExternalId: null,
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
    if (error instanceof SlotFullError) {
      return {
        ok: false,
        error: "That session filled up while you were booking. Please pick another.",
        reason: "slot_gone",
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

  // Best-effort confirmation. A booking that exists and is paid for must not
  // be reported as failed because a mail provider is down.
  void sendBookingConfirmation({
    to: snapshot.email,
    name: snapshot.name,
    startsAt: slot.startsAt,
    durationMinutes: slot.durationMinutes,
    sessionType: slot.sessionType,
    meetingUrl: meeting.url,
    coinsSpent,
  });

  revalidatePath("/bookings");
  revalidatePath("/booking");
  revalidatePath("/events");
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
  if (!ACTIVE_STATUSES.includes(booking.status))
    return { ok: false, error: "That session isn't active." };

  // Refund only outside the cutoff, and only what was actually charged — the
  // cutoff exists to stop someone holding a confirmed slot and dropping it too
  // late for anyone else to take. A PENDING request was never confirmed and
  // nobody was ever turned away from it, so withdrawing one always refunds
  // regardless of how close the slot is.
  const hoursUntil = (booking.slot.startsAt.getTime() - Date.now()) / 36e5;
  const eligible =
    booking.coinCost > 0 &&
    (booking.status === "PENDING" ||
      (settings.bookingRefundHours !== null && hoursUntil >= settings.bookingRefundHours));

  const cancelled = await prisma.booking.updateMany({
    where: { id: bookingId, status: { in: ACTIVE_STATUSES } },
    data: { status: "CANCELLED", cancelledAt: new Date() },
  });
  // Someone else already cancelled it — do not refund twice.
  if (cancelled.count === 0) return { ok: false, error: "That session isn't active." };

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


/**
 * Request-received email.
 *
 * Deliberately NOT a confirmation. A booking now lands as PENDING and a human
 * approves it, so promising a confirmed session here would be a lie the student
 * only discovers if it is later declined. The join link is withheld for the
 * same reason — it is sent with the approval.
 *
 * Times are written in UTC with the offset spelled out, because the server has
 * no reliable way to render the student's local clock in an email and a wrong
 * time is worse than an explicit one they convert themselves.
 */
async function sendBookingConfirmation(args: {
  to: string;
  name: string;
  startsAt: Date;
  durationMinutes: number;
  sessionType: SessionType;
  meetingUrl: string | null;
  coinsSpent: number;
}) {
  const label = EVENT_TYPE_LABELS[args.sessionType];
  const when = args.startsAt.toUTCString();
  const firstName = args.name.trim().split(/\s+/)[0] || "there";

  await sendEmail({
    to: args.to,
    subject: `Request received: ${label}`,
    text:
      `Hi ${firstName},\n\n` +
      `We have your request for a ${label}. A volunteer will review it and you will ` +
      `get another email as soon as it is approved.\n\n` +
      `Requested time: ${when}\n` +
      `Duration: ${args.durationMinutes} minutes\n` +
      (args.coinsSpent > 0
        ? `Coins held: ${args.coinsSpent} — returned in full if the request is not approved.\n`
        : "") +
      `\nRemember to follow @satforge_org on Instagram and join the Telegram channel — ` +
      `volunteers check this before approving.\n\n` +
      `Changed your mind? Withdraw it from My Sessions on satforge.org.`,
    html: layout(
      para(`Hi ${firstName},`) +
        para(
          `We have your request for a <strong style="color:#ffffff;">${label}</strong>. A volunteer will review it and you will get another email as soon as it is approved.`,
        ) +
        para(`<strong style="color:#ffffff;">${when}</strong><br/>${args.durationMinutes} minutes`) +
        (args.coinsSpent > 0
          ? para(
              `<span style="color:#8a97b1;font-size:13px;">${args.coinsSpent} coin${args.coinsSpent === 1 ? "" : "s"} held — returned in full if the request is not approved.</span>`,
            )
          : "") +
        para(
          `<span style="color:#8a97b1;font-size:13px;">Volunteers check your Instagram and Telegram subscription before approving. Changed your mind? Withdraw it from My Sessions.</span>`,
        ),
    ),
  }).catch((e) => console.error("[booking] request-received email failed", e));
}
