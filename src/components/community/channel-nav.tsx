"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Hash, Lock } from "lucide-react";

import type { ChannelView } from "@/lib/community/types";
import { cn } from "@/lib/utils";

/**
 * The channel list.
 *
 * A client component purely so it can highlight the channel you are actually
 * in. The first version was server-rendered links with only a hover style, so
 * every channel looked identical and nothing on the page told you where you
 * were — the single worst thing about navigating it.
 */
export function ChannelNav({ channels }: { channels: ChannelView[] }) {
  const pathname = usePathname();

  return (
    <nav className="flex gap-1 overflow-x-auto lg:flex-col lg:overflow-visible">
      <p className="hidden px-3 pb-1 text-xs font-semibold uppercase tracking-wide text-muted-foreground lg:block">
        Channels
      </p>
      {channels.map((c) => {
        const active = pathname === `/community/${c.slug}`;
        return (
          <Link
            key={c.id}
            href={`/community/${c.slug}`}
            aria-current={active ? "page" : undefined}
            className={cn(
              "flex shrink-0 items-center gap-2 rounded-lg px-3 py-2.5 text-sm transition-colors lg:shrink",
              active
                ? "bg-primary/10 font-medium text-primary"
                : "text-foreground/80 hover:bg-secondary hover:text-foreground"
            )}
          >
            {c.isReadOnly ? (
              <Lock className="h-4 w-4 shrink-0 opacity-70" />
            ) : (
              <Hash className="h-4 w-4 shrink-0 opacity-70" />
            )}
            <span className="min-w-0 flex-1 truncate">{c.name}</span>

            {/* A mention names you personally, so it gets a counted pill; an
                ordinary unread only gets a dot. Two different signals, because
                "someone asked you something" and "the channel moved" are not
                the same news. */}
            {c.mentionsUnread > 0 ? (
              <span className="shrink-0 rounded-full bg-primary px-1.5 py-px text-[10px] font-semibold text-primary-foreground">
                {c.mentionsUnread}
              </span>
            ) : c.unread > 0 ? (
              <span
                className="h-2 w-2 shrink-0 rounded-full bg-primary"
                title={`${c.unread} unread`}
              />
            ) : null}
          </Link>
        );
      })}
    </nav>
  );
}
