"use client";

import { useEffect, useMemo, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { CalendarCheck, Check, Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { cn } from "@/lib/utils";
import { createBooking, type OpenSlot } from "@/server/actions/student/bookings";

export interface BookingPrefill {
  name: string;
  email: string;
  currentScore: number | null;
  targetScore: number | null;
  satDate: string | null;
  weakestArea: string | null;
}

/** Group slots by calendar day *in the viewer's timezone*. */
function groupByDay(slots: OpenSlot[]) {
  const map = new Map<string, OpenSlot[]>();
  for (const s of slots) {
    const key = new Date(s.startsAt).toLocaleDateString(undefined, {
      weekday: "short",
      month: "short",
      day: "numeric",
    });
    if (!map.has(key)) map.set(key, []);
    map.get(key)!.push(s);
  }
  return [...map.entries()];
}

export function BookingForm({ slots, prefill }: { slots: OpenSlot[]; prefill: BookingPrefill }) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  const [slotId, setSlotId] = useState<string | null>(null);
  const [name, setName] = useState(prefill.name);
  const [email, setEmail] = useState(prefill.email);
  const [currentScore, setCurrentScore] = useState(prefill.currentScore?.toString() ?? "");
  const [targetScore, setTargetScore] = useState(prefill.targetScore?.toString() ?? "");
  const [satDate, setSatDate] = useState(prefill.satDate ?? "");
  const [hours, setHours] = useState("");
  const [weakest, setWeakest] = useState(prefill.weakestArea ?? "");
  const [notes, setNotes] = useState("");

  // Day grouping and time labels depend on the viewer's timezone, which the
  // server doesn't share — so hold them back until after mount rather than
  // render times that would hydrate-mismatch (and briefly show the wrong hour).
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  const days = useMemo(() => (mounted ? groupByDay(slots) : []), [slots, mounted]);
  const timezone = useLocalTimezone();
  const selected = slots.find((s) => s.id === slotId);

  function submit(e: React.FormEvent) {
    e.preventDefault();
    if (!slotId) {
      toast.error("Please choose a time slot.");
      return;
    }
    startTransition(async () => {
      const res = await createBooking({
        slotId,
        name,
        email,
        currentScore: currentScore ? parseInt(currentScore, 10) : null,
        targetScore: targetScore ? parseInt(targetScore, 10) : null,
        satDate: satDate || null,
        studyHoursPerWeek: hours ? parseInt(hours, 10) : null,
        weakestArea: weakest || null,
        notes: notes || null,
        timezone,
      });
      if (res.ok) {
        router.push(`/bookings?booked=${res.bookingId}`);
      } else {
        toast.error(res.error);
        // A lost race means the slot list is stale — refresh it.
        router.refresh();
      }
    });
  }

  if (slots.length === 0) {
    return (
      <Card>
        <CardContent className="p-6">
          <p className="font-medium">No times are open right now.</p>
          <p className="mt-1 text-sm text-muted-foreground">
            New sessions are released regularly — check back soon.
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <form onSubmit={submit} className="space-y-6">
      <section aria-labelledby="pick-time">
        <h2 id="pick-time" className="font-display text-lg font-semibold">
          1. Pick a time
        </h2>
        <p className="mt-0.5 text-sm text-muted-foreground">
          Times shown in your local timezone{timezone && ` (${timezone})`}.
        </p>

        <div className="mt-4 space-y-4">
          {!mounted && <p className="text-sm text-muted-foreground">Loading times…</p>}
          {days.map(([day, daySlots]) => (
            <div key={day}>
              <p className="text-sm font-medium">{day}</p>
              <div className="mt-2 flex flex-wrap gap-2">
                {daySlots.map((s) => {
                  const active = slotId === s.id;
                  return (
                    <button
                      key={s.id}
                      type="button"
                      onClick={() => setSlotId(s.id)}
                      aria-pressed={active}
                      className={cn(
                        "rounded-lg border px-3 py-2 text-sm tabular-nums transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
                        active
                          ? "border-primary bg-primary/10 font-medium text-primary"
                          : "border-border hover:bg-secondary"
                      )}
                    >
                      {new Date(s.startsAt).toLocaleTimeString(undefined, {
                        hour: "numeric",
                        minute: "2-digit",
                      })}
                      <span className="ml-1.5 text-xs text-muted-foreground">{s.durationMinutes}m</span>
                    </button>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section aria-labelledby="about-you" className="space-y-4">
        <div>
          <h2 id="about-you" className="font-display text-lg font-semibold">
            2. About you
          </h2>
          <p className="mt-0.5 text-sm text-muted-foreground">
            Prefilled from your profile where we already know the answer.
          </p>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          <Field id="name" label="Name" required>
            <Input id="name" value={name} onChange={(e) => setName(e.target.value)} required />
          </Field>
          <Field id="email" label="Email" required>
            <Input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </Field>
          <Field id="currentScore" label="Current SAT score" hint="Optional">
            <Input
              id="currentScore"
              type="number"
              min={400}
              max={1600}
              value={currentScore}
              onChange={(e) => setCurrentScore(e.target.value)}
            />
          </Field>
          <Field id="targetScore" label="Target SAT score" hint="Optional">
            <Input
              id="targetScore"
              type="number"
              min={400}
              max={1600}
              value={targetScore}
              onChange={(e) => setTargetScore(e.target.value)}
            />
          </Field>
          <Field id="satDate" label="Upcoming test date" hint="Optional">
            <Input
              id="satDate"
              type="date"
              value={satDate}
              onChange={(e) => setSatDate(e.target.value)}
            />
          </Field>
          <Field id="hours" label="Study hours per week" hint="Optional">
            <Input
              id="hours"
              type="number"
              min={0}
              max={80}
              value={hours}
              onChange={(e) => setHours(e.target.value)}
            />
          </Field>
        </div>

        <Field id="weakest" label="Biggest SAT weakness" hint="Optional">
          <Input
            id="weakest"
            value={weakest}
            onChange={(e) => setWeakest(e.target.value)}
            placeholder="e.g. running out of time on Reading"
          />
        </Field>

        <Field id="notes" label="Anything else you'd like to discuss?" hint="Optional">
          <Textarea
            id="notes"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            rows={3}
          />
        </Field>
      </section>

      <Card>
        <CardContent className="flex flex-wrap items-center justify-between gap-4 p-5">
          <p className="text-sm" aria-live="polite">
            {selected ? (
              <>
                <Check className="mr-1 inline h-4 w-4 text-success" />
                <LocalTime iso={new Date(selected.startsAt).toISOString()} format="full" /> ·{" "}
                {selected.durationMinutes} minutes
              </>
            ) : (
              <span className="text-muted-foreground">Choose a time to continue.</span>
            )}
          </p>
          <Button type="submit" disabled={!slotId || isPending}>
            {isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : <CalendarCheck className="h-4 w-4" />}
            Confirm booking
          </Button>
        </CardContent>
      </Card>
    </form>
  );
}

function Field({
  id,
  label,
  hint,
  required,
  children,
}: {
  id: string;
  label: string;
  hint?: string;
  required?: boolean;
  children: React.ReactNode;
}) {
  return (
    <div className="space-y-1.5">
      <Label htmlFor={id}>
        {label}
        {required && <span className="ml-0.5 text-destructive">*</span>}
        {hint && <span className="ml-2 text-xs font-normal text-muted-foreground">{hint}</span>}
      </Label>
      {children}
    </div>
  );
}
