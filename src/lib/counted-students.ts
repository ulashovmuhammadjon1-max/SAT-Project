import { Prisma } from "@prisma/client";

/**
 * Accounts created before this are grandfathered: they count as students and
 * they can sign in, whether or not they ever confirmed an address.
 *
 * One constant, used by two things that must agree: the access gate in
 * `lib/session.ts` and the analytics predicate below. If they ever disagreed,
 * the admin panel would report a population different from the one that can
 * actually sign in, which is the worst kind of wrong — plausible and quiet.
 *
 * Moved forward from the date confirmation first shipped (2026-08-09) to the
 * moment this change did. The earlier cutoff would have dropped every account
 * created in the week between, including real students who had simply not got
 * round to clicking the link, and losing existing students to a reporting
 * change is a worse outcome than counting a few unconfirmed ones for one more
 * cycle. Everyone from here on has to confirm.
 *
 * Deliberately a fixed timestamp rather than something computed at runtime: a
 * moving cutoff would grandfather every new signup forever, which is exactly
 * the bug this is meant to close.
 */
export const VERIFICATION_REQUIRED_FROM = new Date("2026-08-17T09:10:00.000Z");

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
