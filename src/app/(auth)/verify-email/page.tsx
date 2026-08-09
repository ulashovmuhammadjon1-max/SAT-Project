import Link from "next/link";
import { CheckCircle2, MailCheck } from "lucide-react";

import { ResendVerificationButton } from "@/components/auth/resend-verification-button";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";
import { verifyEmail } from "@/server/actions/auth/email-verification";

export const metadata = { title: "Confirm your email" };
export const dynamic = "force-dynamic";

/**
 * Two pages in one, because a student arrives here in two different states.
 *
 * With `?token=` they have clicked the link in the email and this consumes it.
 * Without, they have just signed up (or been bounced out of the app) and are
 * waiting — so this is the "check your inbox" screen, with a way to send it
 * again.
 */
export default async function VerifyEmailPage({
  searchParams,
}: {
  searchParams: { token?: string; email?: string };
}) {
  const { token, email } = searchParams;

  if (token && email) {
    const result = await verifyEmail({ token, email });

    if (result.ok) {
      return (
        <div className="mx-auto w-full max-w-sm space-y-5 text-center">
          <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-emerald-500/10 text-emerald-500">
            <CheckCircle2 className="h-6 w-6" />
          </span>
          <div className="space-y-1.5">
            <h1 className="font-display text-2xl font-semibold tracking-tight">
              {result.alreadyVerified ? "Already confirmed" : "Email confirmed"}
            </h1>
            <p className="text-sm text-muted-foreground">
              {result.alreadyVerified
                ? "This address was confirmed already. You're all set."
                : "Thanks — your account is ready. Everything on SATForge is open to you now."}
            </p>
          </div>
          <Link
            href="/dashboard"
            className="inline-flex h-10 items-center justify-center rounded-lg bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
          >
            Go to my dashboard
          </Link>
        </div>
      );
    }

    return (
      <div className="mx-auto w-full max-w-sm space-y-5 text-center">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Link didn&apos;t work</h1>
        <p className="text-sm text-muted-foreground">{result.error}</p>
        <ResendVerificationButton />
        <p className="text-sm text-muted-foreground">
          Not signed in?{" "}
          <Link href="/login" className="font-medium text-primary underline-offset-4 hover:underline">
            Sign in
          </Link>{" "}
          first, and we&apos;ll send a fresh link.
        </p>
      </div>
    );
  }

  // Waiting state.
  const sessionUser = await getCurrentUser();
  const address = sessionUser?.email
    ? (
        await prisma.user.findUnique({
          where: { id: sessionUser.id },
          select: { email: true, emailVerified: true },
        })
      )
    : null;

  if (address?.emailVerified) {
    return (
      <div className="mx-auto w-full max-w-sm space-y-5 text-center">
        <h1 className="font-display text-2xl font-semibold tracking-tight">You&apos;re confirmed</h1>
        <p className="text-sm text-muted-foreground">Nothing left to do here.</p>
        <Link
          href="/dashboard"
          className="inline-flex h-10 items-center justify-center rounded-lg bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
        >
          Go to my dashboard
        </Link>
      </div>
    );
  }

  return (
    <div className="mx-auto w-full max-w-sm space-y-5 text-center">
      <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-primary/10 text-primary">
        <MailCheck className="h-6 w-6" />
      </span>
      <div className="space-y-1.5">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Check your inbox</h1>
        <p className="text-sm text-muted-foreground">
          {address?.email ? (
            <>
              We sent a confirmation link to{" "}
              <span className="font-medium text-foreground">{address.email}</span>. Click it and
              your account is ready.
            </>
          ) : (
            <>
              We sent you a confirmation link. Click it and your account is ready. Sign in first if
              you want us to send another.
            </>
          )}
        </p>
      </div>

      {sessionUser ? <ResendVerificationButton /> : null}

      <p className="text-[13px] leading-relaxed text-muted-foreground">
        It usually arrives within a minute. If it hasn&apos;t, check your spam folder — and make
        sure the address above is spelled correctly.
      </p>

      <p className="text-sm text-muted-foreground">
        <Link href="/login" className="font-medium text-primary underline-offset-4 hover:underline">
          Back to sign in
        </Link>
      </p>
    </div>
  );
}
