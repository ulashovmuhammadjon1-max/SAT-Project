"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import {
  ArrowRight,
  BellRing,
  CalendarPlus,
  Mail,
  Megaphone,
  Sparkles,
  UserRound,
  X,
} from "lucide-react";

import { Dialog, DialogContent, DialogDescription, DialogTitle } from "@/components/ui/dialog";
import { getWhatsNew, type WhatsNew } from "@/server/actions/student/whats-new";
import { markNotificationRead } from "@/server/actions/student/notifications";
import { cn } from "@/lib/utils";

const SEEN_KEY = (userId: string) => `scholarly-whatsnew:${userId}`;
const TAB_KEY = "scholarly-whatsnew-shown";

function when(iso: string) {
  const d = new Date(iso);
  return d.toLocaleString(undefined, { weekday: "short", day: "numeric", month: "short", hour: "numeric", minute: "2-digit" });
}

function ago(iso: string) {
  const m = Math.round((Date.now() - new Date(iso).getTime()) / 60000);
  if (m < 60) return `${Math.max(1, m)}m ago`;
  const h = Math.round(m / 60);
  if (h < 24) return `${h}h ago`;
  return `${Math.round(h / 24)}d ago`;
}

/**
 * The welcome screen: opens when a student opens Scholarly and something
 * happened since their last visit on this device — new sessions, an
 * announcement, replies or messages waiting. Nothing new, no screen.
 *
 * "Last visit" is stored per account in this browser, and the screen opens at
 * most once per tab, so moving between pages never brings it back.
 */
