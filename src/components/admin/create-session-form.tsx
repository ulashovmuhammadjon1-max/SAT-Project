"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Trash2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createAdminSession, deleteAdminSession, saveHostDefaults } from "@/server/actions/admin/sessions";

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
export interface HostDefaults {
  meetingUrl: string;
  defaultSubject: string;
  defaultTitle: string;
}

export function CreateSessionForm({ defaults }: { defaults: HostDefaults }) {
  // Prefilled from this admin's saved details, and reset back to them after
  // each publish, so the usual subject and link never need retyping.
  const [title, setTitle] = useState(defaults.defaultTitle);
  const [subject, setSubject] = useState(defaults.defaultSubject);
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [meetingUrl, setMeetingUrl] = useState(defaults.meetingUrl);
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
      setTitle(defaults.defaultTitle);
      setSubject(defaults.defaultSubject);
      setDate("");
      setTime("");
      setMeetingUrl(defaults.meetingUrl || meetingUrl);
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

/**
 * This admin's saved details. Stored per admin, so each one keeps their own
 * Meet link; used to prefill the create form above.
 */
export function HostDefaultsForm({ defaults }: { defaults: HostDefaults }) {
  const router = useRouter();
  const [meetingUrl, setMeetingUrl] = useState(defaults.meetingUrl);
  const [defaultSubject, setDefaultSubject] = useState(defaults.defaultSubject);
  const [defaultTitle, setDefaultTitle] = useState(defaults.defaultTitle);
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    startTransition(async () => {
      const res = await saveHostDefaults({ meetingUrl, defaultSubject, defaultTitle });
      if (!res.ok) {
        setError(res.error);
        return;
      }
      toast.success("Saved. New sessions will start with these details.");
      router.refresh();
    });
  }

  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div className="space-y-1.5">
        <Label htmlFor="default-meet">Your Google Meet link</Label>
        <Input
          id="default-meet"
          type="url"
          inputMode="url"
          value={meetingUrl}
          onChange={(e) => setMeetingUrl(e.target.value)}
          placeholder="https://meet.google.com/abc-defg-hij"
        />
      </div>
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <Label htmlFor="default-subject">Subject you usually teach</Label>
          <Input
            id="default-subject"
            value={defaultSubject}
            onChange={(e) => setDefaultSubject(e.target.value)}
            placeholder="e.g. AP Biology"
            maxLength={80}
          />
        </div>
        <div className="space-y-1.5">
          <Label htmlFor="default-title">Usual session title</Label>
          <Input
            id="default-title"
            value={defaultTitle}
            onChange={(e) => setDefaultTitle(e.target.value)}
            placeholder="e.g. 1-on-1 AP Biology help"
            maxLength={120}
          />
        </div>
      </div>
      {error && (
        <p role="alert" className="rounded-lg bg-destructive/10 px-3 py-2 text-sm text-destructive">
          {error}
        </p>
      )}
      <Button type="submit" variant="outline" disabled={isPending}>
        {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
        Save my details
      </Button>
    </form>
  );
}
