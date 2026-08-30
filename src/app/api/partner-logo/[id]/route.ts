import { NextResponse } from "next/server";
import { get } from "@vercel/blob";

import { prisma } from "@/lib/prisma";

/**
 * A published partner's logo, served without a session.
 *
 * Partner logos were being rendered through `/api/images/...`, which requires
 * a signed-in user because the Blob store behind it also holds exam figures and
 * source PDFs. But the partners strip appears on the marketing landing page,
 * which only LOGGED-OUT visitors ever see — so every partner logo was a 401 to
 * exactly the audience a partner is there to reach. It looked fine to an
 * administrator, who is always signed in, which is why it went unnoticed.
 *
 * The fix is a route with a much narrower mouth than the general image
 * endpoint: it takes a Partner id, not a path. It will only ever serve a blob
 * that a PUBLISHED Partner row points at, so no amount of guessing at this URL
 * reaches an exam figure. Unpublished partners 404 like anything else.
 */
export async function GET(_request: Request, { params }: { params: { id: string } }) {
  const partner = await prisma.partner.findFirst({
    where: { id: params.id, isPublished: true },
    select: { logoUrl: true },
  });
  if (!partner) return NextResponse.json({ error: "Not found." }, { status: 404 });

  // An absolute URL is somebody else's CDN; nothing to proxy.
  if (/^https?:\/\//i.test(partner.logoUrl)) {
    return NextResponse.redirect(partner.logoUrl);
  }

  const pathname = partner.logoUrl.replace(/^\/api\/images\//, "");
  if (!pathname || pathname === partner.logoUrl) {
    return NextResponse.json({ error: "Not found." }, { status: 404 });
  }

  // This logo's stored name contains a space ("2026-08-31 01.09.40-...jpg"),
  // because the uploader kept the file's original name. The stored path is used
  // verbatim first, since that is what the blob was written as; the
  // percent-encoded form is tried only as a fallback, for a row whose path was
  // saved already encoded. Trying both costs one extra lookup on a cached route
  // and removes a whole class of "the logo just doesn't show" that is otherwise
  // invisible until someone loads the page.
  const candidates = [pathname];
  const encoded = pathname.split("/").map(encodeURIComponent).join("/");
  if (encoded !== pathname) candidates.push(encoded);
  try {
    let result = null;
    for (const candidate of candidates) {
      result = await get(candidate, { access: "private" }).catch(() => null);
      if (result?.stream) break;
    }
    if (!result?.stream) return NextResponse.json({ error: "Not found." }, { status: 404 });
    return new NextResponse(result.stream, {
      headers: {
        "Content-Type": result.blob.contentType || "application/octet-stream",
        // A published logo is public and rarely changes, so it can be cached
        // by the CDN rather than re-streamed through a function every time.
        "Cache-Control": "public, max-age=3600, s-maxage=86400",
      },
    });
  } catch {
    return NextResponse.json({ error: "Not found." }, { status: 404 });
  }
}
