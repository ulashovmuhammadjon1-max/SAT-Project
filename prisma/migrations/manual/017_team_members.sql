-- Admin-managed team members for the public /team page.
-- New table only; applied to production before the code deploys.

CREATE TABLE "TeamMember" (
  "id"        TEXT NOT NULL PRIMARY KEY,
  "name"      TEXT NOT NULL,
  "title"     TEXT NOT NULL,
  "email"     TEXT,
  -- Portrait as an inline data URI, same storage approach as certificates.
  "photo"     TEXT,
  "bio"       TEXT,
  "order"     INTEGER NOT NULL DEFAULT 0,
  "isActive"  BOOLEAN NOT NULL DEFAULT true,
  "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX "TeamMember_isActive_order_idx" ON "TeamMember"("isActive", "order");
