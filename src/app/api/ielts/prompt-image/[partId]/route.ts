import { NextResponse } from "next/server";

import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";
import { getReviewerCapabilities } from "@/lib/ielts/access";
import {
  contentTypeFor, isManagedPromptImage, readPromptImage,
} from "@/lib/ielts/image-storage";

/**
 * Serve a Writing Task 1 figure.
 *
 * Two kinds of image come through here and they have different audiences:
 *
 * - A figure on a **published** paper is content. Any signed-in student may see
 *   it, the same as the prompt text beside it.
 * - A figure a student uploaded with **their own topic** is theirs. Only they
 *   and the people who mark their work may see it — a chart someone
 *   photographed out of a book they own is not something to hand to the rest
 *   of the cohort.
 *
 * Everything unauthorised gets a 404 rather than a 403, so a stranger cannot
 * learn that a given image exists.
 */
export async function GET(
  _req: Request,
  { params }: { params: { partId: string } }
) {
  const user = await getCurrentUser();
  if (!user) return new NextResponse("Not found", { status: 404 });

  const part = await prisma.ieltsPart.findUnique({
    where: { id: params.partId },
    select: {
      imageUrl: true,
      section: { select: { test: { select: { id: true, status: true } } } },
    },
  });
  if (!part?.imageUrl || !isManagedPromptImage(part.imageUrl)) {
    return new NextResponse("Not found", { status: 404 });
  }

  let allowed = part.section.test.status === "PUBLISHED" || user.role === "ADMIN";
  if (!allowed) {
    // An unpublished paper is a student's own custom topic. Ownership is the
    // attempt on it — created when the topic is, precisely so this check has
    // something to read before any work has been submitted.
    const mine = await prisma.ieltsAttempt.findFirst({
      where: { testId: part.section.test.id, userId: user.id },
      select: { id: true },
    });
    allowed = Boolean(mine);
  }
  if (!allowed) {
    const caps = await getReviewerCapabilities(user.id);
    allowed = Boolean(caps?.canReviewWriting);
  }
  if (!allowed) return new NextResponse("Not found", { status: 404 });

  try {
    const buffer = await readPromptImage(part.imageUrl);
    return new NextResponse(new Uint8Array(buffer), {
      headers: {
        "Content-Type": contentTypeFor(part.imageUrl),
        "Content-Length": String(buffer.byteLength),
        // Private, but cacheable by the browser: a student stares at the same
        // chart for twenty minutes and should not refetch it on every render.
        "Cache-Control": "private, max-age=3600",
      },
    });
  } catch {
    return new NextResponse("Not found", { status: 404 });
  }
}
