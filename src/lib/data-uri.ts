/**
 * Turn a stored `data:` URI back into a real HTTP response.
 *
 * Uploads on this platform — certificates, team photos, assignment worksheets,
 * students' handed-in work — are kept as data URIs on their own row rather
 * than in blob storage, so they cannot go missing separately from the record
 * they belong to. Serving them means decoding here.
 *
 * Decoding also drops about a quarter of the bytes on the wire: base64 costs
 * four characters for every three it encodes.
 */
export interface DecodedFile {
  /** `Uint8Array<ArrayBuffer>`, not the bare `Uint8Array`: `BodyInit` accepts a
   *  view over a real ArrayBuffer, and the default `ArrayBufferLike` parameter
   *  is wide enough that a `NextResponse` body rejects it. */
  body: Uint8Array<ArrayBuffer>;
  contentType: string;
}

export function decodeDataUri(src: string, fallbackType = "application/octet-stream"): DecodedFile | null {
  if (!src.startsWith("data:")) return null;
  const comma = src.indexOf(",");
  if (comma === -1) return null;

  const header = src.slice(5, comma);
  const isBase64 = header.endsWith(";base64");
  const contentType = (isBase64 ? header.slice(0, -7) : header) || fallbackType;
  const payload = src.slice(comma + 1);

  const body = isBase64
    ? Buffer.from(payload, "base64")
    : Buffer.from(decodeURIComponent(payload), "utf8");
  return { body, contentType };
}

/**
 * A filename safe to put in a Content-Disposition header.
 *
 * Quotes and newlines in the name would let an uploaded filename break out of
 * the header and inject one of its own, so everything outside a small safe set
 * is replaced rather than escaped.
 */
export function safeFilename(name: string | null, fallback: string): string {
  const cleaned = (name ?? "").replace(/[^A-Za-z0-9._ -]/g, "_").trim();
  return cleaned.length > 0 ? cleaned.slice(0, 120) : fallback;
}
