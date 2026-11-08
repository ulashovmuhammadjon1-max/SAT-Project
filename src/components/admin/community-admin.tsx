"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import {
  Archive,
  ArchiveRestore,
  ArrowDown,
  ArrowUp,
  ExternalLink,
  Flag,
  Loader2,
  Lock,
  Pencil,
  Plus,
  ShieldOff,
  Trash2,
  Timer,
} from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";
import { ChannelIcon, LocalStamp } from "@/components/community/bits";
import { CHANNEL_ICON_KEYS } from "@/lib/community/icons";
import { cn } from "@/lib/utils";
import {
  deleteCategory,
  findStudents,
  getCommunityAdmin,
  liftRestriction,
  moveCategory,
  moveChannel,
  removeAttachment,
  resolveReport,
  restrictUser,
  saveCategory,
  saveChannel,
  setChannelArchived,
  type ChannelInput,
} from "@/server/actions/admin/community";

type Data = Awaited<ReturnType<typeof getCommunityAdmin>>;
type Channel = Data["channels"][number];

export function CommunityAdmin({ data }: { data: Data }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [editing, setEditing] = useState<Channel | "new" | null>(null);
  const openReports = data.reports.filter((r) => r.status === "OPEN");

  const run = (fn: () => Promise<{ ok: boolean; error?: string }>, success?: string) =>
    start(async () => {
      const r = await fn();
      if (!r.ok) return void toast.error(r.error ?? "Something went wrong.");
      if (success) toast.success(success);
      router.refresh();
    });

  const grouped = [
    ...data.categories.map((c) => ({ ...c, channels: data.channels.filter((ch) => ch.categoryId === c.id) })),
    { id: null as string | null, name: "No category", order: 999, channels: data.channels.filter((ch) => !ch.categoryId || !data.categories.some((c) => c.id === ch.categoryId)) },
  ].filter((g) => g.id !== null || g.channels.length > 0);

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Community</h1>
          <p className="text-sm text-muted-foreground">Channels, categories, reports and restrictions. Every action here is logged.</p>
        </div>
        <Button asChild variant="outline">
          <Link href="/community">
            Open community <ExternalLink className="h-4 w-4" />
          </Link>
        </Button>
      </div>

      <Tabs defaultValue={openReports.length ? "reports" : "channels"}>
        <TabsList className="flex-wrap">
          <TabsTrigger value="channels">Channels</TabsTrigger>
          <TabsTrigger value="reports">
            Reports {openReports.length > 0 && <span className="ml-1.5 rounded-full bg-destructive px-1.5 text-[10px] font-bold text-destructive-foreground">{openReports.length}</span>}
          </TabsTrigger>
          <TabsTrigger value="restrictions">Restrictions</TabsTrigger>
          <TabsTrigger value="log">Moderation log</TabsTrigger>
        </TabsList>

        <TabsContent value="channels" className="mt-4 space-y-4">
          <div className="flex flex-wrap gap-2">
            <Button onClick={() => setEditing("new")}>
              <Plus className="h-4 w-4" /> New channel
            </Button>
            <Button
              variant="outline"
              onClick={() => {
                const name = window.prompt("Name of the new category");
                if (name) run(() => saveCategory(null, name), "Category created.");
              }}
            >
              <Plus className="h-4 w-4" /> New category
            </Button>
          </div>

          {grouped.map((g, gi) => (
            <section key={g.id ?? "none"} className="overflow-hidden rounded-xl border border-border bg-card">
              <div className="flex items-center gap-2 border-b border-border bg-secondary/40 px-4 py-2.5">
                <p className="flex-1 text-xs font-semibold uppercase tracking-[0.12em] text-muted-foreground">{g.name}</p>
                {g.id && (
                  <>
                    <IconBtn label="Move category up" disabled={gi === 0 || pending} onClick={() => run(() => moveCategory(g.id!, -1))}>
                      <ArrowUp className="h-3.5 w-3.5" />
                    </IconBtn>
                    <IconBtn label="Move category down" disabled={gi >= data.categories.length - 1 || pending} onClick={() => run(() => moveCategory(g.id!, 1))}>
                      <ArrowDown className="h-3.5 w-3.5" />
                    </IconBtn>
                    <IconBtn
                      label="Rename category"
                      onClick={() => {
                        const name = window.prompt("Rename category", g.name);
                        if (name) run(() => saveCategory(g.id, name), "Renamed.");
                      }}
                    >
                      <Pencil className="h-3.5 w-3.5" />
                    </IconBtn>
                    <IconBtn
                      label="Delete category"
                      onClick={() => {
                        if (window.confirm(`Delete “${g.name}”? Its channels are kept and move to “No category”.`)) run(() => deleteCategory(g.id!), "Category deleted.");
                      }}
                    >
                      <Trash2 className="h-3.5 w-3.5" />
                    </IconBtn>
                  </>
                )}
              </div>
              {g.channels.length === 0 ? (
                <p className="px-4 py-3 text-sm text-muted-foreground">No channels in this category.</p>
              ) : (
                <ul className="divide-y divide-border">
                  {g.channels.map((c, ci) => (
                    <li key={c.id} className={cn("flex flex-wrap items-center gap-3 px-4 py-3", c.isArchived && "opacity-60")}>
                      <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-primary/10 text-primary">
                        <ChannelIcon icon={c.icon} />
                      </span>
                      <div className="min-w-[12rem] flex-1">
                        <div className="flex flex-wrap items-center gap-2 text-sm font-medium">
                          {c.name} <span className="text-xs font-normal text-muted-foreground">/{c.slug}</span>
                          {c.isReadOnly && (
                            <Badge variant="outline" className="gap-1">
                              <Lock className="h-3 w-3" /> Admins post
                            </Badge>
                          )}
                          {c.slowModeSeconds > 0 && (
                            <Badge variant="outline" className="gap-1">
                              <Timer className="h-3 w-3" /> {c.slowModeSeconds}s
                            </Badge>
                          )}
                          {c.isArchived && <Badge variant="outline">Archived</Badge>}
                        </div>
                        <p className="text-xs text-muted-foreground">
                          {c.messages} messages{c.description ? ` · ${c.description}` : ""}
                        </p>
                      </div>
                      <div className="flex items-center gap-1">
                        <IconBtn label="Move up" disabled={ci === 0 || pending} onClick={() => run(() => moveChannel(c.id, -1))}>
                          <ArrowUp className="h-4 w-4" />
                        </IconBtn>
                        <IconBtn label="Move down" disabled={ci === g.channels.length - 1 || pending} onClick={() => run(() => moveChannel(c.id, 1))}>
                          <ArrowDown className="h-4 w-4" />
                        </IconBtn>
                        <Button size="sm" variant="outline" onClick={() => setEditing(c)}>
                          <Pencil className="h-4 w-4" /> Edit
                        </Button>
                        <Button
                          size="sm"
                          variant="ghost"
                          onClick={() => {
                            if (c.isArchived || window.confirm(`Archive #${c.name}? It disappears for students; messages are kept and it can be restored.`)) {
                              run(() => setChannelArchived(c.id, !c.isArchived), c.isArchived ? "Channel restored." : "Channel archived.");
                            }
                          }}
                        >
                          {c.isArchived ? <ArchiveRestore className="h-4 w-4" /> : <Archive className="h-4 w-4" />}
                          {c.isArchived ? "Restore" : "Archive"}
                        </Button>
                      </div>
                    </li>
                  ))}
                </ul>
              )}
            </section>
          ))}
        </TabsContent>

        <TabsContent value="reports" className="mt-4 space-y-3">
          {data.reports.length === 0 ? (
            <Empty text="No reports. Students can report any message or profile; reports land here." />
          ) : (
            data.reports.map((r) => <ReportCard key={r.id} r={r} pending={pending} run={run} />)
          )}
        </TabsContent>

        <TabsContent value="restrictions" className="mt-4 space-y-4">
          <RestrictForm run={run} pending={pending} />
          {data.restrictions.length === 0 ? (
            <Empty text="Nobody is restricted right now." />
          ) : (
            <ul className="divide-y divide-border overflow-hidden rounded-xl border border-border bg-card">
              {data.restrictions.map((r) => (
                <li key={r.userId} className="flex flex-wrap items-center gap-3 px-4 py-3">
                  <div className="min-w-[12rem] flex-1">
                    <p className="text-sm font-medium">
                      {r.name} <span className="text-xs text-muted-foreground">{r.email}</span>
                    </p>
                    <p className="text-xs text-muted-foreground">
                      Until <LocalStamp iso={r.until} mode="full" /> · {r.reason}
                    </p>
                  </div>
                  <Button size="sm" variant="outline" onClick={() => run(() => liftRestriction(r.userId), "Restriction lifted.")}>
                    <ShieldOff className="h-4 w-4" /> Lift
                  </Button>
                </li>
              ))}
            </ul>
          )}
        </TabsContent>

        <TabsContent value="log" className="mt-4">
          {data.log.length === 0 ? (
            <Empty text="No moderation actions yet." />
          ) : (
            <ul className="divide-y divide-border overflow-hidden rounded-xl border border-border bg-card">
              {data.log.map((l) => (
                <li key={l.id} className="px-4 py-2.5 text-sm">
                  <span className="font-medium">{l.actor}</span>{" "}
                  <span className="rounded bg-secondary px-1.5 py-0.5 font-mono text-[11px]">{l.action}</span>
                  {l.target && <> · {l.target}</>}
                  {l.note && <span className="text-muted-foreground"> · {l.note}</span>}
                  <LocalStamp iso={l.createdAt} mode="full" className="float-right text-xs text-muted-foreground" />
                </li>
              ))}
            </ul>
          )}
        </TabsContent>
      </Tabs>

      {editing && (
        <ChannelDialog
          channel={editing === "new" ? null : editing}
          categories={data.categories}
          onClose={() => setEditing(null)}
          onSaved={() => {
            setEditing(null);
            router.refresh();
          }}
        />
      )}
    </div>
  );
}

