import Link from "next/link";
import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";
import { JOURNAL_PAPERS } from "@/lib/journal/papers";

export const metadata = {
  title: "Journal",
  description:
    "The Scholarly Journal — finished research by students in the Scholarly research programme.",
};

export const dynamic = "force-dynamic";

/**
 * Only finished, published papers are public. Accepted projects that are still
 * in progress are deliberately NOT listed here: they are private to their
 * author and the team (see journal/projects/[slug]).
 */
export default async function JournalPage() {
  const user = await getCurrentUser();

  return (
    <div className="min-h-screen bg-background">
      {user ? <AppReturnBar backHref="/research" backLabel="Back to Research" /> : <SiteNav />}
      <main className="mx-auto w-full max-w-6xl px-4 py-16 sm:px-6 lg:px-8">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(190_84%_42%)]">
          The Scholarly Journal
        </p>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
          Research by students, published here
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted-foreground">
          Finished research from the Scholarly research programme, published with the
          student&apos;s name on it.
        </p>

        <div className="mt-10 space-y-10">
          <section>
            <h2 className="font-display text-xl font-semibold tracking-tight">Published</h2>
            {JOURNAL_PAPERS.length === 0 ? (
              <p className="mt-4 rounded-2xl border border-dashed border-border px-5 py-10 text-center text-sm text-muted-foreground">
                The first papers are being written now. Finished work is published here permanently
                — methodology, findings, and the author&apos;s name.
              </p>
            ) : (
              <ul className="mt-4 space-y-4">
                {JOURNAL_PAPERS.map((paper) => (
                  <li key={paper.slug}>
                    <Link
                      href={`/journal/${paper.slug}`}
                      className="block rounded-2xl border border-border px-5 py-5 transition-colors hover:border-foreground/25 hover:bg-secondary/40"
                    >
                      <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(190_84%_42%)]">
                        {paper.field}
                      </p>
                      <h3 className="mt-2 font-display text-lg font-semibold leading-snug tracking-tight">
                        {paper.title}
                      </h3>
                      {paper.subtitle ? (
                        <p className="mt-1 text-sm text-muted-foreground">{paper.subtitle}</p>
                      ) : null}
                      <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
                        {paper.abstract.slice(0, 240)}…
                      </p>
                      <p className="mt-3 text-[13px] text-muted-foreground">
                        {paper.author} · {paper.readingMinutes} min read
                      </p>
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </section>

          <p className="text-sm text-muted-foreground">
            Have a question you want to investigate?{" "}
            <Link href="/research" className="font-medium text-primary underline-offset-4 hover:underline">
              The research programme is open for proposals
            </Link>
            .
          </p>
        </div>
      </main>
    </div>
  );
}
