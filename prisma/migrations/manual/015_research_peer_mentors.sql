-- Research programme + peer-mentor programme.
--
-- Two new tables and one nullable column. The tables are new, so no existing
-- query can trip over them; MentorSlot."hostId" is the one addition to a live
-- table and MUST be applied to production before the code that selects it
-- deploys (see CLAUDE.md "SCHEMA CHANGES"). Nullable with SET NULL, so every
-- existing slot (hosted by the founder) is untouched and a deleted mentor
-- leaves their past slots intact.

CREATE TYPE "ResearchProposalStatus" AS ENUM ('PENDING', 'ACCEPTED', 'REJECTED');

CREATE TABLE "ResearchProposal" (
  "id"         TEXT NOT NULL PRIMARY KEY,
  "userId"     TEXT NOT NULL REFERENCES "User"("id") ON DELETE CASCADE,
  "title"      TEXT NOT NULL,
  "field"      TEXT NOT NULL,
  "question"   TEXT NOT NULL,
  "motivation" TEXT NOT NULL,
  "experience" TEXT,
  "status"     "ResearchProposalStatus" NOT NULL DEFAULT 'PENDING',
  "adminNote"  TEXT,
  "decidedAt"  TIMESTAMP(3),
  "createdAt"  TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"  TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX "ResearchProposal_status_idx" ON "ResearchProposal"("status");
CREATE INDEX "ResearchProposal_userId_idx" ON "ResearchProposal"("userId");

CREATE TYPE "PeerMentorStatus" AS ENUM ('PENDING', 'APPROVED', 'REJECTED');

CREATE TABLE "PeerMentorApplication" (
  "id"           TEXT NOT NULL PRIMARY KEY,
  -- One application per student: re-applying after a rejection updates the
  -- row rather than stacking history, which keeps "is this student an
  -- approved mentor" a single-row read.
  "userId"       TEXT NOT NULL UNIQUE REFERENCES "User"("id") ON DELETE CASCADE,
  "headline"     TEXT NOT NULL,
  "bio"          TEXT NOT NULL,
  "satScore"     INTEGER,
  "ieltsBand"    DOUBLE PRECISION,
  "subjects"     TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  "telegram"     TEXT,
  -- [{ name, dataUrl }] — score-report uploads stored inline as data URIs,
  -- same approach as question figures (no Blob token dependency).
  "certificates" JSONB NOT NULL DEFAULT '[]',
  "status"       "PeerMentorStatus" NOT NULL DEFAULT 'PENDING',
  "adminNote"    TEXT,
  "decidedAt"    TIMESTAMP(3),
  "createdAt"    TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt"    TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX "PeerMentorApplication_status_idx" ON "PeerMentorApplication"("status");

-- Who hosts a slot. NULL = the founder/admin, which is every slot that exists
-- today, so nothing changes retroactively.
ALTER TABLE "MentorSlot" ADD COLUMN "hostId" TEXT REFERENCES "User"("id") ON DELETE SET NULL;
CREATE INDEX "MentorSlot_hostId_idx" ON "MentorSlot"("hostId");
