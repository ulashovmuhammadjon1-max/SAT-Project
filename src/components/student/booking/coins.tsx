import { CoinIcon } from "@/components/student/coin-badge";
import { cn } from "@/lib/utils";

/**
 * "15 coins" with the Scholarly coin mark. Always the word "coins", never a
 * currency symbol: coins are Scholarly's own points, not money.
 */
export function Coins({
  value,
  className,
  size = "md",
}: {
  value: number;
  className?: string;
  size?: "sm" | "md" | "lg";
}) {
  const s = { sm: ["text-sm", "h-3.5 w-3.5"], md: ["text-base", "h-4 w-4"], lg: ["text-2xl", "h-6 w-6"] }[size];
  return (
    <span className={cn("inline-flex items-center gap-1.5 whitespace-nowrap tabular-nums", s[0], className)}>
      <CoinIcon className={s[1]} />
      <span>
        <span className="font-semibold">{value}</span> {value === 1 ? "coin" : "coins"}
      </span>
    </span>
  );
}
