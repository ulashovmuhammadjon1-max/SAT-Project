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
  CalendarCheck,
  CalendarRange,
  Coins,
  Target,
  UserPlus,
  Settings,
  GraduationCap,
  Award,
  CalendarDays,
  Trophy,
  MessagesSquare,
  PenLine,
  Mic,
  MessageSquareText,
  Microscope,
} from "lucide-react";

import { cn } from "@/lib/utils";

interface NavItem {
  href: string;
  label: string;
  icon: typeof LayoutDashboard;
  exact?: boolean;
}

/**
 * The SAT ecosystem's navigation. Unchanged from before the IELTS work — an
 * SAT-only student sees exactly the sidebar they have always seen.
 */
const SAT_NAV: NavItem[] = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard, exact: true },
  { href: "/daily", label: "Daily Challenge", icon: CalendarDays },
  { href: "/plan", label: "My SAT Plan", icon: Target },
  { href: "/tests", label: "Practice Tests", icon: BookOpen },
  { href: "/practice", label: "Question Bank", icon: ListChecks },
  { href: "/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
  { href: "/community", label: "Community", icon: MessagesSquare },
  { href: "/leaderboard", label: "Leaderboard", icon: Trophy },
  { href: "/achievements", label: "Achievements", icon: Award },
  { href: "/bookmarks", label: "Bookmarks", icon: Bookmark },
  { href: "/events", label: "Events", icon: CalendarRange },
  { href: "/bookings", label: "My Sessions", icon: CalendarCheck },
  { href: "/wallet", label: "Coins", icon: Coins },
  { href: "/invite", label: "Invite Friends", icon: UserPlus },
  { href: "/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/settings", label: "Settings", icon: Settings },
];

/**
 * The IELTS ecosystem's navigation.
 *
 * Writing and Speaking only. The other two skills, the question bank, practice
 * tests, vocabulary and the plan are deliberately absent: this product is the
 * free human-review loop, and a sidebar advertising sections that do not exist
 * is worse than a short one. Icons are skill-specific rather than reused from
 * the SAT set.
 */
const IELTS_NAV: NavItem[] = [
  { href: "/ielts", label: "Dashboard", icon: LayoutDashboard, exact: true },
  { href: "/ielts/plan", label: "My IELTS Plan", icon: Target },
  { href: "/ielts/writing", label: "Writing", icon: PenLine },
  { href: "/ielts/essays", label: "Essay Analyzer", icon: Microscope },
  { href: "/ielts/speaking", label: "Speaking", icon: Mic },
  { href: "/ielts/feedback", label: "My Feedback", icon: MessageSquareText },
  { href: "/ielts/leaderboard", label: "Leaderboard", icon: Trophy },
  { href: "/ielts/invite", label: "Invite Friends", icon: UserPlus },
  { href: "/community", label: "Community", icon: MessagesSquare },
  { href: "/settings", label: "Settings", icon: Settings },
];

/**
 * Both mode keeps one navigation with both plans reachable, rather than
 * concatenating the two lists — a twenty-eight item sidebar is not a product,
 * it is a wall. The exam-specific detail lives one click deeper, under each
 * exam's own hub.
 */
const BOTH_NAV: NavItem[] = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard, exact: true },
  { href: "/daily", label: "Daily Challenge", icon: CalendarDays },
  { href: "/plan", label: "My SAT Plan", icon: Target },
  { href: "/tests", label: "Practice Tests", icon: BookOpen },
  { href: "/practice", label: "Question Bank", icon: ListChecks },
  { href: "/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
  { href: "/ielts/plan", label: "My IELTS Plan", icon: Target },
  { href: "/ielts/writing", label: "IELTS Writing", icon: PenLine },
  { href: "/ielts/essays", label: "IELTS Essay Analyzer", icon: Microscope },
  { href: "/ielts/speaking", label: "IELTS Speaking", icon: Mic },
  { href: "/ielts/feedback", label: "IELTS Feedback", icon: MessageSquareText },
  { href: "/community", label: "Community", icon: MessagesSquare },
  { href: "/leaderboard", label: "Leaderboard", icon: Trophy },
  { href: "/achievements", label: "Achievements", icon: Award },
  { href: "/bookmarks", label: "Bookmarks", icon: Bookmark },
  { href: "/events", label: "Events", icon: CalendarRange },
  { href: "/bookings", label: "My Sessions", icon: CalendarCheck },
  { href: "/wallet", label: "Coins", icon: Coins },
  { href: "/invite", label: "Invite Friends", icon: UserPlus },
  { href: "/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/settings", label: "Settings", icon: Settings },
];

const NAV_FOR: Record<ExamMode, NavItem[]> = {
  SAT: SAT_NAV,
  IELTS: IELTS_NAV,
  BOTH: BOTH_NAV,
};

export function StudentSidebar({ activeExam = "SAT" }: { activeExam?: ExamMode }) {
  const pathname = usePathname();
  const nav = NAV_FOR[activeExam];
  const home = activeExam === "IELTS" ? "/ielts" : "/dashboard";

  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-card/40 lg:flex lg:flex-col">
      <Link href={home} className="flex h-16 items-center gap-2 border-b border-border px-6">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-900 text-white">
          <GraduationCap className="h-4 w-4" />
        </span>
        <span className="font-display text-base font-semibold">Scholarly</span>
      </Link>

      <nav className="flex-1 space-y-1 overflow-y-auto p-3">
        {nav.map((item) => {
          // `exact` matters for the two dashboards: without it, /ielts would
          // light up for every /ielts/* route at once.
          const active = item.exact
            ? pathname === item.href
            : pathname.startsWith(item.href);
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
              {item.label}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}
