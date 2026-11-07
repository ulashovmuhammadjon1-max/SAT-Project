/**
 * Brand marks for the social sign-in buttons.
 *
 * Inline SVG rather than an icon dependency: lucide has no brand logos, and
 * these are the official multi-colour marks the reference shows. Each renders
 * at 18px inside a 20px box and carries aria-hidden — the button's text label
 * is the accessible name, so the icon is decorative.
 */

export function GoogleIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" className={className} aria-hidden="true" focusable="false">
      <path
        fill="#4285F4"
        d="M23.52 12.27c0-.79-.07-1.54-.2-2.27H12v4.51h6.47a5.54 5.54 0 0 1-2.4 3.63v3h3.88c2.27-2.09 3.57-5.17 3.57-8.87Z"
      />
      <path
        fill="#34A853"
        d="M12 24c3.24 0 5.96-1.08 7.95-2.91l-3.88-3c-1.08.72-2.45 1.16-4.07 1.16-3.13 0-5.78-2.11-6.73-4.96H1.26v3.09A12 12 0 0 0 12 24Z"
      />
      <path
        fill="#FBBC05"
        d="M5.27 14.29a7.2 7.2 0 0 1-.38-2.29c0-.8.14-1.57.38-2.29V6.62H1.26a12 12 0 0 0 0 10.76l4.01-3.09Z"
      />
      <path
        fill="#EA4335"
        d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.44-3.44C17.95 1.19 15.24 0 12 0A12 12 0 0 0 1.26 6.62l4.01 3.09C6.22 6.86 8.87 4.75 12 4.75Z"
      />
    </svg>
  );
}

export function MicrosoftIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" className={className} aria-hidden="true" focusable="false">
      <path fill="#F25022" d="M1 1h10.4v10.4H1z" />
      <path fill="#7FBA00" d="M12.6 1H23v10.4H12.6z" />
      <path fill="#00A4EF" d="M1 12.6h10.4V23H1z" />
      <path fill="#FFB900" d="M12.6 12.6H23V23H12.6z" />
    </svg>
  );
}

export function AppleIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" className={className} aria-hidden="true" focusable="false">
      <path
        fill="currentColor"
        d="M17.05 12.54c-.03-2.6 2.12-3.85 2.22-3.91-1.21-1.77-3.09-2.01-3.76-2.04-1.6-.16-3.12.94-3.93.94-.81 0-2.06-.92-3.39-.9-1.74.03-3.35 1.01-4.25 2.57-1.81 3.14-.46 7.79 1.3 10.34.86 1.25 1.88 2.65 3.22 2.6 1.29-.05 1.78-.83 3.34-.83 1.56 0 2 .83 3.37.81 1.39-.03 2.27-1.27 3.12-2.53.98-1.45 1.39-2.85 1.41-2.92-.03-.01-2.7-1.04-2.72-4.12ZM14.6 4.92c.71-.86 1.19-2.06 1.06-3.25-1.02.04-2.26.68-2.99 1.54-.66.76-1.23 1.98-1.08 3.15 1.14.09 2.3-.58 3.01-1.44Z"
      />
    </svg>
  );
}

/** Instagram glyph, single colour so it follows the surrounding text colour. */
export function InstagramIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" className={className} aria-hidden="true" focusable="false">
      <path
        fill="currentColor"
        d="M12 2.2c3.2 0 3.6 0 4.8.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.15 3.23-1.66 4.77-4.92 4.92-1.27.06-1.64.07-4.8.07-3.2 0-3.58-.01-4.85-.07-3.26-.15-4.77-1.7-4.92-4.92C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85C2.38 3.92 3.9 2.38 7.15 2.23 8.42 2.17 8.8 2.16 12 2.16Zm0 1.98c-3.15 0-3.5.01-4.75.07-2.4.11-3.52 1.25-3.63 3.63-.06 1.24-.07 1.6-.07 4.75s.01 3.5.07 4.75c.11 2.37 1.22 3.52 3.63 3.63 1.24.06 1.6.07 4.75.07s3.5-.01 4.75-.07c2.4-.11 3.52-1.26 3.63-3.63.06-1.24.07-1.6.07-4.75s-.01-3.5-.07-4.75c-.11-2.37-1.23-3.52-3.63-3.63-1.24-.06-1.6-.07-4.75-.07Zm0 3.08a4.74 4.74 0 1 1 0 9.48 4.74 4.74 0 0 1 0-9.48Zm0 1.98a2.76 2.76 0 1 0 0 5.52 2.76 2.76 0 0 0 0-5.52Zm4.93-3.32a1.1 1.1 0 1 1 0 2.2 1.1 1.1 0 0 1 0-2.2Z"
      />
    </svg>
  );
}

/** Telegram paper-plane glyph, single colour. */
export function TelegramIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" width="18" height="18" className={className} aria-hidden="true" focusable="false">
      <path
        fill="currentColor"
        d="M21.94 4.6 18.9 19.02c-.23 1.01-.83 1.26-1.68.79l-4.63-3.41-2.23 2.15c-.25.25-.45.45-.93.45l.33-4.73 8.6-7.77c.37-.33-.08-.52-.58-.19L7.2 13.01l-4.57-1.43c-.99-.31-1.01-.99.21-1.47L20.7 3.23c.83-.31 1.55.19 1.24 1.37Z"
      />
    </svg>
  );
}
