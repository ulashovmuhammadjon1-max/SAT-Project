import { NextResponse } from "next/server";

import { auth } from "@/lib/auth";
import { decodeDataUri, safeFilename } from "@/lib/data-uri";
import { prisma } from "@/lib/prisma";

/**
 * A student's handed-in work.
 *
 * Two readers only: the student who uploaded it, and the teacher of the class
 * the assignment belongs to. Classmates deliberately cannot see each other's
 * work — a shared class is not consent to read someone's essay.
 */

export const dynamic = "force-dynamic";

export async function GET(
  _request: Request,
  { params }: { params: { assignmentId: string; studentId: string } },
) {
  const session = await auth();
  const userId = session?.user?.id;
  if (!userId) return NextResponse.json({ error: "Not authorized." }, { status: 401 });

  const completion = await prisma.assignmentCompletion.findFirst({
    where: {
      assignmentId: params.assignmentId,
      userId: params.studentId,
      OR: [
        { userId },
        { assignment: { class: { teacherUserId: userId } } },
      ],
    },
    select: { fileName: true, fileData: true },
  });
  if (!completion?.fileData) {
    return NextResponse.json({ error: "Not found." }, { status: 404 });
  }

  const file = decodeDataUri(completion.fileData);
  if (!file) return NextResponse.json({ error: "Not found." }, { status: 404 });

  const name = safeFilename(completion.fileName, "submission");
  return new NextResponse(file.body, {
    headers: {
      "Content-Type": file.contentType,
      "Content-Length": String(file.body.byteLength),
      "Content-Disposition": `inline; filename="${name}"`,
      "Cache-Control": "private, max-age=3600",
    },
  });
}
