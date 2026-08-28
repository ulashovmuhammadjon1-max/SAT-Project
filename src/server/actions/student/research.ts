"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

/**
 * The research programme's student side: propose a topic, see where it stands.
 *
 * A proposal is an application, not a workspace — the programme itself runs
 * through mentors once a topic is accepted. What matters here is that the ask
 * is small enough for a motivated student to finish in one sitting and
 * structured enough that an admin can make a real decision from it.
 */

const proposalSchema = z.object({
  title: z.string().trim().min(8, "Give your project a real title (at least 8 characters).").max(160),
  field: z.string().trim().min(2, "What field is this in?").max(80),
  question: z
    .string()
    .trim()
    .min(30, "State the question you want to answer — a sentence or two.")
    .max(2000),
  motivation: z
    .string()
    .trim()
    .min(30, "Tell us why this question matters to you.")
    .max(4000),
  experience: z.string().trim().max(4000).optional().or(z.literal("")),
});

export interface ResearchActionResult {
  ok?: boolean;
  error?: string;
}

/** A student may have one undecided proposal at a time, and three total. */
const MAX_PENDING = 1;
const MAX_TOTAL = 3;

export async function submitResearchProposal(formData: FormData): Promise<ResearchActionResult> {
  const user = await requireUser();

  const parsed = proposalSchema.safeParse({
    title: formData.get("title"),
    field: formData.get("field"),
    question: formData.get("question"),
    motivation: formData.get("motivation"),
    experience: formData.get("experience"),
  });
  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Please check the form and try again." };
  }

  const [pending, total] = await Promise.all([
    prisma.researchProposal.count({ where: { userId: user.id, status: "PENDING" } }),
    prisma.researchProposal.count({ where: { userId: user.id } }),
  ]);
  if (pending >= MAX_PENDING) {
    return { error: "You already have a proposal under review — we will get back to you on that one first." };
  }
  if (total >= MAX_TOTAL) {
    return { error: "You have reached the limit of three proposals. Email us if you have a special case." };
  }

  await prisma.researchProposal.create({
    data: {
      userId: user.id,
      title: parsed.data.title,
      field: parsed.data.field,
      question: parsed.data.question,
      motivation: parsed.data.motivation,
      experience: parsed.data.experience || null,
    },
  });

  revalidatePath("/research");
  return { ok: true };
}

export interface MyProposal {
  id: string;
  title: string;
  field: string;
  status: "PENDING" | "ACCEPTED" | "REJECTED";
  adminNote: string | null;
  createdAt: Date;
  decidedAt: Date | null;
}

export async function getMyProposals(): Promise<MyProposal[]> {
  const user = await requireUser();
  return prisma.researchProposal.findMany({
    where: { userId: user.id },
    orderBy: { createdAt: "desc" },
    select: {
      id: true,
      title: true,
      field: true,
      status: true,
      adminNote: true,
      createdAt: true,
      decidedAt: true,
    },
  });
}
