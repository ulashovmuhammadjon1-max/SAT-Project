import Link from "next/link";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Question Bank" };
export const dynamic = "force-dynamic";

export default async function AdminQuestionsPage({
  searchParams,
}: {
  searchParams: { domain?: string; difficulty?: string };
}) {
  const where = {
    domainId: searchParams.domain || undefined,
    difficulty: (searchParams.difficulty as never) || undefined,
  };

  // Named columns rather than a whole-row fetch. The list shows a stem excerpt,
  // some labels and a "has explanation" tick, so pulling `imageUrl` (base64
  // data URIs averaging 127 KB) and full explanation bodies for 100 rows was
  // wasted transfer.
  const [questions, total, domains] = await Promise.all([
    prisma.question.findMany({
      where,
      orderBy: { createdAt: "desc" },
      take: 100,
      select: {
        id: true,
        stem: true,
        type: true,
        difficulty: true,
        isPublished: true,
        domain: { select: { name: true } },
        skill: { select: { name: true } },
        explanation: { select: { id: true } },
      },
    }),
    prisma.question.count({ where }),
    prisma.domain.findMany({ orderBy: { name: "asc" } }),
  ]);

  /** Keeps the other filters intact when one of them is changed. */
  function hrefWith(patch: Record<string, string | undefined>) {
    const next = new URLSearchParams();
    for (const [k, v] of Object.entries({ ...searchParams, ...patch })) {
      if (v) next.set(k, v);
    }
    const qs = next.toString();
    return qs ? `/admin/questions?${qs}` : "/admin/questions";
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Question Bank</h1>
        <p className="text-sm text-muted-foreground">
          {total.toLocaleString()} matching{" "}
          {total === 1 ? "question" : "questions"}
          {total > questions.length && ` — showing the latest ${questions.length}`}
        </p>
      </div>

      <div className="space-y-1.5">
        <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">Domain</p>
        <div className="flex flex-wrap gap-2">
          <Link href={hrefWith({ domain: undefined })}>
            <Badge variant={!searchParams.domain ? "default" : "outline"}>All domains</Badge>
          </Link>
          {domains.map((d) => (
            <Link key={d.id} href={hrefWith({ domain: d.id })}>
              <Badge variant={searchParams.domain === d.id ? "default" : "outline"}>{d.name}</Badge>
            </Link>
          ))}
        </div>
      </div>

      <Card>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Question</TableHead>
                <TableHead>Domain</TableHead>
                <TableHead>Skill</TableHead>
                <TableHead>Difficulty</TableHead>
                <TableHead>Explanation</TableHead>
                <TableHead>Status</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {questions.map((q) => (
                <TableRow key={q.id}>
                  <TableCell className="max-w-md">
                    <Link href={`/admin/questions/${q.id}`} className="line-clamp-1 font-medium hover:underline">
                      {q.stem.replace(/<[^>]+>/g, "")}
                    </Link>
                  </TableCell>
                  <TableCell className="text-sm text-muted-foreground">{q.domain.name}</TableCell>
                  <TableCell className="text-sm text-muted-foreground">{q.skill.name}</TableCell>
                  <TableCell>
                    <Badge variant="outline">{q.difficulty}</Badge>
                  </TableCell>
                  <TableCell>
                    <Badge variant={q.explanation ? "success" : "secondary"}>
                      {q.explanation ? "Present" : "Missing"}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <Badge variant={q.isPublished ? "success" : "warning"}>
                      {q.isPublished ? "Published" : "Draft"}
                    </Badge>
                  </TableCell>
                </TableRow>
              ))}
              {questions.length === 0 && (
                <TableRow>
                  <TableCell colSpan={6} className="py-12 text-center text-sm text-muted-foreground">
                    No questions yet. Publish a PDF upload to populate the bank.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
