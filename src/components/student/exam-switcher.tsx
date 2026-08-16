"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import type { ExamMode } from "@prisma/client";
import { toast } from "sonner";

import { cn } from "@/lib/utils";
import { setActiveExam } from "@/server/actions/student/exam-mode";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";

/**
 * Switching between SATForge's two preparation products.
 *
 * Deliberately not styled as a nav item. Choosing SAT or IELTS changes the
 * sidebar, the hero, the plan, the question bank and the analytics — it is a
 * change of product, and a control that looks like a link would undersell what
 * it does.
 *
 * A segmented control on desktop, a compact dropdown below `sm` so it cannot
 * eat half a phone screen.
 */
export function ExamSwitcher({
  active,
  className,
}: {
  active: ExamMode;
  className?: string;
}) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  // Shown to every account. Both exams are open to everyone, so this is how a
  // student discovers IELTS exists — gating it behind an account that already
  // had two exams meant nobody would ever find it. Picking one enrols them on
  // the spot; there is no setup step to complete first.
  const modes: ExamMode[] = ["SAT", "IELTS", "BOTH"];
  const label: Record<ExamMode, string> = { SAT: "SAT", IELTS: "IELTS", BOTH: "Both" };

  const change = (mode: ExamMode) => {
    if (mode === active) return;
    startTransition(async () => {
      const result = await setActiveExam(mode);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      if (result.redirectTo) router.push(result.redirectTo);
      router.refresh();
    });
  };

  return (
    <>
      <div
        role="group"
        aria-label="Choose exam"
        className={cn(
          "hidden items-center gap-0.5 rounded-full border border-border bg-secondary/60 p-0.5 sm:inline-flex",
          isPending && "opacity-60",
          className
        )}
      >
        {modes.map((mode) => {
          const isActive = mode === active;
          return (
            <button
              key={mode}
              type="button"
              onClick={() => change(mode)}
              disabled={isPending}
              aria-pressed={isActive}
              className={cn(
                "rounded-full px-3 py-1 text-xs font-semibold transition-colors",
                "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                isActive
                  ? "bg-navy-900 text-white shadow-soft"
                  : "text-muted-foreground hover:text-foreground"
              )}
            >
              {label[mode]}
            </button>
          );
        })}
      </div>

      <div className={cn("sm:hidden", className)}>
        <Select value={active} onValueChange={(v) => change(v as ExamMode)} disabled={isPending}>
          <SelectTrigger className="h-8 w-[104px] text-xs" aria-label="Choose exam">
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            {modes.map((mode) => (
              <SelectItem key={mode} value={mode}>{label[mode]}</SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
    </>
  );
}
