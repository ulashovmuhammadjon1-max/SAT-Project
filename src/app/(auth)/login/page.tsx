import { Suspense } from "react";

import { LoginForm } from "@/components/shared/login-form";

export const metadata = {
  title: "Sign in",
  description: "Sign in to Scholarly to continue your SAT and IELTS preparation.",
};

export default function LoginPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-center font-display text-2xl font-semibold tracking-tight sm:text-[28px]">
        Sign in to Scholarly
      </h1>

      {/* useSearchParams (callbackUrl) needs a Suspense boundary. */}
      <Suspense fallback={<LoginCardFallback />}>
        <LoginForm />
      </Suspense>
    </div>
  );
}

/** A quiet placeholder the same shape as the card, so first paint doesn't jump. */
function LoginCardFallback() {
  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-soft sm:p-8">
      <div className="h-4 w-16 rounded bg-muted" />
      <div className="mt-2 h-11 w-full rounded-lg bg-muted" />
      <div className="mt-4 h-11 w-full rounded-lg bg-muted" />
      <div className="my-6 h-px w-full bg-border" />
      <div className="space-y-3">
        <div className="h-11 w-full rounded-lg bg-muted" />
        <div className="h-11 w-full rounded-lg bg-muted" />
        <div className="h-11 w-full rounded-lg bg-muted" />
      </div>
    </div>
  );
}
