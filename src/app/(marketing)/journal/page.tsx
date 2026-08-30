import Link from "next/link";
import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";
import { JOURNAL_PAPERS } from "@/lib/journal/papers";

export const metadata = {
  title: "Journal",
  description:
    "The Scholarly Journal — student research from the community: published work and projects in progress, by area.",
};

export const dynamic = "force-dynamic";

interface Project {
  title: string;
  field: string;
  author: string;
}

async function getProjects(): Promise<Project[]> {
  try {
    const rows = await prisma.researchProposal.findMany({
      where: { status: "ACCEPTED" },
      orderBy: { decidedAt: "desc" },
      select: { title: true, field: true, user: { select: { name: true } } },
    });
    return rows.map((r) => ({
      title: r.title,
      field: r.field,
      author: r.user.name ?? "Scholarly student",
    }));
  } catch (error) {
    // A build without a database must not fail; the first request regenerates.
    console.error("[journal] projects unavailable", error);
    return [];
  }
}

export default async function JournalPage() {
  const [projects, user] = await Promise.all([getProjects(), getCurrentUser()]);

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
          Every project in the research programme ends up on this page — first as work in
          progress, then as finished, published writing with the student&apos;s name on it.
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

          <section>
            <h2 className="font-display text-xl font-semibold tracking-tight">In progress</h2>
            {projects.length === 0 ? (
              <p className="mt-4 rounded-2xl border border-dashed border-border px-5 py-10 text-center text-sm text-muted-foreground">
                No accepted projects yet —{" "}
                <Link
                  href="/research"
                  className="font-medium text-primary underline-offset-4 hover:underline"
                >
                  propose the first one
                </Link>
                .
              </p>
            ) : (
              <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {projects.map((p, i) => (
                  <div key={`${p.title}-${i}`} className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
                    <p className="text-xs font-semibold uppercase tracking-wide text-[hsl(190_84%_42%)]">
                      {p.field}
                    </p>
                    <p className="mt-1.5 font-medium leading-snug">{p.title}</p>
                    <p className="mt-2 text-sm text-muted-foreground">{p.author}</p>
                  </div>
                ))}
              </div>
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
