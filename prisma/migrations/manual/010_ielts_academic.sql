-- 010_ielts_academic.sql
--
-- IELTS Academic: a parallel content and attempt tree, plus a REVIEWER role.
--
-- Every statement here creates something NEW. No existing table gains or loses
-- a column, so no query anywhere in the app can start selecting a column the
-- database does not have — the failure mode CLAUDE.md records as having taken
-- production down twice. The only change to an existing object is a new value
-- on the Role enum, which is safe for reads and matters only when a row is
-- written with it.
--
-- Apply this BEFORE the schema.prisma change reaches the deployed branch.

-- Postgres will not accept a new enum value inside the same transaction that
-- adds it, so this statement runs first and alone.
ALTER TYPE "Role" ADD VALUE IF NOT EXISTS 'REVIEWER';

-- CreateEnum
CREATE TYPE "IeltsModule" AS ENUM ('ACADEMIC', 'GENERAL_TRAINING');

-- CreateEnum
CREATE TYPE "IeltsSkill" AS ENUM ('LISTENING', 'READING', 'WRITING', 'SPEAKING');

-- CreateEnum
CREATE TYPE "IeltsAttemptMode" AS ENUM ('REALISTIC', 'PRACTICE');

-- CreateEnum
CREATE TYPE "IeltsAttemptStatus" AS ENUM ('IN_PROGRESS', 'SUBMITTED', 'ABANDONED', 'AWAITING_REVIEW', 'COMPLETE');

-- CreateEnum
CREATE TYPE "IeltsQuestionType" AS ENUM ('MULTIPLE_CHOICE_SINGLE', 'MULTIPLE_CHOICE_MULTI', 'TRUE_FALSE_NOT_GIVEN', 'YES_NO_NOT_GIVEN', 'MATCHING_INFORMATION', 'MATCHING_HEADINGS', 'MATCHING_FEATURES', 'MATCHING_SENTENCE_ENDINGS', 'MATCHING_GENERAL', 'PLAN_MAP_DIAGRAM_LABEL', 'FORM_COMPLETION', 'NOTE_COMPLETION', 'TABLE_COMPLETION', 'FLOWCHART_COMPLETION', 'SUMMARY_COMPLETION', 'SENTENCE_COMPLETION', 'SHORT_ANSWER', 'DIAGRAM_LABEL_COMPLETION');

-- CreateEnum
CREATE TYPE "IeltsTestStatus" AS ENUM ('DRAFT', 'PUBLISHED', 'ARCHIVED');

-- CreateEnum
CREATE TYPE "IeltsReviewStatus" AS ENUM ('PENDING', 'ASSIGNED', 'IN_REVIEW', 'COMPLETE', 'RETURNED');

