-- Schools programme: classes with join codes.
--
-- Two new tables only — nothing on existing tables — so no live query can be
-- affected. Applied to production before the code deploys, per the standing
-- schema-safety rule. Classes are admin-created for the pilot phase; the
-- teacher is stored as prose (name/contact) rather than a User because pilot
-- teachers may not have accounts yet.

CREATE TABLE "SchoolClass" (
  "id"          TEXT NOT NULL PRIMARY KEY,
  -- The join code students type. Short, human, unique.
  "code"        TEXT NOT NULL UNIQUE,
  "name"        TEXT NOT NULL,
  "school"      TEXT NOT NULL,
  "teacherName" TEXT NOT NULL,
  "teacherEmail" TEXT,
  -- Set when a teacher gets a real account and should see the dashboard.
  "teacherUserId" TEXT REFERENCES "User"("id") ON DELETE SET NULL,
  "isArchived"  BOOLEAN NOT NULL DEFAULT false,
  "createdAt"   TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX "SchoolClass_teacherUserId_idx" ON "SchoolClass"("teacherUserId");

CREATE TABLE "ClassMembership" (
  "id"       TEXT NOT NULL PRIMARY KEY,
  "classId"  TEXT NOT NULL REFERENCES "SchoolClass"("id") ON DELETE CASCADE,
  "userId"   TEXT NOT NULL REFERENCES "User"("id") ON DELETE CASCADE,
  "joinedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "ClassMembership_classId_userId_key" UNIQUE ("classId", "userId")
);

CREATE INDEX "ClassMembership_userId_idx" ON "ClassMembership"("userId");
