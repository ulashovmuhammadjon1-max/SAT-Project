"use client";

import { useEffect, useMemo, useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { CalendarCheck, Check, Coins, Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { CoinAmount } from "@/components/student/coin-badge";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { cn } from "@/lib/utils";
import {
  createBooking,
  type BookingContext,
  type OpenSlot,
} from "@/server/actions/student/bookings";

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

export function BookingForm({
  slots,
  prefill,
  context,
}: {
  slots: OpenSlot[];
  prefill: BookingPrefill;
  context: BookingContext;
}) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  // Which community requirements the student has confirmed. Server-checked
  // again on submit — this only drives the button state.
  const [acked, setAcked] = useState<Set<string>>(new Set());
  const allAcked = context.requirements.every((r) => acked.has(r.id));

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
        acknowledgedRequirements: [...acked],
      });
      if (res.ok) {
        router.push(`/bookings?booked=${res.bookingId}`);
      } else {
        toast.error(res.error);
        // A lost race or a spent balance means what the page is showing is
        // stale, so refetch rather than leaving the student looking at numbers
        // that are no longer true.
        if (res.reason === "slot_gone" || res.reason === "insufficient_coins") {
          router.refresh();
        }
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

  // Not enough coins is a dead end unless we show the way out of it, so this
  // replaces the form entirely rather than letting them fill it in and fail.
  if (!context.canAfford) {
    return (
      <Card className="border-warning/40 bg-warning/5">
        <CardContent className="space-y-4 p-6">
          <div className="flex items-start gap-3">
            <Coins className="mt-0.5 h-5 w-5 shrink-0 text-warning" />
            <div>
              <p className="font-display text-lg font-semibold">Not enough coins yet</p>
              <p className="mt-1 text-sm text-muted-foreground">
                This session costs <strong className="text-foreground">{context.cost}</strong>{" "}
                coins and you have <strong className="text-foreground">{context.balance}</strong>.
                You need {context.shortfall} more.
              </p>
            </div>
          </div>
          <div className="rounded-lg border border-border bg-card p-4">
            <p className="text-sm font-medium">The fastest way to earn them</p>
            <p className="mt-1 text-sm text-muted-foreground">
              Invite a friend and get {context.referralRewardCoins} coins the moment they join —
              that&apos;s {Math.ceil(context.shortfall / Math.max(1, context.referralRewardCoins))}{" "}
              {Math.ceil(context.shortfall / Math.max(1, context.referralRewardCoins)) === 1
                ? "friend"
                : "friends"}{" "}
              away.
            </p>
            <Button asChild className="mt-3">
              <Link href="/invite">Invite friends</Link>
            </Button>
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <form onSubmit={submit} className="space-y-6">
      {/* Requirements. Deliberately worded as a confirmation, not a check —
          neither Instagram nor Telegram can be verified server-side for an
          arbitrary user, and claiming otherwise would be a lie in the UI. */}
      <section aria-labelledby="requirements">
        <h2 id="requirements" className="font-display text-lg font-semibold">
          1. Join the community
        </h2>
        <p className="mt-0.5 text-sm text-muted-foreground">
          SATForge stays free because the community grows. Please do both before booking.
        </p>
        <div className="mt-4 space-y-2">
          {context.requirements.map((r) => {
            const checked = acked.has(r.id);
            return (
              <label
                key={r.id}
                className={cn(
                  "flex cursor-pointer items-center gap-3 rounded-lg border p-3 transition-colors",
                  checked ? "border-primary/50 bg-primary/5" : "border-border hover:bg-secondary/50",
                )}
              >
                <input
                  type="checkbox"
                  checked={checked}
                  onChange={(e) => {
                    setAcked((prev) => {
                      const next = new Set(prev);
                      if (e.target.checked) next.add(r.id);
                      else next.delete(r.id);
                      return next;
                    });
                  }}
                  className="h-4 w-4 shrink-0 rounded border-input accent-primary"
                />
                <span className="min-w-0 flex-1 text-sm">
                  <span className="font-medium">{r.label}</span>{" "}
                  <a
                    href={r.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    onClick={(e) => e.stopPropagation()}
                    className="text-primary underline-offset-4 hover:underline"
                  >
                    {r.handle}
                  </a>
                </span>
              </label>
            );
          })}
        </div>
        {/* Stated plainly: the check is human and it happens after booking.
            A student who finds out only when their session is cancelled has
            been treated unfairly, so the consequence is on screen before they
            spend a coin. */}
        <div className="mt-3 rounded-lg border border-warning/40 bg-warning/5 p-3">
          <p className="text-xs text-muted-foreground">
            <strong className="text-foreground">Please note:</strong> your subscription will be
            checked by volunteers, and if there is no subscription your session will be cancelled.
            Your coins will be returned if that happens.
          </p>
        </div>
      </section>

      <section aria-labelledby="pick-time">
        <h2 id="pick-time" className="font-display text-lg font-semibold">
          2. Pick a time
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
            3. About you
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
        <CardContent className="space-y-4 p-5">
          {/* State the price and the resulting balance before they commit —
              never let a student discover the cost from the receipt. */}
          <dl className="grid gap-1.5 text-sm">
            <div className="flex items-center justify-between">
              <dt className="text-muted-foreground">Your balance</dt>
              <dd>
                <CoinAmount value={context.balance} size="sm" />
              </dd>
            </div>
            <div className="flex items-center justify-between">
              <dt className="text-muted-foreground">This session</dt>
              <dd className="text-destructive">
                <CoinAmount value={-context.cost} size="sm" />
              </dd>
            </div>
            <div className="flex items-center justify-between border-t border-border pt-1.5 font-medium">
              <dt>After booking</dt>
              <dd>
                <CoinAmount value={context.balance - context.cost} size="sm" />
              </dd>
            </div>
          </dl>

          {context.previousBookings > 0 && (
            <p className="text-xs text-muted-foreground">
              Your first session cost {context.cost - context.previousBookings * 5}. The price rises
              by 5 coins each time so the free sessions reach as many students as possible.
            </p>
          )}

          <div className="flex flex-wrap items-center justify-between gap-4">
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
            <Button type="submit" disabled={!slotId || !allAcked || isPending}>
              {isPending ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                <CalendarCheck className="h-4 w-4" />
              )}
              Confirm booking · {context.cost} coins
            </Button>
          </div>

          {!allAcked && (
            <p className="text-xs text-muted-foreground">
              Confirm the community steps above to enable booking.
            </p>
          )}

          {context.refundHours !== null && (
            <p className="text-xs text-muted-foreground">
              Cancel at least {context.refundHours} hours before and your coins come back.
            </p>
          )}
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
