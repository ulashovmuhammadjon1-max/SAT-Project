"use server";

import { revalidatePath } from "next/cache";
import { Prisma } from "@prisma/client";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";

/**
 * The peer-mentor programme.
 *
 * The "role" is an APPROVED row in PeerMentorApplication, not a value in the
 * Role enum — deliberately. Mentors are still students: they practise, they
 * appear in the student counts and leaderboards, they keep every student
 * feature. Changing User.role would silently remove them from all of that
 * (the exact class of bug the student-count fix just closed). Approval is what
 * unlocks the extra ability: publishing bookable session slots.
 */

/** A certificate upload: the original filename and the file as a data URI. */
const certificateSchema = z.object({
  name: z.string().trim().min(1).max(200),
  dataUrl: z
    .string()
    .regex(
      /^data:(image\/(png|jpe?g|webp)|application\/pdf);base64,[A-Za-z0-9+/=]+$/,
      "Certificates must be PNG, JPG, WEBP or PDF files.",
    )
    // ~4MB of file becomes ~5.4MB of base64.
    .max(5_600_000, "Each certificate must be under 4MB."),
});

const applicationSchema = z.object({
  headline: z
    .string()
    .trim()
    .min(8, "Give a one-line headline, e.g. “1520 SAT — strong on Math”.")
    .max(120),
  bio: z
    .string()
    .trim()
    .min(60, "Tell students who you are and how you would help — a short paragraph.")
    .max(3000),
  satScore: z.coerce.number().int().min(400).max(1600).optional().or(z.literal("").transform(() => undefined)),
  ieltsBand: z.coerce.number().min(1).max(9).optional().or(z.literal("").transform(() => undefined)),
  subjects: z.array(z.string().trim().min(1).max(60)).min(1, "Pick at least one thing you can help with.").max(8),
  telegram: z.string().trim().max(64).optional().or(z.literal("")),
  certificates: z
    .array(certificateSchema)
    .min(1, "Upload at least one score report or certificate — approval is impossible without proof.")
    .max(3),
});

export interface PeerMentorActionResult {
  ok?: boolean;
  error?: string;
}

export async function applyPeerMentor(input: unknown): Promise<PeerMentorActionResult> {
  const user = await requireUser();

  const parsed = applicationSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Please check the form and try again." };
  }
  const d = parsed.data;
  if (d.satScore === undefined && d.ieltsBand === undefined) {
    return { error: "Enter the score you are applying with — SAT, IELTS, or both." };
  }

  const existing = await prisma.peerMentorApplication.findUnique({
    where: { userId: user.id },
    select: { status: true },
  });
  if (existing?.status === "PENDING") {
    return { error: "Your application is already under review." };
  }
  if (existing?.status === "APPROVED") {
    return { error: "You are already an approved peer mentor." };
  }

  const data = {
    headline: d.headline,
    bio: d.bio,
    satScore: d.satScore ?? null,
    ieltsBand: d.ieltsBand ?? null,
    subjects: d.subjects,
    telegram: d.telegram || null,
    certificates: d.certificates as Prisma.InputJsonValue,
    status: "PENDING" as const,
    adminNote: null,
    decidedAt: null,
  };

  // One row per student: a re-application after rejection replaces the old one.
  await prisma.peerMentorApplication.upsert({
    where: { userId: user.id },
    create: { userId: user.id, ...data },
    update: data,
  });

  revalidatePath("/mentor");
  return { ok: true };
}

export interface MyMentorState {
  status: "NONE" | "PENDING" | "APPROVED" | "REJECTED";
  headline: string | null;
  adminNote: string | null;
}

export async function getMyMentorState(): Promise<MyMentorState> {
  const user = await requireUser();
  const app = await prisma.peerMentorApplication.findUnique({
    where: { userId: user.id },
    select: { status: true, headline: true, adminNote: true },
  });
  if (!app) return { status: "NONE", headline: null, adminNote: null };
  return { status: app.status, headline: app.headline, adminNote: app.adminNote };
}

/** Gate for mentor-only actions. */
async function requireApprovedMentor() {
  const user = await requireUser();
  const app = await prisma.peerMentorApplication.findUnique({
    where: { userId: user.id },
    select: { status: true },
  });
  if (app?.status !== "APPROVED") throw new Error("Not an approved peer mentor");
  return user;
}

const slotSchema = z.object({
  startsAt: z.coerce.date(),
  durationMinutes: z.union([z.literal(30), z.literal(60)]),
});

export async function createMentorSlot(input: {
  startsAt: string | Date;
  durationMinutes: number;
}): Promise<PeerMentorActionResult> {
  const user = await requireApprovedMentor();

  const parsed = slotSchema.safeParse(input);
  if (!parsed.success) return { error: "Pick a valid time and a 30- or 60-minute duration." };
  const { startsAt, durationMinutes } = parsed.data;

  if (startsAt.getTime() < Date.now() + 60 * 60 * 1000) {
    return { error: "Slots must start at least an hour from now." };
  }
  if (startsAt.getTime() > Date.now() + 60 * 86_400_000) {
    return { error: "Slots can be published at most 60 days ahead." };
  }

  const openCount = await prisma.mentorSlot.count({
    where: { hostId: user.id, startsAt: { gt: new Date() } },
  });
  if (openCount >= 20) {
    return { error: "You already have 20 upcoming slots — let some get booked first." };
  }

  try {
    await prisma.mentorSlot.create({
      data: { startsAt, durationMinutes, sessionType: "ONE_ON_ONE_SAT", hostId: user.id },
    });
  } catch (error) {
    // startsAt is globally unique across hosts; a collision with anyone
    // else's slot is a real conflict the mentor can route around.
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return { error: "Another session already starts at exactly that time — shift yours by a few minutes." };
    }
    throw error;
  }

  revalidatePath("/mentor");
  revalidatePath("/booking");
  return { ok: true };
}

export async function deleteMentorSlot(slotId: string): Promise<PeerMentorActionResult> {
  const user = await requireApprovedMentor();

  const slot = await prisma.mentorSlot.findUnique({
    where: { id: slotId },
    select: {
      id: true,
      hostId: true,
      startsAt: true,
      _count: { select: { bookings: { where: { status: { in: SEAT_HOLDING_STATUSES } } } } },
    },
  });
  if (!slot || slot.hostId !== user.id) return { error: "That slot is not yours." };
  if (slot._count.bookings > 0) {
    return { error: "A student has booked this slot — contact the team to cancel it properly." };
  }

  await prisma.mentorSlot.delete({ where: { id: slotId } });
  revalidatePath("/mentor");
  revalidatePath("/booking");
  return { ok: true };
}

export interface MentorSlotRow {
  id: string;
  startsAt: Date;
  durationMinutes: number;
  booked: number;
  studentNames: string[];
}

export async function getMySlots(): Promise<MentorSlotRow[]> {
  const user = await requireApprovedMentor();
  const slots = await prisma.mentorSlot.findMany({
    where: { hostId: user.id, startsAt: { gt: new Date(Date.now() - 86_400_000) } },
    orderBy: { startsAt: "asc" },
    select: {
      id: true,
      startsAt: true,
      durationMinutes: true,
      bookings: {
        where: { status: { in: SEAT_HOLDING_STATUSES } },
        select: { name: true },
      },
    },
  });
  return slots.map((s) => ({
    id: s.id,
    startsAt: s.startsAt,
    durationMinutes: s.durationMinutes,
    booked: s.bookings.length,
    studentNames: s.bookings.map((b) => b.name),
  }));
}
