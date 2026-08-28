"use client";

import { useRef, useState } from "react";
import { upload } from "@vercel/blob/client";
import { FileText, Image as ImageIcon, Loader2, Upload, X } from "lucide-react";
import { toast } from "sonner";

import { formatBytes } from "@/lib/classroom/status";
import { cn } from "@/lib/utils";

/**
 * The submission upload area: one big drop zone, entirely clickable, plus the
 * list of what is attached. Multiple files, drag and drop, per-file progress,
 * remove — the parent owns both lists (files already saved on the server, and
 * files uploaded this visit but not saved yet), because saving is its move.
 *
 * Files go from the browser straight to Blob storage — Vercel caps a
 * serverless request body at ~4.5MB, so a 10MB scan could never ride through
 * a server action. What the action receives later is just the blob URL.
 */

export const UPLOAD_TYPES = ["application/pdf", "image/png", "image/jpeg", "image/webp"];
export const UPLOAD_MAX_BYTES = 10 * 1024 * 1024;
export const UPLOAD_MAX_FILES = 5;

export interface ExistingFile {
  id: string;
  name: string;
  size: number;
}

export interface NewFile {
  name: string;
  size: number;
  url: string;
}

function FileIcon({ name }: { name: string }) {
  const isImage = /\.(png|jpe?g|webp)$/i.test(name);
  const Icon = isImage ? ImageIcon : FileText;
  return (
    <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
      <Icon className="h-4 w-4" />
    </span>
  );
}

export function FileUploader({
  existing,
  added,
  onAdd,
  onRemoveExisting,
  onRemoveAdded,
  disabled = false,
}: {
  existing: ExistingFile[];
  added: NewFile[];
  onAdd: (files: NewFile[]) => void;
  onRemoveExisting: (id: string) => void;
  onRemoveAdded: (index: number) => void;
  disabled?: boolean;
}) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [dragging, setDragging] = useState(false);
  /** Filename → percent, for the rows currently in flight. */
  const [inFlight, setInFlight] = useState<Record<string, number>>({});

  const uploadingCount = Object.keys(inFlight).length;
  const count = existing.length + added.length + uploadingCount;
  const room = UPLOAD_MAX_FILES - count;

  async function ingest(list: FileList | File[] | null) {
    if (!list || disabled) return;
    const files = Array.from(list);
    if (files.length > room) {
      toast.error(`At most ${UPLOAD_MAX_FILES} files per submission.`);
    }
    for (const file of files.slice(0, Math.max(0, room))) {
      if (!UPLOAD_TYPES.includes(file.type)) {
        toast.error(`${file.name}: use a PDF, PNG, JPG or WEBP file.`);
        continue;
      }
      if (file.size > UPLOAD_MAX_BYTES) {
        toast.error(`${file.name} is over 10MB.`);
        continue;
      }
      setInFlight((m) => ({ ...m, [file.name]: 0 }));
      try {
        const blob = await upload(file.name, file, {
          access: "public",
          handleUploadUrl: "/api/assignments/upload",
          onUploadProgress: ({ percentage }) =>
            setInFlight((m) => ({ ...m, [file.name]: Math.round(percentage) })),
        });
        onAdd([{ name: file.name, size: file.size, url: blob.url }]);
      } catch (e) {
        toast.error(
          e instanceof Error && e.message
            ? `${file.name}: ${e.message}`
            : `${file.name} could not be uploaded. Try again.`,
        );
      } finally {
        setInFlight((m) => {
          const { [file.name]: _done, ...rest } = m;
          return rest;
        });
      }
    }
    if (inputRef.current) inputRef.current.value = "";
  }

  return (
    <div className="space-y-3">
      <input
        ref={inputRef}
        type="file"
        multiple
        accept={UPLOAD_TYPES.join(",")}
        className="hidden"
        onChange={(e) => ingest(e.target.files)}
      />

      {room > 0 && !disabled && (
        <button
          type="button"
          onClick={() => inputRef.current?.click()}
          onDragOver={(e) => {
            e.preventDefault();
            setDragging(true);
          }}
          onDragLeave={() => setDragging(false)}
          onDrop={(e) => {
            e.preventDefault();
            setDragging(false);
            ingest(e.dataTransfer.files);
          }}
          className={cn(
            "flex w-full flex-col items-center justify-center gap-2 rounded-2xl border-2 border-dashed px-6 py-10 text-center transition-colors",
            dragging
              ? "border-primary bg-primary/5"
              : "border-border hover:border-primary/50 hover:bg-secondary/40",
          )}
        >
          <span className="flex h-11 w-11 items-center justify-center rounded-full bg-primary/10 text-primary">
            <Upload className="h-5 w-5" />
          </span>
          <span className="text-sm font-medium">Drop your work here</span>
          <span className="text-xs text-muted-foreground">
            or <span className="font-medium text-primary">choose files</span> — PDF, PNG, JPG or
            WEBP, up to 10MB each
          </span>
        </button>
      )}

      {count > 0 && (
        <ul className="space-y-2">
          {existing.map((f) => (
            <li
              key={f.id}
              className="flex items-center gap-3 rounded-xl border border-border bg-card px-3 py-2.5"
            >
              <FileIcon name={f.name} />
              <span className="min-w-0 flex-1">
                <a
                  href={`/api/submission-file/${f.id}`}
                  target="_blank"
                  rel="noreferrer"
                  className="block truncate text-sm font-medium hover:text-primary hover:underline"
                >
                  {f.name}
                </a>
                <span className="text-xs text-muted-foreground">{formatBytes(f.size)}</span>
              </span>
              {!disabled && (
                <button
                  type="button"
                  onClick={() => onRemoveExisting(f.id)}
                  aria-label={`Remove ${f.name}`}
                  className="rounded-md p-1.5 text-muted-foreground transition-colors hover:bg-destructive/10 hover:text-destructive"
                >
                  <X className="h-4 w-4" />
                </button>
              )}
            </li>
          ))}
          {added.map((f, i) => (
            <li
              key={`${f.url}-${i}`}
              className="flex items-center gap-3 rounded-xl border border-primary/40 bg-primary/5 px-3 py-2.5"
            >
              <FileIcon name={f.name} />
              <span className="min-w-0 flex-1">
                <span className="block truncate text-sm font-medium">{f.name}</span>
                <span className="text-xs text-muted-foreground">
                  {formatBytes(f.size)} · uploaded, not saved yet
                </span>
              </span>
              {!disabled && (
                <button
                  type="button"
                  onClick={() => onRemoveAdded(i)}
                  aria-label={`Remove ${f.name}`}
                  className="rounded-md p-1.5 text-muted-foreground transition-colors hover:bg-destructive/10 hover:text-destructive"
                >
                  <X className="h-4 w-4" />
                </button>
              )}
            </li>
          ))}
          {Object.entries(inFlight).map(([name, pct]) => (
            <li
              key={`uploading-${name}`}
              className="flex items-center gap-3 rounded-xl border border-border bg-card px-3 py-2.5"
            >
              <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
                <Loader2 className="h-4 w-4 animate-spin" />
              </span>
              <span className="min-w-0 flex-1">
                <span className="block truncate text-sm font-medium">{name}</span>
                <span className="mt-1 block h-1.5 overflow-hidden rounded-full bg-secondary">
                  <span
                    className="block h-full rounded-full bg-primary transition-all"
                    style={{ width: `${pct}%` }}
                  />
                </span>
              </span>
              <span className="shrink-0 text-xs tabular-nums text-muted-foreground">{pct}%</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
