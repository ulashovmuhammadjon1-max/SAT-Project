import Link from "next/link";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { Container, Eyebrow, Lede, SectionTitle } from "@/components/marketing/editorial";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";
import { prisma } from "@/lib/prisma";
import { FOUNDER, PEER_MENTORS, RESEARCH_MENTORS, telegramLink, type MentorCard } from "@/lib/team/founder";

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

const OPEN_ROLES = [
  {
    title: "Research Mentor",
    body: "Guide a student project from question to finished paper: scope the topic, review drafts, sign off on method.",
  },
];

function MentorList({ title, intro, mentors, research }: { title: string; intro: React.ReactNode; mentors: Mentor[]; research?: boolean }) {
  return (
    <section className="border-t border-border py-12 lg:grid lg:grid-cols-12 lg:gap-10">
      <div className="lg:col-span-4">
        <h2 className="font-serif text-[1.75rem] font-medium leading-tight">{title}</h2>
        <p className="mt-3 max-w-sm text-[15px] leading-relaxed text-muted-foreground">{intro}</p>
      </div>
      <ul className="mt-8 grid border-t border-border sm:grid-cols-2 lg:col-span-8 lg:mt-0 lg:grid-cols-3">
        {mentors.map((m) => (
          <li key={m.name} className="border-b border-border py-5 sm:pr-6">
            <p className="font-serif text-[1.25rem] leading-snug">{m.name}</p>
            <p className={`mt-1 text-[14px] ${research ? "text-research" : "text-muted-foreground"}`}>{m.headline}</p>
            {m.subjects.length > 0 && <p className="mt-1 text-[13px] text-muted-foreground">{m.subjects.join(" · ")}</p>}
          </li>
        ))}
      </ul>
    </section>
  );
}

