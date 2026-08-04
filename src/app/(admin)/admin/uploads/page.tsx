import Link from "next/link";
import { FileText } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { UploadDialog } from "@/components/admin/upload-dialog";
import { prisma } from "@/lib/prisma";

export const metadata = { title: "PDF Ingestion Queue" };
export const dynamic = "force-dynamic";

const STATUS_VARIANT: Record<string, string> = {
  PENDING: "secondary",
  PROCESSING: "secondary",
  NEEDS_REVIEW: "warning",
  COMPLETED: "success",
  FAILED: "destructive",
};

export default async function UploadsQueuePage() {
  const uploads = await prisma.pDFUpload.findMany({
    orderBy: { createdAt: "desc" },
    include: { uploadedBy: true, jobs: { orderBy: { createdAt: "desc" }, take: 1 } },
  });

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">PDF Ingestion</h1>
          <p className="text-sm text-muted-foreground">
            Upload SAT mock tests, question banks, or vocabulary lists — AI structures them automatically.
          </p>
        </div>
        <UploadDialog />
      </div>

      <Card>
        <CardContent className="p-0">
          {uploads.length === 0 ? (
            <div className="flex flex-col items-center gap-2 p-16 text-center text-muted-foreground">
              <FileText className="h-8 w-8" />
              <p>No uploads yet.</p>
            </div>
          ) : (
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>File</TableHead>
                  <TableHead>Category</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead>Confidence</TableHead>
                  <TableHead>Uploaded by</TableHead>
                  <TableHead>Date</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {uploads.map((upload) => {
                  const job = upload.jobs[0];
                  return (
                    <TableRow key={upload.id} className="cursor-pointer">
                      <TableCell>
                        <Link href={`/admin/uploads/${upload.id}`} className="font-medium hover:underline">
                          {upload.fileName}
                        </Link>
                      </TableCell>
                      <TableCell className="text-sm text-muted-foreground">
                        {upload.category.replace("_", " ")}
                      </TableCell>
                      <TableCell>
                        <Badge variant={(STATUS_VARIANT[upload.status] ?? "secondary") as never}>
                          {upload.status.replace("_", " ")}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-sm">
                        {job?.confidenceScore != null ? `${Math.round(job.confidenceScore * 100)}%` : "—"}
                      </TableCell>
                      <TableCell className="text-sm text-muted-foreground">
                        {upload.uploadedBy?.name ?? "—"}
                      </TableCell>
                      <TableCell className="text-sm text-muted-foreground">
                        {upload.createdAt.toLocaleDateString()}
                      </TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
