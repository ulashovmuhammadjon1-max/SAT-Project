import Link from "next/link";
import { ArrowLeft, Check, X } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { getRecentActivity } from "@/server/actions/student/question-bank";

export const metadata = { title: "Question history" };
export const dynamic = "force-dynamic";

/** "Today" / "Yesterday" / "3 days ago" — friendlier than a raw timestamp. */
function relativeDay(date: Date) {
  const startOfToday = new Date();
  startOfToday.setHours(0, 0, 0, 0);
  const then = new Date(date);
  then.setHours(0, 0, 0, 0);
  const days = Math.round((startOfToday.getTime() - then.getTime()) / 86_400_000);
  if (days <= 0) return "Today";
  if (days === 1) return "Yesterday";
  if (days < 7) return `${days} days ago`;
  return date.toLocaleDateString(undefined, { month: "short", day: "numeric" });
}

export default async function QuestionHistoryPage() {
  const items = await getRecentActivity(50);

  return (
    <div className="space-y-6">
      <div>
        <Link
          href="/practice"
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> Question Bank
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold tracking-tight">Recent activity</h1>
        <p className="text-sm text-muted-foreground">
          Every question you&apos;ve answered, in the Question Bank and in practice tests.
        </p>
      </div>

      {items.length === 0 ? (
        <Card>
          <CardContent className="p-8 text-center text-sm text-muted-foreground">
            You haven&apos;t answered any questions yet.
          </CardContent>
        </Card>
      ) : (
        <ul className="space-y-2">
          {items.map((h, i) => (
            <li key={`${h.questionId}-${i}`}>
              <Card>
                <CardContent className="flex flex-wrap items-center gap-x-3 gap-y-1.5 p-4">
                  <span className="font-mono text-xs text-muted-foreground">{h.ref}</span>
                  <span className="text-sm font-medium">{h.skillName}</span>
                  <span className="text-xs text-muted-foreground">
                    {h.subject === "MATH" ? "Math" : "Reading & Writing"} — {h.domainName}
                  </span>
                  {h.source === "TEST" && <Badge variant="secondary">Practice test</Badge>}
                  <span className="ml-auto flex items-center gap-3">
                    <span className="flex items-center gap-1 text-xs">
                      {h.isCorrect ? (
                        <>
                          <Check className="h-3.5 w-3.5 text-success" />
                          <span className="text-success">Correct</span>
                        </>
                      ) : (
                        <>
                          <X className="h-3.5 w-3.5 text-destructive" />
                          <span className="text-destructive">Incorrect</span>
                        </>
                      )}
                    </span>
                    <span className="text-xs text-muted-foreground">{relativeDay(h.at)}</span>
                  </span>
                </CardContent>
              </Card>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
