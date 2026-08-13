-- Lets an admin set Telegram membership by hand from the bookings queue.
--
-- Idempotent. Keep semicolons out of comments in this directory.

ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "telegramManualOverride" BOOLEAN NOT NULL DEFAULT false;
