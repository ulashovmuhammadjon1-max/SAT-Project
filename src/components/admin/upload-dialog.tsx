"use client";

import { useCallback, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { useDropzone } from "react-dropzone";
import { upload } from "@vercel/blob/client";
import { FileText, Loader2, UploadCloud } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Label } from "@/components/ui/label";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { cn } from "@/lib/utils";
import { createUpload, createUploadFromBlob } from "@/server/actions/admin/uploads";

const CATEGORIES = [
  { value: "FULL_TEST", label: "Full practice test", hint: "Modules, passages, and questions" },
  { value: "QUESTION_BANK", label: "Question bank", hint: "Standalone practice questions" },
  { value: "VOCABULARY", label: "Vocabulary list", hint: "Word, definition, example pairs" },
] as const;

// Vercel serverless functions cap request bodies at ~4.5MB. When Blob storage
// is configured, the browser uploads the PDF directly to Blob storage instead
// of routing the raw file through a Server Action, so large mock-test PDFs
// still work. Without it (local dev), the file goes through createUpload as before.

/**
 * The ceiling on the Server Action fallback path.
 *
 * Vercel enforces ~4.5MB on serverless request bodies at the platform edge,
 * BEFORE Next.js sees the request — so `serverActions.bodySizeLimit` in
 * next.config.mjs cannot raise it, and a file that uploads happily in local dev
 * is rejected in production with no application-level error to report. Held at
 * 4MB rather than 4.5 because multipart encoding and the other form fields ride
 * along in the same body.
 *
 * This only applies when Blob is unconfigured. With Blob the browser uploads
 * straight to storage and the limit does not exist.
 */
const FALLBACK_MAX_BYTES = 4 * 1024 * 1024;
export function UploadDialog({
  blobEnabled,
  continuationParams,
}: {
  blobEnabled: boolean;
  /** When set, this upload is a module for an existing test — carried through to the review page so it opens pre-targeted. */
  continuationParams?: { targetTest: string; subject?: string; slot?: string };
}) {
  const router = useRouter();
  const [open, setOpen] = useState(Boolean(continuationParams));
  const [file, setFile] = useState<File | null>(null);
  const [category, setCategory] = useState<(typeof CATEGORIES)[number]["value"]>("FULL_TEST");
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  const onDrop = useCallback((accepted: File[]) => {
    if (accepted[0]) setFile(accepted[0]);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "application/pdf": [".pdf"] },
    maxFiles: 1,
  });

  function onSubmit() {
    if (!file) {
      setError("Choose a PDF file first.");
      return;
    }

    // Fail here, with a reason, rather than letting the platform reject the
    // request body. That rejection happens before any of this code runs, so
    // there is nothing to catch and the user sees only a generic failure.
    if (!blobEnabled && file.size > FALLBACK_MAX_BYTES) {
      setError(
        `This file is ${(file.size / 1024 / 1024).toFixed(1)}MB. Without Blob storage configured, ` +
          `uploads go through the server and Vercel caps those at about 4.5MB. ` +
          `Connect a Blob store in the Vercel dashboard (Storage tab) to upload files of any size — ` +
          `the browser then uploads straight to storage and this limit disappears.`
      );
      return;
    }

    setError(null);

    startTransition(async () => {
      try {
        const result = blobEnabled ? await submitViaBlob(file, category) : await submitViaFormData(file, category);
        if (result.error) {
          setError(result.error);
          return;
        }
        toast.success("Upload received — extraction started.");
        setOpen(false);
        setFile(null);
        if (result.uploadId) {
          const qs = continuationParams
            ? `?targetTest=${continuationParams.targetTest}${
                continuationParams.subject ? `&subject=${continuationParams.subject}` : ""
              }${continuationParams.slot ? `&slot=${continuationParams.slot}` : ""}`
            : "";
          router.push(`/admin/uploads/${result.uploadId}${qs}`);
        }
        router.refresh();
      } catch (err) {
        setError(err instanceof Error ? err.message : "Upload failed.");
      }
    });
  }

  async function submitViaBlob(file: File, category: (typeof CATEGORIES)[number]["value"]) {
    const blob = await upload(`uploads/${file.name}`, file, {
      access: "private",
      handleUploadUrl: "/api/blob-upload",
      multipart: file.size > 5 * 1024 * 1024,
    });
    return createUploadFromBlob({
      pathname: blob.pathname,
      fileName: file.name,
      fileSize: file.size,
      category,
    });
  }

  async function submitViaFormData(file: File, category: (typeof CATEGORIES)[number]["value"]) {
    const formData = new FormData();
    formData.set("file", file);
    formData.set("category", category);
    return createUpload({}, formData);
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>
          <UploadCloud className="h-4 w-4" /> Upload PDF
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader>
          <DialogTitle>Upload a PDF</DialogTitle>
          <DialogDescription>
            The system extracts text, structures it with AI, and queues it for your review before publishing.
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-4">
          <div className="space-y-2">
            <Label>Content type</Label>
            <RadioGroup value={category} onValueChange={(v) => setCategory(v as typeof category)} className="gap-2">
              {CATEGORIES.map((c) => (
                <label
                  key={c.value}
                  className={cn(
                    "flex cursor-pointer items-start gap-3 rounded-lg border border-border p-3 text-sm transition-colors",
                    category === c.value && "border-primary bg-accent"
                  )}
                >
                  <RadioGroupItem value={c.value} className="mt-0.5" />
                  <span>
                    <span className="block font-medium">{c.label}</span>
                    <span className="block text-xs text-muted-foreground">{c.hint}</span>
                  </span>
                </label>
              ))}
            </RadioGroup>
          </div>

          <div
            {...getRootProps()}
            className={cn(
              "flex cursor-pointer flex-col items-center justify-center gap-2 rounded-xl border-2 border-dashed border-border p-8 text-center transition-colors",
              isDragActive && "border-primary bg-accent"
            )}
          >
            <input {...getInputProps()} />
            {file ? (
              <>
                <FileText className="h-8 w-8 text-primary" />
                <p className="text-sm font-medium">{file.name}</p>
                <p className="text-xs text-muted-foreground">{(file.size / 1024 / 1024).toFixed(2)} MB</p>
              </>
            ) : (
              <>
                <UploadCloud className="h-8 w-8 text-muted-foreground" />
                <p className="text-sm text-muted-foreground">Drag a PDF here, or click to browse</p>
              </>
            )}
          </div>

          {/* Stated up front, because the limit is invisible until a large file
              has already been chosen and rejected. */}
          {!blobEnabled && (
            <p className="text-xs text-muted-foreground">
              Blob storage isn&apos;t configured, so files go through the server and are capped at
              about 4.5MB. Connect a Blob store in the Vercel dashboard to lift the limit.
            </p>
          )}

          {error && <p className="rounded-md bg-destructive/10 px-3 py-2 text-sm text-destructive">{error}</p>}
        </div>

        <DialogFooter>
          <Button onClick={onSubmit} disabled={isPending}>
            {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
            Start processing
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
