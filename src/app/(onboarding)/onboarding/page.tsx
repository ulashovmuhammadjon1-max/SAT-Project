import type { Metadata } from "next";
import { redirect } from "next/navigation";

import { OnboardingWizard } from "@/components/onboarding/onboarding-wizard";
import { auth } from "@/lib/auth";

export const metadata: Metadata = {
  title: "Get started",
  description: "Build your personalised study plan — SAT, IELTS, or both — in about a minute.",
};

export default async function OnboardingPage({
  searchParams,
}: {
  searchParams: { ref?: string };
}) {
  // Someone already signed in has no account to create — send them to work.
  const session = await auth();
  if (session?.user) redirect("/dashboard");

  // The referral code rides in on ?ref= and is handed to the wizard so it
  // survives the multi-step flow and reaches account creation. It is never
  // trusted here — attribution validates it server-side and ignores an
  // unknown, malformed or self-referring code rather than failing the signup.
  return <OnboardingWizard referralCode={searchParams.ref ?? null} />;
}
