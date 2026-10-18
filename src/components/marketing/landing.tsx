"use client";

import Link from "next/link";
import { motion, useReducedMotion, useScroll, useTransform } from "framer-motion";
import { createContext, useContext, useRef } from "react";
import {
  ArrowRight,
  Award,
  BarChart3,
  BookOpen,
  CalendarDays,
  CheckCircle2,
  ClipboardList,
  FlaskConical,
  GraduationCap,
  Languages,
  Layers,
  LineChart,
  Microscope,
  MonitorPlay,
  PenLine,
  ShieldCheck,
  Sparkles,
  Star,
  UserRound,
  Users,
  Wallet,
  Zap,
} from "lucide-react";

import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Button } from "@/components/ui/button";
import { SiteNav } from "@/components/marketing/site-nav";
import { BluebookMockup } from "@/components/marketing/mockups";
import { CountUp, FloatingBlob, HoverLift, Reveal, RevealGroup, RevealItem } from "@/components/marketing/motion";
import { cn } from "@/lib/utils";

/**
 * The landing page.
 *
 * Scholarly is a free academic community: a student research programme,
 * mentorship, AP courses, IELTS and financial literacy. The page is ordered to
 * say so in the first second. SAT preparation is real and well built, but it is
 * one tool among several, so it lives in a single section near the end rather
 * than in the hero.
 *
 * Every number on this page is checkable: subject counts come from the AP
 * catalog itself, and question counts are floors under a measured total.
 */

/**
 * The AP catalog summary, computed on the server (app/page.tsx) and handed in.
 * The catalog module imports the full course outlines, which would otherwise
 * ship to every visitor's browser just to count subjects.
 */
export interface ApSummary {
  live: { code: string; name: string }[];
  plannedCount: number;
}

const ApContext = createContext<ApSummary>({ live: [], plannedCount: 0 });
const useAp = () => useContext(ApContext);
const shortName = (name: string) => name.replace(/^AP /, "");

export function Landing({ ap }: { ap: ApSummary }) {
  return (
    <ApContext.Provider value={ap}>
    <div className="min-h-screen overflow-x-clip bg-background">
      <SiteNav />
      <main>
        <Hero />
        <Programmes />
        <Research />
        <Courses />
        <Stats />
        <StreakBand />
        <SatSection />
        <Faq />
        <FinalCta />
      </main>
      <Footer />
    </div>
    </ApContext.Provider>
  );
}

/* -------------------------------------------------------------------------- */
/* Shared                                                                      */
/* -------------------------------------------------------------------------- */

function SectionLabel({ icon: Icon, children }: { icon: typeof Sparkles; children: React.ReactNode }) {
  return (
    <span className="inline-flex items-center gap-1.5 rounded-full border border-border/70 bg-secondary/60 px-3 py-1 text-xs font-medium text-muted-foreground backdrop-blur">
      <Icon className="h-3.5 w-3.5 text-primary" />
      {children}
    </span>
  );
}

