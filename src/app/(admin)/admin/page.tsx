import { FileText, ListChecks, SpellCheck2, Users } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { prisma } from "@/lib/prisma";
import { countedStudentWhere } from "@/lib/counted-students";

export const metadata = { title: "Admin Overview" };

export default async function AdminOverviewPage() {
  const [userCount, questionCount, vocabCount, pendingUploads, recentUploads] = await Promise.all([
    prisma.user.count({ where: countedStudentWhere }),
    prisma.question.count(),
    prisma.vocabWord.count(),
    prisma.pDFUpload.count({ where: { status: { in: ["PENDING", "PROCESSING", "NEEDS_REVIEW"] } } }),
    prisma.pDFUpload.findMany({ orderBy: { createdAt: "desc" }, take: 6, include: { uploadedBy: true } }),
  ]);

  const stats = [
    { label: "Students", value: userCount, icon: Users },
    { label: "Questions", value: questionCount, icon: ListChecks },
    { label: "Vocabulary words", value: vocabCount, icon: SpellCheck2 },
    { label: "Pending uploads", value: pendingUploads, icon: FileText },
  ];

  return (
    <div className="space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Overview</h1>
        <p className="text-sm text-muted-foreground">Platform-wide status at a glance.</p>
      </div>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.label}>
            <CardContent className="flex items-center justify-between p-6">
              <div>
                <p className="text-sm text-muted-foreground">{stat.label}</p>
                <p className="font-display text-3xl font-semibold">{stat.value}</p>
              </div>
              <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-primary-50 text-primary-600">
                <stat.icon className="h-5 w-5" />
              </span>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Recent PDF uploads</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          {recentUploads.length === 0 && (
            <p className="text-sm text-muted-foreground">No uploads yet — start from PDF Ingestion.</p>
          )}
          {recentUploads.map((upload) => (
            <div key={upload.id} className="flex items-center justify-between rounded-lg border border-border p-3">
              <div>
                <p className="text-sm font-medium">{upload.fileName}</p>
                <p className="text-xs text-muted-foreground">
                  {upload.category.replace("_", " ")} · uploaded by {upload.uploadedBy?.name ?? "—"}
                </p>
              </div>
              <StatusBadge status={upload.status} />
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
}

function StatusBadge({ status }: { status: string }) {
  const variant =
    status === "COMPLETED"
      ? "success"
      : status === "FAILED"
        ? "destructive"
        : status === "NEEDS_REVIEW"
          ? "warning"
          : "secondary";
  return <Badge variant={variant as never}>{status.replace("_", " ")}</Badge>;
}
