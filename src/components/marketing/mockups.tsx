"use client";

import { motion, useReducedMotion } from "framer-motion";
import {
  Bookmark,
  ChevronUp,
  Flame,
  Highlighter,
  MoreHorizontal,
  Search,
  Sparkles,
  TrendingUp,
} from "lucide-react";
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  Cell,
  PolarAngleAxis,
  PolarGrid,
  Radar,
  RadarChart,
  ResponsiveContainer,
  XAxis,
} from "recharts";

import { cn } from "@/lib/utils";

/**
 * Product mockups for the marketing page.
 *
 * These are CSS recreations of the real screens rather than image captures:
 * they stay sharp at any resolution, adapt to dark mode, animate, and never
 * go stale when the underlying UI changes colour. The exam mockup deliberately
 * reuses the same `exam-*` palette tokens as the real testing interface, so it
 * is an accurate preview and not an idealised drawing.
 */

function BrowserChrome({ children, label }: { children: React.ReactNode; label: string }) {
  return (
    <div className="overflow-hidden rounded-xl border border-border/70 bg-card shadow-panel ring-1 ring-black/[0.03]">
      <div className="flex items-center gap-2 border-b border-border/70 bg-secondary/60 px-3 py-2">
        <span className="h-2.5 w-2.5 rounded-full bg-[#FF5F57]" />
        <span className="h-2.5 w-2.5 rounded-full bg-[#FEBC2E]" />
        <span className="h-2.5 w-2.5 rounded-full bg-[#28C840]" />
        <span className="mx-auto rounded-md bg-background/80 px-3 py-0.5 text-[10px] font-medium text-muted-foreground">
          {label}
        </span>
      </div>
      {children}
    </div>
  );
}

