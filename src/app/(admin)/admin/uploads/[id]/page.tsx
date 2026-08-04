import { notFound } from "next/navigation";
import Link from "next/link";
import { AlertTriangle, ArrowLeft, Loader2 } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ExtractionReview } from "@/components/admin/extraction-review";
import { ReprocessButton } from "@/components/admin/reprocess-button";
import { prisma } from "@/lib/prisma";
import type { TestExtractionResult, VocabExtractionResult } from "@/lib/ai/types";

export const dynamic = "force-dynamic";

export default async function UploadDetailPage({ params }: { params: { id: string } }) {
  const upload = await prisma.pDFUpload.findUnique({
    where: { id: params.id },
    include: { jobs: { orderBy: { createdAt: "desc" }, take: 1 }, uploadedBy: true },
  });

  if (!upload) notFound();
  const job = upload.jobs[0];

  const [domains, existingTests] = await Promise.all([
    prisma.domain.findMany({
      orderBy: { name: "asc" },
      include: { skills: { orderBy: { name: "asc" } } },
    }),
    prisma.test.findMany({
      where: { type: "FULL_LENGTH" },
      select: { id: true, title: true, modules: { select: { subject: true, order: true, difficulty: true } } },
      orderBy: { createdAt: "desc" },
    }),
  ]);

  return (
    <div className="space-y-6">
      <div>
        <Link
          href="/admin/uploads"
          className="mb-2 inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" /> Back to queue
        </Link>
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h1 className="font-display text-2xl font-semibold tracking-tight">{upload.fileName}</h1>
            <p className="text-sm text-muted-foreground">
              {upload.category.replace("_", " ")} · uploaded by {upload.uploadedBy?.name ?? "—"} on{" "}
              {upload.createdAt.toLocaleString()}
            </p>
          </div>
          <Badge variant={upload.status === "COMPLETED" ? "success" : "secondary"}>
            {upload.status.replace("_", " ")}
          </Badge>
        </div>
      </div>

      {(upload.status === "PENDING" || upload.status === "PROCESSING") && (
        <Card>
          <CardContent className="flex flex-col items-center gap-3 p-16 text-center">
            <Loader2 className="h-8 w-8 animate-spin text-primary" />
            <p className="font-medium">Extracting and structuring this document…</p>
            <p className="text-sm text-muted-foreground">This page will update automatically once complete.</p>
          </CardContent>
        </Card>
      )}

      {upload.status === "FAILED" && (
        <Card>
          <CardContent className="flex flex-col items-center gap-3 p-16 text-center">
            <AlertTriangle className="h-8 w-8 text-destructive" />
            <p className="font-medium">Extraction failed</p>
            <p className="max-w-md text-sm text-muted-foreground">{job?.errorMessage}</p>
            <ReprocessButton uploadId={upload.id} />
          </CardContent>
        </Card>
      )}

      {(upload.status === "NEEDS_REVIEW" || upload.status === "COMPLETED") && job?.extractedData && (
        <ExtractionReview
          uploadId={upload.id}
          jobId={job.id}
          category={upload.category}
          confidence={job.confidenceScore ?? 0}
          data={job.extractedData as unknown as TestExtractionResult | VocabExtractionResult}
          alreadyPublished={upload.status === "COMPLETED"}
          domains={domains}
          existingTests={existingTests}
        />
      )}
    </div>
  );
}
