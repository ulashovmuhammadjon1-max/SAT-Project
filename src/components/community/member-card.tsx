"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Ban, CheckCircle2, Flag, Loader2, MessageCircle, PenLine } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { Skeleton } from "@/components/ui/skeleton";
import { Textarea } from "@/components/ui/textarea";
import type { MemberProfileView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import { openConversation } from "@/server/actions/student/community-dm";
import { blockUser, getMemberProfile, reportContent, unblockUser } from "@/server/actions/student/community";

import { MemberAvatar, RoleBadge } from "./bits";

/** Clicking a name or avatar opens this. Loads the profile on first open. */
export function MemberPopover({ userId, children }: { userId: string; children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  const [profile, setProfile] = useState<MemberProfileView | null>(null);
  const [reporting, setReporting] = useState(false);

  async function onOpenChange(next: boolean) {
    setOpen(next);
    if (next && !profile) setProfile(await getMemberProfile(userId));
  }

  return (
    <>
      <Popover open={open} onOpenChange={(o) => void onOpenChange(o)}>
        <PopoverTrigger asChild>{children}</PopoverTrigger>
        <PopoverContent align="start" sideOffset={8} className="w-80 max-w-[calc(100vw-1.5rem)] overflow-hidden p-0">
          {profile ? (
            <MemberCard
              profile={profile}
              onChanged={setProfile}
              onReport={() => {
                setOpen(false);
                setReporting(true);
              }}
              onDone={() => setOpen(false)}
            />
          ) : (
            <div className="space-y-3 p-4">
              <div className="flex items-center gap-3">
                <Skeleton className="h-14 w-14 rounded-full" />
                <div className="flex-1 space-y-2">
                  <Skeleton className="h-4 w-2/3" />
                  <Skeleton className="h-3 w-1/2" />
                </div>
              </div>
              <Skeleton className="h-12 w-full" />
            </div>
          )}
        </PopoverContent>
      </Popover>
      {reporting && (
        <ReportDialog target={{ userId }} open={reporting} onOpenChange={setReporting} />
      )}
    </>
  );
}

function MemberCard({
  profile: p,
  onChanged,
  onReport,
  onDone,
}: {
  profile: MemberProfileView;
  onChanged: (p: MemberProfileView) => void;
  onReport: () => void;
  onDone: () => void;
}) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const joined = new Date(p.joined).toLocaleDateString(undefined, { month: "long", year: "numeric" });

  return (
    <div>
      <div className="h-16 bg-gradient-to-br from-primary/30 via-primary/10 to-accent" />
      <div className="-mt-8 px-4 pb-4">
        <MemberAvatar id={p.id} name={p.name} image={p.image} size={60} isAdmin={p.isAdmin} online={p.activeNow} className="ring-4 ring-popover rounded-full" />
        <div className="mt-2 flex flex-wrap items-center gap-2">
          <p className="font-display text-lg font-semibold leading-tight">{p.name}</p>
          <RoleBadge isAdmin={p.isAdmin} isMentor={p.isMentor} />
        </div>
        <p className="text-xs text-muted-foreground">
          {p.activeNow ? <span className="font-medium text-success">Active now · </span> : null}
          Member since {joined}
        </p>
        {p.bio && <p className="mt-3 text-sm leading-relaxed text-foreground/85">{p.bio}</p>}

        <dl className="mt-3 grid grid-cols-2 gap-2">
          <div className="rounded-lg bg-secondary/70 px-3 py-2">
            <dt className="text-[11px] uppercase tracking-wide text-muted-foreground">Posts</dt>
            <dd className="font-display text-lg font-semibold tabular-nums">{p.posts}</dd>
          </div>
          <div className="rounded-lg bg-secondary/70 px-3 py-2">
            <dt className="flex items-center gap-1 text-[11px] uppercase tracking-wide text-muted-foreground">
              <CheckCircle2 className="h-3 w-3 text-success" /> Accepted answers
            </dt>
            <dd className="font-display text-lg font-semibold tabular-nums">{p.acceptedAnswers}</dd>
          </div>
        </dl>

        {[
          ["Can help with", p.helpsWith],
          ["Studying", p.studying],
          ["Interests", p.interests],
        ].map(([label, tags]) =>
          (tags as string[]).length ? (
            <div key={label as string} className="mt-3">
              <p className="text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">{label as string}</p>
              <div className="mt-1 flex flex-wrap gap-1">
                {(tags as string[]).map((t) => (
                  <span key={t} className="rounded-full border border-border bg-background px-2 py-0.5 text-xs">
                    {t}
                  </span>
                ))}
              </div>
            </div>
          ) : null,
        )}

        <div className="mt-4 flex flex-wrap gap-2">
          {p.isMe ? (
            <Button size="sm" variant="outline" className="h-9" onClick={() => { onDone(); router.push("/community/settings"); }}>
              <PenLine className="h-4 w-4" /> Edit profile
            </Button>
          ) : (
            <>
              {p.canMessage && (
                <Button
                  size="sm"
                  className="h-9"
                  disabled={pending}
                  onClick={() =>
                    start(async () => {
                      const r = await openConversation(p.id);
                      if (!r.ok) return void toast.error(r.error);
                      onDone();
                      router.push(`/community/messages/${r.id}`);
                    })
                  }
                >
                  {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <MessageCircle className="h-4 w-4" />}
                  Message
                </Button>
              )}
              {!p.isAdmin && (
                <Button
                  size="sm"
                  variant="outline"
                  className="h-9"
                  disabled={pending}
                  onClick={() =>
                    start(async () => {
                      if (!p.blockedByMe && !window.confirm(`Block ${p.name}? You will not see their messages or get notifications from them, and they cannot message you.`)) return;
                      const r = p.blockedByMe ? await unblockUser(p.id) : await blockUser(p.id);
                      if (!r.ok) return void toast.error(r.error);
                      toast.success(p.blockedByMe ? `${p.name} unblocked.` : `${p.name} blocked.`);
                      onChanged({ ...p, blockedByMe: !p.blockedByMe, canMessage: p.blockedByMe });
                      // Open channels and threads re-fetch so the change shows at once.
                      window.dispatchEvent(new Event("community:refresh"));
                      router.refresh();
                    })
                  }
                >
                  <Ban className="h-4 w-4" /> {p.blockedByMe ? "Unblock" : "Block"}
                </Button>
              )}
              <Button size="sm" variant="ghost" className="h-9 text-muted-foreground" onClick={onReport}>
                <Flag className="h-4 w-4" /> Report
              </Button>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

const REASONS = [
  { id: "SPAM", label: "Spam or advertising" },
  { id: "HARASSMENT", label: "Harassment or bullying" },
  { id: "INAPPROPRIATE", label: "Inappropriate content" },
  { id: "MISINFORMATION", label: "Cheating or misleading information" },
  { id: "OTHER", label: "Something else" },
] as const;

export function ReportDialog({
  target,
  open,
  onOpenChange,
}: {
  target: { messageId?: string; directMessageId?: string; userId?: string };
  open: boolean;
  onOpenChange: (o: boolean) => void;
}) {
  const [reason, setReason] = useState<(typeof REASONS)[number]["id"]>("SPAM");
  const [details, setDetails] = useState("");
  const [pending, start] = useTransition();

  return (
    <Dialog open={open} onOpenChange={(o) => !pending && onOpenChange(o)}>
      <DialogContent className="w-[calc(100vw-2rem)] max-w-md">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Flag className="h-4 w-4 text-destructive" /> Report {target.userId && !target.messageId ? "this student" : "this message"}
          </DialogTitle>
          <DialogDescription>
            Reports go to the Scholarly moderators, not to the person you report. Thank you for keeping the community safe.
          </DialogDescription>
        </DialogHeader>
        <div role="radiogroup" className="space-y-1.5">
          {REASONS.map((r) => (
            <button
              key={r.id}
              type="button"
              role="radio"
              aria-checked={reason === r.id}
              onClick={() => setReason(r.id)}
              className={cn(
                "flex w-full items-center gap-3 rounded-lg border px-3 py-2.5 text-left text-sm transition-colors",
                reason === r.id ? "border-primary bg-primary/[0.06]" : "border-border hover:bg-secondary/60",
              )}
            >
              <span className={cn("h-4 w-4 rounded-full border-2", reason === r.id ? "border-primary bg-primary shadow-[inset_0_0_0_2px_hsl(var(--background))]" : "border-muted-foreground/40")} />
              {r.label}
            </button>
          ))}
        </div>
        <Textarea
          value={details}
          onChange={(e) => setDetails(e.target.value)}
          maxLength={1000}
          placeholder="Anything the moderators should know (optional)"
          className="min-h-20"
        />
        <DialogFooter className="gap-2 sm:gap-0">
          <Button variant="outline" onClick={() => onOpenChange(false)} disabled={pending}>
            Cancel
          </Button>
          <Button
            variant="destructive"
            disabled={pending}
            onClick={() =>
              start(async () => {
                const r = await reportContent({ ...target, reason, details });
                if (!r.ok) return void toast.error(r.error);
                toast.success("Report sent. A moderator will review it.");
                onOpenChange(false);
              })
            }
          >
            {pending && <Loader2 className="h-4 w-4 animate-spin" />}
            Send report
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
