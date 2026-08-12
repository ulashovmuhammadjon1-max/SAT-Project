-- 003_community_chat.sql
--
-- Community chat: channels, messages with threaded replies, attachments,
-- mentions, and per-student read markers.
--
-- Written by hand into prisma/migrations/manual/ to match this project's
-- convention (Prisma's own migrate history is not used here). Apply to
-- production with:
--
--   psql "$DATABASE_URL" -f prisma/migrations/manual/003_community_chat.sql
--
-- Every statement is IF NOT EXISTS or guarded, so re-running it is safe.

-- CreateEnum
DO $$ BEGIN
    CREATE TYPE "CommunityAttachmentKind" AS ENUM ('IMAGE', 'PDF', 'FILE');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- CreateTable
CREATE TABLE IF NOT EXISTS "CommunityChannel" (
    "id" TEXT NOT NULL,
    "slug" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "order" INTEGER NOT NULL DEFAULT 0,
    "isReadOnly" BOOLEAN NOT NULL DEFAULT false,
    "isArchived" BOOLEAN NOT NULL DEFAULT false,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityChannel_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE IF NOT EXISTS "CommunityMessage" (
    "id" TEXT NOT NULL,
    "channelId" TEXT NOT NULL,
    "authorId" TEXT NOT NULL,
    "body" TEXT NOT NULL,
    "replyToId" TEXT,
    "editedAt" TIMESTAMP(3),
    "deletedAt" TIMESTAMP(3),
    "deletedById" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityMessage_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE IF NOT EXISTS "CommunityAttachment" (
    "id" TEXT NOT NULL,
    "messageId" TEXT NOT NULL,
    "kind" "CommunityAttachmentKind" NOT NULL,
    "url" TEXT NOT NULL,
    "fileName" TEXT NOT NULL,
    "contentType" TEXT NOT NULL,
    "sizeBytes" INTEGER NOT NULL,

    CONSTRAINT "CommunityAttachment_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE IF NOT EXISTS "CommunityMention" (
    "id" TEXT NOT NULL,
    "messageId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,

    CONSTRAINT "CommunityMention_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE IF NOT EXISTS "CommunityRead" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "channelId" TEXT NOT NULL,
    "lastReadAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityRead_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "CommunityChannel_slug_key" ON "CommunityChannel"("slug");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "CommunityChannel_isArchived_order_idx" ON "CommunityChannel"("isArchived", "order");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "CommunityMessage_channelId_createdAt_idx" ON "CommunityMessage"("channelId", "createdAt");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "CommunityMessage_authorId_idx" ON "CommunityMessage"("authorId");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "CommunityAttachment_messageId_idx" ON "CommunityAttachment"("messageId");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "CommunityMention_userId_idx" ON "CommunityMention"("userId");

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "CommunityMention_messageId_userId_key" ON "CommunityMention"("messageId", "userId");

-- CreateIndex
CREATE UNIQUE INDEX IF NOT EXISTS "CommunityRead_userId_channelId_key" ON "CommunityRead"("userId", "channelId");

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityMessage" ADD CONSTRAINT "CommunityMessage_replyToId_fkey" FOREIGN KEY ("replyToId") REFERENCES "CommunityMessage"("id") ON DELETE SET NULL ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityMessage" ADD CONSTRAINT "CommunityMessage_channelId_fkey" FOREIGN KEY ("channelId") REFERENCES "CommunityChannel"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityMessage" ADD CONSTRAINT "CommunityMessage_authorId_fkey" FOREIGN KEY ("authorId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityAttachment" ADD CONSTRAINT "CommunityAttachment_messageId_fkey" FOREIGN KEY ("messageId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityMention" ADD CONSTRAINT "CommunityMention_messageId_fkey" FOREIGN KEY ("messageId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityMention" ADD CONSTRAINT "CommunityMention_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityRead" ADD CONSTRAINT "CommunityRead_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- AddForeignKey
DO $$ BEGIN
    ALTER TABLE "CommunityRead" ADD CONSTRAINT "CommunityRead_channelId_fkey" FOREIGN KEY ("channelId") REFERENCES "CommunityChannel"("id") ON DELETE CASCADE ON UPDATE CASCADE;
EXCEPTION WHEN duplicate_object THEN NULL; END $$;


-- Seed the default channels. ON CONFLICT keeps a re-run from duplicating them
-- and from clobbering a name an admin has since edited.
INSERT INTO "CommunityChannel" ("id", "slug", "name", "description", "order", "isReadOnly")
VALUES
  ('chan_general',  'general',  'General',            'Anything SAT — introductions, study plans, motivation.', 1, false),
  ('chan_math',     'math',     'Math help',          'Stuck on a question? Post a screenshot and ask.',        2, false),
  ('chan_rw',       'reading-writing', 'Reading & Writing help', 'Grammar rules, passages, vocabulary.',        3, false),
  ('chan_resources','resources','Resources',          'Share notes, PDFs and anything that helped you.',        4, false),
  ('chan_announce', 'announcements', 'Announcements', 'Updates from the SATForge team.',                        0, true)
ON CONFLICT ("slug") DO NOTHING;
