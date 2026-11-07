import { NextResponse } from "next/server";

import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";
import { getReviewerCapabilities } from "@/lib/ielts/access";
import { contentTypeFor, readPromptImage } from "@/lib/ielts/image-storage";

/**
 * Serve the image a student attached to their Writing Task 1 response.
 *
 * It is the student's own work, so only they and the people who mark it may
 * see it: the owner, an admin, or a reviewer who reviews Writing. Everything
 * else gets a 404 rather than a 403, so a stranger cannot learn the image
 * exists.
 */
export async function GET(
  _req: Request,
  { params }: { params: { submissionId: string } }
) {
  const user = await getCurrentUser();
  if (!user) return new NextResponse("Not found", { status: 404 });

  const submission = await prisma.ieltsWritingSubmission.findUnique({
    where: { id: params.submissionId },
    select: { userId: true, responseImage: true },
  });
  if (!submission?.responseImage) return new NextResponse("Not found", { status: 404 });

  let allowed = submission.userId === user.id || user.role === "ADMIN";
  if (!allowed) {
    const caps = await getReviewerCapabilities(user.id);
    allowed = Boolean(caps?.canReviewWriting);
  }
  if (!allowed) return new NextResponse("Not found", { status: 404 });

  try {
    const buffer = await readPromptImage(submission.responseImage);
    return new NextResponse(new Uint8Array(buffer), {
      headers: {
        "Content-Type": contentTypeFor(submission.responseImage),
        "Content-Length": String(buffer.byteLength),
        // Private, and short: the student can replace the image while drafting,
        // and the editor adds a version query when they do.
        "Cache-Control": "private, max-age=300",
        "X-Content-Type-Options": "nosniff",
      },
    });
  } catch {
    return new NextResponse("Not found", { status: 404 });
  }
}
