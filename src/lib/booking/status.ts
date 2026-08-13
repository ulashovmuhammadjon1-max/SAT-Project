import type { BookingStatus } from "@prisma/client";

/**
 * The two questions the codebase actually asks about a booking's status.
 *
 * They were previously written inline as `status: { not: "CANCELLED" }`, which
 * was correct while CANCELLED was the only terminal state. Adding REJECTED
 * broke that in a way nothing would have caught: a rejected booking would have
 * gone on holding its seat forever, so a slot could silently fill up with
 * sessions the admin had already turned down. Both sets live here so a future
 * status has exactly one place to be classified.
 */

/**
 * Occupies a seat in the slot's capacity.
 *
 * PENDING counts. A student waiting on a decision has really reserved the
 * place — if it did not count, a popular slot would take unlimited requests and
 * approving them would overflow the capacity.
 */
export const SEAT_HOLDING_STATUSES: BookingStatus[] = ["PENDING", "UPCOMING", "COMPLETED"];

/**
 * A live booking from the student's point of view: it is either happening or
 * about to be decided. Used to stop someone holding two sessions at once and to
 * decide what appears on the dashboard.
 */
export const ACTIVE_STATUSES: BookingStatus[] = ["PENDING", "UPCOMING"];

/** Terminal states where the seat is free again and coins have been returned. */
export const RELEASED_STATUSES: BookingStatus[] = ["CANCELLED", "REJECTED"];

export const BOOKING_STATUS_LABELS: Record<BookingStatus, string> = {
  PENDING: "Awaiting approval",
  UPCOMING: "Confirmed",
  COMPLETED: "Completed",
  CANCELLED: "Cancelled",
  REJECTED: "Declined",
};

/** Badge tone per status, so student and admin views agree on the colour. */
export const BOOKING_STATUS_TONE: Record<BookingStatus, "default" | "success" | "secondary" | "destructive" | "outline"> = {
  PENDING: "outline",
  UPCOMING: "default",
  COMPLETED: "success",
  CANCELLED: "secondary",
  REJECTED: "destructive",
};
