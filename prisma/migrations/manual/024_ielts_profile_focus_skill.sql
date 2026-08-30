-- Repair schema drift that was breaking every IELTS page.
--
-- IeltsStudentProfile.focusSkill exists in schema.prisma but was never added to
-- the deployed database. Vercel rebuilds the Prisma client from schema.prisma
-- on every deploy, so the client asks for a column the database does not have,
-- and `prisma.ieltsStudentProfile.findUnique({ where })` — a whole-row fetch
-- with no explicit select — throws P2022. Nothing catches it, so it reaches a
-- logged-in student as a generic error boundary.
--
-- Both readers of this model take that path: src/lib/ielts/dashboard.ts and
-- src/lib/ielts/plan.ts, which is why the IELTS section was down rather than
-- one page of it.
--
-- This is the third time this exact failure has hit production (see the SCHEMA
-- CHANGES section of CLAUDE.md for the previous two). The column is nullable,
-- so adding it is safe on a live table and needs no backfill.

ALTER TABLE "IeltsStudentProfile"
    ADD COLUMN IF NOT EXISTS "focusSkill" TEXT;
