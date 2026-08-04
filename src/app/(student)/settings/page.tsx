import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { StudyPlanForm } from "@/components/student/study-plan-form";
import { readProfile } from "@/lib/onboarding/profile";
import { requireUser } from "@/lib/session";
import { initials } from "@/lib/utils";
import { asSection, asWeakArea, EMPTY_PROFILE, type OnboardingProfile } from "@/lib/validations/onboarding";

export const metadata = { title: "Settings" };
export const dynamic = "force-dynamic";

export default async function StudentSettingsPage() {
  const user = await requireUser();

  const record = await readProfile(user.id);

  const initial: OnboardingProfile = record
    ? {
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
    </div>
  );
}
