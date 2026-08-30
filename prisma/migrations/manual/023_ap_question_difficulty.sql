-- AP question difficulty, and the counters it is derived from.
--
-- The AP banks were authored topic by topic with no difficulty label, so there
-- are 8,700 live questions with no honest way to rate them. Inventing labels
-- would be worse than having none: a filter that claims to give a student HARD
-- questions and hands them a random sample teaches nothing and quietly erodes
-- trust in every other number on the page.
--
-- So difficulty comes from two sources, in order of preference.
--
-- 1. "difficulty" — an author-declared label, when the module carries one.
--    New content can set it; nothing existing is back-filled with a guess.
--
-- 2. timesAnswered / timesCorrect — the empirical record. Once a question has
--    been answered enough times, its observed success rate IS its difficulty,
--    and it is a better measure than an author's guess because it reflects the
--    students actually sitting the course. Below the threshold a question
--    reports as unrated rather than pretending.
--
-- The counters are incremented where attempts are recorded, so they cost one
-- update on a path that is already writing.

ALTER TABLE "ApQuestion"
    ADD COLUMN IF NOT EXISTS "difficulty" TEXT;

ALTER TABLE "ApQuestion"
    ADD COLUMN IF NOT EXISTS "timesAnswered" INTEGER NOT NULL DEFAULT 0;

ALTER TABLE "ApQuestion"
    ADD COLUMN IF NOT EXISTS "timesCorrect" INTEGER NOT NULL DEFAULT 0;

-- Filtering a topic by difficulty is the query this exists for.
CREATE INDEX IF NOT EXISTS "ApQuestion_subject_difficulty_idx"
    ON "ApQuestion"("subject", "difficulty");

-- Backfill the counters from the attempts already recorded, so the empirical
-- signal starts from the real history rather than from zero. Only the LATEST
-- attempt per (user, question) counts: a student who retries a question until
-- they get it right should not make it look easy.
WITH latest AS (
    SELECT DISTINCT ON ("userId", "questionId")
        "userId",
        "questionId",
        "isCorrect"
    FROM "ApQuestionAttempt"
    ORDER BY "userId", "questionId", "createdAt" DESC
),
agg AS (
    SELECT "questionId",
           COUNT(*)::int              AS answered,
           SUM(CASE WHEN "isCorrect" THEN 1 ELSE 0 END)::int AS correct
    FROM latest
    GROUP BY "questionId"
)
UPDATE "ApQuestion" q
SET "timesAnswered" = agg.answered,
    "timesCorrect"  = agg.correct
FROM agg
WHERE q.id = agg."questionId";
