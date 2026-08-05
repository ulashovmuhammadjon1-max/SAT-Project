"use client";

import { ErrorScreen } from "@/components/shared/error-screen";

export default function AuthError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <ErrorScreen
      error={error}
      reset={reset}
      title="Something went wrong signing in"
      message="An unexpected error occurred. Please try again."
      homeHref="/"
      homeLabel="Back to homepage"
    />
  );
}
