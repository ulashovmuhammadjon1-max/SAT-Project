-- Real Telegram membership verification.
--
-- Idempotent, like every migration in this directory. Run against local dev and
-- production. Keep semicolons out of comments here -- the runner splits on
-- semicolons outside dollar-quotes and one inside a comment will cut a
-- statement in half.

ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "telegramUserId"    TEXT;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "telegramUsername"  TEXT;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "telegramLinkedAt"  TIMESTAMP(3);
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "telegramIsMember"  BOOLEAN NOT NULL DEFAULT false;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "telegramCheckedAt" TIMESTAMP(3);

-- One Telegram account per site account. Without this, two students could sign
-- in with the same Telegram identity and both inherit its membership, which
-- would make the whole check meaningless.
CREATE UNIQUE INDEX IF NOT EXISTS "User_telegramUserId_key" ON "User"("telegramUserId");
