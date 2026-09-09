import { prisma } from "@/lib/prisma";

/**
 * Accepted research projects, as the journal shows them.
 *
 * These are `ResearchProposal` rows with status ACCEPTED — work that has been
 * taken into the programme but is not finished. They are deliberately NOT
 * `JOURNAL_PAPERS`: a paper in that registry is finished writing with findings
 * in it, reviewed in a pull request, and immutable once out. A project here is
 * a question someone is working on, and every word on its page is the
 * student's own submission. Nothing about a project's results is stated
 * anywhere, because there are none yet.
 *
 * Kept in one module rather than queried at each page because the index and
 * the detail page must agree on the slug — if they compute it differently
 * every card on the index links to a 404.
 */

export interface JournalProject {
  id: string;
  slug: string;
  title: string;
  field: string;
  author: string;
  /** The student's research question, verbatim. */
  question: string;
  /** Why the student wants to investigate it, verbatim. */
  motivation: string;
  /** Prior experience, verbatim. Usually absent — the form does not require it. */
  experience: string | null;
  /** ISO timestamp of acceptance, or null if the row predates the column. */
  acceptedAt: string | null;
}

/**
 * A title becomes a URL.
 *
 * Truncated at a word boundary rather than mid-word: one of these titles is a
 * whole research question and would otherwise produce a 120-character path.
 * The cut is on the slug, not the title, so the page still shows the full
 * thing.
 */
export function slugifyTitle(title: string, maxLength = 70): string {
  const base = title
    .toLowerCase()
    .replace(/['‘’]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");

  if (base.length <= maxLength) return base || "project";

  const cut = base.slice(0, maxLength);
  const lastBoundary = cut.lastIndexOf("-");
  const trimmed = lastBoundary > 20 ? cut.slice(0, lastBoundary) : cut;
  return trimmed.replace(/^-+|-+$/g, "") || "project";
}

/**
 * Every accepted project, oldest first, each with a slug that is stable for
 * as long as its title is.
 *
 * Two projects whose titles slugify the same would otherwise collide and make
 * one of them unreachable, so a later duplicate takes a suffix from its id.
 * Assignment walks the list in creation order, which does not change when a
 * new project is accepted — so an existing project's URL does not move when
 * the next one arrives.
 */
export async function listAcceptedProjects(): Promise<JournalProject[]> {
  const rows = await prisma.researchProposal.findMany({
    where: { status: "ACCEPTED" },
    orderBy: { createdAt: "asc" },
    select: {
      id: true,
      title: true,
      field: true,
      question: true,
      motivation: true,
      experience: true,
      decidedAt: true,
      user: { select: { name: true } },
    },
  });

  const taken = new Set<string>();
  return rows.map((row) => {
    let slug = slugifyTitle(row.title);
    if (taken.has(slug)) slug = `${slug}-${row.id.slice(-6)}`;
    taken.add(slug);

    return {
      id: row.id,
      slug,
      title: row.title,
      field: row.field,
      author: row.user.name?.trim() || "Scholarly student",
      question: row.question,
      motivation: row.motivation,
      experience: row.experience,
      acceptedAt: row.decidedAt ? row.decidedAt.toISOString() : null,
    };
  });
}

export async function projectBySlug(slug: string): Promise<JournalProject | undefined> {
  const projects = await listAcceptedProjects();
  return projects.find((p) => p.slug === slug);
}

/**
 * Submitted text is a textarea's contents: blank-line separated, with CRLF
 * from browsers that send it. Split so the page can render real paragraphs
 * instead of one block with the line breaks collapsed away.
 */
export function toParagraphs(text: string): string[] {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}
