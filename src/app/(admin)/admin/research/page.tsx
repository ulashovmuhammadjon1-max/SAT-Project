import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ResearchDecision } from "@/components/admin/research-decision";
import { ResearchMessage } from "@/components/admin/research-message";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Research Proposals" };
export const dynamic = "force-dynamic";

/**
 * What the student actually wrote.
 *
 * Shared by the pending queue and the decided list. It used to exist only in
 * the pending branch, so the moment a proposal was accepted its question and
 * motivation disappeared from the admin panel entirely and the only copy left
 * was in the database — which is not somewhere the person running the
 * programme can read it.
 */
function ProposalBody({
  question,
  priorWork,
  motivation,
  qualifications,
  experience,
  introEssay,
}: {
  question: string;
  priorWork: string | null;
  motivation: string;
  qualifications: string | null;
  experience: string | null;
  introEssay: string | null;
}) {
  // The last three questions were added in migration 031; proposals sent
  // before then simply do not have them, so each block shows only if present.
  const blocks: { label: string; text: string | null }[] = [
    { label: "Question", text: question },
    { label: "What they have already done", text: priorWork },
    { label: "Motivation", text: motivation },
    { label: "Qualifications", text: qualifications },
    { label: "Experience", text: experience },
    {
      label: introEssay ? `Introduction (${introEssay.trim().split(/\s+/).filter(Boolean).length} words)` : "Introduction",
      text: introEssay,
    },
  ];
  return (
    <div className="space-y-3">
      {blocks
        .filter((b) => b.text)
        .map((b) => (
          <div key={b.label}>
            <p className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">{b.label}</p>
            <p className="mt-0.5 whitespace-pre-line break-words text-sm leading-relaxed">{b.text}</p>
          </div>
        ))}
    </div>
  );
}

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

  const SITE = process.env.NEXT_PUBLIC_APP_URL ?? "https://scholarly.space";

  /**
   * The message that is nearly always the one being sent to an accepted
   * student: they are in, come and talk to me. Prefilled so sending is one
   * click, and still editable for anything else.
   */
  function draftFor(name: string | null) {
    const firstName = name?.trim().split(/\s+/)[0] || "there";
    return (
      `Hi ${firstName},\n\n` +
      `Your proposal has been accepted into the Scholarly research programme. You can see ` +
      `its status any time at ${SITE}/research (only you and our team can see it).\n\n` +
      `Next step is mentor pairing and planning how the project will run. Please message ` +
      `me on Telegram at @ulashovmuhammadjon1 and we will get you started.\n\n` +
      `Muhammadjon\nScholarly`
    );
  }

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
            <ProposalBody
              question={p.question}
              priorWork={p.priorWork}
              motivation={p.motivation}
              qualifications={p.qualifications}
              experience={p.experience}
              introEssay={p.introEssay}
            />
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
                <li key={p.id} className="py-2.5 text-sm">
                  <details className="group">
                    <summary className="flex cursor-pointer flex-wrap items-center justify-between gap-2 list-none">
                      <span className="min-w-[200px] flex-1">
                        <span className="font-medium">{p.title}</span>
                        <span className="ml-2 text-xs text-muted-foreground">{p.user.name}</span>
                      </span>
                      <span className="flex items-center gap-2">
                        <span className="text-xs text-muted-foreground group-open:hidden">
                          Show submission
                        </span>
                        <Badge variant={p.status === "ACCEPTED" ? "success" : "destructive"}>
                          {p.status === "ACCEPTED" ? "Accepted" : "Rejected"}
                        </Badge>
                      </span>
                    </summary>
                    <div className="mt-3 rounded-lg border border-border bg-secondary/30 p-4">
                      <ProposalBody
                        question={p.question}
                        priorWork={p.priorWork}
                        motivation={p.motivation}
                        qualifications={p.qualifications}
                        experience={p.experience}
                        introEssay={p.introEssay}
                      />
                      {p.adminNote && (
                        <p className="mt-3 text-xs text-muted-foreground">
                          Note sent to the student: {p.adminNote}
                        </p>
                      )}
                      <ResearchMessage
                        proposalId={p.id}
                        studentEmail={p.user.email}
                        defaultSubject="Your Scholarly research proposal was accepted"
                        defaultBody={draftFor(p.user.name)}
                      />
                    </div>
                  </details>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
