"use client";

import { ErrorScreen } from "@/components/shared/error-screen";

export default function StudentError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <ErrorScreen
      error={error}
      reset={reset}
      message="An unexpected error occurred. Your saved progress isn't affected — try again, or head back to your dashboard."
      homeHref="/dashboard"
      homeLabel="Back to dashboard"
    />
  );
}
