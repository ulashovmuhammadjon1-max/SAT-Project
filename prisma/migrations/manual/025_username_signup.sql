-- Username + password signup: drop email from the required path.
--
-- Applied to production BEFORE the schema.prisma change was committed, per
-- CLAUDE.md's standing rule -- a schema field that reaches the deployed branch
-- ahead of its migration makes every whole-row Question/User fetch ask for a
-- column the database does not have, and that has taken this site down twice.
--
-- Both statements are backwards-compatible with the code that was deployed at
-- the time, which is why this ordering is safe:
--
--   * adding a nullable `username` cannot affect a client that does not select
--     it;
--   * dropping NOT NULL from `email` cannot affect reads (every existing row
--     still holds one) and cannot affect the old signup path (which always
--     supplied one).
--
-- EMAIL IS NOT DROPPED, deliberately. 693 accounts existed when this ran, all
-- 693 holding an email and 560 of them verified. Those are the addresses their
-- owners sign in with, and the ones the teacher-invite and referral flows send
-- to. Removing email from SIGNUP is what was asked for; deleting the column
-- would have locked out every existing account.

ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "username" TEXT;
CREATE UNIQUE INDEX IF NOT EXISTS "User_username_key" ON "User"("username");
ALTER TABLE "User" ALTER COLUMN "email" DROP NOT NULL;
