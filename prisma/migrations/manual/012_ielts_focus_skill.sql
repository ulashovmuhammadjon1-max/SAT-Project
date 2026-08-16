-- 012 — which IELTS skill a student wants to lead with.
--
-- Collected by the IELTS branch of the onboarding wizard ("which one worries
-- you more?") and used to order the IELTS roadmap. Nullable, so rows written
-- before this column existed are simply "no preference" and the plan falls
-- back to the lower of the two reported bands.
--
-- Apply against production BEFORE deploying the commit that adds this field to
-- schema.prisma. Vercel rebuilds the Prisma client from the schema on every
-- deploy, so a schema-first deploy makes every unguarded read of this model
-- ask for a column the database does not have.
--
--   psql "$PROD_URL" -f prisma/migrations/manual/012_ielts_focus_skill.sql

ALTER TABLE "IeltsStudentProfile" ADD COLUMN IF NOT EXISTS "focusSkill" TEXT;
