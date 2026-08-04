"use client";

import { useRef, useState } from "react";
import { upload } from "@vercel/blob/client";
import { ImagePlus, Loader2, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";

// For figures a PDF extraction can never recover on its own (graphs, diagrams,
// tables rendered as images) — uploads go straight from the browser to Blob
// storage (see /api/blob-upload-image), then the resulting path is served
// back through /api/images/[...path] since the store is private.
export function ImageUploadField({
  imageUrl,
  onChange,
}: {
  imageUrl: string | null | undefined;
  onChange: (url: string | null) => void;
}) {
  const [isUploading, setIsUploading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  async function handleFile(file: File) {
    setIsUploading(true);
    try {
      const blob = await upload(`images/${file.name}`, file, {
        access: "private",
        handleUploadUrl: "/api/blob-upload-image",
      });
      onChange(`/api/images/${blob.pathname}`);
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Image upload failed.");
    } finally {
      setIsUploading(false);
    }
  }

  return (
    <div className="space-y-2">
      {imageUrl ? (
        <div className="relative w-fit">
          {/* eslint-disable-next-line @next/next/no-img-element -- external/proxy URL, not a static import Next can optimize */}
          <img src={imageUrl} alt="" className="max-h-48 rounded-lg border border-border" />
          <Button
            variant="secondary"
            size="icon"
            className="absolute -right-2 -top-2 h-6 w-6"
            onClick={() => onChange(null)}
          >
            <X className="h-3.5 w-3.5" />
          </Button>
        </div>
      ) : (
        <Button
          type="button"
          variant="outline"
          size="sm"
          disabled={isUploading}
          onClick={() => inputRef.current?.click()}
        >
          {isUploading ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <ImagePlus className="h-3.5 w-3.5" />}
          Upload figure (graph, diagram, table)
        </Button>
      )}
      <input
        ref={inputRef}
        type="file"
        accept="image/png,image/jpeg,image/webp,image/gif,image/svg+xml"
        className="hidden"
        onChange={(e) => {
          const file = e.target.files?.[0];
          if (file) handleFile(file);
          e.target.value = "";
        }}
      />
    </div>
  );
}
