-- Class assignments for the teacher panel. New tables only; applied to
-- production before the code deploys.

CREATE TABLE "ClassAssignment" (
  "id"           TEXT NOT NULL PRIMARY KEY,
  "classId"      TEXT NOT NULL REFERENCES "SchoolClass"("id") ON DELETE CASCADE,
  "title"        TEXT NOT NULL,
  "instructions" TEXT,
  -- Linked practice test: completion is then derived from a submitted
  -- attempt rather than self-reported. NULL = a free-form task students
  -- tick off themselves.
  "testId"       TEXT REFERENCES "Test"("id") ON DELETE SET NULL,
  "dueAt"        TIMESTAMP(3),
  "createdAt"    TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX "ClassAssignment_classId_idx" ON "ClassAssignment"("classId");

-- Self-reported completion for free-form tasks.
CREATE TABLE "AssignmentCompletion" (
  "id"           TEXT NOT NULL PRIMARY KEY,
  "assignmentId" TEXT NOT NULL REFERENCES "ClassAssignment"("id") ON DELETE CASCADE,
  "userId"       TEXT NOT NULL REFERENCES "User"("id") ON DELETE CASCADE,
  "completedAt"  TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "AssignmentCompletion_assignmentId_userId_key" UNIQUE ("assignmentId", "userId")
);

CREATE INDEX "AssignmentCompletion_userId_idx" ON "AssignmentCompletion"("userId");
