import { NextResponse } from "next/server";

import { prisma } from "@/lib/prisma";
import { getCurrentUser } from "@/lib/session";
import { getReviewerCapabilities } from "@/lib/ielts/access";
import { contentTypeFor, readAudioRecording } from "@/lib/ielts/audio-storage";

/**
 * Serve a Speaking recording, to the two people entitled to hear it.
 *
 * The owner and an approved Speaking reviewer (or an admin). Everyone else
 * gets a 404 rather than a 403: a 403 confirms the recording exists, which is
 * itself something a stranger should not learn about another student.
 *
 * Nothing here is cacheable by a shared cache — a CDN holding one student's
 * voice and handing it to the next request would defeat the whole check.
 */
export async function GET(
  _req: Request,
  { params }: { params: { recordingId: string } }
) {
  const user = await getCurrentUser();
  if (!user) return new NextResponse("Not found", { status: 404 });

  const recording = await prisma.ieltsSpeakingRecording.findUnique({
    where: { id: params.recordingId },
    select: {
      audioUrl: true,
      submission: { select: { userId: true, review: { select: { reviewerId: true } } } },
    },
  });
  if (!recording) return new NextResponse("Not found", { status: 404 });

  const isOwner = recording.submission.userId === user.id;
  const isAdmin = user.role === "ADMIN";
  let allowed = isOwner || isAdmin;
  if (!allowed) {
    const caps = await getReviewerCapabilities(user.id);
    // An approved Speaking reviewer may open the queue, so entitlement is the
    // capability rather than a prior assignment — a reviewer has to be able to
    // listen before they can claim a submission.
    allowed = Boolean(caps?.canReviewSpeaking);
  }
  if (!allowed) return new NextResponse("Not found", { status: 404 });

  try {
    const buffer = await readAudioRecording(recording.audioUrl);
    return new NextResponse(new Uint8Array(buffer), {
      headers: {
        "Content-Type": contentTypeFor(recording.audioUrl),
        "Content-Length": String(buffer.byteLength),
        "Cache-Control": "private, no-store",
        "Content-Disposition": "inline",
      },
    });
  } catch {
    return new NextResponse("Not found", { status: 404 });
  }
}
