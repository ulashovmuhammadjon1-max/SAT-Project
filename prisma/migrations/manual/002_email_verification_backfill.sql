-- Email verification: grandfather every existing account.
--
-- `User.emailVerified` has been on the model since Auth.js was wired up, but
-- nothing ever wrote to it, so every row is NULL. Turning on the verification
-- gate without this would lock out every account that already exists —
-- including the admin — for a check they were never asked to pass.
--
-- Only accounts created from here on go through verification.
--
-- Safe to re-run: the WHERE clause makes it a no-op the second time.

UPDATE "User"
   SET "emailVerified" = NOW()
 WHERE "emailVerified" IS NULL;
