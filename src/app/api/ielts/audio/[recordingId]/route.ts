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

  let buffer: Buffer;
  try {
    buffer = await readAudioRecording(recording.audioUrl);
  } catch {
    return new NextResponse("Not found", { status: 404 });
  }

  const contentType = contentTypeFor(recording.audioUrl);
  const base = {
    "Content-Type": contentType,
    "Cache-Control": "private, no-store",
    "Content-Disposition": "inline",
    // Without this a browser will not attempt a ranged request at all, and a
    // reviewer cannot scrub back to re-hear a phrase.
    "Accept-Ranges": "bytes",
  };

  // Range support. A recording is small enough to read whole, so this slices
  // what is already in memory rather than streaming from disk — the point is
  // the 206 and the Content-Range, which is what makes the seek bar draggable.
  const range = _req.headers.get("range");
  const match = range?.match(/^bytes=(\d*)-(\d*)$/);
  if (match) {
    const size = buffer.byteLength;
    const start = match[1] ? Number(match[1]) : 0;
    const end = match[2] ? Math.min(Number(match[2]), size - 1) : size - 1;
    if (Number.isNaN(start) || Number.isNaN(end) || start > end || start >= size) {
      return new NextResponse(null, {
        status: 416,
        headers: { ...base, "Content-Range": `bytes */${size}` },
      });
    }
    const slice = buffer.subarray(start, end + 1);
    return new NextResponse(new Uint8Array(slice), {
      status: 206,
      headers: {
        ...base,
        "Content-Range": `bytes ${start}-${end}/${size}`,
        "Content-Length": String(slice.byteLength),
      },
    });
  }

  return new NextResponse(new Uint8Array(buffer), {
    headers: { ...base, "Content-Length": String(buffer.byteLength) },
  });
}
