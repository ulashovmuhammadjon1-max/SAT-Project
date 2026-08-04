import type { NextAuthConfig } from "next-auth";

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
  callbacks: {
    jwt({ token, user }) {
      if (user) {
        token.id = user.id as string;
        token.role = (user as { role: "STUDENT" | "ADMIN" }).role;
      }
      return token;
    },
    session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
        session.user.role = token.role as "STUDENT" | "ADMIN";
      }
      return session;
    },
  },
} satisfies NextAuthConfig;