-- CreateTable
CREATE TABLE "IeltsTest" (
    "id" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "slug" TEXT NOT NULL,
    "module" "IeltsModule" NOT NULL DEFAULT 'ACADEMIC',
    "status" "IeltsTestStatus" NOT NULL DEFAULT 'DRAFT',
    "description" TEXT,
    "difficulty" INTEGER NOT NULL DEFAULT 3,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "IeltsTest_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsSection" (
    "id" TEXT NOT NULL,
    "testId" TEXT NOT NULL,
    "skill" "IeltsSkill" NOT NULL,
    "order" INTEGER NOT NULL DEFAULT 0,
    "durationMinutes" INTEGER NOT NULL,
    "instructions" TEXT,

    CONSTRAINT "IeltsSection_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsPart" (
    "id" TEXT NOT NULL,
    "sectionId" TEXT NOT NULL,
    "partNumber" INTEGER NOT NULL,
    "title" TEXT,
    "instructions" TEXT,
    "passageHtml" TEXT,
    "promptHtml" TEXT,
    "imageUrl" TEXT,
    "imageAlt" TEXT,
    "audioUrl" TEXT,
    "audioDuration" INTEGER,
    "transcript" TEXT,
    "prepSeconds" INTEGER,
    "speakSeconds" INTEGER,
    "minWords" INTEGER,

    CONSTRAINT "IeltsPart_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsQuestionGroup" (
    "id" TEXT NOT NULL,
    "partId" TEXT NOT NULL,
    "order" INTEGER NOT NULL DEFAULT 0,
    "type" "IeltsQuestionType" NOT NULL,
    "instructions" TEXT NOT NULL,
    "wordLimit" TEXT,
    "maxWords" INTEGER,
    "maxNumbers" INTEGER,
    "bodyHtml" TEXT,
    "optionsJson" JSONB,
    "imageUrl" TEXT,
    "imageAlt" TEXT,

    CONSTRAINT "IeltsQuestionGroup_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsQuestion" (
    "id" TEXT NOT NULL,
    "partId" TEXT NOT NULL,
    "groupId" TEXT,
    "number" INTEGER NOT NULL,
    "type" "IeltsQuestionType" NOT NULL,
    "promptHtml" TEXT,
    "optionsJson" JSONB,
    "correctAnswer" TEXT NOT NULL,
    "acceptedAnswers" JSONB,
    "correctAnswerSet" JSONB,
    "caseSensitive" BOOLEAN NOT NULL DEFAULT false,
    "explanation" TEXT,
    "answerLocation" TEXT,
    "metadata" JSONB,

    CONSTRAINT "IeltsQuestion_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsAttempt" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "testId" TEXT NOT NULL,
    "mode" "IeltsAttemptMode" NOT NULL DEFAULT 'REALISTIC',
    "status" "IeltsAttemptStatus" NOT NULL DEFAULT 'IN_PROGRESS',
    "skills" JSONB NOT NULL,
    "startedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "submittedAt" TIMESTAMP(3),
    "listeningRaw" INTEGER,
    "listeningBand" DOUBLE PRECISION,
    "readingRaw" INTEGER,
    "readingBand" DOUBLE PRECISION,
    "writingBand" DOUBLE PRECISION,
    "speakingBand" DOUBLE PRECISION,
    "overallBand" DOUBLE PRECISION,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "IeltsAttempt_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsSectionAttempt" (
    "id" TEXT NOT NULL,
    "attemptId" TEXT NOT NULL,
    "sectionId" TEXT NOT NULL,
    "startedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "submittedAt" TIMESTAMP(3),
    "expiresAt" TIMESTAMP(3),
    "timeSpentSeconds" INTEGER NOT NULL DEFAULT 0,
    "currentPart" INTEGER NOT NULL DEFAULT 1,
    "playedParts" JSONB,
    "rawScore" INTEGER,
    "totalCount" INTEGER,
    "band" DOUBLE PRECISION,

    CONSTRAINT "IeltsSectionAttempt_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsAnswer" (
    "id" TEXT NOT NULL,
    "attemptId" TEXT NOT NULL,
    "questionId" TEXT NOT NULL,
    "value" TEXT,
    "isCorrect" BOOLEAN,
    "flagged" BOOLEAN NOT NULL DEFAULT false,
    "answeredAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "IeltsAnswer_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsPassageMark" (
    "id" TEXT NOT NULL,
    "attemptId" TEXT NOT NULL,
    "partId" TEXT NOT NULL,
    "startOffset" INTEGER NOT NULL,
    "endOffset" INTEGER NOT NULL,
    "quote" TEXT NOT NULL,
    "note" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "IeltsPassageMark_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsWritingSubmission" (
    "id" TEXT NOT NULL,
    "attemptId" TEXT NOT NULL,
    "partId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "responseText" TEXT NOT NULL,
    "wordCount" INTEGER NOT NULL,
    "submittedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" "IeltsReviewStatus" NOT NULL DEFAULT 'PENDING',

    CONSTRAINT "IeltsWritingSubmission_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsWritingReview" (
    "id" TEXT NOT NULL,
    "submissionId" TEXT NOT NULL,
    "reviewerId" TEXT NOT NULL,
    "taskBand" DOUBLE PRECISION NOT NULL,
    "coherenceBand" DOUBLE PRECISION NOT NULL,
    "lexicalBand" DOUBLE PRECISION NOT NULL,
    "grammarBand" DOUBLE PRECISION NOT NULL,
    "overallBand" DOUBLE PRECISION NOT NULL,
    "overallFeedback" TEXT,
    "didWell" TEXT,
    "toImprove" TEXT,
    "vocabularyNotes" TEXT,
    "grammarNotes" TEXT,
    "coherenceNotes" TEXT,
    "taskResponseNotes" TEXT,
    "nextSteps" TEXT,
    "startedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "completedAt" TIMESTAMP(3),

    CONSTRAINT "IeltsWritingReview_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsWritingAnnotation" (
    "id" TEXT NOT NULL,
    "reviewId" TEXT NOT NULL,
    "startOffset" INTEGER NOT NULL,
    "endOffset" INTEGER NOT NULL,
    "quote" TEXT NOT NULL,
    "comment" TEXT NOT NULL,
    "kind" TEXT NOT NULL DEFAULT 'issue',
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "IeltsWritingAnnotation_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsSpeakingSubmission" (
    "id" TEXT NOT NULL,
    "attemptId" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "submittedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" "IeltsReviewStatus" NOT NULL DEFAULT 'PENDING',

    CONSTRAINT "IeltsSpeakingSubmission_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsSpeakingRecording" (
    "id" TEXT NOT NULL,
    "submissionId" TEXT NOT NULL,
    "partId" TEXT NOT NULL,
    "questionIndex" INTEGER NOT NULL DEFAULT 0,
    "promptText" TEXT NOT NULL,
    "audioUrl" TEXT NOT NULL,
    "durationSeconds" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "IeltsSpeakingRecording_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsSpeakingReview" (
    "id" TEXT NOT NULL,
    "submissionId" TEXT NOT NULL,
    "reviewerId" TEXT NOT NULL,
    "fluencyBand" DOUBLE PRECISION NOT NULL,
    "lexicalBand" DOUBLE PRECISION NOT NULL,
    "grammarBand" DOUBLE PRECISION NOT NULL,
    "pronunciationBand" DOUBLE PRECISION NOT NULL,
    "overallBand" DOUBLE PRECISION NOT NULL,
    "overallFeedback" TEXT,
    "fluencyNotes" TEXT,
    "vocabularyNotes" TEXT,
    "grammarNotes" TEXT,
    "pronunciationNotes" TEXT,
    "strongPoints" TEXT,
    "weaknesses" TEXT,
    "howToImprove" TEXT,
    "startedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "completedAt" TIMESTAMP(3),

    CONSTRAINT "IeltsSpeakingReview_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsSpeakingComment" (
    "id" TEXT NOT NULL,
    "recordingId" TEXT NOT NULL,
    "atSeconds" INTEGER NOT NULL,
    "comment" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "IeltsSpeakingComment_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsReviewerProfile" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "canReviewWriting" BOOLEAN NOT NULL DEFAULT false,
    "canReviewSpeaking" BOOLEAN NOT NULL DEFAULT false,
    "writingBand" DOUBLE PRECISION,
    "speakingBand" DOUBLE PRECISION,
    "approved" BOOLEAN NOT NULL DEFAULT false,
    "approvedById" TEXT,
    "approvedAt" TIMESTAMP(3),
    "bio" TEXT,

    CONSTRAINT "IeltsReviewerProfile_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "IeltsScoreConversion" (
    "id" TEXT NOT NULL,
    "testId" TEXT,
    "module" "IeltsModule" NOT NULL DEFAULT 'ACADEMIC',
    "skill" "IeltsSkill" NOT NULL,
    "rawScore" INTEGER NOT NULL,
    "band" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "IeltsScoreConversion_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "IeltsTest_slug_key" ON "IeltsTest"("slug");

-- CreateIndex
CREATE INDEX "IeltsTest_status_module_idx" ON "IeltsTest"("status", "module");

-- CreateIndex
CREATE INDEX "IeltsSection_testId_idx" ON "IeltsSection"("testId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsSection_testId_skill_key" ON "IeltsSection"("testId", "skill");

-- CreateIndex
CREATE INDEX "IeltsPart_sectionId_idx" ON "IeltsPart"("sectionId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsPart_sectionId_partNumber_key" ON "IeltsPart"("sectionId", "partNumber");

-- CreateIndex
CREATE INDEX "IeltsQuestionGroup_partId_order_idx" ON "IeltsQuestionGroup"("partId", "order");

-- CreateIndex
CREATE INDEX "IeltsQuestion_partId_number_idx" ON "IeltsQuestion"("partId", "number");

-- CreateIndex
CREATE INDEX "IeltsQuestion_groupId_idx" ON "IeltsQuestion"("groupId");

-- CreateIndex
CREATE INDEX "IeltsAttempt_userId_status_idx" ON "IeltsAttempt"("userId", "status");

-- CreateIndex
CREATE INDEX "IeltsAttempt_testId_idx" ON "IeltsAttempt"("testId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsSectionAttempt_attemptId_sectionId_key" ON "IeltsSectionAttempt"("attemptId", "sectionId");

-- CreateIndex
CREATE INDEX "IeltsAnswer_questionId_idx" ON "IeltsAnswer"("questionId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsAnswer_attemptId_questionId_key" ON "IeltsAnswer"("attemptId", "questionId");

-- CreateIndex
CREATE INDEX "IeltsPassageMark_attemptId_partId_idx" ON "IeltsPassageMark"("attemptId", "partId");

-- CreateIndex
CREATE INDEX "IeltsWritingSubmission_userId_status_idx" ON "IeltsWritingSubmission"("userId", "status");

-- CreateIndex
CREATE INDEX "IeltsWritingSubmission_status_idx" ON "IeltsWritingSubmission"("status");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsWritingSubmission_attemptId_partId_key" ON "IeltsWritingSubmission"("attemptId", "partId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsWritingReview_submissionId_key" ON "IeltsWritingReview"("submissionId");

-- CreateIndex
CREATE INDEX "IeltsWritingReview_reviewerId_idx" ON "IeltsWritingReview"("reviewerId");

-- CreateIndex
CREATE INDEX "IeltsWritingAnnotation_reviewId_idx" ON "IeltsWritingAnnotation"("reviewId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsSpeakingSubmission_attemptId_key" ON "IeltsSpeakingSubmission"("attemptId");

-- CreateIndex
CREATE INDEX "IeltsSpeakingSubmission_userId_status_idx" ON "IeltsSpeakingSubmission"("userId", "status");

-- CreateIndex
CREATE INDEX "IeltsSpeakingSubmission_status_idx" ON "IeltsSpeakingSubmission"("status");

-- CreateIndex
CREATE INDEX "IeltsSpeakingRecording_submissionId_idx" ON "IeltsSpeakingRecording"("submissionId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsSpeakingReview_submissionId_key" ON "IeltsSpeakingReview"("submissionId");

-- CreateIndex
CREATE INDEX "IeltsSpeakingReview_reviewerId_idx" ON "IeltsSpeakingReview"("reviewerId");

-- CreateIndex
CREATE INDEX "IeltsSpeakingComment_recordingId_idx" ON "IeltsSpeakingComment"("recordingId");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsReviewerProfile_userId_key" ON "IeltsReviewerProfile"("userId");

-- CreateIndex
CREATE INDEX "IeltsReviewerProfile_approved_idx" ON "IeltsReviewerProfile"("approved");

-- CreateIndex
CREATE INDEX "IeltsScoreConversion_module_skill_idx" ON "IeltsScoreConversion"("module", "skill");

-- CreateIndex
CREATE UNIQUE INDEX "IeltsScoreConversion_testId_module_skill_rawScore_key" ON "IeltsScoreConversion"("testId", "module", "skill", "rawScore");

-- AddForeignKey
ALTER TABLE "IeltsSection" ADD CONSTRAINT "IeltsSection_testId_fkey" FOREIGN KEY ("testId") REFERENCES "IeltsTest"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsPart" ADD CONSTRAINT "IeltsPart_sectionId_fkey" FOREIGN KEY ("sectionId") REFERENCES "IeltsSection"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsQuestionGroup" ADD CONSTRAINT "IeltsQuestionGroup_partId_fkey" FOREIGN KEY ("partId") REFERENCES "IeltsPart"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsQuestion" ADD CONSTRAINT "IeltsQuestion_partId_fkey" FOREIGN KEY ("partId") REFERENCES "IeltsPart"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsQuestion" ADD CONSTRAINT "IeltsQuestion_groupId_fkey" FOREIGN KEY ("groupId") REFERENCES "IeltsQuestionGroup"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsAttempt" ADD CONSTRAINT "IeltsAttempt_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsAttempt" ADD CONSTRAINT "IeltsAttempt_testId_fkey" FOREIGN KEY ("testId") REFERENCES "IeltsTest"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSectionAttempt" ADD CONSTRAINT "IeltsSectionAttempt_attemptId_fkey" FOREIGN KEY ("attemptId") REFERENCES "IeltsAttempt"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSectionAttempt" ADD CONSTRAINT "IeltsSectionAttempt_sectionId_fkey" FOREIGN KEY ("sectionId") REFERENCES "IeltsSection"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsAnswer" ADD CONSTRAINT "IeltsAnswer_attemptId_fkey" FOREIGN KEY ("attemptId") REFERENCES "IeltsAttempt"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsAnswer" ADD CONSTRAINT "IeltsAnswer_questionId_fkey" FOREIGN KEY ("questionId") REFERENCES "IeltsQuestion"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsWritingSubmission" ADD CONSTRAINT "IeltsWritingSubmission_attemptId_fkey" FOREIGN KEY ("attemptId") REFERENCES "IeltsAttempt"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsWritingSubmission" ADD CONSTRAINT "IeltsWritingSubmission_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsWritingReview" ADD CONSTRAINT "IeltsWritingReview_submissionId_fkey" FOREIGN KEY ("submissionId") REFERENCES "IeltsWritingSubmission"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsWritingReview" ADD CONSTRAINT "IeltsWritingReview_reviewerId_fkey" FOREIGN KEY ("reviewerId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsWritingAnnotation" ADD CONSTRAINT "IeltsWritingAnnotation_reviewId_fkey" FOREIGN KEY ("reviewId") REFERENCES "IeltsWritingReview"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSpeakingSubmission" ADD CONSTRAINT "IeltsSpeakingSubmission_attemptId_fkey" FOREIGN KEY ("attemptId") REFERENCES "IeltsAttempt"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSpeakingSubmission" ADD CONSTRAINT "IeltsSpeakingSubmission_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSpeakingRecording" ADD CONSTRAINT "IeltsSpeakingRecording_submissionId_fkey" FOREIGN KEY ("submissionId") REFERENCES "IeltsSpeakingSubmission"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSpeakingReview" ADD CONSTRAINT "IeltsSpeakingReview_submissionId_fkey" FOREIGN KEY ("submissionId") REFERENCES "IeltsSpeakingSubmission"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSpeakingReview" ADD CONSTRAINT "IeltsSpeakingReview_reviewerId_fkey" FOREIGN KEY ("reviewerId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsSpeakingComment" ADD CONSTRAINT "IeltsSpeakingComment_recordingId_fkey" FOREIGN KEY ("recordingId") REFERENCES "IeltsSpeakingRecording"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "IeltsReviewerProfile" ADD CONSTRAINT "IeltsReviewerProfile_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
