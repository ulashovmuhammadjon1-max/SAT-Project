"use client";

import { useRef, useState } from "react";
import { FileUp, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";

/**
 * One-file picker that hands back a data URI.
 *
 * Uploads on this platform are stored on the row they belong to rather than in
 * blob storage, so the client's job is to read the file, not to POST it
 * anywhere. The size check here is a courtesy — the server re-checks, because
 * a client-side limit is a hint and never a rule.
 */

export const UPLOAD_TYPES = ["application/pdf", "image/png", "image/jpeg", "image/webp"];
/** ~4MB of file, matching the server's base64 cap. */
export const UPLOAD_MAX_BYTES = 4 * 1024 * 1024;

export interface PickedFile {
  name: string;
  dataUrl: string;
}

export function FileDrop({
  value,
  onChange,
  label = "Attach a file",
  hint = "PDF, PNG, JPG or WEBP — up to 4MB.",
}: {
  value: PickedFile | null;
  onChange: (file: PickedFile | null) => void;
  label?: string;
  hint?: string;
}) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [reading, setReading] = useState(false);

  async function pick(list: FileList | null) {
    const file = list?.[0];
    if (!file) return;
    if (!UPLOAD_TYPES.includes(file.type)) {
      toast.error("Use a PDF, PNG, JPG or WEBP file.");
      return;
    }
    if (file.size > UPLOAD_MAX_BYTES) {
      toast.error(`${file.name} is over 4MB.`);
      return;
    }
    setReading(true);
    try {
      const dataUrl = await new Promise<string>((resolve, reject) => {
        const r = new FileReader();
        r.onload = () => resolve(String(r.result));
        r.onerror = reject;
        r.readAsDataURL(file);
      });
      onChange({ name: file.name, dataUrl });
    } catch {
      toast.error("That file could not be read. Try another.");
    } finally {
      setReading(false);
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
      ) : (
        <Button
          type="button"
          variant="outline"
          className="w-full justify-start gap-2"
          disabled={reading}
          onClick={() => inputRef.current?.click()}
        >
          {reading ? <Loader2 className="h-4 w-4 animate-spin" /> : <FileUp className="h-4 w-4" />}
          {label}
        </Button>
      )}
      <p className="text-[11px] text-muted-foreground">{hint}</p>
    </div>
  );
}
