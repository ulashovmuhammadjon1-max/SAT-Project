import Link from "next/link";
import type { Subject } from "@prisma/client";
import { Bookmark, History, Sparkles, Target, XCircle } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { DomainProgressList, OverviewStats } from "@/components/student/qb-progress";
import { cn } from "@/lib/utils";
import {
  getDomainProgress,
  getQuestionBankOverview,
} from "@/server/actions/student/question-bank";

export const metadata = { title: "Question Bank" };
export const dynamic = "force-dynamic";

const SUBJECTS: { value: Subject; label: string }[] = [
  { value: "READING_WRITING", label: "Reading & Writing" },
  { value: "MATH", label: "Math" },
];

export default async function QuestionBankPage({
  searchParams,
}: {
  searchParams: { subject?: string };
}) {
  const subject: Subject =
    searchParams.subject === "MATH" ? "MATH" : "READING_WRITING";

  const [overview, domains] = await Promise.all([
    getQuestionBankOverview(subject),
    getDomainProgress(subject),
  ]);

  return (
    <div className="space-y-8">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Question Bank</h1>
          <p className="text-sm text-muted-foreground">Practice exactly what you need to improve.</p>
        </div>
        <div className="flex flex-wrap gap-2">
          <Button asChild variant="outline" size="sm">
            <Link href="/practice/history">
              <History className="h-4 w-4" /> History
            </Link>
          </Button>
          <Button asChild size="sm">
            <Link href={`/practice/start?subject=${subject}`}>
              <Target className="h-4 w-4" /> Start practice
            </Link>
          </Button>
        </div>
      </div>

      {/* Subject switcher */}
      <div
        role="tablist"
        aria-label="Subject"
        className="inline-flex rounded-lg bg-secondary p-1"
      >
        {SUBJECTS.map((s) => {
          const active = s.value === subject;
          return (
            <Link
              key={s.value}
              href={`/practice?subject=${s.value}`}
              role="tab"
              aria-selected={active}
              className={cn(
                "rounded-md px-4 py-1.5 text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                active
                  ? "bg-background text-foreground shadow-sm"
                  : "text-muted-foreground hover:text-foreground"
              )}
            >
              {s.label}
            </Link>
          );
        })}
      </div>

      <OverviewStats overview={overview} />

      {/* Quick entry points */}
      <div className="grid gap-3 sm:grid-cols-3">
        <QuickCard
          href={`/practice/start?subject=${subject}&newOnly=1`}
          icon={Sparkles}
          title="New questions only"
          body="Skip everything you've already answered."
        />
        <QuickCard
          href={`/practice/start?subject=${subject}&mistakes=1`}
          icon={XCircle}
          title="Practice my mistakes"
          body={
            overview.incorrect > 0
              ? `${overview.incorrect} question${overview.incorrect === 1 ? "" : "s"} to revisit.`
              : "Nothing missed yet."
          }
          disabled={overview.incorrect === 0}
        />
        <QuickCard
          href={`/practice/browse?subject=${subject}&status=SAVED`}
          icon={Bookmark}
          title="Saved questions"
          body={
            overview.saved > 0
              ? `${overview.saved} saved for later.`
              : "Bookmark questions to find them here."
          }
          disabled={overview.saved === 0}
        />
      </div>

      <div>
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h2 className="font-display text-lg font-semibold">Progress by topic</h2>
          <Button asChild variant="ghost" size="sm">
            <Link href={`/practice/browse?subject=${subject}`}>Browse all questions</Link>
          </Button>
        </div>
        <p className="mt-1 text-sm text-muted-foreground">
          Click any subtopic to practice it directly.
        </p>
        <div className="mt-4">
          <DomainProgressList domains={domains} subject={subject} />
        </div>
      </div>
    </div>
  );
}

function QuickCard({
  href,
  icon: Icon,
  title,
  body,
  disabled,
}: {
  href: string;
  icon: typeof Sparkles;
  title: string;
  body: string;
  disabled?: boolean;
}) {
  const inner = (
    <Card className={cn("h-full", disabled ? "opacity-60" : "transition-colors hover:border-primary")}>
      <CardContent className="flex items-start gap-3 p-4">
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
          <Icon className="h-4 w-4" />
        </span>
        <div>
          <p className="font-medium leading-snug">{title}</p>
          <p className="mt-0.5 text-[13px] text-muted-foreground">{body}</p>
        </div>
      </CardContent>
    </Card>
  );

  if (disabled) return <div aria-disabled>{inner}</div>;
  return (
    <Link href={href} className="rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
      {inner}
    </Link>
  );
}
