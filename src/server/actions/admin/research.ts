"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { layout, para, sendEmail } from "@/lib/email";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

/**
 * Admin side of the research programme: a queue of proposals and a decision.
 * The note is student-facing prose — it goes into the decision email and onto
 * the student's own research page — not an internal comment.
 */

const decisionSchema = z.object({
  proposalId: z.string().min(1),
  decision: z.enum(["ACCEPTED", "REJECTED"]),
  note: z.string().trim().max(2000).optional().or(z.literal("")),
});

export async function decideResearchProposal(input: {
  proposalId: string;
  decision: "ACCEPTED" | "REJECTED";
  note?: string;
}): Promise<{ ok?: boolean; error?: string }> {
  await requireAdmin();

  const parsed = decisionSchema.safeParse(input);
  if (!parsed.success) return { error: "Invalid decision." };
  const { proposalId, decision, note } = parsed.data;

  const proposal = await prisma.researchProposal.findUnique({
    where: { id: proposalId },
    select: { id: true, title: true, status: true, user: { select: { name: true, email: true } } },
  });
  if (!proposal) return { error: "That proposal no longer exists." };
  if (proposal.status !== "PENDING") return { error: "This proposal was already decided." };

  await prisma.researchProposal.update({
    where: { id: proposalId },
    data: { status: decision, adminNote: note || null, decidedAt: new Date() },
  });

  const accepted = decision === "ACCEPTED";
  const firstName = proposal.user.name?.trim().split(/\s+/)[0] ?? "there";
  await sendEmail({
    to: proposal.user.email ?? "",
    subject: accepted
      ? "Your research proposal was accepted"
      : "About your research proposal",
    text:
      `Hi ${firstName},\n\n` +
      (accepted
        ? `Your research proposal "${proposal.title}" has been accepted into the Scholarly research programme. ` +
          `We will contact you with next steps and mentor pairing.`
        : `Thank you for proposing "${proposal.title}". We are not taking it forward right now.`) +
      (note ? `\n\nNote from the team:\n${note}` : "") +
      `\n\nYou can see the status any time under Research on scholarly.space.`,
    html: layout(
      para(`Hi ${firstName},`) +
        para(
          accepted
            ? `Your research proposal <strong style="color:#ffffff;">${proposal.title}</strong> has been accepted into the Scholarly research programme. We will contact you with next steps and mentor pairing.`
            : `Thank you for proposing <strong style="color:#ffffff;">${proposal.title}</strong>. We are not taking it forward right now.`,
        ) +
        (note ? para(`<span style="color:#8a97b1;">Note from the team: ${note}</span>`) : ""),
    ),
  });

  revalidatePath("/admin/research");
  revalidatePath("/research");
  return { ok: true };
}
