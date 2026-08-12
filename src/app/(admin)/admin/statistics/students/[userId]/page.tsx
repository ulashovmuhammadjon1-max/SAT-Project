import Link from "next/link";
import { notFound } from "next/navigation";
import {
  ArrowLeft,
  BadgeCheck,
  BookOpen,
  CalendarDays,
  Coins,
  Flame,
  GraduationCap,
  Target,
  Users,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { ScoreProgressChart, StudyActivityChart } from "@/components/charts/student-progress-charts";
import { countryByCode } from "@/lib/data/countries";
import { getStudentProfile, type StudentProfile } from "@/lib/admin/student-profile";
import { cn } from "@/lib/utils";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: { userId: string } }) {
  const profile = await getStudentProfile(params.userId);
  return { title: profile ? `${profile.identity.name ?? profile.identity.email}` : "Student" };
}

/* ---------------------------------------------------------------- helpers */

/** SCREAMING_SNAKE enum → "Screaming snake", for display only. */
function humanise(value: string | null): string | null {
  if (!value) return null;
  const words = value.toLowerCase().replace(/_/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
}

/** Session types whose generic humanisation reads badly ("One on one sat"). */
const SESSION_TYPE_LABELS: Record<string, string> = {
  ONE_ON_ONE_SAT: "1-on-1 SAT",
  TEST_ANALYSIS: "Test analysis",
  FINANCIAL_LITERACY: "Financial literacy",
  LECTURE: "Lecture",
  WORKSHOP: "Workshop",
};

function formatDate(date: Date | null | undefined, withTime = false): string {
  if (!date) return "—";
  return new Date(date).toLocaleDateString(undefined, {
    day: "numeric",
    month: "short",
    year: "numeric",
    ...(withTime ? { hour: "2-digit", minute: "2-digit" } : {}),
  });
}

function daysSince(date: Date | null): number | null {
  if (!date) return null;
  return Math.floor((Date.now() - new Date(date).getTime()) / 86_400_000);
}

/* ------------------------------------------------------------------ page */

export default async function StudentProfilePage({ params }: { params: { userId: string } }) {
  const profile = await getStudentProfile(params.userId);
  if (!profile) notFound();

  const { identity, onboarding, totals } = profile;
  const country = countryByCode(onboarding.countryCode);
  const lastActive = daysSince(identity.lastActiveDate);

  return (
    <div className="space-y-6">
      <div>
        <Link
          href="/admin/statistics/students"
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> All students
        </Link>
      </div>

      {/* ---- identity ---------------------------------------------------- */}
      <Card>
        <CardContent className="flex flex-wrap items-start justify-between gap-4 p-6">
          <div className="min-w-0">
            <div className="flex flex-wrap items-center gap-2">
              <h1 className="font-display text-2xl font-semibold tracking-tight">
                {identity.name ?? "Unnamed student"}
              </h1>
              {identity.emailVerified ? (
                <Badge variant="success" className="gap-1">
                  <BadgeCheck className="h-3 w-3" /> Verified
                </Badge>
              ) : (
                <Badge variant="warning">Unverified email</Badge>
              )}
              {country && (
                <Badge variant="outline">
                  {country.flag} {country.name}
                </Badge>
              )}
            </div>
            <p className="mt-1 text-sm text-muted-foreground">{identity.email}</p>
            <p className="mt-2 text-xs text-muted-foreground">
              Joined {formatDate(identity.joinedAt)} ·{" "}
              {lastActive === null
                ? "never studied"
                : lastActive === 0
                  ? "studied today"
                  : `last studied ${lastActive}d ago`}
              {onboarding.onboardedAt
                ? ` · onboarded ${formatDate(onboarding.onboardedAt)}`
                : " · never completed onboarding"}
            </p>
          </div>

          <div className="flex flex-wrap gap-4 text-sm">
            <Mini icon={<Flame className="h-3.5 w-3.5" />} label="Streak">
              {identity.currentStreak}d
              <span className="text-muted-foreground"> · best {identity.longestStreak}d</span>
            </Mini>
            <Mini icon={<Coins className="h-3.5 w-3.5" />} label="Coins">
              {identity.coinBalance}
            </Mini>
            <Mini icon={<Users className="h-3.5 w-3.5" />} label="Referred">
              {profile.referrals.referredCount}
            </Mini>
          </div>
        </CardContent>
      </Card>

      {/* ---- headline numbers -------------------------------------------- */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Stat
          label="Best score"
          value={totals.bestScore ?? "—"}
          sub={
            // A test can be submitted without ever being scored — an attempt
            // abandoned mid-module still lands as SUBMITTED with a null total.
            // Saying "one test completed" beside a dash reads as a bug.
            totals.bestScore == null
              ? totals.testsCompleted
                ? `${totals.testsCompleted} submitted, none scored`
                : "no completed tests"
              : totals.scoredCount > 1
                ? `${totals.firstScore} → ${totals.latestScore} across ${totals.scoredCount} scored tests`
                : "one scored test"
          }
        />
        <Stat
          label="Target score"
          value={onboarding.targetScore ?? "—"}
          sub={
            onboarding.targetScore && totals.bestScore
              ? totals.bestScore >= onboarding.targetScore
                ? "target reached"
                : `${onboarding.targetScore - totals.bestScore} points to go`
              : onboarding.currentScore
                ? `self-reported start ${onboarding.currentScore}`
                : "not set during onboarding"
          }
        />
        <Stat
          label="Questions answered"
          value={totals.questionsAnswered}
          sub={`over ${totals.daysActive} active ${totals.daysActive === 1 ? "day" : "days"}`}
        />
        <Stat
          label="Question Bank accuracy"
          value={totals.qbAccuracyPct == null ? "—" : `${totals.qbAccuracyPct}%`}
          sub={totals.qbAnswered ? `${totals.qbAnswered} graded answers` : "no Question Bank answers yet"}
        />
      </div>

      {/* ---- score progression ------------------------------------------- */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">Score progression</CardTitle>
        </CardHeader>
        <CardContent>
          {profile.scoreTrend.length > 1 ? (
            <ScoreProgressChart data={profile.scoreTrend} />
          ) : (
            <Empty>
              {profile.scoreTrend.length === 1
                ? "Only one test scored so far — a trend needs at least two."
                : "No scored tests yet."}
            </Empty>
          )}
        </CardContent>
      </Card>

      <div className="grid gap-4 lg:grid-cols-2">
        {/* ---- onboarding profile ---------------------------------------- */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <GraduationCap className="h-4 w-4" /> Profile
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-0">
            {onboarding.onboardedAt == null && (
              <p className="mb-3 text-sm text-muted-foreground">
                This student never finished onboarding, so most of this is blank.
              </p>
            )}
            <dl className="divide-y text-sm">
              <Field label="Goal" value={humanise(onboarding.goal)} />
              <Field label="Grade" value={humanise(onboarding.gradeLevel)} />
              <Field label="Country" value={country ? `${country.flag} ${country.name}` : null} />
              <Field label="SAT date" value={onboarding.satDate ? formatDate(onboarding.satDate) : null} />
              <Field label="Starting score" value={onboarding.currentScore} />
              <Field label="Target score" value={onboarding.targetScore} />
              <Field label="Strongest" value={onboarding.strongestSection} />
              <Field label="Weakest" value={onboarding.weakestArea} />
              <Field
                label="Study time"
                value={onboarding.studyMinutesPerDay ? `${onboarding.studyMinutesPerDay} min/day` : null}
              />
              <Field
                label="Daily goal"
                value={
                  onboarding.dailyGoalValue
                    ? `${onboarding.dailyGoalValue} ${onboarding.dailyGoalType?.toLowerCase() ?? ""}`.trim()
                    : null
                }
              />
              <Field
                label="Dream schools"
                value={onboarding.dreamUniversities.length ? onboarding.dreamUniversities.join(", ") : null}
              />
              <Field
                label="Referred by"
                value={
                  profile.referrals.referredByName ?? profile.referrals.referredByEmail ?? null
                }
              />
              <Field
                label="Terms accepted"
                value={
                  identity.termsAcceptedAt
                    ? `${formatDate(identity.termsAcceptedAt)}${identity.termsVersion ? ` (${identity.termsVersion})` : ""}`
                    : null
                }
              />
            </dl>
          </CardContent>
        </Card>

        {/* ---- accuracy by domain ---------------------------------------- */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <Target className="h-4 w-4" /> Accuracy by domain
            </CardTitle>
          </CardHeader>
          <CardContent>
            {profile.domains.length ? (
              <div className="space-y-3">
                {profile.domains.map((d) => (
                  <div key={d.code}>
                    <div className="mb-1 flex items-baseline justify-between gap-2 text-sm">
                      <span className="truncate">
                        {d.name}
                        <span className="ml-1.5 text-xs text-muted-foreground">
                          {d.subject === "MATH" ? "Math" : "R&W"}
                        </span>
                      </span>
                      <span className="shrink-0 tabular-nums">
                        <span
                          className={cn(
                            "font-semibold",
                            d.accuracyPct >= 75 && "text-emerald-500",
                            d.accuracyPct < 40 && "text-amber-500"
                          )}
                        >
                          {d.accuracyPct}%
                        </span>
                        <span className="text-xs text-muted-foreground">
                          {" "}
                          {d.correct}/{d.attempted}
                        </span>
                      </span>
                    </div>
                    <Progress value={d.accuracyPct} className="h-1.5" />
                  </div>
                ))}
                <p className="pt-1 text-xs text-muted-foreground">
                  Pools test answers and Question Bank answers. Questions left ungraded in an
                  abandoned module are excluded rather than counted as wrong.
                </p>
              </div>
            ) : (
              <Empty>No graded answers yet.</Empty>
            )}
          </CardContent>
        </Card>
      </div>

      {/* ---- study activity ---------------------------------------------- */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-base">
            <CalendarDays className="h-4 w-4" /> Questions answered, last 60 days
          </CardTitle>
        </CardHeader>
        <CardContent>
          {profile.activity.some((p) => p.value > 0) ? (
            <StudyActivityChart data={profile.activity} />
          ) : (
            <Empty>No study activity recorded in the last 60 days.</Empty>
          )}
        </CardContent>
      </Card>

      {/* ---- attempts ----------------------------------------------------- */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-base">
            <BookOpen className="h-4 w-4" /> Tests ({totals.testsCompleted} completed of{" "}
            {totals.testsStarted} started)
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          {profile.attempts.length ? (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead className="border-y bg-secondary/40 text-left text-xs uppercase tracking-wide text-muted-foreground">
                  <tr>
                    <th className="px-6 py-2 font-medium">Test</th>
                    <th className="px-3 py-2 font-medium">Started</th>
                    <th className="px-3 py-2 font-medium">Status</th>
                    <th className="px-3 py-2 text-right font-medium">Answered</th>
                    <th className="px-3 py-2 text-right font-medium">R&amp;W</th>
                    <th className="px-3 py-2 text-right font-medium">Math</th>
                    <th className="px-3 py-2 text-right font-medium">Total</th>
                    <th className="px-6 py-2" />
                  </tr>
                </thead>
                <tbody>
                  {profile.attempts.map((a) => (
                    <tr key={a.id} className="border-b last:border-0">
                      <td className="px-6 py-2 font-medium">{a.testTitle}</td>
                      <td className="px-3 py-2 text-xs">{formatDate(a.startedAt)}</td>
                      <td className="px-3 py-2">
                        <Badge
                          variant={
                            a.status === "SUBMITTED"
                              ? "success"
                              : a.status === "IN_PROGRESS"
                                ? "outline"
                                : "secondary"
                          }
                        >
                          {humanise(a.status)}
                        </Badge>
                      </td>
                      <td className="px-3 py-2 text-right tabular-nums text-muted-foreground">
                        {a.answered}
                        {a.questionCount ? `/${a.questionCount}` : ""}
                      </td>
                      <td className="px-3 py-2 text-right tabular-nums">{a.rwScaledScore ?? "—"}</td>
                      <td className="px-3 py-2 text-right tabular-nums">{a.mathScaledScore ?? "—"}</td>
                      <td className="px-3 py-2 text-right font-semibold tabular-nums">
                        {a.totalScaledScore ?? "—"}
                      </td>
                      <td className="px-6 py-2 text-right">
                        {a.status === "SUBMITTED" && (
                          <Link
                            href={`/review/${a.id}`}
                            className="text-xs text-primary hover:underline"
                          >
                            Review
                          </Link>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="p-6">
              <Empty>Has not started a test yet.</Empty>
            </div>
          )}
        </CardContent>
      </Card>

      {/* ---- sessions + vocabulary ---------------------------------------- */}
      <div className="grid gap-4 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Mentorship sessions</CardTitle>
          </CardHeader>
          <CardContent>
            {profile.bookings.length ? (
              <ul className="divide-y text-sm">
                {profile.bookings.map((b) => (
                  <li key={b.id} className="flex items-center justify-between gap-3 py-2 first:pt-0">
                    <div className="min-w-0">
                      <p className="truncate">
                        {SESSION_TYPE_LABELS[b.sessionType] ?? humanise(b.sessionType)}
                      </p>
                      <p className="text-xs text-muted-foreground">
                        {formatDate(b.startsAt, true)} · {b.coinCost} coins
                      </p>
                    </div>
                    <Badge
                      variant={
                        b.status === "COMPLETED"
                          ? "success"
                          : b.status === "CANCELLED"
                            ? "secondary"
                            : "outline"
                      }
                    >
                      {humanise(b.status)}
                    </Badge>
                  </li>
                ))}
              </ul>
            ) : (
              <Empty>Never booked a session.</Empty>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-base">Vocabulary</CardTitle>
          </CardHeader>
          <CardContent>
            {profile.vocab.wordsStarted || profile.vocab.setsAttempted ? (
              <dl className="divide-y text-sm">
                <Field label="Words studied" value={profile.vocab.wordsStarted} />
                <Field label="Words mastered" value={profile.vocab.wordsMastered} />
                <Field label="Sets attempted" value={profile.vocab.setsAttempted} />
                <Field label="Sets passed" value={profile.vocab.setsPassed} />
              </dl>
            ) : (
              <Empty>Has not opened the vocabulary module.</Empty>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

/* ------------------------------------------------------------- fragments */

function Stat({ label, value, sub }: { label: string; value: React.ReactNode; sub?: string }) {
  return (
    <Card>
      <CardContent className="p-5">
        <p className="text-xs uppercase tracking-wide text-muted-foreground">{label}</p>
        <p className="mt-1 font-display text-3xl font-semibold tabular-nums">{value}</p>
        {sub && <p className="mt-1 text-xs text-muted-foreground">{sub}</p>}
      </CardContent>
    </Card>
  );
}

function Mini({
  icon,
  label,
  children,
}: {
  icon: React.ReactNode;
  label: string;
  children: React.ReactNode;
}) {
  return (
    <div>
      <p className="flex items-center gap-1 text-xs uppercase tracking-wide text-muted-foreground">
        {icon} {label}
      </p>
      <p className="mt-0.5 font-medium tabular-nums">{children}</p>
    </div>
  );
}

/** A definition row. Renders an em dash rather than hiding when unset, so a
 *  blank profile reads as "they never told us" instead of vanishing. */
function Field({ label, value }: { label: string; value: React.ReactNode }) {
  const empty = value == null || value === "";
  return (
    <div className="flex items-baseline justify-between gap-4 py-1.5">
      <dt className="shrink-0 text-muted-foreground">{label}</dt>
      <dd className={cn("text-right", empty && "text-muted-foreground")}>{empty ? "—" : value}</dd>
    </div>
  );
}

function Empty({ children }: { children: React.ReactNode }) {
  return <p className="py-6 text-center text-sm text-muted-foreground">{children}</p>;
}

export type { StudentProfile };
