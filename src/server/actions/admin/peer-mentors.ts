"use server";

import { revalidatePath } from "next/cache";
import { z } from "zod";

import { layout, para, sendEmail } from "@/lib/email";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

/**
 * Admin approval for the peer-mentor programme. The certificates are the whole
 * point of the review — an approval without opening them is a rubber stamp, so
 * the queue page renders them inline rather than behind a download.
 */

const decisionSchema = z.object({
  applicationId: z.string().min(1),
  decision: z.enum(["APPROVED", "REJECTED"]),
  note: z.string().trim().max(2000).optional().or(z.literal("")),
});

export async function decidePeerMentor(input: {
  applicationId: string;
  decision: "APPROVED" | "REJECTED";
  note?: string;
}): Promise<{ ok?: boolean; error?: string }> {
  await requireAdmin();

  const parsed = decisionSchema.safeParse(input);
  if (!parsed.success) return { error: "Invalid decision." };
  const { applicationId, decision, note } = parsed.data;

  const app = await prisma.peerMentorApplication.findUnique({
    where: { id: applicationId },
    select: { id: true, status: true, headline: true, user: { select: { name: true, email: true } } },
  });
  if (!app) return { error: "That application no longer exists." };
  if (app.status !== "PENDING") return { error: "This application was already decided." };

  await prisma.peerMentorApplication.update({
    where: { id: applicationId },
    data: { status: decision, adminNote: note || null, decidedAt: new Date() },
  });

  const approved = decision === "APPROVED";
  const firstName = app.user.name?.trim().split(/\s+/)[0] ?? "there";
  await sendEmail({
    to: app.user.email,
    subject: approved ? "You are a Scholarly peer mentor" : "About your peer-mentor application",
    text:
      `Hi ${firstName},\n\n` +
      (approved
        ? `Your peer-mentor application has been approved. You can now publish session slots from the ` +
          `Peer-Mentor page on scholarly.space, and students will be able to book time with you.`
        : `Thank you for applying to the peer-mentor programme. We are not approving the application right now.`) +
      (note ? `\n\nNote from the team:\n${note}` : ""),
    html: layout(
      para(`Hi ${firstName},`) +
        para(
          approved
            ? `Your peer-mentor application has been <strong style="color:#ffffff;">approved</strong>. You can now publish session slots from the Peer-Mentor page, and students will be able to book time with you.`
            : `Thank you for applying to the peer-mentor programme. We are not approving the application right now.`,
        ) +
        (note ? para(`<span style="color:#8a97b1;">Note from the team: ${note}</span>`) : ""),
    ),
  });

  revalidatePath("/admin/peer-mentors");
  revalidatePath("/mentor");
  return { ok: true };
}
