import { NextResponse } from "next/server";

import { auth } from "@/lib/auth";
import { decodeDataUri, safeFilename } from "@/lib/data-uri";
import { prisma } from "@/lib/prisma";

/**
 * One file from a student's submission.
 *
 * Two readers only: the student who uploaded it, and the teacher of the class
 * the assignment belongs to. Classmates deliberately cannot open each other's
 * work — sharing a class is not consent to read someone's essay. The check
 * walks file → completion → assignment → class, so a file can never be read
 * through any class other than the one its assignment belongs to.
 */

export const dynamic = "force-dynamic";

export async function GET(
  _request: Request,
  { params }: { params: { fileId: string } },
) {
  const session = await auth();
  const userId = session?.user?.id;
  if (!userId) return NextResponse.json({ error: "Not authorized." }, { status: 401 });

  const file = await prisma.submissionFile.findFirst({
    where: {
      id: params.fileId,
      completion: {
        OR: [
          { userId },
          { assignment: { class: { teacherUserId: userId } } },
        ],
      },
    },
    select: { name: true, data: true },
  });
  if (!file) return NextResponse.json({ error: "Not found." }, { status: 404 });

  const decoded = decodeDataUri(file.data);
  if (!decoded) return NextResponse.json({ error: "Not found." }, { status: 404 });

  const name = safeFilename(file.name, "submission");
  return new NextResponse(decoded.body, {
    headers: {
      "Content-Type": decoded.contentType,
      "Content-Length": String(decoded.body.byteLength),
      "Content-Disposition": `inline; filename="${name}"`,
      "Cache-Control": "private, max-age=3600",
    },
  });
}
