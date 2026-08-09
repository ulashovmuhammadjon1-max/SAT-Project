"use client";

import { useState, useTransition } from "react";
import { MailCheck } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { requestPasswordReset } from "@/server/actions/auth/password-reset";

export function ForgotPasswordForm() {
  const [pending, startTransition] = useTransition();
  const [sent, setSent] = useState(false);
  const [email, setEmail] = useState("");
  const [error, setError] = useState<string | null>(null);

  // The success state deliberately does not confirm the account exists — the
  // server behaves identically either way, and saying "we sent it" only when
  // it did would turn this page into an account-enumeration tool.
  if (sent) {
    return (
      <div className="rounded-lg border border-success/40 bg-success/5 p-5 text-center">
        <MailCheck className="mx-auto mb-2 h-8 w-8 text-success" />
        <p className="font-medium">Check your inbox</p>
        <p className="mt-1 text-sm text-muted-foreground">
          If an account exists for {email}, a reset link is on its way. It expires in one hour.
        </p>
      </div>
    );
  }

  return (
    <form
      className="space-y-4"
      onSubmit={(e) => {
        e.preventDefault();
        setError(null);
        startTransition(async () => {
          const res = await requestPasswordReset(email);
          if (res.ok) setSent(true);
          else setError(res.error);
        });
      }}
    >
      <div className="space-y-1.5">
        <Label htmlFor="email">Email</Label>
        <Input
          id="email"
          type="email"
          autoComplete="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      {error && <p className="text-sm text-destructive">{error}</p>}
      <Button type="submit" className="w-full" disabled={pending}>
        {pending ? "Sending…" : "Send reset link"}
      </Button>
    </form>
  );
}
