-- Track SAT tutor AI usage for rate limiting (free tier: 5 requests/day per user)
CREATE TABLE "TutorUsage" (
  "id" TEXT NOT NULL PRIMARY KEY,
  "userId" TEXT NOT NULL,
  "date" DATE NOT NULL,
  "requestCount" INTEGER NOT NULL DEFAULT 0,
  "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "TutorUsage_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User" ("id") ON DELETE CASCADE
);

CREATE UNIQUE INDEX "TutorUsage_userId_date_key" ON "TutorUsage"("userId", "date");
CREATE INDEX "TutorUsage_userId_idx" ON "TutorUsage"("userId");
