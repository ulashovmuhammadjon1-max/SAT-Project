import { Skeleton } from "@/components/ui/skeleton";
import { SessionCardSkeleton } from "@/components/student/booking/session-card";

/** Shown while the booking page's data loads, in the page's own shape. */
export default function BookingLoading() {
  return (
    <div className="space-y-10" aria-busy="true" aria-label="Loading sessions">
      <div className="space-y-6">
        <div className="space-y-3">
          <Skeleton className="h-9 w-80 max-w-full" />
          <Skeleton className="h-5 w-full max-w-xl" />
        </div>
        <Skeleton className="h-24 w-full rounded-xl" />
      </div>
      <div className="space-y-5">
        <Skeleton className="h-6 w-48" />
        <Skeleton className="h-12 w-full rounded-lg" />
        <div className="flex gap-2">
          {[96, 120, 140, 110].map((w) => (
            <Skeleton key={w} className="h-11 rounded-full" style={{ width: w }} />
          ))}
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          {[0, 1, 2, 3].map((i) => (
            <SessionCardSkeleton key={i} />
          ))}
        </div>
      </div>
    </div>
  );
}
