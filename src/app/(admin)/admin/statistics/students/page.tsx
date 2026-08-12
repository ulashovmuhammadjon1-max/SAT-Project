import Link from "next/link";
import { ArrowLeft } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { getStudentActivity, type StudentActivityRow } from "@/lib/admin/statistics";
import { cn } from "@/lib/utils";

export const metadata = { title: "Student activity" };
export const dynamic = "force-dynamic";

/** Days since a date, or null when there is none. */
function daysSince(date: Date | null): number | null {
  if (!date) return null;
  return Math.floor((Date.now() - new Date(date).getTime()) / 86_400_000);
}

function LastActive({ date }: { date: Date | null }) {
  const days = daysSince(date);
  if (days === null) return <span className="text-muted-foreground">never</span>;
  const label = days === 0 ? "today" : days === 1 ? "yesterday" : `${days}d ago`;
  return (
    <span
      className={cn(
        days <= 2 && "text-emerald-500",
        days > 14 && "text-muted-foreground",
        days > 30 && "text-destructive"
      )}
    >
      {label}
    </span>
  );
}

export default async function StudentActivityPage() {
  const students = await getStudentActivity();

  const active = students.filter((s) => {
    const d = daysSince(s.lastActiveAt);
    return d !== null && d <= 7;
  }).length;
  const neverStarted = students.filter((s) => s.questionsAnswered === 0).length;

  return (
    <div className="space-y-6">
      <div>
        <Link
          href="/admin/statistics"
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> Statistics
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold tracking-tight">Student activity</h1>
        <p className="text-sm text-muted-foreground">
          One row per student — click a name for their full profile. {students.length} shown ·{" "}
          {active} active in the last week · {neverStarted} who have never answered a question.
        </p>
      </div>

      <Card>
        <CardContent className="p-0">
          {students.length ? (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead className="border-b bg-secondary/40 text-left text-xs uppercase tracking-wide text-muted-foreground">
                  <tr>
                    <Th className="pl-6">Student</Th>
                    <Th>Joined</Th>
                    <Th>Last active</Th>
                    <Th right>Questions</Th>
                    <Th right>Days active</Th>
                    <Th right>Accuracy</Th>
                    <Th right>Tests</Th>
                    <Th right>Best score</Th>
                    <Th right className="pr-6">Sessions</Th>
                  </tr>
                </thead>
                <tbody>
                  {students.map((s) => (
                    <Row key={s.userId} s={s} />
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p className="p-8 text-center text-sm text-muted-foreground">No students yet.</p>
          )}
        </CardContent>
      </Card>

      <p className="text-xs text-muted-foreground">
        Accuracy is from Question Bank answers only, where every answer is graded on submission.
        Test answers are not pooled in, because a student who abandons a module leaves ungraded
        questions behind and they would read as wrong. Sessions shows attended out of booked.
      </p>
    </div>
  );
}

function Row({ s }: { s: StudentActivityRow }) {
  const dormant = s.questionsAnswered === 0;
  return (
    <tr className={cn("border-b last:border-0 hover:bg-secondary/40", dormant && "opacity-60")}>
      <Td className="pl-6">
        <Link
          href={`/admin/statistics/students/${s.userId}`}
          className="font-medium hover:text-primary hover:underline"
        >
          {s.name ?? "—"}
        </Link>
        <span className="block text-xs text-muted-foreground">{s.email}</span>
      </Td>
      <Td>
        <span className="text-xs">
          {new Date(s.joinedAt).toLocaleDateString(undefined, {
            day: "numeric",
            month: "short",
            year: "numeric",
          })}
        </span>
      </Td>
      <Td>
        <span className="text-xs">
          <LastActive date={s.lastActiveAt} />
        </span>
      </Td>
      <Td right>{s.questionsAnswered}</Td>
      <Td right>{s.daysActive}</Td>
      <Td right>
        {s.accuracyPct === null ? (
          <span className="text-muted-foreground">—</span>
        ) : (
          <span
            className={cn(
              "font-semibold tabular-nums",
              s.accuracyPct >= 75 && "text-emerald-500",
              s.accuracyPct < 40 && "text-amber-500"
            )}
          >
            {s.accuracyPct}%
          </span>
        )}
      </Td>
      <Td right>{s.testsCompleted}</Td>
      <Td right>{s.bestScore ?? <span className="text-muted-foreground">—</span>}</Td>
      <Td right className="pr-6">
        {s.sessionsBooked ? (
          <span>
            {s.sessionsAttended}
            <span className="text-muted-foreground">/{s.sessionsBooked}</span>
          </span>
        ) : (
          <span className="text-muted-foreground">—</span>
        )}
      </Td>
    </tr>
  );
}

function Th({
  children,
  right,
  className,
}: {
  children: React.ReactNode;
  right?: boolean;
  className?: string;
}) {
  return <th className={cn("px-3 py-2 font-medium", right && "text-right", className)}>{children}</th>;
}

function Td({
  children,
  right,
  className,
}: {
  children: React.ReactNode;
  right?: boolean;
  className?: string;
}) {
  return <td className={cn("px-3 py-2", right && "text-right tabular-nums", className)}>{children}</td>;
}
