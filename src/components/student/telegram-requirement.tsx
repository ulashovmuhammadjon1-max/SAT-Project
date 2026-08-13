"use client";

import { useEffect, useRef, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { CheckCircle2, Loader2, RefreshCw, XCircle } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { linkTelegram, recheckMyTelegram } from "@/server/actions/student/telegram";
import { cn } from "@/lib/utils";

export interface TelegramState {
  linked: boolean;
  isMember: boolean;
  username: string | null;
}

/**
 * The verified Telegram requirement.
 *
 * Replaces the honour-system checkbox with Telegram's own Login Widget. The
 * widget is a script tag that injects an iframe and calls a global callback, so
 * it cannot be a plain React component — the callback is installed on `window`
 * before the script loads and removed on unmount.
 *
 * Three states the student can be in, and each needs a different next step:
 *   - not linked      → sign in with Telegram
 *   - linked, not in  → join the channel, then Re-check
 *   - linked, in      → done, nothing to do
 *
 * The Re-check button exists because joining happens in a different app. There
 * is no event telling us it happened, so the student comes back and asks.
 */
export function TelegramRequirement({
  botUsername,
  channelHandle,
  channelHref,
  label,
  state,
}: {
  botUsername: string;
  channelHandle: string;
  channelHref: string;
  label: string;
  state: TelegramState;
}) {
  const router = useRouter();
  const mountRef = useRef<HTMLDivElement>(null);
  const [busy, setBusy] = useState(false);
  const [, startTransition] = useTransition();

  useEffect(() => {
    if (state.linked || !mountRef.current) return;
    const el = mountRef.current;

    // Telegram calls this by name from inside its iframe.
    (window as unknown as Record<string, unknown>).onTelegramAuth = (payload: Record<string, unknown>) => {
      setBusy(true);
      startTransition(async () => {
        const res = await linkTelegram({
          id: String(payload.id),
          first_name: payload.first_name as string | undefined,
          last_name: payload.last_name as string | undefined,
          username: payload.username as string | undefined,
          photo_url: payload.photo_url as string | undefined,
          auth_date: String(payload.auth_date),
          hash: String(payload.hash),
        });
        setBusy(false);
        if (!res.ok) {
          toast.error(res.error ?? "Couldn't connect Telegram.");
          return;
        }
        toast.success(
          res.isMember
            ? "Telegram connected — you're in the channel."
            : "Telegram connected. Now join the channel and press Re-check.",
        );
        router.refresh();
      });
    };

    const script = document.createElement("script");
    script.src = "https://telegram.org/js/telegram-widget.js?22";
    script.async = true;
    script.setAttribute("data-telegram-login", botUsername);
    script.setAttribute("data-size", "medium");
    script.setAttribute("data-userpic", "false");
    script.setAttribute("data-request-access", "write");
    script.setAttribute("data-onauth", "onTelegramAuth(user)");
    el.appendChild(script);

    return () => {
      el.innerHTML = "";
      delete (window as unknown as Record<string, unknown>).onTelegramAuth;
    };
  }, [botUsername, state.linked, router]);

  function recheck() {
    setBusy(true);
    startTransition(async () => {
      const res = await recheckMyTelegram();
      setBusy(false);
      if (!res.ok) {
        toast.error(res.error ?? "Couldn't check just now.");
        return;
      }
      toast[res.isMember ? "success" : "error"](
        res.isMember ? "Confirmed — you're in the channel." : "Still not in the channel.",
      );
      router.refresh();
    });
  }

  const done = state.linked && state.isMember;

  return (
    <div
      className={cn(
        "rounded-lg border p-3",
        done ? "border-primary/50 bg-primary/5" : "border-border",
      )}
    >
      <div className="flex items-start gap-3">
        <span className="mt-0.5 shrink-0">
          {done ? (
            <CheckCircle2 className="h-4 w-4 text-emerald-500" />
          ) : (
            <XCircle className="h-4 w-4 text-muted-foreground" />
          )}
        </span>

        <div className="min-w-0 flex-1 text-sm">
          <p>
            <span className="font-medium">{label}</span>{" "}
            <a
              href={channelHref}
              target="_blank"
              rel="noopener noreferrer"
              className="text-primary underline-offset-4 hover:underline"
            >
              {channelHandle}
            </a>
          </p>

          {done ? (
            <p className="mt-1 text-xs text-muted-foreground">
              Verified{state.username ? ` as @${state.username}` : ""} — checked with Telegram, not
              self-reported.
            </p>
          ) : state.linked ? (
            <div className="mt-2 space-y-2">
              <p className="text-xs text-muted-foreground">
                Connected{state.username ? ` as @${state.username}` : ""}, but you are not in the
                channel yet. Join it, then press Re-check.
              </p>
              <div className="flex flex-wrap gap-2">
                <Button size="sm" variant="outline" asChild>
                  <a href={channelHref} target="_blank" rel="noopener noreferrer">
                    Open the channel
                  </a>
                </Button>
                <Button size="sm" onClick={recheck} disabled={busy}>
                  {busy ? (
                    <Loader2 className="h-3.5 w-3.5 animate-spin" />
                  ) : (
                    <RefreshCw className="h-3.5 w-3.5" />
                  )}
                  Re-check
                </Button>
              </div>
            </div>
          ) : (
            <div className="mt-2 space-y-2">
              <p className="text-xs text-muted-foreground">
                Sign in with Telegram so we can confirm your membership. We only read your
                username and whether you are in the channel.
              </p>
              <div ref={mountRef} className={cn(busy && "pointer-events-none opacity-60")} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
