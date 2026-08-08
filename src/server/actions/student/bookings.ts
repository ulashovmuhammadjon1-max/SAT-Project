"use server";

import { revalidatePath } from "next/cache";
import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export interface OpenSlot {
  id: string;
  startsAt: Date;
  durationMinutes: number;
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
    select: { id: true, startsAt: true, durationMinutes: true },
  });
  return slots;
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
}

export type CreateBookingResult =
  | { ok: true; bookingId: string }
  | { ok: false; error: string };

export async function createBooking(input: BookingFormInput): Promise<CreateBookingResult> {
  const user = await requireUser();

  if (!input.name?.trim()) return { ok: false, error: "Please enter your name." };
  if (!input.email?.trim()) return { ok: false, error: "Please enter your email." };

  const slot = await prisma.mentorSlot.findUnique({
    where: { id: input.slotId },
    include: { booking: true },
  });
  if (!slot) return { ok: false, error: "That time slot no longer exists." };
  if (slot.isBlocked) return { ok: false, error: "That time slot is no longer available." };
  if (slot.startsAt <= new Date()) return { ok: false, error: "That time slot is in the past." };
  if (slot.booking && slot.booking.status !== "CANCELLED") {
    return { ok: false, error: "Someone just booked that slot. Please pick another time." };
  }

  // One active session per student keeps the free offer fair while the mentor
  // is a single person.
  const existing = await prisma.booking.findFirst({
    where: { userId: user.id, status: "UPCOMING" },
  });
  if (existing) {
    return { ok: false, error: "You already have an upcoming session booked." };
  }

  try {
    // `Booking.slotId` is unique, so two students racing for the same slot
    // means the loser hits P2002 rather than silently double-booking.
    const booking = await prisma.booking.create({
      data: {
        userId: user.id,
        slotId: slot.id,
        name: input.name.trim(),
        email: input.email.trim(),
        currentScore: input.currentScore ?? null,
        targetScore: input.targetScore ?? null,
        satDate: input.satDate ? new Date(input.satDate) : null,
        studyHoursPerWeek: input.studyHoursPerWeek ?? null,
        weakestArea: input.weakestArea?.trim() || null,
        notes: input.notes?.trim() || null,
        timezone: input.timezone ?? null,
      },
    });

    revalidatePath("/bookings");
    revalidatePath("/booking");
    return { ok: true, bookingId: booking.id };
  } catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return { ok: false, error: "Someone just booked that slot. Please pick another time." };
    }
    // A cancelled booking still occupies the unique slotId; reuse it.
    if (slot.booking?.status === "CANCELLED") {
      const revived = await prisma.booking.update({
        where: { id: slot.booking.id },
        data: {
          userId: user.id,
          status: "UPCOMING",
          cancelledAt: null,
          name: input.name.trim(),
          email: input.email.trim(),
          currentScore: input.currentScore ?? null,
          targetScore: input.targetScore ?? null,
          satDate: input.satDate ? new Date(input.satDate) : null,
          studyHoursPerWeek: input.studyHoursPerWeek ?? null,
          weakestArea: input.weakestArea?.trim() || null,
          notes: input.notes?.trim() || null,
          timezone: input.timezone ?? null,
        },
      });
      revalidatePath("/bookings");
      return { ok: true, bookingId: revived.id };
    }
    console.error("[booking] create failed", error);
    return { ok: false, error: "Couldn't complete the booking. Please try again." };
  }
}

export async function cancelBooking(bookingId: string): Promise<{ ok: boolean; error?: string }> {
  const user = await requireUser();

  const booking = await prisma.booking.findUnique({ where: { id: bookingId } });
  if (!booking) return { ok: false, error: "Booking not found." };
  // Authorization: a student may only cancel their own booking.
  if (booking.userId !== user.id) return { ok: false, error: "Booking not found." };
  if (booking.status !== "UPCOMING") return { ok: false, error: "That session isn't upcoming." };

  await prisma.booking.update({
    where: { id: bookingId },
    data: { status: "CANCELLED", cancelledAt: new Date() },
  });

  revalidatePath("/bookings");
  revalidatePath("/booking");
  return { ok: true };
}

export async function getMyBookings() {
  const user = await requireUser();
  return prisma.booking.findMany({
    where: { userId: user.id },
    orderBy: { createdAt: "desc" },
    include: { slot: { select: { startsAt: true, durationMinutes: true } } },
  });
}
