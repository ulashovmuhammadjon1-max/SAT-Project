-- 031: three more questions on the research proposal.
--   qualifications  exams and scores (SAT, IELTS, AP, olympiads ...)
--   priorWork       what the student has already done on their question
--   introEssay      a self-introduction, at most 300 words (enforced in the app)
-- Nullable: proposals submitted before this have none of them. Additive only;
-- applied to production before the code that reads them.

ALTER TABLE "ResearchProposal" ADD COLUMN IF NOT EXISTS "qualifications" TEXT;
ALTER TABLE "ResearchProposal" ADD COLUMN IF NOT EXISTS "priorWork" TEXT;
ALTER TABLE "ResearchProposal" ADD COLUMN IF NOT EXISTS "introEssay" TEXT;
