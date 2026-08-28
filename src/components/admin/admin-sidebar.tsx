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
  Handshake,
  Megaphone,
  ScrollText,
  GraduationCap,
  AlertTriangle,
  BadgeCheck,
  CalendarCheck,
  FlaskConical,
  School,
  TrendingUp,
  UserPlus,
} from "lucide-react";

import { cn } from "@/lib/utils";

interface AdminNavItem {
  href: string;
  label: string;
  icon: typeof LayoutDashboard;
  exact?: boolean;
}

/**
 * Two admin panels behind one URL space.
 *
 * The single list had SAT content, IELTS content and IELTS review queues
 * interleaved, so an admin looking for the Writing queue read past PDF
 * Ingestion and the Question Bank to find it — and a reviewer who only ever
 * touches IELTS saw fourteen SAT entries they will never open. The two products
 * are run by different people doing different work, and the sidebar now says so.
 *
 * The routes are unchanged. Which panel you are in is derived from the path,
 * so a bookmarked `/admin/ielts/writing` still lands in the IELTS panel with
 * the right sidebar, and no state has to be stored anywhere.
 */
const SAT_NAV: AdminNavItem[] = [
  { href: "/admin", label: "Overview", icon: LayoutDashboard, exact: true },
  { href: "/admin/uploads", label: "PDF Ingestion", icon: UploadCloud },
  { href: "/admin/tests", label: "Tests & Modules", icon: BookOpenText },
  { href: "/admin/questions", label: "Question Bank", icon: ListChecks },
  { href: "/admin/content-health", label: "Content Health", icon: AlertTriangle },
  { href: "/admin/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
  { href: "/admin/bookings", label: "Sessions", icon: CalendarCheck },
  { href: "/admin/peer-mentors", label: "Peer Mentors", icon: BadgeCheck },
  { href: "/admin/research", label: "Research", icon: FlaskConical },
  { href: "/admin/schools", label: "Schools", icon: School },
  { href: "/admin/team", label: "Team Page", icon: Users },
  { href: "/admin/economy", label: "Economy", icon: Coins },
  { href: "/admin/partners", label: "Partners", icon: Handshake },
  { href: "/admin/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/admin/statistics", label: "Statistics", icon: TrendingUp },
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

/** Shared by both panels — these are about the platform, not either exam. */
const COMMON_NAV: AdminNavItem[] = [
  { href: "/admin/users", label: "Users", icon: Users },
  { href: "/admin/announcements", label: "Announcements", icon: Megaphone },
  { href: "/admin/logs", label: "System Logs", icon: ScrollText },
];

function NavLink({ item, pathname }: { item: AdminNavItem; pathname: string }) {
  const active = item.exact ? pathname === item.href : pathname.startsWith(item.href);
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
  const inIelts = pathname.startsWith("/admin/ielts");
  const nav = inIelts ? IELTS_NAV : SAT_NAV;

  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-card/40 lg:flex lg:flex-col">
      <div className="flex h-16 items-center gap-2 border-b border-border px-6">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-900 text-white">
          <GraduationCap className="h-4 w-4" />
        </span>
        <span className="font-display text-base font-semibold">Scholarly Admin</span>
      </div>

      {/* The same SAT | IELTS control students have at the top of the app, so
          the two halves of the product are switched the same way on both
          sides. Each lands on that panel's own overview. */}
      <div className="border-b border-border p-3">
        <div className="flex rounded-lg border border-border bg-secondary/50 p-0.5">
          <Link
            href="/admin"
            className={cn(
              "flex-1 rounded-md px-3 py-1.5 text-center text-xs font-semibold transition-colors",
              inIelts
                ? "text-muted-foreground hover:text-foreground"
                : "bg-card text-foreground shadow-soft"
            )}
          >
            SAT
          </Link>
          <Link
            href="/admin/ielts"
            className={cn(
              "flex-1 rounded-md px-3 py-1.5 text-center text-xs font-semibold transition-colors",
              inIelts
                ? "bg-card text-foreground shadow-soft"
                : "text-muted-foreground hover:text-foreground"
            )}
          >
            IELTS
          </Link>
        </div>
      </div>

      <nav className="flex-1 space-y-1 overflow-y-auto p-3">
        {nav.map((item) => (
          <NavLink key={item.href} item={item} pathname={pathname} />
        ))}

        <div className="!mt-4 space-y-1 border-t border-border pt-3">
          <p className="px-3 pb-1 text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">
            Platform
          </p>
          {COMMON_NAV.map((item) => (
            <NavLink key={item.href} item={item} pathname={pathname} />
          ))}
        </div>
      </nav>
    </aside>
  );
}
