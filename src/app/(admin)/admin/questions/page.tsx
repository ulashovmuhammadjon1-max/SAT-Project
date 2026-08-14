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
  searchParams: { domain?: string; difficulty?: string; collection?: string };
}) {
  // `collection` has three meanings, not two: absent = no filter, "original" =
  // the pre-existing bank (collectionId IS NULL), anything else = that slug.
  // Without the explicit "original" value there would be no way to ask for
  // "everything that did not arrive in an import", which is the whole point of
  // being able to tell the batches apart.
  const collectionFilter =
    searchParams.collection === "original"
      ? { collectionId: null }
      : searchParams.collection
        ? { collection: { slug: searchParams.collection } }
        : {};

  const where = {
    domainId: searchParams.domain || undefined,
    difficulty: (searchParams.difficulty as never) || undefined,
    ...collectionFilter,
  };

  const [questions, total, domains, collections, originalCount] = await Promise.all([
    prisma.question.findMany({
      where,
      orderBy: { createdAt: "desc" },
      take: 100,
      include: { domain: true, skill: true, explanation: true, collection: true },
    }),
    prisma.question.count({ where }),
    prisma.domain.findMany({ orderBy: { name: "asc" } }),
    prisma.questionCollection.findMany({
      orderBy: [{ order: "asc" }, { createdAt: "asc" }],
      include: { _count: { select: { questions: true } } },
    }),
    prisma.question.count({ where: { collectionId: null } }),
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

      {collections.length > 0 && (
        <div className="space-y-1.5">
          <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
            Collection
          </p>
          <div className="flex flex-wrap gap-2">
            <Link href={hrefWith({ collection: undefined })}>
              <Badge variant={!searchParams.collection ? "default" : "outline"}>Everything</Badge>
            </Link>
            <Link href={hrefWith({ collection: "original" })}>
              <Badge variant={searchParams.collection === "original" ? "default" : "outline"}>
                Original bank ({originalCount.toLocaleString()})
              </Badge>
            </Link>
            {collections.map((c) => (
              <Link key={c.id} href={hrefWith({ collection: c.slug })}>
                <Badge variant={searchParams.collection === c.slug ? "default" : "outline"}>
                  {c.name} ({c._count.questions.toLocaleString()})
                </Badge>
              </Link>
            ))}
          </div>
        </div>
      )}

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
                <TableHead>Collection</TableHead>
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
                  <TableCell>
                    {q.collection ? (
                      <Badge variant="outline">{q.collection.name}</Badge>
                    ) : (
                      <span className="text-sm text-muted-foreground">Original bank</span>
                    )}
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
                  <TableCell colSpan={7} className="py-12 text-center text-sm text-muted-foreground">
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
