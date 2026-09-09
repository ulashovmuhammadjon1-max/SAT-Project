import Link from "next/link";
import { notFound } from "next/navigation";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { projectBySlug, toParagraphs } from "@/lib/journal/projects";
import { getCurrentUser } from "@/lib/session";

/**
 * A project in progress, as its own page.
 *
 * Every word of the body is the student's own submission, reproduced. This
 * page states no findings and draws no conclusions, because the work has not
 * been done yet — that is what separates it from a paper under
 * `/journal/[slug]`, and the banner near the top says so to the reader rather
 * than leaving it to be inferred from the section it was linked from.
 */

export const dynamic = "force-dynamic";

const LONG_DATE = new Intl.DateTimeFormat("en-GB", {
  day: "numeric",
  month: "long",
  year: "numeric",
  timeZone: "UTC",
});

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const project = await projectBySlug(slug);
  if (!project) return { title: "Project not found" };
  return {
    title: `${project.title} — The Scholarly Journal`,
    description: `A research project in progress by ${project.author}, in ${project.field}.`,
    authors: [{ name: project.author }],
  };
}

function Section({ heading, body }: { heading: string; body: string }) {
  return (
    <section className="mt-12">
      <h2 className="font-display text-xl font-semibold tracking-tight sm:text-2xl">{heading}</h2>
      {toParagraphs(body).map((paragraph, i) => (
        <p key={i} className="mt-4 text-[15px] leading-[1.75] text-foreground/85">
          {paragraph}
        </p>
      ))}
    </section>
  );
}

export default async function ProjectPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const [project, user] = await Promise.all([projectBySlug(slug), getCurrentUser()]);
  if (!project) notFound();

  return (
    <div className="min-h-screen bg-background">
      {user ? <AppReturnBar backHref="/research" backLabel="Back to Research" /> : <SiteNav />}
      <main className="mx-auto w-full max-w-3xl px-4 py-16 sm:px-6 lg:px-8">
        <Link
          href="/journal"
          className="text-[13px] font-medium text-muted-foreground transition-colors hover:text-foreground"
        >
          ← The Scholarly Journal
        </Link>

        <header className="mt-6 border-b border-border pb-8">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(190_84%_42%)]">
            {project.field}
          </p>
          <h1 className="mt-3 font-display text-3xl font-semibold leading-tight tracking-tight sm:text-4xl">
            {project.title}
          </h1>
          <p className="mt-5 text-[15px] font-medium">{project.author}</p>
          <p className="mt-1 text-[13px] text-muted-foreground">
            Project in progress
            {project.acceptedAt
              ? ` · accepted ${LONG_DATE.format(new Date(project.acceptedAt))}`
              : ""}
          </p>
        </header>

        <p className="mt-8 rounded-xl border border-dashed border-border bg-secondary/30 px-5 py-4 text-[14px] leading-relaxed text-muted-foreground">
          This is a research proposal, not a finished paper. It sets out the question{" "}
          {project.author} is investigating and why. There are no results here yet — the findings
          and method will be published in this journal when the work is complete.
        </p>

        <Section heading="The question" body={project.question} />
        <Section heading="Why this question" body={project.motivation} />
        {project.experience ? (
          <Section heading="Background the author brings" body={project.experience} />
        ) : null}

        <footer className="mt-16 border-t border-border pt-8">
          <p className="text-[13px] leading-relaxed text-muted-foreground">
            Published in The Scholarly Journal, which carries research by students in the Scholarly
            research programme.{" "}
            <Link href="/journal" className="font-medium text-foreground hover:underline">
              See the other projects and papers
            </Link>
            .
          </p>
        </footer>
      </main>
    </div>
  );
}
