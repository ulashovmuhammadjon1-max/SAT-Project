-- IELTS Writing Task 2 — Band 8+ model-essay library ("Essay Analyzer").
--
-- The two product rules that must not be bypassable from a form are enforced
-- here as CHECK constraints: Task 2 only, and Band 8.0/8.5/9.0 only. A rule
-- that lives only in the UI is a preference, not a constraint.

CREATE TYPE "IeltsEssayStatus" AS ENUM ('DRAFT', 'ANALYZING', 'NEEDS_REVIEW', 'READY', 'PUBLISHED');
CREATE TYPE "IeltsEssayAnnotationCategory" AS ENUM ('GRAMMAR', 'VOCABULARY', 'COHESION', 'COLLOCATION');
CREATE TYPE "IeltsAnnotationSource" AS ENUM ('AI', 'ADMIN');

CREATE TABLE "IeltsEssay" (
  "id"               TEXT NOT NULL PRIMARY KEY,
  "title"            TEXT NOT NULL,
  "question"         TEXT NOT NULL,
  "essayText"        TEXT NOT NULL,
  "taskType"         TEXT NOT NULL DEFAULT 'TASK_2',
  "band"             DOUBLE PRECISION NOT NULL,
  "topic"            TEXT NOT NULL,
  "subtopic"         TEXT,
  "tags"             TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  "status"           "IeltsEssayStatus" NOT NULL DEFAULT 'DRAFT',
  "analyzedTextHash" TEXT,
  "analysisError"    TEXT,
  "wordCount"        INTEGER NOT NULL DEFAULT 0,
  "publishedAt"      TIMESTAMP(3),
  "createdById"      TEXT,
  "createdAt"        TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"        TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

  -- Band 8+ only. The library's whole promise is that everything in it is a
  -- Band 8+ model answer; a 7.5 slipping in makes every badge on the site a
  -- lie, so the database refuses it.
  CONSTRAINT "IeltsEssay_band_check" CHECK ("band" IN (8.0, 8.5, 9.0)),
  -- Task 2 only.
  CONSTRAINT "IeltsEssay_taskType_check" CHECK ("taskType" = 'TASK_2'),

  CONSTRAINT "IeltsEssay_createdById_fkey" FOREIGN KEY ("createdById")
    REFERENCES "User" ("id") ON DELETE SET NULL
);

CREATE INDEX "IeltsEssay_status_band_idx"  ON "IeltsEssay" ("status", "band");
CREATE INDEX "IeltsEssay_topic_idx"        ON "IeltsEssay" ("topic");
CREATE INDEX "IeltsEssay_publishedAt_idx"  ON "IeltsEssay" ("publishedAt");

CREATE TABLE "IeltsEssayAnnotation" (
  "id"          TEXT NOT NULL PRIMARY KEY,
  "essayId"     TEXT NOT NULL,
  "category"    "IeltsEssayAnnotationCategory" NOT NULL,
  "subtype"     TEXT NOT NULL,
  "quote"       TEXT NOT NULL,
  "startOffset" INTEGER NOT NULL,
  "endOffset"   INTEGER NOT NULL,
  "explanation" TEXT NOT NULL,
  "ieltsValue"  TEXT,
  "pattern"     TEXT,
  "confidence"  DOUBLE PRECISION,
  "source"      "IeltsAnnotationSource" NOT NULL DEFAULT 'AI',
  "reviewed"    BOOLEAN NOT NULL DEFAULT false,
  "createdAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

  -- A zero-width or reversed span cannot be rendered as a highlight.
  CONSTRAINT "IeltsEssayAnnotation_span_check" CHECK ("endOffset" > "startOffset"),
  CONSTRAINT "IeltsEssayAnnotation_start_check" CHECK ("startOffset" >= 0),

  CONSTRAINT "IeltsEssayAnnotation_essayId_fkey" FOREIGN KEY ("essayId")
    REFERENCES "IeltsEssay" ("id") ON DELETE CASCADE
);

CREATE INDEX "IeltsEssayAnnotation_essayId_category_idx" ON "IeltsEssayAnnotation" ("essayId", "category");
CREATE INDEX "IeltsEssayAnnotation_essayId_start_idx"    ON "IeltsEssayAnnotation" ("essayId", "startOffset");

CREATE TABLE "IeltsEssayIdea" (
  "id"          TEXT NOT NULL PRIMARY KEY,
  "essayId"     TEXT NOT NULL,
  "claim"       TEXT NOT NULL,
  "explanation" TEXT NOT NULL,
  "consequence" TEXT,
  "example"     TEXT,
  "startOffset" INTEGER,
  "endOffset"   INTEGER,
  "order"       INTEGER NOT NULL DEFAULT 0,
  "source"      "IeltsAnnotationSource" NOT NULL DEFAULT 'AI',
  "reviewed"    BOOLEAN NOT NULL DEFAULT false,
  "createdAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT "IeltsEssayIdea_essayId_fkey" FOREIGN KEY ("essayId")
    REFERENCES "IeltsEssay" ("id") ON DELETE CASCADE
);

CREATE INDEX "IeltsEssayIdea_essayId_idx" ON "IeltsEssayIdea" ("essayId");
