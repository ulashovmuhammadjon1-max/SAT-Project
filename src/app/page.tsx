import { Landing, type ApSummary } from "@/components/marketing/landing";
import { AP_CATALOG, AP_CATEGORIES } from "@/lib/ap/catalog";
import { AP_COURSES } from "@/lib/ap/courses";

/**
 * The AP summary is computed here, on the server, so the landing page never
 * ships the catalog (which pulls in every course outline) to the browser.
 *
 * The course excerpt in the hero is real: AP Biology, Unit 3, read from the
 * same outline the course pages render. If that unit is ever renamed or
 * removed the excerpt follows, or disappears, rather than going stale.
 */
const live = AP_CATALOG.filter((s) => s.status === "LIVE");
const biology = AP_COURSES.find((c) => c.code === "BIOLOGY");
const unit = biology?.units.find((u) => u.number === 3);

const AP_SUMMARY: ApSummary = {
  live: live.map((s) => ({ code: s.code, name: s.name, category: s.category })),
  categories: AP_CATEGORIES.filter((c) => live.some((s) => s.category === c.id)).map((c) => ({
    id: c.id,
    label: c.label,
  })),
  plannedCount: AP_CATALOG.length - live.length,
  sample:
    biology && unit?.topics?.length
      ? {
          course: biology.name,
          unitNumber: unit.number,
          unitTitle: unit.title,
          topics: unit.topics.map((t) => ({ code: t.code, title: t.title })),
        }
      : null,
};

export default function HomePage() {
  return <Landing ap={AP_SUMMARY} />;
}
