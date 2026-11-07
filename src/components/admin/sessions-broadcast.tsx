"use client";

import { useEffect, useState, useTransition } from "react";

import { Button } from "@/components/ui/button";
import {
  resetSessionsBroadcast,
  sendSessionsBroadcastBatch,
  sessionsBroadcastStatus,
  type SessionsBroadcastStatus,
} from "@/server/actions/admin/sessions-broadcast";

/**
 * Email the most active students that new sessions are open.
 *
 * Same flow as the referral broadcast: preview the exact email, see how many
 * people get it, confirm with a second click, then it sends batch by batch
 * until done. Progress is stored on the server, so closing the page mid-send
 * is safe and nobody is emailed twice.
 */
export function SessionsBroadcast() {
  const [status, setStatus] = useState<SessionsBroadcastStatus | null>(null);
  const [confirming, setConfirming] = useState(false);
  const [running, setRunning] = useState(false);
  const [showPreview, setShowPreview] = useState(false);
  const [, start] = useTransition();

  useEffect(() => {
    start(async () => setStatus(await sessionsBroadcastStatus()));
  }, []);

  async function runAll() {
    setRunning(true);
    setConfirming(false);
    try {
      for (let guard = 0; guard < 20; guard++) {
        const next = await sendSessionsBroadcastBatch();
        setStatus((prev) => ({ ...next, previewHtml: prev?.previewHtml, previewSubject: prev?.previewSubject }));
        if (next.remaining === 0 || next.error?.startsWith("Nothing sent") || next.sessions === 0) break;
      }
    } finally {
      setRunning(false);
    }
  }

  if (!status) return <p className="text-sm text-muted-foreground">Loading…</p>;

  const done = status.remaining === 0 && status.sent > 0;

  return (
    <div className="space-y-4">
      <p className="text-sm text-muted-foreground">
        Goes to the most active students of the last 90 days (practice, tests, AP, IELTS, streaks) who have a verified
        email and no session already booked. Lists every open 1-on-1 session with a link to book.
      </p>

      <div className="flex flex-wrap items-center gap-3 text-sm">
        <span className="font-medium">{status.sessions} open sessions</span>
        <span className="text-muted-foreground">·</span>
        <span className="font-medium">{status.total} students</span>
        <span className="text-muted-foreground">·</span>
        <span className={done ? "text-success" : "text-muted-foreground"}>
          {status.sent} sent, {status.remaining} remaining
        </span>
        {status.startedAt && (
          <>
            <span className="text-muted-foreground">·</span>
            <span className="text-muted-foreground">started {new Date(status.startedAt).toLocaleString()}</span>
          </>
        )}
      </div>

      {status.error && <p className="text-sm text-destructive">{status.error}</p>}

      <div className="flex flex-wrap gap-2">
        <Button type="button" variant="outline" onClick={() => setShowPreview((v) => !v)}>
          {showPreview ? "Hide preview" : "Preview the email"}
        </Button>

        {status.sessions > 0 && status.remaining > 0 && !confirming && !running && (
          <Button type="button" onClick={() => setConfirming(true)}>
            Send to {status.remaining} students…
          </Button>
        )}
        {confirming && (
          <>
            <Button type="button" variant="destructive" onClick={runAll}>
              Yes, email {status.remaining} students now
            </Button>
            <Button type="button" variant="ghost" onClick={() => setConfirming(false)}>
              Cancel
            </Button>
          </>
        )}
        {running && <span className="self-center text-sm text-muted-foreground">Sending…</span>}
        {done && !running && (
          <>
            <span className="self-center text-sm text-success">All sent.</span>
            <Button
              type="button"
              variant="ghost"
              onClick={() => start(async () => setStatus(await resetSessionsBroadcast()))}
            >
              Start a new round
            </Button>
          </>
        )}
      </div>

      {confirming && (
        <p className="text-xs text-muted-foreground">
          This cannot be undone. Each student gets one email, and anyone already emailed in this round is skipped.
        </p>
      )}
      {done && (
        <p className="text-xs text-muted-foreground">
          Next time you publish sessions, press &ldquo;Start a new round&rdquo; to pick fresh recipients.
        </p>
      )}

      {showPreview && status.previewHtml && (
        <div className="rounded-lg border border-border">
          <p className="border-b border-border px-3 py-2 text-xs text-muted-foreground">
            Subject: <span className="text-foreground">{status.previewSubject}</span>
          </p>
          <iframe title="Email preview" srcDoc={status.previewHtml} className="h-[620px] w-full rounded-b-lg bg-white" />
        </div>
      )}
    </div>
  );
}
