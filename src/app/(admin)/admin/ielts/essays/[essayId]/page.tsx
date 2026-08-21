import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ExternalLink } from "lucide-react";

import { IeltsEssayForm } from "@/components/admin/ielts-essay-form";
import { IeltsEssayReview } from "@/components/admin/ielts-essay-review";
import { Card, CardContent } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { hashEssayText } from "@/lib/ielts/essay-analysis";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: { essayId: string } }) {
  const essay = await prisma.ieltsEssay.findUnique({
    where: { id: params.essayId },
    select: { title: true },
  });
  return { title: essay?.title ?? "Essay" };
}

export default async function AdminEssayPage({ params }: { params: { essayId: string } }) {
  await requireAdmin();

  const essay = await prisma.ieltsEssay.findUnique({
    where: { id: params.essayId },
    include: {
      annotations: { orderBy: { startOffset: "asc" } },
      ideas: { orderBy: { order: "asc" } },
    },
  });
  if (!essay) notFound();

  // Annotations were computed against a specific string. If the stored hash no
  // longer matches the current text, every offset is suspect.
  const offsetsStale =
    essay.annotations.length > 0 &&
    essay.analyzedTextHash !== null &&
    essay.analyzedTextHash !== hashEssayText(essay.essayText);

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <Link
          href="/admin/ielts/essays"
          className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-4 w-4" /> Task 2 Essays
        </Link>
        {essay.status === "PUBLISHED" && (
          <Link
            href={`/ielts/essays/${essay.id}`}
            className="inline-flex items-center gap-1.5 text-sm text-primary hover:underline"
          >
            Open as a student <ExternalLink className="h-3.5 w-3.5" />
          </Link>
        )}
      </div>

      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">
          IELTS Writing Task 2 · Band {essay.band.toFixed(1)}
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">{essay.title}</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted-foreground">{essay.question}</p>
      </div>

      <Tabs defaultValue="review">
        <TabsList>
          <TabsTrigger value="review">Analysis &amp; review</TabsTrigger>
          <TabsTrigger value="edit">Edit essay</TabsTrigger>
        </TabsList>

        <TabsContent value="review" className="mt-5">
          {essay.annotations.length === 0 && essay.status === "DRAFT" ? (
            <Card className="border-dashed">
              <CardContent className="space-y-2 py-8 text-center">
                <p className="text-sm font-semibold">Not analysed yet</p>
                <p className="mx-auto max-w-md text-sm text-muted-foreground">
                  Run the analysis to deconstruct this essay into grammar, vocabulary, cohesion,
                  collocations and reusable ideas. You review everything it finds before any of it
                  reaches a student.
                </p>
              </CardContent>
            </Card>
          ) : null}

          <div className={essay.annotations.length === 0 && essay.status === "DRAFT" ? "mt-4" : ""}>
            <IeltsEssayReview
              essayId={essay.id}
              essayText={essay.essayText}
              status={essay.status}
              analysisError={essay.analysisError}
              offsetsStale={offsetsStale}
              annotations={essay.annotations.map((a) => ({
                id: a.id,
                category: a.category,
                subtype: a.subtype,
                quote: a.quote,
                startOffset: a.startOffset,
                endOffset: a.endOffset,
                explanation: a.explanation,
                ieltsValue: a.ieltsValue,
                pattern: a.pattern,
                confidence: a.confidence,
                source: a.source,
                reviewed: a.reviewed,
              }))}
              ideas={essay.ideas.map((i) => ({
                id: i.id,
                claim: i.claim,
                explanation: i.explanation,
                consequence: i.consequence,
                example: i.example,
                reviewed: i.reviewed,
              }))}
            />
          </div>
        </TabsContent>

        <TabsContent value="edit" className="mt-5 max-w-3xl">
          <IeltsEssayForm
            initial={{
              id: essay.id,
              title: essay.title,
              question: essay.question,
              essayText: essay.essayText,
              band: essay.band,
              topic: essay.topic,
              subtopic: essay.subtopic ?? "",
              tags: essay.tags,
            }}
          />
        </TabsContent>
      </Tabs>
    </div>
  );
}