/** Miniature of the real Bluebook-style testing interface. */
export function BluebookMockup({ className }: { className?: string }) {
  const reduced = useReducedMotion();

  return (
    <BrowserChrome label="satforge.org/exam">
      <div className={cn("bg-exam-bg text-exam-text", className)}>
        <div className="bg-exam-strip py-1 text-center text-[7px] font-medium uppercase tracking-[0.08em] text-white">
          This is a practice test
        </div>

        <div className="flex items-center justify-between border-b border-dashed border-exam-divider bg-exam-header px-3 py-1.5">
          <div>
            <p className="text-[8px] font-semibold leading-tight">Section 1, Module 1: Reading and Writing</p>
            <p className="text-[7px] leading-tight text-exam-muted">Directions</p>
          </div>
          <p className="text-[12px] font-semibold tabular-nums">18:42</p>
          <div className="flex items-center gap-1.5 text-exam-muted">
            <Highlighter className="h-2.5 w-2.5" />
            <Search className="h-2.5 w-2.5" />
            <MoreHorizontal className="h-2.5 w-2.5" />
          </div>
        </div>

        <div className="grid grid-cols-[55%_1px_1fr]">
          <div className="space-y-1.5 bg-exam-passage px-3 py-3">
            <p className="text-[7.5px] leading-[1.7] text-exam-text">
              The mosque&apos;s architecture was widely described as{" "}
              <mark className="rounded-[1px] bg-[#FFE9A6] px-0.5 text-exam-text">imposing</mark>, its scale calibrated
              less to intimidate than to orient: every arch drew the eye upward.
            </p>
            <p className="text-[7.5px] leading-[1.7] text-exam-text">
              Visitors moved slowly through the halls, pausing where the light fell in bands across the stone floor.
            </p>
            <div className="space-y-1 pt-0.5">
              <span className="block h-1 w-full rounded-full bg-exam-divider" />
              <span className="block h-1 w-[92%] rounded-full bg-exam-divider" />
              <span className="block h-1 w-[74%] rounded-full bg-exam-divider" />
            </div>
          </div>

          <div className="bg-exam-divider" />

          <div className="bg-exam-question">
            <div className="flex items-center gap-1.5 border-b border-exam-border bg-exam-header px-2.5 py-1">
              <span className="flex h-3.5 w-3.5 items-center justify-center rounded-[2px] bg-exam-strip text-[7px] font-semibold text-white">
                7
              </span>
              <span className="flex items-center gap-0.5 text-[7px] font-medium">
                <Bookmark className="h-2 w-2 text-exam-muted" /> Mark for Review
              </span>
              <span className="ml-auto rounded-[2px] border border-exam-text px-1 text-[6.5px] font-semibold line-through">
                ABC
              </span>
            </div>

            <div className="space-y-1.5 px-2.5 py-2.5">
              <p className="text-[7.5px] leading-[1.6]">
                As used in the text, what does the word <span className="italic">imposing</span> most nearly mean?
              </p>
              <div className="space-y-1">
                {[
                  { l: "A", t: "Grand in scale", selected: false },
                  { l: "B", t: "Deliberately hostile", selected: false },
                  { l: "C", t: "Commanding attention", selected: true },
                  { l: "D", t: "Recently constructed", selected: false },
                ].map((c, i) => (
                  <motion.div
                    key={c.l}
                    initial={reduced ? undefined : { opacity: 0, x: 8 }}
                    whileInView={reduced ? undefined : { opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: 0.25 + i * 0.09, duration: 0.4 }}
                    className={cn(
                      "flex items-center gap-1.5 rounded-md border bg-white px-1.5 py-1",
                      c.selected ? "border-exam-blue ring-1 ring-inset ring-exam-blue" : "border-exam-disabled"
                    )}
                  >
                    <span
                      className={cn(
                        "flex h-3 w-3 shrink-0 items-center justify-center rounded-full border text-[6px] font-medium",
                        c.selected ? "border-exam-blue bg-exam-blue text-white" : "border-exam-muted text-exam-text"
                      )}
                    >
                      {c.l}
                    </span>
                    <span className="text-[7px] text-exam-text">{c.t}</span>
                  </motion.div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="flex items-center justify-between border-t border-exam-border bg-exam-header px-3 py-1.5">
          <p className="text-[7px] font-medium">Muhammad U.</p>
          <span className="flex items-center gap-1 rounded bg-exam-strip px-2 py-0.5 text-[7px] font-medium text-white">
            Question 7 of 27 <ChevronUp className="h-2 w-2" />
          </span>
          <span className="rounded-full bg-exam-blue px-2.5 py-0.5 text-[7px] font-medium text-white">Next</span>
        </div>
      </div>
    </BrowserChrome>
  );
}

const TREND = [
  { d: "W1", s: 1180 },
  { d: "W2", s: 1220 },
  { d: "W3", s: 1240 },
  { d: "W4", s: 1310 },
  { d: "W5", s: 1350 },
  { d: "W6", s: 1420 },
  { d: "W7", s: 1450 },
];

const SKILLS = [
  { skill: "Info & Ideas", v: 88 },
  { skill: "Craft", v: 74 },
  { skill: "Expression", v: 62 },
  { skill: "Boundaries", v: 54 },
  { skill: "Algebra", v: 91 },
  { skill: "Advanced", v: 70 },
];

const HEAT = [72, 45, 88, 61, 93, 38, 79, 55, 84, 67, 41, 90, 58, 76, 62, 87, 49, 81, 70, 94, 53, 66, 85, 59, 77, 44, 91, 68];

/** Analytics dashboard preview with real charts. */
export function AnalyticsMockup({ className }: { className?: string }) {
  return (
    <BrowserChrome label="satforge.org/analytics">
      <div className={cn("space-y-3 bg-secondary/30 p-3", className)}>
        <div className="grid grid-cols-3 gap-2.5">
          {[
            { label: "Predicted score", value: "1480", tone: "text-primary" },
            { label: "Accuracy", value: "78%", tone: "text-success" },
            { label: "Questions done", value: "1,284", tone: "text-foreground" },
          ].map((s) => (
            <div key={s.label} className="rounded-lg border border-border/70 bg-card p-2.5 shadow-soft">
              <p className="text-[8px] text-muted-foreground">{s.label}</p>
              <p className={cn("font-display text-base font-semibold leading-tight", s.tone)}>{s.value}</p>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-[1.5fr_1fr] gap-2.5">
          <div className="rounded-lg border border-border/70 bg-card p-2.5 shadow-soft">
            <p className="mb-1 text-[9px] font-semibold">Score trend</p>
            <div className="h-[86px]">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={TREND} margin={{ top: 4, right: 4, bottom: 0, left: 4 }}>
                  <defs>
                    <linearGradient id="mockTrend" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stopColor="hsl(226 84% 56%)" stopOpacity={0.35} />
                      <stop offset="100%" stopColor="hsl(226 84% 56%)" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <XAxis dataKey="d" tick={{ fontSize: 7 }} axisLine={false} tickLine={false} />
                  <Area
                    type="monotone"
                    dataKey="s"
                    stroke="hsl(226 84% 56%)"
                    strokeWidth={2}
                    fill="url(#mockTrend)"
                    dot={false}
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="rounded-lg border border-border/70 bg-card p-2.5 shadow-soft">
            <p className="mb-1 text-[9px] font-semibold">Skill map</p>
            <div className="h-[86px]">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart data={SKILLS} outerRadius="72%">
                  <PolarGrid stroke="hsl(var(--border))" />
                  <PolarAngleAxis dataKey="skill" tick={{ fontSize: 5.5 }} />
                  <Radar dataKey="v" stroke="hsl(226 84% 56%)" fill="hsl(226 84% 56%)" fillOpacity={0.3} />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-[1fr_1.4fr] gap-2.5">
          <div className="rounded-lg border border-border/70 bg-card p-2.5 shadow-soft">
            <p className="mb-1.5 text-[9px] font-semibold">Weakest skills</p>
            <div className="space-y-1.5">
              {[
                { n: "Boundaries", v: 54 },
                { n: "Transitions", v: 61 },
                { n: "Vocabulary", v: 66 },
              ].map((s) => (
                <div key={s.n}>
                  <div className="flex justify-between text-[7.5px]">
                    <span>{s.n}</span>
                    <span className="text-muted-foreground">{s.v}%</span>
                  </div>
                  <div className="mt-0.5 h-1 overflow-hidden rounded-full bg-secondary">
                    <motion.div
                      className="h-full rounded-full bg-destructive/70"
                      initial={{ width: 0 }}
                      whileInView={{ width: `${s.v}%` }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.9, ease: "easeOut" }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-lg border border-border/70 bg-card p-2.5 shadow-soft">
            <p className="mb-1.5 text-[9px] font-semibold">Practice heat map</p>
            <div className="grid grid-cols-[repeat(14,minmax(0,1fr))] gap-[3px]">
              {HEAT.map((v, i) => (
                <motion.span
                  key={i}
                  initial={{ opacity: 0, scale: 0.5 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  viewport={{ once: true }}
                  transition={{ delay: i * 0.012, duration: 0.3 }}
                  className="aspect-square rounded-[2px]"
                  style={{ backgroundColor: `hsl(226 84% 56% / ${0.12 + (v / 100) * 0.8})` }}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </BrowserChrome>
  );
}

/**
 * Compact analytics panel for the hero showcase — a slice of the real
 * analytics screen small enough to layer beside the exam window.
 *
 * The numbers here are illustrative, exactly like the rest of these mockups,
 * so the card carries its own "Sample data" marker: it should read as a
 * product preview, never as a claim about real student results.
 */
export function ScorePreviewCard({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "w-[212px] rounded-xl border border-border/70 bg-card/95 p-3 shadow-panel backdrop-blur",
        className
      )}
    >
      <div className="flex items-center justify-between">
        <p className="text-[10px] font-medium text-muted-foreground">Score trend</p>
        <span className="flex items-center gap-0.5 rounded-full bg-success/10 px-1.5 py-0.5 text-[9px] font-medium text-success">
          <TrendingUp className="h-2.5 w-2.5" /> Improving
        </span>
      </div>

      <p className="mt-1 font-display text-2xl font-semibold leading-none tracking-tight">1450</p>

      <div className="mt-2 h-[42px]">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={TREND} margin={{ top: 2, right: 2, bottom: 0, left: 2 }}>
            <defs>
              <linearGradient id="heroTrend" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="hsl(226 84% 56%)" stopOpacity={0.4} />
                <stop offset="100%" stopColor="hsl(226 84% 56%)" stopOpacity={0} />
              </linearGradient>
            </defs>
            <Area
              type="monotone"
              dataKey="s"
              stroke="hsl(226 84% 56%)"
              strokeWidth={2}
              fill="url(#heroTrend)"
              dot={false}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <p className="mt-1 text-[9px] text-muted-foreground">Sample data — product preview</p>
    </div>
  );
}

/** Vocabulary flashcard preview with spaced-repetition affordances. */
export function VocabMockup({ className }: { className?: string }) {
  const reduced = useReducedMotion();

  return (
    <div className={cn("relative", className)}>
      {/* Back cards, fanned out. */}
      <div className="absolute inset-x-6 top-4 h-full rounded-2xl border border-border/60 bg-card/60 shadow-soft" />
      <div className="absolute inset-x-3 top-2 h-full rounded-2xl border border-border/70 bg-card/80 shadow-soft" />

      <motion.div
        animate={reduced ? undefined : { y: [0, -7, 0] }}
        transition={{ duration: 6, repeat: Infinity, ease: "easeInOut" }}
        className="relative rounded-2xl border border-border bg-card p-6 shadow-panel"
      >
        <div className="flex items-center justify-between">
          <span className="rounded-full bg-primary/10 px-2.5 py-1 text-[11px] font-medium text-primary">
            High frequency
          </span>
          <span className="flex items-center gap-1 text-[11px] text-muted-foreground">
            <Flame className="h-3.5 w-3.5 text-warning" /> 5-day streak
          </span>
        </div>

        <p className="mt-5 font-display text-3xl font-semibold tracking-tight">ubiquitous</p>
        <p className="mt-1 text-sm text-muted-foreground">/juːˈbɪkwɪtəs/ · adjective</p>

        <p className="mt-4 text-[15px] leading-relaxed">
          Present, appearing, or found everywhere at the same time.
        </p>
        <p className="mt-2 border-l-2 border-primary/30 pl-3 text-sm italic text-muted-foreground">
          &ldquo;Smartphones have become ubiquitous in modern classrooms.&rdquo;
        </p>

        <div className="mt-5 flex items-center gap-2">
          {[
            { l: "Again", c: "bg-destructive/10 text-destructive" },
            { l: "Hard", c: "bg-warning/15 text-warning-foreground" },
            { l: "Good", c: "bg-primary/10 text-primary" },
            { l: "Easy", c: "bg-success/10 text-success" },
          ].map((b) => (
            <span key={b.l} className={cn("flex-1 rounded-lg px-2 py-1.5 text-center text-xs font-medium", b.c)}>
              {b.l}
            </span>
          ))}
        </div>

        <div className="mt-4 flex items-center justify-between text-[11px] text-muted-foreground">
          <span>Next review in 4 days</span>
          <span className="flex items-center gap-1">
            <Sparkles className="h-3 w-3" /> 24 due today
          </span>
        </div>
      </motion.div>
    </div>
  );
}

const MODULE1 = [
  { n: "Correct", v: 21 },
  { n: "Incorrect", v: 6 },
];

/** Diagram of the adaptive Module 1 → Module 2 routing. */
export function AdaptiveDiagram({ className }: { className?: string }) {
  return (
    <div className={cn("rounded-2xl border border-border bg-card p-6 shadow-panel", className)}>
      <div className="grid gap-5 sm:grid-cols-[1fr_auto_1fr] sm:items-center">
        <div className="rounded-xl border border-border/70 bg-secondary/40 p-4">
          <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">Module 1</p>
          <p className="mt-1 font-display text-lg font-semibold">Everyone starts here</p>
          <p className="mt-1 text-sm text-muted-foreground">27 questions, mixed difficulty.</p>
          <div className="mt-3 h-16">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={MODULE1} margin={{ top: 0, right: 0, bottom: 0, left: 0 }}>
                <XAxis dataKey="n" tick={{ fontSize: 9 }} axisLine={false} tickLine={false} />
                <Bar dataKey="v" radius={[3, 3, 0, 0]}>
                  {MODULE1.map((_, i) => (
                    <Cell key={i} fill={i === 0 ? "hsl(152 60% 36%)" : "hsl(var(--border))"} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="flex justify-center">
          <div className="hidden h-px w-10 bg-gradient-to-r from-border to-primary sm:block" />
          <div className="h-10 w-px bg-gradient-to-b from-border to-primary sm:hidden" />
        </div>

        <div className="space-y-3">
          <div className="rounded-xl border border-success/30 bg-success/5 p-3.5">
            <p className="text-xs font-medium text-success">Above threshold</p>
            <p className="font-display text-base font-semibold">Module 2 — Hard</p>
            <p className="text-xs text-muted-foreground">Unlocks the top of the scale, up to 800.</p>
          </div>
          <div className="rounded-xl border border-border/70 bg-secondary/40 p-3.5">
            <p className="text-xs font-medium text-muted-foreground">Below threshold</p>
            <p className="font-display text-base font-semibold">Module 2 — Easy</p>
            <p className="text-xs text-muted-foreground">Caps the section, exactly like the real thing.</p>
          </div>
        </div>
      </div>

      <div className="mt-5 flex items-center justify-between rounded-xl bg-navy-950 px-5 py-3.5 text-white">
        <div>
          <p className="text-xs text-navy-300">Predicted total</p>
          <p className="font-display text-2xl font-semibold">1480</p>
        </div>
        <p className="max-w-[16rem] text-right text-xs text-navy-200">
          Scored on the same routing logic the College Board uses, so your practice score means something.
        </p>
      </div>
    </div>
  );
}
