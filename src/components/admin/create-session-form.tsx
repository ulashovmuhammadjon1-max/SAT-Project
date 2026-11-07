"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Pencil, Trash2 } from "lucide-react";
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
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  createAdminSession,
  deleteAdminSession,
  saveHostDefaults,
  updateAdminSession,
} from "@/server/actions/admin/sessions";

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

/** "YYYY-MM-DD" and "HH:MM" for an instant, in the admin's own timezone. */
function localParts(iso: string) {
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return {
    date: `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`,
    time: `${pad(d.getHours())}:${pad(d.getMinutes())}`,
  };
}

export interface EditableSession {
  id: string;
  title: string;
  subject: string;
  startsAt: string;
  meetingUrl: string;
  /** A student has requested or booked it, so its time is fixed. */
  booked: boolean;
}

/**
 * Edit a published session in a dialog. Title, subject and Meet link can
 * always change; the time is locked once a student has booked, and the server
 * enforces the same rule.
 */
export function EditSessionButton({ session }: { session: EditableSession }) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState(session.title);
  const [subject, setSubject] = useState(session.subject);
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [meetingUrl, setMeetingUrl] = useState(session.meetingUrl);
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  // Seeded on open, in the browser, so the date and time are in the admin's
  // own timezone rather than the server's.
  function onOpenChange(next: boolean) {
    if (next) {
      const parts = localParts(session.startsAt);
      setTitle(session.title);
      setSubject(session.subject);
      setDate(parts.date);
      setTime(parts.time);
      setMeetingUrl(session.meetingUrl);
      setError(null);
    }
    if (!isPending) setOpen(next);
  }

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
    // A booked session keeps its exact instant, whatever rounding the inputs did.
    const startsAt = session.booked ? session.startsAt : start.toISOString();
    startTransition(async () => {
      const res = await updateAdminSession(session.id, { title, subject, startsAt, meetingUrl });
      if (!res.ok) {
        setError(res.error);
        return;
      }
      toast.success(
        session.booked && meetingUrl !== session.meetingUrl
          ? "Session updated. The student's booking now has the new Meet link."
          : "Session updated.",
      );
      setOpen(false);
      router.refresh();
    });
  }

  return (
    <>
      <Button
        type="button"
        variant="outline"
        size="sm"
        onClick={() => onOpenChange(true)}
        aria-label={`Edit ${session.title || "session"}`}
      >
        <Pencil className="h-4 w-4" /> Edit
      </Button>
      <Dialog open={open} onOpenChange={onOpenChange}>
        <DialogContent className="max-h-[calc(100dvh-2rem)] w-[calc(100vw-2rem)] max-w-lg overflow-y-auto">
          <DialogHeader>
            <DialogTitle>Edit session</DialogTitle>
            <DialogDescription>
              {session.booked
                ? "A student has booked this session, so its date and time are fixed. You can still change the title, subject and Meet link."
                : "Changes show to students straight away."}
            </DialogDescription>
          </DialogHeader>
          <form onSubmit={onSubmit} className="space-y-4">
            <div className="space-y-1.5">
              <Label htmlFor={`edit-title-${session.id}`}>Title</Label>
              <Input
                id={`edit-title-${session.id}`}
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                maxLength={120}
                required
              />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor={`edit-subject-${session.id}`}>Subject you will teach</Label>
              <Input
                id={`edit-subject-${session.id}`}
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                maxLength={80}
                required
              />
            </div>
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="space-y-1.5">
                <Label htmlFor={`edit-date-${session.id}`}>Date</Label>
                <Input
                  id={`edit-date-${session.id}`}
                  type="date"
                  value={date}
                  min={session.booked ? undefined : todayLocal()}
                  onChange={(e) => setDate(e.target.value)}
                  disabled={session.booked}
                  required
                />
              </div>
              <div className="space-y-1.5">
                <Label htmlFor={`edit-time-${session.id}`}>Start time</Label>
                <Input
                  id={`edit-time-${session.id}`}
                  type="time"
                  step={900}
                  value={time}
                  onChange={(e) => setTime(e.target.value)}
                  disabled={session.booked}
                  required
                />
              </div>
            </div>
            <p className="-mt-2 text-xs text-muted-foreground">
              {start && end ? `${fmt(start)} – ${fmt(end)}, your local time (1 hour)` : "Every session is 1 hour."}
            </p>
            <div className="space-y-1.5">
              <Label htmlFor={`edit-meet-${session.id}`}>Google Meet link</Label>
              <Input
                id={`edit-meet-${session.id}`}
                type="url"
                inputMode="url"
                value={meetingUrl}
                onChange={(e) => setMeetingUrl(e.target.value)}
                placeholder="https://meet.google.com/abc-defg-hij"
                required
              />
              {session.booked && (
                <p className="text-xs text-muted-foreground">
                  A new link is copied to the student&apos;s booking automatically.
                </p>
              )}
            </div>
            {error && (
              <p role="alert" className="rounded-lg bg-destructive/10 px-3 py-2 text-sm text-destructive">
                {error}
              </p>
            )}
            <DialogFooter className="gap-2 sm:gap-0">
              <Button type="button" variant="outline" onClick={() => onOpenChange(false)} disabled={isPending}>
                Cancel
              </Button>
              <Button type="submit" disabled={isPending}>
                {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
                Save changes
              </Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>
    </>
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
