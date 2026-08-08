import Link from "next/link";
import { CheckCircle2 } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { BookingForm } from "@/components/student/booking-form";
import { LocalTime } from "@/components/shared/local-time";
import { prisma } from "@/lib/prisma";
import { requireUser } from "@/lib/session";
import { getOpenSlots } from "@/server/actions/student/bookings";

export const metadata = { title: "Get Your Free SAT Plan" };
export const dynamic = "force-dynamic";

const COVERED = [
  "Review your current SAT level",
  "Identify your biggest weaknesses",
  "Discuss your target score",
  "Build a realistic study schedule",
  "Decide what to practice",
  "Answer your SAT questions",
  "Leave with a concrete plan",
];

export default async function BookingPage() {
  const user = await requireUser();

  const [profile, slots, existing] = await Promise.all([
    prisma.user.findUnique({
      where: { id: user.id },
      select: {
        name: true,
        email: true,
        currentScore: true,
        targetScore: true,
        satDate: true,
        weakestArea: true,
      },
    }),
    getOpenSlots(),
    prisma.booking.findFirst({
      where: { userId: user.id, status: "UPCOMING" },
      include: { slot: true },
    }),
  ]);

  if (existing) {
    return (
      <div className="mx-auto max-w-2xl space-y-6">
        <h1 className="font-display text-2xl font-semibold tracking-tight">Get Your Free SAT Plan</h1>
        <Card>
          <CardContent className="space-y-3 p-6">
            <p className="font-medium">You already have a session booked.</p>
            <p className="text-sm text-muted-foreground">
              <LocalTime iso={existing.slot.startsAt.toISOString()} format="full" />
            </p>
            <Button asChild>
              <Link href="/bookings">View my booking</Link>
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight sm:text-3xl">
          Get Your Free SAT Plan
        </h1>
        <p className="mt-2 text-[15px] leading-relaxed text-muted-foreground">
          Meet 1-on-1 with a 1580 SAT scorer and build a study plan around your score, target,
          timeline, and weaknesses.
        </p>
      </div>

      <Card>
        <CardContent className="p-6">
          <h2 className="font-display font-semibold">In your session</h2>
          <ul className="mt-3 grid gap-2 sm:grid-cols-2">
            {COVERED.map((c) => (
              <li key={c} className="flex items-start gap-2 text-sm">
                <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-success" />
                {c}
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <BookingForm
        slots={slots}
        prefill={{
          name: profile?.name ?? "",
          email: profile?.email ?? "",
          currentScore: profile?.currentScore ?? null,
          targetScore: profile?.targetScore ?? null,
          satDate: profile?.satDate ? profile.satDate.toISOString().slice(0, 10) : null,
          weakestArea: profile?.weakestArea ?? null,
        }}
      />
    </div>
  );
}
