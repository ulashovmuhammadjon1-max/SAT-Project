"use client";

import {
  AtSign,
  AlertTriangle,
  CheckCircle2,
  CornerDownRight,
  Heart,
  Mail,
  Megaphone,
  MessageCircleQuestion,
  MessagesSquare,
  type LucideIcon,
} from "lucide-react";

import type { NotificationView } from "@/lib/community/types";
import { cn } from "@/lib/utils";
import { MemberAvatar, relativeTime } from "@/components/community/bits";

const META: Record<NotificationView["type"], { icon: LucideIcon; tone: string; label: string }> = {
  REPLY: { icon: CornerDownRight, tone: "bg-primary text-primary-foreground", label: "Reply" },
  MENTION: { icon: AtSign, tone: "bg-[hsl(262_70%_60%)] text-white", label: "Mention" },
  THREAD_REPLY: { icon: MessagesSquare, tone: "bg-secondary text-foreground", label: "Discussion" },
  ANSWER: { icon: MessageCircleQuestion, tone: "bg-warning text-warning-foreground", label: "Answer" },
  ANSWER_ACCEPTED: { icon: CheckCircle2, tone: "bg-success text-success-foreground", label: "Accepted" },
  REACTION: { icon: Heart, tone: "bg-destructive/90 text-destructive-foreground", label: "Reaction" },
  ANNOUNCEMENT: { icon: Megaphone, tone: "bg-foreground text-background", label: "Announcement" },
  DIRECT_MESSAGE: { icon: Mail, tone: "bg-primary text-primary-foreground", label: "Message" },
  MODERATION: { icon: AlertTriangle, tone: "bg-warning text-warning-foreground", label: "Moderation" },
};

export function NotificationItem({
  n,
  onOpen,
  dense,
}: {
  n: NotificationView;
  onOpen: (n: NotificationView) => void;
  dense?: boolean;
}) {
  const meta = META[n.type] ?? META.REPLY;
  const Icon = meta.icon;
  return (
    <button
      type="button"
      onClick={() => onOpen(n)}
      className={cn(
        "group relative flex w-full items-start gap-3 rounded-xl px-3 text-left transition-colors hover:bg-secondary/70 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        dense ? "py-2.5" : "py-3.5",
        !n.read && "bg-primary/[0.06]",
      )}
    >
      <span className="relative mt-0.5">
        {n.actor ? (
          <MemberAvatar id={n.actor.name} name={n.actor.name} image={n.actor.image} size={dense ? 36 : 40} />
        ) : (
          <span className={cn("flex items-center justify-center rounded-full", meta.tone)} style={{ width: dense ? 36 : 40, height: dense ? 36 : 40 }}>
            <Icon className="h-4 w-4" />
          </span>
        )}
        {n.actor && (
          <span className={cn("absolute -bottom-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full ring-2 ring-popover", meta.tone)}>
            <Icon className="h-3 w-3" />
          </span>
        )}
      </span>
      <span className="min-w-0 flex-1">
        <span className={cn("block text-sm leading-snug", n.read ? "text-foreground/80" : "font-semibold text-foreground")}>
          {n.title}
        </span>
        {n.body && <span className="mt-0.5 line-clamp-2 block text-[13px] leading-snug text-muted-foreground">{n.body}</span>}
        <span className="mt-1 block text-[11px] font-medium uppercase tracking-wide text-muted-foreground/80">
          {meta.label} · {relativeTime(n.createdAt)}
        </span>
      </span>
      {!n.read && <span className="mt-2 h-2.5 w-2.5 shrink-0 rounded-full bg-primary" aria-label="Unread" />}
    </button>
  );
}
