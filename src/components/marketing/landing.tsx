import Link from "next/link";
import { ArrowRight } from "lucide-react";

import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { ArrowLink, Container, Eyebrow, Lede, PrimaryLink, SectionTitle } from "@/components/marketing/editorial";
import { SiteNav } from "@/components/marketing/site-nav";
import { Wordmark } from "@/components/marketing/wordmark";
import { cn } from "@/lib/utils";

/**
 * The landing page.
 *
 * Scholarly is a free academic community — a research programme, AP courses,
 * mentorship, IELTS and financial literacy — and the page is ordered to say
 * so in the first screen. SAT preparation is real and well built but is one
 * tool among several, so it sits in a single short section near the end.
 *
 * Content rules this page keeps:
 *  - Every number is checkable. Subject counts come from the AP catalog; the
 *    question count is a floor under a measured total (see AP section).
 *  - Nothing about other students is shown. Proposals and projects are private
 *    to the student and the team, so the hero's proposal is labelled as an
 *    illustration of the format, and no stage of it is shown as achieved.
 *  - No member counts, testimonials, partner logos or outcome claims.
 *
 * A server component: there is no client-side motion here. The only
 * interactive pieces (the header and the FAQ) are their own client islands.
 */

export interface ApSummary {
  live: { code: string; name: string; category: string }[];
  categories: { id: string; label: string }[];
  plannedCount: number;
  /** A real unit from a real course outline, for the hero's course excerpt. */
  sample: {
    course: string;
    unitNumber: number;
    unitTitle: string;
    topics: { code: string; title: string }[];
  } | null;
}

const shortName = (name: string) => name.replace(/^AP /, "");

