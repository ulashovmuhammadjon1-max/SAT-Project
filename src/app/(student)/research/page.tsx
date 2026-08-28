import { FlaskConical, Lightbulb, Users2, FileText } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ResearchProposalForm } from "@/components/student/research-proposal-form";
import { getMyProposals } from "@/server/actions/student/research";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Research Programme" };
export const dynamic = "force-dynamic";

const STATUS_BADGE: Record<string, { label: string; variant: "outline" | "success" | "destructive" | "warning" }> = {
  PENDING: { label: "Under review", variant: "warning" },
  ACCEPTED: { label: "Accepted", variant: "success" },
  REJECTED: { label: "Not taken forward", variant: "destructive" },
};

const STEPS = [
  {
    icon: Lightbulb,
    title: "Propose a topic",
    body: "Submit a research question you genuinely care about, in any field — a paragraph of motivation is enough.",
  },
  {
    icon: Users2,
    title: "Get paired with a mentor",
    body: "Accepted proposals are matched with a mentor who helps you scope the question and design the work.",
  },
  {
    icon: FileText,
    title: "Do the work, publish it",
    body: "You run the project with guidance, and finished work is published on Scholarly with your name on it.",
  },
];

export default async function ResearchPage() {
  await requireUser();
  const proposals = await getMyProposals();

  return (
    <div className="space-y-6">
      <div>
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[hsl(190_84%_42%)]">
          <FlaskConical className="mr-1 inline h-3.5 w-3.5 align-[-2px]" />
          Scholarly Research
        </p>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Student Research Programme</h1>
        <p className="mt-1 max-w-2xl text-sm text-muted-foreground">
          Real research, done by students, with mentors. Universities notice students who have
          investigated something properly — this is where you start.
        </p>
      </div>

      <div className="grid gap-4 sm:grid-cols-3">
        {STEPS.map((s, i) => (
          <Card key={s.title}>
            <CardContent className="space-y-2 py-5">
              <div className="flex items-center gap-2.5">
                <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-[hsl(190_84%_42%)]/10 text-[hsl(190_84%_42%)]">
                  <s.icon className="h-4 w-4" />
                </span>
                <span className="text-xs font-semibold tabular-nums text-muted-foreground">Step {i + 1}</span>
              </div>
              <p className="font-medium">{s.title}</p>
              <p className="text-sm leading-relaxed text-muted-foreground">{s.body}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      {proposals.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Your proposals</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="divide-y divide-border">
              {proposals.map((p) => {
                const badge = STATUS_BADGE[p.status];
                return (
                  <li key={p.id} className="flex flex-wrap items-start justify-between gap-3 py-3">
                    <div className="min-w-[220px] flex-1">
                      <p className="text-sm font-medium">{p.title}</p>
                      <p className="text-xs text-muted-foreground">
                        {p.field} · submitted{" "}
                        {p.createdAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
                      </p>
                      {p.adminNote && (
                        <p className="mt-1.5 rounded-lg bg-secondary/60 px-3 py-2 text-xs leading-relaxed text-muted-foreground">
                          <span className="font-medium text-foreground">Note from the team: </span>
                          {p.adminNote}
                        </p>
                      )}
                    </div>
                    <Badge variant={badge.variant}>{badge.label}</Badge>
                  </li>
                );
              })}
            </ul>
          </CardContent>
        </Card>
      )}

      <Card className="max-w-3xl">
        <CardHeader>
          <CardTitle className="text-base">Propose your topic</CardTitle>
          <CardDescription>
            One proposal under review at a time. Be specific — a sharp question in a small area is a
            far stronger application than a broad one.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <ResearchProposalForm />
        </CardContent>
      </Card>
    </div>
  );
}
