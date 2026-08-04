import type { Metadata } from "next";
import { redirect } from "next/navigation";

import { OnboardingWizard } from "@/components/onboarding/onboarding-wizard";
import { auth } from "@/lib/auth";

export const metadata: Metadata = {
  title: "Get started",
  description: "Build your personalised Digital SAT study plan in about a minute.",
};

export default async function OnboardingPage() {
  // Someone already signed in has no account to create — send them to work.
  const session = await auth();
  if (session?.user) redirect("/dashboard");

  return <OnboardingWizard />;
}