function SectionHeading({
  label,
  title,
  body,
  align = "center",
  icon = Sparkles,
}: {
  label: string;
  title: React.ReactNode;
  body?: React.ReactNode;
  align?: "center" | "left";
  icon?: typeof Sparkles;
}) {
  return (
    <div className={cn("max-w-2xl", align === "center" && "mx-auto text-center")}>
      <Reveal>
        <SectionLabel icon={icon}>{label}</SectionLabel>
      </Reveal>
      <Reveal delay={0.06}>
        <h2 className="mt-5 font-display text-3xl font-semibold tracking-tight text-balance sm:text-4xl lg:text-[2.75rem] lg:leading-[1.1]">
          {title}
        </h2>
      </Reveal>
      {body && (
        <Reveal delay={0.12}>
          <p className="mt-4 text-[17px] leading-relaxed text-muted-foreground text-balance">{body}</p>
        </Reveal>
      )}
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* 1. Hero                                                                     */
/* -------------------------------------------------------------------------- */

function Hero() {
  const { live } = useAp();
  const ref = useRef<HTMLDivElement>(null);
  const reduced = useReducedMotion();
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
  const mockY = useTransform(scrollYProgress, [0, 1], [0, 56]);

  return (
    <section ref={ref} className="relative isolate overflow-hidden pb-14 pt-28 sm:pt-32 lg:pb-16 lg:pt-32">
      {/* Background: campus plate (dark theme only), wash, soft colour fields. */}
      <div className="pointer-events-none absolute inset-0 -z-10">
        <div className="hero-plate absolute inset-0 hidden dark:block" />
        <div className="hero-wash absolute inset-0 hidden dark:block" />
        <div className="absolute inset-0 bg-[radial-gradient(70%_50%_at_50%_0%,hsl(226_84%_56%/0.10),transparent_70%)]" />
        <FloatingBlob className="absolute -top-24 left-[8%] h-[380px] w-[380px] rounded-full bg-primary/20 blur-[110px]" />
        <FloatingBlob
          className="absolute right-[6%] top-10 h-[420px] w-[420px] rounded-full bg-[hsl(190_84%_42%)]/15 blur-[120px]"
          duration={22}
          delay={1.5}
        />
        <FloatingBlob
          className="absolute left-[38%] top-[42%] h-[300px] w-[300px] rounded-full bg-success/10 blur-[100px]"
          duration={26}
          delay={3}
        />
        <div className="absolute inset-0 bg-[linear-gradient(to_right,hsl(var(--border))_1px,transparent_1px),linear-gradient(to_bottom,hsl(var(--border))_1px,transparent_1px)] bg-[size:56px_56px] opacity-[0.35] [mask-image:radial-gradient(70%_50%_at_50%_0%,black,transparent)]" />
      </div>

      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="grid items-center gap-12 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.05fr)] lg:gap-10">
          <div className="text-center lg:text-left">
            <Reveal direction="none" scale={0.96}>
              <span className="inline-flex items-center gap-2 rounded-full border border-border/70 bg-card/70 px-3.5 py-1.5 text-[10px] font-semibold uppercase leading-tight tracking-[0.08em] text-muted-foreground shadow-soft backdrop-blur sm:text-[11.5px] sm:tracking-[0.1em]">
                <span className="flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-success/15">
                  <span className="h-1.5 w-1.5 rounded-full bg-success" />
                </span>
                <span className="text-left">
                  Free academic community
                  <span className="mx-1.5 text-border">•</span>
                  <span className="whitespace-nowrap">For students who want more</span>
                </span>
              </span>
            </Reveal>

            <Reveal delay={0.08}>
              <h1 className="mt-6 font-display text-[2.7rem] font-bold leading-[0.98] tracking-[-0.02em] text-balance sm:text-[3.5rem] lg:text-[3.5rem] xl:text-[4rem]">
                Learn like a scholar.
                <br />
                <span className="text-gradient-animated bg-gradient-to-r from-primary via-[hsl(190_84%_42%)] to-[hsl(152_60%_42%)] bg-[length:200%_auto] bg-clip-text text-transparent">
                  Research, mentors &amp; real courses.
                </span>
              </h1>
            </Reveal>

            <Reveal delay={0.16}>
              <p className="mx-auto mt-6 max-w-xl text-[17px] leading-relaxed text-muted-foreground text-balance lg:mx-0 lg:text-lg">
                Investigate your own research question with a mentor, study AP subjects unit by unit, prepare for
                IELTS, and learn how money actually works — in one free community.
              </p>
            </Reveal>

            <Reveal delay={0.24}>
              <div className="mt-9 flex flex-col items-stretch gap-3 sm:flex-row sm:items-center sm:justify-center lg:justify-start">
                <Button
                  size="lg"
                  className="group h-12 rounded-full px-7 text-[15px] shadow-card transition-shadow hover:shadow-panel"
                  asChild
                >
                  <Link href="/onboarding">
                    Join Scholarly — Free
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                  </Link>
                </Button>
                <Button
                  size="lg"
                  variant="outline"
                  className="h-12 rounded-full border-border/80 px-7 text-[15px] backdrop-blur"
                  asChild
                >
                  <a href="#research">How research works</a>
                </Button>
              </div>
            </Reveal>

            <Reveal delay={0.32}>
              <ul className="mt-5 flex flex-wrap items-center justify-center gap-x-5 gap-y-2 text-[13px] text-muted-foreground lg:justify-start">
                {["Free to join", "Research programme open", `${live.length} AP subjects live`].map((t) => (
                  <li key={t} className="flex items-center gap-1.5">
                    <CheckCircle2 className="h-3.5 w-3.5 shrink-0 text-success" />
                    {t}
                  </li>
                ))}
              </ul>
            </Reveal>
          </div>

          <motion.div style={reduced ? undefined : { y: mockY }} className="relative">
            <div className="absolute -inset-8 -z-10 rounded-[2.5rem] bg-gradient-to-br from-primary/20 via-[hsl(190_84%_42%)]/5 to-transparent blur-3xl" />
            <HeroPathways />
          </motion.div>
        </div>

        <ValueStrip />
      </div>
    </section>
  );
}

/**
 * The hero visual: what a student actually does here, as product cards — a
 * research project moving through the programme's real stages, an AP unit in
 * progress, and a mentor session. Illustrative UI: no names, and no claims
 * about other students.
 */
function HeroPathways() {
  const stages = [
    { label: "Proposal accepted", state: "done" },
    { label: "Mentor paired", state: "done" },
    { label: "Doing the research", state: "current" },
    { label: "Paper finished", state: "next" },
  ] as const;

  return (
    <div className="relative mx-auto max-w-[560px]">
      <Reveal direction="none" scale={0.97} duration={0.7}>
        <div className="rounded-2xl border border-border/70 bg-card/95 p-5 shadow-panel backdrop-blur sm:p-6">
          <div className="flex items-center justify-between gap-3">
            <span className="inline-flex items-center gap-1.5 rounded-full bg-[hsl(190_84%_42%)]/10 px-2.5 py-1 text-[11px] font-semibold text-[hsl(190_84%_42%)]">
              <FlaskConical className="h-3.5 w-3.5" /> Research project
            </span>
            <span className="rounded-full border border-success/30 bg-success/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.08em] text-success">
              Accepted
            </span>
          </div>
          <p className="mt-4 text-xs font-medium uppercase tracking-[0.12em] text-muted-foreground">
            Your research question
          </p>
          <p className="mt-1.5 font-display text-lg font-semibold leading-snug text-balance">
            How does a full night of sleep change what you remember the next day?
          </p>
          <ol className="mt-5 space-y-2.5">
            {stages.map((s) => (
              <li key={s.label} className="flex items-center gap-3 text-sm">
                <span
                  className={cn(
                    "flex h-5 w-5 shrink-0 items-center justify-center rounded-full border",
                    s.state === "done" && "border-success bg-success text-white",
                    s.state === "current" && "border-primary bg-primary/10",
                    s.state === "next" && "border-border",
                  )}
                >
                  {s.state === "done" ? (
                    <CheckCircle2 className="h-3.5 w-3.5" />
                  ) : s.state === "current" ? (
                    <span className="h-1.5 w-1.5 rounded-full bg-primary" />
                  ) : null}
                </span>
                <span className={cn(s.state === "next" ? "text-muted-foreground" : "text-foreground")}>
                  {s.label}
                </span>
              </li>
            ))}
          </ol>
        </div>
      </Reveal>

      <Reveal delay={0.4} direction="up" className="relative z-10 -mt-5 ml-auto w-[86%] sm:-mt-6 sm:w-[72%]">
        <div className="rounded-2xl border border-border/70 bg-card p-4 shadow-panel">
          <div className="flex items-center gap-3">
            <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-success/10 text-success">
              <Award className="h-4 w-4" />
            </span>
            <div className="min-w-0 flex-1">
              <p className="text-[11px] font-semibold uppercase tracking-[0.1em] text-muted-foreground">AP Biology</p>
              <p className="truncate text-sm font-medium">Unit 3 · Cellular Energetics</p>
            </div>
          </div>
          <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-secondary">
            <div className="h-full w-[62%] rounded-full bg-gradient-to-r from-success to-[hsl(190_84%_42%)]" />
          </div>
        </div>
      </Reveal>

      <Reveal delay={0.55} direction="up" className="relative -mt-3 w-[80%] sm:w-[64%]">
        <div className="rounded-2xl border border-primary/25 bg-card p-4 shadow-panel">
          <div className="flex items-center gap-3">
            <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-primary/10 text-primary">
              <UserRound className="h-4 w-4" />
            </span>
            <div className="min-w-0 flex-1">
              <p className="text-[11px] font-semibold uppercase tracking-[0.1em] text-primary">1-on-1 with a mentor</p>
              <p className="truncate text-sm font-medium">Scoping your research method</p>
            </div>
          </div>
        </div>
      </Reveal>
    </div>
  );
}

const valueStrip = (apCount: number) => [
  { icon: FlaskConical, title: "Student research", body: "Investigate a question you care about" },
  { icon: UserRound, title: "Mentorship", body: "Guidance from people a step ahead" },
  { icon: Award, title: "AP courses", body: `${apCount} subjects, unit by unit` },
  { icon: Languages, title: "IELTS", body: "Writing and Speaking practice" },
  { icon: Sparkles, title: "Free", body: "No paywall on the essentials" },
];

function ValueStrip() {
  return (
    <Reveal delay={0.5}>
      <ul className="mt-16 grid gap-x-8 gap-y-6 border-t border-border/60 pt-8 sm:grid-cols-2 lg:mt-20 lg:grid-cols-5">
        {valueStrip(useAp().live.length).map((v) => (
          <li key={v.title} className="flex items-start gap-3">
            <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
              <v.icon className="h-4 w-4" />
            </span>
            <div>
              <p className="text-[15px] font-medium leading-snug">{v.title}</p>
              <p className="mt-0.5 text-[13px] leading-snug text-muted-foreground">{v.body}</p>
            </div>
          </li>
        ))}
      </ul>
    </Reveal>
  );
}

/* -------------------------------------------------------------------------- */
/* 2. Programmes                                                               */
/* -------------------------------------------------------------------------- */

/**
 * `label` is a cadence/status badge and is the only claim each card makes about
 * how established a programme is. Anything that has not launched must read
 * "Coming soon"; move a card to a real cadence only once it is running.
 */
const programmes = (apCount: number) => [
  {
    icon: FlaskConical,
    title: "Student Research",
    body: "Propose a research question in any field, get paired with a mentor, do the work, and finish with a paper in your own name.",
    label: "Applications open",
    href: "#research",
    tint: "bg-[hsl(190_84%_42%)]/10 text-[hsl(190_84%_42%)]",
    chip: "border-[hsl(190_84%_42%)]/30 text-[hsl(190_84%_42%)]",
  },
  {
    icon: UserRound,
    title: "Mentorship",
    body: "Book free 1-on-1 sessions with mentors, or apply to become a peer mentor and help the students coming after you.",
    label: "Free 1-on-1",
    href: "/onboarding",
    tint: "bg-primary/10 text-primary",
    chip: "border-primary/25 text-primary",
  },
  {
    icon: Award,
    title: "AP Courses",
    body: `${apCount} AP subjects, practised unit by unit and topic by topic, with an explanation on every question and full practice tests.`,
    label: `${apCount} subjects live`,
    href: "#courses",
    tint: "bg-success/10 text-success",
    chip: "border-success/30 text-success",
  },
  {
    icon: Languages,
    title: "IELTS Preparation",
    body: "Writing and Speaking practice with band-scored feedback, whole-mark criteria, cue cards, and a leaderboard.",
    label: "Live now",
    href: "/onboarding",
    tint: "bg-[hsl(266_84%_60%)]/10 text-[hsl(266_84%_60%)]",
    chip: "border-[hsl(266_84%_60%)]/30 text-[hsl(266_84%_60%)]",
  },
  {
    icon: Wallet,
    title: "Financial Literacy",
    body: "How money, inflation, interest rates, banking and investing actually affect everyday life, taught in live classes.",
    label: "Monthly",
    href: "/onboarding",
    tint: "bg-warning/15 text-warning",
    chip: "border-warning/30 text-warning",
  },
  {
    icon: GraduationCap,
    title: "Learn From Experts",
    body: "Guest lectures and conversations with university professors and other experts, bringing real academic perspectives to students.",
    label: "Coming soon",
    href: "/onboarding",
    tint: "bg-[hsl(340_78%_56%)]/10 text-[hsl(340_78%_56%)]",
    chip: "border-[hsl(340_78%_56%)]/30 text-[hsl(340_78%_56%)]",
  },
];

function Programmes() {
  const { live } = useAp();
  return (
    <section id="programmes" className="scroll-mt-24 py-20 sm:py-24 lg:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <SectionHeading
          label="What you can do here"
          icon={Sparkles}
          title="One community, many ways to grow."
          body="Scholarly is a free academic community. Do original research, learn from mentors, study AP subjects, prepare for IELTS, and build financial literacy, all with one account."
        />

        <RevealGroup className="mx-auto mt-12 grid max-w-6xl gap-4 sm:grid-cols-2 lg:grid-cols-3" delay={0.05}>
          {programmes(live.length).map((p) => (
            <RevealItem key={p.title}>
              <HoverLift className="h-full">
                <Link
                  href={p.href}
                  className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-6 shadow-soft transition-shadow hover:shadow-card focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                >
                  <div className="flex items-center justify-between gap-3">
                    <span
                      className={cn(
                        "flex h-10 w-10 items-center justify-center rounded-xl transition-transform duration-300 group-hover:-rotate-6 group-hover:scale-110",
                        p.tint,
                      )}
                    >
                      <p.icon className="h-[18px] w-[18px]" />
                    </span>
                    <span
                      className={cn(
                        "rounded-full border px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.1em]",
                        p.chip,
                      )}
                    >
                      {p.label}
                    </span>
                  </div>
                  <h3 className="mt-4 font-display text-lg font-semibold tracking-tight">{p.title}</h3>
                  <p className="mt-2 text-[14px] leading-relaxed text-muted-foreground">{p.body}</p>
                </Link>
              </HoverLift>
            </RevealItem>
          ))}
        </RevealGroup>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 3. Research                                                                 */
/* -------------------------------------------------------------------------- */

const RESEARCH_STEPS = [
  {
    icon: PenLine,
    title: "Propose a topic",
    body: "Submit a research question you genuinely care about, in any field. A paragraph of motivation is enough.",
  },
  {
    icon: Users,
    title: "Get paired with a mentor",
    body: "Accepted proposals are matched with a mentor who helps you scope the question and design the work.",
  },
  {
    icon: Microscope,
    title: "Do the research",
    body: "You run the project with guidance: the reading, the data, the method, the writing.",
  },
  {
    icon: BookOpen,
    title: "Finish the paper",
    body: "You finish with a written paper in your own name, ready to show universities.",
  },
];

function Research() {
  return (
    <section
      id="research"
      className="relative scroll-mt-20 overflow-hidden border-y border-border/60 bg-secondary/25 py-20 sm:py-28"
    >
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="grid items-start gap-12 lg:grid-cols-[0.9fr_1.1fr] lg:gap-16">
          <div>
            <SectionHeading
              align="left"
              icon={FlaskConical}
              label="The research programme"
              title="Ask a real question. Answer it properly."
              body="Universities notice students who have done original work. The programme takes a question you care about from a first paragraph to a finished paper, with a mentor beside you."
            />
            <Reveal delay={0.2}>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <Button className="h-11 rounded-full px-6" asChild>
                  <Link href="/onboarding">
                    Propose a project <ArrowRight className="h-4 w-4" />
                  </Link>
                </Button>
              </div>
            </Reveal>
          </div>

          <RevealGroup className="grid gap-4 sm:grid-cols-2" stagger={0.08}>
            {RESEARCH_STEPS.map((s, i) => (
              <RevealItem key={s.title}>
                <div className="h-full rounded-2xl border border-border/70 bg-card p-5 shadow-soft">
                  <div className="flex items-center gap-3">
                    <span className="font-display text-sm font-semibold text-primary">0{i + 1}</span>
                    <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-[hsl(190_84%_42%)]/10 text-[hsl(190_84%_42%)]">
                      <s.icon className="h-4 w-4" />
                    </span>
                  </div>
                  <h3 className="mt-4 font-display text-lg font-semibold tracking-tight">{s.title}</h3>
                  <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">{s.body}</p>
                </div>
              </RevealItem>
            ))}
          </RevealGroup>
        </div>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 4. AP courses                                                               */
/* -------------------------------------------------------------------------- */

const COURSE_POINTS = [
  { icon: Layers, title: "Unit by unit", body: "Every course follows its official unit outline, topic by topic." },
  { icon: CheckCircle2, title: "Explained answers", body: "Each question carries a written explanation of why the answer is right." },
  { icon: ClipboardList, title: "Practice tests", body: "Full AP practice tests, scored when you finish." },
];

function Courses() {
  const { live, plannedCount } = useAp();
  return (
    <section id="courses" className="scroll-mt-20 py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <SectionHeading
          label="AP courses"
          icon={Award}
          title="Study AP subjects the way the course is taught."
          body={`${live.length} AP subjects are live today, with ${plannedCount} more on the way. Pick the ones you take and practise them unit by unit.`}
        />

        <Reveal delay={0.1}>
          <ul className="mx-auto mt-10 flex max-w-4xl flex-wrap justify-center gap-2.5">
            {live.map((s) => (
              <li key={s.code} className="rounded-full border border-border/70 bg-card px-4 py-2 text-sm font-medium shadow-soft">
                {shortName(s.name)}
              </li>
            ))}
          </ul>
        </Reveal>

        <RevealGroup className="mx-auto mt-12 grid max-w-5xl gap-4 sm:grid-cols-3" stagger={0.07}>
          {COURSE_POINTS.map((p) => (
            <RevealItem key={p.title}>
              <div className="h-full rounded-xl border border-border/70 bg-card p-5 shadow-soft">
                <p.icon className="h-5 w-5 text-success" />
                <h3 className="mt-2.5 text-[15px] font-semibold">{p.title}</h3>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">{p.body}</p>
              </div>
            </RevealItem>
          ))}
        </RevealGroup>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 5. Stats                                                                    */
/* -------------------------------------------------------------------------- */

/**
 * Every number here must be checkable.
 *
 * - AP subjects: counted from the catalog at build time.
 * - AP questions: a floor. The banks held 23,560 by a count of the authored
 *   modules and 25,885 in the database when last measured; "20,000+" is true
 *   under both, and the banks only grow.
 * - 4: the programme's own stages (propose, mentor, research, publish).
 */
const stats = (apCount: number): { value: number; prefix?: string; suffix?: string; label: string }[] => [
  { value: apCount, label: "AP subjects live" },
  { value: 20000, suffix: "+", label: "AP practice questions, all explained" },
  { value: 4, label: "Stages from proposal to finished paper" },
  { value: 0, prefix: "$", label: "To join" },
];

function Stats() {
  const { live } = useAp();
  return (
    <section className="border-y border-border/60 bg-secondary/25 py-16 sm:py-20">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <RevealGroup className="grid grid-cols-2 gap-6 sm:gap-10 lg:grid-cols-4">
          {stats(live.length).map((s) => (
            <RevealItem key={s.label}>
              <div className="text-center">
                <p className="bg-gradient-to-br from-primary to-[hsl(190_84%_42%)] bg-clip-text font-display text-3xl font-semibold tracking-tight text-transparent sm:text-4xl">
                  <CountUp value={s.value} prefix={s.prefix} suffix={s.suffix} />
                </p>
                <p className="mt-1.5 text-sm text-muted-foreground">{s.label}</p>
              </div>
            </RevealItem>
          ))}
        </RevealGroup>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 6. Streak                                                                   */
/* -------------------------------------------------------------------------- */

const STREAK_DAYS = ["M", "T", "W", "T", "F", "S", "S"];

function StreakBand() {
  return (
    <section className="mx-auto w-full max-w-7xl px-4 pt-16 sm:px-6 sm:pt-20 lg:px-8">
      <Reveal direction="up">
        <div className="relative overflow-hidden rounded-2xl border border-primary/25 bg-card/95 shadow-panel backdrop-blur">
          <div
            aria-hidden
            className="pointer-events-none absolute -left-24 -top-24 h-56 w-56 rounded-full bg-primary/15 blur-3xl"
          />
          <div className="relative grid gap-6 p-6 sm:p-7 lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)_minmax(0,1.15fr)] lg:items-center lg:gap-8">
            <div>
              <p className="flex items-center gap-2 font-display text-lg font-semibold">
                <Zap className="h-5 w-5 text-warning" />
                Build a 7-day streak
              </p>
              <p className="mt-0.5 text-sm text-muted-foreground">Seven days in a row is where the habit starts.</p>
              <ul className="mt-4 flex flex-wrap gap-2">
                {STREAK_DAYS.map((label, i) => (
                  <li key={i} className="flex flex-col items-center gap-1">
                    <span className="flex h-8 w-8 items-center justify-center rounded-full border border-dashed border-primary/40 text-xs font-semibold text-primary/60">
                      {label}
                    </span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="lg:border-l lg:border-border/60 lg:pl-8">
              <p className="flex items-center gap-2 text-sm font-medium text-muted-foreground">
                <Star className="h-4 w-4 text-warning" />
                Then aim for
              </p>
              <p className="mt-1 font-display text-2xl font-semibold tabular-nums">14 days</p>
              <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-secondary">
                <div className="h-full w-0 rounded-full bg-gradient-to-r from-primary to-[hsl(190_84%_42%)]" />
              </div>
              <p className="mt-1.5 text-xs tabular-nums text-muted-foreground">
                Your streak starts on your first day of learning
              </p>
            </div>

            <div className="lg:border-l lg:border-border/60 lg:pl-8">
              <p className="flex items-center gap-2 text-sm font-medium">
                <LineChart className="h-4 w-4 text-success" />
                Why streaks work
              </p>
              <p className="mt-1 text-sm text-muted-foreground">Twenty minutes a day beats a whole weekend once a month.</p>
              <Button asChild className="mt-4 w-full sm:w-auto">
                <Link href="/onboarding">
                  Start your streak <ArrowRight className="ml-1.5 h-4 w-4" />
                </Link>
              </Button>
            </div>
          </div>
        </div>
      </Reveal>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 7. SAT — one supplementary section                                          */
/* -------------------------------------------------------------------------- */

const SAT_POINTS = [
  { icon: MonitorPlay, text: "31 full-length practice tests in a Bluebook-style interface" },
  { icon: Layers, text: "Adaptive modules that route like the real Digital SAT" },
  { icon: Zap, text: "A written explanation on every question" },
  { icon: BarChart3, text: "Analytics that show which skills are costing you points" },
  { icon: BookOpen, text: "Vocabulary sets with spaced repetition" },
];

function SatSection() {
  return (
    <section id="sat" className="scroll-mt-20 py-20 sm:py-24">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="grid items-center gap-10 rounded-3xl border border-border/70 bg-card/60 p-6 shadow-soft sm:p-10 lg:grid-cols-[1fr_1.1fr] lg:gap-14">
          <div>
            <SectionLabel icon={CalendarDays}>Also on Scholarly</SectionLabel>
            <h2 className="mt-5 font-display text-2xl font-semibold tracking-tight text-balance sm:text-3xl">
              SAT preparation, when you need it
            </h2>
            <p className="mt-3 text-[15px] leading-relaxed text-muted-foreground">
              Sitting the Digital SAT? The same free account includes a full practice engine.
            </p>
            <ul className="mt-6 space-y-3">
              {SAT_POINTS.map((p) => (
                <li key={p.text} className="flex items-start gap-3">
                  <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-primary/10">
                    <p.icon className="h-3.5 w-3.5 text-primary" />
                  </span>
                  <span className="text-[14px] leading-relaxed text-muted-foreground">{p.text}</span>
                </li>
              ))}
            </ul>
            <p className="mt-6 flex items-start gap-1.5 text-[11.5px] leading-relaxed text-muted-foreground">
              <ShieldCheck className="mt-0.5 h-3.5 w-3.5 shrink-0" />
              Scholarly is independent and not affiliated with or endorsed by the College Board. SAT&reg; and
              Bluebook&trade; are trademarks of their owners, referenced only to describe the exam format.
            </p>
          </div>
          <Reveal direction="left" delay={0.1}>
            <BluebookMockup />
          </Reveal>
        </div>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 8. FAQ                                                                      */
/* -------------------------------------------------------------------------- */

const faqs = ({ live, plannedCount }: ApSummary) => [
  {
    q: "What is Scholarly?",
    a: "A free academic community for students. You can do original research with a mentor through the research programme, book 1-on-1 sessions with mentors, study AP subjects, prepare for IELTS, and join financial literacy classes, all with one account.",
  },
  {
    q: "How does the research programme work?",
    a: "You propose a research question in any field with a short paragraph about why it matters to you. Accepted proposals are paired with a mentor who helps you scope the question and design the work. When the work is done, you finish with a paper in your own name.",
  },
  {
    q: "Which AP subjects are available?",
    a: `${live.map((s) => shortName(s.name)).join(", ")}. ${plannedCount} more subjects are being written now.`,
  },
  {
    q: "Is it really free?",
    a: "Yes. You can create an account and use the research programme, AP practice, IELTS practice and mentorship without entering payment details.",
  },
  {
    q: "Do you offer test preparation?",
    a: "Yes, for IELTS and the SAT. IELTS covers Writing and Speaking with band-scored feedback. SAT preparation includes full-length adaptive practice tests in a Bluebook-style interface, a question bank and analytics.",
  },
  {
    q: "Is Scholarly affiliated with the College Board?",
    a: "No. We are completely independent. SAT® and Bluebook™ are trademarks of the College Board, which does not sponsor or endorse this platform.",
  },
];

function Faq() {
  const ap = useAp();
  return (
    <section id="faq" className="scroll-mt-20 py-20 sm:py-28">
      <div className="mx-auto max-w-3xl px-5 sm:px-8">
        <SectionHeading label="FAQ" icon={ClipboardList} title="Questions, answered" />
        <Reveal delay={0.1}>
          <Accordion type="single" collapsible className="mt-12 w-full">
            {faqs(ap).map((f, i) => (
              <AccordionItem
                key={f.q}
                value={`item-${i}`}
                className="mb-3 rounded-xl border border-border/70 bg-card px-5 shadow-soft transition-shadow data-[state=open]:shadow-card"
              >
                <AccordionTrigger className="text-left text-[15px] font-semibold hover:no-underline">{f.q}</AccordionTrigger>
                <AccordionContent className="text-[15px] leading-relaxed text-muted-foreground">{f.a}</AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </Reveal>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 9. Final CTA                                                                */
/* -------------------------------------------------------------------------- */

function FinalCta() {
  return (
    <section className="relative overflow-hidden py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <Reveal scale={0.97} direction="none">
          <div className="relative overflow-hidden rounded-3xl border border-border/60 bg-navy-950 px-6 py-16 text-center text-white sm:px-12 sm:py-20">
            <div className="pointer-events-none absolute inset-0">
              <div className="absolute inset-0 bg-[radial-gradient(60%_60%_at_50%_0%,hsl(226_84%_56%/0.35),transparent_70%)]" />
              <FloatingBlob className="absolute -bottom-20 left-[20%] h-[300px] w-[300px] rounded-full bg-primary/25 blur-[100px]" />
              <FloatingBlob
                className="absolute -top-16 right-[18%] h-[260px] w-[260px] rounded-full bg-[hsl(190_84%_42%)]/20 blur-[100px]"
                duration={20}
                delay={2}
              />
              <div className="absolute inset-0 bg-[linear-gradient(to_right,rgb(255_255_255/0.04)_1px,transparent_1px),linear-gradient(to_bottom,rgb(255_255_255/0.04)_1px,transparent_1px)] bg-[size:48px_48px] [mask-image:radial-gradient(70%_60%_at_50%_40%,black,transparent)]" />
            </div>

            <div className="relative mx-auto max-w-2xl">
              <h2 className="font-display text-3xl font-semibold tracking-tight text-balance sm:text-5xl sm:leading-[1.08]">
                Start where you want to go
              </h2>
              <p className="mx-auto mt-5 max-w-lg text-[17px] leading-relaxed text-navy-200 text-balance">
                Propose a research project, pick your AP subjects, prepare for IELTS, or book a session with a mentor.
                It is free, and it takes about a minute to join.
              </p>
              <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
                <Button
                  size="lg"
                  className="group h-[52px] w-full rounded-full bg-primary px-8 text-base font-semibold text-white shadow-panel hover:bg-primary-600 sm:w-auto"
                  asChild
                >
                  <Link href="/onboarding">
                    Join Scholarly free
                    <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-0.5" />
                  </Link>
                </Button>
                <Button
                  size="lg"
                  variant="outline"
                  className="h-[52px] w-full rounded-full border-white/20 bg-white/5 px-8 text-base text-white backdrop-blur hover:bg-white/10 hover:text-white sm:w-auto"
                  asChild
                >
                  <Link href="/login">I already have an account</Link>
                </Button>
              </div>
              <p className="mt-6 text-[13px] text-navy-300">Free to join · No credit card · Takes about a minute</p>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* Footer                                                                      */
/* -------------------------------------------------------------------------- */

function Footer() {
  return (
    <footer className="border-t border-border/60 bg-secondary/25">
      <div className="mx-auto max-w-7xl px-5 py-14 sm:px-8">
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
          <div className="lg:col-span-2">
            <Link href="/" className="flex items-center gap-2.5">
              <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-950 text-white">
                <GraduationCap className="h-[18px] w-[18px]" />
              </span>
              <span className="font-display text-[17px] font-semibold tracking-tight">Scholarly</span>
            </Link>
            <p className="mt-4 max-w-sm text-sm leading-relaxed text-muted-foreground">
              A free academic community: student research with mentors, AP courses, IELTS preparation, financial
              literacy, and SAT practice.
            </p>
          </div>

          <div>
            <p className="text-sm font-semibold">Explore</p>
            <ul className="mt-3 space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#research" className="transition-colors hover:text-foreground">
                  Research programme
                </a>
              </li>
              <li>
                <a href="#programmes" className="transition-colors hover:text-foreground">
                  Mentorship
                </a>
              </li>
              <li>
                <a href="#courses" className="transition-colors hover:text-foreground">
                  AP courses
                </a>
              </li>
              <li>
                <a href="#programmes" className="transition-colors hover:text-foreground">
                  IELTS &amp; financial literacy
                </a>
              </li>
              <li>
                <a href="#sat" className="transition-colors hover:text-foreground">
                  SAT preparation
                </a>
              </li>
            </ul>
          </div>

          <div>
            <p className="text-sm font-semibold">Get started</p>
            <ul className="mt-3 space-y-2 text-sm text-muted-foreground">
              <li>
                <Link href="/onboarding" className="transition-colors hover:text-foreground">
                  Create an account
                </Link>
              </li>
              <li>
                <Link href="/login" className="transition-colors hover:text-foreground">
                  Sign in
                </Link>
              </li>
              <li>
                <Link href="/team" className="transition-colors hover:text-foreground">
                  Team
                </Link>
              </li>
              <li>
                <Link href="/schools" className="transition-colors hover:text-foreground">
                  For Schools
                </Link>
              </li>
              <li>
                <a href="#faq" className="transition-colors hover:text-foreground">
                  FAQ
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-12 border-t border-border/60 pt-6">
          <p className="mb-3 flex flex-wrap gap-x-4 gap-y-1 text-xs">
            <Link href="/terms" className="text-muted-foreground hover:text-foreground">
              Terms of Use
            </Link>
            <Link href="/privacy" className="text-muted-foreground hover:text-foreground">
              Privacy Policy
            </Link>
            <a href="mailto:scholarlyhub.space@gmail.com" className="text-muted-foreground hover:text-foreground">
              Contact
            </a>
          </p>
          <p className="text-xs leading-relaxed text-muted-foreground">
            &copy; {new Date().getFullYear()} Scholarly. SAT&reg; is a trademark registered by the College Board, which
            is not affiliated with and does not endorse this platform. Bluebook&trade; is a trademark of the College
            Board. All other marks belong to their respective owners.
          </p>
        </div>
      </div>
    </footer>
  );
}
