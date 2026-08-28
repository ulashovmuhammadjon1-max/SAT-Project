"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { CalendarPlus, Loader2, Trash2, Users } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/components/ui/select";
import type { MentorSlotRow } from "@/server/actions/student/peer-mentor";
import { createMentorSlot, deleteMentorSlot } from "@/server/actions/student/peer-mentor";

/**
 * The approved mentor's slot manager: publish times, see who booked, retire
 * empty slots. Times are entered in the mentor's local timezone (the
 * datetime-local input) and stored as UTC instants server-side.
 */
export function MentorStudio({ slots }: { slots: MentorSlotRow[] }) {
  const router = useRouter();
  const [pending, start] = useTransition();
  const [when, setWhen] = useState("");
  const [duration, setDuration] = useState<"30" | "60">("30");

  function publish() {
    if (!when) {
      toast.error("Pick a date and time first.");
      return;
    }
    start(async () => {
      const res = await createMentorSlot({
        startsAt: new Date(when),
        durationMinutes: Number(duration),
      });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Slot published — students can book it now.");
      setWhen("");
      router.refresh();
    });
  }

  function remove(slotId: string) {
    start(async () => {
      const res = await deleteMentorSlot(slotId);
      if (res.error) {
        toast.error(res.error);
        return;
      }
      toast.success("Slot removed.");
      router.refresh();
    });
  }

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end gap-3">
        <div className="space-y-1.5">
          <Label htmlFor="slot-when">New slot</Label>
          <Input
            id="slot-when"
            type="datetime-local"
            value={when}
            onChange={(e) => setWhen(e.target.value)}
            className="w-[220px]"
          />
        </div>
        <div className="space-y-1.5">
          <Label>Duration</Label>
          <Select value={duration} onValueChange={(v) => setDuration(v as "30" | "60")}>
            <SelectTrigger className="w-[130px]">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="30">30 minutes</SelectItem>
              <SelectItem value="60">60 minutes</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <Button onClick={publish} disabled={pending} className="gap-2">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <CalendarPlus className="h-4 w-4" />}
          Publish slot
        </Button>
      </div>

      {slots.length === 0 ? (
        <p className="rounded-xl border border-dashed border-border px-4 py-8 text-center text-sm text-muted-foreground">
          No upcoming slots yet — publish your first one above and it appears on the booking page
          with your name on it.
        </p>
      ) : (
        <ul className="divide-y divide-border">
          {slots.map((s) => (
            <li key={s.id} className="flex flex-wrap items-center gap-3 py-3">
              <div className="min-w-[200px] flex-1">
                <p className="text-sm font-medium tabular-nums">
                  {s.startsAt.toLocaleString(undefined, {
                    weekday: "short",
                    month: "short",
                    day: "numeric",
                    hour: "numeric",
                    minute: "2-digit",
                  })}
                  <span className="ml-2 text-xs text-muted-foreground">{s.durationMinutes}m</span>
                </p>
                {s.booked > 0 && (
                  <p className="mt-0.5 flex items-center gap-1 text-xs text-success">
                    <Users className="h-3 w-3" /> Booked by {s.studentNames.join(", ")}
                  </p>
                )}
              </div>
              {s.booked === 0 && (
                <Button
                  size="sm"
                  variant="ghost"
                  disabled={pending}
                  onClick={() => remove(s.id)}
                  className="text-destructive hover:text-destructive"
                >
                  <Trash2 className="h-4 w-4" />
                </Button>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
