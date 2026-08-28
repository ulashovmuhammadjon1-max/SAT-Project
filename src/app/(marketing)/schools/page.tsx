import Link from "next/link";
import { BarChart3, CheckCircle2, ClipboardList, School, Users2 } from "lucide-react";

import { SiteNav } from "@/components/marketing/site-nav";

export const metadata = {
  title: "For Schools",
  description:
    "Free classroom SAT & IELTS practice: a class code, auto-graded adaptive tests, and a per-student progress view for teachers.",
};

const BENEFITS = [
  {
    icon: ClipboardList,
    title: "Ready-made assignments",
    body: "31 full adaptive SAT practice tests and a 5,000+ question bank — assign real practice instead of photocopies, graded automatically.",
  },
  {
    icon: BarChart3,
    title: "See the whole class at a glance",
    body: "Which students are falling behind, and which skills the whole class is weakest on — so lesson time goes where the data says.",
  },
  {
    icon: Users2,
    title: "One account, both exams",
    body: "Your students need SAT and IELTS. Scholarly covers both under one free account, instead of two separate paid tools.",
  },
];

const STEPS = [
  "Write to us — we set up your class personally and give you a 6-letter code.",
  "Your students enter the code once, under My Class. That's the whole setup.",
  "You get a progress view of your class, and we stay one message away.",
];

export default function SchoolsPage() {
  return (
    <div className="min-h-screen bg-background">
      <SiteNav />
      <main className="mx-auto w-full max-w-5xl px-4 py-16 sm:px-6 lg:px-8">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-success">
          <School className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly for Schools
        </p>
        <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
          Free classroom prep, with a teacher&apos;s view
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted-foreground">
          Everything students already get on Scholarly — adaptive tests, a Bluebook-style
          interface, IELTS practice — plus a class code that shows you, the teacher, exactly how
          your class is doing. Free, with no per-seat pricing, ever.
        </p>

        <div className="mt-10 grid gap-4 sm:grid-cols-3">
          {BENEFITS.map((b) => (
            <div key={b.title} className="rounded-2xl border border-border/70 bg-card p-6 shadow-soft">
              <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-success/10 text-success">
                <b.icon className="h-5 w-5" />
              </span>
              <p className="mt-4 font-medium">{b.title}</p>
              <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">{b.body}</p>
            </div>
          ))}
        </div>

        <div className="mt-12 max-w-2xl">
          <h2 className="font-display text-xl font-semibold tracking-tight">How the pilot works</h2>
          <ul className="mt-4 space-y-3">
            {STEPS.map((s, i) => (
              <li key={i} className="flex items-start gap-3 text-[15px] leading-relaxed">
                <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-success" />
                <span className="text-muted-foreground">{s}</span>
              </li>
            ))}
          </ul>
          <p className="mt-6 text-sm text-muted-foreground">
            We are onboarding pilot classes one at a time, personally — early teachers shape what
            gets built next.
          </p>
          <a
            href="mailto:scholarlyhub.space@gmail.com?subject=Scholarly%20for%20Schools%20—%20pilot%20class"
            className="mt-6 inline-flex h-11 items-center justify-center rounded-full bg-primary px-6 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90"
          >
            Request a class code
          </a>
        </div>

        <p className="mt-12 text-sm text-muted-foreground">
          Curious what your students would be using?{" "}
          <Link href="/" className="font-medium text-primary underline-offset-4 hover:underline">
            See the platform
          </Link>{" "}
          or{" "}
          <Link href="/impact" className="font-medium text-primary underline-offset-4 hover:underline">
            our live numbers
          </Link>
          .
        </p>
      </main>
    </div>
  );
}
