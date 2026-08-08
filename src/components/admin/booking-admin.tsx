"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Ban, Check, Loader2, Plus, Trash2, Undo2 } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { cn } from "@/lib/utils";
import {
  createSlots,
  deleteSlot,
  setBookingStatus,
  setSlotBlocked,
} from "@/server/actions/admin/bookings";

export interface AdminSlotRow {
  id: string;
  startsAt: string;
  durationMinutes: number;
  isBlocked: boolean;
  booking: {
    id: string;
    status: "UPCOMING" | "COMPLETED" | "CANCELLED";
    name: string;
    email: string;
    currentScore: number | null;
    targetScore: number | null;
    satDate: string | null;
    studyHoursPerWeek: number | null;
    weakestArea: string | null;
    notes: string | null;
    timezone: string | null;
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

export function SlotTable({ slots }: { slots: AdminSlotRow[] }) {
  const router = useRouter();
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
    <ul className="space-y-2">
      {slots.map((s) => {
        const taken = s.booking && s.booking.status !== "CANCELLED";
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
                    <Badge variant={s.booking!.status === "COMPLETED" ? "success" : "default"}>
                      {s.booking!.status[0] + s.booking!.status.slice(1).toLowerCase()}
                    </Badge>
                  ) : (
                    <Badge variant="outline">Open</Badge>
                  )}

                  <div className="ml-auto flex flex-wrap gap-2">
                    {taken && s.booking!.status === "UPCOMING" && (
                      <Button
                        size="sm"
                        variant="outline"
                        disabled={busy === s.id}
                        onClick={() => run(s.id, () => setBookingStatus(s.booking!.id, "COMPLETED"), "Marked completed.")}
                      >
                        <Check className="h-3.5 w-3.5" /> Complete
                      </Button>
                    )}
                    {taken && s.booking!.status === "UPCOMING" && (
                      <Button
                        size="sm"
                        variant="outline"
                        disabled={busy === s.id}
                        onClick={() => run(s.id, () => setBookingStatus(s.booking!.id, "CANCELLED"), "Booking cancelled.")}
                      >
                        Cancel booking
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
