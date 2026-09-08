import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { PrismaAdapter } from "@auth/prisma-adapter";
import bcrypt from "bcryptjs";

import { prisma } from "@/lib/prisma";
import { loginSchema, looksLikeEmail } from "@/lib/validations/auth";
import authConfig from "@/lib/auth.config";

/** 30 days, in seconds. */
const SESSION_MAX_AGE = 30 * 24 * 60 * 60;

export const { handlers, auth, signIn, signOut } = NextAuth({
  ...authConfig,
  adapter: PrismaAdapter(prisma),

  // Behind a proxy/CDN (Vercel, and any custom domain in front of it) Auth.js
  // needs to be told the forwarded host is trustworthy, otherwise callback URL
  // checks can fail on some deployments.
  trustHost: true,

  // Session lifetime is stated explicitly rather than inherited from the
  // library default, so changing it is a deliberate edit and reading it does
  // not require knowing what @auth/core happens to default to.
  //
  // `updateAge` makes the expiry sliding: any request more than a day after the
  // token was issued re-issues it with a fresh 30-day window. A student who
  // uses Scholarly even once a month stays signed in indefinitely; one who
  // disappears for 30 days is asked to sign in again.
  session: {
    strategy: "jwt",
    maxAge: SESSION_MAX_AGE,
    updateAge: 24 * 60 * 60,
  },
  jwt: { maxAge: SESSION_MAX_AGE },
  providers: [
    Credentials({
      name: "Credentials",
      credentials: {
        identifier: { label: "Username or email", type: "text" },
        password: { label: "Password", type: "password" },
      },
      authorize: async (credentials) => {
        const parsed = loginSchema.safeParse(credentials);
        if (!parsed.success) return null;

        // ONE FIELD, EITHER KIND. Accounts created since username signup have
        // no email; the 693 that predate it have no username. An "@" is what
        // separates the two, and a username cannot contain one (see
        // usernameSchema), so the test cannot misroute a real username.
        //
        // Usernames are stored lowercase, so the lookup lowercases too --
        // otherwise "Alice" and "alice" would be different accounts to the
        // database and the same one to the person typing.
        const identifier = parsed.data.identifier.trim();
        const user = looksLikeEmail(identifier)
          ? await prisma.user.findUnique({ where: { email: identifier.toLowerCase() } })
          : await prisma.user.findUnique({ where: { username: identifier.toLowerCase() } });
        if (!user?.passwordHash) return null;

        const isValid = await bcrypt.compare(parsed.data.password, user.passwordHash);
        if (!isValid) return null;

        return {
          id: user.id,
          name: user.name,
          email: user.email,
          image: user.image,
          role: user.role,
        };
      },
    }),
  ],
});
