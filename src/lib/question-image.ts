/**
 * The `src` a client should use for a question's figure.
 *
 * Figures live on `Question.imageUrl` in two shapes: a base64 `data:` URI for
 * everything inserted before Blob storage existed, and a real path for
 * everything since. Handed to the browser as-is, the first shape is serialized
 * into the page payload on every render — hundreds of kilobytes per module,
 * rebuilt each time, and Active CPU is billed for exactly that kind of work.
 *
 * So data URIs are swapped for a route the browser can fetch once and cache;
 * real paths are already fine and pass through untouched.
 *
 * Where a page can avoid selecting `imageUrl` at all — the live exam, which
 * knows only *which* questions have a figure — that is better still, because
 * the bytes never leave Postgres. This helper is for the pages that have the
 * column in hand already.
 */
export function questionImageSrc(
  questionId: string,
  imageUrl: string | null | undefined
): string | null {
  if (!imageUrl) return null;
  return imageUrl.startsWith("data:") ? `/api/question-image/${questionId}` : imageUrl;
}
