"use client";

import { useRef, useState } from "react";
import { upload } from "@vercel/blob/client";
import { FileUp, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";

/**
 * One-file picker that uploads straight to Blob storage and hands back the
 * URL. Vercel caps a serverless request body at ~4.5MB, so the file itself
 * never rides through a server action — only its URL does. The size and type
 * limits are enforced server-side by the token route; the checks here are a
 * courtesy.
 */

export const UPLOAD_TYPES = ["application/pdf", "image/png", "image/jpeg", "image/webp"];
export const UPLOAD_MAX_BYTES = 10 * 1024 * 1024;

export interface PickedFile {
  name: string;
  size: number;
  url: string;
}

export function FileDrop({
  value,
  onChange,
  label = "Attach a file",
  hint = "PDF, PNG, JPG or WEBP — up to 10MB.",
}: {
  value: PickedFile | null;
  onChange: (file: PickedFile | null) => void;
  label?: string;
  hint?: string;
}) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [progress, setProgress] = useState<number | null>(null);

  async function pick(list: FileList | null) {
    const file = list?.[0];
    if (!file) return;
    if (!UPLOAD_TYPES.includes(file.type)) {
      toast.error("Use a PDF, PNG, JPG or WEBP file.");
      return;
    }
    if (file.size > UPLOAD_MAX_BYTES) {
      toast.error(`${file.name} is over 10MB.`);
      return;
    }
    setProgress(0);
    try {
      const blob = await upload(file.name, file, {
        // Private store: the URL alone opens nothing — the download
        // routes are the only door.
        access: "private",
        handleUploadUrl: "/api/assignments/upload",
        onUploadProgress: ({ percentage }) => setProgress(Math.round(percentage)),
      });
      onChange({ name: file.name, size: file.size, url: blob.url });
    } catch (e) {
      toast.error(
        e instanceof Error && e.message ? e.message : "That file could not be uploaded. Try another.",
      );
    } finally {
      setProgress(null);
      // Let the same file be picked again after being removed.
      if (inputRef.current) inputRef.current.value = "";
    }
  }

  return (
    <div className="space-y-1.5">
      <input
        ref={inputRef}
        type="file"
        accept={UPLOAD_TYPES.join(",")}
        className="hidden"
        onChange={(e) => pick(e.target.files)}
      />
      {value ? (
        <div className="flex items-center gap-2 rounded-lg border border-border bg-secondary/40 px-3 py-2">
          <FileUp className="h-4 w-4 shrink-0 text-primary" />
          <span className="min-w-0 flex-1 truncate text-sm">{value.name}</span>
          <Button
            type="button"
            size="sm"
            variant="ghost"
            className="h-7 px-2"
            onClick={() => onChange(null)}
          >
            <X className="h-4 w-4" />
          </Button>
        </div>
      ) : progress !== null ? (
        <div className="flex items-center gap-2 rounded-lg border border-border px-3 py-2">
          <Loader2 className="h-4 w-4 shrink-0 animate-spin text-primary" />
          <span className="h-1.5 min-w-0 flex-1 overflow-hidden rounded-full bg-secondary">
            <span
              className="block h-full rounded-full bg-primary transition-all"
              style={{ width: `${progress}%` }}
            />
          </span>
          <span className="shrink-0 text-xs tabular-nums text-muted-foreground">{progress}%</span>
        </div>
      ) : (
        <Button
          type="button"
          variant="outline"
          className="w-full justify-start gap-2"
          onClick={() => inputRef.current?.click()}
        >
          <FileUp className="h-4 w-4" />
          {label}
        </Button>
      )}
      <p className="text-[11px] text-muted-foreground">{hint}</p>
    </div>
  );
}
