"use client";

import { ErrorScreen } from "@/components/shared/error-screen";

export default function OnboardingError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <ErrorScreen
      error={error}
      reset={reset}
      title="Something interrupted setup"
      message="Your answers so far are saved in this browser, so trying again should pick back up where you left off."
      homeHref="/"
      homeLabel="Back to homepage"
    />
  );
}
