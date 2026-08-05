/**
 * `redirect()` from a Server Action works by throwing a special error that
 * Next.js's own machinery catches further up the tree — it is not a real
 * failure. A client component that wraps a Server Action call in try/catch
 * must let this one through, or it silently breaks the redirect (the action
 * runs, but the page never navigates) while looking like nothing happened.
 *
 * `next/navigation` doesn't publicly export a checker for this in Next 14, so
 * this checks the documented digest format directly rather than reaching into
 * `next/dist/...` internals, which are not a stable import path.
 */
export function isNextRedirectError(error: unknown): boolean {
  return (
    typeof error === "object" &&
    error !== null &&
    "digest" in error &&
    typeof (error as { digest: unknown }).digest === "string" &&
    (error as { digest: string }).digest.startsWith("NEXT_REDIRECT")
  );
}
