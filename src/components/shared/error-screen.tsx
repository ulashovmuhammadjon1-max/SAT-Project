"use client";

import { useEffect } from "react";
import Link from "next/link";
import { AlertTriangle, RotateCcw } from "lucide-react";

import { Button } from "@/components/ui/button";

/**
 * Shared body for every route-level error.tsx boundary. Before these
 * existed, ANY uncaught exception anywhere in the app — a foreign-key
 * violation, a race condition, a network blip — surfaced as Next.js's raw
 * "Application error: a server-side exception has occurred" screen with
 * nothing a user could do except reload and hope. This gives every route
 * group the same graceful, actionable landing instead.
 */
export function ErrorScreen({
  error,
  reset,
  title = "Something went wrong",
  message = "An unexpected error occurred. You can try again, or head back and pick up where you left off.",
  homeHref = "/",
  homeLabel = "Go back",
  tone = "default",
}: {
  error: Error & { digest?: string };
  reset: () => void;
  title?: string;
  message?: string;
  homeHref?: string;
  homeLabel?: string;
  tone?: "default" | "dark";
}) {
  useEffect(() => {
    console.error("[error-boundary]", error);
  }, [error]);

  const dark = tone === "dark";

  return (
    <div
      className={
        dark
          ? "flex min-h-screen flex-col items-center justify-center bg-navy-950 px-6 text-center text-white"
          : "flex min-h-screen flex-col items-center justify-center bg-background px-6 text-center"
      }
    >
      <span
        className={
          dark
            ? "flex h-14 w-14 items-center justify-center rounded-2xl bg-white/10"
            : "flex h-14 w-14 items-center justify-center rounded-2xl bg-destructive/10"
        }
      >
        <AlertTriangle className={dark ? "h-7 w-7 text-white" : "h-7 w-7 text-destructive"} />
      </span>

      <h1 className="mt-5 font-display text-xl font-semibold tracking-tight sm:text-2xl">{title}</h1>
      <p className={dark ? "mt-2 max-w-md text-sm text-navy-200" : "mt-2 max-w-md text-sm text-muted-foreground"}>
        {message}
      </p>

      {error.digest && (
        <p className={dark ? "mt-3 text-xs text-navy-300" : "mt-3 text-xs text-muted-foreground/70"}>
          Error reference: {error.digest}
        </p>
      )}

      <div className="mt-7 flex flex-col items-center gap-3 sm:flex-row">
        <Button onClick={reset} className="min-w-[9rem]">
          <RotateCcw className="h-4 w-4" /> Try again
        </Button>
        <Button
          variant={dark ? "outline" : "ghost"}
          asChild
          className={dark ? "min-w-[9rem] border-white/20 bg-white/5 text-white hover:bg-white/10 hover:text-white" : "min-w-[9rem]"}
        >
          <Link href={homeHref}>{homeLabel}</Link>
        </Button>
      </div>
    </div>
  );
}
