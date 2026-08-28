-- Classroom redesign: drafts and multi-file submissions.
--
-- Additive and re-runnable; statements are sent one at a time with no
-- enclosing transaction, so each must be independently safe.

-- A completion row now has two moments: created (work uploaded) and
-- submitted. NULL submittedAt = a draft the student has not handed in yet.
ALTER TABLE "AssignmentCompletion" ADD COLUMN IF NOT EXISTS "submittedAt" TIMESTAMP(3);

-- Every row that exists today was a real hand-in — drafts did not exist yet.
-- The date guard makes a re-run safe: it can never touch a draft created
-- after this migration shipped.
UPDATE "AssignmentCompletion"
   SET "submittedAt" = "completedAt"
 WHERE "submittedAt" IS NULL AND "completedAt" < TIMESTAMP '2026-08-29 00:00:00';

-- A submission can carry several files (a PDF plus screenshots). Stored as
-- data URIs on their own rows, same as every other upload on the platform.
CREATE TABLE IF NOT EXISTS "SubmissionFile" (
  "id"           TEXT NOT NULL PRIMARY KEY,
  "completionId" TEXT NOT NULL REFERENCES "AssignmentCompletion"("id") ON DELETE CASCADE,
  "name"         TEXT NOT NULL,
  "data"         TEXT NOT NULL,
  -- Decoded size in bytes (approximate for backfilled rows), for display.
  "size"         INTEGER NOT NULL DEFAULT 0,
  "createdAt"    TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS "SubmissionFile_completionId_idx" ON "SubmissionFile"("completionId");

-- Carry the old single-file uploads forward. The derived id makes this
-- idempotent: re-running inserts nothing new.
INSERT INTO "SubmissionFile" ("id", "completionId", "name", "data", "size")
SELECT 'sf_' || md5("id"), "id", "fileName", "fileData", (length("fileData") * 3) / 4
  FROM "AssignmentCompletion"
 WHERE "fileData" IS NOT NULL AND "fileName" IS NOT NULL
ON CONFLICT ("id") DO NOTHING;
