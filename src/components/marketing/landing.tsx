"use client";

import Link from "next/link";
import { motion, useReducedMotion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";
import {
  ArrowRight,
  BarChart3,
  BookOpen,
  Brain,
  CheckCircle2,
  ClipboardList,
  FlaskConical,
  GraduationCap,
  Languages,
  Layers,
  LineChart,
  MonitorPlay,
  ShieldCheck,
  Sparkles,
  Star,
  Target,
  Timer,
  Wallet,
  UserRound,
  Zap,
} from "lucide-react";

import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Button } from "@/components/ui/button";
import { SiteNav } from "@/components/marketing/site-nav";
import {
  AdaptiveDiagram,
  AnalyticsMockup,
  BluebookMockup,
  ScorePreviewCard,
  VocabMockup,
} from "@/components/marketing/mockups";
import { CountUp, FloatingBlob, HoverLift, Reveal, RevealGroup, RevealItem } from "@/components/marketing/motion";
import { cn } from "@/lib/utils";

/**
 * Where the "Get My Free SAT Plan" / "Book a session" CTAs point.
 *
 * `/booking` is behind auth, so a signed-out visitor lands on the login page
 * and returns here afterwards — that's the intended funnel for a free service
 * that needs an account anyway.
 */
const PLAN_CTA_HREF = "/booking";

/**
 * `partners` is passed in rather than imported because this is a client
 * component and the partners strip is an async server component that reads the
 * database. Handing it down as a child keeps the query on the server.
 */