export default async function TeamPage() {
  const [approved, core, user] = await Promise.all([getMentors(), getCoreMembers(), getCurrentUser()]);
  // Named mentors first, then anyone approved through /mentor who is not already listed.
  const named = new Set(PEER_MENTORS.map((m) => m.name.toLowerCase()));
  const mentors = [...PEER_MENTORS, ...approved.filter((m) => !named.has(m.name.toLowerCase()))];

  const contacts: { key: string; term: string; label: string; href?: string }[] = [];
  if (FOUNDER.age !== null) contacts.push({ key: "age", term: "Age", label: String(FOUNDER.age) });
  if (FOUNDER.phone) {
    contacts.push({ key: "phone", term: "Phone", label: FOUNDER.phone, href: `tel:${FOUNDER.phone.replace(/[^\d+]/g, "")}` });
  }
  if (FOUNDER.email) contacts.push({ key: "email", term: "Email", label: FOUNDER.email, href: `mailto:${FOUNDER.email}` });
  if (FOUNDER.telegram) {
    const tg = telegramLink(FOUNDER.telegram);
    contacts.push({ key: "telegram", term: "Telegram", label: tg.label, href: tg.href });
  }

  return (
    <div className="min-h-screen bg-background">
      {user ? <AppReturnBar backHref="/dashboard" backLabel="Back to home" /> : <SiteNav />}
      <main id="main">
        <Container className="py-16 lg:py-24">
          <div className="grid gap-6 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <Eyebrow>Team</Eyebrow>
              <SectionTitle as="h1" className="mt-5 sm:text-[2.9rem]">
                The people behind Scholarly
              </SectionTitle>
            </div>
            <Lede className="lg:col-span-5 lg:pt-12">
              Scholarly is student-built and student-run. Everyone here earned their place with real work, and the
              team grows as the community does.
            </Lede>
          </div>

          {/* Founder */}
          <section aria-labelledby="founder-name" className="mt-14 border-t border-border py-12 lg:grid lg:grid-cols-12 lg:gap-10">
            <div className="lg:col-span-4">
              <p className="text-[13px] text-muted-foreground">{FOUNDER.title}</p>
              <h2 id="founder-name" className="mt-2 font-serif text-[2rem] font-medium leading-tight">
                {FOUNDER.name}
              </h2>
            </div>
            <div className="mt-5 lg:col-span-8 lg:mt-0">
              <p className="max-w-2xl font-serif text-[1.3rem] leading-[1.5]">{FOUNDER.bio}</p>
              {contacts.length > 0 && (
                <dl className="mt-8 grid max-w-2xl border-t border-border sm:grid-cols-2">
                  {contacts.map((c) => (
                    <div key={c.key} className="border-b border-border py-3 sm:pr-6">
                      <dt className="text-[13px] text-muted-foreground">{c.term}</dt>
                      <dd className="mt-0.5 break-all text-[15px]">
                        {c.href ? (
                          <a
                            href={c.href}
                            {...(c.key === "telegram" ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                            className="text-primary underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                          >
                            {c.label}
                          </a>
                        ) : (
                          c.label
                        )}
                      </dd>
                    </div>
                  ))}
                </dl>
              )}
            </div>
          </section>

          {/* Core team — managed from the admin panel */}
          {core.length > 0 && (
            <section className="border-t border-border py-12 lg:grid lg:grid-cols-12 lg:gap-10">
              <h2 className="font-serif text-[1.75rem] font-medium leading-tight lg:col-span-4">Core team</h2>
              <ul className="mt-8 grid border-t border-border sm:grid-cols-2 lg:col-span-8 lg:mt-0">
                {core.map((m) => (
                  <li key={m.name} className="flex gap-4 border-b border-border py-5 sm:pr-6">
                    {m.photo && (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img src={m.photo} alt="" className="h-14 w-14 shrink-0 rounded-md border border-border object-cover" />
                    )}
                    <div className="min-w-0">
                      <p className="font-serif text-[1.25rem] leading-snug">{m.name}</p>
                      <p className="mt-0.5 text-[14px] text-muted-foreground">{m.title}</p>
                      {m.bio && <p className="mt-2 text-[14.5px] leading-relaxed text-muted-foreground">{m.bio}</p>}
                      {m.email && (
                        <a href={`mailto:${m.email}`} className="mt-1.5 block truncate text-[13.5px] text-primary underline-offset-4 hover:underline">
                          {m.email}
                        </a>
                      )}
                    </div>
                  </li>
                ))}
              </ul>
            </section>
          )}

          <MentorList
            title="Research mentors"
            intro="They guide students in the research programme from a first question to a finished paper."
            mentors={RESEARCH_MENTORS}
            research
          />

          <MentorList
            title="Peer mentors"
            intro={
              <>
                Students with top SAT results who now host sessions for the next cohort.{" "}
                <Link href="/mentor" className="font-medium text-primary underline-offset-4 hover:underline">
                  Apply to become a peer mentor
                </Link>
                .
              </>
            }
            mentors={mentors}
          />

          {/* Open roles */}
          <section className="border-t border-border py-12 lg:grid lg:grid-cols-12 lg:gap-10">
            <div className="lg:col-span-4">
              <h2 className="font-serif text-[1.75rem] font-medium leading-tight">Open roles</h2>
              <p className="mt-3 max-w-sm text-[15px] leading-relaxed text-muted-foreground">
                Volunteer positions with real ownership. Write to{" "}
                <a href="mailto:scholarlyhub.space@gmail.com" className="font-medium text-primary underline-offset-4 hover:underline">
                  scholarlyhub.space@gmail.com
                </a>{" "}
                with what you would do in your first month.
              </p>
            </div>
            <ul className="mt-8 border-t border-border lg:col-span-8 lg:mt-0">
              {OPEN_ROLES.map((r) => (
                <li key={r.title} className="border-b border-border py-5">
                  <p className="font-serif text-[1.25rem] leading-snug">{r.title}</p>
                  <p className="mt-1.5 max-w-xl text-[15px] leading-relaxed text-muted-foreground">{r.body}</p>
                </li>
              ))}
            </ul>
          </section>
        </Container>
      </main>
    </div>
  );
}
