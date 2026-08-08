import { cn } from "@/lib/utils";

/**
 * The SATForge Coins mark.
 *
 * One component so the coin reads identically on the dashboard, the wallet, the
 * booking page and the invite page. The gradient and glow are the same electric
 * blue/purple language as the landing hero, expressed through the existing
 * primary token rather than a new hard-coded colour.
 */
export function CoinIcon({ className }: { className?: string }) {
  return (
    <span
      aria-hidden
      className={cn(
        "inline-flex shrink-0 items-center justify-center rounded-full",
        "bg-gradient-to-br from-amber-300 via-amber-400 to-amber-600",
        "text-[0.6em] font-bold text-amber-950 shadow-[0_0_0_1px_rgba(180,120,20,0.35)]",
        className,
      )}
    >
      S
    </span>
  );
}

export function CoinAmount({
  value,
  size = "md",
  signed = false,
  className,
}: {
  value: number;
  size?: "sm" | "md" | "lg" | "xl";
  /** Show an explicit + for credits, as a ledger would. */
  signed?: boolean;
  className?: string;
}) {
  const sizes = {
    sm: { text: "text-sm", coin: "h-3.5 w-3.5" },
    md: { text: "text-base", coin: "h-4 w-4" },
    lg: { text: "text-2xl", coin: "h-6 w-6" },
    xl: { text: "text-4xl", coin: "h-8 w-8" },
  }[size];

  const positive = value > 0;
  return (
    <span className={cn("inline-flex items-center gap-1.5 font-semibold tabular-nums", sizes.text, className)}>
      <CoinIcon className={sizes.coin} />
      {signed && positive ? "+" : ""}
      {value}
    </span>
  );
}

/** Compact pill for the topbar and dashboard header. */
export function CoinBadge({ balance, className }: { balance: number; className?: string }) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full border border-amber-500/30",
        "bg-amber-500/10 px-3 py-1 text-sm font-semibold tabular-nums text-amber-600 dark:text-amber-400",
        className,
      )}
    >
      <CoinIcon className="h-3.5 w-3.5" />
      {balance}
      <span className="sr-only">SATForge Coins</span>
    </span>
  );
}
