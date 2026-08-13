"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Ban, Check, Loader2, Plus, RefreshCw, RotateCcw, Trash2, Undo2, UserMinus, X } from "lucide-react";
import { toast } from "sonner";

import type { BookingStatus } from "@prisma/client";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { BOOKING_STATUS_LABELS, BOOKING_STATUS_TONE } from "@/lib/booking/status";
import { cn } from "@/lib/utils";
import {
  createSlots,
  decideBooking,
  deleteSlot,
  recheckStudentTelegram,
  setBookingStatus,
  setStudentTelegramVerified,
  setSlotBlocked,
  type BookingDecision,
} from "@/server/actions/admin/bookings";

export interface AdminSlotRow {
  id: string;
  startsAt: string;
  durationMinutes: number;
  isBlocked: boolean;
  booking: {
    id: string;
    status: BookingStatus;
    statusReason: string | null;
    name: string;
    email: string;
    currentScore: number | null;
    targetScore: number | null;
    satDate: string | null;
    studyHoursPerWeek: number | null;
    weakestArea: string | null;
    notes: string | null;
    timezone: string | null;
    telegram: {
      linked: boolean;
      username: string | null;
      isMember: boolean;
      checkedAt: string | null;
      manual: boolean;
    } | null;
  } | null;
}

