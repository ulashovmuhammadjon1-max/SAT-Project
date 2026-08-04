-- Onboarding profile fields (collected by the pre-signup wizard at /onboarding).
--
-- This project uses `prisma db push` rather than a migrations history, so this
-- file exists to make the production change reviewable and repeatable. It is
-- fully idempotent — running it twice is a no-op — so it is safe to re-run.
--
-- Apply with either:
--   psql "$DATABASE_URL" -f prisma/migrations/manual/001_onboarding_profile.sql
--   npx prisma db push          (with DATABASE_URL pointed at production)

DO $$ BEGIN
  CREATE TYPE "OnboardingGoal" AS ENUM (
    'IMPROVE_SCORE', 'FIRST_SAT', 'RETAKING', 'COLLEGE_ADMISSIONS'
  );
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

DO $$ BEGIN
  CREATE TYPE "GradeLevel" AS ENUM (
    'GRADE_9', 'GRADE_10', 'GRADE_11', 'GRADE_12', 'GAP_YEAR', 'COLLEGE', 'OTHER'
  );
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

DO $$ BEGIN
  CREATE TYPE "DailyGoalType" AS ENUM ('QUESTIONS', 'MINUTES');
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "onboardingGoal"     "OnboardingGoal";
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "currentScore"       INTEGER;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "targetScore"        INTEGER;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "dreamUniversities"  TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[];
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "countryCode"        TEXT;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "gradeLevel"         "GradeLevel";
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "satDate"            TIMESTAMP(3);
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "strongestSection"   TEXT;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "weakestArea"        TEXT;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "studyMinutesPerDay" INTEGER;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "dailyGoalType"      "DailyGoalType";
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "dailyGoalValue"     INTEGER;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "onboardedAt"        TIMESTAMP(3);

CREATE INDEX IF NOT EXISTS "User_countryCode_idx" ON "User"("countryCode");
CREATE INDEX IF NOT EXISTS "User_gradeLevel_idx"  ON "User"("gradeLevel");
CREATE INDEX IF NOT EXISTS "User_onboardedAt_idx" ON "User"("onboardedAt");
