import type { LucideIcon } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { CountUp } from "@/components/shared/motion";
import { cn } from "@/lib/utils";

/**
 * A headline number.
 *
 * Numeric values count up on first view; anything else (an em dash, a "1:10"
 * duration) renders straight, since counting a string is meaningless. The card
 * lifts on hover only when it is actually a link — a lift on something inert
 * promises an interaction that never arrives.
 */
export function StatCard({
  label,
  value,
  sublabel,
  icon: Icon,
  tone = "primary",
  interactive,
}: {
  label: string;
  value: string | number;
  sublabel?: string;
  icon: LucideIcon;
  tone?: "primary" | "emerald" | "amber" | "violet";
  interactive?: boolean;
}) {
  const tones = {
    primary: "bg-primary/10 text-primary",
    emerald: "bg-emerald-500/10 text-emerald-500",
    amber: "bg-amber-500/10 text-amber-500",
    violet: "bg-violet-500/10 text-violet-500",
  } as const;

  return (
    <Card className={cn("overflow-hidden", interactive && "lift cursor-pointer")}>
      <CardContent className="flex items-center justify-between gap-3 p-5">
        <div className="min-w-0">
          <p className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
            {label}
          </p>
          <p className="font-display text-2xl font-semibold">
            {typeof value === "number" ? <CountUp value={value} /> : value}
          </p>
          {sublabel && <p className="truncate text-xs text-muted-foreground">{sublabel}</p>}
        </div>
        <span
          className={cn(
            "flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl transition-transform duration-300",
            tones[tone]
          )}
        >
          <Icon className="h-5 w-5" />
        </span>
      </CardContent>
    </Card>
  );
}
