import type { NextAuthConfig } from "next-auth";

import type { UserRole } from "@/types/next-auth";

/**
 * Edge-compatible config (no bcrypt, no Prisma adapter, no Credentials provider).
 * Used by middleware for session checks; the full config in `auth.ts` extends this
 * with the Credentials provider + Prisma adapter for Node.js runtime routes/actions.
 */
export default {
  pages: {
    signIn: "/login",
  },
  providers: [],
  trustHost: true,
  // Must match auth.ts. The middleware builds its own NextAuth instance from
  // this config, and a shorter lifetime here would make the edge runtime treat
  // a token the server still considers valid as expired.
  session: {
    strategy: "jwt",
    maxAge: 30 * 24 * 60 * 60,
    updateAge: 24 * 60 * 60,
  },
  callbacks: {
    jwt({ token, user }) {
      if (user) {
        token.id = user.id as string;
        token.role = (user as { role: UserRole }).role;
      }
      return token;
    },
    session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
        session.user.role = token.role as UserRole;
      }
      return session;
    },
  },
} satisfies NextAuthConfig;
