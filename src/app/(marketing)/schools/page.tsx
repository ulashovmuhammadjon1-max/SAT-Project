import Link from "next/link";
import { Container, Eyebrow, Lede, SectionTitle } from "@/components/marketing/editorial";

import { AppReturnBar } from "@/components/marketing/app-return-bar";
import { SiteNav } from "@/components/marketing/site-nav";
import { getCurrentUser } from "@/lib/session";

export const metadata = {
  title: "For Schools",
  description:
    "Free classroom SAT & IELTS practice: a class code, auto-graded adaptive tests, and a per-student progress view for teachers.",
};

const BENEFITS = [
  {
    title: "Ready-made assignments",
    body: "31 full adaptive SAT practice tests and a 5,000+ question bank — assign real practice instead of photocopies, graded automatically.",
  },
  {
    title: "See the whole class at a glance",
    body: "Which students are falling behind, and which skills the whole class is weakest on — so lesson time goes where the data says.",
  },
  {
    title: "One account, both exams",
    body: "Your students need SAT and IELTS. Scholarly covers both under one free account, instead of two separate paid tools.",
  },
];

const STEPS = [
  "Write to us — we set up your class personally and give you a 6-letter code.",
  "Your students enter the code once, under My Class. That's the whole setup.",
  "You get a progress view of your class, and we stay one message away.",
];

export const dynamic = "force-dynamic";

export default async function SchoolsPage() {
  const user = await getCurrentUser();
  return (
    <div className="min-h-screen bg-background">
      {user ? <AppReturnBar backHref="/class" backLabel="Back to My Class" /> : <SiteNav />}
      <main id="main">
        <Container className="py-16 lg:py-24">
          <div className="grid gap-6 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <Eyebrow>Scholarly for Schools</Eyebrow>
              <SectionTitle as="h1" className="mt-5 sm:text-[2.9rem]">
                Free classroom prep, with a teacher&apos;s view
              </SectionTitle>
            </div>
            <Lede className="lg:col-span-5 lg:pt-12">
              Everything students already get on Scholarly — adaptive tests, a Bluebook-style interface, IELTS
              practice — plus a class code that shows you, the teacher, exactly how your class is doing. Free, with no
              per-seat pricing, ever.
            </Lede>
          </div>

          <ol className="mt-14 grid border-t border-border sm:grid-cols-3">
            {BENEFITS.map((b, i) => (
              <li
                key={b.title}
                className="border-b border-border py-7 sm:border-b-0 sm:py-8 sm:pr-8 sm:[&:not(:first-child)]:border-l sm:[&:not(:first-child)]:pl-8"
              >
                <p aria-hidden className="font-serif text-[15px] tabular-nums text-muted-foreground">
                  {String(i + 1).padStart(2, "0")}
                </p>
                <h2 className="mt-3 font-serif text-[1.35rem] leading-snug">{b.title}</h2>
                <p className="mt-2 text-[15px] leading-relaxed text-muted-foreground">{b.body}</p>
              </li>
            ))}
          </ol>

          <div className="mt-16 grid gap-8 border-t border-border pt-12 lg:grid-cols-12">
            <h2 className="font-serif text-[1.75rem] font-medium leading-tight lg:col-span-4">How the pilot works</h2>
            <div className="lg:col-span-7 lg:col-start-6">
              <ol className="divide-y divide-border border-y border-border">
                {STEPS.map((step, i) => (
                  <li key={i} className="grid grid-cols-[2rem_minmax(0,1fr)] gap-3 py-4 text-[15.5px] leading-relaxed">
                    <span className="font-serif tabular-nums text-muted-foreground">{i + 1}</span>
                    <span>{step}</span>
                  </li>
                ))}
              </ol>
              <p className="mt-6 text-[15px] leading-relaxed text-muted-foreground">
                We are onboarding pilot classes one at a time, personally — early teachers shape what gets built next.
              </p>
              <a
                href="mailto:scholarlyhub.space@gmail.com?subject=Scholarly%20for%20Schools%20—%20pilot%20class"
                className="mt-6 inline-flex h-11 items-center justify-center rounded-md bg-primary px-5 text-[15px] font-medium text-primary-foreground transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
              >
                Request a class code
              </a>
              {!user && (
                <p className="mt-8 text-[15px] text-muted-foreground">
                  Curious what your students would be using?{" "}
                  <Link href="/" className="font-medium text-primary underline-offset-4 hover:underline">
                    See the platform
                  </Link>
                  .
                </p>
              )}
            </div>
          </div>
        </Container>
      </main>
    </div>
  );
}
