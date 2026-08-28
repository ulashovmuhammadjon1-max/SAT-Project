"use client";

import { useRef, useState } from "react";
import { FileText, Image as ImageIcon, Loader2, Upload, X } from "lucide-react";
import { toast } from "sonner";

import { formatBytes } from "@/lib/classroom/status";
import { cn } from "@/lib/utils";

/**
 * The submission upload area: one big drop zone, entirely clickable, plus the
 * list of what is attached. Multiple files, drag and drop, remove — the
 * parent owns both lists (files already saved on the server, and files added
 * this visit but not saved yet), because saving is the parent's move.
 *
 * Client-side checks are a courtesy; the server re-validates every file.
 */

export const UPLOAD_TYPES = ["application/pdf", "image/png", "image/jpeg", "image/webp"];
export const UPLOAD_MAX_BYTES = 4 * 1024 * 1024;
export const UPLOAD_MAX_FILES = 5;

export interface ExistingFile {
  id: string;
  name: string;
  size: number;
}

export interface NewFile {
  name: string;
  size: number;
  dataUrl: string;
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
  const [reading, setReading] = useState(false);
  const [dragging, setDragging] = useState(false);

  const count = existing.length + added.length;
  const room = UPLOAD_MAX_FILES - count;

  async function ingest(list: FileList | File[] | null) {
    if (!list || disabled) return;
    const files = Array.from(list);
    if (files.length > room) {
      toast.error(`At most ${UPLOAD_MAX_FILES} files per submission.`);
    }
    const accepted: NewFile[] = [];
    setReading(true);
    try {
      for (const file of files.slice(0, room)) {
        if (!UPLOAD_TYPES.includes(file.type)) {
          toast.error(`${file.name}: use a PDF, PNG, JPG or WEBP file.`);
          continue;
        }
        if (file.size > UPLOAD_MAX_BYTES) {
          toast.error(`${file.name} is over 4MB.`);
          continue;
        }
        try {
          const dataUrl = await new Promise<string>((resolve, reject) => {
            const r = new FileReader();
            r.onload = () => resolve(String(r.result));
            r.onerror = reject;
            r.readAsDataURL(file);
          });
          accepted.push({ name: file.name, size: file.size, dataUrl });
        } catch {
          toast.error(`${file.name} could not be read. Try again.`);
        }
      }
      if (accepted.length) onAdd(accepted);
    } finally {
      setReading(false);
      if (inputRef.current) inputRef.current.value = "";
    }
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
          {reading ? (
            <Loader2 className="h-6 w-6 animate-spin text-primary" />
          ) : (
            <span className="flex h-11 w-11 items-center justify-center rounded-full bg-primary/10 text-primary">
              <Upload className="h-5 w-5" />
            </span>
          )}
          <span className="text-sm font-medium">
            {reading ? "Adding your files…" : "Drop your work here"}
          </span>
          <span className="text-xs text-muted-foreground">
            or <span className="font-medium text-primary">choose files</span> — PDF, PNG, JPG or
            WEBP, up to 4MB each
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
              key={`${f.name}-${i}`}
              className="flex items-center gap-3 rounded-xl border border-primary/40 bg-primary/5 px-3 py-2.5"
            >
              <FileIcon name={f.name} />
              <span className="min-w-0 flex-1">
                <span className="block truncate text-sm font-medium">{f.name}</span>
                <span className="text-xs text-muted-foreground">
                  {formatBytes(f.size)} · not saved yet
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
        </ul>
      )}
    </div>
  );
}
