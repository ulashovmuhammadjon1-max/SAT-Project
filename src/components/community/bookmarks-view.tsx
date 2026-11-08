"use client";

import { useState } from "react";
import Link from "next/link";
import { Bookmark } from "lucide-react";

import type { CommunityMessageView } from "@/lib/community/types";

import { MessageItem } from "./message-item";
import { PageHeader } from "./community-shell";

export function BookmarksView({ initial }: { initial: CommunityMessageView[] }) {
  const [items, setItems] = useState(initial);
  const patch = (id: string, p: Partial<CommunityMessageView>) =>
    setItems((xs) => (p.bookmarked === false ? xs.filter((m) => m.id !== id) : xs.map((m) => (m.id === id ? { ...m, ...p } : m))));
  return (
    <div className="flex min-h-0 min-w-0 flex-1 flex-col">
      <PageHeader title="Saved" subtitle="Discussions and resources you bookmarked" icon={Bookmark} />
      <div className="min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto max-w-3xl px-4 py-6 sm:px-6">
          {items.length === 0 ? (
            <div className="flex flex-col items-center rounded-2xl border border-dashed border-border px-6 py-16 text-center">
              <span className="flex h-12 w-12 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                <Bookmark className="h-5 w-5" />
              </span>
              <p className="mt-3 font-serif text-xl">Nothing saved yet</p>
              <p className="mt-1 max-w-sm text-sm text-muted-foreground">
                Hover over any message and press the bookmark to keep it here — useful answers, resources, notes.
              </p>
              <Link href="/community" className="mt-4 text-sm font-semibold text-primary hover:underline">
                Explore the community →
              </Link>
            </div>
          ) : (
            <div className="divide-y divide-border overflow-hidden rounded-2xl border border-border bg-card">
              {items.map((m) => (
                <div key={m.id} className="relative">
                  <MessageItem message={m} context="list" handlers={{ onPatch: patch }} />
                  <button
                    type="button"
                    onClick={async () => {
                      const { toggleBookmark } = await import("@/server/actions/student/community");
                      const r = await toggleBookmark(m.id);
                      if (r.ok && !r.bookmarked) patch(m.id, { bookmarked: false });
                    }}
                    className="absolute right-3 top-3 z-10 rounded-lg border border-border bg-background px-2.5 py-1 text-xs font-medium text-muted-foreground hover:text-foreground"
                  >
                    Remove
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
