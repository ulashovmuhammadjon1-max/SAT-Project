-- AP prep: its own light question store, separate from the SAT Question
-- Bank on purpose — AP questions carry five choices, a unit/topic taxonomy,
-- and no Domain/Skill rows, so bolting them onto the SAT schema would bend
-- both. Applied to production before the code deploys.

CREATE TABLE IF NOT EXISTS "ApQuestion" (
  "id"           TEXT NOT NULL PRIMARY KEY,
  -- 'MICRO' | 'MACRO' | 'CALC_AB' | 'CALC_BC'
  "subject"      TEXT NOT NULL,
  "unit"         INTEGER NOT NULL,
  -- CED topic code, e.g. '1.1', and its display title
  "topic"        TEXT NOT NULL,
  "topicTitle"   TEXT NOT NULL,
  "order"        INTEGER NOT NULL DEFAULT 0,
  "stem"         TEXT NOT NULL,
  -- Optional data table: {"headers": [...], "rows": [[...], ...]}
  "tableJson"    TEXT,
  -- Exactly five choices, A-E, as a JSON array of strings
  "choicesJson"  TEXT NOT NULL,
  "correctIndex" INTEGER NOT NULL,
  "explanation"  TEXT,
  "createdAt"    TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS "ApQuestion_subject_unit_topic_idx"
  ON "ApQuestion"("subject", "unit", "topic");

CREATE TABLE IF NOT EXISTS "ApQuestionAttempt" (
  "id"          TEXT NOT NULL PRIMARY KEY,
  "userId"      TEXT NOT NULL REFERENCES "User"("id") ON DELETE CASCADE,
  "questionId"  TEXT NOT NULL REFERENCES "ApQuestion"("id") ON DELETE CASCADE,
  "chosenIndex" INTEGER NOT NULL,
  "isCorrect"   BOOLEAN NOT NULL,
  "createdAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS "ApQuestionAttempt_userId_questionId_idx"
  ON "ApQuestionAttempt"("userId", "questionId");
