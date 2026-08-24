import Link from "next/link";
import { Suspense } from "react";

import { LoginForm } from "@/components/shared/login-form";

export default function LoginPage() {
  return (
    <div className="space-y-6">
      <div className="space-y-1.5">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Welcome back</h1>
        <p className="text-sm text-muted-foreground">Sign in to continue where you left off.</p>
      </div>
      <Suspense>
        <LoginForm />
      </Suspense>
      <p className="text-center text-sm text-muted-foreground">
        Don&apos;t have an account?{" "}
        <Link href="/onboarding" className="font-medium text-primary hover:underline">
          Create one
        </Link>
      </p>
    </div>
  );
}
