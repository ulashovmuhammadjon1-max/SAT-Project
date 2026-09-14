"use client";

import Link from "next/link";
import { useEffect, useRef, useState, useTransition } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { signIn } from "next-auth/react";
import { ArrowLeft, Loader2 } from "lucide-react";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { GoogleIcon, MicrosoftIcon, AppleIcon } from "@/components/shared/brand-icons";

type Step = "email" | "password";

/**
 * Sign-in card, modelled on a clean, minimal reference: one identifier field,
 * a primary "Continue with email", an OR divider, and three social options.
 *
 * The reference is passwordless; this product is not — it authenticates with a
 * password. Rather than crowd the first screen, the password is revealed only
 * after "Continue with email", so the opening view matches the reference
 * exactly (one field, one button, the social row) while the real credential
 * flow still works. The field is labelled "Email" per the design but accepts a
 * username too — the bulk-provisioned accounts have no address — so the input
 * stays `type="text"` and never blocks a username at the browser layer.
 *
 * Social sign-in is presented but not yet wired to a provider (none is
 * configured server-side). Clicking one explains that and points back to
 * email, instead of dropping the user on an OAuth error page. When a provider
 * is added to `auth.ts`, swap the handler for `signIn("<provider>")`.
 */
export function LoginForm() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const [step, setStep] = useState<Step>("email");
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [socialNotice, setSocialNotice] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  // Move focus to the field that just appeared, so the keyboard flow never
  // stalls between steps.
  useEffect(() => {
    if (step === "password") passwordRef.current?.focus();
    else emailRef.current?.focus();
  }, [step]);

  function toPasswordStep() {
    setError(null);
    setSocialNotice(null);
    if (!identifier.trim()) {
      setError("Enter your email to continue.");
      emailRef.current?.focus();
      return;
    }
    setStep("password");
  }

  function toEmailStep() {
    setError(null);
    setPassword("");
    setStep("email");
  }

  function submitPassword() {
    setError(null);
    startTransition(async () => {
      const result = await signIn("credentials", {
        identifier: identifier.trim(),
        password,
        redirect: false,
      });

      if (result?.error) {
        setError("That email or password doesn't look right.");
        passwordRef.current?.focus();
        return;
      }

      const callbackUrl = searchParams.get("callbackUrl") ?? "/dashboard";
      router.push(callbackUrl);
      router.refresh();
    });
  }

  function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (step === "email") toPasswordStep();
    else submitPassword();
  }

  function onSocial(provider: string) {
    setError(null);
    // No OAuth provider is configured yet — see the note above.
    setSocialNotice(`${provider} sign-in is coming soon. Continue with your email for now.`);
  }

  const busy = isPending;

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-soft sm:p-8">
      <form onSubmit={onSubmit} className="space-y-4" noValidate>
        {step === "email" ? (
          <div className="space-y-2">
            <Label htmlFor="identifier">Email</Label>
            <Input
              ref={emailRef}
              id="identifier"
              name="identifier"
              type="text"
              inputMode="email"
              autoComplete="username"
              autoCapitalize="none"
              autoCorrect="off"
              spellCheck={false}
              placeholder="Your email address"
              value={identifier}
              onChange={(e) => setIdentifier(e.target.value)}
              className="h-11"
              aria-invalid={Boolean(error) || undefined}
              aria-describedby={error ? "auth-error" : undefined}
              autoFocus
            />
          </div>
        ) : (
          <div className="space-y-3">
            {/* The identifier just entered, with a way back to change it. */}
            <button
              type="button"
              onClick={toEmailStep}
              className="group inline-flex max-w-full items-center gap-1.5 text-sm text-muted-foreground transition-colors hover:text-foreground"
            >
              <ArrowLeft className="h-3.5 w-3.5 shrink-0 transition-transform group-hover:-translate-x-0.5" />
              <span className="truncate font-medium text-foreground">{identifier.trim()}</span>
              <span className="shrink-0 text-xs">· change</span>
            </button>

            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label htmlFor="password">Password</Label>
                <Link
                  href="/forgot-password"
                  className="text-xs font-medium text-primary underline-offset-4 hover:underline"
                >
                  Forgot password?
                </Link>
              </div>
              <Input
                ref={passwordRef}
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                placeholder="Your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="h-11"
                aria-invalid={Boolean(error) || undefined}
                aria-describedby={error ? "auth-error" : undefined}
                autoFocus
              />
            </div>
          </div>
        )}

        {error && (
          <p
            id="auth-error"
            role="alert"
            aria-live="assertive"
            className="rounded-lg bg-destructive/10 px-3 py-2 text-sm text-destructive"
          >
            {error}
          </p>
        )}

        <Button
          type="submit"
          disabled={busy}
          aria-busy={busy}
          className="h-11 w-full bg-foreground text-background shadow-sm hover:bg-foreground/90"
        >
          {busy && <Loader2 className="h-4 w-4 animate-spin" />}
          {step === "email" ? "Continue with email" : "Sign in"}
        </Button>
      </form>

      {step === "email" && (
        <>
          <div className="my-6 flex items-center gap-3" aria-hidden="true">
            <span className="h-px flex-1 bg-border" />
            <span className="text-xs font-medium tracking-wide text-muted-foreground">OR</span>
            <span className="h-px flex-1 bg-border" />
          </div>

          <div className="space-y-3">
            <SocialButton icon={<GoogleIcon />} label="Continue with Google" onClick={() => onSocial("Google")} disabled={busy} />
            <SocialButton icon={<MicrosoftIcon />} label="Continue with Microsoft" onClick={() => onSocial("Microsoft")} disabled={busy} />
            <SocialButton icon={<AppleIcon />} label="Continue with Apple" onClick={() => onSocial("Apple")} disabled={busy} />
          </div>

          {socialNotice && (
            <p role="status" aria-live="polite" className="mt-3 text-center text-xs text-muted-foreground">
              {socialNotice}
            </p>
          )}
        </>
      )}

      <p className="mt-6 text-center text-sm text-muted-foreground">
        Don&apos;t have an account?{" "}
        <Link
          href="/onboarding"
          className="font-medium text-primary underline-offset-4 hover:underline"
        >
          Create a free account
        </Link>
      </p>
    </div>
  );
}

function SocialButton({
  icon,
  label,
  onClick,
  disabled,
}: {
  icon: React.ReactNode;
  label: string;
  onClick: () => void;
  disabled?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={cn(
        "inline-flex h-11 w-full items-center justify-center gap-2.5 rounded-lg border border-input bg-background text-sm font-medium text-foreground shadow-sm transition-colors",
        "hover:bg-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
        "disabled:pointer-events-none disabled:opacity-50",
      )}
    >
      <span className="flex h-5 w-5 shrink-0 items-center justify-center">{icon}</span>
      {label}
    </button>
  );
}
