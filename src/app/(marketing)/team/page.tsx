import Link from "next/link";
import { BadgeCheck, Cake, Camera, CheckCircle2, FlaskConical, GraduationCap, Languages, Mail, Phone, Send, Sparkles } from "lucide-react";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";
import {
  FOUNDER, IELTS_ASSESSORS, MEDIA_TEAM, PEER_MENTORS, RESEARCH_MENTORS, SAT_MENTOR_REQUIREMENT,
  telegramLink, type MentorCard,
} from "@/lib/team/founder";

export const metadata = {
  title: "Team",
  description: "The people who run Scholarly — founder, core team, peer mentors, and the roles we are opening next.",
};

/**
 * The organisation, publicly. Three kinds of entry:
 *  - the founder, static (src/lib/team/founder.ts);
 *  - the core team, managed from the admin panel (TeamMember rows);
 *  - approved peer mentors, pulled live from the database — the same approval
 *    that lets them host sessions puts them on this page.
 * Every query selects explicit columns (see CLAUDE.md on whole-row fetches).
 */
export const dynamic = "force-dynamic";

type Mentor = MentorCard;

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

const OPEN_ROLES: { title: string; body: string; requirements: string[] }[] = [
  {
    title: "Research Mentor",
    body: "Guide a student project from question to finished paper: scope the topic, review drafts, sign off on method.",
    requirements: [],
  },
  {
    title: "IELTS Writing Score Assessor",
    body: "Mark students' Task 1 and Task 2 responses on the four IELTS criteria and write feedback they can act on.",
    requirements: ["IELTS Writing band 6.5 or higher."],
  },
  {
    title: "IELTS Speaking Score Assessor",
    body: "Listen to recorded Speaking answers, band each criterion, and tell students exactly what to fix.",
    requirements: ["IELTS Speaking band 6.5 or higher."],
  },
  {
    title: "Media Team",
    body: "Make posts, short videos and stories for Scholarly's Instagram and Telegram, and show what the community is doing.",
    requirements: ["Not being shy ;)"],
  },
];

function MentorGrid({ mentors, accent }: { mentors: Mentor[]; accent: string }) {
  return (
    <div className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {mentors.map((m) => (
        <div key={m.name} className="rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
          <p className="font-medium">{m.name}</p>
          <p className={`mt-0.5 text-sm ${accent}`}>{m.headline}</p>
          {m.subjects.length > 0 && <p className="mt-2 text-xs text-muted-foreground">{m.subjects.join(" · ")}</p>}
        </div>
      ))}
    </div>
  );
}

