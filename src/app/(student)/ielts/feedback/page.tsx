import Link from "next/link";
import { Mic, PenLine } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { formatBand, PRACTICE_DISCLAIMER } from "@/lib/ielts/bands";
import { REVIEWER_CLAIM, SPEAKING_CRITERIA, WRITING_CRITERIA } from "@/lib/ielts/constants";

export const metadata = { title: "My Feedback" };
export const dynamic = "force-dynamic";

const STATUS_LABEL: Record<string, string> = {
  ASSIGNED: "Waiting for reviewer",
  IN_REVIEW: "Under review",
  COMPLETE: "Reviewed",
  RETURNED: "Returned",
};

function Criterion({ label, band }: { label: string; band: number }) {
  return (
    <div className="flex items-baseline justify-between gap-3 border-b border-border py-1.5 last:border-0">
      <span className="text-sm text-muted-foreground">{label}</span>
      <span className="font-display text-base font-semibold tabular-nums">
        {formatBand(band)}
      </span>
    </div>
  );
}

function Note({ label, text }: { label: string; text?: string | null }) {
  if (!text?.trim()) return null;
  return (
    <div className="space-y-1">
      <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
        {label}
      </p>
      <p className="whitespace-pre-wrap text-sm leading-relaxed">{text}</p>
    </div>
  );
}

