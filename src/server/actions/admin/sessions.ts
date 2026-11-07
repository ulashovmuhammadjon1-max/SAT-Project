"use server";

import { revalidatePath } from "next/cache";
import { Prisma } from "@prisma/client";
import { z } from "zod";

import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

/**
 * 1-on-1 sessions an admin hosts themselves, published from /admin/my-sessions.
 *
 * Each one is a MentorSlot with this admin as host, one seat, one hour, a title,
 * a subject, and the admin's own Google Meet link. Students book it through the
 * normal /booking flow (same coins, same approval step); the Meet link is copied
 * onto the booking when it is made, so the student gets it in the same places
 * as any other session.
 */

/** Every admin-hosted session is one hour. */
const SESSION_MINUTES = 60;

const MEET_LINK = /^https:\/\/meet\.google\.com\/[a-z]{3}-[a-z]{4}-[a-z]{3}(?:[/?#].*)?$/i;

const sessionSchema = z.object({
  title: z.string().trim().min(3, "Give the session a title (at least 3 characters).").max(120, "Keep the title under 120 characters."),
  subject: z.string().trim().min(2, "Say which subject you will teach.").max(80, "Keep the subject under 80 characters."),
  startsAt: z.coerce.date({ errorMap: () => ({ message: "Pick a date and start time." }) }),
  meetingUrl: z
    .string()
    .trim()
    .regex(MEET_LINK, "Paste a Google Meet link, like https://meet.google.com/abc-defg-hij."),
});

export type SessionActionResult = { ok: true } | { ok: false; error: string };

export async function createAdminSession(input: {
  title: string;
  subject: string;
  startsAt: string;
  meetingUrl: string;
}): Promise<SessionActionResult> {
  const admin = await requireAdmin();

  const parsed = sessionSchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: parsed.error.issues[0]?.message ?? "Check the form and try again." };
  const { title, subject, startsAt, meetingUrl } = parsed.data;

  if (Number.isNaN(startsAt.getTime())) return { ok: false, error: "Pick a date and start time." };
  if (startsAt.getTime() < Date.now() + 15 * 60_000) {
    return { ok: false, error: "Sessions must start at least 15 minutes from now." };
  }
  if (startsAt.getTime() > Date.now() + 180 * 86_400_000) {
    return { ok: false, error: "Sessions can be scheduled at most 6 months ahead." };
  }

  // An hour-long session cannot overlap another of this admin's own sessions.
  const end = new Date(startsAt.getTime() + SESSION_MINUTES * 60_000);
  const mine = await prisma.mentorSlot.findMany({
    where: {
      hostId: admin.id,
      startsAt: { gt: new Date(startsAt.getTime() - 24 * 60 * 60_000), lt: end },
    },
    select: { startsAt: true, durationMinutes: true },
  });
  const clash = mine.find((s) => s.startsAt.getTime() + s.durationMinutes * 60_000 > startsAt.getTime());
  if (clash) {
    return { ok: false, error: "You already have a session during that hour. Pick another time." };
  }

  try {
    await prisma.mentorSlot.create({
      data: {
        hostId: admin.id,
        startsAt,
        durationMinutes: SESSION_MINUTES,
        capacity: 1,
        sessionType: "ONE_ON_ONE_SAT",
        title,
        subject,
        meetingUrl,
      },
      select: { id: true },
    });
  } catch (error) {
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return { ok: false, error: "You already have a session starting at exactly that time." };
    }
    throw error;
  }

  revalidatePath("/admin/my-sessions");
  revalidatePath("/admin/bookings");
  revalidatePath("/booking");
  return { ok: true };
}

/** Deletes one of this admin's own sessions, if nobody holds a seat on it. */
export async function deleteAdminSession(slotId: string): Promise<SessionActionResult> {
  const admin = await requireAdmin();

  const slot = await prisma.mentorSlot.findUnique({
    where: { id: slotId },
    select: {
      hostId: true,
      _count: { select: { bookings: { where: { status: { in: SEAT_HOLDING_STATUSES } } } } },
    },
  });
  if (!slot) return { ok: true };
  if (slot.hostId !== admin.id) return { ok: false, error: "That session is not yours." };
  if (slot._count.bookings > 0) {
    return {
      ok: false,
      error: "A student has booked this session. Cancel the booking from Sessions first, so their coins are returned.",
    };
  }

  await prisma.mentorSlot.delete({ where: { id: slotId } });
  revalidatePath("/admin/my-sessions");
  revalidatePath("/admin/bookings");
  revalidatePath("/booking");
  return { ok: true };
}

const defaultsSchema = z.object({
  meetingUrl: z
    .string()
    .trim()
    .refine((v) => v === "" || MEET_LINK.test(v), "Paste a Google Meet link, like https://meet.google.com/abc-defg-hij."),
  defaultSubject: z.string().trim().max(80, "Keep the subject under 80 characters."),
  defaultTitle: z.string().trim().max(120, "Keep the title under 120 characters."),
});

/**
 * Saves this admin's own session defaults. Each admin has a separate row, so
 * one admin's Meet link never appears in another admin's form.
 */
export async function saveHostDefaults(input: {
  meetingUrl: string;
  defaultSubject: string;
  defaultTitle: string;
}): Promise<SessionActionResult> {
  const admin = await requireAdmin();
  const parsed = defaultsSchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: parsed.error.issues[0]?.message ?? "Check the form and try again." };
  const data = {
    meetingUrl: parsed.data.meetingUrl || null,
    defaultSubject: parsed.data.defaultSubject || null,
    defaultTitle: parsed.data.defaultTitle || null,
  };
  await prisma.hostProfile.upsert({
    where: { userId: admin.id },
    create: { userId: admin.id, ...data },
    update: data,
    select: { userId: true },
  });
  revalidatePath("/admin/my-sessions");
  return { ok: true };
}