export function Landing({ partners }: { partners?: React.ReactNode }) {
  return (
    <div className="min-h-screen overflow-x-clip bg-background">
      <SiteNav />
      <main>
        <Hero />
        {/* Streak and the "what it's for" band sit immediately under the hero,
            so the first scroll shows the product working and the reason to
            bother — before any feature copy. */}
        <div className="space-y-4 pt-2 sm:space-y-5">
          <StreakBand />
          <OpensDoors />
        </div>
        <BeyondSat />
        <Ecosystem />
        <Stats />
        <Features />
        <Experience />
        <Analytics />
        <Adaptive />
        <Vocabulary />
        <Faq />
        {partners}
        <FinalCta />
      </main>
      <Footer />
    </div>
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
  const ref = useRef<HTMLDivElement>(null);
  const reduced = useReducedMotion();
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
  // Gentle parallax only — the split layout already carries the depth, and a
  // strong tilt fights the layered cards overlapping the product window.
  const mockY = useTransform(scrollYProgress, [0, 1], [0, 56]);

  return (
    <section
      ref={ref}
      // `isolate` gives this section its own stacking context. Without it the
      // -z-10 background wrapper escapes to the root and paints BEHIND the page
      // shell's opaque bg-background, which is why the plate was invisible.
      // Purely a paint-order fix: nothing moves, resizes or restyles.
      className="relative isolate overflow-hidden pb-14 pt-28 sm:pt-32 lg:pb-16 lg:pt-32"
    >
      {/* Animated background.
          Layer order inside this existing -z-10 wrapper is paint order, so the
          plate goes first and everything already here keeps sitting on top of
          it. No z-index anywhere else changes, and no foreground UI moves.
            1. hero-plate       — the campus photograph
            2. readability wash — navy, heaviest on the left under the headline
            3. the original radial gradient, blobs and grid
          Dark-only: the theme provider defaults to dark but has enableSystem,
          so a visitor whose OS is set to light still gets the light palette,
          and a dark plate under light-theme type would be unreadable. In light
          mode this renders exactly as it did before. */}
      <div className="pointer-events-none absolute inset-0 -z-10">
        <div className="hero-plate absolute inset-0 hidden dark:block" />
        <div className="hero-wash absolute inset-0 hidden dark:block" />
        <div className="absolute inset-0 bg-[radial-gradient(70%_50%_at_50%_0%,hsl(226_84%_56%/0.10),transparent_70%)]" />
        <FloatingBlob className="absolute -top-24 left-[8%] h-[380px] w-[380px] rounded-full bg-primary/20 blur-[110px]" />
        <FloatingBlob
          className="absolute right-[6%] top-10 h-[420px] w-[420px] rounded-full bg-[hsl(266_84%_60%)]/15 blur-[120px]"
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
      <div className="grid items-center gap-12 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.12fr)] lg:gap-8 xl:gap-10">
        {/* ---------------------------------------------------------------- */}
        {/* Copy column                                                       */}
        {/* ---------------------------------------------------------------- */}
        <div className="text-center lg:text-left">
          <Reveal direction="none" scale={0.96}>
            <span className="inline-flex items-center gap-2 rounded-full border border-border/70 bg-card/70 px-3.5 py-1.5 text-[10px] font-semibold uppercase leading-tight tracking-[0.08em] text-muted-foreground shadow-soft backdrop-blur sm:text-[11.5px] sm:tracking-[0.1em]">
              <span className="flex h-4 w-4 shrink-0 items-center justify-center rounded-full bg-success/15">
                <span className="h-1.5 w-1.5 rounded-full bg-success" />
              </span>
              <span className="text-left">
                Free academic community
                <span className="mx-1.5 text-border">•</span>
                <span className="whitespace-nowrap">Built for ambitious students</span>
              </span>
            </span>
          </Reveal>

          <Reveal delay={0.08}>
            <h1 className="mt-6 font-display text-[2.7rem] font-bold leading-[0.98] tracking-[-0.02em] text-balance sm:text-[3.5rem] lg:text-[3.5rem] xl:text-[4rem]">
              Learn like a scholar.
              <br />
              <span className="text-gradient-animated bg-gradient-to-r from-primary via-[hsl(266_84%_62%)] to-[hsl(320_80%_58%)] bg-[length:200%_auto] bg-clip-text text-transparent">
                SAT, IELTS &amp; beyond.
              </span>
            </h1>
          </Reveal>

          <Reveal delay={0.16}>
            <p className="mx-auto mt-6 max-w-xl text-[17px] leading-relaxed text-muted-foreground text-balance lg:mx-0 lg:text-lg">
              Adaptive SAT practice, full IELTS preparation, financial literacy, and mentorship from real
              scorers — one free academic community, with research programmes on the way.
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
                  Start Practicing — Free
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </Link>
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="h-12 rounded-full border-border/80 px-7 text-[15px] backdrop-blur"
                asChild
              >
                <Link href={PLAN_CTA_HREF}>Get My Free Study Plan</Link>
              </Button>
            </div>
          </Reveal>

          <Reveal delay={0.32}>
            <ul className="mt-5 flex flex-wrap items-center justify-center gap-x-5 gap-y-2 text-[13px] text-muted-foreground lg:justify-start">
              {["No credit card", "Setup in 60 seconds", "100% free core features"].map((t) => (
                <li key={t} className="flex items-center gap-1.5">
                  <CheckCircle2 className="h-3.5 w-3.5 shrink-0 text-success" />
                  {t}
                </li>
              ))}
            </ul>
          </Reveal>
        </div>

        {/* ---------------------------------------------------------------- */}
        {/* Product showcase column                                           */}
        {/* ---------------------------------------------------------------- */}
        <motion.div style={reduced ? undefined : { y: mockY }} className="relative">
          <div className="absolute -inset-8 -z-10 rounded-[2.5rem] bg-gradient-to-br from-primary/20 via-primary/5 to-transparent blur-3xl" />

          <Reveal direction="none" scale={0.97} duration={0.7}>
            {/* The exam window is the hero of this column: the only element
                allowed to overlap it is the analytics card, and only at a
                corner, so the interface itself stays readable. */}
            <div className="relative">
              <BluebookMockup />

              {/* Anchored bottom-left: the only region of the exam window it
                  covers is the passage's placeholder lines, so no real
                  interface content is hidden behind it. */}
              <Reveal
                delay={0.45}
                direction="up"
                className="absolute -bottom-12 -left-4 hidden sm:block lg:-left-10"
              >
                <ScorePreviewCard />
              </Reveal>
            </div>
          </Reveal>

          {/* 1580 mentorship card. Tucked UNDER the exam window rather than
              stacked below it: the negative margin lets the window overlap its
              top edge, which is what gives the column depth instead of reading
              as two separate boxes with a gap between them. -z-10 keeps it
              behind the window; pt compensates so its own text is never
              covered. */}
          <Reveal delay={0.58} direction="up" className="relative -z-10 -mt-10 pt-16 sm:-mt-14 sm:pt-20 lg:-mt-16 lg:pt-28">
            <MentorshipCard className="sm:max-w-[380px] lg:max-w-none" />
          </Reveal>
        </motion.div>
        </div>

        {/* Value strip — spans both columns, so it reads as a summary of the
            whole hero on desktop and lands last in the mobile stack. */}
        <ValueStrip />
      </div>
    </section>
  );
}

const VALUE_STRIP = [
  { icon: Layers, title: "Adaptive Practice", body: "Questions adjust to you in real time" },
  { icon: Target, title: "Targeted Practice", body: "Focus on your weakest skills first" },
  { icon: BarChart3, title: "Smart Analytics", body: "See exactly what to fix and why" },
  { icon: UserRound, title: "Personalized Plan", body: "A study plan built around your goals" },
  { icon: Sparkles, title: "100% Free", body: "Core learning features are always free" },
];

function ValueStrip() {
  return (
    <Reveal delay={0.5}>
      <ul className="mt-16 grid gap-x-8 gap-y-6 border-t border-border/60 pt-8 sm:grid-cols-2 lg:mt-20 lg:grid-cols-5">
        {VALUE_STRIP.map((v) => (
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

/**
 * The streak goal.
 *
 * Framed as something to reach, not something the visitor already has. A
 * logged-out student has no streak, so "7 Day Streak! You're on fire!" would
 * be describing a stranger — and "Continue practising" would be inviting them
 * to continue something they never started. Everything here is written in the
 * second person future: this is what you are aiming at.
 */
const STREAK_DAYS = ["M", "T", "W", "T", "F", "S", "S"];

function StreakBand() {
  return (
    <section className="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
      <Reveal direction="up">
        <div className="relative overflow-hidden rounded-2xl border border-primary/25 bg-card/95 shadow-panel backdrop-blur">
          {/* Same corner glow language as the hero's mockup frame. */}
          <div
            aria-hidden
            className="pointer-events-none absolute -left-24 -top-24 h-56 w-56 rounded-full bg-primary/15 blur-3xl"
          />

          <div className="relative grid gap-6 p-6 sm:p-7 lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)_minmax(0,1.15fr)] lg:items-center lg:gap-8">
            {/* The goal, with an empty week to fill in */}
            <div>
              <p className="flex items-center gap-2 font-display text-lg font-semibold">
                <Zap className="h-5 w-5 text-warning" />
                Build a 7-day streak
              </p>
              <p className="mt-0.5 text-sm text-muted-foreground">
                Seven days in a row is where the habit starts.
              </p>
              <ul className="mt-4 flex flex-wrap gap-2">
                {STREAK_DAYS.map((label, i) => (
                  <li key={i} className="flex flex-col items-center gap-1">
                    {/* Outlined, not filled: nothing has been earned yet. */}
                    <span className="flex h-8 w-8 items-center justify-center rounded-full border border-dashed border-primary/40 text-xs font-semibold text-primary/60">
                      {label}
                    </span>
                  </li>
                ))}
              </ul>
            </div>

            {/* What comes after */}
            <div className="lg:border-l lg:border-border/60 lg:pl-8">
              <p className="flex items-center gap-2 text-sm font-medium text-muted-foreground">
                <Star className="h-4 w-4 text-warning" />
                Then aim for
              </p>
              <p className="mt-1 font-display text-2xl font-semibold tabular-nums">14 days</p>
              <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-secondary">
                <div className="h-full w-0 rounded-full bg-gradient-to-r from-primary to-[hsl(266_84%_60%)]" />
              </div>
              <p className="mt-1.5 text-xs tabular-nums text-muted-foreground">
                Your streak starts on your first day of practice
              </p>
            </div>

            {/* Why it matters + CTA */}
            <div className="lg:border-l lg:border-border/60 lg:pl-8">
              <p className="flex items-center gap-2 text-sm font-medium">
                <LineChart className="h-4 w-4 text-success" />
                Why streaks work
              </p>
              <p className="mt-1 text-sm text-muted-foreground">
                Twenty minutes a day beats cramming the week before the test.
              </p>
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

/**
 * "The SAT opens doors".
 *
 * Deliberately typeset names rather than university logos. Reproducing a
 * university's wordmark on a commercial-looking page implies a partnership or
 * endorsement that does not exist; naming them in a factual sentence about
 * what SAT scores are used for does not. The caption is worded to make the
 * claim about the test, never about Scholarly.
 */
const UNIVERSITIES = [
  "Harvard",
  "Yale",
  "Stanford",
  "Columbia",
  "NYU",
  "Chicago",
  "Penn",
  "MIT",
];

function OpensDoors() {
  return (
    <section className="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
      <Reveal direction="up">
        <div className="rounded-2xl border border-border/60 bg-card/60 px-6 py-7 backdrop-blur sm:px-8">
          <p className="text-center font-display text-lg font-semibold">Strong scores open doors.</p>
          <p className="mx-auto mt-1 max-w-xl text-center text-sm text-muted-foreground">
            An SAT score, an IELTS band — these are among the few things a student anywhere in the
            world can control, and they are read by admissions offices everywhere.
          </p>
          <ul className="mt-6 flex flex-wrap items-center justify-center gap-x-8 gap-y-4">
            {UNIVERSITIES.map((u) => (
              <li
                key={u}
                className="font-display text-base font-semibold tracking-wide text-muted-foreground/80 transition-colors hover:text-foreground"
              >
                {u}
              </li>
            ))}
            <li className="text-sm text-muted-foreground">+ many more</li>
          </ul>
        </div>
      </Reveal>
    </section>
  );
}

/** Reusable 1580-scorer guidance card (hero + "beyond the SAT" section). */
function MentorshipCard({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "rounded-2xl border border-primary/25 bg-card/95 p-4 shadow-panel backdrop-blur",
        className
      )}
    >
      <div className="flex flex-wrap items-center gap-x-4 gap-y-3">
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-primary/10">
          <UserRound className="h-4 w-4 text-primary" />
        </span>

        <div className="min-w-[190px] flex-1">
          <p className="text-[10px] font-semibold uppercase tracking-[0.1em] text-primary">
            Free 1-on-1 guidance
          </p>
          <p className="mt-1 text-[15px] font-medium leading-snug text-balance">
            Personalized SAT plan from a 1580 scorer
          </p>
        </div>

        <Link
          href={PLAN_CTA_HREF}
          className="group inline-flex shrink-0 items-center gap-1 text-[13px] font-medium text-primary transition-colors hover:text-primary/80"
        >
          Book a session
          <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
        </Link>
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* 2. More than test prep                                                      */
/* -------------------------------------------------------------------------- */

/**
 * The four pillars of the wider platform.
 *
 * `label` is a cadence/status badge and is the only claim each card makes about
 * how established a programme is — no attendee counts, named professors or
 * partnerships. Anything that hasn't launched must read "COMING SOON"; move a
 * card to a real cadence only once it is actually running.
 */
const PILLARS = [
  {
    icon: LineChart,
    title: "Weekly SAT Analysis",
    body: "Break down difficult questions, understand common mistakes, and learn how to approach the SAT more effectively.",
    label: "Every week",
    tint: "bg-primary/10 text-primary",
    chip: "border-primary/25 text-primary",
  },
  {
    icon: Languages,
    title: "IELTS Preparation",
    body: "Full Writing and Speaking practice with band-scored feedback, whole-mark criteria, cue cards, and a leaderboard — the same account, the same community.",
    label: "Live now",
    tint: "bg-[hsl(266_84%_60%)]/10 text-[hsl(266_84%_60%)]",
    chip: "border-[hsl(266_84%_60%)]/30 text-[hsl(266_84%_60%)]",
  },
  {
    icon: Wallet,
    title: "Financial Literacy",
    body: "Learn how money, inflation, interest rates, banking, investing, and the economy actually affect your everyday life.",
    label: "Monthly",
    tint: "bg-warning/15 text-warning",
    chip: "border-warning/30 text-warning",
  },
  {
    icon: FlaskConical,
    title: "Student Research",
    body: "Research programmes where students investigate real questions with guidance from mentors — and build the kind of work universities actually notice.",
    label: "Coming soon",
    tint: "bg-[hsl(190_84%_42%)]/10 text-[hsl(190_84%_42%)]",
    chip: "border-[hsl(190_84%_42%)]/30 text-[hsl(190_84%_42%)]",
  },
  {
    icon: GraduationCap,
    title: "Learn From Experts",
    body: "Guest lectures and conversations with university professors and other experts, bringing real academic perspectives directly to students.",
    label: "Coming soon",
    tint: "bg-[hsl(340_78%_56%)]/10 text-[hsl(340_78%_56%)]",
    chip: "border-[hsl(340_78%_56%)]/30 text-[hsl(340_78%_56%)]",
  },
];

function BeyondSat() {
  return (
    <section id="mentorship" className="scroll-mt-24 py-20 sm:py-24 lg:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <SectionHeading
          label="More than test prep"
          icon={Sparkles}
          title="Build skills that go beyond any exam."
          body="Scholarly is a free academic community, not a single test. Prepare for the SAT and IELTS, learn economics and financial literacy, join research programmes and expert lectures, and learn directly from experienced mentors and professors."
        />

        <RevealGroup className="mx-auto mt-12 grid max-w-5xl gap-4 sm:grid-cols-2" delay={0.05}>
          {PILLARS.map((p) => (
            <RevealItem key={p.title}>
              <HoverLift className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-6 shadow-soft">
                <div className="flex items-center justify-between gap-3">
                  <span
                    className={cn(
                      "flex h-10 w-10 items-center justify-center rounded-xl transition-transform duration-300 group-hover:-rotate-6 group-hover:scale-110",
                      p.tint
                    )}
                  >
                    <p.icon className="h-[18px] w-[18px]" />
                  </span>
                  <span
                    className={cn(
                      "rounded-full border px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.1em]",
                      p.chip
                    )}
                  >
                    {p.label}
                  </span>
                </div>
                <h3 className="mt-4 font-display text-lg font-semibold tracking-tight">{p.title}</h3>
                <p className="mt-2 text-[14px] leading-relaxed text-muted-foreground">{p.body}</p>
              </HoverLift>
            </RevealItem>
          ))}

          {/* Fourth card carries the differentiator, so it gets the primary
              tint and the only CTA — enough to lead the eye without turning
              the grid into an ad. */}
          <RevealItem>
            <HoverLift className="flex h-full flex-col rounded-2xl border border-primary/30 bg-gradient-to-br from-primary/[0.06] to-card p-6 shadow-card">
              <div className="flex items-center justify-between gap-3">
                <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                  <UserRound className="h-[18px] w-[18px]" />
                </span>
                <span className="rounded-full bg-primary/10 px-2.5 py-1 text-[10px] font-semibold uppercase tracking-[0.1em] text-primary">
                  Free 1-on-1
                </span>
              </div>

              <h3 className="mt-4 font-display text-lg font-semibold tracking-tight">Your Own Study Plan</h3>
              <p className="mt-2 text-[14px] leading-relaxed text-muted-foreground">
                Get personalized guidance from a 1580 SAT scorer and build a study plan around your score, target,
                timeline, and weaknesses.
              </p>

              <Link
                href={PLAN_CTA_HREF}
                className="group mt-5 inline-flex w-fit items-center gap-1.5 rounded-full bg-primary px-4 py-2 text-[14px] font-medium text-primary-foreground transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
              >
                Get a Free Plan
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </Link>
            </HoverLift>
          </RevealItem>
        </RevealGroup>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 3. Ecosystem / "trusted by"                                                 */
/* -------------------------------------------------------------------------- */

const ECOSYSTEM = [
  { name: "College Board", sub: "Digital SAT" },
  { name: "Bluebook", sub: "Test interface" },
  { name: "Khan Academy", sub: "Official practice" },
  { name: "Digital SAT", sub: "2024 format" },
  { name: "Desmos", sub: "Graphing calculator" },
];

function Ecosystem() {
  return (
    <section className="border-y border-border/60 bg-secondary/25 py-14">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <Reveal>
          <p className="text-center text-[13px] font-medium uppercase tracking-[0.14em] text-muted-foreground">
            SAT practice built around the official Digital SAT ecosystem
          </p>
        </Reveal>

        <Reveal delay={0.08}>
          {/* The track holds the list twice — the animation slides one full
              copy's width and loops, so the strip scrolls forever. aria-hidden
              on the duplicate keeps screen readers from reading it twice. */}
          <div className="marquee mt-8">
            <div className="marquee-track items-center">
              {[false, true].map((dup) => (
                <div
                  key={dup ? "dup" : "main"}
                  aria-hidden={dup || undefined}
                  className="flex items-center gap-x-14 pr-14"
                >
                  {ECOSYSTEM.map((e) => (
                    <div key={e.name} className="text-center opacity-70 transition-opacity hover:opacity-100">
                      <p className="whitespace-nowrap font-display text-lg font-semibold tracking-tight sm:text-xl">
                        {e.name}
                      </p>
                      <p className="whitespace-nowrap text-[11px] text-muted-foreground">{e.sub}</p>
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </Reveal>

        <Reveal delay={0.15}>
          <p className="mx-auto mt-9 max-w-2xl text-center text-xs leading-relaxed text-muted-foreground">
            <ShieldCheck className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
            Scholarly is an independent study platform. We are not affiliated with, authorized by, or endorsed by the
            College Board, Khan Academy, or Desmos. SAT&reg; and Bluebook&trade; are trademarks of their respective
            owners and are referenced here only to describe the exam format our practice material follows.
          </p>
        </Reveal>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 3. Stats                                                                    */
/* -------------------------------------------------------------------------- */

/**
 * Every number here must be checkable against the database.
 *
 * This block previously carried "+180 pts average practice gain" and "98%
 * Bluebook layout parity". Neither was measured — the platform has never had
 * enough completed tests to compute a score gain, and the parity figure was a
 * number with no method behind it. An invented statistic on a landing page is a
 * false advertising claim, and it is also the easiest thing for a sceptical
 * student to catch, which costs more trust than the claim ever bought.
 */
const STATS: { value: number; prefix?: string; suffix?: string; label: string }[] = [
  { value: 31, label: "Full-length practice tests" },
  // A floor, not a snapshot. The exact count was 4,605 when this was written and
  // only ever grows as content is added, so a "+" keeps the claim true without
  // needing a code change every time questions are authored.
  { value: 4600, suffix: "+", label: "Questions, every one explained" },
  { value: 27, label: "Questions per R&W module" },
  { value: 1600, label: "Point scale, fully modelled" },
];

function Stats() {
  return (
    <section className="py-16 sm:py-20">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <RevealGroup className="grid grid-cols-2 gap-6 sm:gap-10 lg:grid-cols-4">
          {STATS.map((s) => (
            <RevealItem key={s.label}>
              <div className="text-center">
                <p className="bg-gradient-to-br from-primary to-[hsl(266_84%_60%)] bg-clip-text font-display text-3xl font-semibold tracking-tight text-transparent sm:text-4xl">
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
/* 4. Features                                                                 */
/* -------------------------------------------------------------------------- */

const FEATURES = [
  {
    icon: MonitorPlay,
    title: "Bluebook-accurate interface",
    tint: "bg-primary/10 text-primary",
    body: "The same two-panel layout, annotation tools, cross-out, question menu and review page — down to the colours and spacing. Test day should feel like a Tuesday.",
    accent: "from-primary/15 to-primary/0",
  },
  {
    icon: Layers,
    title: "Real adaptive modules",
    tint: "bg-[hsl(266_84%_60%)]/10 text-[hsl(266_84%_60%)]",
    body: "Module 2 routes to easy or hard based on your Module 1 performance, using the same threshold logic as the real exam. Your score means what it says.",
    accent: "from-[hsl(266_84%_60%)]/15 to-transparent",
  },
  {
    icon: Zap,
    title: "Instant explanations",
    tint: "bg-warning/15 text-warning",
    body: "Every question carries a written explanation, why the right answer works, and the trap the other three were setting.",
    accent: "from-warning/15 to-transparent",
  },
  {
    icon: BarChart3,
    title: "Performance analytics",
    tint: "bg-success/10 text-success",
    body: "Score trends, per-domain accuracy, pacing, and a predicted total that updates with every session you finish.",
    accent: "from-success/15 to-transparent",
  },
  {
    icon: Target,
    title: "Mistake tracking",
    tint: "bg-destructive/10 text-destructive",
    body: "Every miss is filed by skill and revisited. Guessed answers and changed answers are flagged separately, because they are different problems.",
    accent: "from-destructive/15 to-transparent",
  },
  {
    icon: BookOpen,
    title: "Vocabulary system",
    tint: "bg-[hsl(190_84%_42%)]/10 text-[hsl(190_84%_42%)]",
    body: "Spaced repetition over the words the Digital SAT actually tests — plus any word you add yourself.",
    accent: "from-[hsl(190_84%_50%)]/15 to-transparent",
  },
];

function Features() {
  return (
    <section id="features" className="scroll-mt-20 py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <SectionHeading
          label="Why Scholarly"
          icon={Sparkles}
          title="Everything you need, nothing you don't"
          body="Six systems that work together — so practice actually converts into points instead of hours."
        />

        <RevealGroup className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3" stagger={0.07}>
          {FEATURES.map((f) => (
            <RevealItem key={f.title}>
              <HoverLift className="h-full">
                <div className="group relative h-full overflow-hidden rounded-2xl border border-border/70 bg-card p-6 shadow-soft transition-shadow hover:shadow-card">
                  <div
                    className={cn(
                      "absolute inset-x-0 top-0 h-24 bg-gradient-to-b opacity-0 transition-opacity duration-300 group-hover:opacity-100",
                      f.accent
                    )}
                  />
                  <div className="relative">
                    <span
                      className={cn(
                        "flex h-11 w-11 items-center justify-center rounded-xl transition-transform duration-300 group-hover:-rotate-6 group-hover:scale-110",
                        f.tint
                      )}
                    >
                      <f.icon className="h-5 w-5" />
                    </span>
                    <h3 className="mt-4 font-display text-lg font-semibold tracking-tight">{f.title}</h3>
                    <p className="mt-2 text-[15px] leading-relaxed text-muted-foreground">{f.body}</p>
                  </div>
                </div>
              </HoverLift>
            </RevealItem>
          ))}
        </RevealGroup>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 5. Experience — text left, mockup right                                     */
/* -------------------------------------------------------------------------- */

const EXPERIENCE_POINTS = [
  "Two-panel passage and question layout with a draggable divider",
  "Highlights and notes that survive navigation, in three colours",
  "Cross-out eliminator, Mark for Review, and the Question Menu popup",
  "Desmos graphing calculator and the official reference sheet on Math",
  "Countdown timer with hide/show, plus the Check Your Work review page",
];

function Experience() {
  return (
    <section
      id="experience"
      className="relative scroll-mt-20 overflow-hidden border-y border-border/60 bg-secondary/25 py-20 sm:py-28"
    >
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="grid items-center gap-12 lg:grid-cols-2 lg:gap-16">
          <div>
            <SectionHeading
              align="left"
              icon={MonitorPlay}
              label="The test engine"
              title="It doesn't look like Bluebook. It behaves like it."
              body="We rebuilt the Digital SAT interface component by component — the layout, the tools, the wording, the exact greys. Nothing about test day should be a surprise."
            />

            <RevealGroup className="mt-8 space-y-3.5" stagger={0.06}>
              {EXPERIENCE_POINTS.map((p) => (
                <RevealItem key={p}>
                  <div className="flex items-start gap-3">
                    <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-primary/10">
                      <CheckCircle2 className="h-3.5 w-3.5 text-primary" />
                    </span>
                    <p className="text-[15px] leading-relaxed text-muted-foreground">{p}</p>
                  </div>
                </RevealItem>
              ))}
            </RevealGroup>

            <Reveal delay={0.2}>
              <Button className="mt-9 h-11 rounded-full px-6" asChild>
                <Link href="/onboarding">
                  Try a full module <ArrowRight className="h-4 w-4" />
                </Link>
              </Button>
            </Reveal>
          </div>

          <Reveal direction="left" delay={0.1}>
            <div className="relative">
              <div className="absolute -inset-5 -z-10 rounded-[2rem] bg-gradient-to-tr from-primary/15 via-transparent to-[hsl(266_84%_60%)]/15 blur-2xl" />
              <BluebookMockup />
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 6. Analytics — mockup left, text right                                      */
/* -------------------------------------------------------------------------- */

const ANALYTICS_POINTS = [
  {
    icon: LineChart,
    title: "Predicted score",
    body: "A running 1600-scale projection built from your real answer history, not a vibe.",
  },
  {
    icon: Target,
    title: "Weak skill surfacing",
    body: "The three domains costing you the most points, ranked, with practice queued behind them.",
  },
  {
    icon: Timer,
    title: "Pacing analysis",
    body: "Time per question against the pace you need to finish — per module, per skill.",
  },
  {
    icon: ClipboardList,
    title: "Mistake ledger",
    body: "Every miss categorised, with guessed and changed answers tracked separately.",
  },
];

function Analytics() {
  return (
    <section id="analytics" className="scroll-mt-20 py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="grid items-center gap-12 lg:grid-cols-2 lg:gap-16">
          <Reveal direction="right" className="order-2 lg:order-1">
            <div className="relative">
              <div className="absolute -inset-5 -z-10 rounded-[2rem] bg-gradient-to-br from-success/15 via-transparent to-primary/15 blur-2xl" />
              <AnalyticsMockup />
            </div>
          </Reveal>

          <div className="order-1 lg:order-2">
            <SectionHeading
              align="left"
              icon={BarChart3}
              label="Analytics"
              title="Stop guessing what to study"
              body="Most students practise what they're already good at. Scholarly points at the thing that's actually costing you points."
            />

            <RevealGroup className="mt-8 grid gap-4 sm:grid-cols-2" stagger={0.07}>
              {ANALYTICS_POINTS.map((p) => (
                <RevealItem key={p.title}>
                  <div className="h-full rounded-xl border border-border/70 bg-card p-4 shadow-soft">
                    <p.icon className="h-5 w-5 text-primary" />
                    <h3 className="mt-2.5 text-[15px] font-semibold">{p.title}</h3>
                    <p className="mt-1 text-sm leading-relaxed text-muted-foreground">{p.body}</p>
                  </div>
                </RevealItem>
              ))}
            </RevealGroup>
          </div>
        </div>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 7. Adaptive — dark timeline + diagram                                       */
/* -------------------------------------------------------------------------- */

const ADAPTIVE_STEPS = [
  {
    n: "01",
    title: "Module 1",
    body: "Everyone sees the same mixed-difficulty module. Your performance here is the only thing that matters for routing.",
  },
  {
    n: "02",
    title: "The threshold",
    body: "Cross it and Module 2 gets harder. Miss it and Module 2 stays easy — and quietly caps your section score.",
  },
  {
    n: "03",
    title: "Module 2",
    body: "Hard-module questions carry more scoring weight. This is where 700+ sections are actually won.",
  },
  {
    n: "04",
    title: "Your score",
    body: "Scaled on the same routing rules as the real exam, so your practice number is one you can trust.",
  },
];

function Adaptive() {
  return (
    <section className="relative overflow-hidden border-y border-border/60 bg-navy-950 py-20 text-white sm:py-28">
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute inset-0 bg-[radial-gradient(60%_50%_at_50%_0%,hsl(226_84%_56%/0.28),transparent_70%)]" />
        <FloatingBlob className="absolute bottom-0 left-[15%] h-[320px] w-[320px] rounded-full bg-primary/20 blur-[120px]" />
      </div>

      <div className="relative mx-auto max-w-7xl px-5 sm:px-8">
        <div className="mx-auto max-w-2xl text-center">
          <Reveal>
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/15 bg-white/5 px-3 py-1 text-xs font-medium text-navy-200 backdrop-blur">
              <Brain className="h-3.5 w-3.5" /> Adaptive testing
            </span>
          </Reveal>
          <Reveal delay={0.06}>
            <h2 className="mt-5 font-display text-3xl font-semibold tracking-tight text-balance sm:text-4xl lg:text-[2.75rem] lg:leading-[1.1]">
              The part most practice tests fake
            </h2>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="mt-4 text-[17px] leading-relaxed text-navy-200 text-balance">
              The Digital SAT is section-adaptive. If a practice platform ignores that, its scores are fiction. Ours
              routes exactly like the real thing.
            </p>
          </Reveal>
        </div>

        <RevealGroup className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4" stagger={0.09}>
          {ADAPTIVE_STEPS.map((s, i) => (
            <RevealItem key={s.n}>
              <div className="relative h-full rounded-2xl border border-white/10 bg-white/[0.04] p-5 backdrop-blur">
                {i < ADAPTIVE_STEPS.length - 1 && (
                  <span className="absolute -right-3 top-1/2 hidden h-px w-6 bg-gradient-to-r from-white/25 to-transparent lg:block" />
                )}
                <p className="font-display text-sm font-semibold text-primary-300">{s.n}</p>
                <h3 className="mt-2 font-display text-lg font-semibold">{s.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-navy-200">{s.body}</p>
              </div>
            </RevealItem>
          ))}
        </RevealGroup>

        <Reveal delay={0.2}>
          <div className="mx-auto mt-12 max-w-3xl text-foreground">
            <AdaptiveDiagram />
          </div>
        </Reveal>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 8. Vocabulary — card left, text right                                       */
/* -------------------------------------------------------------------------- */

const VOCAB_POINTS = [
  { title: "Spaced repetition", body: "An SM-2 style scheduler shows each word right before you'd forget it." },
  { title: "Daily review queue", body: "A finite, achievable stack every day — not an endless list that guilt-trips you." },
  { title: "Memory tracking", body: "Per-word retention, streaks, and the words quietly slipping back out of memory." },
  { title: "Your own words", body: "Add anything you meet in a passage. Private to you, straight into rotation." },
];

function Vocabulary() {
  return (
    <section id="vocabulary" className="scroll-mt-20 py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-5 sm:px-8">
        <div className="grid items-center gap-12 lg:grid-cols-[0.9fr_1.1fr] lg:gap-20">
          <Reveal direction="right">
            <VocabMockup />
          </Reveal>

          <div>
            <SectionHeading
              align="left"
              icon={BookOpen}
              label="Vocabulary"
              title="Words in context, remembered for good"
              body="The Digital SAT tests vocabulary in context, so drilling definitions alone doesn't move the needle. Ours drills the words the way the test asks about them."
            />

            <RevealGroup className="mt-8 space-y-4" stagger={0.07}>
              {VOCAB_POINTS.map((v, i) => (
                <RevealItem key={v.title}>
                  <div className="flex gap-4 rounded-xl border border-border/70 bg-card p-4 shadow-soft">
                    <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-primary/10 font-display text-sm font-semibold text-primary">
                      {i + 1}
                    </span>
                    <div>
                      <h3 className="text-[15px] font-semibold">{v.title}</h3>
                      <p className="mt-0.5 text-sm leading-relaxed text-muted-foreground">{v.body}</p>
                    </div>
                  </div>
                </RevealItem>
              ))}
            </RevealGroup>
          </div>
        </div>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 10. FAQ                                                                     */
/* -------------------------------------------------------------------------- */

const FAQS = [
  {
    q: "Is Scholarly only for the SAT?",
    a: "No. The SAT engine is the most built-out part, but the same free account includes full IELTS preparation — Writing and Speaking practice with band-scored feedback — plus financial literacy sessions and 1-on-1 mentorship. Research programmes and expert lectures are coming next. Pick SAT, IELTS, or both during setup.",
  },
  {
    q: "How close to Bluebook is the test interface really?",
    a: "Close enough that the muscle memory transfers. We match the two-panel layout, the annotation and cross-out tools, the Question Menu, the Check Your Work review page, the button placement and wording, and the actual colour values. It is a rebuild, not a skin — but it is our rebuild, not College Board software.",
  },
  {
    q: "Is the adaptive scoring real?",
    a: "Yes. Module 1 performance is measured against a configurable threshold, and Module 2 routes to the easy or hard form accordingly. Section scores are scaled with the routing taken into account, which is why a capped easy module cannot produce a top score here — same as the real exam.",
  },
  {
    q: "Is Scholarly affiliated with the College Board?",
    a: "No. We are completely independent. SAT® and Bluebook™ are trademarks of the College Board, which does not sponsor or endorse this platform. We reference them only to describe the exam format our material follows.",
  },
  {
    q: "Do I need to pay to start?",
    a: "No. You can create an account and take a full adaptive practice test without entering payment details.",
  },
  {
    q: "How long does setup take?",
    a: "About a minute. We ask a few questions about your target score, timeline and weak areas first, then build your plan — you only create an account at the end.",
  },
  {
    q: "What if my SAT is in three weeks?",
    a: "Tell us the date during setup. The plan compresses: fewer full-length tests, far more targeted drilling on the specific skills your diagnostic says are costing you the most points.",
  },
];

function Faq() {
  return (
    <section id="faq" className="scroll-mt-20 py-20 sm:py-28">
      <div className="mx-auto max-w-3xl px-5 sm:px-8">
        <SectionHeading label="FAQ" icon={ClipboardList} title="Questions, answered" />

        <Reveal delay={0.1}>
          <Accordion type="single" collapsible className="mt-12 w-full">
            {FAQS.map((f, i) => (
              <AccordionItem
                key={f.q}
                value={`item-${i}`}
                className="mb-3 rounded-xl border border-border/70 bg-card px-5 shadow-soft transition-shadow data-[state=open]:shadow-card"
              >
                <AccordionTrigger className="text-left text-[15px] font-semibold hover:no-underline">
                  {f.q}
                </AccordionTrigger>
                <AccordionContent className="text-[15px] leading-relaxed text-muted-foreground">
                  {f.a}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </Reveal>
      </div>
    </section>
  );
}

/* -------------------------------------------------------------------------- */
/* 11. Final CTA                                                               */
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
                className="absolute -top-16 right-[18%] h-[260px] w-[260px] rounded-full bg-[hsl(266_84%_60%)]/20 blur-[100px]"
                duration={20}
                delay={2}
              />
              <div className="absolute inset-0 bg-[linear-gradient(to_right,rgb(255_255_255/0.04)_1px,transparent_1px),linear-gradient(to_bottom,rgb(255_255_255/0.04)_1px,transparent_1px)] bg-[size:48px_48px] [mask-image:radial-gradient(70%_60%_at_50%_40%,black,transparent)]" />
            </div>

            <div className="relative mx-auto max-w-2xl">
              <h2 className="font-display text-3xl font-semibold tracking-tight text-balance sm:text-5xl sm:leading-[1.08]">
                Your next practice test could be the one that matters
              </h2>
              <p className="mx-auto mt-5 max-w-lg text-[17px] leading-relaxed text-navy-200 text-balance">
                Answer a few questions, get a plan built around your target score and test date, and start on a real
                adaptive module today.
              </p>

              <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
                <Button
                  size="lg"
                  className="group h-[52px] w-full rounded-full bg-primary px-8 text-base font-semibold text-white shadow-panel hover:bg-primary-600 sm:w-auto"
                  asChild
                >
                  <Link href="/onboarding">
                    Start practicing free
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

              <p className="mt-6 text-[13px] text-navy-300">Free to start · No credit card · Takes about a minute</p>
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
              A free academic community: adaptive SAT practice, full IELTS preparation, financial
              literacy, and mentorship — with research programmes and expert lectures on the way.
            </p>
          </div>

          <div>
            <p className="text-sm font-semibold">Product</p>
            <ul className="mt-3 space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#features" className="transition-colors hover:text-foreground">
                  Features
                </a>
              </li>
              <li>
                <a href="#experience" className="transition-colors hover:text-foreground">
                  Test engine
                </a>
              </li>
              <li>
                <a href="#analytics" className="transition-colors hover:text-foreground">
                  Analytics
                </a>
              </li>
              <li>
                <a href="#vocabulary" className="transition-colors hover:text-foreground">
                  Vocabulary
                </a>
              </li>
              <li>
                <a href="#mentorship" className="transition-colors hover:text-foreground">
                  Community
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
            <a
              href="mailto:scholarlyhub.space@gmail.com"
              className="text-muted-foreground hover:text-foreground"
            >
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
