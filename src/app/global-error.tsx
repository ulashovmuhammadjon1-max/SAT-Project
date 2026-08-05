"use client";

/**
 * Catches errors thrown by the root layout itself, which `error.tsx` cannot
 * — Next.js requires this to render its own <html>/<body> since the layout
 * that would normally provide them is what crashed. Deliberately plain (no
 * shared components, no Tailwind-dependent chrome) so it can't itself fail.
 */
export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <html lang="en">
      <body
        style={{
          display: "flex",
          minHeight: "100vh",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: "system-ui, sans-serif",
          textAlign: "center",
          padding: "1.5rem",
        }}
      >
        <h1 style={{ fontSize: "1.25rem", fontWeight: 600 }}>Something went wrong</h1>
        <p style={{ marginTop: "0.5rem", color: "#6B7280", maxWidth: "28rem" }}>
          Summit Prep hit an unexpected error loading the page. Please try again.
        </p>
        {error.digest && (
          <p style={{ marginTop: "0.75rem", fontSize: "0.75rem", color: "#9CA3AF" }}>Error reference: {error.digest}</p>
        )}
        <button
          onClick={reset}
          style={{
            marginTop: "1.5rem",
            padding: "0.625rem 1.5rem",
            borderRadius: "9999px",
            background: "#2563EB",
            color: "white",
            fontWeight: 500,
            border: "none",
            cursor: "pointer",
          }}
        >
          Try again
        </button>
      </body>
    </html>
  );
}
