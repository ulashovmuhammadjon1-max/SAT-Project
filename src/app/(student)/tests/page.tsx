import Link from "next/link";
import { Clock, PlayCircle } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { StartTestButton } from "@/components/student/start-test-button";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { sortTests } from "@/lib/tests/order";

export const metadata = { title: "Practice Tests" };
export const dynamic = "force-dynamic";

export default async function TestsPage() {
  const user = await requireUser();

  const [published, myAttempts] = await Promise.all([
    prisma.test.findMany({
      where: { status: "PUBLISHED" },
      include: { modules: { include: { _count: { select: { questions: true } } } } },
    }),
    prisma.attempt.findMany({
      where: { userId: user.id },
      orderBy: { createdAt: "desc" },
      include: { test: true },
    }),
  ]);

  // Test 1 first, Test 31 last — a student works through these in order, so
  // the list has to read in that order too.
  const tests = sortTests(published);

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Practice Tests</h1>
        <p className="text-sm text-muted-foreground">
          Full-length adaptive tests. Module 2 difficulty adjusts automatically based on your Module 1 performance.
        </p>
      </div>

      <div className="stagger grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {tests.map((test) => {
          const questionCount = test.modules.reduce((sum, m) => sum + m._count.questions, 0);
          const totalMinutes = test.modules.reduce((sum, m) => sum + m.timeLimitMinutes, 0);
          return (
            <Card key={test.id} className="lift">
              <CardHeader>
                <CardTitle className="text-base">{test.title}</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex flex-wrap gap-2 text-xs text-muted-foreground">
                  <Badge variant="outline">{questionCount} questions</Badge>
                  <Badge variant="outline">
                    <Clock className="h-3 w-3" /> ~{totalMinutes} min
                  </Badge>
                  {test.isAdaptive && <Badge variant="navy">Adaptive</Badge>}
                </div>
                <StartTestButton testId={test.id} />
              </CardContent>
            </Card>
          );
        })}
        {tests.length === 0 && (
          <p className="text-sm text-muted-foreground">No practice tests are published yet — check back soon.</p>
        )}
      </div>

      {myAttempts.length > 0 && (
        <div>
          <h2 className="mb-3 font-display text-lg font-semibold">Your attempts</h2>
          <div className="space-y-2">
            {myAttempts.map((attempt) => (
              <Card key={attempt.id}>
                <CardContent className="flex items-center justify-between p-4">
                  <div>
                    <p className="text-sm font-medium">{attempt.test.title}</p>
                    <p className="text-xs text-muted-foreground">
                      {attempt.createdAt.toLocaleDateString()} · {attempt.status.replace("_", " ")}
                    </p>
                  </div>
                  {attempt.status === "SUBMITTED" ? (
                    <Button variant="outline" size="sm" asChild>
                      <Link href={`/results/${attempt.id}`}>View result</Link>
                    </Button>
                  ) : (
                    <Button size="sm" asChild>
                      <Link href={`/exam/${attempt.id}`}>
                        <PlayCircle className="h-4 w-4" /> Resume
                      </Link>
                    </Button>
                  )}
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
