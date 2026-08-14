import Link from "next/link";
import { AlertTriangle } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Content Health" };
export const dynamic = "force-dynamic";

// Best-effort text scan for questions that reference a figure/graph/table
// but have neither an attached image nor structured table data -- can't be
// certain from text alone (a false positive just means "check and dismiss"),
// so this is a worklist for a human, not an authoritative defect list.
const DIAGRAM_HINT = /\b(graph|scatterplot|diagram|chart|figure|table|shown (?:below|above|in the))\b/i;

function moduleLabel(subject: "READING_WRITING" | "MATH", order: number, difficulty: "STANDARD" | "EASY" | "HARD") {
  const subjectLabel = subject === "READING_WRITING" ? "R&W" : "Math";
  if (order === 1) return `${subjectLabel} Module 1`;
  return `${subjectLabel} Module 2 (${difficulty === "HARD" ? "Hard" : "Easy"})`;
}

export default async function ContentHealthPage() {
  // Which questions carry an image, as a set of ids. The diagram check only
  // ever tests `imageUrl` for truthiness, never reads it, and the column holds
  // base64 data URIs averaging 127 KB — so selecting it would move tens of
  // megabytes across the wire to answer a yes/no question.
  const withImage = new Set(
    (
      await prisma.$queryRaw<{ id: string }[]>`
        SELECT id FROM "Question" WHERE "imageUrl" IS NOT NULL AND "imageUrl" <> ''`
    ).map((r) => r.id)
  );

  // Named columns rather than whole rows. This scans every published question
  // — over 4,500 of them — so `include` was pulling every `imageUrl` in the
  // database (base64 data URIs averaging 127 KB each) purely to test whether
  // one was null. Selecting the columns the checks actually read also keeps
  // the page working while schema.prisma is ahead of the deployed database.
  const questions = await prisma.question.findMany({
    where: { isPublished: true },
    select: {
      id: true,
      stem: true,
      type: true,
      order: true,
      tableData: true,
      choices: { select: { content: true, isCorrect: true } },
      passage: { select: { content: true } },
      module: {
        select: {
          subject: true,
          order: true,
          difficulty: true,
          test: { select: { id: true, title: true } },
        },
      },
    },
    orderBy: [{ moduleId: "asc" }, { order: "asc" }],
  });

  const badChoices = questions.filter(
    (q) =>
      q.type === "MULTIPLE_CHOICE" &&
      (q.choices.length !== 4 ||
        q.choices.some((c) => !c.content.trim()) ||
        q.choices.filter((c) => c.isCorrect).length !== 1)
  );

  const missingDiagrams = questions.filter(
    (q) =>
      !withImage.has(q.id) &&
      !q.tableData &&
      !q.stem.includes("<table") &&
      !q.passage?.content.includes("<table") &&
      (DIAGRAM_HINT.test(q.stem) || DIAGRAM_HINT.test(q.passage?.content ?? ""))
  );

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Content Health</h1>
        <p className="text-sm text-muted-foreground">
          Already-published questions that likely need a fix. Missing choices are a hard defect; missing diagrams
          are a best-effort guess from the question text — check each one before acting.
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-base">
            <AlertTriangle className="h-4 w-4 text-destructive" />
            Missing or invalid choices ({badChoices.length})
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Test</TableHead>
                <TableHead>Module</TableHead>
                <TableHead>#</TableHead>
                <TableHead>Stem</TableHead>
                <TableHead>Choices</TableHead>
                <TableHead />
              </TableRow>
            </TableHeader>
            <TableBody>
              {badChoices.map((q) => (
                <TableRow key={q.id}>
                  <TableCell className="text-sm">{q.module?.test.title ?? "—"}</TableCell>
                  <TableCell className="text-sm text-muted-foreground">
                    {q.module ? moduleLabel(q.module.subject, q.module.order, q.module.difficulty) : "Question Bank"}
                  </TableCell>
                  <TableCell className="text-sm">{q.order}</TableCell>
                  <TableCell className="max-w-md truncate text-sm text-muted-foreground">
                    {q.stem.replace(/<[^>]+>/g, "").slice(0, 80)}
                  </TableCell>
                  <TableCell>
                    <Badge variant="destructive">{q.choices.length} choice{q.choices.length === 1 ? "" : "s"}</Badge>
                  </TableCell>
                  <TableCell>
                    <Link href={`/admin/questions/${q.id}`} className="text-sm font-medium text-primary hover:underline">
                      Fix
                    </Link>
                  </TableCell>
                </TableRow>
              ))}
              {badChoices.length === 0 && (
                <TableRow>
                  <TableCell colSpan={6} className="py-10 text-center text-sm text-muted-foreground">
                    No published questions are missing choices.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-base">
            <AlertTriangle className="h-4 w-4 text-warning" />
            Possibly missing a diagram ({missingDiagrams.length})
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Test</TableHead>
                <TableHead>Module</TableHead>
                <TableHead>#</TableHead>
                <TableHead>Stem</TableHead>
                <TableHead />
              </TableRow>
            </TableHeader>
            <TableBody>
              {missingDiagrams.map((q) => (
                <TableRow key={q.id}>
                  <TableCell className="text-sm">{q.module?.test.title ?? "—"}</TableCell>
                  <TableCell className="text-sm text-muted-foreground">
                    {q.module ? moduleLabel(q.module.subject, q.module.order, q.module.difficulty) : "Question Bank"}
                  </TableCell>
                  <TableCell className="text-sm">{q.order}</TableCell>
                  <TableCell className="max-w-md truncate text-sm text-muted-foreground">
                    {q.stem.replace(/<[^>]+>/g, "").slice(0, 80)}
                  </TableCell>
                  <TableCell>
                    <Link href={`/admin/questions/${q.id}`} className="text-sm font-medium text-primary hover:underline">
                      Review
                    </Link>
                  </TableCell>
                </TableRow>
              ))}
              {missingDiagrams.length === 0 && (
                <TableRow>
                  <TableCell colSpan={5} className="py-10 text-center text-sm text-muted-foreground">
                    No published questions look like they&apos;re missing a diagram.
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