export default async function TeamPage() {
  const [approved, core, user] = await Promise.all([getMentors(), getCoreMembers(), getCurrentUser()]);
  // Named mentors first, then anyone approved through /mentor who is not already listed.
  const named = new Set(PEER_MENTORS.map((m) => m.name.toLowerCase()));
  const mentors = [...PEER_MENTORS, ...approved.filter((m) => !named.has(m.name.toLowerCase()))];

  const contacts: { key: string; icon: typeof Mail; label: string; href?: string }[] = [];
  if (FOUNDER.age !== null) contacts.push({ key: "age", icon: Cake, label: `Age ${FOUNDER.age}` });
  if (FOUNDER.phone) {
    contacts.push({ key: "phone", icon: Phone, label: FOUNDER.phone, href: `tel:${FOUNDER.phone.replace(/[^\d+]/g, "")}` });
  }
  if (FOUNDER.email) contacts.push({ key: "email", icon: Mail, label: FOUNDER.email, href: `mailto:${FOUNDER.email}` });
  if (FOUNDER.telegram) {
    const tg = telegramLink(FOUNDER.telegram);
    contacts.push({ key: "telegram", icon: Send, label: tg.label, href: tg.href });
  }

  return (
    <div className="min-h-screen bg-background">
      {user ? <AppReturnBar backHref="/dashboard" backLabel="Back to home" /> : <SiteNav />}
      <main className="mx-auto w-full max-w-5xl px-4 py-16 sm:px-6 lg:px-8">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-primary">Team</p>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
          The people behind Scholarly
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted-foreground">
          Scholarly is student-built and student-run. Everyone here earned their place with real
          work — and the team grows as the community does.
        </p>

        {/* Founder */}
        <section className="mt-10">
          <div className="rounded-2xl border border-primary/25 bg-gradient-to-br from-primary/[0.06] to-card p-6 shadow-card sm:p-8">
            <div className="flex flex-wrap items-center gap-4">
              <span className="flex h-14 w-14 items-center justify-center rounded-2xl bg-navy-900 text-white">
                <GraduationCap className="h-7 w-7" />
              </span>
              <div className="min-w-[220px] flex-1">
                <p className="font-display text-xl font-semibold tracking-tight">{FOUNDER.name}</p>
                <p className="text-sm font-medium text-primary">{FOUNDER.title}</p>
              </div>
            </div>
            <p className="mt-4 max-w-3xl text-[15px] leading-relaxed text-muted-foreground">{FOUNDER.bio}</p>
            {contacts.length > 0 && (
              <ul className="mt-5 flex flex-wrap gap-2">
                {contacts.map((c) => {
                  const Icon = c.icon;
                  const body = (
                    <>
                      <Icon className="h-4 w-4 shrink-0 text-primary" />
                      <span className="truncate">{c.label}</span>
                    </>
                  );
                  return (
                    <li key={c.key} className="min-w-0 max-w-full">
                      {c.href ? (
                        <a
                          href={c.href}
                          {...(c.key === "telegram" ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                          className="flex items-center gap-2 rounded-full border border-border bg-card px-3.5 py-1.5 text-sm font-medium transition-colors hover:border-primary/40 hover:text-primary"
                        >
                          {body}
                        </a>
                      ) : (
                        <span className="flex items-center gap-2 rounded-full border border-border bg-card px-3.5 py-1.5 text-sm font-medium">
                          {body}
                        </span>
                      )}
                    </li>
                  );
                })}
              </ul>
            )}
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
            Students who earned top SAT scores and now host sessions for the next cohort.{" "}
            <Link href="/mentor" className="font-medium text-primary underline-offset-4 hover:underline">
              Apply to become a peer mentor
            </Link>
            .
          </p>
          <p className="mt-2 flex items-start gap-1.5 text-sm text-muted-foreground">
            <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-[hsl(266_84%_60%)]" aria-hidden />
            <span>
              <span className="font-medium text-foreground">Requirement:</span> {SAT_MENTOR_REQUIREMENT}
            </span>
          </p>
          <MentorGrid mentors={mentors} accent="text-[hsl(266_84%_60%)]" />
        </section>

        {/* Research mentors */}
        <section className="mt-12">
          <h2 className="flex items-center gap-2 font-display text-xl font-semibold tracking-tight">
            <FlaskConical className="h-5 w-5 text-[hsl(190_84%_42%)]" />
            Research mentors
          </h2>
          <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
            They guide students in the research programme from a first question to a finished paper.
          </p>
          <MentorGrid mentors={RESEARCH_MENTORS} accent="text-[hsl(190_84%_42%)]" />
        </section>

        {/* IELTS assessors */}
        <section className="mt-12">
          <h2 className="flex items-center gap-2 font-display text-xl font-semibold tracking-tight">
            <Languages className="h-5 w-5 text-[hsl(152_60%_40%)]" />
            IELTS assessors
          </h2>
          <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
            They mark IELTS Writing and Speaking practice and give every student a band with feedback.
          </p>
          <MentorGrid mentors={IELTS_ASSESSORS} accent="text-[hsl(152_60%_40%)]" />
        </section>

        {/* Media team */}
        <section className="mt-12">
          <h2 className="flex items-center gap-2 font-display text-xl font-semibold tracking-tight">
            <Camera className="h-5 w-5 text-[hsl(340_75%_55%)]" />
            Media team
          </h2>
          <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
            They run Scholarly&apos;s channels and tell the community&apos;s story.
          </p>
          <MentorGrid mentors={MEDIA_TEAM} accent="text-[hsl(340_75%_55%)]" />
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
          <div className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {OPEN_ROLES.map((r) => (
              <div key={r.title} className="rounded-2xl border border-dashed border-border bg-card/50 p-5">
                <p className="font-medium">{r.title}</p>
                <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">{r.body}</p>
                {r.requirements.length > 0 && (
                  <div className="mt-3 border-t border-border/70 pt-3">
                    <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Requirements</p>
                    <ul className="mt-1.5 space-y-1">
                      {r.requirements.map((req) => (
                        <li key={req} className="flex items-start gap-1.5 text-sm">
                          <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-primary" aria-hidden />
                          {req}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
