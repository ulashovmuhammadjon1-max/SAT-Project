import Link from "next/link";
import { notFound } from "next/navigation";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { StudyTimeSatPaper } from "@/components/journal/study-time-sat";
import { JOURNAL_PAPERS, paperBySlug } from "@/lib/journal/papers";
import { getCurrentUser } from "@/lib/session";

/** Paper bodies, keyed by slug. Adding a paper means a registry entry and a
 *  component here — both reviewed, which is the editorial gate. */
const BODIES: Record<string, () => React.JSX.Element> = {
  "study-time-focus-and-sat-score-improvement": StudyTimeSatPaper,
};

export function generateStaticParams() {
  return JOURNAL_PAPERS.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const paper = paperBySlug(slug);
  if (!paper) return { title: "Paper not found" };
  return {
    title: `${paper.title} — The Scholarly Journal`,
    description: paper.abstract.slice(0, 200),
    authors: [{ name: paper.author }],
  };
}

const LONG_DATE = new Intl.DateTimeFormat("en-GB", {
  day: "numeric",
  month: "long",
  year: "numeric",
  timeZone: "UTC",
});

export default async function PaperPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const paper = paperBySlug(slug);
  const Body = BODIES[slug];
  if (!paper || !Body) notFound();

  const user = await getCurrentUser();

  return (
    <div className="min-h-screen bg-background">
      {user ? (
        <AppReturnBar backHref="/research" backLabel="Back to Research" />
      ) : (
        <SiteNav />
      )}
      <main className="mx-auto w-full max-w-3xl px-4 py-16 sm:px-6 lg:px-8">
        <Link
          href="/journal"
          className="text-[13px] font-medium text-muted-foreground transition-colors hover:text-foreground"
        >
          ← The Scholarly Journal
        </Link>

        <header className="mt-6 border-b border-border pb-8">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(190_84%_42%)]">
            {paper.field}
          </p>
          <h1 className="mt-3 font-display text-3xl font-semibold leading-tight tracking-tight sm:text-4xl">
            {paper.title}
          </h1>
          {paper.subtitle ? (
            <p className="mt-3 text-lg leading-snug text-muted-foreground">{paper.subtitle}</p>
          ) : null}
          <p className="mt-5 text-[15px] font-medium">{paper.author}</p>
          <p className="mt-1 text-[13px] text-muted-foreground">
            Published {LONG_DATE.format(new Date(paper.publishedAt))} ·{" "}
            {paper.readingMinutes} min read
          </p>
        </header>

        <Body />

        <footer className="mt-16 border-t border-border pt-8">
          <p className="text-[13px] leading-relaxed text-muted-foreground">
            Published in The Scholarly Journal, which carries research written by students in
            the Scholarly research programme.{" "}
            <Link href="/journal" className="font-medium text-foreground hover:underline">
              See the other papers
            </Link>
            .
          </p>
        </footer>
      </main>
    </div>
  );
}
