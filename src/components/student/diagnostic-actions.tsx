"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { ArrowRight, Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { enableDiagnostic, startIeltsDiagnostic, startSatDiagnostic } from "@/server/actions/student/diagnostic";

/** Start or continue a diagnostic; the server pins the test and says where to go. */
export function StartDiagnosticButton({
  kind,
  label,
  size = "default",
  variant = "default",
}: {
  kind: "SAT" | "IELTS";
  label: string;
  size?: "default" | "sm" | "lg";
  variant?: "default" | "outline";
}) {
  const router = useRouter();
  const [pending, start] = useTransition();
  return (
    <Button
      size={size}
      variant={variant}
      disabled={pending}
      onClick={() =>
        start(async () => {
          const r = kind === "SAT" ? await startSatDiagnostic() : await startIeltsDiagnostic();
          if (!r.ok) return void toast.error(r.error);
          router.push(r.href);
        })
      }
      className="gap-2"
    >
      {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : null}
      {label}
      {!pending && <ArrowRight className="h-4 w-4" />}
    </Button>
  );
}

/** For students who said "not now" at sign-up. */
export function EnableDiagnosticButton({ kind, label }: { kind: "SAT" | "IELTS"; label: string }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  return (
    <Button
      variant="outline"
      disabled={pending}
      onClick={() =>
        start(async () => {
          await enableDiagnostic(kind);
          toast.success("Your free diagnostic is ready.");
          router.refresh();
        })
      }
    >
      {pending && <Loader2 className="h-4 w-4 animate-spin" />} {label}
    </Button>
  );
}
