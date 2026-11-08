"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import {
  ArrowRight,
  BarChart3,
  CircleHelp,
  Compass,
  Flame,
  Library,
  Megaphone,
  Search,
  Sparkles,
  Trophy,
  Users,
  MessageSquareText,
} from "lucide-react";

import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import type { CategoryView, CommunityMessageView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import type { CommunityHome as HomeData } from "@/server/actions/student/community";

import { ChannelIcon, LocalStamp, MemberAvatar, useMounted } from "./bits";
import { MessageItem } from "./message-item";
import { NavToggle } from "./community-shell";

function greeting() {
  const h = new Date().getHours();
  return h < 5 ? "Up late" : h < 12 ? "Good morning" : h < 18 ? "Good afternoon" : "Good evening";
}

export function CommunityHomeView({ data, categories }: { data: HomeData; categories: CategoryView[] }) {
  const router = useRouter();
  const [lists, setLists] = useState(data);
  const [q, setQ] = useState("");
  const firstName = data.me.name.split(" ")[0];
  const mounted = useMounted();
  const channels = categories.flatMap((c) => c.channels);
  const postable = channels.filter((c) => !c.isReadOnly);

  const patch = (id: string, p: Partial<CommunityMessageView>) =>
    setLists((d) => {
      const fix = (xs: CommunityMessageView[]) => xs.map((m) => (m.id === id ? { ...m, ...p } : m));
      return { ...d, trending: fix(d.trending), unanswered: fix(d.unanswered), recent: fix(d.recent), resources: fix(d.resources), achievements: fix(d.achievements), announcements: fix(d.announcements) };
    });
  const handlers = { onPatch: patch };

  const feature = lists.trending.length > 0 ? lists.trending : lists.recent;
  const announcement = lists.announcements[0];
  // Channels with something new for this student first, then the rest.
  const recommended = [...postable].sort((a, b) => b.unread + b.mentionsUnread * 5 - (a.unread + a.mentionsUnread * 5)).slice(0, 6);

  return (
    <div className="min-h-0 flex-1 overflow-y-auto">
      <div className="flex h-14 items-center gap-2 border-b border-border px-3 lg:hidden">
        <NavToggle />
        <span className="font-serif text-lg">Community</span>
      </div>

      {/* Hero */}
      <section className="relative overflow-hidden border-b border-border">
        <div aria-hidden className="pointer-events-none absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,hsl(var(--primary)/0.16),transparent_55%),radial-gradient(ellipse_at_bottom_left,hsl(var(--accent-foreground)/0.08),transparent_50%)]" />
        <div aria-hidden className="pointer-events-none absolute inset-0 opacity-[0.35] [background-image:linear-gradient(hsl(var(--border))_1px,transparent_1px),linear-gradient(90deg,hsl(var(--border))_1px,transparent_1px)] [background-size:44px_44px] [mask-image:linear-gradient(to_bottom,black,transparent)]" />
        <div className="relative mx-auto max-w-6xl px-5 pb-8 pt-8 sm:px-8 sm:pt-12">
          <p className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">The Scholarly Community</p>
          <h1 className="mt-3 max-w-3xl font-serif text-[2.1rem] font-medium leading-[1.08] tracking-[-0.02em] text-foreground sm:text-5xl">
            <span suppressHydrationWarning>{mounted ? greeting() : "Welcome back"}</span>, {firstName}.<br />
            <span className="italic text-muted-foreground">What are you curious about today?</span>
          </h1>

          <form
            onSubmit={(e) => {
              e.preventDefault();
              router.push(`/community/search?q=${encodeURIComponent(q)}`);
            }}
            className="mt-6 flex max-w-2xl items-center gap-2 rounded-2xl border border-border bg-card/90 p-1.5 shadow-sm backdrop-blur focus-within:border-primary/50 focus-within:shadow-[0_0_0_4px_hsl(var(--primary)/0.1)]"
          >
            <Search className="ml-2.5 h-5 w-5 shrink-0 text-muted-foreground" />
            <input
              value={q}
              onChange={(e) => setQ(e.target.value)}
              placeholder="Search questions, resources and discussions"
              className="min-w-0 flex-1 bg-transparent py-2 text-[15px] placeholder:text-muted-foreground/80 focus:outline-none"
              aria-label="Search the community"
            />
            <button type="submit" className="rounded-xl bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground hover:brightness-110">
              Search
            </button>
          </form>

          <div className="mt-5 flex flex-wrap gap-2">
            <QuickPost label="Ask a question" icon={CircleHelp} kind="QUESTION" channels={postable} preferred={["math", "reading-writing", "ielts", "ap"]} tone="primary" />
            <QuickPost label="Share a resource" icon={Library} kind="RESOURCE" channels={postable} preferred={["resources"]} />
            <QuickPost label="Celebrate a win" icon={Trophy} kind="ACHIEVEMENT" channels={postable} preferred={["achievements"]} />
            <QuickPost label="Start a poll" icon={BarChart3} kind="POLL" channels={postable} preferred={["general"]} />
          </div>
        </div>
      </section>

      <div className="mx-auto grid grid-cols-1 max-w-6xl gap-8 px-5 py-8 sm:px-8 lg:grid-cols-[minmax(0,1fr)_20rem]">
        <div className="min-w-0 space-y-10">
          {announcement && (
            <Link
              href={`/community/${announcement.channelSlug}?m=${announcement.id}`}
              className="group flex items-start gap-4 rounded-2xl border border-primary/25 bg-gradient-to-r from-primary/[0.09] via-card to-card p-5 transition-shadow hover:shadow-md"
            >
              <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-foreground text-background">
                <Megaphone className="h-5 w-5" />
              </span>
              <span className="min-w-0 flex-1">
                <span className="text-[11px] font-semibold uppercase tracking-wider text-primary">Latest announcement · <LocalStamp iso={announcement.createdAt} mode="relative" /></span>
                <span className="mt-1 block font-serif text-xl font-medium leading-snug">{announcement.title ?? announcement.body.split("\n")[0].slice(0, 120)}</span>
                {announcement.title && <span className="mt-1 line-clamp-2 block text-sm text-muted-foreground">{announcement.body}</span>}
              </span>
              <ArrowRight className="mt-1 h-5 w-5 shrink-0 text-muted-foreground transition-transform group-hover:translate-x-1 group-hover:text-primary" />
            </Link>
          )}

          <Section
            icon={lists.trending.length ? Flame : Sparkles}
            title={lists.trending.length ? "Highlights" : "Recent conversations"}
            subtitle={lists.trending.length ? "The discussions with the most replies, reactions and saves over the last two weeks." : "The latest from across the channels."}
          >
            {feature.length === 0 ? (
              <EmptyCard
                icon={MessageSquareText}
                title="It's quiet here — for now"
                body="Be the first to start a conversation. Ask a question, share something useful, or introduce yourself."
                href="/community/introductions"
                cta="Introduce yourself"
              />
            ) : (
              <div className="divide-y divide-border overflow-hidden rounded-2xl border border-border bg-card">
                {feature.map((m) => (
                  <FeedItem key={m.id} m={m} handlers={handlers} />
                ))}
              </div>
            )}
          </Section>

          <Section icon={CircleHelp} title="Unanswered questions" subtitle="Help someone get unstuck. Answers can be accepted as the solution.">
            {lists.unanswered.length === 0 ? (
              <EmptyCard icon={CircleHelp} title="Every question has an answer" body="Nothing is waiting right now. Got a question of your own?" href={`/community/${postable.find((c) => c.slug === "math")?.slug ?? postable[0]?.slug ?? "general"}?compose=question`} cta="Ask a question" />
            ) : (
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                {lists.unanswered.map((m) => (
                  <Link
                    key={m.id}
                    href={`/community/${m.channelSlug}?thread=${m.id}`}
                    className="group flex flex-col rounded-2xl border border-border bg-card p-4 transition-all hover:-translate-y-0.5 hover:border-primary/40 hover:shadow-md"
                  >
                    <span className="flex items-center gap-2 text-xs text-muted-foreground">
                      <MemberAvatar id={m.author.id} name={m.author.name} image={m.author.image} size={22} />
                      {m.author.name} · #{channels.find((c) => c.slug === m.channelSlug)?.name ?? m.channelSlug}
                    </span>
                    <span className="mt-2 font-serif text-lg font-medium leading-snug group-hover:text-primary">{m.title}</span>
                    {m.subject && <span className="mt-2 w-fit rounded-full border border-border px-2 py-0.5 text-[11px] text-muted-foreground">{m.subject}</span>}
                    <span className="mt-auto flex items-center gap-1 pt-3 text-sm font-semibold text-primary">
                      Help answer <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                    </span>
                  </Link>
                ))}
              </div>
            )}
          </Section>

          {lists.achievements.length > 0 && (
            <Section icon={Trophy} title="Recent achievements" subtitle="Scores, offers and milestones from the community.">
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                {lists.achievements.map((m) => (
                  <Link
                    key={m.id}
                    href={`/community/${m.channelSlug}?m=${m.id}`}
                    className="group relative overflow-hidden rounded-2xl border border-warning/30 bg-gradient-to-br from-warning/[0.14] via-card to-card p-4 transition-shadow hover:shadow-md"
                  >
                    <span aria-hidden className="absolute -right-3 -top-3 text-6xl opacity-15">🏆</span>
                    <span className="flex items-center gap-2 text-xs text-muted-foreground">
                      <MemberAvatar id={m.author.id} name={m.author.name} image={m.author.image} size={22} />
                      <span className="font-medium text-foreground">{m.author.name}</span> · <LocalStamp iso={m.createdAt} mode="relative" />
                    </span>
                    <span className="mt-2 block font-serif text-lg font-medium leading-snug">{m.title ?? m.body.slice(0, 100)}</span>
                    <span className="mt-2 block text-xs text-muted-foreground">
                      {(m.reactions.find((r) => r.emoji === "🎉")?.count ?? 0) > 0 ? `🎉 ${m.reactions.find((r) => r.emoji === "🎉")!.count} congratulations` : "Be the first to congratulate"}
                    </span>
                  </Link>
                ))}
              </div>
            </Section>
          )}
        </div>

        <aside className="space-y-6">
          <SideCard icon={Users} title="Active now">
            {lists.activeMembers.length === 0 ? (
              <p className="text-sm text-muted-foreground">Nobody else is around right now. Posts still reach everyone.</p>
            ) : (
              <>
                <div className="flex flex-wrap gap-1.5">
                  {lists.activeMembers.map((p) => (
                    <span key={p.id} title={p.name}>
                      <MemberAvatar id={p.id} name={p.name} image={p.image} size={34} online />
                    </span>
                  ))}
                </div>
                <p className="mt-2 text-xs text-muted-foreground">
                  {lists.activeMembers.length === 1 ? "1 student" : `${lists.activeMembers.length} students`} active in the last few minutes
                </p>
              </>
            )}
          </SideCard>

          <SideCard icon={Compass} title="Channels for you">
            <ul className="-mx-1 space-y-0.5">
              {recommended.map((c) => (
                <li key={c.id}>
                  <Link href={`/community/${c.slug}`} className="flex items-center gap-3 rounded-lg px-1 py-1.5 hover:bg-secondary/70">
                    <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
                      <ChannelIcon icon={c.icon} />
                    </span>
                    <span className="min-w-0 flex-1">
                      <span className="block truncate text-sm font-medium">{c.name}</span>
                      {c.description && <span className="block truncate text-xs text-muted-foreground">{c.description}</span>}
                    </span>
                    {c.unread > 0 && !c.muted && <span className="rounded-full bg-primary/15 px-1.5 text-[11px] font-semibold text-primary">{c.unread}</span>}
                  </Link>
                </li>
              ))}
            </ul>
          </SideCard>

          <SideCard icon={Library} title="Popular resources">
            {lists.resources.length === 0 ? (
              <p className="text-sm text-muted-foreground">
                No resources yet.{" "}
                <Link href="/community/resources?compose=resource" className="font-medium text-primary hover:underline">
                  Share the first one
                </Link>
                .
              </p>
            ) : (
              <ul className="space-y-3">
                {lists.resources.map((m) => (
                  <li key={m.id}>
                    <Link href={`/community/${m.channelSlug}?m=${m.id}`} className="group block">
                      <span className="block text-sm font-semibold leading-snug group-hover:text-primary">{m.title ?? m.attachments[0]?.fileName ?? m.body.slice(0, 60)}</span>
                      <span className="text-xs text-muted-foreground">
                        {m.author.name} · {m.bookmarked ? "Saved · " : ""}
                        {m.reactions.reduce((n, r) => n + r.count, 0)} reactions
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </SideCard>
        </aside>
      </div>
    </div>
  );
}

function FeedItem({ m, handlers }: { m: CommunityMessageView; handlers: { onPatch: (id: string, p: Partial<CommunityMessageView>) => void } }) {
  return (
    <div className="relative">
      <MessageItem message={m} context="list" handlers={handlers} />
      <div className="pointer-events-none -mt-1 flex items-center gap-3 px-4 pb-3 pl-[4.25rem] text-xs text-muted-foreground">
        <span className="font-medium">#{m.channelSlug}</span>
        {m.replyCount > 0 && <span>{m.replyCount} {m.replyCount === 1 ? "reply" : "replies"}</span>}
      </div>
    </div>
  );
}

function Section({ icon: Icon, title, subtitle, children }: { icon: typeof Flame; title: string; subtitle?: string; children: React.ReactNode }) {
  return (
    <section>
      <div className="mb-4 flex items-end gap-3">
        <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-primary/10 text-primary">
          <Icon className="h-[18px] w-[18px]" />
        </span>
        <div>
          <h2 className="font-display text-lg font-semibold tracking-tight">{title}</h2>
          {subtitle && <p className="text-sm text-muted-foreground">{subtitle}</p>}
        </div>
      </div>
      {children}
    </section>
  );
}

function SideCard({ icon: Icon, title, children }: { icon: typeof Flame; title: string; children: React.ReactNode }) {
  return (
    <div className="rounded-2xl border border-border bg-card p-4 shadow-sm">
      <p className="mb-3 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.12em] text-muted-foreground">
        <Icon className="h-3.5 w-3.5" /> {title}
      </p>
      {children}
    </div>
  );
}

function EmptyCard({ icon: Icon, title, body, href, cta }: { icon: typeof Flame; title: string; body: string; href: string; cta: string }) {
  return (
    <div className="flex flex-col items-center rounded-2xl border border-dashed border-border bg-card/50 px-6 py-10 text-center">
      <span className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent text-primary">
        <Icon className="h-5 w-5" />
      </span>
      <p className="mt-3 font-serif text-xl font-medium">{title}</p>
      <p className="mt-1 max-w-sm text-sm text-muted-foreground">{body}</p>
      <Link href={href} className="mt-4 inline-flex items-center gap-1.5 rounded-xl bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground hover:brightness-110">
        {cta} <ArrowRight className="h-4 w-4" />
      </Link>
    </div>
  );
}

function QuickPost({
  label,
  icon: Icon,
  kind,
  channels,
  preferred,
  tone,
}: {
  label: string;
  icon: typeof Flame;
  kind: string;
  channels: CategoryView["channels"];
  preferred: string[];
  tone?: "primary";
}) {
  const router = useRouter();
  const sorted = [...channels].sort((a, b) => {
    const ia = preferred.indexOf(a.slug);
    const ib = preferred.indexOf(b.slug);
    return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
  });
  return (
    <Popover>
      <PopoverTrigger asChild>
        <button
          type="button"
          className={cn(
            "inline-flex items-center gap-2 rounded-xl border px-3.5 py-2 text-sm font-medium shadow-sm transition-all hover:-translate-y-px hover:shadow",
            tone === "primary" ? "border-primary bg-primary text-primary-foreground" : "border-border bg-card hover:border-primary/40",
          )}
        >
          <Icon className="h-4 w-4" /> {label}
        </button>
      </PopoverTrigger>
      <PopoverContent align="start" className="w-64 p-1.5">
        <p className="px-2 pb-1.5 pt-1 text-xs font-semibold uppercase tracking-wide text-muted-foreground">Post in…</p>
        {sorted.slice(0, 8).map((c) => (
          <button
            key={c.id}
            type="button"
            onClick={() => router.push(`/community/${c.slug}?compose=${kind.toLowerCase()}`)}
            className="flex w-full items-center gap-2.5 rounded-lg px-2 py-1.5 text-left text-sm hover:bg-secondary"
          >
            <ChannelIcon icon={c.icon} className="text-muted-foreground" /> {c.name}
          </button>
        ))}
      </PopoverContent>
    </Popover>
  );
}
