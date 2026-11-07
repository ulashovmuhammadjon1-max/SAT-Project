"use client";

import { useMemo, useState } from "react";
import { CalendarX2, Search, SearchX, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { topicOf } from "@/lib/booking/topics";
import { cn } from "@/lib/utils";
import type { OpenSlot } from "@/server/actions/student/bookings";

import { dayKey, dayLong, useMounted } from "./format";
import { SessionCard, SessionCardSkeleton } from "./session-card";

type Sort = "soonest" | "topic";

/**
 * Session discovery: search, sort, topic chips, and the list itself.
 *
 * Everything here filters the sessions already on the page. The server sent
 * every open slot once, so filtering is instant and costs no requests.
 */
export function SessionBrowser({
  slots,
  cost,
  canAfford,
  onBook,
}: {
  slots: OpenSlot[];
  cost: number;
  canAfford: boolean;
  onBook: (slotId: string) => void;
}) {
  const mounted = useMounted();
  const [topic, setTopic] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [sort, setSort] = useState<Sort>("soonest");

  const topics = useMemo(() => {
    const counts = new Map<string, number>();
    for (const s of slots) counts.set(topicOf(s.subject), (counts.get(topicOf(s.subject)) ?? 0) + 1);
    return [...counts.entries()].sort((a, b) => a[0].localeCompare(b[0]));
  }, [slots]);

  const q = query.trim().toLowerCase();
  const visible = useMemo(() => {
    const list = slots.filter((s) => {
      if (topic && topicOf(s.subject) !== topic) return false;
      if (!q) return true;
      return [s.title, s.subject, topicOf(s.subject), s.hostName].some((v) => v?.toLowerCase().includes(q));
    });
    return [...list].sort((a, b) =>
      sort === "topic"
        ? topicOf(a.subject).localeCompare(topicOf(b.subject)) ||
          new Date(a.startsAt).getTime() - new Date(b.startsAt).getTime()
        : new Date(a.startsAt).getTime() - new Date(b.startsAt).getTime(),
    );
  }, [slots, topic, q, sort]);

  // Grouped by local calendar day when sorted by time, which is how people
  // think about when they are free.
  const groups = useMemo(() => {
    if (!mounted) return [];
    if (sort === "topic") return [{ key: "all", label: null as string | null, items: visible }];
    const map = new Map<string, { key: string; label: string | null; items: OpenSlot[] }>();
    for (const s of visible) {
      const k = dayKey(s.startsAt);
      if (!map.has(k)) map.set(k, { key: k, label: dayLong(s.startsAt), items: [] });
      map.get(k)!.items.push(s);
    }
    return [...map.values()];
  }, [visible, sort, mounted]);

  const clearAll = () => {
    setTopic(null);
    setQuery("");
  };

  if (slots.length === 0) {
    return (
      <EmptyState
        icon={CalendarX2}
        title="No sessions are open right now"
        body="Mentors publish new sessions regularly, often a few days ahead. Check back soon, or look at the group events while you wait."
        action={{ href: "/events", label: "Browse events" }}
      />
    );
  }

  return (
    <section aria-labelledby="browse-title" className="space-y-5">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h2 id="browse-title" className="font-display text-xl font-semibold tracking-tight">
            Available sessions
          </h2>
          <p className="mt-1 text-sm text-muted-foreground" aria-live="polite">
            {visible.length === slots.length
              ? `${slots.length} open ${slots.length === 1 ? "session" : "sessions"}`
              : `Showing ${visible.length} of ${slots.length} sessions`}
            {topic && <> in <span className="font-medium text-foreground">{topic}</span></>}
            {q && <> matching &ldquo;<span className="font-medium text-foreground">{query.trim()}</span>&rdquo;</>}
          </p>
        </div>
      </div>

      <div className="flex flex-col gap-3 sm:flex-row">
        <div className="relative flex-1">
          <Search
            aria-hidden
            className="pointer-events-none absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground"
          />
          <Input
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search by title, subject or teacher"
            aria-label="Search sessions by title, subject or teacher"
            className="h-12 rounded-lg pl-12 pr-12 text-base"
          />
          {query && (
            <button
              type="button"
              onClick={() => setQuery("")}
              aria-label="Clear search"
              className="absolute right-1 top-1/2 flex h-10 w-10 -translate-y-1/2 items-center justify-center rounded-md text-muted-foreground hover:bg-secondary hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            >
              <X className="h-4 w-4" />
            </button>
          )}
        </div>
        <label className="flex items-center gap-2 text-sm text-muted-foreground sm:w-56">
          <span className="whitespace-nowrap">Sort by</span>
          <select
            value={sort}
            onChange={(e) => setSort(e.target.value as Sort)}
            className="h-12 w-full rounded-lg border border-input bg-background px-3 text-base text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          >
            <option value="soonest">Soonest first</option>
            <option value="topic">Topic (A–Z)</option>
          </select>
        </label>
      </div>

      {topics.length > 1 && (
        <div
          role="group"
          aria-label="Filter by topic"
          className="-mx-4 flex gap-2 overflow-x-auto px-4 pb-1 sm:mx-0 sm:flex-wrap sm:overflow-visible sm:px-0 [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
        >
          {[[null, slots.length] as const, ...topics].map(([t, count]) => {
            const active = topic === t;
            return (
              <button
                key={t ?? "all"}
                type="button"
                onClick={() => setTopic(t)}
                aria-pressed={active}
                className={cn(
                  "inline-flex h-11 shrink-0 items-center gap-2 whitespace-nowrap rounded-full border px-4 text-[15px] font-medium transition-colors",
                  "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
                  active
                    ? "border-foreground bg-foreground text-background"
                    : "border-border bg-card text-foreground hover:border-foreground/40",
                )}
              >
                {t ?? "All sessions"}
                <span
                  className={cn(
                    "rounded-full px-1.5 text-xs tabular-nums",
                    active ? "bg-background/20" : "bg-secondary text-muted-foreground",
                  )}
                >
                  {count}
                </span>
              </button>
            );
          })}
        </div>
      )}

      {!mounted ? (
        <div className="grid gap-4 md:grid-cols-2" aria-busy="true" aria-label="Loading sessions">
          {Array.from({ length: Math.min(4, slots.length) }, (_, i) => (
            <SessionCardSkeleton key={i} />
          ))}
        </div>
      ) : visible.length === 0 ? (
        <EmptyState
          icon={SearchX}
          title={q ? `No sessions match “${query.trim()}”` : `No ${topic} sessions right now`}
          body={
            q
              ? "Try a different word, or search for a subject or a teacher's name."
              : "Sessions on this topic have all been booked. Other topics may still have times open."
          }
          onAction={{ label: "Show all sessions", run: clearAll }}
        />
      ) : (
        <div className="space-y-8">
          {groups.map((g) => (
            <div key={g.key}>
              {g.label && (
                <h3 className="mb-3 text-sm font-semibold text-muted-foreground">{g.label}</h3>
              )}
              <div className="grid gap-4 md:grid-cols-2">
                {g.items.map((s) => (
                  <SessionCard key={s.id} slot={s} cost={cost} canAfford={canAfford} onBook={() => onBook(s.id)} />
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

function EmptyState({
  icon: Icon,
  title,
  body,
  action,
  onAction,
}: {
  icon: typeof Search;
  title: string;
  body: string;
  action?: { href: string; label: string };
  onAction?: { label: string; run: () => void };
}) {
  return (
    <div className="flex flex-col items-center rounded-xl border border-dashed border-border px-6 py-14 text-center">
      <span className="flex h-12 w-12 items-center justify-center rounded-full bg-secondary text-muted-foreground">
        <Icon className="h-6 w-6" aria-hidden />
      </span>
      <p className="mt-4 text-lg font-semibold">{title}</p>
      <p className="mt-1.5 max-w-md text-sm leading-relaxed text-muted-foreground">{body}</p>
      {action && (
        <Button asChild variant="outline" className="mt-5 h-11 px-5">
          <a href={action.href}>{action.label}</a>
        </Button>
      )}
      {onAction && (
        <Button type="button" variant="outline" onClick={onAction.run} className="mt-5 h-11 px-5">
          {onAction.label}
        </Button>
      )}
    </div>
  );
}
