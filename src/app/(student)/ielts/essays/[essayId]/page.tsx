import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { EssayReader } from "@/components/ielts/essay-reader";
import { CATEGORY_STYLES, type Category } from "@/lib/ielts/essay-segments";
import { CATEGORY_LABELS } from "@/lib/validations/ielts-essay";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const dynamic = "force-dynamic";

const ORDER: Category[] = ["GRAMMAR", "VOCABULARY", "COHESION", "COLLOCATION"];

export async function generateMetadata({ params }: { params: { essayId: string } }) {
  const essay = await prisma.ieltsEssay.findFirst({
    where: { id: params.essayId, status: "PUBLISHED" },
    select: { title: true },
  });
  return { title: essay?.title ?? "Essay" };
}

/**
 * One Band 8+ essay, turned into a complete learning resource.
 *
 * Reading order on desktop is essay first, banks second — the essay gets the
 * majority of the space because it is the material, and the extracted language
 * is a reference beside it. On mobile the banks fall below the essay rather
 * than being squeezed next to it.
 */
export default async function EssayDetailPage({ params }: { params: { essayId: string } }) {
  await requireUser();

  // `status: PUBLISHED` in the query, not a check afterwards: a draft must be
  // unreachable by URL, not merely unlinked.
  const essay = await prisma.ieltsEssay.findFirst({
    where: { id: params.essayId, status: "PUBLISHED" },
    include: {
      annotations: { orderBy: { startOffset: "asc" } },
      ideas: { orderBy: { order: "asc" } },
    },
  });
  if (!essay) notFound();

  // Only annotations that still match the text they point at. An admin edit
  // between publish and now would shift offsets, and a highlight on the wrong
  // words teaches something false — dropping it is the safe failure.
  const intact = essay.annotations.filter(
    (a) => essay.essayText.slice(a.startOffset, a.endOffset) === a.quote
  );

  const byCategory = (c: Category) => intact.filter((a) => a.category === c);

  return (
    <div className="space-y-6">
      <Link
        href="/ielts/essays"
        className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-4 w-4" />
        Band 8+ Essay Library
      </Link>

      <div className="space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <Badge variant="navy" className="font-semibold tabular-nums">
            Band {essay.band.toFixed(1)}
          </Badge>
          <span className="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">
            IELTS Writing Task 2
          </span>
          <span className="text-xs text-muted-foreground">
            {essay.topic}
            {essay.subtopic ? ` · ${essay.subtopic}` : ""}
          </span>
        </div>
        <h1 className="max-w-4xl font-display text-xl font-semibold leading-snug tracking-tight sm:text-2xl">
          {essay.question}
        </h1>
      </div>

      <div className="grid gap-6 lg:grid-cols-[minmax(0,1.9fr)_minmax(0,1fr)] lg:items-start">
        <Card>
          <CardContent className="py-6">
            <EssayReader essayText={essay.essayText} annotations={intact} />
          </CardContent>
        </Card>

        {/* Learning panel — the essay deconstructed into reusable knowledge. */}
        <div className="space-y-4 lg:sticky lg:top-4">
          {essay.ideas.length > 0 && (
            <Card>
              <CardContent className="space-y-4 py-5">
                <div>
                  <h2 className="text-sm font-semibold">Ideas</h2>
                  <p className="text-xs text-muted-foreground">
                    Arguments from this essay you can reuse on other questions.
                  </p>
                </div>
                <ol className="space-y-4">
                  {essay.ideas.map((idea, i) => (
                    <li key={idea.id} className="space-y-1.5 border-l-2 border-border pl-3">
                      <p className="text-sm font-medium leading-snug">
                        <span className="mr-1.5 text-muted-foreground tabular-nums">{i + 1}.</span>
                        {idea.claim}
                      </p>
                      <p className="text-xs leading-relaxed text-muted-foreground">{idea.explanation}</p>
                      {idea.consequence && (
                        <p className="text-xs leading-relaxed text-muted-foreground">
                          <span className="font-medium text-foreground">Result: </span>
                          {idea.consequence}
                        </p>
                      )}
                      {idea.example && (
                        <p className="text-xs leading-relaxed text-muted-foreground">
                          <span className="font-medium text-foreground">Example: </span>
                          {idea.example}
                        </p>
                      )}
                    </li>
                  ))}
                </ol>
              </CardContent>
            </Card>
          )}

          {ORDER.map((c) => {
            const items = byCategory(c);
            if (items.length === 0) return null;
            const style = CATEGORY_STYLES[c];
            return (
              <Card key={c}>
                <CardContent className="space-y-3 py-5">
                  <div className="flex items-center gap-2">
                    <span className={cn("h-2 w-2 rounded-full", style.dot)} />
                    <h2 className="text-sm font-semibold">{CATEGORY_LABELS[c]}</h2>
                    <span className="text-xs tabular-nums text-muted-foreground">{items.length}</span>
                  </div>
                  <ul className="space-y-3">
                    {items.map((a) => (
                      <li key={a.id} className="space-y-1">
                        <p className="text-sm font-medium leading-snug">{a.quote}</p>
                        <p className="text-xs leading-relaxed text-muted-foreground">{a.explanation}</p>
                        {a.pattern && <p className="font-mono text-[11px] text-muted-foreground">{a.pattern}</p>}
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>

      <p className="border-t border-border pt-4 text-xs text-muted-foreground">
        A Band 8+ model essay curated for study. Not an official IELTS examiner script, and
        independent of IELTS, British Council, IDP and Cambridge.
      </p>
    </div>
  );
}
