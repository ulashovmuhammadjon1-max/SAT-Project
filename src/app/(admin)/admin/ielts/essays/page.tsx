import Link from "next/link";
import { Plus } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";
import { STATUS_LABELS } from "@/lib/validations/ielts-essay";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Task 2 Essays" };
export const dynamic = "force-dynamic";

const STATUS_VARIANT: Record<string, "success" | "warning" | "outline" | "navy"> = {
  PUBLISHED: "success",
  READY: "navy",
  NEEDS_REVIEW: "warning",
  ANALYZING: "outline",
  DRAFT: "outline",
};

export default async function AdminEssayListPage() {
  await requireAdmin();

  const essays = await prisma.ieltsEssay.findMany({
    orderBy: { updatedAt: "desc" },
    select: {
      id: true, title: true, question: true, band: true, topic: true, status: true,
      wordCount: true, createdAt: true, updatedAt: true, essayText: true, analyzedTextHash: true,
      _count: { select: { annotations: true, ideas: true } },
      annotations: { where: { reviewed: false }, select: { id: true } },
    },
  });

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">
            IELTS Writing Task 2 Essays
          </h1>
          <p className="text-sm text-muted-foreground">
            Band 8+ model essays for the student library. Task 2 only, Band 8.0 and above only.
          </p>
        </div>
        <Button asChild>
          <Link href="/admin/ielts/essays/new">
            <Plus className="h-4 w-4" /> New essay
          </Link>
        </Button>
      </div>

      {essays.length === 0 ? (
        <Card className="border-dashed">
          <CardContent className="flex flex-col items-center gap-2 py-14 text-center">
            <p className="text-sm font-semibold">No essays yet</p>
            <p className="max-w-sm text-sm text-muted-foreground">
              Add a Band 8+ Task 2 essay, let the analysis deconstruct it, review the highlights,
              then publish it to students.
            </p>
            <Button asChild className="mt-2">
              <Link href="/admin/ielts/essays/new">Add the first essay</Link>
            </Button>
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Question</TableHead>
                  <TableHead>Band</TableHead>
                  <TableHead>Topic</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead>Analysis</TableHead>
                  <TableHead className="text-right">Updated</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {essays.map((e) => {
                  // Offsets were computed against a specific string; if the text
                  // has moved on, the highlights cannot be trusted and the admin
                  // needs to know at a glance, not at publish time.
                  const stale =
                    e._count.annotations > 0 &&
                    e.analyzedTextHash !== null &&
                    e.status !== "ANALYZING" &&
                    !e.analyzedTextHash;
                  const unreviewed = e.annotations.length;
                  return (
                    <TableRow key={e.id}>
                      <TableCell className="max-w-md">
                        <Link href={`/admin/ielts/essays/${e.id}`} className="font-medium hover:underline">
                          {e.title}
                        </Link>
                        <p className="line-clamp-1 text-xs text-muted-foreground">{e.question}</p>
                      </TableCell>
                      <TableCell className="tabular-nums">{e.band.toFixed(1)}</TableCell>
                      <TableCell className="text-sm">{e.topic}</TableCell>
                      <TableCell>
                        <Badge variant={STATUS_VARIANT[e.status] ?? "outline"}>
                          {STATUS_LABELS[e.status] ?? e.status}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-xs text-muted-foreground">
                        {e._count.annotations === 0 ? (
                          "Not analysed"
                        ) : (
                          <>
                            {e._count.annotations} highlights · {e._count.ideas} ideas
                            {unreviewed > 0 && (
                              <span className="ml-1 font-medium text-amber-600 dark:text-amber-400">
                                {unreviewed} to review
                              </span>
                            )}
                            {stale && <span className="ml-1 font-medium text-destructive">stale</span>}
                          </>
                        )}
                      </TableCell>
                      <TableCell className="text-right text-xs tabular-nums text-muted-foreground">
                        {e.updatedAt.toLocaleDateString()}
                      </TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
