"use client";

import { useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { CalendarDays, Check, Loader2, Users, Video } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { CoinAmount } from "@/components/student/coin-badge";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { cn } from "@/lib/utils";
import { createBooking } from "@/server/actions/student/bookings";
import { cancelEventRegistration, type EventListItem } from "@/server/actions/student/events";
import type { CommunityRequirement } from "@/lib/community";

/**
 * One event, with registration inline.
 *
 * The community checklist appears only after "Register" is pressed, rather than
 * repeated above every card — on a page with eight events that would be eight
 * copies of the same two checkboxes.
 */
export function EventCard({
  event,
  cost,
  balance,
  requirements,
  refundHours,
  prefill,
}: {
  event: EventListItem;
  cost: number;
  balance: number;
  requirements: CommunityRequirement[];
  refundHours: number | null;
  prefill: { name: string; email: string };
}) {
  const router = useRouter();
  const [pending, startTransition] = useTransition();
  const [open, setOpen] = useState(false);
  const [acked, setAcked] = useState<Set<string>>(new Set());
  const timezone = useLocalTimezone();

  const allAcked = requirements.every((r) => acked.has(r.id));
  const canAfford = balance >= cost;
  const soon = new Date(event.startsAt).getTime() - Date.now() < 10 * 60_000;

  function register() {
    startTransition(async () => {
      const res = await createBooking({
        slotId: event.id,
        name: prefill.name,
        email: prefill.email,
        timezone,
        acknowledgedRequirements: [...acked],
      });
      if (res.ok) {
        toast.success(`You're registered for ${event.title}`);
        setOpen(false);
        router.refresh();
      } else {
        toast.error(res.error);
        if (res.reason === "slot_gone" || res.reason === "insufficient_coins") router.refresh();
      }
    });
  }

  function unregister() {
    startTransition(async () => {
      // The list never exposes booking ids, so cancellation goes by slot.
      const res = await cancelEventRegistration(event.id);
      if (res.ok) {
        toast.success(
          res.refunded ? `Cancelled — ${res.refunded} coins returned` : "Registration cancelled",
        );
        router.refresh();
      } else {
        toast.error(res.error ?? "Couldn't cancel.");
      }
    });
  }

  return (
    <Card className={cn(event.registered && "border-success/40 bg-success/5")}>
      <CardContent className="p-5">
        <div className="flex flex-wrap items-start justify-between gap-3">
          <div className="min-w-0">
            <div className="flex flex-wrap items-center gap-2">
              <p className="font-display text-base font-semibold">{event.title}</p>
              {event.registered && (
                <Badge className="bg-success/15 text-success hover:bg-success/20">
                  <Check className="mr-1 h-3 w-3" />
                  Registered
                </Badge>
              )}
              {!event.registered && event.isFull && <Badge variant="secondary">Full</Badge>}
            </div>
            <p className="mt-1 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-muted-foreground">
              <span className="inline-flex items-center gap-1.5">
                <CalendarDays className="h-3.5 w-3.5" />
                <LocalTime iso={new Date(event.startsAt).toISOString()} format="full" />
              </span>
              <span>{event.durationMinutes} min</span>
              <span className="inline-flex items-center gap-1.5">
                <Users className="h-3.5 w-3.5" />
                {event.isFull ? "Full" : `${event.seatsLeft} of ${event.capacity} seats left`}
              </span>
            </p>
            {event.description && (
              <p className="mt-2 max-w-prose text-sm text-muted-foreground">{event.description}</p>
            )}
          </div>

          <div className="flex shrink-0 flex-col items-end gap-2">
            {event.registered ? (
              <>
                {event.meetingUrl && soon && (
                  <Button asChild size="sm">
                    <a href={event.meetingUrl} target="_blank" rel="noopener noreferrer">
                      <Video className="mr-1.5 h-3.5 w-3.5" />
                      Join
                    </a>
                  </Button>
                )}
                <Button size="sm" variant="ghost" disabled={pending} onClick={unregister}>
                  Cancel
                </Button>
              </>
            ) : event.isFull ? (
              <Button size="sm" disabled>
                Full
              </Button>
            ) : (
              <Button size="sm" onClick={() => setOpen((v) => !v)}>
                {cost > 0 ? `Register · ${cost} coins` : "Register — free"}
              </Button>
            )}
          </div>
        </div>

        {open && !event.registered && (
          <div className="mt-4 space-y-3 rounded-lg border border-border bg-card/70 p-4">
            {!canAfford ? (
              <div>
                <p className="text-sm font-medium">Not enough coins</p>
                <p className="mt-1 text-sm text-muted-foreground">
                  This event costs {cost} and you have {balance}.
                </p>
                <Button asChild size="sm" className="mt-3">
                  <Link href="/invite">Invite friends to earn coins</Link>
                </Button>
              </div>
            ) : (
              <>
                <p className="text-sm font-medium">Before you register</p>
                {requirements.map((r) => (
                  <label key={r.id} className="flex cursor-pointer items-center gap-3 text-sm">
                    <input
                      type="checkbox"
                      checked={acked.has(r.id)}
                      onChange={(e) =>
                        setAcked((prev) => {
                          const next = new Set(prev);
                          if (e.target.checked) next.add(r.id);
                          else next.delete(r.id);
                          return next;
                        })
                      }
                      className="h-4 w-4 shrink-0 rounded border-input accent-primary"
                    />
                    <span>
                      {r.label}{" "}
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
                ))}
                <p className="text-xs text-muted-foreground">
                  Your subscription will be checked by volunteers, and if there is no subscription
                  your place will be cancelled. Your coins will be returned if that happens.
                </p>

                <div className="flex flex-wrap items-center justify-between gap-3 border-t border-border pt-3">
                  <p className="text-sm text-muted-foreground">
                    {cost > 0 ? (
                      <>
                        <CoinAmount value={balance} size="sm" /> →{" "}
                        <CoinAmount value={balance - cost} size="sm" /> after
                      </>
                    ) : (
                      "This event is free."
                    )}
                  </p>
                  <Button size="sm" disabled={!allAcked || pending} onClick={register}>
                    {pending && <Loader2 className="mr-1.5 h-3.5 w-3.5 animate-spin" />}
                    Confirm registration
                  </Button>
                </div>
                {refundHours !== null && cost > 0 && (
                  <p className="text-xs text-muted-foreground">
                    Cancel at least {refundHours} hours before and your coins come back.
                  </p>
                )}
              </>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
