import { NextResponse } from "next/server";
import { get } from "@vercel/blob";

import { auth } from "@/lib/auth";

// The Blob store backing question/passage figures is private (the account's
// only store, also used for source PDFs, doesn't allow public access — see
// storage.ts). Any signed-in user (admin or student, since students need to
// see figures during an exam) can stream an image through here; the actual
// blob token never reaches the browser.
export async function GET(request: Request, { params }: { params: { path: string[] } }) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Not authorized." }, { status: 401 });
  }

  const pathname = params.path.join("/");

  try {
    const result = await get(pathname, { access: "private" });
    if (!result || !result.stream) return NextResponse.json({ error: "Not found." }, { status: 404 });

    return new NextResponse(result.stream, {
      headers: {
        "Content-Type": result.blob.contentType || "application/octet-stream",
        "Cache-Control": "private, max-age=3600",
      },
    });
  } catch {
    return NextResponse.json({ error: "Not found." }, { status: 404 });
  }
}
