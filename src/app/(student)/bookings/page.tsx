import Link from "next/link";
import { PartyPopper } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { BookingList } from "@/components/student/booking-list";
import { LocalTime } from "@/components/shared/local-time";
import { getMyBookings } from "@/server/actions/student/bookings";

export const metadata = { title: "My sessions" };
export const dynamic = "force-dynamic";

export default async function MyBookingsPage({
  searchParams,
}: {
  searchParams: { booked?: string };
}) {
  const bookings = await getMyBookings();
  const justBooked = bookings.find((b) => b.id === searchParams.booked);

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">My sessions</h1>
          <p className="text-sm text-muted-foreground">Your free 1-on-1 SAT guidance sessions.</p>
        </div>
        {!bookings.some((b) => b.status === "UPCOMING") && (
          <Button asChild>
            <Link href="/booking">Book a session</Link>
          </Button>
        )}
      </div>

      {justBooked && (
        <Card className="border-success/40 bg-success/5">
          <CardContent className="p-6">
            <div className="flex items-center gap-2">
              <PartyPopper className="h-5 w-5 text-success" />
              <p className="font-display text-lg font-semibold">You&apos;re booked!</p>
            </div>

            <dl className="mt-4 grid gap-x-8 gap-y-2 text-sm sm:grid-cols-2">
              <div className="flex justify-between sm:block">
                <dt className="text-muted-foreground">Date</dt>
                <dd className="font-medium">
                  <LocalTime iso={justBooked.slot.startsAt.toISOString()} format="date" />
                </dd>
              </div>
              <div className="flex justify-between sm:block">
                <dt className="text-muted-foreground">Time</dt>
                <dd className="font-medium">
                  <LocalTime iso={justBooked.slot.startsAt.toISOString()} format="time" />
                </dd>
              </div>
              <div className="flex justify-between sm:block">
                <dt className="text-muted-foreground">Duration</dt>
                <dd className="font-medium">{justBooked.slot.durationMinutes} minutes</dd>
              </div>
              <div className="flex justify-between sm:block">
                <dt className="text-muted-foreground">Timezone</dt>
                <dd className="font-medium">{justBooked.timezone ?? "Your local time"}</dd>
              </div>
            </dl>

            <p className="mt-4 text-sm text-muted-foreground">
              <span className="font-medium text-foreground">What to expect: </span>
              Come prepared with your latest SAT score or practice results if available.
            </p>
          </CardContent>
        </Card>
      )}

      {bookings.length === 0 ? (
        <Card>
          <CardContent className="space-y-3 p-8 text-center">
            <p className="font-medium">No sessions yet.</p>
            <p className="text-sm text-muted-foreground">
              Book a free 1-on-1 with a 1580 scorer to build your study plan.
            </p>
            <Button asChild>
              <Link href="/booking">Get My Free SAT Plan</Link>
            </Button>
          </CardContent>
        </Card>
      ) : (
        <BookingList
          bookings={bookings.map((b) => ({
            id: b.id,
            status: b.status,
            startsAt: b.slot.startsAt.toISOString(),
            durationMinutes: b.slot.durationMinutes,
          }))}
        />
      )}
    </div>
  );
}