export default async function IeltsFeedbackPage() {
  const user = await requireUser();

  const [writing, speaking] = await Promise.all([
    prisma.ieltsWritingSubmission.findMany({
      where: { userId: user.id, status: { not: "PENDING" } },
      orderBy: { submittedAt: "desc" },
      include: { review: true },
    }),
    prisma.ieltsSpeakingSubmission.findMany({
      where: { userId: user.id, status: { not: "PENDING" } },
      orderBy: { submittedAt: "desc" },
      include: { review: true, attempt: { select: { test: { select: { title: true } } } } },
    }),
  ]);

  const parts = await prisma.ieltsPart.findMany({
    where: { id: { in: writing.map((w) => w.partId) } },
    select: {
      id: true, partNumber: true, title: true,
      section: { select: { test: { select: { title: true } } } },
    },
  });
  const partOf = new Map(parts.map((p) => [p.id, p]));

  const empty = writing.length === 0 && speaking.length === 0;

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <h1 className="font-display text-2xl font-semibold tracking-tight">My Feedback</h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Every Writing and Speaking response you send is scored by a human against the four
          official criteria. Free, with no limit.
        </p>
      </div>

      {empty && (
        <Card>
          <CardContent className="space-y-3 py-10 text-center">
            <p className="text-sm text-muted-foreground">
              You have not submitted anything for review yet.
            </p>
            <div className="flex justify-center gap-2">
              <Link href="/ielts/writing" className="text-sm font-medium underline">
                Start a Writing task
              </Link>
              <span className="text-muted-foreground">or</span>
              <Link href="/ielts/speaking" className="text-sm font-medium underline">
                record a Speaking test
              </Link>
            </div>
          </CardContent>
        </Card>
      )}

      {writing.length > 0 && (
        <section className="space-y-3">
          <h2 className="flex items-center gap-2 font-display text-lg font-semibold">
            <PenLine className="h-4 w-4" /> Writing
          </h2>
          {writing.map((s) => {
            const part = partOf.get(s.partId);
            const r = s.review;
            return (
              <Card key={s.id}>
                <CardContent className="space-y-4 py-5">
                  <div className="flex flex-wrap items-center justify-between gap-3">
                    <div>
                      <p className="text-sm font-semibold">
                        {part?.section.test.title} — {part?.title ?? `Task ${part?.partNumber}`}
                      </p>
                      <p className="text-xs text-muted-foreground">
                        {s.wordCount} words · submitted{" "}
                        {new Date(s.submittedAt).toLocaleDateString()}
                      </p>
                    </div>
                    {r ? (
                      <div className="text-right">
                        <p className="text-xs uppercase tracking-wide text-muted-foreground">
                          Practice band
                        </p>
                        <p className="font-display text-3xl font-semibold tabular-nums">
                          {formatBand(r.overallBand)}
                        </p>
                      </div>
                    ) : (
                      <Badge variant="outline">{STATUS_LABEL[s.status] ?? s.status}</Badge>
                    )}
                  </div>

                  {r && (
                    <>
                      <div className="rounded-lg border border-border p-3">
                        <Criterion label={WRITING_CRITERIA[0].label} band={r.taskBand} />
                        <Criterion label={WRITING_CRITERIA[1].label} band={r.coherenceBand} />
                        <Criterion label={WRITING_CRITERIA[2].label} band={r.lexicalBand} />
                        <Criterion label={WRITING_CRITERIA[3].label} band={r.grammarBand} />
                      </div>
                      <div className="space-y-3">
                        <Note label="Overall feedback" text={r.overallFeedback} />
                        <Note label="What you did well" text={r.didWell} />
                        <Note label="What to improve" text={r.toImprove} />
                        <Note label={WRITING_CRITERIA[0].label} text={r.taskResponseNotes} />
                        <Note label={WRITING_CRITERIA[1].label} text={r.coherenceNotes} />
                        <Note label={WRITING_CRITERIA[2].label} text={r.vocabularyNotes} />
                        <Note label={WRITING_CRITERIA[3].label} text={r.grammarNotes} />
                        <Note label="Next steps" text={r.nextSteps} />
                      </div>
                      <p className="text-xs text-muted-foreground">{REVIEWER_CLAIM.WRITING}.</p>
                    </>
                  )}
                </CardContent>
              </Card>
            );
          })}
        </section>
      )}

      {speaking.length > 0 && (
        <section className="space-y-3">
          <h2 className="flex items-center gap-2 font-display text-lg font-semibold">
            <Mic className="h-4 w-4" /> Speaking
          </h2>
          {speaking.map((s) => {
            const r = s.review;
            return (
              <Card key={s.id}>
                <CardContent className="space-y-4 py-5">
                  <div className="flex flex-wrap items-center justify-between gap-3">
                    <div>
                      <p className="text-sm font-semibold">{s.attempt.test.title}</p>
                      <p className="text-xs text-muted-foreground">
                        submitted {new Date(s.submittedAt).toLocaleDateString()}
                      </p>
                    </div>
                    {r ? (
                      <div className="text-right">
                        <p className="text-xs uppercase tracking-wide text-muted-foreground">
                          Practice band
                        </p>
                        <p className="font-display text-3xl font-semibold tabular-nums">
                          {formatBand(r.overallBand)}
                        </p>
                      </div>
                    ) : (
                      <Badge variant="outline">{STATUS_LABEL[s.status] ?? s.status}</Badge>
                    )}
                  </div>

                  {r && (
                    <>
                      <div className="rounded-lg border border-border p-3">
                        <Criterion label={SPEAKING_CRITERIA[0].label} band={r.fluencyBand} />
                        <Criterion label={SPEAKING_CRITERIA[1].label} band={r.lexicalBand} />
                        <Criterion label={SPEAKING_CRITERIA[2].label} band={r.grammarBand} />
                        <Criterion label={SPEAKING_CRITERIA[3].label} band={r.pronunciationBand} />
                      </div>
                      <div className="space-y-3">
                        <Note label="Overall feedback" text={r.overallFeedback} />
                        <Note label="Strong points" text={r.strongPoints} />
                        <Note label="Main weaknesses" text={r.weaknesses} />
                        <Note label={SPEAKING_CRITERIA[0].label} text={r.fluencyNotes} />
                        <Note label={SPEAKING_CRITERIA[1].label} text={r.vocabularyNotes} />
                        <Note label={SPEAKING_CRITERIA[2].label} text={r.grammarNotes} />
                        <Note label={SPEAKING_CRITERIA[3].label} text={r.pronunciationNotes} />
                        <Note label="How to improve" text={r.howToImprove} />
                      </div>
                      <p className="text-xs text-muted-foreground">{REVIEWER_CLAIM.SPEAKING}.</p>
                    </>
                  )}
                </CardContent>
              </Card>
            );
          })}
        </section>
      )}

      <p className="border-t border-border pt-4 text-xs text-muted-foreground">
        {PRACTICE_DISCLAIMER}
      </p>
    </div>
  );
}
