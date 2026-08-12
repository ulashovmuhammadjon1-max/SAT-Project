import { Fragment } from "react";

/**
 * Renders a message body.
 *
 * The body is plain text — it is stored that way and never rendered with
 * `dangerouslySetInnerHTML`. React escapes every string it renders, so the
 * only job here is to pick out mentions and URLs and wrap those *fragments*
 * in elements. Building an HTML string and injecting it would hand any
 * student the ability to run script in every reader's browser, which is
 * precisely why this function returns nodes instead.
 */

// A mention token as typed: @ followed by word characters. Deliberately does
// not span whitespace — "@Dilnoza said" must highlight only the name.
const TOKEN = /(@[A-Za-z0-9_-]+)|(https?:\/\/[^\s<>"']+)/g;

export function MessageText({ body, className }: { body: string; className?: string }) {
  const parts: React.ReactNode[] = [];
  let last = 0;
  let match: RegExpExecArray | null;

  // exec with /g walks the string; reset first in case the literal is reused.
  TOKEN.lastIndex = 0;
  while ((match = TOKEN.exec(body)) !== null) {
    if (match.index > last) parts.push(body.slice(last, match.index));

    if (match[1]) {
      parts.push(
        <span key={match.index} className="rounded bg-primary/15 px-1 font-medium text-primary">
          {match[1]}
        </span>
      );
    } else {
      const url = match[2];
      parts.push(
        <a
          key={match.index}
          href={url}
          target="_blank"
          // noreferrer as well as noopener: without it the destination learns
          // which page linked to it, and a chat message is not a referral.
          rel="noopener noreferrer nofollow"
          className="text-primary underline underline-offset-2 hover:no-underline"
        >
          {url.length > 60 ? `${url.slice(0, 59)}…` : url}
        </a>
      );
    }
    last = match.index + match[0].length;
  }
  if (last < body.length) parts.push(body.slice(last));

  return (
    <p className={className}>
      {parts.map((p, i) => (
        <Fragment key={i}>{p}</Fragment>
      ))}
    </p>
  );
}
