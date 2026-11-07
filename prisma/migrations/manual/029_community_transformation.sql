-- 029: Community transformation.
--
-- Purely additive: new columns are nullable or defaulted, new tables are new.
-- No existing channel, message, attachment, mention, reaction or read row is
-- changed except that existing channels are placed into categories and given
-- icons at the end of this file.
--
--   CommunityChannel   + categoryId, icon, slowModeSeconds
--   CommunityMessage   + kind, title, subject, linkUrl, threadRootId, replyCount,
--                        lastReplyAt, acceptedAnswerId, pinnedAt, pinnedById, pollClosedAt
--   CommunityRead      + mutedAt
--   new: CommunityCategory, CommunityPollOption, CommunityPollVote,
--        CommunityBookmark, CommunityThreadFollow, CommunityNotification,
--        CommunityEmailDelivery, CommunityMember, CommunityPresence,
--        CommunityReport, CommunityBlock, CommunityRestriction,
--        CommunityModerationLog, CommunityConversation,
--        CommunityConversationMember, CommunityDirectMessage
--
-- Generated with `prisma migrate diff` from the previous schema, then the
-- category/channel seed appended by hand.

-- CreateEnum
CREATE TYPE "CommunityMessageKind" AS ENUM ('MESSAGE', 'QUESTION', 'RESOURCE', 'ACHIEVEMENT', 'POLL', 'ANNOUNCEMENT');

-- CreateEnum
CREATE TYPE "CommunityFollowState" AS ENUM ('FOLLOWING', 'MUTED');

-- CreateEnum
CREATE TYPE "CommunityNotificationType" AS ENUM ('REPLY', 'MENTION', 'REACTION', 'THREAD_REPLY', 'ANSWER', 'ANSWER_ACCEPTED', 'ANNOUNCEMENT', 'DIRECT_MESSAGE', 'MODERATION');

-- CreateEnum
CREATE TYPE "CommunityEmailStatus" AS ENUM ('PENDING', 'SENDING', 'SENT', 'SKIPPED', 'FAILED');

-- CreateEnum
CREATE TYPE "CommunityDmPolicy" AS ENUM ('EVERYONE', 'NOBODY');

-- CreateEnum
CREATE TYPE "CommunityReportReason" AS ENUM ('SPAM', 'HARASSMENT', 'INAPPROPRIATE', 'MISINFORMATION', 'OTHER');

-- CreateEnum
CREATE TYPE "CommunityReportStatus" AS ENUM ('OPEN', 'DISMISSED', 'ACTIONED');

-- AlterTable
ALTER TABLE "CommunityChannel" ADD COLUMN     "categoryId" TEXT,
ADD COLUMN     "icon" TEXT NOT NULL DEFAULT 'hash',
ADD COLUMN     "slowModeSeconds" INTEGER NOT NULL DEFAULT 0;

-- AlterTable
ALTER TABLE "CommunityMessage" ADD COLUMN     "acceptedAnswerId" TEXT,
ADD COLUMN     "kind" "CommunityMessageKind" NOT NULL DEFAULT 'MESSAGE',
ADD COLUMN     "lastReplyAt" TIMESTAMP(3),
ADD COLUMN     "linkUrl" TEXT,
ADD COLUMN     "pinnedAt" TIMESTAMP(3),
ADD COLUMN     "pinnedById" TEXT,
ADD COLUMN     "pollClosedAt" TIMESTAMP(3),
ADD COLUMN     "replyCount" INTEGER NOT NULL DEFAULT 0,
ADD COLUMN     "subject" TEXT,
ADD COLUMN     "threadRootId" TEXT,
ADD COLUMN     "title" TEXT;

-- AlterTable
ALTER TABLE "CommunityRead" ADD COLUMN     "mutedAt" TIMESTAMP(3);

