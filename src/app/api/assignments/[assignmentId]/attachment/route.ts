import { NextResponse } from "next/server";

import { auth } from "@/lib/auth";
import { streamPrivateBlob } from "@/lib/classroom/blob";
import { decodeDataUri, safeFilename } from "@/lib/data-uri";
import { prisma } from "@/lib/prisma";

/**
 * The worksheet a teacher attached to an assignment.
 *
 * Readable by the class's teacher and by the students in that class, nobody
 * else — the id is a cuid, but an unguessable URL is not an access control.
 */

export const dynamic = "force-dynamic";

export async function GET(
  _request: Request,
  { params }: { params: { assignmentId: string } },
) {
  const session = await auth();
  const userId = session?.user?.id;
  if (!userId) return NextResponse.json({ error: "Not authorized." }, { status: 401 });

  const assignment = await prisma.classAssignment.findFirst({
    where: {
      id: params.assignmentId,
      class: {
        OR: [{ teacherUserId: userId }, { memberships: { some: { userId } } }],
      },
    },
    select: { attachmentName: true, attachmentData: true },
  });
  if (!assignment?.attachmentData) {
    return NextResponse.json({ error: "Not found." }, { status: 404 });
  }

  // Blob-backed attachments live in a private store — stream them out here,
  // after the access decision above. The URL alone opens nothing.
  if (assignment.attachmentData.startsWith("https://")) {
    return streamPrivateBlob(assignment.attachmentData, assignment.attachmentName);
  }

  const file = decodeDataUri(assignment.attachmentData);
  if (!file) return NextResponse.json({ error: "Not found." }, { status: 404 });

  const name = safeFilename(assignment.attachmentName, "assignment");
  return new NextResponse(file.body, {
    headers: {
      "Content-Type": file.contentType,
      "Content-Length": String(file.body.byteLength),
      "Content-Disposition": `inline; filename="${name}"`,
      // Private: this is class material behind a login, never a shared cache.
      "Cache-Control": "private, max-age=3600",
    },
  });
}
