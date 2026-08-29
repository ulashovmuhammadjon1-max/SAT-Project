import { get } from "@vercel/blob";
import { NextResponse } from "next/server";

import { safeFilename } from "@/lib/data-uri";

/**
 * Stream a private blob out through an already-authorized route.
 *
 * Classroom files live in a private Blob store: their URLs open nothing on
 * their own, so possession of a URL is worthless and the class-scoped routes
 * that call this are the only doors. The bytes are streamed rather than
 * buffered — Vercel's ~4.5MB payload cap applies to buffered bodies, not
 * streamed ones, which is what makes a 10MB download possible here at all.
 */
export async function streamPrivateBlob(url: string, name: string | null): Promise<NextResponse> {
  const result = await get(url, { access: "private" });
  if (!result) return NextResponse.json({ error: "Not found." }, { status: 404 });

  const filename = safeFilename(name, "file");
  const headers = new Headers();
  const contentType = result.headers.get("content-type");
  const contentLength = result.headers.get("content-length");
  if (contentType) headers.set("Content-Type", contentType);
  if (contentLength) headers.set("Content-Length", contentLength);
  headers.set("Content-Disposition", `inline; filename="${filename}"`);
  // Private to the requesting browser — never a shared cache.
  headers.set("Cache-Control", "private, max-age=3600");

  return new NextResponse(result.stream as unknown as ReadableStream, { headers });
}
