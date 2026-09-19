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
import type { EnabledOAuth } from "@/lib/auth-providers";

type Step = "email" | "password";

/** Auth.js provider ids, paired with their button label and icon. */
const OAUTH = [
  { key: "google", id: "google", label: "Continue with Google", Icon: GoogleIcon },
  { key: "microsoft", id: "microsoft-entra-id", label: "Continue with Microsoft", Icon: MicrosoftIcon },
  { key: "apple", id: "apple", label: "Continue with Apple", Icon: AppleIcon },
] as const;

/** Map an Auth.js `?error=` code to something a person can act on. */
function friendlyAuthError(code: string | null): string | null {
  if (!code) return null;
  switch (code) {
    case "OAuthAccountNotLinked":
      return "That email is already registered a different way. Sign in with your email and password.";
    case "AccessDenied":
      return "That sign-in was cancelled or not permitted.";
    case "Configuration":
      return "That sign-in option isn't set up correctly. Try email for now.";
    default:
      return "Something went wrong signing in. Please try again.";
  }
}

/**
 * Sign-in card, modelled on a clean, minimal reference: one identifier field,
 * a primary "Continue with email", an OR divider, and any configured social
 * providers.
 *
 * The reference is passwordless; this product is not — it authenticates with a
 * password, revealed only after "Continue with email" so the opening view stays
 * minimal. The field is labelled "Email" but accepts a username too (the
 * bulk-provisioned accounts have no address), so it stays `type="text"`.
 *
 * Social buttons render ONLY for providers configured in this deployment (see
 * `enabledOAuth`). A button that is shown is a button that works; unconfigured
 * providers are simply absent, so nothing dead is ever presented.
 */
export function LoginForm({ providers }: { providers: EnabledOAuth }) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const [step, setStep] = useState<Step>("email");
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(() =>
    friendlyAuthError(searchParams.get("error")),
  );
  const [oauthPending, setOauthPending] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  const callbackUrl = searchParams.get("callbackUrl") ?? "/dashboard";
  const socials = OAUTH.filter((o) => providers[o.key]);

  useEffect(() => {
    if (step === "password") passwordRef.current?.focus();
    else emailRef.current?.focus();
  }, [step]);

  function toPasswordStep() {
    setError(null);
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
      router.push(callbackUrl);
      router.refresh();
    });
  }

  function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (step === "email") toPasswordStep();
    else submitPassword();
  }

  function onOAuth(id: string) {
    setError(null);
    setOauthPending(id);
    // Full-page redirect to the provider and back to callbackUrl on success.
    void signIn(id, { callbackUrl });
  }

  const busy = isPending || oauthPending !== null;

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
          {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
          {step === "email" ? "Continue with email" : "Sign in"}
        </Button>
      </form>

      {step === "email" && socials.length > 0 && (
        <>
          <div className="my-6 flex items-center gap-3" aria-hidden="true">
            <span className="h-px flex-1 bg-border" />
            <span className="text-xs font-medium tracking-wide text-muted-foreground">OR</span>
            <span className="h-px flex-1 bg-border" />
          </div>

          <div className="space-y-3">
            {socials.map(({ id, label, Icon }) => (
              <SocialButton
                key={id}
                icon={<Icon />}
                label={label}
                onClick={() => onOAuth(id)}
                disabled={busy}
                loading={oauthPending === id}
              />
            ))}
          </div>
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
  loading,
}: {
  icon: React.ReactNode;
  label: string;
  onClick: () => void;
  disabled?: boolean;
  loading?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      aria-busy={loading}
      className={cn(
        "inline-flex h-11 w-full items-center justify-center gap-2.5 rounded-lg border border-input bg-background text-sm font-medium text-foreground shadow-sm transition-colors",
        "hover:bg-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
        "disabled:pointer-events-none disabled:opacity-50",
      )}
    >
      <span className="flex h-5 w-5 shrink-0 items-center justify-center">
        {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : icon}
      </span>
      {label}
    </button>
  );
}
