-- 030: free diagnostic test, offered at the end of sign-up.
-- New table only; nothing existing changes. Applied to production before the code.

-- CreateEnum
CREATE TYPE "DiagnosticKind" AS ENUM ('SAT', 'IELTS');

-- CreateTable
CREATE TABLE "DiagnosticTest" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "kind" "DiagnosticKind" NOT NULL,
    "requestedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "startedAt" TIMESTAMP(3),
    "completedAt" TIMESTAMP(3),
    "questionIds" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "ieltsPartId" TEXT,
    "result" JSONB,

    CONSTRAINT "DiagnosticTest_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "DiagnosticTest_userId_kind_key" ON "DiagnosticTest"("userId", "kind");

-- AddForeignKey
ALTER TABLE "DiagnosticTest" ADD CONSTRAINT "DiagnosticTest_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

