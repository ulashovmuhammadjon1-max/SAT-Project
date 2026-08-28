import Link from "next/link";
import { BadgeCheck, GraduationCap, Sparkles } from "lucide-react";

import { SiteNav } from "@/components/marketing/site-nav";
import { prisma } from "@/lib/prisma";

export const metadata = {
  title: "Team",
  description: "The people who run Scholarly — founder, peer mentors, and the roles we are opening next.",
};

/**
 * The organisation, publicly. Two kinds of entry:
 *  - the founder, static;
 *  - approved peer mentors, pulled live from the database — the same approval
 *    that lets them host sessions puts them on this page, so the team grows
 *    exactly as fast as the programme does and never needs hand-editing.
 * Open roles are listed deliberately: a team page with vacancies reads as an
 * institution that is growing, not a finished list of friends.
 */
export const revalidate = 3600;

interface Mentor {
  name: string;
  headline: string;
  subjects: string[];
}

interface CoreMember {
  name: string;
  title: string;
  email: string | null;
  photo: string | null;
  bio: string | null;
}

async function getCoreMembers(): Promise<CoreMember[]> {
  try {
    return await prisma.teamMember.findMany({
      where: { isActive: true },
      orderBy: [{ order: "asc" }, { createdAt: "asc" }],
      select: { name: true, title: true, email: true, photo: true, bio: true },
    });
  } catch (error) {
    console.error("[team] core members unavailable", error);
    return [];
  }
}

async function getMentors(): Promise<Mentor[]> {
  try {
    const rows = await prisma.peerMentorApplication.findMany({
      where: { status: "APPROVED" },
      orderBy: { decidedAt: "asc" },
      select: { headline: true, subjects: true, user: { select: { name: true } } },
    });
    return rows
      .filter((r) => r.user.name)
      .map((r) => ({ name: r.user.name as string, headline: r.headline, subjects: r.subjects }));
  } catch (error) {
    // A build without a database must not fail; the first request regenerates.
    console.error("[team] mentors unavailable", error);
    return [];
  }
}

const OPEN_ROLES = [
  {
    title: "Content Lead",
    body: "Own the question bank's quality bar: review disputes, keep explanations sharp, run the verification pipeline.",
  },
  {
    title: "Community Lead",
    body: "Run the Telegram community, weekly analysis sessions, and events — the heartbeat of the platform.",
  },
  {
    title: "IELTS Review Lead",
    body: "Coordinate Writing and Speaking reviews so every submission gets feedback fast.",
  },
];

export default async function TeamPage() {
  const [mentors, core] = await Promise.all([getMentors(), getCoreMembers()]);

  return (
    <div className="min-h-screen bg-background">
      <SiteNav />
      <main className="mx-auto w-full max-w-5xl px-4 py-16 sm:px-6 lg:px-8">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-primary">Team</p>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
          The people behind Scholarly
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted-foreground">
          Scholarly is student-built and student-run. Everyone here earned their place with a
          verified score, real work, or both — and the team grows as the community does.
        </p>

        {/* Founder */}
        <section className="mt-10">
          <div className="rounded-2xl border border-primary/25 bg-gradient-to-br from-primary/[0.06] to-card p-6 shadow-card sm:p-8">
            <div className="flex flex-wrap items-center gap-4">
              <span className="flex h-14 w-14 items-center justify-center rounded-2xl bg-navy-900 text-white">
                <GraduationCap className="h-7 w-7" />
              </span>
              <div className="min-w-[220px] flex-1">
                <p className="font-display text-xl font-semibold tracking-tight">Muhammadjon Ulashov</p>
                <p className="text-sm font-medium text-primary">Founder · 1580 SAT</p>
              </div>
            </div>
            <p className="mt-4 max-w-3xl text-[15px] leading-relaxed text-muted-foreground">
              Built Scholarly to make serious SAT and IELTS preparation free — full adaptive
              tests, verified content, human mentorship, and a community that grows by word of
              mouth. Runs the 1-on-1 study-plan sessions and reviews every peer-mentor certificate
              personally.
            </p>
          </div>
        </section>

        {/* Core team — managed from the admin panel */}
        {core.length > 0 && (
          <section className="mt-12">
            <h2 className="font-display text-xl font-semibold tracking-tight">Core team</h2>
            <div className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {core.map((m) => (
                <div key={m.name} className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
                  <div className="flex items-center gap-3">
                    {m.photo ? (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img
                        src={m.photo}
                        alt={m.name}
                        className="h-12 w-12 rounded-xl border border-border object-cover"
                      />
                    ) : (
                      <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-secondary font-display text-lg font-semibold text-muted-foreground">
                        {m.name.slice(0, 1)}
                      </span>
                    )}
                    <div className="min-w-0">
                      <p className="truncate font-medium">{m.name}</p>
                      <p className="truncate text-sm text-primary">{m.title}</p>
                    </div>
                  </div>
                  {m.bio && <p className="mt-3 text-sm leading-relaxed text-muted-foreground">{m.bio}</p>}
                  {m.email && (
                    <a
                      href={`mailto:${m.email}`}
                      className="mt-2 block truncate text-xs text-muted-foreground underline-offset-4 hover:text-foreground hover:underline"
                    >
                      {m.email}
                    </a>
                  )}
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Peer mentors — live from the database */}
        <section className="mt-12">
          <h2 className="flex items-center gap-2 font-display text-xl font-semibold tracking-tight">
            <BadgeCheck className="h-5 w-5 text-[hsl(266_84%_60%)]" />
            Peer mentors
          </h2>
          <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
            Students who earned top scores, proved them with verified score reports, and now host
            sessions for the next cohort.
          </p>
          {mentors.length === 0 ? (
            <p className="mt-5 rounded-2xl border border-dashed border-border px-5 py-8 text-sm text-muted-foreground">
              The first cohort is being reviewed now. Scored high?{" "}
              <Link href="/mentor" className="font-medium text-primary underline-offset-4 hover:underline">
                Apply to become a peer mentor
              </Link>
              .
            </p>
          ) : (
            <div className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {mentors.map((m) => (
                <div key={m.name} className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
                  <p className="font-medium">{m.name}</p>
                  <p className="mt-0.5 text-sm text-[hsl(266_84%_60%)]">{m.headline}</p>
                  {m.subjects.length > 0 && (
                    <p className="mt-2 text-xs text-muted-foreground">{m.subjects.join(" · ")}</p>
                  )}
                </div>
              ))}
            </div>
          )}
        </section>

        {/* Open roles */}
        <section className="mt-12">
          <h2 className="flex items-center gap-2 font-display text-xl font-semibold tracking-tight">
            <Sparkles className="h-5 w-5 text-primary" />
            Open roles
          </h2>
          <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
            Volunteer positions with real ownership. Write to{" "}
            <a
              href="mailto:scholarlyhub.space@gmail.com"
              className="font-medium text-primary underline-offset-4 hover:underline"
            >
              scholarlyhub.space@gmail.com
            </a>{" "}
            with what you would do in your first month.
          </p>
          <div className="mt-5 grid gap-4 sm:grid-cols-3">
            {OPEN_ROLES.map((r) => (
              <div key={r.title} className="rounded-2xl border border-dashed border-border bg-card/50 p-5">
                <p className="font-medium">{r.title}</p>
                <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">{r.body}</p>
              </div>
            ))}
          </div>
        </section>

        <p className="mt-12 text-sm text-muted-foreground">
          See what the team has built:{" "}
          <Link href="/impact" className="font-medium text-primary underline-offset-4 hover:underline">
            our live impact numbers
          </Link>
          .
        </p>
      </main>
    </div>
  );
}
