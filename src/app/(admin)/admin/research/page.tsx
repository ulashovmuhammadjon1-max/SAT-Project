import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ResearchDecision } from "@/components/admin/research-decision";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Research Proposals" };
export const dynamic = "force-dynamic";

export default async function AdminResearchPage() {
  await requireAdmin();

  const [pending, decided] = await Promise.all([
    prisma.researchProposal.findMany({
      where: { status: "PENDING" },
      orderBy: { createdAt: "asc" },
      include: { user: { select: { name: true, email: true, gradeLevel: true, countryCode: true } } },
    }),
    prisma.researchProposal.findMany({
      where: { status: { not: "PENDING" } },
      orderBy: { decidedAt: "desc" },
      take: 20,
      include: { user: { select: { name: true, email: true } } },
    }),
  ]);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Research proposals</h1>
        <p className="text-sm text-muted-foreground">
          {pending.length} awaiting a decision. The note you write is emailed to the student.
        </p>
      </div>

      {pending.length === 0 && (
        <Card>
          <CardContent className="py-10 text-center text-sm text-muted-foreground">
            No proposals waiting.
          </CardContent>
        </Card>
      )}

      {pending.map((p) => (
        <Card key={p.id}>
          <CardHeader className="pb-3">
            <div className="flex flex-wrap items-center gap-2">
              <CardTitle className="text-base">{p.title}</CardTitle>
              <Badge variant="outline">{p.field}</Badge>
              <span className="ml-auto text-xs text-muted-foreground">
                {p.user.name} · {p.user.email} ·{" "}
                {p.createdAt.toLocaleDateString(undefined, { month: "short", day: "numeric" })}
              </span>
            </div>
          </CardHeader>
          <CardContent className="space-y-3">
            <div>
              <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Question</p>
              <p className="mt-0.5 text-sm leading-relaxed">{p.question}</p>
            </div>
            <div>
              <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Motivation</p>
              <p className="mt-0.5 text-sm leading-relaxed">{p.motivation}</p>
            </div>
            {p.experience && (
              <div>
                <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Experience</p>
                <p className="mt-0.5 text-sm leading-relaxed">{p.experience}</p>
              </div>
            )}
            <ResearchDecision proposalId={p.id} />
          </CardContent>
        </Card>
      ))}

      {decided.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Recently decided</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="divide-y divide-border">
              {decided.map((p) => (
                <li key={p.id} className="flex flex-wrap items-center justify-between gap-2 py-2.5 text-sm">
                  <span className="min-w-[200px] flex-1">
                    <span className="font-medium">{p.title}</span>
                    <span className="ml-2 text-xs text-muted-foreground">{p.user.name}</span>
                  </span>
                  <Badge variant={p.status === "ACCEPTED" ? "success" : "destructive"}>
                    {p.status === "ACCEPTED" ? "Accepted" : "Rejected"}
                  </Badge>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
