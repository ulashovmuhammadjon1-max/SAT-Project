"use client";

import { useCallback, useEffect, useState } from "react";
import { createPortal } from "react-dom";
import { ChevronLeft, ChevronRight, Download, ExternalLink, FileText, Globe, Play, X } from "lucide-react";

import type { CommunityAttachmentView } from "@/lib/community/types";
import { cn } from "@/lib/utils";

import { fileSize } from "./bits";

/* -------------------------------------------------------------------------- */
/* Lightbox                                                                    */
/* -------------------------------------------------------------------------- */

export function Lightbox({
  images,
  index,
  onClose,
}: {
  images: CommunityAttachmentView[];
  index: number;
  onClose: () => void;
}) {
  const [i, setI] = useState(index);
  const img = images[i];
  const go = useCallback((d: number) => setI((n) => (n + d + images.length) % images.length), [images.length]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
      if (e.key === "ArrowRight") go(1);
      if (e.key === "ArrowLeft") go(-1);
    };
    document.addEventListener("keydown", onKey);
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = prev;
    };
  }, [go, onClose]);

  if (!img) return null;
  return createPortal(
    <div
      role="dialog"
      aria-modal="true"
      aria-label={`Image ${i + 1} of ${images.length}`}
      className="fixed inset-0 z-[100] flex flex-col bg-black/90 backdrop-blur-sm animate-fade-in"
      onClick={onClose}
    >
      <div className="flex items-center justify-between gap-3 px-4 py-3 text-white/90" onClick={(e) => e.stopPropagation()}>
        <p className="min-w-0 truncate text-sm">
          {img.fileName} <span className="text-white/50">· {fileSize(img.sizeBytes)}</span>
        </p>
        <div className="flex items-center gap-1">
          <a
            href={img.url}
            download={img.fileName}
            target="_blank"
            rel="noopener noreferrer"
            className="flex h-10 w-10 items-center justify-center rounded-full hover:bg-white/10"
            aria-label="Download image"
          >
            <Download className="h-5 w-5" />
          </a>
          <button type="button" onClick={onClose} className="flex h-10 w-10 items-center justify-center rounded-full hover:bg-white/10" aria-label="Close">
            <X className="h-5 w-5" />
          </button>
        </div>
      </div>
      <div className="relative flex min-h-0 flex-1 items-center justify-center px-2 pb-6 sm:px-16">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          key={img.id}
          src={img.url}
          alt={img.fileName}
          onClick={(e) => e.stopPropagation()}
          className="max-h-full max-w-full rounded-lg object-contain shadow-2xl animate-pop-in"
        />
        {images.length > 1 && (
          <>
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                go(-1);
              }}
              className="absolute left-2 top-1/2 flex h-11 w-11 -translate-y-1/2 items-center justify-center rounded-full bg-white/10 text-white hover:bg-white/20 sm:left-4"
              aria-label="Previous image"
            >
              <ChevronLeft className="h-6 w-6" />
            </button>
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                go(1);
              }}
              className="absolute right-2 top-1/2 flex h-11 w-11 -translate-y-1/2 items-center justify-center rounded-full bg-white/10 text-white hover:bg-white/20 sm:right-4"
              aria-label="Next image"
            >
              <ChevronRight className="h-6 w-6" />
            </button>
          </>
        )}
      </div>
    </div>,
    document.body,
  );
}

/* -------------------------------------------------------------------------- */
/* Attachments                                                                 */
/* -------------------------------------------------------------------------- */

export function Attachments({ items, compact }: { items: CommunityAttachmentView[]; compact?: boolean }) {
  const [open, setOpen] = useState<number | null>(null);
  const images = items.filter((a) => a.kind === "IMAGE");
  const docs = items.filter((a) => a.kind !== "IMAGE");
  if (items.length === 0) return null;

  const grid =
    images.length === 1
      ? "grid-cols-1"
      : images.length === 2
        ? "grid-cols-2"
        : "grid-cols-2";

  return (
    <div className="mt-2 space-y-2">
      {images.length > 0 && (
        <div className={cn("grid max-w-xl gap-1.5 overflow-hidden rounded-xl", grid)}>
          {images.map((a, idx) => (
            <button
              key={a.id}
              type="button"
              onClick={() => setOpen(idx)}
              className={cn(
                "group relative overflow-hidden bg-secondary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                images.length === 1 ? "rounded-xl" : "rounded-md",
                images.length === 3 && idx === 0 && "row-span-2",
              )}
              aria-label={`Open image ${a.fileName}`}
            >
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={a.url}
                alt={a.fileName}
                loading="lazy"
                className={cn(
                  "w-full object-cover transition-transform duration-300 group-hover:scale-[1.02]",
                  images.length === 1 ? (compact ? "max-h-56" : "max-h-[22rem]") : "h-full min-h-32 max-h-60",
                )}
              />
              <span className="pointer-events-none absolute inset-0 bg-black/0 transition-colors group-hover:bg-black/10" />
            </button>
          ))}
        </div>
      )}
      {docs.map((a) => (
        <div
          key={a.id}
          className="flex max-w-md items-center gap-3 rounded-xl border border-border bg-card p-3 shadow-sm transition-colors hover:border-foreground/20"
        >
          <span className="flex h-11 w-9 shrink-0 flex-col items-center justify-center rounded-md bg-destructive/10 text-destructive">
            <FileText className="h-4 w-4" />
            <span className="text-[9px] font-bold">{a.kind === "PDF" ? "PDF" : "FILE"}</span>
          </span>
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium">{a.fileName}</p>
            <p className="text-xs text-muted-foreground">
              {a.kind === "PDF" ? "PDF document" : a.contentType} · {fileSize(a.sizeBytes)}
            </p>
          </div>
          <a
            href={a.url}
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-lg px-2.5 py-1.5 text-xs font-medium text-primary hover:bg-primary/10"
          >
            Open
          </a>
          <a
            href={a.url}
            download={a.fileName}
            className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground"
            aria-label={`Download ${a.fileName}`}
          >
            <Download className="h-4 w-4" />
          </a>
        </div>
      ))}
      {open !== null && <Lightbox images={images} index={open} onClose={() => setOpen(null)} />}
    </div>
  );
}

