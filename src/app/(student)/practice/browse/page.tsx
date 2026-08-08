import Link from "next/link";
import type { QuestionDifficulty, Subject } from "@prisma/client";
import { ArrowLeft, Bookmark, Check, X } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";
import { listQuestions, type AttemptStatus } from "@/server/actions/student/question-bank";

export const metadata = { title: "Browse questions" };
export const dynamic = "force-dynamic";

const PAGE_SIZE = 20;
const VALID_STATUSES = new Set(["ALL", "NOT_ATTEMPTED", "ATTEMPTED", "CORRECT", "INCORRECT", "SAVED"]);
const STATUS_TABS: { value: AttemptStatus; label: string }[] = [
  { value: "ALL", label: "All" },
  { value: "NOT_ATTEMPTED", label: "Not attempted" },
  { value: "INCORRECT", label: "Mistakes" },
  { value: "CORRECT", label: "Correct" },
  { value: "SAVED", label: "Saved" },
];

export default async function BrowseQuestionsPage({
  searchParams,
}: {
  searchParams: { subject?: string; status?: string; difficulty?: string; page?: string };
}) {
  await requireUser();
  const subject: Subject = searchParams.subject === "MATH" ? "MATH" : "READING_WRITING";
  const status = (
    VALID_STATUSES.has(searchParams.status ?? "") ? searchParams.status : "ALL"
  ) as AttemptStatus;
  const page = Math.max(1, parseInt(searchParams.page ?? "1", 10) || 1);

  const { items, total } = await listQuestions({ subject, status }, page, PAGE_SIZE);
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));

  function hrefFor(next: Partial<{ status: string; page: number }>) {
    const p = new URLSearchParams({ subject, status, page: String(page) });
    if (next.status !== undefined) {
      p.set("status", next.status);
      p.set("page", "1");
    }
    if (next.page !== undefined) p.set("page", String(next.page));
    return `/practice/browse?${p.toString()}`;
  }

  return (
    <div className="space-y-6">
      <div>
        <Link
          href={`/practice?subject=${subject}`}
          className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> Question Bank
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold tracking-tight">Browse questions</h1>
        <p className="text-sm text-muted-foreground">
          {total.toLocaleString()} question{total === 1 ? "" : "s"} in{" "}
          {subject === "MATH" ? "Math" : "Reading & Writing"}.
        </p>
      </div>

      <div className="flex flex-wrap gap-2">
        {STATUS_TABS.map((t) => (
          <Link
            key={t.value}
            href={hrefFor({ status: t.value })}
            className={cn(
              "rounded-full border px-3 py-1.5 text-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
              status === t.value
                ? "border-primary bg-primary/10 font-medium text-primary"
                : "border-border text-muted-foreground hover:bg-secondary"
            )}
          >
            {t.label}
          </Link>
        ))}
      </div>

      {items.length === 0 ? (
        <Card>
          <CardContent className="p-8 text-center text-sm text-muted-foreground">
            No questions here yet.
          </CardContent>
        </Card>
      ) : (
        <ul className="space-y-2">
          {items.map((q) => (
            <li key={q.id}>
              <Card>
                <CardContent className="flex flex-wrap items-center gap-x-3 gap-y-2 p-4">
                  <span className="font-mono text-xs text-muted-foreground">{q.ref}</span>
                  <span className="text-sm font-medium">{q.skillName}</span>
                  <span className="text-xs text-muted-foreground">{q.domainName}</span>
                  <Badge
                    variant={
                      q.difficulty === "HARD" ? "destructive" : q.difficulty === "EASY" ? "success" : "warning"
                    }
                  >
                    {q.difficulty[0] + q.difficulty.slice(1).toLowerCase()}
                  </Badge>
                  {q.saved && (
                    <Bookmark className="h-3.5 w-3.5 fill-current text-primary" aria-label="Saved" />
                  )}
                  <span className="ml-auto flex items-center gap-1.5 text-xs">
                    {q.status === "CORRECT" && (
                      <>
                        <Check className="h-3.5 w-3.5 text-success" />
                        <span className="text-success">Correct</span>
                      </>
                    )}
                    {q.status === "INCORRECT" && (
                      <>
                        <X className="h-3.5 w-3.5 text-destructive" />
                        <span className="text-destructive">Incorrect previously</span>
                      </>
                    )}
                    {q.status === "NOT_ATTEMPTED" && (
                      <span className="text-muted-foreground">Not attempted</span>
                    )}
                  </span>
                </CardContent>
              </Card>
            </li>
          ))}
        </ul>
      )}

      {totalPages > 1 && (
        <nav className="flex items-center justify-between" aria-label="Pagination">
          <Button asChild variant="outline" size="sm" disabled={page <= 1}>
            <Link href={hrefFor({ page: Math.max(1, page - 1) })} aria-disabled={page <= 1}>
              Previous
            </Link>
          </Button>
          <span className="text-sm text-muted-foreground">
            Page {page} of {totalPages}
          </span>
          <Button asChild variant="outline" size="sm" disabled={page >= totalPages}>
            <Link
              href={hrefFor({ page: Math.min(totalPages, page + 1) })}
              aria-disabled={page >= totalPages}
            >
              Next
            </Link>
          </Button>
        </nav>
      )}
    </div>
  );
}
