import { Prisma } from "@prisma/client";

/**
 * Accounts created before this are grandfathered: they can sign in whether or
 * not they ever confirmed an address (see the gate in `lib/session.ts`).
 *
 * Used to also gate the analytics student count (`countedStudentWhere`
 * below), until that was relaxed to count every `STUDENT` role regardless of
 * verification. It still defines `awaitingVerificationWhere`, the "stuck in
 * verification" population shown as its own callout on the statistics page —
 * accounts before this date were never asked to verify, so they were never
 * "awaiting" it.
 *
 * Deliberately a fixed timestamp rather than something computed at runtime: a
 * moving cutoff would grandfather every new signup forever, which is exactly
 * the bug this is meant to close.
 */
export const VERIFICATION_REQUIRED_FROM = new Date("2026-08-17T09:10:00.000Z");

/**
 * Who counts as a student.
 *
 * Every account with role `STUDENT` counts, confirmed or not. This used to
 * exclude unconfirmed signups from after `VERIFICATION_REQUIRED_FROM`, on the
 * reasoning that an unconfirmed address is "an address someone typed, not a
 * student" — reversed on the user's explicit instruction: unconfirmed
 * students should still appear in the students section. `awaitingVerificationWhere`
 * below still identifies that same population for the separate "stuck in
 * verification" callout on the statistics page — that diagnostic is still
 * useful, it just no longer subtracts from the headline count.
 *
 * This intentionally no longer agrees with the login gate in `lib/session.ts`,
 * which still blocks sign-in until an address is confirmed (grandfathered
 * accounts excepted) — the count reported here can include people who cannot
 * yet sign in. That was flagged as a risk when the two were first tied
 * together; it is accepted now because the counting change was explicit and
 * the login gate was not part of it.
 */
export const countedStudentWhere = {
  role: "STUDENT",
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
  return Prisma.sql`${Prisma.raw(`${p}role`)} = 'STUDENT'`;
}
