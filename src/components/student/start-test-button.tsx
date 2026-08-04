"use client";

import { useTransition } from "react";
import { Loader2, PlayCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { startAttempt } from "@/server/actions/student/attempts";

export function StartTestButton({ testId }: { testId: string }) {
  const [isPending, startTransition] = useTransition();

  return (
    <Button className="w-full" disabled={isPending} onClick={() => startTransition(() => startAttempt(testId))}>
      {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <PlayCircle className="h-4 w-4" />}
      Start test
    </Button>
  );
}
