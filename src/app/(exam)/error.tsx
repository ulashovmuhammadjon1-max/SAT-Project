"use client";

import { ErrorScreen } from "@/components/shared/error-screen";

/**
 * The exam route is the highest-stakes place in the app for a crash to
 * happen — a student mid-timed-test. The reassurance here is deliberately
 * specific and accurate rather than generic: answers autosave immediately on
 * every selection plus every 5 seconds, so "Try again" (which remounts the
 * page and re-fetches the attempt fresh from the server) reliably picks back
 * up at the last saved answer, not a blank test.
 */
export default function ExamError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <ErrorScreen
      error={error}
      reset={reset}
      tone="dark"
      title="Something interrupted your test"
      message="Your answers are saved as you go, so nothing you've already answered is lost. Try again to pick back up where you left off."
      homeHref="/dashboard"
      homeLabel="Save & exit to dashboard"
    />
  );
}
