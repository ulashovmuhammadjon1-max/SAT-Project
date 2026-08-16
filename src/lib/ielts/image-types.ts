/**
 * The parts of prompt-image handling that a browser needs.
 *
 * Split from `image-storage.ts` because that module imports `fs/promises` and
 * `@vercel/blob`: a client component asking it for the accepted MIME types
 * dragged the filesystem into the browser bundle and failed the build. Types
 * and pure string helpers here; anything that touches storage stays there.
 */

/** What a phone camera or a screenshot actually produces. */
export const IMAGE_EXT: Record<string, string> = {
  "image/png": "png",
  "image/jpeg": "jpg",
  "image/webp": "webp",
  "image/gif": "gif",
};

/**
 * SVG is deliberately absent.
 *
 * An SVG is a document that can carry script, and this one is uploaded by a
 * student and then displayed to a reviewer. The other four cannot execute
 * anything.
 */
export const ACCEPTED_IMAGE_TYPES = Object.keys(IMAGE_EXT);

/** Generous for a phone photo of a printed chart, mean for anything else. */
export const MAX_IMAGE_BYTES = 8 * 1024 * 1024;

export function extensionFor(mime: string): string {
  return IMAGE_EXT[(mime || "").split(";")[0].trim().toLowerCase()] ?? "png";
}

export function contentTypeFor(stored: string): string {
  const ext = stored.split(".").pop()?.toLowerCase() ?? "png";
  return Object.entries(IMAGE_EXT).find(([, e]) => e === ext)?.[0] ?? "image/png";
}

/**
 * Whether a stored value is one of ours or an ordinary URL.
 *
 * Admin-authored parts may carry a data URI or an `/api/images/...` path from
 * the older pipeline; those are already renderable and must pass through
 * untouched rather than being sent to the prompt-image route.
 */
export function isManagedPromptImage(value: string | null | undefined): boolean {
  if (!value) return false;
  return !value.startsWith("data:") && !value.startsWith("/") && !value.startsWith("http");
}

/** What an `<img src>` should point at for a given stored value. */
export function promptImageSrc(partId: string, value: string | null | undefined): string | null {
  if (!value) return null;
  return isManagedPromptImage(value) ? `/api/ielts/prompt-image/${partId}` : value;
}
