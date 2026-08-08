"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  UploadCloud,
  ListChecks,
  BookOpenText,
  SpellCheck2,
  Users,
  BarChart3,
  Sliders,
  Megaphone,
  ScrollText,
  GraduationCap,
  AlertTriangle,
  CalendarCheck,
} from "lucide-react";

import { cn } from "@/lib/utils";

const NAV = [
  { href: "/admin", label: "Overview", icon: LayoutDashboard, exact: true },
  { href: "/admin/uploads", label: "PDF Ingestion", icon: UploadCloud },
  { href: "/admin/tests", label: "Tests & Modules", icon: BookOpenText },
  { href: "/admin/questions", label: "Question Bank", icon: ListChecks },
  { href: "/admin/content-health", label: "Content Health", icon: AlertTriangle },
  { href: "/admin/vocabulary", label: "Vocabulary", icon: SpellCheck2 },
  { href: "/admin/bookings", label: "Sessions", icon: CalendarCheck },
  { href: "/admin/users", label: "Users", icon: Users },
  { href: "/admin/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/admin/settings", label: "Adaptive Settings", icon: Sliders },
  { href: "/admin/announcements", label: "Announcements", icon: Megaphone },
  { href: "/admin/logs", label: "System Logs", icon: ScrollText },
];

export function AdminSidebar() {
  const pathname = usePathname();

  return (
    <aside className="hidden w-64 shrink-0 border-r border-border bg-card/40 lg:flex lg:flex-col">
      <div className="flex h-16 items-center gap-2 border-b border-border px-6">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-navy-900 text-white">
          <GraduationCap className="h-4 w-4" />
        </span>
        <span className="font-display text-base font-semibold">Summit Admin</span>
      </div>
      <nav className="flex-1 space-y-1 overflow-y-auto p-3">
        {NAV.map((item) => {
          const active = item.exact ? pathname === item.href : pathname.startsWith(item.href);
          return (
            <Link
              key={item.href}
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
        })}
      </nav>
    </aside>
  );
}
