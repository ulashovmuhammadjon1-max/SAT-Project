import { Prisma } from "@prisma/client";

import { prisma } from "@/lib/prisma";
import { SEAT_HOLDING_STATUSES } from "@/lib/booking/status";

/**
 * How many 1-on-1 sessions a student could book right now: future, published,
 * not blocked, and with a seat still free.
 *
 * One aggregate query, because the student layout runs it on every page to put
 * the "N open" badge on the Sessions link. The same rules as getOpenSlots, so
 * the badge and the booking page can never disagree.
 */
export async function countOpenSessions(): Promise<number> {
  const rows = await prisma.$queryRaw<{ n: number }[]>`
    SELECT count(*)::int AS n
    FROM "MentorSlot" s
    WHERE s."isBlocked" = false
      AND s."startsAt" > now()
      AND s."sessionType" = 'ONE_ON_ONE_SAT'
      AND s.capacity > (
        SELECT count(*) FROM "Booking" b
        WHERE b."slotId" = s.id
          AND b.status IN (${Prisma.join(SEAT_HOLDING_STATUSES.map((st) => Prisma.sql`${st}::"BookingStatus"`))})
      )`;
  return rows[0]?.n ?? 0;
}
