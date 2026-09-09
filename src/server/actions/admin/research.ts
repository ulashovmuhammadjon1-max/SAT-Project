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

const messageSchema = z.object({
  proposalId: z.string().min(1),
  subject: z.string().trim().min(1).max(200),
  body: z.string().trim().min(1).max(5000),
});

/**
 * Email one student about their proposal, from the admin panel.
 *
 * The decision email is the only message this programme could previously send,
 * and it goes out exactly once, at the moment of the decision. Everything
 * after that — mentor pairing, asking someone to get in touch, chasing a
 * student who has gone quiet — had no channel at all. The broadcast tool is
 * not it: that reaches every student on the platform.
 *
 * Unlike `sendEmail`'s usual callers this one reports the provider's failure
 * to the operator instead of swallowing it. A student signup must not fail
 * because mail is down; a person clicking Send and being told it worked when
 * it did not is a different thing entirely, and it is how a misconfigured key
 * stayed invisible here for days.
 */
export async function messageProposalAuthor(input: {
  proposalId: string;
  subject: string;
  body: string;
}): Promise<{ ok?: boolean; error?: string; provider?: string }> {
  await requireAdmin();

  const parsed = messageSchema.safeParse(input);
  if (!parsed.success) return { error: "Write a subject and a message first." };
  const { proposalId, subject, body } = parsed.data;

  const proposal = await prisma.researchProposal.findUnique({
    where: { id: proposalId },
    select: { id: true, user: { select: { name: true, email: true } } },
  });
  if (!proposal) return { error: "That proposal no longer exists." };

  // Since username signup an account can have no address. Saying so beats
  // handing the provider an empty string and reporting its rejection.
  if (!proposal.user.email) {
    return { error: "This student signed up with a username and has no email address." };
  }

  const result = await sendEmail({
    to: proposal.user.email,
    subject,
    text: body,
    html: layout(
      body
        .split(/\n{2,}/)
        .map((block) => para(block.replace(/\n/g, "<br/>")))
        .join(""),
    ),
  });

  if (!result.ok) {
    return { error: result.error || "The mail provider rejected it.", provider: result.provider };
  }
  return { ok: true, provider: result.provider };
}
