-- Teacher panel, second pass: file attachments, Question Bank sets, and
-- student work submissions.
--
-- Additive columns only. Every statement is IF NOT EXISTS because the runner
-- sends statements one at a time with no enclosing transaction.

-- A teacher can attach one file (PDF or an image of a worksheet) to a task.
-- Stored as a data URI on the row, the same as peer-mentor certificates and
-- team photos — no blob token needed, and it cannot go missing separately
-- from the assignment it belongs to.
ALTER TABLE "ClassAssignment" ADD COLUMN IF NOT EXISTS "attachmentName" TEXT;
ALTER TABLE "ClassAssignment" ADD COLUMN IF NOT EXISTS "attachmentData" TEXT;

-- A hand-picked set of Question Bank questions. Deliberately NOT a foreign
-- key table: the ids are a soft reference, so retiring a question later
-- shrinks the set instead of breaking the assignment or the student's history.
ALTER TABLE "ClassAssignment" ADD COLUMN IF NOT EXISTS "questionIds" TEXT[] NOT NULL DEFAULT '{}';

-- Which Question Bank subject the set opens in. Derived from the picked
-- questions at creation; stored so the student's practice link needs no join.
ALTER TABLE "ClassAssignment" ADD COLUMN IF NOT EXISTS "subject" TEXT;

-- The student's submitted work: a short note and one uploaded file
-- (screenshot or PDF), both optional.
ALTER TABLE "AssignmentCompletion" ADD COLUMN IF NOT EXISTS "note" TEXT;
ALTER TABLE "AssignmentCompletion" ADD COLUMN IF NOT EXISTS "fileName" TEXT;
ALTER TABLE "AssignmentCompletion" ADD COLUMN IF NOT EXISTS "fileData" TEXT;
