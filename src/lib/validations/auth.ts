import { z } from "zod";

/**
 * Signing up takes a username and a password. Nothing else.
 *
 * No email, no verification step, no questions. A student who lands on the
 * site can have an account in two fields, which is the whole point of the
 * change: every field between "I want to try this" and "I am practising" is a
 * field some students stop at.
 */

/**
 * 3 to 24 characters, letters/digits/underscore/dot, starting with a letter or
 * digit. Deliberately narrow: a username is typed at sign-in, sometimes on a
 * phone, so spaces and punctuation that need a modifier key are excluded, and
 * a leading dot or underscore is excluded because it is invisible in most UI.
 *
 * Stored and compared LOWERCASE. Usernames that differ only in case are the
 * same account to a person typing one, and treating them as different is how
 * an impersonation gap opens.
 */
export const usernameSchema = z
  .string()
  .trim()
  .toLowerCase()
  .min(3, "Username must be at least 3 characters")
  .max(24, "Username must be 24 characters or fewer")
  .regex(
    /^[a-z0-9][a-z0-9._]*$/,
    "Use letters, numbers, dots and underscores; start with a letter or number",
  );

/**
 * FOUR CHARACTERS, and four digits is explicitly allowed.
 *
 * This is a deliberate relaxation from the previous 8 characters with an
 * uppercase letter and a digit, and it is worth being honest about the
 * trade: "1234" is a guessable password. It is accepted because the accounts
 * here hold practice results rather than anything of value, and because a
 * complexity rule that turns a student away costs more than it protects.
 *
 * Rate limiting at sign-in is what has to carry the weight instead; see
 * `loginSchema`'s note.
 */
export const passwordSchema = z
  .string()
  .min(4, "Password must be at least 4 characters")
  .max(200, "Password must be 200 characters or fewer");

/**
 * Sign-in accepts EITHER a username or an email address, in one field.
 *
 * Both are needed at once and neither can be dropped: accounts created since
 * username signup have no email, and the 693 accounts that predate it have no
 * username. Asking the user which kind of thing they are typing would be a
 * question about our migration history, so the field just takes both.
 */
export const loginSchema = z.object({
  identifier: z.string().trim().min(1, "Enter your username or email"),
  password: z.string().min(1, "Enter your password"),
});

export const registerSchema = z.object({
  username: usernameSchema,
  password: passwordSchema,
});

export type LoginInput = z.infer<typeof loginSchema>;
export type RegisterInput = z.infer<typeof registerSchema>;

/** True when the string looks like an email rather than a username. */
export function looksLikeEmail(identifier: string): boolean {
  return identifier.includes("@");
}
