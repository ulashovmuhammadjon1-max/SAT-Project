"use client";

import { useState } from "react";
import { Check, Copy, Download, Share2 } from "lucide-react";

import { Button } from "@/components/ui/button";

export interface ScoreCardData {
  studentName: string;
  testTitle: string;
  total: number;
  rw: number | null;
  math: number | null;
  correct: number;
  outOf: number;
  dateLabel: string;
  percentile: number | null;
  improvement: number | null;
}

/**
 * A screenshot-shaped summary of one test result.
 *
 * Students already share results — by photographing their screen. This gives
 * them something worth photographing, and puts the site name in the frame when
 * they do. That is the whole mechanism: the card is the advertisement.
 *
 * It is deliberately built from ordinary DOM rather than rendered to an image
 * on the server. A canvas render would need fonts embedded and a headless
 * browser in the request path; a styled div screenshots just as well on a
 * phone, works offline, and cannot break the results page if it fails.
 */
export function ScoreCard({ data }: { data: ScoreCardData }) {
  const [copied, setCopied] = useState(false);

  const shareText =
    `I scored ${data.total} on ${data.testTitle} at SATForge` +
    (data.improvement && data.improvement > 0 ? ` — up ${data.improvement} points.` : ".") +
    ` Free SAT practice: satforge.org`;

  async function share() {
    // The Web Share API is the good path on a phone, which is where this gets
    // used. It rejects when the user dismisses the sheet, so a failure falls
    // back to the clipboard rather than surfacing an error.
    if (typeof navigator !== "undefined" && navigator.share) {
      try {
        await navigator.share({ text: shareText, url: "https://satforge.org" });
        return;
      } catch {
        /* dismissed — fall through to copying */
      }
    }
    await copy();
  }

  async function copy() {
    try {
      await navigator.clipboard.writeText(shareText);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      /* clipboard blocked; the text is visible on the card regardless */
    }
  }

  return (
    <div className="space-y-3">
      {/* The card itself — self-contained so a screenshot crops cleanly. */}
      <div
        id="satforge-score-card"
        className="overflow-hidden rounded-2xl bg-gradient-to-br from-navy-900 via-navy-900 to-primary/40 p-6 text-white shadow-lg"
      >
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0">
            <p className="truncate text-sm font-medium text-white/80">{data.studentName}</p>
            <p className="truncate text-xs text-white/60">
              {data.testTitle} · {data.dateLabel}
            </p>
          </div>
          <p className="shrink-0 font-display text-sm font-semibold tracking-tight">SATForge</p>
        </div>

        <div className="mt-6 flex items-end gap-3">
          <p className="font-display text-6xl font-semibold leading-none tabular-nums">
            {data.total}
          </p>
          <p className="pb-1 text-sm text-white/60">/ 1600</p>
          {data.improvement != null && data.improvement > 0 && (
            <p className="ml-auto pb-1 text-sm font-medium text-emerald-300">
              +{data.improvement} pts
            </p>
          )}
        </div>

        <div className="mt-6 grid grid-cols-3 gap-3 text-center">
          <Metric label="Reading & Writing" value={data.rw} />
          <Metric label="Math" value={data.math} />
          <Metric label="Correct" value={`${data.correct}/${data.outOf}`} />
        </div>

        {data.percentile != null && (
          <p className="mt-5 rounded-lg bg-white/10 px-3 py-2 text-center text-xs text-white/85">
            Better than {data.percentile}% of students who took this test
          </p>
        )}

        <p className="mt-5 text-center text-[11px] text-white/50">
          Free, non-profit SAT practice · satforge.org
        </p>
      </div>

      <div className="flex flex-wrap gap-2">
        <Button size="sm" onClick={share}>
          <Share2 className="h-4 w-4" /> Share result
        </Button>
        <Button size="sm" variant="outline" onClick={copy}>
          {copied ? <Check className="h-4 w-4" /> : <Copy className="h-4 w-4" />}
          {copied ? "Copied" : "Copy text"}
        </Button>
        <p className="flex items-center gap-1.5 text-xs text-muted-foreground">
          <Download className="h-3.5 w-3.5" />
          Or screenshot the card above.
        </p>
      </div>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: number | string | null }) {
  return (
    <div className="rounded-lg bg-white/10 px-2 py-2.5">
      <p className="font-display text-xl font-semibold tabular-nums">{value ?? "—"}</p>
      <p className="mt-0.5 text-[10px] leading-tight text-white/60">{label}</p>
    </div>
  );
}