/* -------------------------------------------------------------------------- */
/* Link previews                                                               */
/* -------------------------------------------------------------------------- */

/** A YouTube video id from any of its URL shapes, or null. */
export function youtubeId(raw: string): string | null {
  try {
    const u = new URL(raw);
    const host = u.hostname.replace(/^www\.|^m\./, "");
    let id: string | null = null;
    if (host === "youtu.be") id = u.pathname.slice(1).split("/")[0];
    else if (host === "youtube.com" || host === "youtube-nocookie.com") {
      if (u.pathname === "/watch") id = u.searchParams.get("v");
      else if (/^\/(embed|shorts|live)\//.test(u.pathname)) id = u.pathname.split("/")[2];
    }
    return id && /^[A-Za-z0-9_-]{6,15}$/.test(id) ? id : null;
  } catch {
    return null;
  }
}

/**
 * Previews built from the URL alone. Nothing is fetched from the linked site on
 * our servers (no SSRF surface) and nothing third-party loads until the
 * student asks: a YouTube thumbnail is an image from YouTube's own image host,
 * and the player is the privacy-enhanced nocookie embed, only after a click.
 */
export function LinkPreviews({ urls }: { urls: string[] }) {
  return (
    <div className="mt-2 space-y-2">
      {urls.map((u) => {
        const yt = youtubeId(u);
        return yt ? <YouTubeCard key={u} id={yt} url={u} /> : <LinkCard key={u} url={u} />;
      })}
    </div>
  );
}

function YouTubeCard({ id, url }: { id: string; url: string }) {
  const [play, setPlay] = useState(false);
  return (
    <div className="max-w-md overflow-hidden rounded-xl border border-border bg-card shadow-sm">
      <div className="relative aspect-video bg-black">
        {play ? (
          <iframe
            src={`https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`}
            title="YouTube video"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            sandbox="allow-scripts allow-same-origin allow-presentation allow-popups"
            className="absolute inset-0 h-full w-full"
          />
        ) : (
          <button type="button" onClick={() => setPlay(true)} className="group absolute inset-0" aria-label="Play video">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={`https://i.ytimg.com/vi/${id}/hqdefault.jpg`} alt="" loading="lazy" className="h-full w-full object-cover opacity-90" />
            <span className="absolute inset-0 flex items-center justify-center">
              <span className="flex h-14 w-14 items-center justify-center rounded-full bg-black/70 text-white shadow-lg transition-transform group-hover:scale-110">
                <Play className="ml-1 h-6 w-6 fill-current" />
              </span>
            </span>
          </button>
        )}
      </div>
      <a href={url} target="_blank" rel="noopener noreferrer nofollow" className="flex items-center gap-2 px-3 py-2 text-xs text-muted-foreground hover:text-foreground">
        <Play className="h-3.5 w-3.5 text-destructive" /> YouTube <ExternalLink className="ml-auto h-3.5 w-3.5" />
      </a>
    </div>
  );
}

export function LinkCard({ url, title, description }: { url: string; title?: string | null; description?: string | null }) {
  let host = url;
  let path = "";
  try {
    const u = new URL(url);
    host = u.hostname.replace(/^www\./, "");
    path = (u.pathname + u.search).replace(/\/$/, "");
  } catch {
    /* shown as typed */
  }
  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer nofollow ugc"
      className="group flex max-w-md items-center gap-3 rounded-xl border border-border bg-card p-3 shadow-sm transition-all hover:-translate-y-px hover:border-primary/40 hover:shadow-md"
    >
      <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
        <Globe className="h-5 w-5" />
      </span>
      <span className="min-w-0 flex-1">
        <span className="block truncate text-sm font-semibold group-hover:text-primary">{title || host}</span>
        <span className="block truncate text-xs text-muted-foreground">{description || (title ? host + path : path || "Open link")}</span>
      </span>
      <ExternalLink className="h-4 w-4 shrink-0 text-muted-foreground group-hover:text-primary" />
    </a>
  );
}
