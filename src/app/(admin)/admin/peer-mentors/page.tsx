import { FileText } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { PeerMentorDecision } from "@/components/admin/peer-mentor-decision";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Peer Mentors" };
export const dynamic = "force-dynamic";

interface Certificate {
  name: string;
  dataUrl: string;
}

function asCertificates(value: unknown): Certificate[] {
  if (!Array.isArray(value)) return [];
  return value.filter(
    (c): c is Certificate =>
      typeof c === "object" && c !== null &&
      typeof (c as Certificate).name === "string" &&
      typeof (c as Certificate).dataUrl === "string",
  );
}

export default async function AdminPeerMentorsPage() {
  await requireAdmin();

  const [pending, decided] = await Promise.all([
    prisma.peerMentorApplication.findMany({
      where: { status: "PENDING" },
      orderBy: { createdAt: "asc" },
      include: { user: { select: { name: true, email: true, createdAt: true } } },
    }),
    prisma.peerMentorApplication.findMany({
      where: { status: { not: "PENDING" } },
      orderBy: { decidedAt: "desc" },
      take: 20,
      include: { user: { select: { name: true, email: true } } },
    }),
  ]);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Peer-mentor applications</h1>
        <p className="text-sm text-muted-foreground">
          {pending.length} awaiting review. Open every certificate before approving — the badge is a
          trust mark, and it is only worth what this check makes it worth.
        </p>
      </div>

      {pending.length === 0 && (
        <Card>
          <CardContent className="py-10 text-center text-sm text-muted-foreground">
            No applications waiting.
          </CardContent>
        </Card>
      )}

      {pending.map((a) => {
        const certs = asCertificates(a.certificates);
        return (
          <Card key={a.id}>
            <CardHeader className="pb-3">
              <div className="flex flex-wrap items-center gap-2">
                <CardTitle className="text-base">{a.user.name ?? a.user.email}</CardTitle>
                {a.satScore != null && <Badge variant="outline">SAT {a.satScore}</Badge>}
                {a.ieltsBand != null && <Badge variant="outline">IELTS {a.ieltsBand.toFixed(1)}</Badge>}
                <span className="ml-auto text-xs text-muted-foreground">
                  {a.user.email} · student since{" "}
                  {a.user.createdAt.toLocaleDateString(undefined, { month: "short", year: "numeric" })}
                </span>
              </div>
              <p className="text-sm font-medium text-muted-foreground">{a.headline}</p>
            </CardHeader>
            <CardContent className="space-y-4">
              <p className="text-sm leading-relaxed">{a.bio}</p>

              <div className="flex flex-wrap gap-1.5">
                {a.subjects.map((s) => (
                  <Badge key={s} variant="navy" className="text-[11px]">{s}</Badge>
                ))}
                {a.telegram && <Badge variant="outline" className="text-[11px]">TG: {a.telegram}</Badge>}
              </div>

              <div>
                <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                  Certificates ({certs.length})
                </p>
                <div className="flex flex-wrap gap-3">
                  {certs.map((c, i) =>
                    c.dataUrl.startsWith("data:application/pdf") ? (
                      <a
                        key={i}
                        href={c.dataUrl}
                        download={c.name}
                        className="flex items-center gap-2 rounded-lg border border-border px-3 py-2 text-sm text-primary hover:bg-secondary"
                      >
                        <FileText className="h-4 w-4" /> {c.name} (PDF)
                      </a>
                    ) : (
                      <a key={i} href={c.dataUrl} target="_blank" rel="noreferrer" className="block">
                        {/* eslint-disable-next-line @next/next/no-img-element */}
                        <img
                          src={c.dataUrl}
                          alt={c.name}
                          className="h-40 rounded-lg border border-border object-contain"
                        />
                      </a>
                    ),
                  )}
                </div>
              </div>

              <PeerMentorDecision applicationId={a.id} />
            </CardContent>
          </Card>
        );
      })}

      {decided.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Recently decided</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="divide-y divide-border">
              {decided.map((a) => (
                <li key={a.id} className="flex flex-wrap items-center justify-between gap-2 py-2.5 text-sm">
                  <span className="min-w-[200px] flex-1">
                    <span className="font-medium">{a.user.name ?? a.user.email}</span>
                    <span className="ml-2 text-xs text-muted-foreground">{a.headline}</span>
                  </span>
                  <Badge variant={a.status === "APPROVED" ? "success" : "destructive"}>
                    {a.status === "APPROVED" ? "Approved" : "Rejected"}
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
