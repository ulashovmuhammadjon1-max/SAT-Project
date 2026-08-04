import Link from "next/link";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "Tests & Modules" };
export const dynamic = "force-dynamic";

export default async function AdminTestsPage() {
  const tests = await prisma.test.findMany({
    orderBy: { createdAt: "desc" },
    include: { modules: { include: { _count: { select: { questions: true } } } }, _count: { select: { attempts: true } } },
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Tests & Modules</h1>
        <p className="text-sm text-muted-foreground">
          Tests created by publishing PDF uploads, or built manually via the question bank.
        </p>
      </div>

      <Card>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Title</TableHead>
                <TableHead>Type</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Modules</TableHead>
                <TableHead>Questions</TableHead>
                <TableHead>Attempts</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {tests.map((test) => {
                const questionCount = test.modules.reduce((sum, m) => sum + m._count.questions, 0);
                return (
                  <TableRow key={test.id}>
                    <TableCell>
                      <Link href={`/admin/tests/${test.id}`} className="font-medium hover:underline">
                        {test.title}
                      </Link>
                    </TableCell>
                    <TableCell className="text-sm text-muted-foreground">{test.type.replace("_", " ")}</TableCell>
                    <TableCell>
                      <Badge variant={test.status === "PUBLISHED" ? "success" : "secondary"}>{test.status}</Badge>
                    </TableCell>
                    <TableCell className="text-sm">{test.modules.length}</TableCell>
                    <TableCell className="text-sm">{questionCount}</TableCell>
                    <TableCell className="text-sm">{test._count.attempts}</TableCell>
                  </TableRow>
                );
              })}
              {tests.length === 0 && (
                <TableRow>
                  <TableCell colSpan={6} className="py-12 text-center text-sm text-muted-foreground">
                    No tests yet. Publish a PDF upload to create one.
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
