import { Landing, type ApSummary } from "@/components/marketing/landing";
import { AP_CATALOG } from "@/lib/ap/catalog";

/**
 * The AP summary is computed here, on the server, so the client-side landing
 * page never imports the catalog (which pulls in every course outline).
 */
const AP_SUMMARY: ApSummary = {
  live: AP_CATALOG.filter((s) => s.status === "LIVE").map((s) => ({ code: s.code, name: s.name })),
  plannedCount: AP_CATALOG.filter((s) => s.status !== "LIVE").length,
};

export default function HomePage() {
  return <Landing ap={AP_SUMMARY} />;
}
