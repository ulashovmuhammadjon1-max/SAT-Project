"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { PlayCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { clearQbSession, readQbSession, type StoredQbSession } from "@/lib/practice/qb-session-storage";

/**
 * "Pick up where you left off" for an unfinished Question Bank session.
 *
 * The session lives in `localStorage`, which a server component cannot read, so
 * this renders nothing on the server and fills in after mount. That also keeps
 * it out of the way entirely for students who have no session waiting.
 */
export function ResumeSessionCard() {
  const [session, setSession] = useState<StoredQbSession | null>(null);

  useEffect(() => {
    setSession(readQbSession());
  }, []);

  if (!session) return null;

  const remaining = session.total - session.answered;
  if (remaining <= 0) return null;

  return (
    <Card className="border-primary/40 bg-primary/5">
      <CardContent className="flex flex-wrap items-center gap-4 p-4">
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
          <PlayCircle className="h-4 w-4" />
        </span>
        <div className="min-w-0 flex-1">
          <p className="font-medium leading-snug">Continue your practice session</p>
          <p className="mt-0.5 text-[13px] text-muted-foreground">
            {session.label} — you were on question {session.index + 1} of {session.total},{" "}
            {remaining} still to answer.
          </p>
        </div>
        <div className="flex gap-2">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => {
              clearQbSession(session.signature);
              setSession(null);
            }}
          >
            Discard
          </Button>
          <Button asChild size="sm">
            <Link href={session.href}>Resume</Link>
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
