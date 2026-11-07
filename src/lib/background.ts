import { waitUntil } from "@vercel/functions";

/**
 * Run work after the response is sent, without making the caller wait.
 *
 * On Vercel, `waitUntil` keeps the function alive until the promise settles,
 * so an email sent "in the background" is not cut off when the response
 * returns. Elsewhere (local dev, `next start`) the process is long-lived and
 * the promise simply runs on. Errors are logged, never thrown at the caller —
 * a background failure must not undo the foreground action that queued it.
 */
export function runInBackground(label: string, task: () => Promise<unknown>): void {
  const p = task().catch((error) => console.error(`[background:${label}]`, error));
  try {
    waitUntil(p);
  } catch {
    /* not in a request context: the promise is already running */
  }
}
