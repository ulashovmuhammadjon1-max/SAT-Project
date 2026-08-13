"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";

import type { BookingStatus } from "@prisma/client";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { ACTIVE_STATUSES, BOOKING_STATUS_LABELS, BOOKING_STATUS_TONE } from "@/lib/booking/status";
import { cancelBooking } from "@/server/actions/student/bookings";

export interface BookingRow {
  id: string;
  status: BookingStatus;
  /** What an admin said when approving, declining or cancelling. */
  statusReason?: string | null;
  startsAt: string;
  durationMinutes: number;
}

export function BookingList({ bookings }: { bookings: BookingRow[] }) {
  const router = useRouter();
  const [pendingId, setPendingId] = useState<string | null>(null);
  const [, startTransition] = useTransition();
  const tz = useLocalTimezone();

  function cancel(id: string) {
    setPendingId(id);
    startTransition(async () => {
      const res = await cancelBooking(id);
      setPendingId(null);
      if (res.ok) {
        toast.success(
          res.refunded
            ? `Cancelled — ${res.refunded} coin${res.refunded === 1 ? "" : "s"} returned.`
            : "Cancelled. That time is open again.",
        );
        router.refresh();
      } else {
        toast.error(res.error ?? "Couldn't cancel.");
      }
    });
  }

  return (
    <ul className="space-y-3">
      {bookings.map((b) => {
        return (
          <li key={b.id}>
            <Card>
              <CardContent className="flex flex-wrap items-center justify-between gap-4 p-5">
                <div>
                  <p className="font-medium">
                    <LocalTime iso={b.startsAt} format="full" />
                  </p>
                  <p className="mt-0.5 text-sm text-muted-foreground">
                    {b.durationMinutes} minutes{tz && ` · ${tz}`}
                  </p>
                </div>

                <div className="flex items-center gap-3">
                  <Badge variant={BOOKING_STATUS_TONE[b.status]}>
                    {BOOKING_STATUS_LABELS[b.status]}
                  </Badge>
                  {ACTIVE_STATUSES.includes(b.status) && (
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => cancel(b.id)}
                      disabled={pendingId === b.id}
                    >
                      {pendingId === b.id && <Loader2 className="h-3.5 w-3.5 animate-spin" />}
                      {b.status === "PENDING" ? "Withdraw" : "Cancel"}
                    </Button>
                  )}
                </div>
              </CardContent>
              {b.statusReason && (
                <div className="border-t px-5 py-3">
                  <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
                    Note from the SATForge team
                  </p>
                  <p className="mt-1 whitespace-pre-line text-sm">{b.statusReason}</p>
                </div>
              )}
            </Card>
          </li>
        );
      })}
    </ul>
  );
}
