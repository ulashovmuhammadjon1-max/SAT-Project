import { prisma } from "@/lib/prisma";
import { Reveal } from "@/components/shared/motion";

/**
 * Partner logos, each linking out to the partner.
 *
 * Rendered in two places, because they have different audiences: the marketing
 * landing page, which only logged-out visitors see, and the student dashboard.
 * A student logs in straight to /dashboard and never returns to /, so a strip
 * that lived only on the landing page would be invisible to exactly the people
 * a partner most wants reaching their channel. `compact` is the in-app version:
 * same data, less vertical shouting inside the app shell.
 *
 * Renders nothing at all when there are no published partners — an empty
 * "Our partners" heading reads as a company with no partners, which is worse
 * than not raising the subject.
 *
 * Every link is `rel="noopener noreferrer"`: without `noopener` the destination
 * gets a handle on this window through `window.opener` and can navigate it
 * somewhere else, which is a real phishing vector on any outbound link.
 */
export async function PartnersStrip({ compact = false }: { compact?: boolean }) {
  // Fails soft, deliberately. This component is rendered on the marketing
  // landing page, which Next prerenders at build time — so a database that is
  // unreachable during a build would otherwise fail the whole deploy over a
  // decorative logo strip. Caught here, a build with no database simply ships a
  // page without partners, and the next request-time render fills them in.
  let partners: { id: string; name: string; logoUrl: string; href: string; blurb: string | null }[];
  try {
    partners = await prisma.partner.findMany({
      where: { isPublished: true },
      orderBy: [{ order: "asc" }, { createdAt: "asc" }],
      select: { id: true, name: true, logoUrl: true, href: true, blurb: true },
    });
  } catch (error) {
    console.error("[partners] could not load, rendering nothing", error);
    return null;
  }

  if (partners.length === 0) return null;

  if (compact) {
    return (
      <section aria-labelledby="partners-heading">
        <h2 id="partners-heading" className="font-display text-lg font-semibold">
          Our partners
        </h2>
        <p className="mt-0.5 text-sm text-muted-foreground">
          Communities we work with. Worth following.
        </p>
        <ul className="stagger mt-4 flex flex-wrap gap-3">
          {partners.map((p) => (
            <li key={p.id}>
              <a
                href={p.href}
                target="_blank"
                rel="noopener noreferrer"
                className="lift group flex items-center gap-3 rounded-xl border border-border bg-card/60 p-3 pr-4 transition-colors hover:border-primary/40 hover:bg-card"
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={p.logoUrl}
                  alt=""
                  aria-hidden
                  className="h-10 w-10 rounded-full object-cover ring-1 ring-border transition-transform duration-300 group-hover:scale-105"
                  loading="lazy"
                />
                <span className="min-w-0">
                  <span className="block text-sm font-medium">{p.name}</span>
                  {p.blurb && (
                    <span className="block text-xs text-muted-foreground">{p.blurb}</span>
                  )}
                </span>
              </a>
            </li>
          ))}
        </ul>
      </section>
    );
  }

  return (
    <section className="border-t border-border/60 py-16">
      <div className="mx-auto max-w-5xl px-6">
        <Reveal>
          <p className="text-center text-xs font-semibold uppercase tracking-[0.18em] text-muted-foreground">
            Our partners
          </p>
          <h2 className="mt-2 text-center font-display text-2xl font-semibold tracking-tight">
            Building the SAT community together
          </h2>
        </Reveal>

        <ul className="stagger mt-10 flex flex-wrap items-stretch justify-center gap-4">
          {partners.map((p) => (
            <li key={p.id}>
              <a
                href={p.href}
                target="_blank"
                rel="noopener noreferrer"
                className="lift group flex h-full w-56 flex-col items-center gap-3 rounded-2xl border border-border bg-card/60 p-6 text-center transition-colors hover:border-primary/40 hover:bg-card"
              >
                {/* A plain img, not next/image: partner logos are arbitrary
                    remote hosts and every one would need adding to the image
                    config before it would render at all. */}
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={p.logoUrl}
                  alt=""
                  aria-hidden
                  className="h-16 w-16 rounded-full object-cover ring-1 ring-border transition-transform duration-300 group-hover:scale-105"
                  loading="lazy"
                />
                <span className="font-medium">{p.name}</span>
                {p.blurb && <span className="text-xs text-muted-foreground">{p.blurb}</span>}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
