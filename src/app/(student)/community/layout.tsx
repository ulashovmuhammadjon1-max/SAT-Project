import Link from "next/link";
import { Hash, Lock } from "lucide-react";

import { listChannels } from "@/server/actions/student/community";
import { cn } from "@/lib/utils";

export const metadata = { title: "Community" };
export const dynamic = "force-dynamic";

export default async function CommunityLayout({ children }: { children: React.ReactNode }) {
  const channels = await listChannels();

  return (
    <div className="space-y-4">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Community</h1>
        <p className="text-sm text-muted-foreground">
          Ask questions, share what worked, help someone else out.
        </p>
      </div>

      <div className="grid gap-4 lg:grid-cols-[14rem_1fr]">
        <nav className="space-y-1">
          {channels.map((c) => (
            <Link
              key={c.id}
              href={`/community/${c.slug}`}
              className="flex items-center gap-2 rounded-lg px-3 py-2 text-sm hover:bg-secondary"
            >
              {c.isReadOnly ? (
                <Lock className="h-3.5 w-3.5 shrink-0 text-muted-foreground" />
              ) : (
                <Hash className="h-3.5 w-3.5 shrink-0 text-muted-foreground" />
              )}
              <span className="min-w-0 flex-1 truncate">{c.name}</span>
              {/* A mention is louder than an unread: it names you personally,
                  so it gets the coloured pill and unread gets a plain dot. */}
              {c.mentionsUnread > 0 ? (
                <span className="shrink-0 rounded-full bg-primary px-1.5 py-px text-[10px] font-semibold text-primary-foreground">
                  {c.mentionsUnread}
                </span>
              ) : c.unread > 0 ? (
                <span
                  className={cn("h-1.5 w-1.5 shrink-0 rounded-full bg-primary")}
                  title={`${c.unread} unread`}
                />
              ) : null}
            </Link>
          ))}
        </nav>

        <div className="min-w-0">{children}</div>
      </div>
    </div>
  );
}
