"use server";

import { revalidatePath } from "next/cache";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { proposalSchema } from "@/lib/validations/research";

/**
 * The research programme's student side: propose a topic, see where it stands.
 *
 * A proposal is an application, not a workspace — the programme itself runs
 * through mentors once a topic is accepted. What matters here is that the ask
 * is small enough for a motivated student to finish in one sitting and
 * structured enough that an admin can make a real decision from it.
 */

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
    priorWork: formData.get("priorWork"),
    motivation: formData.get("motivation"),
    qualifications: formData.get("qualifications"),
    experience: formData.get("experience"),
    introEssay: formData.get("introEssay"),
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
      qualifications: parsed.data.qualifications,
      priorWork: parsed.data.priorWork,
      introEssay: parsed.data.introEssay,
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
