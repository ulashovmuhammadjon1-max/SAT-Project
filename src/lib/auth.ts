import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { PrismaAdapter } from "@auth/prisma-adapter";
import bcrypt from "bcryptjs";

import { prisma } from "@/lib/prisma";
import { loginSchema } from "@/lib/validations/auth";
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
  // uses SATForge even once a month stays signed in indefinitely; one who
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
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      authorize: async (credentials) => {
        const parsed = loginSchema.safeParse(credentials);
        if (!parsed.success) return null;

        const user = await prisma.user.findUnique({
          where: { email: parsed.data.email },
        });
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