export function WhatsNewScreen({ userId, firstName }: { userId: string; firstName: string }) {
  const router = useRouter();
  const [data, setData] = useState<WhatsNew | null>(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    let cancelled = false;
    let since: string | null = null;
    try {
      if (sessionStorage.getItem(TAB_KEY) === "1") return;
      since = localStorage.getItem(SEEN_KEY(userId));
    } catch {
      /* storage blocked: still show, from the default window */
    }
    const t = setTimeout(async () => {
      const d = await getWhatsNew(since).catch(() => null);
      if (cancelled || !d || d.isEmpty) return;
      setData(d);
      setOpen(true);
      try {
        sessionStorage.setItem(TAB_KEY, "1");
      } catch {
        /* ignore */
      }
    }, 700);
    return () => {
      cancelled = true;
      clearTimeout(t);
    };
  }, [userId]);

  function close() {
    setOpen(false);
    try {
      localStorage.setItem(SEEN_KEY(userId), new Date().toISOString());
    } catch {
      /* ignore */
    }
  }

  function go(href: string) {
    close();
    router.push(href);
  }

  if (!data) return null;
  const s = data.sessions;
  const sections = [s.total > 0, data.announcements.length > 0, data.notifications.items.length > 0, data.messagesUnread > 0].filter(Boolean).length;

  return (
    <Dialog open={open} onOpenChange={(o) => !o && close()}>
      <DialogContent className="flex max-h-[calc(100dvh-1.5rem)] w-[calc(100vw-1.5rem)] max-w-2xl flex-col gap-0 overflow-hidden p-0 [&>button]:hidden">
        <div className="relative shrink-0 overflow-hidden border-b border-border px-6 pb-5 pt-7 sm:px-8 sm:pb-6">
          <div aria-hidden className="pointer-events-none absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,hsl(var(--primary)/0.22),transparent_60%),radial-gradient(ellipse_at_bottom_left,hsl(var(--accent-foreground)/0.1),transparent_55%)]" />
          <button type="button" onClick={close} aria-label="Close" className="absolute right-4 top-4 rounded-lg p-1.5 text-muted-foreground hover:bg-secondary hover:text-foreground">
            <X className="h-5 w-5" />
          </button>
          <p className="relative flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.18em] text-primary">
            <Sparkles className="h-3.5 w-3.5" /> Since your last visit
          </p>
          <DialogTitle className="relative mt-2 font-serif text-3xl font-medium leading-tight tracking-tight sm:text-4xl">
            Welcome back, {firstName}.
          </DialogTitle>
          <DialogDescription className="relative mt-1.5 text-[15px] text-muted-foreground">
            {sections === 1 ? "There is something new for you." : `Here are ${sections} things that happened while you were away.`}
          </DialogDescription>
        </div>

        <div className="min-h-0 flex-1 space-y-5 overflow-y-auto px-6 py-6 sm:px-8">
          {s.total > 0 && (
            <Section
              icon={CalendarPlus}
              tone="bg-primary text-primary-foreground"
              title={s.total === 1 ? "A new 1-on-1 session opened" : `${s.total} new 1-on-1 sessions opened`}
              subtitle="Free with your Scholarly coins. Seats go quickly."
              action={{ label: "Book a session", onClick: () => go("/booking") }}
            >
              <ul className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                {s.items.map((x) => (
                  <li key={x.id} className="rounded-xl border border-border bg-card p-3">
                    <p className="text-[11px] font-semibold uppercase tracking-wide text-primary">{x.topic}</p>
                    <p className="mt-0.5 line-clamp-1 text-sm font-semibold">{x.title}</p>
                    <p className="mt-1 text-xs text-muted-foreground">{when(x.startsAt)}</p>
                    {x.host && (
                      <p className="mt-0.5 flex items-center gap-1 text-xs text-muted-foreground">
                        <UserRound className="h-3 w-3" /> with {x.host.split(" ")[0]}
                      </p>
                    )}
                  </li>
                ))}
              </ul>
              {s.total > s.items.length && <p className="mt-2 text-xs text-muted-foreground">…and {s.total - s.items.length} more on the Sessions page.</p>}
            </Section>
          )}

          {data.announcements.length > 0 && (
            <Section icon={Megaphone} tone="bg-foreground text-background" title={data.announcements.length === 1 ? "New announcement" : "New announcements"}>
              <ul className="space-y-2">
                {data.announcements.map((a) => (
                  <li key={a.id}>
                    <button type="button" onClick={() => go(`/community/${a.channelSlug}?m=${a.id}`)} className="group w-full rounded-xl border border-border bg-card p-3 text-left transition-colors hover:border-primary/40">
                      <p className="flex items-center justify-between gap-2 text-sm font-semibold group-hover:text-primary">
                        {a.title}
                        <span className="shrink-0 text-[11px] font-normal text-muted-foreground">{ago(a.createdAt)}</span>
                      </p>
                      {a.body && <p className="mt-0.5 line-clamp-2 text-sm text-muted-foreground">{a.body}</p>}
                    </button>
                  </li>
                ))}
              </ul>
            </Section>
          )}

          {data.notifications.items.length > 0 && (
            <Section
              icon={BellRing}
              tone="bg-warning text-warning-foreground"
              title={data.notifications.unread === 1 ? "1 reply or mention for you" : `${data.notifications.unread} replies and mentions for you`}
              action={{ label: "See all", onClick: () => go("/notifications") }}
            >
              <ul className="space-y-1.5">
                {data.notifications.items.map((n) => (
                  <li key={n.id}>
                    <button
                      type="button"
                      onClick={() => {
                        void markNotificationRead(n.id);
                        go(n.url);
                      }}
                      className="w-full rounded-xl px-3 py-2 text-left transition-colors hover:bg-secondary/70"
                    >
                      <p className="text-sm font-medium">{n.title}</p>
                      {n.body && <p className="line-clamp-1 text-[13px] text-muted-foreground">{n.body}</p>}
                    </button>
                  </li>
                ))}
              </ul>
            </Section>
          )}

          {data.messagesUnread > 0 && (
            <Section
              icon={Mail}
              tone="bg-primary/15 text-primary"
              title={data.messagesUnread === 1 ? "A new private message" : `${data.messagesUnread} conversations with new messages`}
              action={{ label: "Open messages", onClick: () => go("/community/messages") }}
            />
          )}
        </div>

        <div className="flex shrink-0 flex-col-reverse gap-2 border-t border-border bg-secondary/30 px-6 py-4 sm:flex-row sm:items-center sm:justify-between sm:px-8">
          <Link href="/community" onClick={close} className="text-center text-sm font-medium text-muted-foreground hover:text-foreground sm:text-left">
            Visit the community →
          </Link>
          <button type="button" onClick={close} className="h-11 rounded-xl bg-primary px-6 text-sm font-semibold text-primary-foreground hover:brightness-110">
            Got it
          </button>
        </div>
      </DialogContent>
    </Dialog>
  );
}

function Section({
  icon: Icon,
  tone,
  title,
  subtitle,
  action,
  children,
}: {
  icon: typeof Sparkles;
  tone: string;
  title: string;
  subtitle?: string;
  action?: { label: string; onClick: () => void };
  children?: React.ReactNode;
}) {
  return (
    <section className="animate-fade-up">
      <div className="flex items-start gap-3">
        <span className={cn("flex h-10 w-10 shrink-0 items-center justify-center rounded-xl", tone)}>
          <Icon className="h-5 w-5" />
        </span>
        <div className="min-w-0 flex-1">
          <h3 className="font-display text-base font-semibold leading-snug">{title}</h3>
          {subtitle && <p className="text-sm text-muted-foreground">{subtitle}</p>}
        </div>
        {action && (
          <button type="button" onClick={action.onClick} className="hidden shrink-0 items-center gap-1 rounded-lg px-2.5 py-1.5 text-sm font-semibold text-primary hover:bg-primary/10 sm:flex">
            {action.label} <ArrowRight className="h-4 w-4" />
          </button>
        )}
      </div>
      {children && <div className="mt-3 sm:pl-[3.25rem]">{children}</div>}
      {action && (
        <button type="button" onClick={action.onClick} className="mt-3 flex w-full items-center justify-center gap-1 rounded-xl border border-primary/40 py-2.5 text-sm font-semibold text-primary sm:hidden">
          {action.label} <ArrowRight className="h-4 w-4" />
        </button>
      )}
    </section>
  );
}
