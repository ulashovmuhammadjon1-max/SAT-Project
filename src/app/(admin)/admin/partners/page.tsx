import { PartnersAdmin, type PartnerRow } from "@/components/admin/partners-admin";
import { prisma } from "@/lib/prisma";
import { requireAdmin } from "@/lib/session";

export const metadata = { title: "Partners" };
export const dynamic = "force-dynamic";

export default async function PartnersPage() {
  await requireAdmin();

  const partners = await prisma.partner.findMany({
    orderBy: [{ order: "asc" }, { createdAt: "asc" }],
  });

  const rows: PartnerRow[] = partners.map((p) => ({
    id: p.id,
    name: p.name,
    logoUrl: p.logoUrl,
    href: p.href,
    blurb: p.blurb,
    order: p.order,
    isPublished: p.isPublished,
  }));

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold tracking-tight">Partners</h1>
        <p className="text-sm text-muted-foreground">
          Logos on the landing page. Each one links out to the partner. Nothing appears on the site
          until you press Publish, and the section is hidden entirely while no partner is live.
        </p>
      </div>

      <PartnersAdmin partners={rows} />
    </div>
  );
}
