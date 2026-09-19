import Google from "next-auth/providers/google";
import Apple from "next-auth/providers/apple";
import MicrosoftEntraId from "next-auth/providers/microsoft-entra-id";
import type { Provider } from "next-auth/providers";

/**
 * OAuth sign-in providers, each gated on its own credentials.
 *
 * A provider is added ONLY when its environment variables are present, and the
 * sign-in button for it (see the login form) is shown ONLY when it is added.
 * So a provider is never half-there: no button appears until the credentials
 * exist, and once they do the button both appears and works. This is what
 * turns "the social buttons don't do anything" into "the social buttons you
 * see are the ones that work".
 *
 * Environment variables (set them in Vercel; never commit them):
 *   Google     AUTH_GOOGLE_ID, AUTH_GOOGLE_SECRET
 *   Microsoft  AUTH_MICROSOFT_ENTRA_ID_ID, AUTH_MICROSOFT_ENTRA_ID_SECRET
 *              (optional AUTH_MICROSOFT_ENTRA_ID_ISSUER — omit for "common",
 *              i.e. any personal or work Microsoft account)
 *   Apple      AUTH_APPLE_ID, AUTH_APPLE_SECRET
 *              (the secret is a generated, expiring client-secret JWT)
 *
 * `allowDangerousEmailAccountLinking` is on for all three: it links an OAuth
 * sign-in to an existing account with the same email. The "dangerous" only
 * applies when a provider does not verify email ownership — Google, Microsoft
 * and Apple all do — so here it is the safe, friendly behaviour: a student who
 * first signed up with an email can later click "Continue with Google" for the
 * same address instead of hitting an account-already-exists dead end.
 */

export interface EnabledOAuth {
  google: boolean;
  microsoft: boolean;
  apple: boolean;
}

function present(...names: string[]): boolean {
  return names.every((n) => Boolean(process.env[n]?.trim()));
}

/** Which OAuth providers are configured in this runtime. Safe to call anywhere
 *  server-side; reads only presence, never the secret values. */
export function enabledOAuth(): EnabledOAuth {
  return {
    google: present("AUTH_GOOGLE_ID", "AUTH_GOOGLE_SECRET"),
    microsoft: present("AUTH_MICROSOFT_ENTRA_ID_ID", "AUTH_MICROSOFT_ENTRA_ID_SECRET"),
    apple: present("AUTH_APPLE_ID", "AUTH_APPLE_SECRET"),
  };
}

/** The provider instances to hand to NextAuth — only the configured ones. */
export function oauthProviders(): Provider[] {
  const enabled = enabledOAuth();
  const providers: Provider[] = [];
  const link = { allowDangerousEmailAccountLinking: true };

  if (enabled.google) {
    providers.push(
      Google({
        clientId: process.env.AUTH_GOOGLE_ID,
        clientSecret: process.env.AUTH_GOOGLE_SECRET,
        ...link,
      }),
    );
  }

  if (enabled.microsoft) {
    providers.push(
      MicrosoftEntraId({
        clientId: process.env.AUTH_MICROSOFT_ENTRA_ID_ID,
        clientSecret: process.env.AUTH_MICROSOFT_ENTRA_ID_SECRET,
        // Omitted issuer defaults to "common" — any Microsoft account.
        issuer: process.env.AUTH_MICROSOFT_ENTRA_ID_ISSUER,
        ...link,
      }),
    );
  }

  if (enabled.apple) {
    providers.push(
      Apple({
        clientId: process.env.AUTH_APPLE_ID,
        clientSecret: process.env.AUTH_APPLE_SECRET,
        ...link,
      }),
    );
  }

  return providers;
}
