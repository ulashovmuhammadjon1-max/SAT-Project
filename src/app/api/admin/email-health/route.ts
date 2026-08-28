import { NextResponse } from "next/server";

import { sendEmail } from "@/lib/email";
import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";

/**
 * Email observability, admin-only.
 *
 * sendEmail() deliberately never surfaces failures to students — a signup must
 * not fail because a mail provider is down. The cost is that a misconfigured
 * key fails in total silence, which has now caused a multi-day outage nobody
 * could see. This endpoint is the pressure gauge:
 *
 *   GET  — what the runtime actually has: is RESEND_API_KEY present, its
 *          shape (first characters + length, never the whole key), EMAIL_FROM.
 *   POST — send a real test email to the calling admin and return the
 *          provider's raw result, including its error text on failure.
 */

export const dynamic = "force-dynamic";

async function requireAdminApi() {
  const user = await getCurrentUser();
  if (!user) return null;
  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { role: true, email: true },
  });
  return row?.role === "ADMIN" ? { email: row.email } : null;
}

export async function GET() {
  const admin = await requireAdminApi();
  if (!admin) return NextResponse.json({ error: "admin only" }, { status: 403 });

  const key = process.env.RESEND_API_KEY ?? "";
  return NextResponse.json({
    resendKeyPresent: key.length > 0,
    // Enough to spot a wrong/truncated/whitespace-padded value, never the key.
    resendKeyShape: key ? `${key.slice(0, 5)}… (${key.length} chars)` : null,
    resendKeyHasWhitespace: key !== key.trim(),
    emailFrom: process.env.EMAIL_FROM ?? "(unset — falls back to onboarding@resend.dev)",
  });
}

export async function POST() {
  const admin = await requireAdminApi();
  if (!admin) return NextResponse.json({ error: "admin only" }, { status: 403 });

  const result = await sendEmail({
    to: admin.email,
    subject: "Scholarly email health check",
    text: "If you can read this, transactional email is working end to end.",
  });
  return NextResponse.json(result);
}
