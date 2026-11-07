"use client";

import { useEffect, useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Bell, CheckCheck, Loader2, Settings2 } from "lucide-react";

import { broadcastRead, useLive } from "@/components/live/live-provider";
import type { NotificationView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import {
  listNotifications,
  markAllNotificationsRead,
  markNotificationRead,
  type NotificationFilter,
} from "@/server/actions/student/notifications";

import { NotificationItem } from "./notification-item";

const FILTERS: { id: NotificationFilter; label: string }[] = [
  { id: "all", label: "All" },
  { id: "unread", label: "Unread" },
  { id: "replies", label: "Replies" },
  { id: "mentions", label: "Mentions" },
  { id: "messages", label: "Messages" },
];

export function NotificationsPage() {
  const router = useRouter();
  const { data, pokeNow } = useLive();
  const [filter, setFilter] = useState<NotificationFilter>("all");
  const [items, setItems] = useState<NotificationView[] | null>(null);
  const [cursor, setCursor] = useState<string | null>(null);
  const [pending, start] = useTransition();

  useEffect(() => {
    setItems(null);
    start(async () => {
      const r = await listNotifications({ filter });
      setItems(r.items);
      setCursor(r.nextCursor);
    });
  }, [filter, data?.latestNotificationAt]);

  const unread = data?.notificationsUnread ?? 0;

  return (
    <div className="mx-auto max-w-3xl">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-serif text-4xl font-medium tracking-tight">Notifications</h1>
          <p className="mt-1 text-sm text-muted-foreground">{unread > 0 ? `${unread} unread` : "You're all caught up."}</p>
        </div>
        <div className="flex items-center gap-2">
          {unread > 0 && (
            <button
              type="button"
              onClick={async () => {
                await markAllNotificationsRead();
                setItems((xs) => xs?.map((x) => ({ ...x, read: true })) ?? null);
                broadcastRead();
                pokeNow();
              }}
              className="inline-flex items-center gap-1.5 rounded-xl border border-border bg-card px-3 py-2 text-sm font-medium hover:bg-secondary"
            >
              <CheckCheck className="h-4 w-4" /> Mark all read
            </button>
          )}
          <Link href="/community/settings" className="inline-flex items-center gap-1.5 rounded-xl border border-border bg-card px-3 py-2 text-sm font-medium hover:bg-secondary">
            <Settings2 className="h-4 w-4" /> Settings
          </Link>
        </div>
      </div>

      <div className="mt-6 flex gap-1.5 overflow-x-auto no-scrollbar" role="tablist">
        {FILTERS.map((f) => (
          <button
            key={f.id}
            type="button"
            role="tab"
            aria-selected={filter === f.id}
            onClick={() => setFilter(f.id)}
            className={cn("shrink-0 rounded-full border px-3.5 py-1.5 text-sm font-medium transition-colors", filter === f.id ? "border-primary bg-primary text-primary-foreground" : "border-border bg-card hover:border-primary/40")}
          >
            {f.label}
          </button>
        ))}
      </div>

      <div className="mt-4 overflow-hidden rounded-2xl border border-border bg-card p-1.5 shadow-sm">
        {items === null ? (
          <div className="flex justify-center py-16">
            <Loader2 className="h-5 w-5 animate-spin text-muted-foreground" />
          </div>
        ) : items.length === 0 ? (
          <div className="px-6 py-16 text-center">
            <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-secondary">
              <Bell className="h-5 w-5 text-muted-foreground" />
            </span>
            <p className="mt-3 font-serif text-xl">Nothing here</p>
            <p className="mt-1 text-sm text-muted-foreground">When someone replies to you, mentions you or sends you a message, it shows up here.</p>
          </div>
        ) : (
          items.map((n) => (
            <NotificationItem
              key={n.id}
              n={n}
              onOpen={async (x) => {
                if (!x.read) {
                  await markNotificationRead(x.id);
                  broadcastRead();
                  pokeNow();
                }
                router.push(x.url);
              }}
            />
          ))
        )}
      </div>
      {cursor && (
        <div className="mt-4 flex justify-center">
          <button
            type="button"
            disabled={pending}
            onClick={() =>
              start(async () => {
                const r = await listNotifications({ filter, cursor });
                setItems((xs) => [...(xs ?? []), ...r.items]);
                setCursor(r.nextCursor);
              })
            }
            className="inline-flex items-center gap-2 rounded-full border border-border px-4 py-2 text-sm font-medium hover:bg-secondary"
          >
            {pending && <Loader2 className="h-4 w-4 animate-spin" />} Load more
          </button>
        </div>
      )}
    </div>
  );
}
