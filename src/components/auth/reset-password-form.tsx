"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { CheckCircle2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { resetPassword } from "@/server/actions/auth/password-reset";

export function ResetPasswordForm({ token, email }: { token: string; email: string }) {
  const router = useRouter();
  const [pending, startTransition] = useTransition();
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(false);

  if (done) {
    return (
      <div className="rounded-lg border border-success/40 bg-success/5 p-5 text-center">
        <CheckCircle2 className="mx-auto mb-2 h-8 w-8 text-success" />
        <p className="font-medium">Password updated</p>
        <p className="mt-1 text-sm text-muted-foreground">
          You&apos;ve been signed out everywhere else for safety.
        </p>
        <Button asChild className="mt-4 w-full">
          <Link href="/login">Sign in</Link>
        </Button>
      </div>
    );
  }

  return (
    <form
      className="space-y-4"
      onSubmit={(e) => {
        e.preventDefault();
        setError(null);
        // Checked here as well as by the browser so the mismatch message is
        // ours rather than a native tooltip.
        if (password !== confirm) return setError("Those passwords don't match.");
        startTransition(async () => {
          const res = await resetPassword({ token, email, password });
          if (res.ok) {
            setDone(true);
            router.refresh();
          } else {
            setError(res.error);
          }
        });
      }}
    >
      <div className="space-y-1.5">
        <Label htmlFor="password">New password</Label>
        <Input
          id="password"
          type="password"
          autoComplete="new-password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <p className="text-xs text-muted-foreground">
          At least 8 characters, with one uppercase letter and one number.
        </p>
      </div>
      <div className="space-y-1.5">
        <Label htmlFor="confirm">Confirm password</Label>
        <Input
          id="confirm"
          type="password"
          autoComplete="new-password"
          required
          value={confirm}
          onChange={(e) => setConfirm(e.target.value)}
        />
      </div>
      {error && <p className="text-sm text-destructive">{error}</p>}
      <Button type="submit" className="w-full" disabled={pending}>
        {pending ? "Updating…" : "Update password"}
      </Button>
    </form>
  );
}
