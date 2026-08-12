-- 004_community_reactions.sql
--
-- Emoji reactions on community messages, and nothing else — `editedAt` already
-- exists on CommunityMessage from 003, so editing needs no schema change.
--
--   psql "$DATABASE_URL" -f prisma/migrations/manual/004_community_reactions.sql
--
-- Safe to re-run.

-- CreateTable
CREATE TABLE IF NOT EXISTS "CommunityReaction" (
    "id" TEXT NOT NULL,
    "messageId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "emoji" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityReaction_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX IF NOT EXISTS "CommunityReaction_messageId_idx" ON "CommunityReaction"("messageId");

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "CommunityReaction_messageId_userId_emoji_key" ON "CommunityReaction"("messageId", "userId", "emoji");

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityReaction" ADD CONSTRAINT "CommunityReaction_messageId_fkey" FOREIGN KEY ("messageId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityReaction" ADD CONSTRAINT "CommunityReaction_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

