-- 026: admin-hosted 1-on-1 sessions.
--
-- Every admin can publish their own 1-on-1 sessions from /admin/my-sessions,
-- with a title, a subject and their own Google Meet link.
--
-- 1. Two nullable columns on MentorSlot: subject and meetingUrl. Additive, so
--    code that does not know about them keeps working.
-- 2. The uniqueness rule moves from (startsAt) to (hostId, startsAt), so two
--    different admins can teach at the same hour. NULLS NOT DISTINCT keeps the
--    old guarantee for host-less (founder) slots: two of those still cannot
--    start at the same instant, which createSlots' skipDuplicates relies on.
--    Requires Postgres 15+ (production is 17).
--
-- Idempotent: safe to run more than once. Apply BEFORE deploying the code.

ALTER TABLE "MentorSlot" ADD COLUMN IF NOT EXISTS "subject" TEXT;
ALTER TABLE "MentorSlot" ADD COLUMN IF NOT EXISTS "meetingUrl" TEXT;

CREATE UNIQUE INDEX IF NOT EXISTS "MentorSlot_hostId_startsAt_key"
  ON "MentorSlot" ("hostId", "startsAt") NULLS NOT DISTINCT;

DROP INDEX IF EXISTS "MentorSlot_startsAt_key";
