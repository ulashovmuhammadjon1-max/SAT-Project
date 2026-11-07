"use client";

import {
  Atom,
  Award,
  BookOpen,
  Bookmark,
  Briefcase,
  Calculator,
  Code2,
  Coffee,
  FlaskConical,
  Globe2,
  GraduationCap,
  Hand,
  Hash,
  Heart,
  Languages,
  Library,
  Lightbulb,
  Megaphone,
  MessagesSquare,
  Music,
  PenLine,
  Sigma,
  Sparkles,
  Trophy,
  type LucideIcon,
} from "lucide-react";

import { useEffect, useState } from "react";

import { cn } from "@/lib/utils";

/**
 * False on the server and during hydration, true after. Anything that depends
 * on the reader's timezone or the current time (clock times, "2h ago", "Today"
 * separators) waits for this, or the server's UTC rendering and the browser's
 * local one disagree and React throws away the server HTML.
 */
export function useMounted() {
  const [m, setM] = useState(false);
  useEffect(() => setM(true), []);
  return m;
}

/** A time that renders only in the browser, in the reader's own timezone. */
export function LocalStamp({ iso, mode = "clock", className }: { iso: string; mode?: "clock" | "relative" | "full"; className?: string }) {
  const mounted = useMounted();
  const text = !mounted
    ? ""
    : mode === "clock"
      ? clockTime(iso)
      : mode === "relative"
        ? relativeTime(iso)
        : new Date(iso).toLocaleString();
  return (
    <time dateTime={iso} title={mounted ? new Date(iso).toLocaleString() : undefined} className={className} suppressHydrationWarning>
      {text}
    </time>
  );
}

const ICONS: Record<string, LucideIcon> = {
  hash: Hash,
  messages: MessagesSquare,
  megaphone: Megaphone,
  trophy: Trophy,
  lightbulb: Lightbulb,
  hand: Hand,
  sigma: Sigma,
  "book-open": BookOpen,
  languages: Languages,
  award: Award,
  flask: FlaskConical,
  library: Library,
  graduation: GraduationCap,
  calculator: Calculator,
  atom: Atom,
  globe: Globe2,
  code: Code2,
  pen: PenLine,
  coffee: Coffee,
  briefcase: Briefcase,
  music: Music,
  heart: Heart,
  sparkles: Sparkles,
  bookmark: Bookmark,
};

export function channelIcon(key: string): LucideIcon {
  return ICONS[key] ?? Hash;
}

export function ChannelIcon({ icon, className }: { icon: string; className?: string }) {
  const Icon = channelIcon(icon);
  return <Icon className={cn("h-4 w-4", className)} aria-hidden />;
}

/** Deterministic, theme-aware tint per person, so the same student is always the same colour. */
const TINTS = [
  "bg-[hsl(226_80%_60%/0.16)] text-[hsl(226_75%_52%)]",
  "bg-[hsl(152_55%_45%/0.16)] text-[hsl(152_55%_36%)]",
  "bg-[hsl(28_85%_55%/0.18)] text-[hsl(24_80%_42%)]",
  "bg-[hsl(262_70%_62%/0.16)] text-[hsl(262_60%_52%)]",
  "bg-[hsl(340_70%_58%/0.15)] text-[hsl(340_62%_48%)]",
  "bg-[hsl(190_75%_45%/0.16)] text-[hsl(192_75%_36%)]",
];

function hash(s: string): number {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0;
  return Math.abs(h);
}

export function initials(name: string): string {
  return (
    name
      .replace(/\./g, "")
      .split(/\s+/)
      .filter(Boolean)
      .slice(0, 2)
      .map((p) => p[0])
      .join("")
      .toUpperCase() || "?"
  );
}

export function MemberAvatar({
  id,
  name,
  image,
  size = 36,
  isAdmin,
  online,
  className,
}: {
  id: string;
  name: string;
  image?: string | null;
  size?: number;
  isAdmin?: boolean;
  online?: boolean;
  className?: string;
}) {
  const style = { width: size, height: size, fontSize: Math.max(10, Math.round(size * 0.36)) };
  return (
    <span className={cn("relative inline-flex shrink-0", className)} style={{ width: size, height: size }}>
      {image ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={image}
          alt=""
          referrerPolicy="no-referrer"
          className="h-full w-full rounded-full object-cover ring-1 ring-border"
          style={style}
        />
      ) : (
        <span
          aria-hidden
          style={style}
          className={cn(
            "flex items-center justify-center rounded-full font-semibold tracking-tight",
            isAdmin ? "bg-foreground text-background" : TINTS[hash(id) % TINTS.length],
          )}
        >
          {initials(name)}
        </span>
      )}
      {online && (
        <span
          className="absolute -bottom-0.5 -right-0.5 h-3 w-3 rounded-full border-2 border-background bg-success"
          aria-label="Active now"
        />
      )}
    </span>
  );
}

export function relativeTime(iso: string, now = Date.now()): string {
  const t = new Date(iso).getTime();
  const s = Math.max(0, Math.round((now - t) / 1000));
  if (s < 45) return "just now";
  const m = Math.round(s / 60);
  if (m < 60) return `${m}m ago`;
  const h = Math.round(m / 60);
  if (h < 24) return `${h}h ago`;
  const d = Math.round(h / 24);
  if (d < 7) return `${d}d ago`;
  return new Date(iso).toLocaleDateString(undefined, { day: "numeric", month: "short" });
}

export function clockTime(iso: string): string {
  return new Date(iso).toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });
}

export function dayLabel(iso: string): string {
  const d = new Date(iso);
  const today = new Date();
  const yesterday = new Date(Date.now() - 86_400_000);
  if (d.toDateString() === today.toDateString()) return "Today";
  if (d.toDateString() === yesterday.toDateString()) return "Yesterday";
  return d.toLocaleDateString(undefined, { weekday: "long", day: "numeric", month: "long" });
}

export function fileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

/** Shown beside names: a moderator or a verified peer mentor. */
export function RoleBadge({ isAdmin, isMentor }: { isAdmin?: boolean; isMentor?: boolean }) {
  if (isAdmin)
    return (
      <span className="rounded-md bg-foreground px-1.5 py-px text-[10px] font-semibold uppercase tracking-wider text-background">
        Team
      </span>
    );
  if (isMentor)
    return (
      <span className="rounded-md bg-primary/10 px-1.5 py-px text-[10px] font-semibold uppercase tracking-wider text-primary">
        Mentor
      </span>
    );
  return null;
}
