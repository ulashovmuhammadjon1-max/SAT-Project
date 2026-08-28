import Link from "next/link";
import { BookOpen, CheckCircle2, XCircle } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Proposal Guide" };

const GOOD_VS_VAGUE: { good: string; vague: string }[] = [
  {
    vague: "How does social media affect students?",
    good: "Does time spent on short-form video the night before a practice test predict a lower Reading score the next day?",
  },
  {
    vague: "Why is the SAT hard?",
    good: "Which SAT question skill costs students in my country the most points, and does it differ from published US data?",
  },
  {
    vague: "Is money important in education?",
    good: "How does the price of private SAT tutoring in three Tashkent districts compare to the score gains tutors advertise?",
  },
];

const SECTIONS = [
  {
    title: "1. Ask one narrow question",
    body: "A research project answers one question well. If your question has the word “and” in it twice, it is two projects. Narrow does not mean small — it means answerable: you can imagine the exact evidence that would settle it.",
  },
  {
    title: "2. Say why it matters to you",
    body: "Reviewers accept curiosity they can feel. “I noticed my classmates all lose points on the same question type and I want to know if that is true beyond my class” beats any grand statement about the future of education.",
  },
  {
    title: "3. Think about evidence before methods",
    body: "You do not need to know statistics to propose. You need to say what you would look at: survey answers, practice-test records, prices, historical documents, interviews. Your mentor helps turn that into a method after acceptance.",
  },
  {
    title: "4. Honesty beats polish",
    body: "“I have never done research before” is a perfectly good experience section. What gets proposals rejected is vagueness, not inexperience.",
  },
];

export default async function ResearchGuidePage() {
  await requireUser();

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(190_84%_42%)]">
          <BookOpen className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly Research
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">
          How to write a proposal that gets accepted
        </h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Everything a reviewer looks for, in four rules and three examples.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        {SECTIONS.map((s) => (
          <Card key={s.title}>
            <CardContent className="py-5">
              <p className="font-medium">{s.title}</p>
              <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">{s.body}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Vague vs. answerable</CardTitle>
        </CardHeader>
        <CardContent>
          <ul className="space-y-4">
            {GOOD_VS_VAGUE.map((ex, i) => (
              <li key={i} className="space-y-1.5">
                <p className="flex items-start gap-2 text-sm text-muted-foreground">
                  <XCircle className="mt-0.5 h-4 w-4 shrink-0 text-destructive" />
                  {ex.vague}
                </p>
                <p className="flex items-start gap-2 text-sm">
                  <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-success" />
                  {ex.good}
                </p>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <p className="text-sm text-muted-foreground">
        Ready?{" "}
        <Link href="/research" className="font-medium text-primary underline-offset-4 hover:underline">
          Submit your proposal
        </Link>{" "}
        — or see what other students are working on in{" "}
        <Link href="/journal" className="font-medium text-primary underline-offset-4 hover:underline">
          the Journal
        </Link>
        .
      </p>
    </div>
  );
}
