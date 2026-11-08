"use client";

import { useEffect, useState, useTransition } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Loader2, Paperclip, Search, SlidersHorizontal } from "lucide-react";

import type { ChannelView, CommunityMessageView, MessageKind } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import { searchMessages } from "@/server/actions/student/community";

import { MessageItem } from "./message-item";
import { PageHeader } from "./community-shell";

const KINDS: { id: MessageKind | ""; label: string }[] = [
  { id: "", label: "Everything" },
  { id: "QUESTION", label: "Questions" },
  { id: "RESOURCE", label: "Resources" },
  { id: "ACHIEVEMENT", label: "Achievements" },
  { id: "POLL", label: "Polls" },
  { id: "ANNOUNCEMENT", label: "Announcements" },
];

export function SearchView({ channels }: { channels: ChannelView[] }) {
  const router = useRouter();
  const params = useSearchParams();
  const [q, setQ] = useState(params.get("q") ?? "");
  const [channel, setChannel] = useState(params.get("channel") ?? "");
  const [kind, setKind] = useState<MessageKind | "">((params.get("kind") as MessageKind) ?? "");
  const [author, setAuthor] = useState(params.get("author") ?? "");
  const [from, setFrom] = useState(params.get("from") ?? "");
  const [to, setTo] = useState(params.get("to") ?? "");
  const [files, setFiles] = useState(params.get("files") === "1");
  const [showFilters, setShowFilters] = useState(Boolean(params.get("author") || params.get("from") || params.get("to")));
  const [results, setResults] = useState<CommunityMessageView[] | null>(null);
  const [hasMore, setHasMore] = useState(false);
  const [page, setPage] = useState(0);
  const [pending, start] = useTransition();

  function run(nextPage = 0) {
    const sp = new URLSearchParams();
    if (q) sp.set("q", q);
    if (channel) sp.set("channel", channel);
    if (kind) sp.set("kind", kind);
    if (author) sp.set("author", author);
    if (from) sp.set("from", from);
    if (to) sp.set("to", to);
    if (files) sp.set("files", "1");
    if (nextPage === 0) router.replace(`/community/search?${sp}`, { scroll: false });
    start(async () => {
      const r = await searchMessages({ q, channel: channel || null, kind: kind || null, author: author || null, from: from || null, to: to || null, hasAttachments: files, page: nextPage });
      setResults((prev) => (nextPage === 0 ? r.results : [...(prev ?? []), ...r.results]));
      setHasMore(r.hasMore);
      setPage(nextPage);
    });
  }

  useEffect(() => {
    if (q || kind || files || author || from || to) run(0);
    // Run once for a shared link with filters already in it.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const patch = (id: string, p: Partial<CommunityMessageView>) => setResults((xs) => xs?.map((m) => (m.id === id ? { ...m, ...p } : m)) ?? null);

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <PageHeader title="Search" subtitle="Find questions, answers, resources and discussions" icon={Search} />
      <div className="min-h-0 flex-1 overflow-y-auto">
        <div className="mx-auto max-w-3xl px-4 py-6 sm:px-6">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              run(0);
            }}
            className="space-y-3"
          >
            <div className="flex items-center gap-2 rounded-2xl border border-border bg-card p-1.5 shadow-sm focus-within:border-primary/50">
              <Search className="ml-2 h-5 w-5 text-muted-foreground" />
              <input autoFocus value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search the community…" className="min-w-0 flex-1 bg-transparent py-2 text-[15px] focus:outline-none" aria-label="Search terms" />
              <button type="button" onClick={() => setShowFilters((v) => !v)} aria-expanded={showFilters} className={cn("flex h-9 w-9 items-center justify-center rounded-xl", showFilters ? "bg-primary/10 text-primary" : "text-muted-foreground hover:bg-secondary")} aria-label="Filters">
                <SlidersHorizontal className="h-4 w-4" />
              </button>
              <button type="submit" className="rounded-xl bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground">
                Search
              </button>
            </div>
            <div className="flex flex-wrap gap-1.5">
              {KINDS.map((k) => (
                <button key={k.id || "all"} type="button" onClick={() => setKind(k.id)} className={cn("rounded-full border px-3 py-2 text-xs font-medium transition-colors sm:py-1", kind === k.id ? "border-primary bg-primary text-primary-foreground" : "border-border bg-card hover:border-primary/40")}>
                  {k.label}
                </button>
              ))}
              <button type="button" onClick={() => setFiles((v) => !v)} className={cn("inline-flex items-center gap-1 rounded-full border px-3 py-1 text-xs font-medium", files ? "border-primary bg-primary text-primary-foreground" : "border-border bg-card hover:border-primary/40")}>
                <Paperclip className="h-3 w-3" /> Has files
              </button>
            </div>
            {showFilters && (
              <div className="grid grid-cols-1 gap-3 rounded-2xl border border-border bg-card p-4 sm:grid-cols-2 animate-fade-in">
                <label className="text-xs font-medium text-muted-foreground">
                  Channel
                  <select value={channel} onChange={(e) => setChannel(e.target.value)} className="mt-1 block w-full rounded-lg border border-input bg-background px-2.5 py-2 text-sm text-foreground">
                    <option value="">All channels</option>
                    {channels.map((c) => (
                      <option key={c.id} value={c.slug}>
                        {c.name}
                      </option>
                    ))}
                  </select>
                </label>
                <label className="text-xs font-medium text-muted-foreground">
                  Author
                  <input value={author} onChange={(e) => setAuthor(e.target.value)} placeholder="Name" className="mt-1 block w-full rounded-lg border border-input bg-background px-2.5 py-2 text-sm text-foreground" />
                </label>
                <label className="text-xs font-medium text-muted-foreground">
                  From
                  <input type="date" value={from} onChange={(e) => setFrom(e.target.value)} className="mt-1 block w-full rounded-lg border border-input bg-background px-2.5 py-2 text-sm text-foreground" />
                </label>
                <label className="text-xs font-medium text-muted-foreground">
                  To
                  <input type="date" value={to} onChange={(e) => setTo(e.target.value)} className="mt-1 block w-full rounded-lg border border-input bg-background px-2.5 py-2 text-sm text-foreground" />
                </label>
              </div>
            )}
          </form>

          <div className="mt-6">
            {pending && results === null ? (
              <div className="flex justify-center py-16">
                <Loader2 className="h-5 w-5 animate-spin text-muted-foreground" />
              </div>
            ) : results === null ? (
              <p className="py-16 text-center text-sm text-muted-foreground">Search by words, or pick a type or filter to browse.</p>
            ) : results.length === 0 ? (
              <div className="py-16 text-center">
                <p className="font-serif text-xl">Nothing found</p>
                <p className="mt-1 text-sm text-muted-foreground">Try fewer words, or a different channel or type.</p>
              </div>
            ) : (
              <>
                <p className="mb-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
                  {results.length}
                  {hasMore ? "+" : ""} results
                </p>
                <div className="divide-y divide-border overflow-hidden rounded-2xl border border-border bg-card">
                  {results.map((m) => (
                    <MessageItem key={m.id} message={m} context="list" handlers={{ onPatch: patch }} />
                  ))}
                </div>
                {hasMore && (
                  <div className="mt-4 flex justify-center">
                    <button type="button" onClick={() => run(page + 1)} disabled={pending} className="inline-flex items-center gap-2 rounded-full border border-border px-4 py-2 text-sm font-medium hover:bg-secondary">
                      {pending && <Loader2 className="h-4 w-4 animate-spin" />} Load more
                    </button>
                  </div>
                )}
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
