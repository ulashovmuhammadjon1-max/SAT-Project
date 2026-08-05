"use client";

import { ErrorScreen } from "@/components/shared/error-screen";

export default function AdminError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <ErrorScreen
      error={error}
      reset={reset}
      title="Something went wrong in the admin panel"
      message="The action didn't go through. Nothing was left half-done — try again, or head back to the admin dashboard."
      homeHref="/admin"
      homeLabel="Back to admin dashboard"
    />
  );
}