export function SlotCreator() {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [dates, setDates] = useState<string[]>([""]);
  const [times, setTimes] = useState<string[]>(["16:00"]);
  const [duration, setDuration] = useState("30");
  const tz = useLocalTimezone();

  function submit(e: React.FormEvent) {
    e.preventDefault();
    const cleanDates = dates.filter(Boolean);
    const cleanTimes = times.filter(Boolean);
    if (!cleanDates.length || !cleanTimes.length) {
      toast.error("Add at least one date and one time.");
      return;
    }
    startTransition(async () => {
      const res = await createSlots({
        dates: cleanDates,
        times: cleanTimes,
        durationMinutes: parseInt(duration, 10) || 30,
        tzOffsetMinutes: new Date().getTimezoneOffset(),
      });
      if (res.ok) {
        toast.success(`${res.created ?? 0} slot(s) published.`);
        setDates([""]);
        router.refresh();
      } else {
        toast.error(res.error ?? "Couldn't create slots.");
      }
    });
  }

  return (
    <Card>
      <CardContent className="p-5">
        <h2 className="font-display font-semibold">Publish availability</h2>
        <p className="mt-0.5 text-sm text-muted-foreground">
          Every selected date is combined with every selected time. Entered in your own timezone
          {tz && ` (${tz})`}.
        </p>

        <form onSubmit={submit} className="mt-4 space-y-4">
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-2">
              <Label>Dates</Label>
              {dates.map((d, i) => (
                <Input
                  key={i}
                  type="date"
                  value={d}
                  aria-label={`Date ${i + 1}`}
                  onChange={(e) => setDates((cur) => cur.map((x, j) => (j === i ? e.target.value : x)))}
                />
              ))}
              <Button type="button" variant="outline" size="sm" onClick={() => setDates((c) => [...c, ""])}>
                <Plus className="h-3.5 w-3.5" /> Add date
              </Button>
            </div>

            <div className="space-y-2">
              <Label>Times</Label>
              {times.map((t, i) => (
                <Input
                  key={i}
                  type="time"
                  value={t}
                  aria-label={`Time ${i + 1}`}
                  onChange={(e) => setTimes((cur) => cur.map((x, j) => (j === i ? e.target.value : x)))}
                />
              ))}
              <Button type="button" variant="outline" size="sm" onClick={() => setTimes((c) => [...c, "17:00"])}>
                <Plus className="h-3.5 w-3.5" /> Add time
              </Button>
            </div>
          </div>

          <div className="flex flex-wrap items-end gap-3">
            <div className="space-y-1.5">
              <Label htmlFor="dur">Duration (minutes)</Label>
              <Input
                id="dur"
                type="number"
                min={10}
                max={180}
                value={duration}
                onChange={(e) => setDuration(e.target.value)}
                className="w-32"
              />
            </div>
            <Button type="submit" disabled={isPending}>
              {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
              Publish slots
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
}

/** Which booking the reason dialog is open for, and what it will do. */
interface DecisionTarget {
  bookingId: string;
  slotId: string;
  decision: BookingDecision;
  who: string;
}

const DECISION_COPY: Record<
  BookingDecision,
  { title: string; verb: string; done: string; reasonRequired: boolean; hint: string }
> = {
  APPROVE: {
    title: "Approve this session",
    verb: "Approve",
    done: "Approved — the student has been emailed.",
    reasonRequired: false,
    hint: "Optional. Anything you add here goes into the approval email.",
  },
  REJECT: {
    title: "Decline this request",
    verb: "Decline",
    done: "Declined — the student has been emailed and their coins returned.",
    reasonRequired: true,
    hint: "Required. The student sees this, so say what went wrong and what they can do instead.",
  },
  REVOKE: {
    title: "Send this session back for review",
    verb: "Un-approve",
    done: "Sent back for review — the student has been emailed what to fix.",
    reasonRequired: true,
    hint: "Required. Say which step is missing. The slot and the coins stay held, so the student can fix it and be approved again.",
  },
  REMOVE: {
    title: "Remove this student from the slot",
    verb: "Remove from slot",
    done: "Removed — the slot is open again.",
    reasonRequired: true,
    hint: "Required. The student is emailed this. The slot reopens immediately so someone else can book it. A session that already happened is not refunded; anything else is.",
  },
  CANCEL: {
    title: "Cancel this approved session",
    verb: "Cancel session",
    done: "Cancelled — the student has been emailed and their coins returned.",
    reasonRequired: true,
    hint: "Required. This session was already confirmed, so tell the student why it is being called off.",
  },
};

export function SlotTable({ slots }: { slots: AdminSlotRow[] }) {
  const router = useRouter();
  const [deciding, setDeciding] = useState<DecisionTarget | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [, startTransition] = useTransition();

  function run(id: string, fn: () => Promise<{ ok: boolean; error?: string }>, okMsg: string) {
    setBusy(id);
    startTransition(async () => {
      const res = await fn();
      setBusy(null);
      if (res.ok) {
        toast.success(okMsg);
        router.refresh();
      } else {
        toast.error(res.error ?? "Something went wrong.");
      }
    });
  }

  if (slots.length === 0) {
    return (
      <Card>
        <CardContent className="p-8 text-center text-sm text-muted-foreground">
          No slots published yet.
        </CardContent>
      </Card>
    );
  }

  return (
    <>
      {deciding && (
        <DecisionDialog
          target={deciding}
          busy={busy === deciding.slotId}
          onClose={() => setDeciding(null)}
          onConfirm={(reason) => {
            const copy = DECISION_COPY[deciding.decision];
            const { bookingId, decision, slotId } = deciding;
            setDeciding(null);
            run(slotId, () => decideBooking({ bookingId, decision, reason }), copy.done);
          }}
        />
      )}
    <ul className="space-y-2">
      {slots.map((s) => {
        const b = s.booking;
        // A rejected booking releases the slot exactly like a cancelled one, so
        // the slot reads as Open again and can be blocked, deleted or rebooked.
        const taken = b && b.status !== "CANCELLED" && b.status !== "REJECTED";
        return (
          <li key={s.id}>
            <Card className={cn(s.isBlocked && "opacity-60")}>
              <CardContent className="space-y-3 p-4">
                <div className="flex flex-wrap items-center gap-x-3 gap-y-2">
                  <span className="font-medium tabular-nums">
                    <LocalTime iso={s.startsAt} format="dateShort" />
                  </span>
                  <span className="text-xs text-muted-foreground">{s.durationMinutes}m</span>

                  {s.isBlocked ? (
                    <Badge variant="secondary">Blocked</Badge>
                  ) : taken ? (
                    <Badge variant={BOOKING_STATUS_TONE[b!.status]}>{BOOKING_STATUS_LABELS[b!.status]}</Badge>
                  ) : (
                    <Badge variant="outline">Open</Badge>
                  )}

                  <div className="ml-auto flex flex-wrap gap-2">
                    {taken && b!.status === "PENDING" && (
                      <Button size="sm" disabled={busy === s.id} onClick={() => setDeciding({ bookingId: b!.id, slotId: s.id, decision: "APPROVE", who: b!.name })}>
                        <Check className="h-3.5 w-3.5" /> Approve
                      </Button>
                    )}
                    {taken && b!.status === "PENDING" && (
                      <Button size="sm" variant="outline" disabled={busy === s.id} onClick={() => setDeciding({ bookingId: b!.id, slotId: s.id, decision: "REJECT", who: b!.name })}>
                        <X className="h-3.5 w-3.5" /> Decline
                      </Button>
                    )}
                    {taken && b!.status === "UPCOMING" && (
                      <Button
                        size="sm"
                        variant="outline"
                        disabled={busy === s.id}
                        onClick={() => run(s.id, () => setBookingStatus(b!.id, "COMPLETED"), "Marked completed.")}
                      >
                        <Check className="h-3.5 w-3.5" /> Complete
                      </Button>
                    )}
                    {taken && b!.status === "UPCOMING" && (
                      <Button size="sm" variant="outline" disabled={busy === s.id} onClick={() => setDeciding({ bookingId: b!.id, slotId: s.id, decision: "REVOKE", who: b!.name })}>
                        <RotateCcw className="h-3.5 w-3.5" /> Un-approve
                      </Button>
                    )}
                    {taken && b!.status === "UPCOMING" && (
                      <Button size="sm" variant="outline" disabled={busy === s.id} onClick={() => setDeciding({ bookingId: b!.id, slotId: s.id, decision: "CANCEL", who: b!.name })}>
                        Cancel booking
                      </Button>
                    )}
                    {taken && (
                      <Button
                        size="sm"
                        variant="ghost"
                        className="text-destructive hover:text-destructive"
                        disabled={busy === s.id}
                        onClick={() => setDeciding({ bookingId: b!.id, slotId: s.id, decision: "REMOVE", who: b!.name })}
                      >
                        <UserMinus className="h-3.5 w-3.5" /> Free the slot
                      </Button>
                    )}
                    {!taken && (
                      <>
                        <Button
                          size="sm"
                          variant="outline"
                          disabled={busy === s.id}
                          onClick={() => run(s.id, () => setSlotBlocked(s.id, !s.isBlocked), s.isBlocked ? "Slot reopened." : "Slot blocked.")}
                        >
                          {s.isBlocked ? <Undo2 className="h-3.5 w-3.5" /> : <Ban className="h-3.5 w-3.5" />}
                          {s.isBlocked ? "Unblock" : "Block"}
                        </Button>
                        <Button
                          size="sm"
                          variant="ghost"
                          disabled={busy === s.id}
                          onClick={() => run(s.id, () => deleteSlot(s.id), "Slot deleted.")}
                        >
                          <Trash2 className="h-3.5 w-3.5" />
                        </Button>
                      </>
                    )}
                  </div>
                </div>

                {taken && (
                  <div className="rounded-lg border border-border/70 bg-secondary/30 p-3 text-sm">
                    <p className="font-medium">
                      {s.booking!.name}{" "}
                      <a href={`mailto:${s.booking!.email}`} className="font-normal text-primary hover:underline">
                        {s.booking!.email}
                      </a>
                    </p>
                    {b!.telegram && (
                      <TelegramStatus
                        t={b!.telegram}
                        busy={busy === s.id}
                        onSet={(isMember) =>
                          run(
                            s.id,
                            () => setStudentTelegramVerified({ bookingId: b!.id, isMember }),
                            isMember ? "Marked as subscribed." : "Marked as not subscribed.",
                          )
                        }
                        onRecheck={() =>
                          run(s.id, () => recheckStudentTelegram(b!.id), "Re-checked with Telegram.")
                        }
                      />
                    )}
                    <dl className="mt-2 grid gap-x-6 gap-y-1 text-xs sm:grid-cols-2">
                      <Detail label="Current score" value={s.booking!.currentScore} />
                      <Detail label="Target score" value={s.booking!.targetScore} />
                      <Detail
                        label="Test date"
                        // Date-only value: show the calendar date the student
                        // picked, not a timezone-shifted version of it.
                        value={s.booking!.satDate ? s.booking!.satDate.slice(0, 10) : null}
                      />
                      <Detail label="Study hrs/week" value={s.booking!.studyHoursPerWeek} />
                      <Detail label="Timezone" value={s.booking!.timezone} />
                      <Detail label="Weakest area" value={s.booking!.weakestArea} />
                    </dl>
                    {s.booking!.notes && (
                      <p className="mt-2 text-xs">
                        <span className="text-muted-foreground">Notes: </span>
                        {s.booking!.notes}
                      </p>
                    )}
                  </div>
                )}
              </CardContent>
            </Card>
          </li>
        );
      })}
    </ul>
    </>
  );
}

/**
 * The reason box.
 *
 * A modal rather than an inline field because a decline or a cancellation is
 * irreversible from the admin's side and sends mail to a student the moment it
 * lands — it deserves a deliberate confirm, not a button that fires on the
 * first click. Approving goes through the same dialog so the admin can attach a
 * note, but leaves the reason optional.
 */
function DecisionDialog({
  target,
  busy,
  onClose,
  onConfirm,
}: {
  target: DecisionTarget;
  busy: boolean;
  onClose: () => void;
  onConfirm: (reason: string) => void;
}) {
  const copy = DECISION_COPY[target.decision];
  const [reason, setReason] = useState("");
  const blocked = copy.reasonRequired && !reason.trim();

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      role="dialog"
      aria-modal="true"
      aria-label={copy.title}
      onClick={onClose}
    >
      <Card className="w-full max-w-lg" onClick={(e) => e.stopPropagation()}>
        <CardContent className="space-y-4 p-6">
          <div>
            <h2 className="font-display text-lg font-semibold">{copy.title}</h2>
            <p className="mt-0.5 text-sm text-muted-foreground">
              {target.who} will be emailed straight away.
            </p>
          </div>

          <div className="space-y-1.5">
            <Label htmlFor="decision-reason">
              Reason {copy.reasonRequired ? "" : <span className="text-muted-foreground">(optional)</span>}
            </Label>
            <Textarea
              id="decision-reason"
              rows={4}
              value={reason}
              autoFocus
              placeholder={
                target.decision === "REMOVE"
                  ? "e.g. You did not attend and did not let us know, so the slot is going back to the queue."
                  : target.decision === "REJECT"
                  ? "e.g. That slot is reserved for students sitting the March test — please pick a time in April."
                  : target.decision === "REVOKE"
                    ? "e.g. We could not find you following @satforge_org on Instagram. Follow the account and reply, and we will approve this again."
                    : target.decision === "CANCEL"
                      ? "e.g. Your mentor is ill. Please rebook any open slot and we will prioritise you."
                      : "e.g. Bring your last practice test score to the session."
              }
              onChange={(e) => setReason(e.target.value)}
            />
            <p className="text-xs text-muted-foreground">{copy.hint}</p>
          </div>

          <div className="flex justify-end gap-2">
            <Button variant="ghost" onClick={onClose} disabled={busy}>
              Never mind
            </Button>
            <Button
              variant={target.decision === "APPROVE" ? "default" : "destructive"}
              disabled={blocked || busy}
              onClick={() => onConfirm(reason)}
            >
              {busy && <Loader2 className="h-4 w-4 animate-spin" />}
              {copy.verb}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

/**
 * Whether this student is really in the Telegram channel.
 *
 * Shown from the cached result of the last real `getChatMember` call rather
 * than from what they ticked at booking time — the tick is what could not be
 * trusted. "Not connected" is its own state and is not the same as "not a
 * member": it means the student never signed in through Telegram, so nothing
 * has been checked either way.
 */
function TelegramStatus({
  t,
  busy,
  onSet,
  onRecheck,
}: {
  t: {
    linked: boolean;
    username: string | null;
    isMember: boolean;
    checkedAt: string | null;
    manual: boolean;
  };
  busy: boolean;
  onSet: (isMember: boolean) => void;
  onRecheck: () => void;
}) {
  const tone = !t.linked
    ? "border-border bg-secondary/40 text-muted-foreground"
    : t.isMember
      ? "border-emerald-500/40 bg-emerald-500/10 text-emerald-600 dark:text-emerald-400"
      : "border-destructive/40 bg-destructive/10 text-destructive";
  const text = !t.linked
    ? "Telegram not connected — unverified"
    : t.isMember
      ? `In the Telegram channel${t.username ? ` (@${t.username})` : ""}`
      : `NOT in the Telegram channel${t.username ? ` (@${t.username})` : ""}`;

  return (
    <div className={cn("mt-2 flex items-center gap-2 rounded-md border px-2.5 py-1.5 text-xs", tone)}>
      {t.linked && t.isMember ? (
        <Check className="h-3.5 w-3.5 shrink-0" />
      ) : (
        <X className="h-3.5 w-3.5 shrink-0" />
      )}
      <span className="font-medium">{text}</span>
      {t.checkedAt && (
        <span className="opacity-70">
          {t.manual ? "set by hand" : "checked"} <LocalTime iso={t.checkedAt} format="dateShort" />
        </span>
      )}

      {/* Manual override. The automatic check only exists once a bot token is
          configured and the student has signed in, and Instagram can never be
          checked at all — so the admin is the verifier and needs a place to
          record what they found. */}
      <span className="ml-auto flex shrink-0 gap-1">
        {t.isMember ? (
          <Button size="sm" variant="ghost" className="h-6 px-2 text-xs" disabled={busy} onClick={() => onSet(false)}>
            Mark unverified
          </Button>
        ) : (
          <Button size="sm" variant="ghost" className="h-6 px-2 text-xs" disabled={busy} onClick={() => onSet(true)}>
            Mark verified
          </Button>
        )}
        {t.linked && (
          <Button
            size="sm"
            variant="ghost"
            className="h-6 px-2 text-xs"
            disabled={busy}
            onClick={onRecheck}
            title="Ask Telegram again"
          >
            <RefreshCw className="h-3 w-3" />
          </Button>
        )}
      </span>
    </div>
  );
}

function Detail({ label, value }: { label: string; value: string | number | null }) {
  if (value === null || value === undefined || value === "") return null;
  return (
    <div className="flex gap-1.5">
      <dt className="text-muted-foreground">{label}:</dt>
      <dd className="font-medium">{value}</dd>
    </div>
  );
}
