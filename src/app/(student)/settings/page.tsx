import Link from "next/link";
import { GraduationCap, Mail } from "lucide-react";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { StudyPlanForm } from "@/components/student/study-plan-form";
import { ThemeToggle } from "@/components/shared/theme-toggle";
import { readProfile } from "@/lib/onboarding/profile";
import { requireUser } from "@/lib/session";
import { isTeacher } from "@/server/actions/teacher/classes";
import { initials } from "@/lib/utils";
import { asSection, asWeakArea, EMPTY_PROFILE, type OnboardingProfile } from "@/lib/validations/onboarding";

export const metadata = { title: "Settings" };
export const dynamic = "force-dynamic";

const SUPPORT_EMAIL = "ulashovmuhammadjo1@gmail.com";

export default async function StudentSettingsPage() {
  const user = await requireUser();

  const [record, teaching] = await Promise.all([
    readProfile(user.id),
    isTeacher(user.id, user.email ?? null),
  ]);

  // Settings edits the SAT answers only; the track and the IELTS answers are
  // set during onboarding and changed from the IELTS side, so they are carried
  // through as defaults rather than surfaced here.
  const initial: OnboardingProfile = record
    ? {
        ...EMPTY_PROFILE,
        goal: record.onboardingGoal,
        currentScore: record.currentScore,
        targetScore: record.targetScore,
        dreamUniversities: record.dreamUniversities,
        countryCode: record.countryCode,
        gradeLevel: record.gradeLevel,
        // Stored with day precision; the form only edits the month.
        satMonth: record.satDate
          ? `${record.satDate.getUTCFullYear()}-${String(record.satDate.getUTCMonth() + 1).padStart(2, "0")}`
          : null,
        strongestSection: asSection(record.strongestSection),
        weakestArea: asWeakArea(record.weakestArea),
        studyMinutesPerDay: record.studyMinutesPerDay,
        dailyGoalType: record.dailyGoalType,
        dailyGoalValue: record.dailyGoalValue,
      }
    : EMPTY_PROFILE;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Settings</h1>
        <p className="text-sm text-muted-foreground">Your account and study plan.</p>
      </div>

      <Card className="max-w-lg">
        <CardHeader>
          <CardTitle className="text-base">Profile</CardTitle>
        </CardHeader>
        <CardContent className="flex items-center gap-4">
          <Avatar className="h-16 w-16">
            <AvatarImage src={user.image ?? undefined} />
            <AvatarFallback className="text-lg">{initials(user.name)}</AvatarFallback>
          </Avatar>
          <div>
            <p className="font-medium">{user.name}</p>
            <p className="text-sm text-muted-foreground">{user.email}</p>
          </div>
        </CardContent>
      </Card>

      <Card className="max-w-lg">
        <CardHeader>
          <CardTitle className="text-base">Appearance</CardTitle>
          <CardDescription>
            Scholarly is dark by default. Pick whatever is easiest on your eyes — the choice is
            remembered on this device. The exam interface always keeps its own fixed appearance so
            practice tests look like the real thing.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <ThemeToggle />
        </CardContent>
      </Card>

      <Card className="max-w-2xl">
        <CardHeader>
          <CardTitle className="text-base">Study plan</CardTitle>
          <CardDescription>
            These answers drive your dashboard — your target, countdown, daily goal, and what we recommend next.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <StudyPlanForm initial={initial} />
        </CardContent>
      </Card>

      {teaching && (
        <Card className="max-w-lg border-success/40">
          <CardHeader>
            <CardTitle className="text-base">Teaching</CardTitle>
            <CardDescription>
              A class is linked to this account. Track your students&apos; practice, tests and
              scores from your Teacher Panel.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Link
              href="/teach"
              className="inline-flex items-center gap-2 text-sm font-medium text-primary underline-offset-4 hover:underline"
            >
              <GraduationCap className="h-4 w-4" />
              Open Teacher Panel
            </Link>
          </CardContent>
        </Card>
      )}

      <Card className="max-w-lg">
        <CardHeader>
          <CardTitle className="text-base">Contact support</CardTitle>
          <CardDescription>
            Stuck on something, found a bug, or have feedback? Email us directly and we&apos;ll get
            back to you.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <a
            href={`mailto:${SUPPORT_EMAIL}`}
            className="inline-flex items-center gap-2 text-sm font-medium text-primary underline-offset-4 hover:underline"
          >
            <Mail className="h-4 w-4" />
            {SUPPORT_EMAIL}
          </a>
        </CardContent>
      </Card>
    </div>
  );
}
