"use client";

import { useEffect, useState } from "react";
import { BellRing, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { useLive } from "@/components/live/live-provider";
import { Switch } from "@/components/ui/switch";

const DISMISS_KEY = "scholarly-browser-prompt-dismissed";

/**
 * Asks for browser notification permission — never on page load. It appears
 * inside the notification dropdown once the student has at least looked at
 * their notifications, explains what it is for, and can be dismissed for good.
 * The settings page offers the same switch.
 */
export function BrowserAlertsPrompt({ compact }: { compact?: boolean }) {
  const { browserNotify, setBrowserNotify } = useLive();
  const [state, setState] = useState<"unknown" | "unsupported" | NotificationPermission>("unknown");
  const [dismissed, setDismissed] = useState(true);

  useEffect(() => {
    if (typeof window === "undefined" || !("Notification" in window)) {
      setState("unsupported");
      return;
    }
    setState(Notification.permission);
    try {
      setDismissed(localStorage.getItem(DISMISS_KEY) === "1");
    } catch {
      setDismissed(false);
    }
  }, []);

  async function enable() {
    if (!("Notification" in window)) return;
    const p = await Notification.requestPermission();
    setState(p);
    setBrowserNotify(p === "granted");
  }

  if (compact) {
    if (state !== "default" || dismissed || browserNotify) return null;
    return (
      <div className="flex items-start gap-3 border-t border-border bg-primary/[0.05] px-4 py-3">
        <BellRing className="mt-0.5 h-4 w-4 shrink-0 text-primary" />
        <div className="min-w-0 flex-1">
          <p className="text-[13px] font-medium">Get an alert when someone replies</p>
          <p className="text-xs text-muted-foreground">Even when Scholarly is in another tab. You can turn it off any time.</p>
          <Button size="sm" className="mt-2 h-8" onClick={() => void enable()}>
            Turn on alerts
          </Button>
        </div>
        <button
          type="button"
          aria-label="Not now"
          onClick={() => {
            setDismissed(true);
            try {
              localStorage.setItem(DISMISS_KEY, "1");
            } catch {
              /* ignore */
            }
          }}
          className="rounded-md p-1 text-muted-foreground hover:bg-secondary"
        >
          <X className="h-3.5 w-3.5" />
        </button>
      </div>
    );
  }

  return (
    <div className="flex items-start justify-between gap-4">
      <div>
        <p className="text-sm font-medium">Browser alerts</p>
        <p className="text-xs text-muted-foreground">
          {state === "unsupported"
            ? "This browser does not support notifications."
            : state === "denied"
              ? "Notifications are blocked for this site in your browser settings."
              : "A pop-up on this device when someone replies, mentions or messages you while Scholarly is in the background."}
        </p>
      </div>
      <Switch
        checked={browserNotify && state === "granted"}
        disabled={state === "unsupported" || state === "denied"}
        onCheckedChange={(on) => {
          if (on && state !== "granted") void enable();
          else setBrowserNotify(on);
        }}
        aria-label="Browser alerts"
      />
    </div>
  );
}
