-- Partner logos on the landing page.
--
-- Idempotent, like every migration in this directory. Keep semicolons out of
-- comments here -- the runner splits on semicolons outside dollar-quotes.

CREATE TABLE IF NOT EXISTS "Partner" (
  "id"          TEXT NOT NULL,
  "name"        TEXT NOT NULL,
  "logoUrl"     TEXT NOT NULL,
  "href"        TEXT NOT NULL,
  "blurb"       TEXT,
  "order"       INTEGER NOT NULL DEFAULT 0,
  "isPublished" BOOLEAN NOT NULL DEFAULT false,
  "createdAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"   TIMESTAMP(3) NOT NULL,
  CONSTRAINT "Partner_pkey" PRIMARY KEY ("id")
);

-- The public strip reads exactly this: published rows in display order.
CREATE INDEX IF NOT EXISTS "Partner_isPublished_order_idx" ON "Partner"("isPublished", "order");
