"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { LocalTime, useLocalTimezone } from "@/components/shared/local-time";
import { cancelBooking } from "@/server/actions/student/bookings";

export interface BookingRow {
  id: string;
  status: "UPCOMING" | "COMPLETED" | "CANCELLED";
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
        toast.success("Session cancelled. That time is open again.");
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
                  <Badge
                    variant={
                      b.status === "UPCOMING"
                        ? "default"
                        : b.status === "COMPLETED"
                          ? "success"
                          : "secondary"
                    }
                  >
                    {b.status[0] + b.status.slice(1).toLowerCase()}
                  </Badge>
                  {b.status === "UPCOMING" && (
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => cancel(b.id)}
                      disabled={pendingId === b.id}
                    >
                      {pendingId === b.id && <Loader2 className="h-3.5 w-3.5 animate-spin" />}
                      Cancel
                    </Button>
                  )}
                </div>
              </CardContent>
            </Card>
          </li>
        );
      })}
    </ul>
  );
}
