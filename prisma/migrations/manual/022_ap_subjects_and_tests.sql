-- AP Prep: personal subject selection, and practice-test attempts.
--
-- Two things the AP section could not previously express.
--
-- 1. Which AP subjects a student actually takes. The sidebar hard-coded four
--    courses for everyone, so a student taking Statistics and Psychology saw
--    Calculus BC anyway. ApSubjectEnrollment is the many-to-many between a
--    user and a subject, so the catalog can grow to thirty subjects without
--    any student's sidebar growing at all.
--
--    Removing a subject deletes only the enrollment row. Question attempts and
--    test attempts key on userId and the subject STRING, never on the
--    enrollment, so a student who drops a subject and picks it up months later
--    still has every answer, score and attempt they had before. That is the
--    point of keeping enrollment separate from progress.
--
-- 2. Practice-test attempts. ApTestAttempt holds one sitting of one test: the
--    frozen question order, the answers so far, which questions are marked for
--    review, and when the clock runs out. Storing the question ids at start
--    means a test the student is halfway through cannot change under them if
--    the bank is edited.

CREATE TABLE IF NOT EXISTS "ApSubjectEnrollment" (
    "id"      TEXT NOT NULL,
    -- Matches ApQuestion.subject: 'MICRO' | 'MACRO' | 'CALC_AB' | 'CALC_BC' |
    -- 'STATISTICS' | 'PSYCHOLOGY' | ... Deliberately a string, like
    -- ApQuestion.subject, so adding a subject is a catalog edit and not a
    -- migration.
    "subject" TEXT NOT NULL,
    "userId"  TEXT NOT NULL,
    "addedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "ApSubjectEnrollment_pkey" PRIMARY KEY ("id")
);

-- One row per (user, subject): adding a subject twice is a no-op rather than a
-- duplicate, which lets the server action be a plain upsert.
CREATE UNIQUE INDEX IF NOT EXISTS "ApSubjectEnrollment_userId_subject_key"
    ON "ApSubjectEnrollment"("userId", "subject");
CREATE INDEX IF NOT EXISTS "ApSubjectEnrollment_userId_idx"
    ON "ApSubjectEnrollment"("userId");

DO $$
BEGIN
    ALTER TABLE "ApSubjectEnrollment"
        ADD CONSTRAINT "ApSubjectEnrollment_userId_fkey"
        FOREIGN KEY ("userId") REFERENCES "User"("id")
        ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS "ApTestAttempt" (
    "id"              TEXT NOT NULL,
    "userId"          TEXT NOT NULL,
    "subject"         TEXT NOT NULL,
    -- Identifies the test within its subject, e.g. 'practice-1'. Tests are
    -- defined in the catalog, not in the database, so this is a slug.
    "testSlug"        TEXT NOT NULL,
    -- 'IN_PROGRESS' | 'SUBMITTED'
    "status"          TEXT NOT NULL DEFAULT 'IN_PROGRESS',
    -- The question order frozen at start: a JSON array of ApQuestion ids.
    "questionIdsJson" TEXT NOT NULL,
    -- {"<questionId>": <chosenIndex>} — answers persist across navigation and
    -- across a reload, since a student who loses their connection mid-exam
    -- must not lose the sitting.
    "answersJson"     TEXT NOT NULL DEFAULT '{}',
    -- ["<questionId>", ...] flagged for review.
    "markedJson"      TEXT NOT NULL DEFAULT '[]',
    "startedAt"       TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -- When the clock expires. Computed server-side at start from the test's
    -- configured duration, so the timer cannot be extended from the browser.
    "expiresAt"       TIMESTAMP(3),
    "submittedAt"     TIMESTAMP(3),
    "score"           INTEGER,
    "total"           INTEGER,
    CONSTRAINT "ApTestAttempt_pkey" PRIMARY KEY ("id")
);

CREATE INDEX IF NOT EXISTS "ApTestAttempt_userId_subject_idx"
    ON "ApTestAttempt"("userId", "subject");
CREATE INDEX IF NOT EXISTS "ApTestAttempt_userId_status_idx"
    ON "ApTestAttempt"("userId", "status");

DO $$
BEGIN
    ALTER TABLE "ApTestAttempt"
        ADD CONSTRAINT "ApTestAttempt_userId_fkey"
        FOREIGN KEY ("userId") REFERENCES "User"("id")
        ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

-- Backfill: until now every student saw the same four AP courses, so every
-- existing user keeps exactly those four. Without this, the change would look
-- to a current student like their subjects had been taken away.
--
-- Ids are derived rather than random so re-running this migration is a no-op
-- instead of a second set of rows.
INSERT INTO "ApSubjectEnrollment" ("id", "userId", "subject", "addedAt")
SELECT
    'apenr_' || substr(md5(u."id" || '|' || s.subject), 1, 20),
    u."id",
    s.subject,
    CURRENT_TIMESTAMP
FROM "User" u
CROSS JOIN (VALUES ('MACRO'), ('MICRO'), ('CALC_AB'), ('CALC_BC')) AS s(subject)
ON CONFLICT ("userId", "subject") DO NOTHING;
