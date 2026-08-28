"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import type { ExamMode } from "@prisma/client";
import {
  LayoutDashboard,
  BookOpen,
  ListChecks,
  SpellCheck2,
  Bookmark,
  BarChart3,
  BadgeCheck,
  CalendarCheck,
  CalendarRange,
  Coins,
  FlaskConical,
  Target,
  UserPlus,
  Settings,
  GraduationCap,
  Award,
  CalendarDays,
  ChevronDown,
  School,
  Trophy,
  MessagesSquare,
  PenLine,
  Mic,
  MessageSquareText,
  Microscope,
} from "lucide-react";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { toast } from "sonner";

import { setActiveExam } from "@/server/actions/student/exam-mode";
import { cn } from "@/lib/utils";

interface NavItem {
  href: string;
  label: string;
  icon: typeof LayoutDashboard;
  exact?: boolean;
  /** Small pill next to the label, for genuinely new programmes. */
  badge?: string;
}

/** A labelled group of links, OnePrep-style: PRACTICE, PROGRESS, ... */
interface NavGroup {
  /** Null renders the items with no heading (the Home block). */
  label: string | null;
  items: NavItem[];
}

const SAT_GROUPS: NavGroup[] = [
  { label: null, items: [{ href: "/dashboard", label: "Home", icon: LayoutDashboard, exact: true }] },
  {
    label: "Practice",
    items: [
      { href: "/tests", label: "Full-Length Tests", icon: BookOpen },
      { href: "/practice", label: "Question Bank", icon: ListChecks },
      { href: "/daily", label: "Daily Challenge", icon: CalendarDays },
      { href: "/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
    ],
  },
  {
    label: "Progress",
    items: [
      { href: "/plan", label: "My SAT Plan", icon: Target },
      { href: "/analytics", label: "Analytics", icon: BarChart3 },
      { href: "/bookmarks", label: "Saved Questions", icon: Bookmark },
      { href: "/achievements", label: "Achievements", icon: Award },
    ],
  },
  {
    label: "Community",
    items: [
      { href: "/community", label: "Community", icon: MessagesSquare },
      { href: "/leaderboard", label: "Leaderboard", icon: Trophy },
      { href: "/events", label: "Events", icon: CalendarRange },
      { href: "/invite", label: "Invite Friends", icon: UserPlus },
    ],
  },
  {
    label: "Mentorship",
    items: [
      { href: "/bookings", label: "My Sessions", icon: CalendarCheck },
      { href: "/mentor", label: "Peer-Mentor Programme", icon: BadgeCheck, badge: "New" },
      { href: "/wallet", label: "Coins", icon: Coins },
    ],
  },
  { label: null, items: [{ href: "/settings", label: "Settings", icon: Settings }] },
];

const IELTS_GROUPS: NavGroup[] = [
  { label: null, items: [{ href: "/ielts", label: "Home", icon: LayoutDashboard, exact: true }] },
  {
    label: "Practice",
    items: [
      { href: "/ielts/writing", label: "Writing", icon: PenLine },
      { href: "/ielts/speaking", label: "Speaking", icon: Mic },
      { href: "/ielts/essays", label: "Essay Analyzer", icon: Microscope },
    ],
  },
  {
    label: "Progress",
    items: [
      { href: "/ielts/plan", label: "My IELTS Plan", icon: Target },
      { href: "/ielts/feedback", label: "My Feedback", icon: MessageSquareText },
      { href: "/ielts/leaderboard", label: "Leaderboard", icon: Trophy },
    ],
  },
  {
    label: "Community",
    items: [
      { href: "/community", label: "Community", icon: MessagesSquare },
      { href: "/ielts/invite", label: "Invite Friends", icon: UserPlus },
    ],
  },
  {
    label: "Mentorship",
    items: [{ href: "/mentor", label: "Peer-Mentor Programme", icon: BadgeCheck, badge: "New" }],
  },
  { label: null, items: [{ href: "/settings", label: "Settings", icon: Settings }] },
];

const BOTH_GROUPS: NavGroup[] = [
  { label: null, items: [{ href: "/dashboard", label: "Home", icon: LayoutDashboard, exact: true }] },
  {
    label: "SAT",
    items: [
      { href: "/tests", label: "Full-Length Tests", icon: BookOpen },
      { href: "/practice", label: "Question Bank", icon: ListChecks },
      { href: "/daily", label: "Daily Challenge", icon: CalendarDays },
      { href: "/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
      { href: "/plan", label: "My SAT Plan", icon: Target },
    ],
  },
  {
    label: "IELTS",
    items: [
      { href: "/ielts/writing", label: "Writing", icon: PenLine },
      { href: "/ielts/speaking", label: "Speaking", icon: Mic },
      { href: "/ielts/essays", label: "Essay Analyzer", icon: Microscope },
      { href: "/ielts/plan", label: "My IELTS Plan", icon: Target },
      { href: "/ielts/feedback", label: "My Feedback", icon: MessageSquareText },
    ],
  },
  {
    label: "Progress",
    items: [
      { href: "/analytics", label: "Analytics", icon: BarChart3 },
      { href: "/bookmarks", label: "Saved Questions", icon: Bookmark },
      { href: "/achievements", label: "Achievements", icon: Award },
    ],
  },
  {
    label: "Community",
    items: [
      { href: "/community", label: "Community", icon: MessagesSquare },
      { href: "/leaderboard", label: "Leaderboard", icon: Trophy },
      { href: "/events", label: "Events", icon: CalendarRange },
      { href: "/invite", label: "Invite Friends", icon: UserPlus },
    ],
  },
  {
    label: "Mentorship",
    items: [
      { href: "/bookings", label: "My Sessions", icon: CalendarCheck },
      { href: "/mentor", label: "Peer-Mentor Programme", icon: BadgeCheck, badge: "New" },
      { href: "/wallet", label: "Coins", icon: Coins },
    ],
  },
  { label: null, items: [{ href: "/settings", label: "Settings", icon: Settings }] },
];

const GROUPS_FOR: Record<ExamMode, NavGroup[]> = {
  SAT: SAT_GROUPS,
  IELTS: IELTS_GROUPS,
  BOTH: BOTH_GROUPS,
};

export function StudentSidebar({ activeExam = "SAT" }: { activeExam?: ExamMode }) {
  const pathname = usePathname();
  const groups = GROUPS_FOR[activeExam];
  const home = activeExam === "IELTS" ? "/ielts" : "/dashboard";

  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-card/40 lg:flex lg:flex-col">
      <Link href={home} className="flex h-16 items-center gap-2 border-b border-border px-6">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-900 text-white">
          <GraduationCap className="h-4 w-4" />
        </span>
        <span className="font-display text-base font-semibold">Scholarly</span>
      </Link>

      {/* Which programme this sidebar is showing. SAT by default; the chevron
          opens the other programmes — IELTS (switches the whole sidebar),
          Research, and School. */}
      <ProductMenu activeExam={activeExam} />

      <nav className="flex-1 space-y-4 overflow-y-auto p-3">
        {groups.map((group, gi) => (
          <div key={group.label ?? `plain-${gi}`} className="space-y-0.5">
            {group.label && (
              <p className="px-3 pb-1 pt-1 text-[10.5px] font-semibold uppercase tracking-[0.12em] text-muted-foreground/80">
                {group.label}
              </p>
            )}
            {group.items.map((item) => {
              // `exact` matters for the dashboards: without it, /ielts would
              // light up for every /ielts/* route at once.
              const active = item.exact ? pathname === item.href : pathname.startsWith(item.href);
              return (
                <Link
                  key={`${item.href}-${item.label}`}
                  href={item.href}
                  className={cn(
                    "group flex items-center gap-3 rounded-xl px-3 py-2 text-sm font-medium transition-all duration-200",
                    active
                      ? "bg-primary text-primary-foreground shadow-soft"
                      : "text-muted-foreground hover:translate-x-0.5 hover:bg-secondary hover:text-foreground"
                  )}
                >
                  <item.icon className="h-4 w-4 transition-transform duration-200 group-hover:scale-110" />
                  <span className="min-w-0 flex-1 truncate">{item.label}</span>
                  {item.badge && (
                    <span
                      className={cn(
                        "rounded-full px-1.5 py-0.5 text-[9px] font-bold uppercase tracking-wide",
                        active ? "bg-white/20 text-white" : "bg-primary/10 text-primary"
                      )}
                    >
                      {item.badge}
                    </span>
                  )}
                </Link>
              );
            })}
          </div>
        ))}
      </nav>
    </aside>
  );
}

/**
 * The programme menu, closed by default: the sidebar shows one programme (SAT
 * unless the student switched) and a single chevron reveals the rest — IELTS,
 * Research, School. Choosing IELTS/SAT swaps the whole sidebar via the same
 * server action the old segmented switcher used; Research and School are
 * ordinary links.
 */
function ProductMenu({ activeExam }: { activeExam: ExamMode }) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [pending, startTransition] = useTransition();

  const current = activeExam === "IELTS" ? "IELTS" : "SAT";
  const otherExam: ExamMode = current === "SAT" ? "IELTS" : "SAT";

  const switchExam = (mode: ExamMode) => {
    startTransition(async () => {
      const result = await setActiveExam(mode);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      setOpen(false);
      if (result.redirectTo) router.push(result.redirectTo);
      router.refresh();
    });
  };

  return (
    <div className="border-b border-border p-3">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        className="flex w-full items-center gap-2.5 rounded-xl border border-border bg-secondary/50 px-3 py-2 text-sm font-semibold transition-colors hover:bg-secondary"
      >
        <span className="flex h-6 w-6 items-center justify-center rounded-md bg-navy-900 text-[10px] font-bold text-white">
          {current === "SAT" ? "SAT" : "IE"}
        </span>
        {current === "SAT" ? "SAT Prep" : "IELTS Prep"}
        <ChevronDown
          className={cn(
            "ml-auto h-4 w-4 text-muted-foreground transition-transform duration-200",
            open && "rotate-180"
          )}
        />
      </button>

      {open && (
        <div className="mt-1.5 space-y-0.5 rounded-xl border border-border bg-card p-1.5 shadow-soft">
          <button
            type="button"
            disabled={pending}
            onClick={() => switchExam(otherExam)}
            className="flex w-full items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground disabled:opacity-60"
          >
            {otherExam === "IELTS" ? <PenLine className="h-4 w-4" /> : <BookOpen className="h-4 w-4" />}
            {otherExam === "IELTS" ? "IELTS Prep" : "SAT Prep"}
          </button>
          <Link
            href="/research"
            onClick={() => setOpen(false)}
            className="flex items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground"
          >
            <FlaskConical className="h-4 w-4" />
            Research
            <span className="ml-auto rounded-full bg-primary/10 px-1.5 py-0.5 text-[9px] font-bold uppercase tracking-wide text-primary">
              New
            </span>
          </Link>
          <Link
            href="/class"
            onClick={() => setOpen(false)}
            className="flex items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground"
          >
            <School className="h-4 w-4" />
            School
            <span className="ml-auto rounded-full bg-primary/10 px-1.5 py-0.5 text-[9px] font-bold uppercase tracking-wide text-primary">
              New
            </span>
          </Link>
        </div>
      )}
    </div>
  );
}
