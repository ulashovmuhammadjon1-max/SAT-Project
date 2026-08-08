"use client";

import { useState } from "react";
import { Check, Copy, Share2 } from "lucide-react";

import { Button } from "@/components/ui/button";

/**
 * Copy/share control for the referral link.
 *
 * `navigator.share` is offered only where it exists — most students will reach
 * this from Instagram or Telegram on a phone, where the native share sheet is
 * the fastest path. Desktop falls back to copy. The clipboard write can reject
 * (permissions, insecure origin), so failure selects the text instead of
 * silently doing nothing.
 */
export function ReferralLink({ link, reward }: { link: string; reward: number }) {
  const [copied, setCopied] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function copy() {
    setError(null);
    try {
      await navigator.clipboard.writeText(link);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setError("Couldn't copy automatically — select the link above and copy it.");
    }
  }

  async function share() {
    const data = {
      title: "SATForge",
      text: `Free SAT prep with a personalized plan — join me on SATForge and we both get ${reward} coins.`,
      url: link,
    };
    try {
      if (navigator.share) await navigator.share(data);
      else await copy();
    } catch {
      /* the user dismissed the share sheet — not an error */
    }
  }

  const canShare = typeof navigator !== "undefined" && "share" in navigator;

  return (
    <div className="space-y-3">
      <div className="flex flex-col gap-2 sm:flex-row">
        <input
          readOnly
          value={link}
          onFocus={(e) => e.currentTarget.select()}
          aria-label="Your referral link"
          className="min-w-0 flex-1 rounded-lg border border-input bg-secondary/50 px-3 py-2 font-mono text-sm text-foreground"
        />
        <div className="flex gap-2">
          <Button onClick={copy} className="flex-1 sm:flex-none">
            {copied ? <Check className="mr-2 h-4 w-4" /> : <Copy className="mr-2 h-4 w-4" />}
            {copied ? "Copied" : "Copy"}
          </Button>
          {canShare && (
            <Button onClick={share} variant="outline" className="flex-1 sm:flex-none">
              <Share2 className="mr-2 h-4 w-4" />
              Share
            </Button>
          )}
        </div>
      </div>
      {error && <p className="text-sm text-destructive">{error}</p>}
    </div>
  );
}
