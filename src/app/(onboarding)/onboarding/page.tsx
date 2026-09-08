import type { Metadata } from "next";
import Link from "next/link";
import { redirect } from "next/navigation";

import { SignupForm } from "@/components/auth/signup-form";
import { auth } from "@/lib/auth";

export const metadata: Metadata = {
  title: "Create your account",
  description: "Start practising in two fields — a username and a password.",
};

/**
 * Signup. A username and a password, and nothing else.
 *
 * This route used to render the onboarding wizard, which asked for an exam
 * track, a target score, a grade level, a test month, strengths, weaknesses, a
 * daily goal and an email before it would create the account. None of that is
 * deleted -- `OnboardingWizard`, `onboardingProfileSchema` and
 * `registerWithOnboarding` are all still in the tree and every profile column
 * still exists on User -- it is simply no longer in the way. Those questions
 * can be asked once someone is inside and written to the same columns.
 */
export default async function OnboardingPage({
  searchParams,
}: {
  searchParams: { ref?: string };
}) {
  // Someone already signed in has no account to create — send them to work.
  const session = await auth();
  if (session?.user) redirect("/dashboard");

  // The referral code rides in on ?ref= and is handed to the form so it
  // reaches account creation. It is never trusted here — attribution
  // validates it server-side and ignores an unknown, malformed or
  // self-referring code rather than failing the signup.
  return (
    <main className="flex min-h-screen items-center justify-center px-4 py-12">
      <div className="w-full max-w-sm space-y-6">
        <div className="space-y-2 text-center">
          <Link href="/" className="text-lg font-semibold tracking-tight">
            Scholarly
          </Link>
          <h1 className="text-2xl font-semibold tracking-tight">Create your account</h1>
          <p className="text-sm text-muted-foreground">
            Pick a username and a password. That is all we need.
          </p>
        </div>
        <SignupForm referralCode={searchParams.ref ?? null} />
      </div>
    </main>
  );
}
