"use client";

import { useState, useTransition } from "react";
import { Loader2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { resendVerificationEmail } from "@/server/actions/auth/email-verification";

/**
 * "Send it again."
 *
 * The action is session-scoped, so this can only ever target the signed-in
 * account's own address — there is no address input to point somewhere else.
 * The cooldown lives on the server; this just reports what it says.
 */
export function ResendVerificationButton() {
  const [isPending, startTransition] = useTransition();
  const [message, setMessage] = useState<{ ok: boolean; text: string } | null>(null);

  return (
    <div className="space-y-2">
      <Button
        variant="outline"
        disabled={isPending}
        onClick={() =>
          startTransition(async () => {
            try {
              const result = await resendVerificationEmail();
              setMessage(
                result.ok
                  ? { ok: true, text: "Sent. It should arrive within a minute." }
                  : { ok: false, text: result.error }
              );
            } catch {
              setMessage({ ok: false, text: "Couldn't send it just now. Try again in a moment." });
            }
          })
        }
      >
        {isPending ? (
          <>
            <Loader2 className="h-4 w-4 animate-spin" /> Sending
          </>
        ) : (
          "Send the link again"
        )}
      </Button>
      {message && (
        <p
          role="status"
          className={message.ok ? "text-sm text-emerald-500" : "text-sm text-destructive"}
        >
          {message.text}
        </p>
      )}
    </div>
  );
}