-- CreateTable
CREATE TABLE "CommunityCategory" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "order" INTEGER NOT NULL DEFAULT 0,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityCategory_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityPollOption" (
    "id" TEXT NOT NULL,
    "messageId" TEXT NOT NULL,
    "label" TEXT NOT NULL,
    "order" INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT "CommunityPollOption_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityPollVote" (
    "id" TEXT NOT NULL,
    "messageId" TEXT NOT NULL,
    "optionId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityPollVote_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityBookmark" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "messageId" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityBookmark_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityThreadFollow" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "rootId" TEXT NOT NULL,
    "state" "CommunityFollowState" NOT NULL DEFAULT 'FOLLOWING',
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityThreadFollow_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityNotification" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "type" "CommunityNotificationType" NOT NULL,
    "actorId" TEXT,
    "messageId" TEXT,
    "channelId" TEXT,
    "conversationId" TEXT,
    "title" TEXT NOT NULL,
    "body" TEXT NOT NULL,
    "url" TEXT NOT NULL,
    "dedupeKey" TEXT NOT NULL,
    "readAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityNotification_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityEmailDelivery" (
    "id" TEXT NOT NULL,
    "notificationId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "status" "CommunityEmailStatus" NOT NULL DEFAULT 'PENDING',
    "sendAfter" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "attempts" INTEGER NOT NULL DEFAULT 0,
    "lastAttemptAt" TIMESTAMP(3),
    "lastError" TEXT,
    "skipReason" TEXT,
    "provider" TEXT,
    "sentAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityEmailDelivery_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityMember" (
    "userId" TEXT NOT NULL,
    "bio" TEXT,
    "interests" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "helpsWith" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "studying" TEXT[] DEFAULT ARRAY[]::TEXT[],
    "emailReplies" BOOLEAN NOT NULL DEFAULT true,
    "emailMentions" BOOLEAN NOT NULL DEFAULT true,
    "emailDirect" BOOLEAN NOT NULL DEFAULT true,
    "emailActivity" BOOLEAN NOT NULL DEFAULT false,
    "emailAnnouncements" BOOLEAN NOT NULL DEFAULT false,
    "emailDigest" BOOLEAN NOT NULL DEFAULT false,
    "dmPolicy" "CommunityDmPolicy" NOT NULL DEFAULT 'EVERYONE',
    "showPresence" BOOLEAN NOT NULL DEFAULT true,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "CommunityMember_pkey" PRIMARY KEY ("userId")
);

-- CreateTable
CREATE TABLE "CommunityPresence" (
    "userId" TEXT NOT NULL,
    "lastSeenAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "lastActiveAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityPresence_pkey" PRIMARY KEY ("userId")
);

-- CreateTable
CREATE TABLE "CommunityReport" (
    "id" TEXT NOT NULL,
    "reporterId" TEXT NOT NULL,
    "messageId" TEXT,
    "directMessageId" TEXT,
    "targetUserId" TEXT,
    "reason" "CommunityReportReason" NOT NULL,
    "details" TEXT,
    "status" "CommunityReportStatus" NOT NULL DEFAULT 'OPEN',
    "reviewedById" TEXT,
    "reviewedAt" TIMESTAMP(3),
    "resolution" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityReport_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityBlock" (
    "id" TEXT NOT NULL,
    "blockerId" TEXT NOT NULL,
    "blockedId" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityBlock_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityRestriction" (
    "userId" TEXT NOT NULL,
    "until" TIMESTAMP(3) NOT NULL,
    "reason" TEXT NOT NULL,
    "createdById" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityRestriction_pkey" PRIMARY KEY ("userId")
);

-- CreateTable
CREATE TABLE "CommunityModerationLog" (
    "id" TEXT NOT NULL,
    "actorId" TEXT NOT NULL,
    "action" TEXT NOT NULL,
    "targetUserId" TEXT,
    "messageId" TEXT,
    "reportId" TEXT,
    "note" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityModerationLog_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityConversation" (
    "id" TEXT NOT NULL,
    "pairKey" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "lastMessageAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityConversation_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityConversationMember" (
    "id" TEXT NOT NULL,
    "conversationId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "lastReadAt" TIMESTAMP(3),
    "mutedAt" TIMESTAMP(3),

    CONSTRAINT "CommunityConversationMember_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommunityDirectMessage" (
    "id" TEXT NOT NULL,
    "conversationId" TEXT NOT NULL,
    "authorId" TEXT NOT NULL,
    "body" TEXT NOT NULL,
    "replyToId" TEXT,
    "attachments" JSONB,
    "editedAt" TIMESTAMP(3),
    "deletedAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommunityDirectMessage_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "CommunityPollOption_messageId_idx" ON "CommunityPollOption"("messageId");

-- CreateIndex
CREATE INDEX "CommunityPollVote_optionId_idx" ON "CommunityPollVote"("optionId");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityPollVote_messageId_userId_key" ON "CommunityPollVote"("messageId", "userId");

-- CreateIndex
CREATE INDEX "CommunityBookmark_userId_createdAt_idx" ON "CommunityBookmark"("userId", "createdAt");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityBookmark_userId_messageId_key" ON "CommunityBookmark"("userId", "messageId");

-- CreateIndex
CREATE INDEX "CommunityThreadFollow_rootId_state_idx" ON "CommunityThreadFollow"("rootId", "state");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityThreadFollow_userId_rootId_key" ON "CommunityThreadFollow"("userId", "rootId");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityNotification_dedupeKey_key" ON "CommunityNotification"("dedupeKey");

-- CreateIndex
CREATE INDEX "CommunityNotification_userId_createdAt_idx" ON "CommunityNotification"("userId", "createdAt");

-- CreateIndex
CREATE INDEX "CommunityNotification_userId_readAt_idx" ON "CommunityNotification"("userId", "readAt");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityEmailDelivery_notificationId_key" ON "CommunityEmailDelivery"("notificationId");

-- CreateIndex
CREATE INDEX "CommunityEmailDelivery_status_sendAfter_idx" ON "CommunityEmailDelivery"("status", "sendAfter");

-- CreateIndex
CREATE INDEX "CommunityEmailDelivery_userId_status_idx" ON "CommunityEmailDelivery"("userId", "status");

-- CreateIndex
CREATE INDEX "CommunityPresence_lastActiveAt_idx" ON "CommunityPresence"("lastActiveAt");

-- CreateIndex
CREATE INDEX "CommunityReport_status_createdAt_idx" ON "CommunityReport"("status", "createdAt");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityReport_reporterId_messageId_key" ON "CommunityReport"("reporterId", "messageId");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityReport_reporterId_directMessageId_key" ON "CommunityReport"("reporterId", "directMessageId");

-- CreateIndex
CREATE INDEX "CommunityBlock_blockedId_idx" ON "CommunityBlock"("blockedId");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityBlock_blockerId_blockedId_key" ON "CommunityBlock"("blockerId", "blockedId");

-- CreateIndex
CREATE INDEX "CommunityModerationLog_createdAt_idx" ON "CommunityModerationLog"("createdAt");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityConversation_pairKey_key" ON "CommunityConversation"("pairKey");

-- CreateIndex
CREATE INDEX "CommunityConversation_lastMessageAt_idx" ON "CommunityConversation"("lastMessageAt");

-- CreateIndex
CREATE INDEX "CommunityConversationMember_userId_idx" ON "CommunityConversationMember"("userId");

-- CreateIndex
CREATE UNIQUE INDEX "CommunityConversationMember_conversationId_userId_key" ON "CommunityConversationMember"("conversationId", "userId");

-- CreateIndex
CREATE INDEX "CommunityDirectMessage_conversationId_createdAt_idx" ON "CommunityDirectMessage"("conversationId", "createdAt");

-- CreateIndex
CREATE INDEX "CommunityChannel_categoryId_idx" ON "CommunityChannel"("categoryId");

-- CreateIndex
CREATE INDEX "CommunityMessage_channelId_threadRootId_createdAt_idx" ON "CommunityMessage"("channelId", "threadRootId", "createdAt");

-- CreateIndex
CREATE INDEX "CommunityMessage_threadRootId_createdAt_idx" ON "CommunityMessage"("threadRootId", "createdAt");

-- CreateIndex
CREATE INDEX "CommunityMessage_kind_createdAt_idx" ON "CommunityMessage"("kind", "createdAt");

-- AddForeignKey
ALTER TABLE "CommunityChannel" ADD CONSTRAINT "CommunityChannel_categoryId_fkey" FOREIGN KEY ("categoryId") REFERENCES "CommunityCategory"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityMessage" ADD CONSTRAINT "CommunityMessage_threadRootId_fkey" FOREIGN KEY ("threadRootId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityPollOption" ADD CONSTRAINT "CommunityPollOption_messageId_fkey" FOREIGN KEY ("messageId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityPollVote" ADD CONSTRAINT "CommunityPollVote_optionId_fkey" FOREIGN KEY ("optionId") REFERENCES "CommunityPollOption"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityPollVote" ADD CONSTRAINT "CommunityPollVote_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityBookmark" ADD CONSTRAINT "CommunityBookmark_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityBookmark" ADD CONSTRAINT "CommunityBookmark_messageId_fkey" FOREIGN KEY ("messageId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityThreadFollow" ADD CONSTRAINT "CommunityThreadFollow_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityThreadFollow" ADD CONSTRAINT "CommunityThreadFollow_rootId_fkey" FOREIGN KEY ("rootId") REFERENCES "CommunityMessage"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityNotification" ADD CONSTRAINT "CommunityNotification_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityNotification" ADD CONSTRAINT "CommunityNotification_actorId_fkey" FOREIGN KEY ("actorId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityEmailDelivery" ADD CONSTRAINT "CommunityEmailDelivery_notificationId_fkey" FOREIGN KEY ("notificationId") REFERENCES "CommunityNotification"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityMember" ADD CONSTRAINT "CommunityMember_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityPresence" ADD CONSTRAINT "CommunityPresence_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityReport" ADD CONSTRAINT "CommunityReport_reporterId_fkey" FOREIGN KEY ("reporterId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityReport" ADD CONSTRAINT "CommunityReport_targetUserId_fkey" FOREIGN KEY ("targetUserId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityReport" ADD CONSTRAINT "CommunityReport_messageId_fkey" FOREIGN KEY ("messageId") REFERENCES "CommunityMessage"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityReport" ADD CONSTRAINT "CommunityReport_directMessageId_fkey" FOREIGN KEY ("directMessageId") REFERENCES "CommunityDirectMessage"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityBlock" ADD CONSTRAINT "CommunityBlock_blockerId_fkey" FOREIGN KEY ("blockerId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityBlock" ADD CONSTRAINT "CommunityBlock_blockedId_fkey" FOREIGN KEY ("blockedId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityRestriction" ADD CONSTRAINT "CommunityRestriction_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityConversationMember" ADD CONSTRAINT "CommunityConversationMember_conversationId_fkey" FOREIGN KEY ("conversationId") REFERENCES "CommunityConversation"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityConversationMember" ADD CONSTRAINT "CommunityConversationMember_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityDirectMessage" ADD CONSTRAINT "CommunityDirectMessage_conversationId_fkey" FOREIGN KEY ("conversationId") REFERENCES "CommunityConversation"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityDirectMessage" ADD CONSTRAINT "CommunityDirectMessage_authorId_fkey" FOREIGN KEY ("authorId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommunityDirectMessage" ADD CONSTRAINT "CommunityDirectMessage_replyToId_fkey" FOREIGN KEY ("replyToId") REFERENCES "CommunityDirectMessage"("id") ON DELETE SET NULL ON UPDATE CASCADE;


-- ---------------------------------------------------------------------------
-- Seed: categories, icons for the five existing channels, and six new
-- channels chosen for who actually uses Scholarly (SAT, IELTS, AP, research).
-- Idempotent: re-running changes nothing.
-- ---------------------------------------------------------------------------
INSERT INTO "CommunityCategory" ("id", "name", "order") VALUES
  ('ccat_scholarly', 'Scholarly', 0),
  ('ccat_general', 'General', 1),
  ('ccat_help', 'Study help', 2),
  ('ccat_resources', 'Resources', 3)
ON CONFLICT ("id") DO NOTHING;

UPDATE "CommunityChannel" SET "categoryId" = 'ccat_scholarly', "icon" = 'megaphone', "order" = 0 WHERE "slug" = 'announcements' AND "categoryId" IS NULL;
UPDATE "CommunityChannel" SET "categoryId" = 'ccat_general', "icon" = 'messages', "order" = 0 WHERE "slug" = 'general' AND "categoryId" IS NULL;
UPDATE "CommunityChannel" SET "categoryId" = 'ccat_help', "icon" = 'sigma', "order" = 0 WHERE "slug" = 'math' AND "categoryId" IS NULL;
UPDATE "CommunityChannel" SET "categoryId" = 'ccat_help', "icon" = 'book-open', "order" = 1 WHERE "slug" = 'reading-writing' AND "categoryId" IS NULL;
UPDATE "CommunityChannel" SET "categoryId" = 'ccat_resources', "icon" = 'library', "order" = 0 WHERE "slug" = 'resources' AND "categoryId" IS NULL;

INSERT INTO "CommunityChannel" ("id", "slug", "name", "description", "order", "isReadOnly", "categoryId", "icon") VALUES
  ('cch_achievements', 'achievements', 'Achievements', 'Scores, acceptances and milestones. Share yours and congratulate others.', 1, false, 'ccat_scholarly', 'trophy'),
  ('cch_feedback', 'feedback', 'Suggestions & feedback', 'Ideas and bug reports for Scholarly itself.', 2, false, 'ccat_scholarly', 'lightbulb'),
  ('cch_introductions', 'introductions', 'Introductions', 'New here? Say who you are and what you are preparing for.', 1, false, 'ccat_general', 'hand'),
  ('cch_ielts', 'ielts', 'IELTS help', 'Writing, Speaking, Reading and Listening questions.', 2, false, 'ccat_help', 'languages'),
  ('cch_ap', 'ap', 'AP courses', 'Questions on any AP subject, unit by unit.', 3, false, 'ccat_help', 'award'),
  ('cch_research', 'research', 'Research & projects', 'Research questions, methods, sources and feedback on drafts.', 4, false, 'ccat_help', 'flask')
ON CONFLICT ("slug") DO NOTHING;
