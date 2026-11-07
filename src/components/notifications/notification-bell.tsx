"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Bell, BellRing, CheckCheck, Settings2 } from "lucide-react";

import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Skeleton } from "@/components/ui/skeleton";
import { broadcastRead, useLive } from "@/components/live/live-provider";
import type { NotificationView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import {
  listNotifications,
  markAllNotificationsRead,
  markNotificationRead,
} from "@/server/actions/student/notifications";

import { NotificationItem } from "./notification-item";
import { BrowserAlertsPrompt } from "./browser-alerts";

/** The bell in the top bar: live badge, dropdown of recent notifications. */
export function NotificationBell() {
  const router = useRouter();
  const { data, pokeNow } = useLive();
  const unread = data?.notificationsUnread ?? 0;
  const [open, setOpen] = useState(false);
  const [items, setItems] = useState<NotificationView[] | null>(null);

  const load = useCallback(async () => {
    const r = await listNotifications({ take: 8 });
    setItems(r.items);
  }, []);

  // Refresh the open list when something new arrives.
  useEffect(() => {
    if (open) void load();
  }, [open, load, data?.latestNotificationAt]);

  async function openItem(n: NotificationView) {
    setOpen(false);
    if (!n.read) {
      await markNotificationRead(n.id);
      broadcastRead();
      pokeNow();
    }
    router.push(n.url);
  }

  async function readAll() {
    await markAllNotificationsRead();
    setItems((xs) => xs?.map((x) => ({ ...x, read: true })) ?? null);
    broadcastRead();
    pokeNow();
  }

  const label = unread > 0 ? `Notifications, ${unread} unread` : "Notifications";
  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <button
          type="button"
          aria-label={label}
          title={label}
          className={cn(
            "relative flex h-9 w-9 items-center justify-center rounded-full border border-border bg-secondary/60 text-muted-foreground transition-colors hover:text-foreground",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
            open && "text-foreground",
          )}
        >
          {unread > 0 ? <BellRing className="h-4 w-4 text-foreground" /> : <Bell className="h-4 w-4" />}
          {unread > 0 && (
            <span
              key={unread}
              className="absolute -right-1 -top-1 flex h-[18px] min-w-[18px] items-center justify-center rounded-full bg-destructive px-1 text-[10px] font-bold tabular-nums text-destructive-foreground ring-2 ring-background animate-badge-bump"
            >
              {unread > 99 ? "99+" : unread}
            </span>
          )}
        </button>
      </PopoverTrigger>
      <PopoverContent align="end" sideOffset={10} className="w-[min(24rem,calc(100vw-1.5rem))] overflow-hidden p-0">
        <div className="flex items-center justify-between border-b border-border px-4 py-3">
          <div>
            <p className="font-display text-[15px] font-semibold">Notifications</p>
            <p className="text-xs text-muted-foreground">{unread > 0 ? `${unread} unread` : "You're all caught up"}</p>
          </div>
          <div className="flex items-center gap-1">
            {unread > 0 && (
              <button
                type="button"
                onClick={() => void readAll()}
                className="flex items-center gap-1 rounded-lg px-2 py-1.5 text-xs font-medium text-primary hover:bg-primary/10"
              >
                <CheckCheck className="h-3.5 w-3.5" /> Mark all read
              </button>
            )}
            <Link
              href="/community/settings"
              onClick={() => setOpen(false)}
              className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground"
              aria-label="Notification settings"
            >
              <Settings2 className="h-4 w-4" />
            </Link>
          </div>
        </div>
        <div className="max-h-[min(28rem,60vh)] overflow-y-auto p-1.5">
          {items === null ? (
            <div className="space-y-2 p-2">
              {[0, 1, 2].map((i) => (
                <div key={i} className="flex gap-3">
                  <Skeleton className="h-9 w-9 rounded-full" />
                  <div className="flex-1 space-y-1.5">
                    <Skeleton className="h-3.5 w-4/5" />
                    <Skeleton className="h-3 w-3/5" />
                  </div>
                </div>
              ))}
            </div>
          ) : items.length === 0 ? (
            <div className="px-6 py-10 text-center">
              <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-secondary">
                <Bell className="h-5 w-5 text-muted-foreground" />
              </span>
              <p className="mt-3 text-sm font-medium">Nothing yet</p>
              <p className="mt-1 text-xs text-muted-foreground">
                Replies, mentions and messages from the community appear here.
              </p>
            </div>
          ) : (
            items.map((n) => <NotificationItem key={n.id} n={n} onOpen={(x) => void openItem(x)} dense />)
          )}
        </div>
        <BrowserAlertsPrompt compact />
        <Link
          href="/notifications"
          onClick={() => setOpen(false)}
          className="block border-t border-border px-4 py-2.5 text-center text-sm font-medium text-primary hover:bg-secondary/60"
        >
          See all notifications
        </Link>
      </PopoverContent>
    </Popover>
  );
}
