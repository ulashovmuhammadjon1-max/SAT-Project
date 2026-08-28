import { redirect } from "next/navigation";

/** Leaderboards are per class now: /classes/{id}/leaderboard. */
export default function LegacyClassLeaderboardPage() {
  redirect("/classes");
}
