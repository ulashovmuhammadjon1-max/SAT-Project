-- Named question collections, so a bulk import stays distinguishable from the
-- existing bank.
--
-- Idempotent, like every migration in this directory. Keep semicolons out of
-- comments here -- the runner splits on semicolons outside dollar-quotes.

CREATE TABLE IF NOT EXISTS "QuestionCollection" (
  "id"          TEXT NOT NULL,
  "name"        TEXT NOT NULL,
  "slug"        TEXT NOT NULL,
  "description" TEXT,
  "origin"      TEXT,
  "order"       INTEGER NOT NULL DEFAULT 0,
  "createdAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "QuestionCollection_pkey" PRIMARY KEY ("id")
);

-- The slug is what importers look a collection up by, so it has to be unique.
CREATE UNIQUE INDEX IF NOT EXISTS "QuestionCollection_slug_key"
  ON "QuestionCollection"("slug");

CREATE INDEX IF NOT EXISTS "QuestionCollection_order_idx"
  ON "QuestionCollection"("order");

ALTER TABLE "Question" ADD COLUMN IF NOT EXISTS "collectionId" TEXT;

-- Every existing question stays NULL, which is exactly the intended reading --
-- NULL means "the original bank", and only imported batches carry a collection.
CREATE INDEX IF NOT EXISTS "Question_collectionId_idx"
  ON "Question"("collectionId");

-- ON DELETE SET NULL, matching the moduleId relation: dropping a collection
-- must never cascade into deleting student-visible questions and their
-- attempt history. Emptying a batch is a deliberate, separate action.
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint WHERE conname = 'Question_collectionId_fkey'
  ) THEN
    ALTER TABLE "Question"
      ADD CONSTRAINT "Question_collectionId_fkey"
      FOREIGN KEY ("collectionId") REFERENCES "QuestionCollection"("id")
      ON DELETE SET NULL ON UPDATE CASCADE;
  END IF;
END $$;
