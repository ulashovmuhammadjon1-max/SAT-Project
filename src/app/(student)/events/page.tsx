import { CalendarRange } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { CoinAmount } from "@/components/student/coin-badge";
import { EventCard } from "@/components/student/event-card";
import { getEvents } from "@/server/actions/student/events";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";

export const metadata = { title: "Events" };
export const dynamic = "force-dynamic";

export default async function EventsPage() {
  const user = await requireUser();
  const [page, profile] = await Promise.all([
    getEvents(),
    prisma.user.findUnique({
      where: { id: user.id },
      select: { name: true, email: true },
    }),
  ]);

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-2xl font-semibold tracking-tight">Events</h1>
          <p className="text-sm text-muted-foreground">
            Weekly practice-test reviews, lectures and workshops — free, and open to everyone.
          </p>
        </div>
        <CoinAmount value={page.balance} />
      </div>

      {page.events.length === 0 ? (
        <Card className="border-dashed">
          <CardContent className="p-10 text-center">
            <CalendarRange className="mx-auto mb-3 h-10 w-10 text-muted-foreground" />
            <p className="font-medium">No events scheduled yet</p>
            <p className="mx-auto mt-1 max-w-sm text-sm text-muted-foreground">
              The weekly practice-test review and guest lectures will show up here. Follow the
              Telegram channel and you&apos;ll hear about them first.
            </p>
          </CardContent>
        </Card>
      ) : (
        <div className="space-y-3">
          {page.events.map((e) => (
            <EventCard
              key={e.id}
              event={e}
              cost={page.cost}
              balance={page.balance}
              requirements={page.requirements}
              refundHours={page.refundHours}
              prefill={{ name: profile?.name ?? "", email: profile?.email ?? "" }}
            />
          ))}
        </div>
      )}
    </div>
  );
}