function IconBtn({ label, onClick, disabled, children }: { label: string; onClick: () => void; disabled?: boolean; children: React.ReactNode }) {
  return (
    <button type="button" aria-label={label} title={label} disabled={disabled} onClick={onClick} className="flex h-8 w-8 items-center justify-center rounded-lg text-muted-foreground hover:bg-secondary hover:text-foreground disabled:opacity-30">
      {children}
    </button>
  );
}

function Empty({ text }: { text: string }) {
  return <p className="rounded-xl border border-dashed border-border px-4 py-10 text-center text-sm text-muted-foreground">{text}</p>;
}

function ReportCard({
  r,
  pending,
  run,
}: {
  r: Data["reports"][number];
  pending: boolean;
  run: (fn: () => Promise<{ ok: boolean; error?: string }>, success?: string) => void;
}) {
  const [note, setNote] = useState("");
  const [days, setDays] = useState(3);
  const open = r.status === "OPEN";
  return (
    <div className={cn("rounded-xl border bg-card p-4", open ? "border-destructive/30" : "border-border opacity-75")}>
      <div className="flex flex-wrap items-center gap-2">
        <Flag className={cn("h-4 w-4", open ? "text-destructive" : "text-muted-foreground")} />
        <Badge variant="outline">{r.reason.toLowerCase()}</Badge>
        <Badge variant={open ? "warning" : "outline"}>{r.status.toLowerCase()}</Badge>
        <span className="text-xs text-muted-foreground">
          by {r.reporter} · <LocalStamp iso={r.createdAt} mode="full" />
        </span>
      </div>
      {r.target && (
        <p className="mt-2 text-sm">
          About <span className="font-medium">{r.target.name}</span> <span className="text-xs text-muted-foreground">{r.target.email}</span>
        </p>
      )}
      {r.details && <p className="mt-1 text-sm text-muted-foreground">“{r.details}”</p>}
      {r.message && (
        <div className="mt-3 rounded-lg border border-border bg-secondary/40 p-3">
          <p className="text-xs text-muted-foreground">
            In #{r.message.channel}
            {r.message.deleted && " · already removed"} ·{" "}
            <Link href={r.message.link} className="text-primary hover:underline">
              view in context
            </Link>
          </p>
          <p className="mt-1 whitespace-pre-wrap text-sm">{r.message.text || "(no text)"}</p>
          {r.message.attachments.length > 0 && (
            <ul className="mt-2 flex flex-wrap gap-2">
              {r.message.attachments.map((a) => (
                <li key={a.id} className="flex items-center gap-2 rounded-lg border border-border bg-background px-2 py-1 text-xs">
                  <a href={a.url} target="_blank" rel="noopener noreferrer" className="hover:underline">
                    {a.fileName}
                  </a>
                  <button type="button" className="text-destructive hover:underline" onClick={() => window.confirm("Remove this attachment for everyone?") && run(() => removeAttachment(a.id), "Attachment removed.")}>
                    Remove
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
      {r.directMessage && (
        <div className="mt-3 rounded-lg border border-border bg-secondary/40 p-3">
          <p className="text-xs text-muted-foreground">Private message{r.directMessage.deleted && " · already removed"}</p>
          <p className="mt-1 whitespace-pre-wrap text-sm">{r.directMessage.text}</p>
        </div>
      )}
      {open ? (
        <div className="mt-3 space-y-2">
          <Textarea value={note} onChange={(e) => setNote(e.target.value)} placeholder="Note for the log (optional; shown to the student if a message is removed)" className="min-h-16" />
          <div className="flex flex-wrap items-center gap-2">
            <Button size="sm" variant="outline" disabled={pending} onClick={() => run(() => resolveReport(r.id, "DISMISS", { note }), "Report dismissed.")}>
              Dismiss
            </Button>
            {(r.message || r.directMessage) && (
              <Button size="sm" variant="destructive" disabled={pending} onClick={() => run(() => resolveReport(r.id, "DELETE_MESSAGE", { note }), "Message removed.")}>
                <Trash2 className="h-4 w-4" /> Remove message
              </Button>
            )}
            {r.target && (
              <span className="inline-flex items-center gap-1.5">
                <Input type="number" min={1} max={365} value={days} onChange={(e) => setDays(Number(e.target.value))} className="h-9 w-20" aria-label="Days" />
                <Button size="sm" variant="outline" disabled={pending} onClick={() => run(() => resolveReport(r.id, "RESTRICT", { note, days }), "Student restricted.")}>
                  Restrict {days} day{days === 1 ? "" : "s"}
                </Button>
              </span>
            )}
          </div>
        </div>
      ) : (
        r.resolution && <p className="mt-2 text-xs text-muted-foreground">Resolution: {r.resolution}</p>
      )}
    </div>
  );
}

function RestrictForm({ run, pending }: { run: (fn: () => Promise<{ ok: boolean; error?: string }>, success?: string) => void; pending: boolean }) {
  const [q, setQ] = useState("");
  const [matches, setMatches] = useState<{ id: string; label: string }[]>([]);
  const [chosen, setChosen] = useState<{ id: string; label: string } | null>(null);
  const [days, setDays] = useState(3);
  const [reason, setReason] = useState("");
  return (
    <div className="rounded-xl border border-border bg-card p-4">
      <p className="text-sm font-semibold">Pause a student&apos;s posting</p>
      <p className="text-xs text-muted-foreground">They can still read. They are notified, and it lifts automatically.</p>
      <div className="mt-3 grid grid-cols-1 gap-2 sm:grid-cols-[1fr_6rem]">
        <div className="relative">
          <Input
            value={chosen ? chosen.label : q}
            onChange={async (e) => {
              setChosen(null);
              setQ(e.target.value);
              setMatches(await findStudents(e.target.value));
            }}
            placeholder="Search name, username or email"
          />
          {!chosen && matches.length > 0 && (
            <ul className="absolute z-10 mt-1 w-full overflow-hidden rounded-lg border border-border bg-popover shadow-lg">
              {matches.map((m) => (
                <li key={m.id}>
                  <button type="button" onClick={() => { setChosen(m); setMatches([]); }} className="block w-full px-3 py-2 text-left text-sm hover:bg-secondary">
                    {m.label}
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
        <Input type="number" min={1} max={365} value={days} onChange={(e) => setDays(Number(e.target.value))} aria-label="Days" />
      </div>
      <Input className="mt-2" value={reason} onChange={(e) => setReason(e.target.value)} placeholder="Reason (shown to the student)" />
      <Button className="mt-3" size="sm" disabled={!chosen || pending} onClick={() => chosen && run(() => restrictUser(chosen.id, days, reason), "Student restricted.")}>
        {pending && <Loader2 className="h-4 w-4 animate-spin" />} Restrict for {days} day{days === 1 ? "" : "s"}
      </Button>
    </div>
  );
}

function ChannelDialog({
  channel,
  categories,
  onClose,
  onSaved,
}: {
  channel: Channel | null;
  categories: Data["categories"];
  onClose: () => void;
  onSaved: () => void;
}) {
  const [form, setForm] = useState<ChannelInput>({
    name: channel?.name ?? "",
    slug: channel?.slug ?? "",
    description: channel?.description ?? "",
    icon: channel?.icon ?? "hash",
    categoryId: channel?.categoryId ?? categories[0]?.id ?? null,
    isReadOnly: channel?.isReadOnly ?? false,
    slowModeSeconds: channel?.slowModeSeconds ?? 0,
  });
  const [error, setError] = useState<string | null>(null);
  const [pending, start] = useTransition();
  const set = <K extends keyof ChannelInput>(k: K, v: ChannelInput[K]) => setForm((f) => ({ ...f, [k]: v }));

  return (
    <Dialog open onOpenChange={(o) => !o && !pending && onClose()}>
      <DialogContent className="max-h-[calc(100dvh-2rem)] w-[calc(100vw-2rem)] max-w-lg overflow-y-auto">
        <DialogHeader>
          <DialogTitle>{channel ? `Edit #${channel.name}` : "New channel"}</DialogTitle>
          <DialogDescription>Changes appear for students straight away.</DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            <div className="space-y-1.5">
              <Label htmlFor="ch-name">Name</Label>
              <Input
                id="ch-name"
                value={form.name}
                onChange={(e) => {
                  const name = e.target.value;
                  setForm((f) => ({ ...f, name, slug: channel ? f.slug : name.toLowerCase().replace(/&/g, "and").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40) }));
                }}
                maxLength={40}
              />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="ch-slug">URL name</Label>
              <Input id="ch-slug" value={form.slug} onChange={(e) => set("slug", e.target.value)} maxLength={40} />
              <p className="text-[11px] text-muted-foreground">/community/{form.slug || "…"}</p>
            </div>
          </div>
          <div className="space-y-1.5">
            <Label htmlFor="ch-desc">Description</Label>
            <Textarea id="ch-desc" value={form.description} onChange={(e) => set("description", e.target.value)} maxLength={200} className="min-h-16" />
          </div>
          <div className="space-y-1.5">
            <Label>Icon</Label>
            <div className="grid grid-cols-8 gap-1">
              {CHANNEL_ICON_KEYS.map((k) => (
                <button key={k} type="button" onClick={() => set("icon", k)} aria-label={k} aria-pressed={form.icon === k} className={cn("flex h-9 items-center justify-center rounded-lg border", form.icon === k ? "border-primary bg-primary/10 text-primary" : "border-border hover:bg-secondary")}>
                  <ChannelIcon icon={k} />
                </button>
              ))}
            </div>
          </div>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            <div className="space-y-1.5">
              <Label htmlFor="ch-cat">Category</Label>
              <select id="ch-cat" value={form.categoryId ?? ""} onChange={(e) => set("categoryId", e.target.value || null)} className="block w-full rounded-lg border border-input bg-background px-2.5 py-2 text-sm">
                {categories.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.name}
                  </option>
                ))}
                <option value="">No category</option>
              </select>
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="ch-slow">Slow mode (seconds)</Label>
              <Input id="ch-slow" type="number" min={0} max={3600} value={form.slowModeSeconds} onChange={(e) => set("slowModeSeconds", Number(e.target.value))} />
            </div>
          </div>
          <div className="flex items-start justify-between gap-4 rounded-lg border border-border p-3">
            <div>
              <p className="text-sm font-medium">Only admins can post</p>
              <p className="text-xs text-muted-foreground">For announcements. Students can read and react.</p>
            </div>
            <Switch checked={form.isReadOnly} onCheckedChange={(v) => set("isReadOnly", v)} aria-label="Only admins can post" />
          </div>
          {error && <p className="rounded-lg bg-destructive/10 px-3 py-2 text-sm text-destructive">{error}</p>}
        </div>
        <DialogFooter className="gap-2 sm:gap-0">
          <Button variant="outline" onClick={onClose} disabled={pending}>
            Cancel
          </Button>
          <Button
            disabled={pending}
            onClick={() =>
              start(async () => {
                setError(null);
                const r = await saveChannel(channel?.id ?? null, form);
                if (!r.ok) return setError(r.error);
                toast.success(channel ? "Channel updated." : "Channel created.");
                onSaved();
              })
            }
          >
            {pending && <Loader2 className="h-4 w-4 animate-spin" />} {channel ? "Save" : "Create channel"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
