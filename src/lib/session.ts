import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { VERIFICATION_REQUIRED_FROM } from "@/lib/counted-students";

export async function getCurrentUser() {
  const session = await auth();
  return session?.user ?? null;
}

export async function requireUser() {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  return user;
}

/**
 * Accounts created before this were never asked to confirm an address, so the
 * gate below does not apply to them.
 *
 * Grandfathering in code rather than by backfilling `emailVerified` is
 * deliberate: it makes the rollout safe *without* a manual database step, so
 * shipping the gate before the backfill runs cannot lock out a single existing
 * student. The backfill in `prisma/migrations/manual/002` is a tidy-up, not a
 * prerequisite.
 *
 * Now shared with the admin analytics predicate — see `lib/counted-students`
 * for why the two must not be allowed to drift.
 *
 * Signed in *and* confirmed their email address.
 *
 * Read from the database rather than the session token on purpose: the JWT is
 * issued at sign-in and lives for 30 days, so a student who verified two
 * minutes ago would still be carrying an "unverified" claim and would be bounced
 * back to the waiting screen in a loop.
 *
 * Admins are exempt. Locking the operator out of their own admin panel because
 * a mail provider is down is not a trade worth making.
 */
export async function requireVerifiedUser() {
  const user = await requireUser();
  if (user.role === "ADMIN") return user;

  const row = await prisma.user.findUnique({
    where: { id: user.id },
    select: { emailVerified: true, createdAt: true },
  });
  if (!row) return user;
  if (row.emailVerified) return user;
  if (row.createdAt < VERIFICATION_REQUIRED_FROM) return user;

  redirect("/verify-email");
}

export async function requireAdmin() {
  const user = await requireUser();
  if (user.role !== "ADMIN") redirect("/dashboard");
  return user;
}
