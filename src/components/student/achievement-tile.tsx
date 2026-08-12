import {
  Award,
  BookOpen,
  Brain,
  Crosshair,
  Flame,
  Lock,
  SpellCheck2,
  Trophy,
  Users,
} from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import type {
  AchievementCategory,
  AchievementTier,
  EarnedAchievement,
} from "@/lib/achievements/definitions";
import { cn } from "@/lib/utils";

export const CATEGORY_ICONS: Record<AchievementCategory, typeof Award> = {
  CONSISTENCY: Flame,
  VOLUME: Brain,
  TESTS: BookOpen,
  SCORE: Trophy,
  ACCURACY: Crosshair,
  VOCABULARY: SpellCheck2,
  COMMUNITY: Users,
};

/**
 * Tier colours. Unlocked badges are saturated; locked ones fall back to muted,
 * so a wall of achievements reads at a glance as "what I have" instead of
 * needing every tile inspected.
 */
export const TIER_STYLES: Record<AchievementTier, string> = {
  BRONZE: "bg-orange-500/15 text-orange-500 ring-orange-500/30",
  SILVER: "bg-slate-400/15 text-slate-400 ring-slate-400/30",
  GOLD: "bg-amber-400/15 text-amber-500 ring-amber-400/30",
  PLATINUM: "bg-cyan-400/15 text-cyan-400 ring-cyan-400/30",
};

export function AchievementMedal({
  achievement: a,
  className,
}: {
  achievement: EarnedAchievement;
  className?: string;
}) {
  return (
    <span
      className={cn(
        "flex h-10 w-10 shrink-0 items-center justify-center rounded-full ring-1 transition-transform duration-300",
        a.unlocked
          ? `${TIER_STYLES[a.tier]} group-hover/tile:scale-110`
          : "bg-muted text-muted-foreground ring-border",
        className
      )}
    >
      {a.unlocked ? <Award className="h-5 w-5" /> : <Lock className="h-4 w-4" />}
    </span>
  );
}

export function AchievementTile({ achievement: a }: { achievement: EarnedAchievement }) {
  return (
    <Card className={cn("group/tile lift", !a.unlocked && "opacity-75 hover:opacity-100")}>
      <CardContent className="flex gap-3 p-4">
        <AchievementMedal achievement={a} />

        <div className="min-w-0 flex-1">
          <p className="flex items-baseline gap-2 font-medium">
            {a.title}
            <span className="text-[10px] uppercase tracking-wide text-muted-foreground">
              {a.tier.toLowerCase()}
            </span>
          </p>
          <p className="mt-0.5 text-xs text-muted-foreground">{a.description}</p>

          {a.unlocked ? (
            <p className="mt-2 text-xs font-medium text-emerald-500">Unlocked</p>
          ) : a.blockedBy ? (
            // Gated rather than merely short — showing a progress bar here
            // would imply the badge is close when the gate is what blocks it.
            <p className="mt-2 text-xs text-muted-foreground">{a.blockedBy}</p>
          ) : (
            <div className="mt-2">
              <Progress value={a.progressPct} className="h-1" />
              <p className="mt-1 text-xs tabular-nums text-muted-foreground">
                {a.currentValue.toLocaleString()}
                {a.unit} / {a.target.toLocaleString()}
                {a.unit}
              </p>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
