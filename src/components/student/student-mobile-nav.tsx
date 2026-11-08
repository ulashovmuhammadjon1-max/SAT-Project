"use client";

import { createContext, useContext, useEffect, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { CalendarPlus, ClipboardList, LayoutDashboard, Menu, MessagesSquare, PenLine } from "lucide-react";

import { Sheet, SheetContent, SheetTitle } from "@/components/ui/sheet";
import { SidebarContent, type StudentNavProps } from "@/components/student/student-sidebar";
import { useLive } from "@/components/live/live-provider";
import { cn } from "@/lib/utils";

/**
 * Navigation for screens narrower than the desktop sidebar (below `lg`).
 *
 * Two pieces share one drawer:
 *  - the hamburger in the top bar (phones and tablets), and
 *  - a bottom tab bar on phones (below `md`) for the four places students go
 *    most, with "Menu" opening the full drawer for everything else.
 *
 * The drawer renders the very same SidebarContent as the desktop aside, so a
 * link added to the sidebar appears on mobile with no second list to update.
 */

const MobileNavContext = createContext<{ open: () => void }>({ open: () => {} });

export function StudentMobileNavProvider({ children, ...nav }: StudentNavProps & { children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  const pathname = usePathname();

  // Any navigation — a link, the programme menu, the back button — closes it.
  useEffect(() => setOpen(false), [pathname]);

  return (
    <MobileNavContext.Provider value={{ open: () => setOpen(true) }}>
      {children}
      <Sheet open={open} onOpenChange={setOpen}>
        <SheetContent
          side="left"
          className="flex w-[86vw] max-w-[320px] flex-col gap-0 p-0 pb-[env(safe-area-inset-bottom)] pl-[env(safe-area-inset-left)] lg:hidden"
        >
          <SheetTitle className="sr-only">Navigation</SheetTitle>
          <SidebarContent {...nav} touch />
        </SheetContent>
      </Sheet>
    </MobileNavContext.Provider>
  );
}

/** The top-bar hamburger. Hidden once the desktop sidebar is on screen. */
export function MobileNavTrigger() {
  const { open } = useContext(MobileNavContext);
  return (
    <button
      type="button"
      onClick={open}
      aria-label="Open navigation"
      className="-ml-1.5 flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-foreground transition-colors hover:bg-secondary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring lg:hidden"
    >
      <Menu className="h-5 w-5" />
    </button>
  );
}

/** Routes with their own full-height layout and bottom composer. */
const NO_TAB_BAR = ["/community"];

/**
 * The phone tab bar. It sits in the page flow as a spacer (so nothing is ever
 * hidden behind it) plus the fixed bar itself, padded for the home indicator.
 */
export function StudentTabBar({ activeExam = "SAT" }: { activeExam?: StudentNavProps["activeExam"] }) {
  const pathname = usePathname();
  const { open } = useContext(MobileNavContext);
  const { data } = useLive();
  if (NO_TAB_BAR.some((p) => pathname === p || pathname.startsWith(`${p}/`))) return null;

  const ielts = activeExam === "IELTS";
  const practiceRoots = ielts
    ? ["/ielts"]
    : ["/sat", "/tests", "/practice", "/daily", "/vocabulary", "/plan", "/analytics", "/bookmarks"];
  const tabs = [
    { href: "/dashboard", label: "Home", icon: LayoutDashboard, active: pathname === "/dashboard" },
    {
      href: ielts ? "/ielts" : "/sat",
      label: ielts ? "IELTS" : "SAT",
      icon: ielts ? PenLine : ClipboardList,
      active: practiceRoots.some((p) => pathname === p || pathname.startsWith(`${p}/`)),
    },
    { href: "/community", label: "Community", icon: MessagesSquare, active: false, dot: (data?.dmUnread ?? 0) > 0 },
    {
      href: "/booking",
      label: "Sessions",
      icon: CalendarPlus,
      active: pathname.startsWith("/booking"),
    },
  ];

  return (
    <>
      <div aria-hidden className="h-[calc(4.25rem+env(safe-area-inset-bottom))] md:hidden" />
      <nav
        aria-label="Quick navigation"
        className="fixed inset-x-0 bottom-0 z-40 border-t border-border bg-background/95 pb-[env(safe-area-inset-bottom)] backdrop-blur supports-[backdrop-filter]:bg-background/85 md:hidden"
      >
        <ul className="mx-auto grid h-16 max-w-md grid-cols-5 px-1">
          {tabs.map((t) => (
            <li key={t.href} className="flex">
              <Link
                href={t.href}
                aria-current={t.active ? "page" : undefined}
                className={cn(
                  "relative flex flex-1 flex-col items-center justify-center gap-1 rounded-xl text-[11px] font-medium transition-colors",
                  t.active ? "text-primary" : "text-muted-foreground active:bg-secondary"
                )}
              >
                <span
                  className={cn(
                    "flex h-7 w-12 items-center justify-center rounded-full transition-colors",
                    t.active && "bg-primary/10"
                  )}
                >
                  <t.icon className="h-[19px] w-[19px]" />
                </span>
                {t.label}
                {t.dot && (
                  <span className="absolute right-[calc(50%-16px)] top-2 h-2 w-2 rounded-full bg-destructive ring-2 ring-background" />
                )}
              </Link>
            </li>
          ))}
          <li className="flex">
            <button
              type="button"
              onClick={open}
              className="flex flex-1 flex-col items-center justify-center gap-1 rounded-xl text-[11px] font-medium text-muted-foreground transition-colors active:bg-secondary"
            >
              <span className="flex h-7 w-12 items-center justify-center rounded-full">
                <Menu className="h-[19px] w-[19px]" />
              </span>
              Menu
            </button>
          </li>
        </ul>
      </nav>
    </>
  );
}
