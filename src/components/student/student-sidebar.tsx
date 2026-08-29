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

import { ClassSwitcher, type SwitcherClass } from "@/components/classroom/class-switcher";
import { setActiveExam } from "@/server/actions/student/exam-mode";
import { cn } from "@/lib/utils";

interface NavItem {
  href: string;
  label: string;
  icon: typeof LayoutDashboard;
  exact?: boolean;
  /** Extra prefix that also lights this item up (child routes of an exact href). */
  also?: string;
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

/**
 * Research and School are products of their own: opening one swaps the whole
 * sidebar to that product's navigation, exactly like switching exams — so a
 * student on /class is *in* School, not in an exam with a page borrowed.
 */
const RESEARCH_GROUPS: NavGroup[] = [
  { label: null, items: [{ href: "/research", label: "Research Home", icon: FlaskConical, exact: true }] },
  {
    label: "Programme",
    items: [
      { href: "/research/guide", label: "Proposal Guide", icon: BookOpen },
      { href: "/journal", label: "The Journal", icon: Microscope },
    ],
  },
  { label: null, items: [{ href: "/settings", label: "Settings", icon: Settings }] },
];

/**
 * The School sidebar is class-aware: inside /classes/{id} it grows a "This
 * class" block, so the nav always answers "which class am I in" together with
 * the switcher above it.
 */
function schoolGroups(pathname: string): NavGroup[] {
  const classId = pathname.match(/^\/classes\/([^/]+)/)?.[1];
  return [
    { label: null, items: [{ href: "/classes", label: "All Classes", icon: School, exact: true }] },
    ...(classId
      ? [
          {
            label: "This class",
            items: [
              {
                href: `/classes/${classId}`,
                label: "Assignments",
                icon: ListChecks,
                exact: true,
                also: `/classes/${classId}/assignments`,
              },
              { href: `/classes/${classId}/leaderboard`, label: "Class Leaderboard", icon: Trophy },
            ],
          },
        ]
      : []),
    {
      label: "Teachers",
    items: [{ href: "/schools", label: "For Teachers", icon: GraduationCap }],
    },
    { label: null, items: [{ href: "/settings", label: "Settings", icon: Settings }] },
  ];
}

const AP_GROUPS: NavGroup[] = [
  { label: null, items: [{ href: "/ap", label: "AP Home", icon: Award, exact: true }] },
  {
    label: "Subjects",
    items: [
      { href: "/ap/macroeconomics", label: "AP Macroeconomics", icon: BookOpen },
      { href: "/ap/microeconomics", label: "AP Microeconomics", icon: BookOpen },
      { href: "/ap/calculus-ab", label: "AP Calculus AB", icon: BookOpen },
      { href: "/ap/calculus-bc", label: "AP Calculus BC", icon: BookOpen },
    ],
  },
  { label: null, items: [{ href: "/settings", label: "Settings", icon: Settings }] },
];

type Product = "SAT" | "IELTS" | "RESEARCH" | "SCHOOL" | "AP";

/** Which product a path belongs to; exam pages fall back to activeExam. */
function productFor(pathname: string, activeExam: ExamMode): Product {
  if (pathname.startsWith("/research")) return "RESEARCH";
  if (pathname.startsWith("/ap")) return "AP";
  if (
    pathname.startsWith("/class") ||
    pathname.startsWith("/classes") ||
    pathname.startsWith("/teach")
  )
    return "SCHOOL";
  return activeExam === "IELTS" ? "IELTS" : "SAT";
}

export function StudentSidebar({
  activeExam = "SAT",
  teaching = false,
  classes = [],
}: {
  activeExam?: ExamMode;
  /** True when a class is linked to this account — shows the Teacher Panel. */
  teaching?: boolean;
  /** The student's classes, for the School product's switcher. */
  classes?: SwitcherClass[];
}) {
  const pathname = usePathname();
  const product = productFor(pathname, activeExam);
  const baseGroups =
    product === "RESEARCH"
      ? RESEARCH_GROUPS
      : product === "AP"
        ? AP_GROUPS
        : product === "SCHOOL"
          ? schoolGroups(pathname)
          : GROUPS_FOR[activeExam];
  // Teachers see their panel in every product's sidebar, right before
  // Settings — a teacher checking on their class should never have to hunt.
  const groups = teaching
    ? [
        ...baseGroups.slice(0, -1),
        {
          label: "Teaching",
          items: [{ href: "/teach", label: "Teacher Panel", icon: GraduationCap, badge: "New" }],
        },
        baseGroups[baseGroups.length - 1],
      ]
    : baseGroups;
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
      <ProductMenu activeExam={activeExam} product={product} />

      {/* Inside School, the class is the unit everything hangs off — the
          switcher keeps "which class am I in?" answered at all times. */}
      {product === "SCHOOL" && <ClassSwitcher classes={classes} />}

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
              // light up for every /ielts/* route at once. `also` lets an
              // exact item still own a child subtree (assignment pages).
              const active =
                (item.exact ? pathname === item.href : pathname.startsWith(item.href)) ||
                (item.also ? pathname.startsWith(item.also) : false);
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
 * The programme menu, closed by default: the sidebar shows one product and a
 * single chevron reveals the other three. SAT/IELTS switch the stored exam
 * mode (and navigate to that exam's home); Research and School navigate to
 * their own product homes — the sidebar re-derives the product from the URL.
 */
function ProductMenu({ activeExam, product }: { activeExam: ExamMode; product: Product }) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [pending, startTransition] = useTransition();

  const META: Record<Product, { label: string; short: string }> = {
    SAT: { label: "SAT Prep", short: "SAT" },
    IELTS: { label: "IELTS Prep", short: "IE" },
    AP: { label: "AP Prep", short: "AP" },
    RESEARCH: { label: "Research", short: "RS" },
    SCHOOL: { label: "School", short: "SC" },
  };

  const goExam = (mode: ExamMode) => {
    startTransition(async () => {
      // Already in that exam mode but viewing another product: just go home.
      if (mode === activeExam || (mode === "SAT" && activeExam === "BOTH")) {
        setOpen(false);
        router.push(mode === "IELTS" ? "/ielts" : "/dashboard");
        return;
      }
      const result = await setActiveExam(mode);
      if (result.error) {
        toast.error(result.error);
        return;
      }
      setOpen(false);
      router.push(result.redirectTo ?? (mode === "IELTS" ? "/ielts" : "/dashboard"));
      router.refresh();
    });
  };

  const options: { key: Product; icon: typeof BookOpen; onSelect?: () => void; href?: string; badge?: string }[] = [
    { key: "SAT", icon: BookOpen, onSelect: () => goExam("SAT") },
    { key: "IELTS", icon: PenLine, onSelect: () => goExam("IELTS") },
    { key: "AP", icon: Award, href: "/ap", badge: "New" },
    { key: "RESEARCH", icon: FlaskConical, href: "/research", badge: "New" },
    { key: "SCHOOL", icon: School, href: "/classes", badge: "New" },
  ];

  return (
    <div className="border-b border-border p-3">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        className="flex w-full items-center gap-2.5 rounded-xl border border-border bg-secondary/50 px-3 py-2 text-sm font-semibold transition-colors hover:bg-secondary"
      >
        <span className="flex h-6 w-6 items-center justify-center rounded-md bg-navy-900 text-[10px] font-bold text-white">
          {META[product].short}
        </span>
        {META[product].label}
        <ChevronDown
          className={cn(
            "ml-auto h-4 w-4 text-muted-foreground transition-transform duration-200",
            open && "rotate-180"
          )}
        />
      </button>

      {open && (
        <div className="mt-1.5 space-y-0.5 rounded-xl border border-border bg-card p-1.5 shadow-soft">
          {options
            .filter((o) => o.key !== product)
            .map((o) =>
              o.href ? (
                <Link
                  key={o.key}
                  href={o.href}
                  onClick={() => setOpen(false)}
                  className="flex items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground"
                >
                  <o.icon className="h-4 w-4" />
                  {META[o.key].label}
                  {o.badge && (
                    <span className="ml-auto rounded-full bg-primary/10 px-1.5 py-0.5 text-[9px] font-bold uppercase tracking-wide text-primary">
                      {o.badge}
                    </span>
                  )}
                </Link>
              ) : (
                <button
                  key={o.key}
                  type="button"
                  disabled={pending}
                  onClick={o.onSelect}
                  className="flex w-full items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground disabled:opacity-60"
                >
                  <o.icon className="h-4 w-4" />
                  {META[o.key].label}
                </button>
              ),
            )}
        </div>
      )}
    </div>
  );
}
