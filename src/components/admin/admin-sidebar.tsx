"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  UploadCloud,
  ListChecks,
  Globe2,
  Microscope,
  PenLine,
  Mic,
  BookOpenText,
  SpellCheck2,
  Users,
  BarChart3,
  Sliders,
  Coins,
  HandCoins,
  Megaphone,
  ScrollText,
  GraduationCap,
  AlertTriangle,
  BadgeCheck,
  CalendarCheck,
  CalendarPlus,
  FlaskConical,
  School,
  TrendingUp,
  UserPlus,
  UsersRound,
} from "lucide-react";

import { cn } from "@/lib/utils";

interface AdminNavItem {
  href: string;
  label: string;
  icon: typeof LayoutDashboard;
  exact?: boolean;
}

/**
 * Four admin sections behind one URL space: Scholarly (the platform as a
 * whole), SAT, IELTS and Research.
 *
 * A single list mixed SAT content, IELTS review queues, research decisions and
 * platform settings, so finding one page meant reading past fifteen others.
 * Each section is run as its own piece of work, and the sidebar now shows only
 * that section's pages.
 *
 * The routes are unchanged. Which section you are in is derived from the path
 * (see `sectionFor`), so a bookmarked `/admin/ielts/writing` still lands in the
 * IELTS section with the right sidebar, and no state is stored anywhere.
 */
type Section = "scholarly" | "sat" | "ielts" | "research";

const SECTIONS: { id: Section; label: string; href: string }[] = [
  { id: "scholarly", label: "Scholarly", href: "/admin" },
  { id: "sat", label: "SAT", href: "/admin/sat" },
  { id: "ielts", label: "IELTS", href: "/admin/ielts" },
  { id: "research", label: "Research", href: "/admin/research" },
];

/** The platform: people, sessions, communication, money, and logs. */
const SCHOLARLY_NAV: AdminNavItem[] = [
  { href: "/admin", label: "Overview", icon: LayoutDashboard, exact: true },
  { href: "/admin/users", label: "Users", icon: Users },
  { href: "/admin/announcements", label: "Announcements", icon: Megaphone },
  { href: "/admin/my-sessions", label: "My Sessions", icon: CalendarPlus },
  { href: "/admin/bookings", label: "Sessions", icon: CalendarCheck },
  { href: "/admin/peer-mentors", label: "Peer Mentors", icon: BadgeCheck },
  { href: "/admin/schools", label: "Schools", icon: School },
  { href: "/admin/team", label: "Team Page", icon: UsersRound },
  { href: "/admin/coins", label: "Give Coins", icon: HandCoins },
  { href: "/admin/economy", label: "Economy", icon: Coins },
  { href: "/admin/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/admin/logs", label: "System Logs", icon: ScrollText },
];

const SAT_NAV: AdminNavItem[] = [
  { href: "/admin/sat", label: "Overview", icon: LayoutDashboard, exact: true },
  { href: "/admin/uploads", label: "PDF Ingestion", icon: UploadCloud },
  { href: "/admin/tests", label: "Tests & Modules", icon: BookOpenText },
  { href: "/admin/questions", label: "Question Bank", icon: ListChecks },
  { href: "/admin/content-health", label: "Content Health", icon: AlertTriangle },
  { href: "/admin/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
  { href: "/admin/statistics", label: "Statistics", icon: TrendingUp, exact: true },
  { href: "/admin/settings", label: "Adaptive Settings", icon: Sliders },
];

const IELTS_NAV: AdminNavItem[] = [
  { href: "/admin/ielts", label: "Overview", icon: LayoutDashboard, exact: true },
  { href: "/admin/ielts/writing", label: "Writing Reviews", icon: PenLine },
  { href: "/admin/ielts/speaking", label: "Speaking Reviews", icon: Mic },
  { href: "/admin/ielts/economy", label: "Reviews & Invites", icon: UserPlus },
  { href: "/admin/ielts/essays", label: "Task 2 Essays", icon: Microscope },
  { href: "/admin/ielts/papers", label: "Papers", icon: Globe2 },
];

const RESEARCH_NAV: AdminNavItem[] = [
  { href: "/admin/research", label: "Proposals", icon: FlaskConical },
];

const NAV: Record<Section, AdminNavItem[]> = {
  scholarly: SCHOLARLY_NAV,
  sat: SAT_NAV,
  ielts: IELTS_NAV,
  research: RESEARCH_NAV,
};

const SAT_PREFIXES = [
  "/admin/sat",
  "/admin/uploads",
  "/admin/tests",
  "/admin/questions",
  "/admin/content-health",
  "/admin/vocabulary",
  "/admin/settings",
];

function under(pathname: string, prefix: string) {
  return pathname === prefix || pathname.startsWith(prefix + "/");
}

/**
 * Which section a path belongs to. A student's profile page lives under
 * /admin/statistics/students but is reached from Users, so it stays in the
 * Scholarly section; the Statistics page itself is SAT (test funnel, scores).
 */
function sectionFor(pathname: string): Section {
  if (under(pathname, "/admin/ielts")) return "ielts";
  if (under(pathname, "/admin/research")) return "research";
  if (under(pathname, "/admin/statistics/students")) return "scholarly";
  if (under(pathname, "/admin/statistics") || SAT_PREFIXES.some((p) => under(pathname, p))) return "sat";
  return "scholarly";
}

function NavLink({ item, pathname }: { item: AdminNavItem; pathname: string }) {
  const active = item.exact ? pathname === item.href : under(pathname, item.href);
  return (
    <Link
      href={item.href}
      className={cn(
        "flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors",
        active
          ? "bg-primary text-primary-foreground shadow-soft"
          : "text-muted-foreground hover:bg-secondary hover:text-foreground"
      )}
    >
      <item.icon className="h-4 w-4" />
      {item.label}
    </Link>
  );
}

export function AdminSidebar() {
  const pathname = usePathname();
  const section = sectionFor(pathname);

  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-card/40 lg:flex lg:flex-col">
      <div className="flex h-16 items-center gap-2 border-b border-border px-6">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-900 text-white">
          <GraduationCap className="h-4 w-4" />
        </span>
        <span className="font-display text-base font-semibold">Scholarly Admin</span>
      </div>

      {/* Section switcher. Each option lands on that section's own overview. */}
      <div className="border-b border-border p-3">
        <div
          role="tablist"
          aria-label="Admin section"
          className="grid grid-cols-2 gap-0.5 rounded-lg border border-border bg-secondary/50 p-0.5"
        >
          {SECTIONS.map((s) => (
            <Link
              key={s.id}
              href={s.href}
              role="tab"
              aria-selected={section === s.id}
              className={cn(
                "rounded-md px-3 py-1.5 text-center text-xs font-semibold transition-colors",
                section === s.id
                  ? "bg-card text-foreground shadow-soft"
                  : "text-muted-foreground hover:text-foreground"
              )}
            >
              {s.label}
            </Link>
          ))}
        </div>
      </div>

      <nav className="flex-1 space-y-1 overflow-y-auto p-3">
        {NAV[section].map((item) => (
          <NavLink key={item.href} item={item} pathname={pathname} />
        ))}
      </nav>
    </aside>
  );
}
