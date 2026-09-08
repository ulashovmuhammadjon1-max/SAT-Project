"use client";

import Link from "next/link";
import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { signIn } from "next-auth/react";
import { Loader2 } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { registerWithUsername } from "@/server/actions/auth/register";

/**
 * Sign up: a username, a password, and a button.
 *
 * There is deliberately nothing else on this screen. No email, no
 * verification, no confirm-password field, no questions about which exam or
 * what score. The questions still exist in the codebase and can be asked once
 * someone is inside; every one of them on this screen is a place a student can
 * stop.
 *
 * Consent is stated rather than clicked -- a checkbox is a field, and the
 * brief was that there be none. The line under the button is the disclosure,
 * and `registerWithUsername` records the acceptance and the terms version.
 */
export function SignupForm({ referralCode }: { referralCode: string | null }) {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [field, setField] = useState<"username" | "password" | null>(null);
  const [isPending, startTransition] = useTransition();

  function onSubmit(formData: FormData) {
    setError(null);
    setField(null);
    const username = String(formData.get("username") ?? "");
    const password = String(formData.get("password") ?? "");

    startTransition(async () => {
      const result = await registerWithUsername({ username, password, referralCode });
      if (result.error) {
        setError(result.error);
        setField(result.field ?? null);
        return;
      }

      // Sign the new account straight in. Making someone type the credentials
      // they just chose, on the next screen, is the kind of step this change
      // exists to remove.
      const signedIn = await signIn("credentials", {
        identifier: username,
        password,
        redirect: false,
      });
      if (signedIn?.error) {
        // The account exists; only the automatic sign-in failed. Send them to
        // the sign-in page rather than implying the signup did not work.
        router.push("/login");
        return;
      }
      router.push("/dashboard");
      router.refresh();
    });
  }

  return (
    <form action={onSubmit} className="space-y-4">
      <div className="space-y-2">
        <Label htmlFor="username">Username</Label>
        <Input
          id="username"
          name="username"
          type="text"
          placeholder="pick a username"
          required
          autoFocus
          autoComplete="username"
          autoCapitalize="none"
          spellCheck={false}
          aria-invalid={field === "username"}
        />
        <p className="text-xs text-muted-foreground">
          3 to 24 characters. Letters, numbers, dots and underscores.
        </p>
      </div>

      <div className="space-y-2">
        <Label htmlFor="password">Password</Label>
        <Input
          id="password"
          name="password"
          type="password"
          required
          autoComplete="new-password"
          aria-invalid={field === "password"}
        />
        <p className="text-xs text-muted-foreground">
          At least 4 characters. Four numbers is fine.
        </p>
      </div>

      {error && (
        <p className="rounded-md bg-destructive/10 px-3 py-2 text-sm text-destructive">{error}</p>
      )}

      <Button type="submit" className="w-full" disabled={isPending}>
        {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
        Create account
      </Button>

      <p className="text-center text-xs text-muted-foreground">
        By creating an account you agree to our{" "}
        <Link href="/terms" className="underline underline-offset-4">Terms</Link> and{" "}
        <Link href="/privacy" className="underline underline-offset-4">Privacy Policy</Link>.
      </p>

      <p className="text-center text-sm text-muted-foreground">
        Already have an account?{" "}
        <Link href="/login" className="font-medium text-primary underline-offset-4 hover:underline">
          Sign in
        </Link>
      </p>
    </form>
  );
}
