-- Booking approval workflow: PENDING -> approved / rejected, with a reason.
--
-- Idempotent, like every migration in this directory: safe to re-run against a
-- database that already has some of it. Run against local dev and production.
--
-- Existing bookings are deliberately left alone. Anything already UPCOMING was
-- confirmed under the old auto-confirm rule and stays confirmed, and only
-- bookings made after this ships land in PENDING. Nothing a student already
-- holds is taken back and put in a queue.
--
-- NOTE: keep semicolons out of comments in this directory. The runner splits
-- statements on semicolons outside dollar-quotes, and one inside a comment cut
-- a DO block in half — the PENDING value silently did not apply on the first
-- production run.

-- 1. New enum values. ADD VALUE cannot run inside a transaction block in older
--    Postgres and cannot be rolled back, so each is guarded on its own.
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_enum e JOIN pg_type t ON t.oid = e.enumtypid
     WHERE t.typname = 'BookingStatus' AND e.enumlabel = 'PENDING'
  ) THEN
    ALTER TYPE "BookingStatus" ADD VALUE 'PENDING' BEFORE 'UPCOMING';
  END IF;
END $$;

DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_enum e JOIN pg_type t ON t.oid = e.enumtypid
     WHERE t.typname = 'BookingStatus' AND e.enumlabel = 'REJECTED'
  ) THEN
    ALTER TYPE "BookingStatus" ADD VALUE 'REJECTED';
  END IF;
END $$;

-- 2. Decision columns.
ALTER TABLE "Booking" ADD COLUMN IF NOT EXISTS "statusReason" TEXT;
ALTER TABLE "Booking" ADD COLUMN IF NOT EXISTS "decidedAt"   TIMESTAMP(3);
ALTER TABLE "Booking" ADD COLUMN IF NOT EXISTS "decidedById" TEXT;

-- 3. Who decided. SetNull rather than Cascade: deleting an admin account must
--    not delete the students' bookings they happened to approve.
DO $$
BEGIN
  ALTER TABLE "Booking"
    ADD CONSTRAINT "Booking_decidedById_fkey"
    FOREIGN KEY ("decidedById") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

-- 4. The admin queue reads "everything awaiting a decision, oldest first".
CREATE INDEX IF NOT EXISTS "Booking_status_createdAt_idx" ON "Booking"("status", "createdAt");
