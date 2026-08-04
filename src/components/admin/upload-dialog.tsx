"use client";

import { useCallback, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { useDropzone } from "react-dropzone";
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
import { createUpload } from "@/server/actions/admin/uploads";

const CATEGORIES = [
  { value: "FULL_TEST", label: "Full practice test", hint: "Modules, passages, and questions" },
  { value: "QUESTION_BANK", label: "Question bank", hint: "Standalone practice questions" },
  { value: "VOCABULARY", label: "Vocabulary list", hint: "Word, definition, example pairs" },
] as const;

export function UploadDialog() {
  const router = useRouter();
  const [open, setOpen] = useState(false);
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
    setError(null);
    const formData = new FormData();
    formData.set("file", file);
    formData.set("category", category);

    startTransition(async () => {
      const result = await createUpload({}, formData);
      if (result.error) {
        setError(result.error);
        return;
      }
      toast.success("Upload received — extraction started.");
      setOpen(false);
      setFile(null);
      if (result.uploadId) router.push(`/admin/uploads/${result.uploadId}`);
      router.refresh();
    });
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
