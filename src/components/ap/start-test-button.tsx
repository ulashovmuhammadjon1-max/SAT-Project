"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { ArrowRight, Loader2 } from "lucide-react";
import { toast } from "sonner";

import { startTest } from "@/server/actions/student/ap-tests";
import { cn } from "@/lib/utils";

/**
 * Starts or resumes a practice test.
 *
 * The attempt id comes back from the server, never from here — the button knows
 * only which test it belongs to. `startTest` decides whether that means a new
 * sitting or picking up an open one, so a student with a half-finished test
 * cannot accidentally start a second and lose the first.
 */
export function StartTestButton({
  subject,
  testSlug,
  resume,
  label,
}: {
  subject: string;
  testSlug: string;
  /** An open sitting exists; the button offers to continue it. */
  resume?: boolean;
  label?: string;
}) {
  const router = useRouter();
  const [pending, start] = useTransition();

  return (
    <button
      type="button"
      disabled={pending}
      onClick={() =>
        start(async () => {
          const res = await startTest({ subject, testSlug });
          if (res.error || !res.attemptId) {
            toast.error(res.error ?? "Could not start that test — try again.");
            return;
          }
          router.push(`/ap/tests/attempt/${res.attemptId}`);
        })
      }
      className={cn(
        "inline-flex items-center gap-1.5 rounded-lg px-4 py-2 text-sm font-medium text-white transition-colors disabled:opacity-60",
        resume ? "bg-warning hover:bg-warning/90" : "bg-primary hover:bg-primary/90",
      )}
    >
      {pending ? (
        <>
          <Loader2 className="h-4 w-4 animate-spin" /> Opening
        </>
      ) : (
        <>
          {label ?? (resume ? "Resume test" : "Start test")}
          <ArrowRight className="h-4 w-4" />
        </>
      )}
    </button>
  );
}
