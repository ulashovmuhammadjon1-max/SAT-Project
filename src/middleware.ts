import NextAuth from "next-auth";
import { NextResponse } from "next/server";

import authConfig from "@/lib/auth.config";

const { auth } = NextAuth(authConfig);

const PUBLIC_ROUTES = [
  "/",
  "/login",
  "/register",
  "/onboarding",
  "/forgot-password",
  "/reset-password",
  // Public because the link in the email must work whether or not the browser
  // that opens it is signed in — a student often clicks it on their phone.
  "/verify-email",
  "/terms",
  "/privacy",
  // The whole point of the impact page is that anyone — an admissions
  // officer included — can open it without an account.
  "/impact",
  "/team",
  "/schools",
  "/journal",
];

// Prefixes, not exact paths. PUBLIC_ROUTES matches a pathname exactly, so a
// published paper at /journal/<slug> was redirecting to the login page while
// the index it is linked from stayed open. A paper nobody can read without an
// account is not published, and a citation of one would break for the reader.
const PUBLIC_PREFIXES = ["/journal/"];

export default auth((req) => {
  const { pathname } = req.nextUrl;
  const isPublic =
    PUBLIC_ROUTES.includes(pathname) ||
    PUBLIC_PREFIXES.some((prefix) => pathname.startsWith(prefix)) ||
    pathname.startsWith("/api/auth") ||
    pathname.startsWith("/_next") ||
    pathname.startsWith("/favicon") ||
    pathname.startsWith("/icon");

  if (isPublic) return NextResponse.next();

  const user = req.auth?.user;

  if (!user) {
    const loginUrl = new URL("/login", req.nextUrl.origin);
    loginUrl.searchParams.set("callbackUrl", pathname);
    return NextResponse.redirect(loginUrl);
  }

  if (pathname.startsWith("/admin") && user.role !== "ADMIN") {
    return NextResponse.redirect(new URL("/dashboard", req.nextUrl.origin));
  }

  return NextResponse.next();
});

export const config = {
  // Static image extensions are excluded so they are served directly rather
  // than redirected to /login for a logged-out visitor. .webp was missing,
  // which made the hero background plate 307 on the marketing page — the
  // one page whose visitors are all logged out.
  matcher: ["/((?!_next/static|_next/image|favicon.ico|.*\\.(?:png|svg|webp|avif|jpg|jpeg|gif|ico)$).*)"],
};
