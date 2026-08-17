import { Prisma } from "@prisma/client";

/**
 * Accounts created before this were never asked to confirm an address.
 *
 * One constant, used by two things that must agree: the access gate in
 * `lib/session.ts` and the analytics predicate below. If they ever disagreed,
 * the admin panel would report a population different from the one that can
 * actually sign in, which is the worst kind of wrong — plausible and quiet.
 *
 * It is the moment the gate shipped, not a round date: a cutoff even a few
 * hours ahead would excuse the accounts it is meant to catch.
 */
export const VERIFICATION_REQUIRED_FROM = new Date("2026-08-09T02:31:00.000Z");

/**
 * Who counts as a student.
 *
 * A student is counted when they have confirmed their address, **or** when
 * their account predates the day confirmation was introduced. The second half
 * is what keeps the existing roll intact: those people were never asked to
 * verify, so excluding them would silently delete real students from every
 * chart on the day this shipped.
 *
 * Everyone signing up from now on has to confirm before they appear. An
 * unconfirmed address is not a student — it is an address someone typed, and
 * counting it inflates every funnel, every country split and every average on
 * the page.
 */
export const countedStudentWhere = {
  role: "STUDENT",
  OR: [
    { emailVerified: { not: null } },
    { createdAt: { lt: VERIFICATION_REQUIRED_FROM } },
  ],
} satisfies Prisma.UserWhereInput;

/**
 * The complement: signed up since the cutoff and still has not confirmed.
 *
 * Its own export rather than a hand-written negation at each call site, because
 * the negation of "verified OR old" is the one people get wrong.
 */
export const awaitingVerificationWhere = {
  role: "STUDENT",
  emailVerified: null,
  createdAt: { gte: VERIFICATION_REQUIRED_FROM },
} satisfies Prisma.UserWhereInput;

/**
 * The same rule for the raw-SQL statistics queries.
 *
 * `alias` is the table alias the query gave `"User"` — several of them join it
 * as `u`, and one selects from it bare. Passed as a literal rather than
 * interpolated as a parameter because an alias is an identifier, not a value;
 * it is a fixed string from this file's callers, never user input.
 */
export function countedStudentSql(alias: string | null = null): Prisma.Sql {
  const p = alias ? `${alias}.` : "";
  return Prisma.sql`${Prisma.raw(`${p}role`)} = 'STUDENT' AND (${Prisma.raw(`${p}"emailVerified"`)} IS NOT NULL OR ${Prisma.raw(`${p}"createdAt"`)} < ${VERIFICATION_REQUIRED_FROM.toISOString()}::timestamptz)`;
}
