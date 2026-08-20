import { NextResponse } from "next/server";

import { auth } from "@/lib/auth";
import { prisma } from "@/lib/prisma";

/**
 * Serves a question's figure as a real image instead of an inline data URI.
 *
 * Most figures are stored on `Question.imageUrl` as a base64 `data:` URI. Sent
 * that way they are serialized into the page payload on **every** render of
 * every module containing them — the heaviest module in the bank carries
 * 898 KB of base64, and that string is built, escaped and streamed each time a
 * student opens it. Serializing payload is Active CPU; a database read is not,
 * because Vercel does not bill CPU during I/O.
 *
 * Behind this route the page carries a ~40-byte URL instead, the bytes are
 * fetched once by the browser and then cached, and a student paging back and
 * forth through a module re-fetches nothing.
 *
 * Auth-gated, so the cache is `private`: question figures are paid content and
 * a shared CDN copy would be readable by anyone with the id. The browser cache
 * is where the repeat-view saving comes from anyway.
 */

/** A year. Figures are immutable — editing one is a new question in practice. */
const ONE_YEAR = 31_536_000;

export async function GET(
  _request: Request,
  { params }: { params: { questionId: string } }
) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Not authorized." }, { status: 401 });
  }

  const question = await prisma.question.findUnique({
    where: { id: params.questionId },
    // Only this column. Selecting the row would pull the stem and every other
    // field to serve one image.
    select: { imageUrl: true },
  });

  if (!question?.imageUrl) {
    return NextResponse.json({ error: "Not found." }, { status: 404 });
  }

  const src = question.imageUrl;

  // Already a path or URL (Blob-backed figures) — send the caller there rather
  // than proxying bytes through this function.
  if (!src.startsWith("data:")) {
    return NextResponse.redirect(new URL(src, _request.url), 308);
  }

  // data:[<mediatype>][;base64],<data>
  const comma = src.indexOf(",");
  const header = src.slice(5, comma);
  const isBase64 = header.endsWith(";base64");
  const contentType = (isBase64 ? header.slice(0, -7) : header) || "image/png";
  const payload = src.slice(comma + 1);

  // Decoding to binary also drops about a quarter of the bytes on the wire:
  // base64 costs 4 characters for every 3 it encodes.
  const body = isBase64
    ? Buffer.from(payload, "base64")
    : Buffer.from(decodeURIComponent(payload), "utf8");

  return new NextResponse(body, {
    headers: {
      "Content-Type": contentType,
      "Content-Length": String(body.byteLength),
      "Cache-Control": `private, max-age=${ONE_YEAR}, immutable`,
    },
  });
}
