import Link from "next/link";
import {
  BookMarked, Brain, Coins, FlaskConical, Languages, LineChart, Sparkles,
} from "lucide-react";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";
import { cn } from "@/lib/utils";

export const metadata = {
  title: "Journal",
  description:
    "The Scholarly Journal — student research from the community: published work and projects in progress, by area.",
};

export const dynamic = "force-dynamic";

/**
 * Research areas. `match` is tested against the free-text `field` a student
 * typed in their proposal, so an accepted project files itself under the right
 * area with no admin step; anything unmatched lands in the last area.
 */
const AREAS = [
  { slug: "tests", label: "Tests & Assessment", icon: LineChart, match: /test|assess|sat|ielts|exam|score/i },
  { slug: "social", label: "Social Science", icon: Brain, match: /psych|social|sociol|anthro|politic/i },
  { slug: "education", label: "Education", icon: BookMarked, match: /educat|learn|teach|school|study/i },
  { slug: "economics", label: "Economics & Finance", icon: Coins, match: /econ|financ|money|market|business/i },
  { slug: "science", label: "Science & Technology", icon: FlaskConical, match: /bio|chem|phys|computer|data|tech|environment|math/i },
  { slug: "language", label: "Language & Linguistics", icon: Languages, match: /lang|linguist|writing|vocab/i },
  { slug: "other", label: "Other Fields", icon: Sparkles, match: /$^/ },
] as const;

type AreaSlug = (typeof AREAS)[number]["slug"];

function areaFor(field: string): AreaSlug {
  for (const a of AREAS) {
    if (a.match.test(field)) return a.slug;
  }
  return "other";
}

interface Project {
  title: string;
  field: string;
  author: string;
  area: AreaSlug;
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
      area: areaFor(r.field),
    }));
  } catch (error) {
    // A build without a database must not fail; the first request regenerates.
    console.error("[journal] projects unavailable", error);
    return [];
  }
}

export default async function JournalPage({
  searchParams,
}: {
  searchParams: { area?: string };
}) {
  const [projects, user] = await Promise.all([getProjects(), getCurrentUser()]);
  const selected: AreaSlug | null = AREAS.some((a) => a.slug === searchParams.area)
    ? (searchParams.area as AreaSlug)
    : null;
  const shown = selected ? projects.filter((p) => p.area === selected) : projects;
  const countFor = (slug: AreaSlug) => projects.filter((p) => p.area === slug).length;

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

        <div className="mt-10 grid gap-8 lg:grid-cols-[240px_1fr]">
          {/* Areas sidebar */}
          <nav className="lg:border-r lg:border-border/70 lg:pr-6">
            <p className="px-3 pb-2 text-[10.5px] font-semibold uppercase tracking-[0.12em] text-muted-foreground/80">
              Areas of research
            </p>
            <div className="flex flex-row flex-wrap gap-1 lg:flex-col">
              <Link
                href="/journal"
                className={cn(
                  "flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm font-medium transition-colors",
                  selected === null
                    ? "bg-primary text-primary-foreground shadow-soft"
                    : "text-muted-foreground hover:bg-secondary hover:text-foreground"
                )}
              >
                <Sparkles className="h-4 w-4" />
                All areas
                <span className="ml-auto text-xs tabular-nums opacity-70">{projects.length}</span>
              </Link>
              {AREAS.map((a) => (
                <Link
                  key={a.slug}
                  href={`/journal?area=${a.slug}`}
                  className={cn(
                    "flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm font-medium transition-colors",
                    selected === a.slug
                      ? "bg-primary text-primary-foreground shadow-soft"
                      : "text-muted-foreground hover:bg-secondary hover:text-foreground"
                  )}
                >
                  <a.icon className="h-4 w-4" />
                  <span className="min-w-0 flex-1 truncate">{a.label}</span>
                  <span className="ml-auto text-xs tabular-nums opacity-70">{countFor(a.slug)}</span>
                </Link>
              ))}
            </div>
          </nav>

          {/* Content */}
          <div className="space-y-10">
            <section>
              <h2 className="font-display text-xl font-semibold tracking-tight">Published</h2>
              <p className="mt-4 rounded-2xl border border-dashed border-border px-5 py-10 text-center text-sm text-muted-foreground">
                The first papers are being written now. Finished work is published here permanently
                — methodology, findings, and the author&apos;s name.
              </p>
            </section>

            <section>
              <h2 className="font-display text-xl font-semibold tracking-tight">In progress</h2>
              {shown.length === 0 ? (
                <p className="mt-4 rounded-2xl border border-dashed border-border px-5 py-10 text-center text-sm text-muted-foreground">
                  No accepted projects in this area yet —{" "}
                  <Link
                    href="/research"
                    className="font-medium text-primary underline-offset-4 hover:underline"
                  >
                    propose the first one
                  </Link>
                  .
                </p>
              ) : (
                <div className="mt-4 grid gap-4 sm:grid-cols-2">
                  {shown.map((p, i) => (
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
        </div>
      </main>
    </div>
  );
}
