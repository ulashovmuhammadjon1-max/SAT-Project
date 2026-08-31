"use client";

import { useEffect, useState, useTransition } from "react";

import { Button } from "@/components/ui/button";
import {
  type BroadcastStatus,
  referralContestStandings,
  referralContestStatus,
  sendReferralContestBatch,
} from "@/server/actions/admin/broadcast";

/**
 * Send the referral-contest announcement to every registered student.
 *
 * Sending is irreversible and goes to real people, so the design is: show the
 * exact message first, state the recipient count, and require a deliberate
 * second click on a confirmation. After that it drives itself — each call
 * sends one provider batch and returns progress, and the component keeps
 * calling until nothing is left, because 650 recipients cannot be delivered in
 * one serverless invocation.
 *
 * Progress is stored server-side, so closing this page mid-send loses nothing
 * and reopening it resumes where it stopped rather than starting over.
 */
export function ReferralContestBroadcast() {
  const [status, setStatus] = useState<BroadcastStatus | null>(null);
  const [standings, setStandings] = useState<Awaited<ReturnType<typeof referralContestStandings>> | null>(null);
  const [confirming, setConfirming] = useState(false);
  const [running, setRunning] = useState(false);
  const [showPreview, setShowPreview] = useState(false);
  const [, start] = useTransition();

  useEffect(() => {
    start(async () => {
      setStatus(await referralContestStatus());
      setStandings(await referralContestStandings());
    });
  }, []);

  async function runAll() {
    setRunning(true);
    setConfirming(false);
    try {
      // Loop until the server says nothing is left. Bounded so a persistent
      // provider failure cannot spin forever.
      for (let guard = 0; guard < 40; guard++) {
        const next = await sendReferralContestBatch();
        setStatus(next);
        if (next.remaining === 0 || next.error?.startsWith("Nothing sent")) break;
      }
      setStandings(await referralContestStandings());
    } finally {
      setRunning(false);
    }
  }

  if (!status) return <p className="text-sm text-muted-foreground">Loading…</p>;

  const done = status.remaining === 0 && status.sent > 0;

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-3 text-sm">
        <span className="font-medium">{status.total} registered accounts</span>
        <span className="text-muted-foreground">·</span>
        <span className={done ? "text-emerald-500" : "text-muted-foreground"}>
          {status.sent} sent, {status.remaining} remaining
        </span>
        {status.startedAt && (
          <>
            <span className="text-muted-foreground">·</span>
            <span className="text-muted-foreground">
              counting from {new Date(status.startedAt).toLocaleString()}
            </span>
          </>
        )}
      </div>

      {status.error && <p className="text-sm text-destructive">{status.error}</p>}

      <div className="flex flex-wrap gap-2">
        <Button type="button" variant="outline" size="sm" onClick={() => setShowPreview((v) => !v)}>
          {showPreview ? "Hide preview" : "Preview the email"}
        </Button>

        {status.remaining > 0 && !confirming && !running && (
          <Button type="button" size="sm" onClick={() => setConfirming(true)}>
            Send to {status.remaining} students…
          </Button>
        )}
        {confirming && (
          <>
            <Button type="button" size="sm" variant="destructive" onClick={runAll}>
              Yes, email {status.remaining} people now
            </Button>
            <Button type="button" size="sm" variant="ghost" onClick={() => setConfirming(false)}>
              Cancel
            </Button>
          </>
        )}
        {running && <span className="self-center text-sm text-muted-foreground">Sending…</span>}
        {done && <span className="self-center text-sm text-emerald-500">All sent.</span>}
      </div>

      {confirming && (
        <p className="text-xs text-muted-foreground">
          This cannot be undone. Each student receives their own invite link, and the contest clock
          starts on the first batch — referrals from that moment on are what count.
        </p>
      )}

      {showPreview && (
        <div className="rounded-lg border border-border">
          <p className="border-b border-border px-3 py-2 text-xs text-muted-foreground">
            Subject: <span className="text-foreground">{status.previewSubject}</span>
          </p>
          <iframe
            title="Email preview"
            srcDoc={status.previewHtml}
            className="h-[520px] w-full rounded-b-lg bg-white"
          />
        </div>
      )}

      {standings?.startedAt && (
        <div className="rounded-lg border border-border p-3">
          <p className="mb-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
            Standings since the contest started · first to {standings.target} wins
          </p>
          {standings.rows.length === 0 ? (
            <p className="text-sm text-muted-foreground">No qualifying invites yet.</p>
          ) : (
            <ol className="space-y-1 text-sm">
              {standings.rows.map((r, i) => (
                <li key={i} className="flex justify-between gap-4">
                  <span>
                    {i + 1}. {r.name ?? "Unnamed"}
                  </span>
                  <span className="tabular-nums text-muted-foreground">{r.qualified}</span>
                </li>
              ))}
            </ol>
          )}
        </div>
      )}
    </div>
  );
}
