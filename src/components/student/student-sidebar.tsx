"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
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
  Globe2,
} from "lucide-react";

import { cn } from "@/lib/utils";

const NAV = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard, exact: true },
  { href: "/daily", label: "Daily Challenge", icon: CalendarDays },
  { href: "/plan", label: "My SAT Plan", icon: Target },
  { href: "/tests", label: "Practice Tests", icon: BookOpen },
  { href: "/ielts", label: "IELTS", icon: Globe2 },
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

export function StudentSidebar() {
  const pathname = usePathname();

  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-card/40 lg:flex lg:flex-col">
      <Link href="/dashboard" className="flex h-16 items-center gap-2 border-b border-border px-6">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-900 text-white">
          <GraduationCap className="h-4 w-4" />
        </span>
        <span className="font-display text-base font-semibold">SATForge</span>
      </Link>
      <nav className="flex-1 space-y-1 overflow-y-auto p-3">
        {NAV.map((item) => {
          const active = item.exact ? pathname === item.href : pathname.startsWith(item.href);
          return (
            <Link
              key={item.href}
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