export function Landing({ ap }: { ap: ApSummary }) {
  return (
    <div className="min-h-screen overflow-x-clip bg-background">
      <SiteNav />
      <main id="main">
        <Hero ap={ap} />
        <Programmes apCount={ap.live.length} />
        <ResearchProcess />
        <ResearchableQuestions />
        <Courses ap={ap} />
        <MentorshipAndFinance />
        <Purpose />
        <SatSection />
        <Faq ap={ap} />
        <FinalCta />
      </main>
      <Footer />
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Hero                                                                        */
/* -------------------------------------------------------------------------- */

function Hero({ ap }: { ap: ApSummary }) {
  return (
    <section aria-labelledby="hero-title" className="border-b border-border">
      <Container className="grid items-center gap-12 py-12 sm:py-16 lg:grid-cols-12 lg:gap-10 lg:py-20">
        <div className="lg:col-span-6">
          <Eyebrow>A free academic community for students</Eyebrow>

          <h1
            id="hero-title"
            className="mt-6 font-serif text-[clamp(2.05rem,9.2vw,2.65rem)] font-medium leading-[1.04] tracking-[-0.02em] sm:text-[3.4rem] lg:text-[3.6rem] xl:text-[3.9rem]"
          >
            Learn like a scholar,
            <br />
            <em className="font-normal italic text-primary">before university.</em>
          </h1>

          <Lede className="mt-6 text-[17px] sm:text-[18px]">
            Investigate a research question of your own with a mentor, study AP subjects unit by unit, prepare for
            IELTS, and learn how money actually works — in one free community.
          </Lede>

          <div className="mt-8 flex flex-col items-start gap-5 sm:flex-row sm:items-center sm:gap-7">
            <PrimaryLink href="/onboarding" className="w-full sm:w-auto">
              Join Scholarly — free
              <ArrowRight aria-hidden className="h-4 w-4" />
            </PrimaryLink>
            <ArrowLink href="#research">How research works</ArrowLink>
          </div>

          <ul className="mt-10 flex flex-wrap gap-x-6 gap-y-2 border-t border-border pt-5 text-[13.5px] text-muted-foreground">
            <li>
              <span className="font-medium text-foreground">Free</span> to join
            </li>
            <li>
              Research programme <span className="font-medium text-foreground">open to proposals</span>
            </li>
            <li>
              <span className="font-medium text-foreground">{ap.live.length}</span> AP subjects live
            </li>
          </ul>
        </div>

        <div className="lg:col-span-6">
          <HeroArtifact sample={ap.sample} />
        </div>
      </Container>
    </section>
  );
}

const STAGES = ["Proposal", "Review", "Mentor", "Investigation", "Paper"] as const;

/**
 * The hero visual: a research proposal, typeset as the document it is, with a
 * real AP unit outline beside it. One focal object and one secondary one —
 * no floating panels, progress bars or glowing badges. The proposal is an
 * illustration of the format and says so; the course outline is real data.
 */
function HeroArtifact({ sample }: { sample: ApSummary["sample"] }) {
  return (
    <figure aria-labelledby="hero-artifact-caption">
      <div className="rounded-md border border-border bg-card shadow-[0_1px_0_hsl(var(--border)),0_28px_56px_-36px_rgb(21_28_43/0.45)] dark:shadow-none">
        <div className="flex items-center justify-between gap-4 border-b border-border px-5 py-3 sm:px-7">
          <p className="text-[13px] font-medium text-research">Research proposal</p>
          <p className="text-[13px] text-muted-foreground">
            Status: <span className="font-medium text-foreground">Under review</span>
          </p>
        </div>

        <dl className="space-y-5 px-5 py-6 sm:px-7 sm:py-7">
          <div>
            <dt className="text-[12.5px] text-muted-foreground">Field</dt>
            <dd className="mt-1 text-[15px]">Psychology</dd>
          </div>
          <div>
            <dt className="text-[12.5px] text-muted-foreground">Research question</dt>
            <dd className="mt-1.5 font-serif text-[1.45rem] leading-[1.3] tracking-[-0.005em] text-balance sm:text-[1.65rem]">
              How does a full night of sleep change what you remember the next day?
            </dd>
          </div>
          <div>
            <dt className="text-[12.5px] text-muted-foreground">Evidence I would look at</dt>
            <dd className="mt-1 max-w-md text-[14.5px] leading-relaxed text-muted-foreground">
              A week of sleep diaries kept by volunteer classmates, set beside a short recall test taken each morning.
            </dd>
          </div>
        </dl>

        <div className="border-t border-border px-5 py-3.5 sm:px-7">
          <ol aria-label="Stages of a project" className="flex flex-wrap items-center gap-x-2 gap-y-1 text-[12.5px]">
            {STAGES.map((stage, i) => (
              <li key={stage} className="flex items-center gap-2">
                <span
                  aria-current={stage === "Review" ? "step" : undefined}
                  className={cn(
                    stage === "Review"
                      ? "font-medium text-foreground underline decoration-research decoration-2 underline-offset-[5px]"
                      : "text-muted-foreground",
                  )}
                >
                  {stage}
                </span>
                {i < STAGES.length - 1 && (
                  <span aria-hidden className="text-border">
                    /
                  </span>
                )}
              </li>
            ))}
          </ol>
        </div>
      </div>

      <div className="mt-4 grid gap-4 sm:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)] sm:items-start">
        {sample && (
          <div className="hidden rounded-md border border-border bg-card px-5 py-4 sm:block">
            <p className="text-[12.5px] text-muted-foreground">
              {sample.course} · Unit {sample.unitNumber}
            </p>
            <p className="mt-0.5 font-serif text-[1.15rem] leading-snug">{sample.unitTitle}</p>
            <ol className="mt-3 space-y-1.5">
              {sample.topics.map((t) => (
                <li key={t.code} className="flex gap-3 text-[13px] leading-snug">
                  <span className="w-7 shrink-0 tabular-nums text-muted-foreground">{t.code}</span>
                  <span>{t.title}</span>
                </li>
              ))}
            </ol>
          </div>
        )}
        <figcaption id="hero-artifact-caption" className="text-[12.5px] leading-relaxed text-muted-foreground sm:pt-1">
          An illustration of the proposal format, not a real submission — students&rsquo; proposals are private to
          them and the review team.
          {sample && (
            <span className="hidden sm:inline">
              {" "}
              Beside it, a unit outline exactly as it appears in the {shortName(sample.course)} course.
            </span>
          )}
        </figcaption>
      </div>
    </figure>
  );
}

/* -------------------------------------------------------------------------- */
/* Programmes                                                                  */
/* -------------------------------------------------------------------------- */

interface Programme {
  title: string;
  status: string;
  body: string;
  link?: { href: string; label: string };
  research?: boolean;
}

/**
 * `status` is the only claim each row makes about how established a programme
 * is. Anything not yet running must say so; a row gets a link only when there
 * is somewhere real to go.
 */
const programmes = (apCount: number): Programme[] => [
  {
    title: "Independent research",
    status: "Open to proposals",
    body: "Formulate a question in any field and write a proposal. If it is accepted, you investigate it with a mentor until you have a finished paper in your own name.",
    link: { href: "#research", label: "How it works" },
    research: true,
  },
  {
    title: "AP courses",
    status: `${apCount} subjects live`,
    body: "Study each subject against its official course outline, unit by unit and topic by topic. Every practice question carries a written explanation, and full practice tests are scored when you finish.",
    link: { href: "#courses", label: "See the subjects" },
  },
  {
    title: "Mentorship",
    status: "Free one-to-one sessions",
    body: "Book free one-to-one sessions for study planning and test analysis. Once you have earned strong results yourself, you can apply to mentor the students coming after you.",
    link: { href: "#mentorship", label: "About mentorship" },
  },
  {
    title: "IELTS preparation",
    status: "Live now",
    body: "Practise Writing and Speaking with band-scored feedback against the marking criteria, Speaking cue cards, and a leaderboard to measure yourself against.",
    link: { href: "/onboarding", label: "Start practising" },
  },
  {
    title: "Financial literacy",
    status: "Monthly live classes",
    body: "Live classes on how money, inflation, interest rates, banking and investing shape the decisions people make every day.",
    link: { href: "#financial-literacy", label: "About the classes" },
  },
  {
    title: "Learn from experts",
    status: "In preparation",
    body: "Guest lectures and conversations with university professors and other experts, bringing academic perspectives to students directly.",
  },
];

function Programmes({ apCount }: { apCount: number }) {
  return (
    <section id="programmes" aria-labelledby="programmes-title" className="scroll-mt-16 py-20 lg:py-28">
      <Container>
        <div className="grid gap-6 lg:grid-cols-12">
          <div className="lg:col-span-5">
            <Eyebrow>Programmes</Eyebrow>
            <SectionTitle id="programmes-title" className="mt-5">
              One account, several ways to work.
            </SectionTitle>
          </div>
          <Lede className="lg:col-span-6 lg:col-start-7 lg:pt-10">
            Begin with the programme that fits what you are working on now and add others whenever you like. Each
            is free, and each asks something different of you.
          </Lede>
        </div>

        <ol className="mt-14 border-b border-border">
          {programmes(apCount).map((p, i) => (
            <li key={p.title} className="grid gap-3 border-t border-border py-7 sm:grid-cols-12 sm:gap-6 lg:py-8">
              <p aria-hidden className="font-serif text-[15px] tabular-nums text-muted-foreground sm:col-span-1 sm:pt-1.5">
                {String(i + 1).padStart(2, "0")}
              </p>
              <div className="sm:col-span-11 lg:col-span-4">
                <h3 className="font-serif text-[1.55rem] leading-tight tracking-[-0.01em]">{p.title}</h3>
                <p className={cn("mt-1.5 text-[13.5px] font-medium", p.research ? "text-research" : "text-muted-foreground")}>
                  {p.status}
                </p>
              </div>
              <p className="text-[15.5px] leading-relaxed text-muted-foreground sm:col-span-11 sm:col-start-2 lg:col-span-5 lg:col-start-auto">
                {p.body}
              </p>
              <div className="sm:col-span-11 sm:col-start-2 lg:col-span-2 lg:col-start-auto lg:text-right">
                {p.link ? (
                  <ArrowLink href={p.link.href} className="text-[14.5px]">
                    {p.link.label}
                  </ArrowLink>
                ) : (
                  <span className="text-[14.5px] text-muted-foreground">Announced when ready</span>
                )}
              </div>
            </li>
          ))}
        </ol>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Research — the process                                                      */
/* -------------------------------------------------------------------------- */

/**
 * The stages a project actually passes through. None is marked done: this is
 * a description of the programme, not anybody's record.
 */
const RESEARCH_STAGES = [
  {
    title: "Formulate a question",
    body: "Start from something you have noticed and want to understand, in any field. Narrow it until you can picture the evidence that would settle it.",
  },
  {
    title: "Write the proposal",
    body: "A title, the field, your question in a sentence or two, and why it matters to you. Experience is optional — “none yet” is an honest and acceptable answer.",
  },
  {
    title: "Review and decision",
    body: "The team reads every proposal and emails you its decision with a written note. A proposal that is not taken forward can be reworked and submitted again.",
  },
  {
    title: "Mentor pairing",
    body: "An accepted proposal is matched with a research mentor, who helps you scope the question and turn the evidence you described into a method.",
  },
  {
    title: "Investigation",
    body: "You do the reading, gather the data and run the method, with your mentor on hand to work through problems as they come up.",
  },
  {
    title: "Drafting and revision",
    body: "You write the paper and revise it against your mentor’s feedback. The argument, the analysis and the conclusions remain your own.",
  },
  {
    title: "The finished paper",
    body: "The project ends with a complete paper in your own name — a piece of original work you can discuss and stand behind.",
  },
];

const PROPOSAL_FIELDS = [
  { term: "Title", detail: "What the project is called" },
  { term: "Field", detail: "Any discipline" },
  { term: "Research question", detail: "A sentence or two" },
  { term: "Motivation", detail: "Why this question matters to you" },
  { term: "Experience", detail: "Optional" },
];

function ResearchProcess() {
  return (
    <section
      id="research"
      aria-labelledby="research-title"
      className="scroll-mt-16 border-y border-border bg-secondary/50 py-20 lg:py-28"
    >
      <Container className="grid gap-14 lg:grid-cols-12 lg:gap-10">
        <div className="lg:col-span-5">
          <div className="lg:sticky lg:top-24">
            <Eyebrow tone="research">The research programme</Eyebrow>
            <SectionTitle id="research-title" className="mt-5">
              Ask a real question. Answer it properly.
            </SectionTitle>
            <Lede className="mt-5">
              The programme takes a question you care about from a first paragraph to a finished paper, with a
              mentor beside you. You do not need prior experience. You need a question you can answer.
            </Lede>

            <div className="mt-9 rounded-md border border-border bg-card">
              <p className="border-b border-border px-5 py-3 text-[13px] font-medium">What a proposal asks for</p>
              <dl className="divide-y divide-border">
                {PROPOSAL_FIELDS.map((f) => (
                  <div key={f.term} className="flex items-baseline justify-between gap-4 px-5 py-2.5 text-[14px]">
                    <dt>{f.term}</dt>
                    <dd className="text-right text-muted-foreground">{f.detail}</dd>
                  </div>
                ))}
              </dl>
              <p className="border-t border-border px-5 py-3 text-[13px] leading-relaxed text-muted-foreground">
                One proposal under review at a time, and up to three in total.
              </p>
            </div>

            <div className="mt-8">
              <PrimaryLink href="/onboarding">
                Propose a project
                <ArrowRight aria-hidden className="h-4 w-4" />
              </PrimaryLink>
            </div>
          </div>
        </div>

        <div className="lg:col-span-6 lg:col-start-7">
          <h3 className="text-[13px] font-medium text-muted-foreground">From question to paper</h3>
          <ol className="relative mt-6">
            {RESEARCH_STAGES.map((s, i) => (
              <li key={s.title} className="relative grid grid-cols-[2.5rem_minmax(0,1fr)] gap-4 pb-9 last:pb-0">
                {i < RESEARCH_STAGES.length - 1 && (
                  <span aria-hidden className="absolute left-[1.2rem] top-10 h-[calc(100%-2.5rem)] w-px bg-border" />
                )}
                <span className="flex h-10 w-10 items-center justify-center rounded-full border border-research/40 bg-card font-serif text-[15px] tabular-nums text-research">
                  {i + 1}
                </span>
                <div className="pt-1.5">
                  <h4 className="font-serif text-[1.3rem] leading-snug">{s.title}</h4>
                  <p className="mt-1.5 text-[15px] leading-relaxed text-muted-foreground">{s.body}</p>
                </div>
              </li>
            ))}
          </ol>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Research — what a researchable question looks like                         */
/* -------------------------------------------------------------------------- */

/** Taken from the Scholarly proposal guide (app/(student)/research/guide). */
const QUESTION_PAIRS = [
  {
    vague: "How does social media affect students?",
    good: "Does time spent on short-form video the night before a practice test predict a lower Reading score the next day?",
  },
  {
    vague: "Is money important in education?",
    good: "How does the price of private SAT tutoring in three Tashkent districts compare to the score gains tutors advertise?",
  },
];

function ResearchableQuestions() {
  return (
    <section aria-labelledby="questions-title" className="py-20 lg:py-28">
      <Container>
        <div className="grid gap-6 lg:grid-cols-12">
          <div className="lg:col-span-5">
            <Eyebrow tone="research">Before you propose</Eyebrow>
            <SectionTitle id="questions-title" className="mt-5">
              A good question is narrow enough to answer.
            </SectionTitle>
          </div>
          <Lede className="lg:col-span-6 lg:col-start-7 lg:pt-10">
            A research project answers one question well. Narrow does not mean small — it means answerable: you can
            imagine the exact evidence that would settle it.
          </Lede>
        </div>

        <div className="mt-12 border-t border-border">
          <div className="hidden grid-cols-12 gap-6 py-3 text-[13px] text-muted-foreground md:grid">
            <p className="col-span-4">Too broad to answer</p>
            <p className="col-span-7 col-start-6">Answerable</p>
          </div>
          {QUESTION_PAIRS.map((q) => (
            <div key={q.vague} className="grid gap-3 border-t border-border py-7 md:grid-cols-12 md:gap-6">
              <p className="text-[15.5px] text-muted-foreground line-through decoration-muted-foreground/50 md:col-span-4">
                <span className="sr-only">Too broad: </span>
                {q.vague}
              </p>
              <p className="font-serif text-[1.3rem] leading-snug md:col-span-7 md:col-start-6">
                <span className="sr-only">Answerable: </span>
                {q.good}
              </p>
            </div>
          ))}
          <p className="border-t border-border pt-4 text-[12.5px] text-muted-foreground">
            Examples from the Scholarly proposal guide, which every student can read before submitting.
          </p>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* AP courses                                                                  */
/* -------------------------------------------------------------------------- */

const COURSE_NOTES = [
  { title: "Unit by unit", body: "Every course follows its official outline, so you practise topic 3.4 when your class reaches topic 3.4." },
  { title: "Explained answers", body: "Each question carries a written explanation of why the right answer is right." },
  { title: "Practice tests", body: "Full AP practice tests, scored when you finish." },
];

function Courses({ ap }: { ap: ApSummary }) {
  return (
    <section
      id="courses"
      aria-labelledby="courses-title"
      className="scroll-mt-16 border-t border-border bg-card py-20 lg:py-28"
    >
      <Container>
        <div className="grid gap-6 lg:grid-cols-12">
          <div className="lg:col-span-5">
            <Eyebrow>AP courses</Eyebrow>
            <SectionTitle id="courses-title" className="mt-5">
              Study each subject the way the course is taught.
            </SectionTitle>
          </div>
          <Lede className="lg:col-span-6 lg:col-start-7 lg:pt-10">
            {ap.live.length} AP subjects are live, with {ap.plannedCount} more in preparation. Each follows the units
            and topics of its official course outline, and you choose only the subjects you take.
          </Lede>
        </div>

        <div className="mt-14 grid gap-12 lg:grid-cols-12 lg:gap-10">
          <div className="grid gap-10 sm:grid-cols-2 lg:col-span-8 lg:grid-cols-3">
            {ap.categories.map((c) => (
              <div key={c.id}>
                <h3 className="border-b border-foreground/80 pb-2 text-[13px] font-medium">{c.label}</h3>
                <ul className="divide-y divide-border">
                  {ap.live
                    .filter((s) => s.category === c.id)
                    .map((s) => (
                      <li key={s.code} className="py-2.5 font-serif text-[17px] leading-snug">
                        {shortName(s.name)}
                      </li>
                    ))}
                </ul>
              </div>
            ))}
          </div>

          <div className="lg:col-span-4">
            <h3 className="border-b border-foreground/80 pb-2 text-[13px] font-medium">How a course works</h3>
            <dl className="divide-y divide-border">
              {COURSE_NOTES.map((n) => (
                <div key={n.title} className="py-3.5">
                  <dt className="text-[15px] font-medium">{n.title}</dt>
                  <dd className="mt-1 text-[14.5px] leading-relaxed text-muted-foreground">{n.body}</dd>
                </div>
              ))}
            </dl>
            {/* A floor, not a count: the banks held 23,560 by a count of the
                authored modules and 25,885 in the database when last measured.
                "More than 20,000" is true under both, and the banks only grow. */}
            <p className="mt-4 border-t border-border pt-4 text-[14px] leading-relaxed text-muted-foreground">
              More than <span className="font-medium text-foreground">20,000</span> practice questions across the AP
              banks, each with a written explanation.
            </p>
          </div>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Mentorship and financial literacy                                           */
/* -------------------------------------------------------------------------- */

const MENTORSHIP_POINTS = [
  { title: "Research mentors", body: "Paired with every accepted research project: scoping the question, designing the method, and reading drafts critically." },
  { title: "One-to-one sessions", body: "Free sessions for study planning and test analysis, booked from your account." },
  { title: "Peer mentors", body: "Students with strong results of their own, hosting sessions for the cohort behind them." },
];

const FINANCE_TOPICS = ["Money and banking", "Inflation", "Interest rates and borrowing", "Saving and investing"];

function MentorshipAndFinance() {
  return (
    <section aria-label="Mentorship and financial literacy" className="border-t border-border py-20 lg:py-28">
      <Container className="grid gap-16 lg:grid-cols-2 lg:gap-0">
        <div id="mentorship" className="scroll-mt-24 lg:pr-14">
          <Eyebrow>Mentorship</Eyebrow>
          <SectionTitle className="mt-5 sm:text-[2.25rem]">Guidance from people a step ahead.</SectionTitle>
          <Lede className="mt-5 text-[16px]">
            Mentorship here is practical: guidance from people who have recently done what you are attempting.
            Mentors advise and question; the work and its conclusions remain yours.
          </Lede>
          <dl className="mt-8 divide-y divide-border border-y border-border">
            {MENTORSHIP_POINTS.map((p) => (
              <div key={p.title} className="py-4">
                <dt className="text-[15px] font-medium">{p.title}</dt>
                <dd className="mt-1 text-[14.5px] leading-relaxed text-muted-foreground">{p.body}</dd>
              </div>
            ))}
          </dl>
          <ArrowLink href="/team" className="mt-6">
            Meet the mentors
          </ArrowLink>
        </div>

        <div id="financial-literacy" className="scroll-mt-24 lg:border-l lg:border-border lg:pl-14">
          <Eyebrow>Financial literacy</Eyebrow>
          <SectionTitle className="mt-5 sm:text-[2.25rem]">How money actually works.</SectionTitle>
          <Lede className="mt-5 text-[16px]">
            Live classes on the financial ideas behind everyday decisions, explained from first principles. No jargon
            and nothing to buy — the aim is understanding, not a product.
          </Lede>
          <ul className="mt-8 divide-y divide-border border-y border-border">
            {FINANCE_TOPICS.map((t) => (
              <li key={t} className="py-4 font-serif text-[1.2rem]">
                {t}
              </li>
            ))}
          </ul>
          <p className="mt-6 text-[14.5px] text-muted-foreground">
            Classes run monthly and are free for members.{" "}
            <Link
              href="/onboarding"
              className="font-medium text-primary underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            >
              Join to attend
            </Link>
            .
          </p>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Purpose                                                                     */
/* -------------------------------------------------------------------------- */

function Purpose() {
  return (
    <section aria-labelledby="purpose-title" className="border-t border-border bg-secondary/50 py-20 lg:py-24">
      <Container className="grid gap-6 lg:grid-cols-12">
        <h2 id="purpose-title" className="text-[13px] font-medium text-muted-foreground lg:col-span-3 lg:pt-3">
          Why Scholarly exists
        </h2>
        <p className="font-serif text-[1.65rem] leading-[1.35] tracking-[-0.01em] text-balance sm:text-[2.1rem] lg:col-span-9">
          So that students can begin working like scholars before they reach university: asking real questions,
          reading carefully, and finishing what they start. <span className="text-muted-foreground">It is free to
          join, and the essentials sit behind no paywall.</span>
        </p>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* SAT — one supplementary section                                             */
/* -------------------------------------------------------------------------- */

const SAT_POINTS = [
  "31 full-length practice tests in a Bluebook-style interface",
  "Adaptive modules that route like the real Digital SAT",
  "A written explanation on every question",
  "Analytics that show which skills are costing you points",
  "Vocabulary sets with spaced repetition",
];

function SatSection() {
  return (
    <section id="sat" aria-labelledby="sat-title" className="scroll-mt-16 border-t border-border py-20 lg:py-24">
      <Container className="grid gap-10 lg:grid-cols-12">
        <div className="lg:col-span-5">
          <Eyebrow>Also on Scholarly</Eyebrow>
          <h2 id="sat-title" className="mt-5 font-serif text-[1.85rem] font-medium leading-tight tracking-[-0.01em]">
            SAT preparation, when you need it
          </h2>
          <p className="mt-4 max-w-md text-[15.5px] leading-relaxed text-muted-foreground">
            Sitting the Digital SAT? The same free account includes a full practice engine.
          </p>
        </div>
        <div className="lg:col-span-6 lg:col-start-7">
          <ul className="divide-y divide-border border-y border-border">
            {SAT_POINTS.map((p) => (
              <li key={p} className="py-3 text-[15px]">
                {p}
              </li>
            ))}
          </ul>
          <p className="mt-4 text-[12.5px] leading-relaxed text-muted-foreground">
            Scholarly is independent and not affiliated with or endorsed by the College Board. SAT&reg; and
            Bluebook&trade; are trademarks of their owners, referenced only to describe the exam format.
          </p>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* FAQ                                                                         */
/* -------------------------------------------------------------------------- */

const faqs = ({ live, plannedCount }: ApSummary) => [
  {
    q: "What is Scholarly?",
    a: "A free academic community for students. You can carry out original research with a mentor, book one-to-one sessions, study AP subjects, prepare for IELTS, and join financial literacy classes — all with one account.",
  },
  {
    q: "How does the research programme work?",
    a: "You propose a research question in any field, with a short paragraph about why it matters to you. The team reads every proposal and emails a decision with a written note. Accepted proposals are paired with a mentor who helps you scope the question and design the method, and the project ends with a finished paper in your own name.",
  },
  {
    q: "Do I need research experience to apply?",
    a: "No. What gets a proposal turned down is vagueness, not inexperience. A narrow, answerable question and an honest account of why it interests you matter far more than a long list of past work.",
  },
  {
    q: "Can other people see my proposal?",
    a: "No. Proposals and projects in progress are private to you and the Scholarly team.",
  },
  {
    q: "Which AP subjects are available?",
    a: `${live.map((s) => shortName(s.name)).join(", ")}. ${plannedCount} more subjects are in preparation.`,
  },
  {
    q: "Is it really free?",
    a: "Yes. You can create an account and use the research programme, AP practice, IELTS practice and mentorship without entering any payment details.",
  },
  {
    q: "Is Scholarly affiliated with the College Board?",
    a: "No. Scholarly is independent. AP®, SAT® and Bluebook™ are trademarks of the College Board, which does not sponsor or endorse this platform.",
  },
];

function Faq({ ap }: { ap: ApSummary }) {
  return (
    <section id="faq" aria-labelledby="faq-title" className="scroll-mt-16 border-t border-border py-20 lg:py-28">
      <Container className="grid gap-10 lg:grid-cols-12">
        <div className="lg:col-span-4">
          <Eyebrow>FAQ</Eyebrow>
          <SectionTitle id="faq-title" className="mt-5">
            Questions, answered.
          </SectionTitle>
          <p className="mt-5 text-[15px] leading-relaxed text-muted-foreground">
            Something else? Write to{" "}
            <a
              href="mailto:scholarlyhub.space@gmail.com"
              className="font-medium text-primary underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            >
              scholarlyhub.space@gmail.com
            </a>
            .
          </p>
        </div>
        <Accordion type="single" collapsible className="border-t border-border lg:col-span-7 lg:col-start-6">
          {faqs(ap).map((f, i) => (
            <AccordionItem key={f.q} value={`item-${i}`}>
              <AccordionTrigger className="py-5 text-left text-[16px] font-medium hover:no-underline">
                {f.q}
              </AccordionTrigger>
              <AccordionContent className="max-w-[40rem] pb-6 text-[15.5px] leading-relaxed text-muted-foreground">
                {f.a}
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Final call to action                                                        */
/* -------------------------------------------------------------------------- */

/**
 * An inverted band: ink on paper becomes paper on ink, in either theme,
 * because it is drawn from the foreground and background tokens themselves.
 */
function FinalCta() {
  return (
    <section aria-labelledby="cta-title" className="bg-foreground text-background">
      <Container className="grid gap-8 py-20 lg:grid-cols-12 lg:items-end lg:py-24">
        <div className="lg:col-span-7">
          <h2
            id="cta-title"
            className="font-serif text-[2.25rem] font-medium leading-[1.08] tracking-[-0.015em] sm:text-[3rem]"
          >
            Begin with a question.
          </h2>
          <p className="mt-5 max-w-[34rem] text-[17px] leading-relaxed opacity-80">
            Propose a research project, choose your AP subjects, prepare for IELTS, or book a session with a mentor.
            Joining is free and takes about a minute.
          </p>
        </div>
        <div className="flex flex-col items-start gap-4 sm:flex-row sm:items-center lg:col-span-5 lg:justify-end">
          <Link
            href="/onboarding"
            className="inline-flex h-11 w-full items-center justify-center gap-2 rounded-md bg-background px-5 text-[15px] font-medium text-foreground transition-opacity hover:opacity-90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-background focus-visible:ring-offset-2 focus-visible:ring-offset-foreground sm:w-auto"
          >
            Join Scholarly — free
            <ArrowRight aria-hidden className="h-4 w-4" />
          </Link>
          <Link
            href="/login"
            className="rounded-sm text-[15px] font-medium underline underline-offset-4 opacity-85 hover:opacity-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-background"
          >
            I already have an account
          </Link>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Footer                                                                      */
/* -------------------------------------------------------------------------- */

const FOOTER_COLUMNS: { title: string; links: { href: string; label: string }[] }[] = [
  {
    title: "Programmes",
    links: [
      { href: "#research", label: "Independent research" },
      { href: "#courses", label: "AP courses" },
      { href: "#mentorship", label: "Mentorship" },
      { href: "#financial-literacy", label: "Financial literacy" },
      { href: "#sat", label: "SAT preparation" },
    ],
  },
  {
    title: "Scholarly",
    links: [
      { href: "/team", label: "Team" },
      { href: "/schools", label: "For schools" },
      { href: "#faq", label: "FAQ" },
    ],
  },
  {
    title: "Account",
    links: [
      { href: "/onboarding", label: "Join free" },
      { href: "/login", label: "Sign in" },
    ],
  },
];

function Footer() {
  return (
    <footer className="border-t border-border">
      <Container className="py-14">
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-12">
          <div className="sm:col-span-2 lg:col-span-5">
            <Wordmark />
            <p className="mt-4 max-w-sm text-[14.5px] leading-relaxed text-muted-foreground">
              A free academic community: independent research with mentors, AP courses, IELTS preparation and
              financial literacy.
            </p>
            <a
              href="mailto:scholarlyhub.space@gmail.com"
              className="mt-4 inline-block text-[14.5px] text-foreground underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            >
              scholarlyhub.space@gmail.com
            </a>
          </div>
          {FOOTER_COLUMNS.map((col) => (
            <nav key={col.title} aria-label={col.title} className="lg:col-span-2">
              <h2 className="text-[13px] font-medium">{col.title}</h2>
              <ul className="mt-3 space-y-2">
                {col.links.map((l) => (
                  <li key={l.label}>
                    <Link
                      href={l.href}
                      className="text-[14.5px] text-muted-foreground transition-colors hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                    >
                      {l.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </nav>
          ))}
        </div>

        <div className="mt-12 flex flex-col gap-3 border-t border-border pt-6 text-[12.5px] text-muted-foreground sm:flex-row sm:items-start sm:justify-between">
          <p className="max-w-2xl leading-relaxed">
            &copy; {new Date().getFullYear()} Scholarly. AP&reg;, SAT&reg; and Bluebook&trade; are trademarks of the
            College Board, which is not affiliated with and does not endorse this platform.
          </p>
          <p className="flex shrink-0 gap-5">
            <Link href="/terms" className="hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
              Terms of Use
            </Link>
            <Link href="/privacy" className="hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
              Privacy Policy
            </Link>
          </p>
        </div>
      </Container>
    </footer>
  );
}
