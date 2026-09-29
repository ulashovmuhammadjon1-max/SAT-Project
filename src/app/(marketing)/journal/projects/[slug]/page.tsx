import Link from "next/link";
import { notFound } from "next/navigation";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { projectBySlug, toParagraphs, type JournalProject } from "@/lib/journal/projects";
import { getCurrentUser } from "@/lib/session";

/**
 * A project in progress, as its own page — PRIVATE.
 *
 * Visible only to the project's author and to admins. Anyone else, signed in
 * or not, gets a plain 404, so the page does not even confirm that a project
 * exists. Signed-out visitors never reach this code: the middleware sends them
 * to sign in. The metadata is gated the same way, so no title or author leaks
 * into the page head either.
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

/** The project, if the current user may see it; otherwise undefined. */
async function visibleProject(slug: string): Promise<JournalProject | undefined> {
  const [project, user] = await Promise.all([projectBySlug(slug), getCurrentUser()]);
  if (!project || !user) return undefined;
  if (user.role === "ADMIN" || user.id === project.userId) return project;
  return undefined;
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const project = await visibleProject(slug);
  // Never index, and never reveal a title to someone who cannot see the page.
  if (!project) return { title: "Not found", robots: { index: false, follow: false } };
  return {
    title: `${project.title} — Research project`,
    robots: { index: false, follow: false },
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
  const project = await visibleProject(slug);
  if (!project) notFound();

  return (
    <div className="min-h-screen bg-background">
      <AppReturnBar backHref="/research" backLabel="Back to Research" />
      <main className="mx-auto w-full max-w-3xl px-4 py-16 sm:px-6 lg:px-8">
        <Link
          href="/research"
          className="text-[13px] font-medium text-muted-foreground transition-colors hover:text-foreground"
        >
          ← Research
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
          This project is private: only its author and the Scholarly team can see this page. It
          sets out the question {project.author} is investigating and why. When the work is
          finished, the paper can be published in the Scholarly Journal.
        </p>

        <Section heading="The question" body={project.question} />
        <Section heading="Why this question" body={project.motivation} />
        {project.experience ? (
          <Section heading="Background the author brings" body={project.experience} />
        ) : null}

        <footer className="mt-16 border-t border-border pt-8">
          <p className="text-[13px] leading-relaxed text-muted-foreground">
            A project in the Scholarly research programme. This page is not public.
          </p>
        </footer>
      </main>
    </div>
  );
}
