-- 027: per-admin saved session details ("My saved details" on My Sessions).
--
-- One row per admin who has saved anything: their own Google Meet link and
-- the subject and title they usually teach, used to prefill new sessions.
-- A new table that no existing code reads, so it is safe to apply before the
-- code that uses it is deployed. Idempotent.

CREATE TABLE IF NOT EXISTS "HostProfile" (
  "userId"         TEXT PRIMARY KEY,
  "meetingUrl"     TEXT,
  "defaultSubject" TEXT,
  "defaultTitle"   TEXT,
  "updatedAt"      TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "HostProfile_userId_fkey" FOREIGN KEY ("userId")
    REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
