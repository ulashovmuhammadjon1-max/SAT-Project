-- 011_exam_modes.sql
--
-- SAT and IELTS as two exam ecosystems under one account.
--
-- Unlike 010, this DOES add columns to an existing table (`User`), which is
-- the case CLAUDE.md records as having taken production down twice: the moment
-- schema.prisma names a column the database lacks, every whole-row `User`
-- fetch in the app starts asking for it and Prisma throws P2022 at a logged-in
-- student. So this must be applied BEFORE the schema change reaches the
-- deployed branch.
--
-- Every column has a DEFAULT, so existing rows are valid the instant they are
-- added. The default is SAT-only, which is what makes this safe for the whole
-- current userbase: every account that existed before this keeps exactly the
-- dashboard it had, with no backfill and no onboarding replay.

CREATE TYPE "ExamKind" AS ENUM ('SAT', 'IELTS');
CREATE TYPE "ExamMode" AS ENUM ('SAT', 'IELTS', 'BOTH');
CREATE TYPE "ExamPriority" AS ENUM ('SAT', 'IELTS', 'EQUAL');

ALTER TABLE "User"
  ADD COLUMN IF NOT EXISTS "preparationExams" "ExamKind"[] NOT NULL DEFAULT ARRAY['SAT']::"ExamKind"[],
  ADD COLUMN IF NOT EXISTS "activeExam" "ExamMode" NOT NULL DEFAULT 'SAT',
  ADD COLUMN IF NOT EXISTS "examPriority" "ExamPriority" NOT NULL DEFAULT 'EQUAL';

CREATE TABLE IF NOT EXISTS "IeltsStudentProfile" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "targetBand" DOUBLE PRECISION,
    "examDate" TIMESTAMP(3),
    "reason" TEXT,
    "currentListening" DOUBLE PRECISION,
    "currentReading" DOUBLE PRECISION,
    "currentWriting" DOUBLE PRECISION,
    "currentSpeaking" DOUBLE PRECISION,
    "currentOverall" DOUBLE PRECISION,
    "levelSource" TEXT,
    "studyMinutesPerDay" INTEGER,
    "onboardedAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "IeltsStudentProfile_pkey" PRIMARY KEY ("id")
);

CREATE UNIQUE INDEX IF NOT EXISTS "IeltsStudentProfile_userId_key" ON "IeltsStudentProfile"("userId");

ALTER TABLE "IeltsStudentProfile"
  ADD CONSTRAINT "IeltsStudentProfile_userId_fkey"
  FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
