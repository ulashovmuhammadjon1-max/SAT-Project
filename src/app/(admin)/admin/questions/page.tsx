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
  const questions = await prisma.question.findMany({
    where: {
      domainId: searchParams.domain || undefined,
      difficulty: (searchParams.difficulty as never) || undefined,
    },
    orderBy: { createdAt: "desc" },
    take: 100,
    include: { domain: true, skill: true, explanation: true },
  });

  const domains = await prisma.domain.findMany({ orderBy: { name: "asc" } });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Question Bank</h1>
        <p className="text-sm text-muted-foreground">{questions.length} questions shown (latest 100)</p>
      </div>

      <div className="flex flex-wrap gap-2">
        <Link href="/admin/questions">
          <Badge variant={!searchParams.domain ? "default" : "outline"}>All domains</Badge>
        </Link>
        {domains.map((d) => (
          <Link key={d.id} href={`/admin/questions?domain=${d.id}`}>
            <Badge variant={searchParams.domain === d.id ? "default" : "outline"}>{d.name}</Badge>
          </Link>
        ))}
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
