import Link from "next/link";

import { ResetPasswordForm } from "@/components/auth/reset-password-form";

export const metadata = { title: "Set a new password" };

export default function ResetPasswordPage({
  searchParams,
}: {
  searchParams: { token?: string; email?: string };
}) {
  const { token, email } = searchParams;

  // A link that arrives without both halves cannot be completed, so say so
  // here rather than letting someone fill in a form that will always fail.
  if (!token || !email) {
    return (
      <div className="mx-auto w-full max-w-sm space-y-4 text-center">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Link incomplete</h1>
        <p className="text-sm text-muted-foreground">
          That reset link is missing part of its address. Email clients sometimes cut long links in
          half — try copying the whole thing, or request a new one.
        </p>
        <Link
          href="/forgot-password"
          className="inline-block font-medium text-primary underline-offset-4 hover:underline"
        >
          Send a new link
        </Link>
      </div>
    );
  }

  return (
    <div className="mx-auto w-full max-w-sm space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Set a new password</h1>
        <p className="mt-1 text-sm text-muted-foreground">for {email}</p>
      </div>
      <ResetPasswordForm token={token} email={email} />
    </div>
  );
}
