import { NextResponse } from "next/server";

import { getScenicImage } from "@/lib/backgrounds/pexels";
import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";

/**
 * Scenic-background observability, admin-only.
 *
 * Like the email-health route: a scenic background that cannot reach Pexels
 * fails quietly to a gradient, which is the right behaviour for a visitor but
 * makes a misconfigured key invisible. This is the pressure gauge — is
 * PEXELS_API_KEY present in this runtime, and does a real fetch succeed?
 *
 * Never returns the key, only its shape.
 */
export const dynamic = "force-dynamic";

export async function GET() {
  const user = await getCurrentUser();
  if (!user) return NextResponse.json({ error: "admin only" }, { status: 403 });
  const row = await prisma.user.findUnique({ where: { id: user.id }, select: { role: true } });
  if (row?.role !== "ADMIN") return NextResponse.json({ error: "admin only" }, { status: 403 });

  const key = process.env.PEXELS_API_KEY ?? "";
  const image = await getScenicImage("dashboard");

  return NextResponse.json({
    keyPresent: key.length > 0,
    keyShape: key ? `${key.slice(0, 4)}… (${key.length} chars)` : null,
    keyHasWhitespace: key !== key.trim(),
    fetchOk: Boolean(image),
    samplePhotographer: image?.photographer ?? null,
    // What a visitor would see right now: a photo, or the fallback gradient.
    rendering: image ? "photo" : "fallback-gradient",
  });
}
