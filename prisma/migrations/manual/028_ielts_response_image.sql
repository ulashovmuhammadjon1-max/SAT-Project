-- 028: a student may attach an image to a Writing Task 1 response.
--
-- Optional, and Task 1 only (enforced in the server action, not here). Holds a
-- storage key written by `savePromptImage` — a Vercel Blob pathname or a local
-- file name — never a URL; the image is served through
-- /api/ielts/response-image/[submissionId], which checks who is asking.
--
-- Additive and nullable: safe to apply before the code that reads it ships.

ALTER TABLE "IeltsWritingSubmission" ADD COLUMN IF NOT EXISTS "responseImage" TEXT;
