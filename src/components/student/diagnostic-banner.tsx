import Link from "next/link";
import { ArrowRight, FlaskConical } from "lucide-react";

import { getMyDiagnostics } from "@/server/actions/student/diagnostic";

/**
 * Dashboard card for an enabled diagnostic the student has not finished yet.
 * Renders nothing once every enabled diagnostic is done, or if none is enabled.
 */
export async function DiagnosticBanner() {
  const pending = (await getMyDiagnostics()).filter((d) => d.state !== "DONE");
  if (pending.length === 0) return null;
  const inProgress = pending.some((d) => d.state === "IN_PROGRESS");
  const kinds = pending.map((d) => d.kind);
  const what =
    kinds.length === 2
      ? "your SAT diagnostic and IELTS essay"
      : kinds[0] === "SAT"
        ? "25 questions, about 35 minutes — an estimated score and your weakest skills"
        : "one Writing Task 2 essay, marked by a real person";

  return (
    <Link
      href="/diagnostic"
      className="group flex flex-col gap-4 overflow-hidden rounded-2xl border border-primary/30 bg-gradient-to-r from-primary/[0.12] via-card to-card p-5 shadow-soft transition-shadow hover:shadow-md sm:flex-row sm:items-center sm:p-6"
    >
      <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-primary text-primary-foreground shadow-sm">
        <FlaskConical className="h-6 w-6" />
      </span>
      <span className="min-w-0 flex-1">
        <span className="block text-xs font-semibold uppercase tracking-wider text-primary">Free diagnostic</span>
        <span className="mt-0.5 block font-display text-lg font-semibold tracking-tight">
          {inProgress ? "Pick up your diagnostic where you left off" : "Your free diagnostic test is ready"}
        </span>
        <span className="block text-sm text-muted-foreground">{what}.</span>
      </span>
      <span className="inline-flex items-center gap-1.5 self-start rounded-xl bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground sm:self-auto">
        {inProgress ? "Continue" : "Start now"} <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
      </span>
    </Link>
  );
}
