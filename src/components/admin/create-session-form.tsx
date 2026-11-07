"use client";

import { useState, useTransition } from "react";
import { Loader2, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createAdminSession, deleteAdminSession } from "@/server/actions/admin/sessions";

/** "YYYY-MM-DD" for today in the admin's own timezone, for the date picker's min. */
function todayLocal() {
  const d = new Date();
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

/**
 * Create a 1-on-1 session. Date and time are read in the admin's own timezone
 * by the browser and sent as an absolute instant, so students elsewhere see the
 * session at the right local time.
 */
export function CreateSessionForm() {
  const [title, setTitle] = useState("");
  const [subject, setSubject] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [meetingUrl, setMeetingUrl] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  const start = date && time ? new Date(`${date}T${time}`) : null;
  const valid = start && !Number.isNaN(start.getTime());
  const end = valid ? new Date(start.getTime() + 60 * 60_000) : null;
  const fmt = (d: Date) => d.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });

  function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    if (!valid) {
      setError("Pick a date and start time.");
      return;
    }
    startTransition(async () => {
      const res = await createAdminSession({ title, subject, startsAt: start.toISOString(), meetingUrl });
      if (!res.ok) {
        setError(res.error);
        return;
      }
      toast.success("Session published. Students can book it now.");
      setTitle("");
      setSubject("");
      setDate("");
      setTime("");
    });
  }

  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <Label htmlFor="session-title">Title</Label>
          <Input
            id="session-title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g. Writing a strong research question"
            maxLength={120}
            required
          />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="session-subject">Subject you will teach</Label>
          <Input
            id="session-subject"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
            placeholder="e.g. AP Biology, SAT Math, IELTS Writing"
            maxLength={80}
            required
          />
        </div>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <Label htmlFor="session-date">Date</Label>
          <Input
            id="session-date"
            type="date"
            value={date}
            min={todayLocal()}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="session-time">Start time</Label>
          <Input
            id="session-time"
            type="time"
            step={900}
            value={time}
            onChange={(e) => setTime(e.target.value)}
            required
          />
          <p className="text-xs text-muted-foreground">
            {start && end ? `${fmt(start)} – ${fmt(end)}, your local time (1 hour)` : "Every session is 1 hour, in your local time."}
          </p>
        </div>
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="session-meet">Google Meet link</Label>
        <Input
          id="session-meet"
          type="url"
          inputMode="url"
          value={meetingUrl}
          onChange={(e) => setMeetingUrl(e.target.value)}
          placeholder="https://meet.google.com/abc-defg-hij"
          required
        />
        <p className="text-xs text-muted-foreground">
          The student who books this session gets this link. You can reuse the same link for every session.
        </p>
      </div>

      {error && (
        <p role="alert" className="rounded-lg bg-destructive/10 px-3 py-2 text-sm text-destructive">
          {error}
        </p>
      )}

      <Button type="submit" disabled={isPending}>
        {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
        Publish session
      </Button>
    </form>
  );
}

export function DeleteSessionButton({ slotId }: { slotId: string }) {
  const [isPending, startTransition] = useTransition();
  return (
    <Button
      type="button"
      variant="ghost"
      size="sm"
      disabled={isPending}
      aria-label="Delete session"
      onClick={() => {
        if (!window.confirm("Delete this session?")) return;
        startTransition(async () => {
          const res = await deleteAdminSession(slotId);
          if (res.ok) toast.success("Session deleted.");
          else toast.error(res.error);
        });
      }}
    >
      {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Trash2 className="h-4 w-4" />}
    </Button>
  );
}
