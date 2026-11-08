"use client";

import { createContext, useCallback, useContext, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Bookmark,
  ChevronDown,
  Compass,
  Mail,
  PanelLeftOpen,
  Search,
  Settings,
  ShieldCheck,
  X,
} from "lucide-react";

import { useLive } from "@/components/live/live-provider";
import type { CategoryView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import { listCategories } from "@/server/actions/student/community";

import { ChannelIcon, MemberAvatar } from "./bits";

const ShellContext = createContext<{ openNav: () => void }>({ openNav: () => {} });

/** The hamburger shown in page headers on phones and tablets. */
export function NavToggle() {
  const { openNav } = useContext(ShellContext);
  return (
    <button
      type="button"
      onClick={openNav}
      aria-label="Open channels"
      className="-ml-1 flex h-10 w-10 shrink-0 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground lg:hidden"
    >
      {/* Not a hamburger: the app menu already owns that icon in the top
          bar, and two identical buttons one above the other read as one. */}
      <PanelLeftOpen className="h-5 w-5" />
    </button>
  );
}

export function CommunityShell({
  initialCategories,
  me,
  isAdmin,
  children,
}: {
  initialCategories: CategoryView[];
  me: { id: string; name: string; image: string | null };
  isAdmin: boolean;
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const { data } = useLive();
  const [categories, setCategories] = useState(initialCategories);
  const [drawer, setDrawer] = useState(false);
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({});
  const lastVersion = useRef<string | null>(null);

  useEffect(() => {
    try {
      setCollapsed(JSON.parse(localStorage.getItem("scholarly-collapsed-categories") ?? "{}"));
    } catch {
      /* ignore */
    }
  }, []);

  const refresh = useCallback(async () => setCategories(await listCategories()), []);

  // Unread counts follow the live stamp; reading a channel clears its badge.
  useEffect(() => {
    const v = `${data?.communityVersion ?? ""}|${data?.notificationsUnread ?? ""}`;
    if (lastVersion.current && v !== lastVersion.current) void refresh();
    lastVersion.current = v;
  }, [data?.communityVersion, data?.notificationsUnread, refresh]);

  useEffect(() => {
    setDrawer(false);
    // The channel just opened has been read.
    const t = setTimeout(() => void refresh(), 800);
    return () => clearTimeout(t);
  }, [pathname, refresh]);

  function toggle(id: string) {
    setCollapsed((c) => {
      const next = { ...c, [id]: !c[id] };
      try {
        localStorage.setItem("scholarly-collapsed-categories", JSON.stringify(next));
      } catch {
        /* ignore */
      }
      return next;
    });
  }

  const dmUnread = data?.dmUnread ?? 0;
  const nav = (
    <nav aria-label="Community" className="flex h-full flex-col">
      <div className="flex items-center gap-3 px-4 pb-3 pt-4">
        <MemberAvatar id={me.id} name={me.name} image={me.image} size={36} />
        <div className="min-w-0 flex-1">
          <p className="font-serif text-lg font-medium leading-none tracking-tight">Community</p>
          <p className="mt-1 truncate text-xs text-muted-foreground">{me.name}</p>
        </div>
        <button type="button" onClick={() => setDrawer(false)} aria-label="Close channels" className="rounded-lg p-1.5 text-muted-foreground hover:bg-secondary lg:hidden">
          <X className="h-5 w-5" />
        </button>
      </div>

      <div className="space-y-0.5 px-2">
        <ShellLink href="/community" icon={Compass} label="Home" active={pathname === "/community"} />
        <ShellLink href="/community/search" icon={Search} label="Search" active={pathname === "/community/search"} />
        <ShellLink href="/community/messages" icon={Mail} label="Messages" active={pathname.startsWith("/community/messages")} badge={dmUnread} />
        <ShellLink href="/community/bookmarks" icon={Bookmark} label="Saved" active={pathname === "/community/bookmarks"} />
      </div>

      <div className="mt-3 min-h-0 flex-1 overflow-y-auto px-2 pb-4">
        {categories.map((cat) => {
          const key = cat.id ?? "other";
          const isCollapsed = collapsed[key];
          const catUnread = cat.channels.reduce((n, c) => n + (c.muted ? 0 : c.unread), 0);
          return (
            <div key={key} className="mt-3">
              <button
                type="button"
                onClick={() => toggle(key)}
                aria-expanded={!isCollapsed}
                className="flex w-full items-center gap-1 px-2 py-1 text-[11px] font-semibold uppercase tracking-[0.12em] text-muted-foreground hover:text-foreground"
              >
                <ChevronDown className={cn("h-3 w-3 transition-transform", isCollapsed && "-rotate-90")} />
                {cat.name}
                {isCollapsed && catUnread > 0 && <span className="ml-auto h-1.5 w-1.5 rounded-full bg-primary" />}
              </button>
              {!isCollapsed && (
                <ul className="mt-0.5 space-y-px">
                  {cat.channels.map((c) => {
                    const href = `/community/${c.slug}`;
                    const active = pathname === href;
                    const unread = !c.muted && c.unread > 0;
                    return (
                      <li key={c.id}>
                        <Link
                          href={href}
                          title={c.description ?? c.name}
                          aria-current={active ? "page" : undefined}
                          className={cn(
                            "group relative flex items-center gap-2.5 rounded-lg px-2 py-1.5 text-[14px] transition-colors",
                            active
                              ? "bg-primary/10 font-semibold text-foreground"
                              : unread
                                ? "font-semibold text-foreground hover:bg-secondary/80"
                                : "text-muted-foreground hover:bg-secondary/80 hover:text-foreground",
                            c.muted && !active && "opacity-60",
                          )}
                        >
                          {active && <span className="absolute -left-2 top-1.5 bottom-1.5 w-1 rounded-r-full bg-primary" aria-hidden />}
                          <span
                            className={cn(
                              "flex h-7 w-7 shrink-0 items-center justify-center rounded-md transition-colors",
                              active ? "bg-primary text-primary-foreground shadow-sm" : "bg-secondary text-muted-foreground group-hover:text-foreground",
                            )}
                          >
                            <ChannelIcon icon={c.icon} className="h-3.5 w-3.5" />
                          </span>
                          <span className="min-w-0 flex-1 truncate">{c.name}</span>
                          {c.mentionsUnread > 0 ? (
                            <span className="flex h-5 min-w-5 items-center justify-center rounded-full bg-destructive px-1.5 text-[10px] font-bold text-destructive-foreground animate-badge-bump" aria-label={`${c.mentionsUnread} mentions`}>
                              @{c.mentionsUnread}
                            </span>
                          ) : unread ? (
                            <span className="rounded-full bg-primary/15 px-1.5 text-[11px] font-semibold tabular-nums text-primary" aria-label={`${c.unread} unread`}>
                              {c.unread > 99 ? "99+" : c.unread}
                            </span>
                          ) : null}
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              )}
            </div>
          );
        })}
      </div>

      <div className="space-y-0.5 border-t border-border px-2 py-2">
        {isAdmin && <ShellLink href="/admin/community" icon={ShieldCheck} label="Moderation" active={false} />}
        <ShellLink href="/community/settings" icon={Settings} label="Profile & notifications" active={pathname === "/community/settings"} />
      </div>
    </nav>
  );

  return (
    <ShellContext.Provider value={{ openNav: () => setDrawer(true) }}>
      {/* Full-bleed: undo the student layout's padding so the community fills
          the space under the top bar like an app, not a card on a page. */}
      <div className="-m-4 flex h-[calc(100dvh-4rem)] min-h-0 overflow-hidden bg-background sm:-m-6 lg:-m-8">
        <aside className="hidden w-[17rem] shrink-0 border-r border-border bg-secondary/25 lg:block">{nav}</aside>

        {drawer && (
          <div className="fixed inset-0 z-50 lg:hidden" role="dialog" aria-modal="true" aria-label="Channels">
            <button type="button" aria-label="Close channels" onClick={() => setDrawer(false)} className="absolute inset-0 bg-black/40 backdrop-blur-[2px] animate-fade-in" />
            <aside className="absolute inset-y-0 left-0 w-[min(20rem,86vw)] border-r border-border bg-background shadow-2xl animate-slide-in-left">{nav}</aside>
          </div>
        )}

        <div className="flex min-h-0 min-w-0 flex-1">{children}</div>
      </div>
    </ShellContext.Provider>
  );
}

function ShellLink({
  href,
  icon: Icon,
  label,
  active,
  badge,
}: {
  href: string;
  icon: typeof Compass;
  label: string;
  active: boolean;
  badge?: number;
}) {
  return (
    <Link
      href={href}
      aria-current={active ? "page" : undefined}
      className={cn(
        "flex items-center gap-2.5 rounded-lg px-2 py-1.5 text-[14px] font-medium transition-colors",
        active ? "bg-primary/10 text-primary" : "text-muted-foreground hover:bg-secondary/80 hover:text-foreground",
      )}
    >
      <Icon className="h-4 w-4" />
      <span className="flex-1">{label}</span>
      {badge ? (
        <span className="flex h-5 min-w-5 items-center justify-center rounded-full bg-destructive px-1.5 text-[10px] font-bold text-destructive-foreground animate-badge-bump">
          {badge}
        </span>
      ) : null}
    </Link>
  );
}

/** Standard header for community pages that are not a channel. */
export function PageHeader({ title, subtitle, icon: Icon, actions }: { title: string; subtitle?: string; icon: typeof Compass; actions?: React.ReactNode }) {
  return (
    <header className="flex h-14 shrink-0 items-center gap-2 border-b border-border bg-background/70 px-3 backdrop-blur sm:px-5">
      <NavToggle />
      <Icon className="h-4 w-4 text-primary" />
      <div className="min-w-0 flex-1">
        <h1 className="truncate font-display text-[15px] font-semibold leading-tight">{title}</h1>
        {subtitle && <p className="hidden truncate text-xs text-muted-foreground sm:block">{subtitle}</p>}
      </div>
      {actions}
    </header>
  );
}
