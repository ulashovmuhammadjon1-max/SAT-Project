import Link from "next/link";
import { ArrowRight, BookOpenCheck, Search } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { cn } from "@/lib/utils";

export const metadata = { title: "Essay Analyzer" };
export const dynamic = "force-dynamic";

const BANDS = ["8", "8.5", "9"] as const;

/**
 * The Band 8+ Task 2 library.
 *
 * Students only ever see PUBLISHED essays — the filter is applied in the query
 * rather than in the page, so a draft cannot leak through a filter combination
 * nobody thought to test.
 */
export default async function EssayLibraryPage({
  searchParams,
}: {
  searchParams: { band?: string; topic?: string; q?: string };
}) {
  await requireUser();

  const band = BANDS.includes(searchParams.band as (typeof BANDS)[number])
    ? Number(searchParams.band)
    : null;
  const topic = searchParams.topic?.trim() || null;
  const q = searchParams.q?.trim() || null;

  const where = {
    status: "PUBLISHED" as const,
    ...(band ? { band } : {}),
    ...(topic ? { topic } : {}),
    ...(q
      ? {
          OR: [
            { question: { contains: q, mode: "insensitive" as const } },
            { title: { contains: q, mode: "insensitive" as const } },
            { topic: { contains: q, mode: "insensitive" as const } },
            { tags: { has: q } },
          ],
        }
      : {}),
  };

  const [essays, topics, total] = await Promise.all([
    prisma.ieltsEssay.findMany({
      where,
      orderBy: [{ publishedAt: "desc" }],
      select: {
        id: true, title: true, question: true, band: true, topic: true,
        subtopic: true, wordCount: true,
        _count: { select: { annotations: true, ideas: true } },
      },
    }),
    prisma.ieltsEssay.findMany({
      where: { status: "PUBLISHED" },
      select: { topic: true },
      distinct: ["topic"],
      orderBy: { topic: "asc" },
    }),
    prisma.ieltsEssay.count({ where: { status: "PUBLISHED" } }),
  ]);

  const href = (patch: Record<string, string | null>) => {
    const p = new URLSearchParams();
    const merged = { band: searchParams.band, topic: searchParams.topic, q: searchParams.q, ...patch };
    for (const [k, v] of Object.entries(merged)) if (v) p.set(k, v);
    const s = p.toString();
    return s ? `/ielts/essays?${s}` : "/ielts/essays";
  };

  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">
          IELTS Writing Task 2
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Band 8+ Essay Library</h1>
        <p className="max-w-2xl text-sm text-muted-foreground">
          Explore high-scoring Task 2 essays and deconstruct the ideas, vocabulary, grammar and
          cohesion behind them. Every essay here is a Band 8+ model answer, marked up so you can
          see exactly what makes it work.
        </p>
      </div>

      {total > 0 && (
        <div className="space-y-3">
          <form method="GET" className="relative max-w-md">
            {searchParams.band && <input type="hidden" name="band" value={searchParams.band} />}
            {searchParams.topic && <input type="hidden" name="topic" value={searchParams.topic} />}
            <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
            <Input
              name="q"
              defaultValue={searchParams.q ?? ""}
              placeholder="Search questions, titles or topics"
              className="pl-9"
            />
          </form>

          <div className="flex flex-wrap items-center gap-2">
            <span className="text-xs font-medium text-muted-foreground">Band</span>
            <FilterPill href={href({ band: null })} active={!band}>All</FilterPill>
            {BANDS.map((b) => (
              <FilterPill key={b} href={href({ band: b })} active={searchParams.band === b}>
                {b === "8" ? "8.0" : b}
              </FilterPill>
            ))}
          </div>

          {topics.length > 1 && (
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-xs font-medium text-muted-foreground">Topic</span>
              <FilterPill href={href({ topic: null })} active={!topic}>All</FilterPill>
              {topics.map((t) => (
                <FilterPill key={t.topic} href={href({ topic: t.topic })} active={topic === t.topic}>
                  {t.topic}
                </FilterPill>
              ))}
            </div>
          )}
        </div>
      )}

      {essays.length === 0 ? (
        <Card className="border-dashed">
          <CardContent className="flex flex-col items-center gap-2 py-14 text-center">
            <BookOpenCheck className="h-6 w-6 text-muted-foreground" />
            <p className="text-sm font-semibold">
              {total === 0 ? "No essays published yet" : "Nothing matches those filters"}
            </p>
            <p className="max-w-sm text-sm text-muted-foreground">
              {total === 0
                ? "Band 8+ model essays will appear here as they are added."
                : "Try a different band or topic."}
            </p>
            {total > 0 && (
              <Link href="/ielts/essays" className="text-sm font-medium text-primary underline-offset-4 hover:underline">
                Clear filters
              </Link>
            )}
          </CardContent>
        </Card>
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {essays.map((e) => (
            <Link key={e.id} href={`/ielts/essays/${e.id}`} className="group">
              <Card className="h-full transition-colors hover:border-primary/50">
                <CardContent className="flex h-full flex-col gap-3 py-5">
                  <div className="flex flex-wrap items-center gap-2">
                    <Badge variant="navy" className="font-semibold tabular-nums">
                      Band {e.band.toFixed(1)}
                    </Badge>
                    <span className="text-xs text-muted-foreground">IELTS Writing Task 2</span>
                  </div>

                  {/* The question is the most prominent thing on the card — it
                      is what a student is actually looking for. */}
                  <p className="flex-1 text-[15px] font-medium leading-snug">{e.question}</p>

                  <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-muted-foreground">
                    <span>{e.topic}{e.subtopic ? ` · ${e.subtopic}` : ""}</span>
                    <span className="tabular-nums">{e.wordCount} words</span>
                    <span className="tabular-nums">{e._count.annotations} highlights</span>
                  </div>

                  <span className="flex items-center gap-1 text-sm font-medium text-primary">
                    Explore essay
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                  </span>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

function FilterPill({
  href,
  active,
  children,
}: {
  href: string;
  active: boolean;
  children: React.ReactNode;
}) {
  return (
    <Link
      href={href}
      className={cn(
        "rounded-full border px-3 py-1 text-xs font-medium transition-colors",
        active
          ? "border-primary bg-primary text-primary-foreground"
          : "border-border text-muted-foreground hover:bg-secondary"
      )}
    >
      {children}
    </Link>
  );
}
