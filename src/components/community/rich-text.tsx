import { Fragment, type ReactNode } from "react";

import { cn } from "@/lib/utils";

/**
 * Renders a message body.
 *
 * Bodies are stored as plain text. This turns a small markdown subset into
 * React elements — never into an HTML string — so nothing a student types can
 * become live markup in someone else's browser. Anything the parser does not
 * recognise is shown exactly as typed.
 *
 *   **bold**  *italic*  __underline__  ~~strike~~  `code`
 *   ```code block```   - bullets   1. numbered   > quote
 *   [label](https://link)   bare https:// links   @mentions
 */

const INLINE =
  /(`[^`\n]+`)|(\[[^\]\n]{1,200}\]\(https?:\/\/[^\s)]+\))|(\*\*[^*\n]+\*\*)|(__[^_\n]+__)|(~~[^~\n]+~~)|(\*[^*\s][^*\n]*\*)|(https?:\/\/[^\s<>"']+[^\s<>"'.,;:!?)\]])|(@[A-Za-z0-9_-]+)/g;

function safeHref(url: string): string | null {
  try {
    const u = new URL(url);
    return u.protocol === "https:" || u.protocol === "http:" ? u.toString() : null;
  } catch {
    return null;
  }
}

function Link({ href, children }: { href: string; children: ReactNode }) {
  return (
    <a
      href={href}
      target="_blank"
      // noreferrer as well as noopener: a chat message is not a referral.
      rel="noopener noreferrer nofollow ugc"
      className="font-medium text-primary underline decoration-primary/40 underline-offset-2 transition-colors hover:decoration-primary"
    >
      {children}
    </a>
  );
}

export function renderInline(text: string, keyPrefix = "i"): ReactNode[] {
  const out: ReactNode[] = [];
  let last = 0;
  let m: RegExpExecArray | null;
  const re = new RegExp(INLINE.source, "g");
  let i = 0;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(text.slice(last, m.index));
    const key = `${keyPrefix}-${i++}`;
    const [tok] = m;
    if (m[1]) {
      out.push(
        <code key={key} className="rounded-md border border-border/70 bg-secondary/80 px-1.5 py-0.5 font-mono text-[0.85em]">
          {tok.slice(1, -1)}
        </code>,
      );
    } else if (m[2]) {
      const close = tok.indexOf("](");
      const label = tok.slice(1, close);
      const href = safeHref(tok.slice(close + 2, -1));
      out.push(href ? <Link key={key} href={href}>{renderInline(label, key)}</Link> : tok);
    } else if (m[3]) {
      out.push(<strong key={key} className="font-semibold text-foreground">{renderInline(tok.slice(2, -2), key)}</strong>);
    } else if (m[4]) {
      out.push(<u key={key} className="underline-offset-2">{renderInline(tok.slice(2, -2), key)}</u>);
    } else if (m[5]) {
      out.push(<s key={key} className="opacity-70">{renderInline(tok.slice(2, -2), key)}</s>);
    } else if (m[6]) {
      out.push(<em key={key}>{renderInline(tok.slice(1, -1), key)}</em>);
    } else if (m[7]) {
      const href = safeHref(tok);
      out.push(
        href ? (
          <Link key={key} href={href}>
            {tok.length > 64 ? `${tok.slice(0, 63)}…` : tok}
          </Link>
        ) : (
          tok
        ),
      );
    } else if (m[8]) {
      out.push(
        <span key={key} className="rounded-md bg-primary/10 px-1 font-medium text-primary">
          {tok}
        </span>,
      );
    }
    last = m.index + tok.length;
  }
  if (last < text.length) out.push(text.slice(last));
  return out;
}

type Block =
  | { t: "p"; lines: string[] }
  | { t: "code"; text: string }
  | { t: "ul"; items: string[] }
  | { t: "ol"; items: string[]; start: number }
  | { t: "quote"; lines: string[] };

export function parseBlocks(body: string): Block[] {
  const lines = body.replace(/\r\n/g, "\n").split("\n");
  const blocks: Block[] = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (line.trimStart().startsWith("```")) {
      const buf: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trimStart().startsWith("```")) buf.push(lines[i++]);
      i++; // closing fence (or end of text)
      blocks.push({ t: "code", text: buf.join("\n") });
      continue;
    }
    if (/^\s*[-*•]\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*[-*•]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*[-*•]\s+/, ""));
      blocks.push({ t: "ul", items });
      continue;
    }
    const ol = /^\s*(\d{1,3})[.)]\s+/.exec(line);
    if (ol) {
      const items: string[] = [];
      while (i < lines.length && /^\s*\d{1,3}[.)]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*\d{1,3}[.)]\s+/, ""));
      blocks.push({ t: "ol", items, start: Number(ol[1]) });
      continue;
    }
    if (/^\s*>\s?/.test(line)) {
      const buf: string[] = [];
      while (i < lines.length && /^\s*>\s?/.test(lines[i])) buf.push(lines[i++].replace(/^\s*>\s?/, ""));
      blocks.push({ t: "quote", lines: buf });
      continue;
    }
    const buf: string[] = [];
    while (
      i < lines.length &&
      !lines[i].trimStart().startsWith("```") &&
      !/^\s*[-*•]\s+/.test(lines[i]) &&
      !/^\s*\d{1,3}[.)]\s+/.test(lines[i]) &&
      !/^\s*>\s?/.test(lines[i])
    ) {
      buf.push(lines[i++]);
    }
    if (buf.length) blocks.push({ t: "p", lines: buf });
  }
  return blocks;
}

function Lines({ lines, k }: { lines: string[]; k: string }) {
  return (
    <>
      {lines.map((l, j) => (
        <Fragment key={`${k}-${j}`}>
          {j > 0 && <br />}
          {renderInline(l, `${k}-${j}`)}
        </Fragment>
      ))}
    </>
  );
}

export function RichText({ body, className }: { body: string; className?: string }) {
  const blocks = parseBlocks(body);
  return (
    <div className={cn("space-y-2 break-words text-[15px] leading-relaxed text-foreground/90", className)}>
      {blocks.map((b, bi) => {
        const k = `b${bi}`;
        switch (b.t) {
          case "code":
            return (
              <pre
                key={k}
                className="max-h-96 overflow-auto rounded-lg border border-border bg-secondary/70 p-3 font-mono text-[13px] leading-relaxed text-foreground"
              >
                <code>{b.text}</code>
              </pre>
            );
          case "ul":
            return (
              <ul key={k} className="ml-5 list-disc space-y-1 marker:text-primary/70">
                {b.items.map((it, j) => (
                  <li key={j}>{renderInline(it, `${k}-${j}`)}</li>
                ))}
              </ul>
            );
          case "ol":
            return (
              <ol key={k} start={b.start} className="ml-5 list-decimal space-y-1 marker:font-medium marker:text-primary/80">
                {b.items.map((it, j) => (
                  <li key={j}>{renderInline(it, `${k}-${j}`)}</li>
                ))}
              </ol>
            );
          case "quote":
            return (
              <blockquote key={k} className="border-l-2 border-primary/40 pl-3 italic text-muted-foreground">
                <Lines lines={b.lines} k={k} />
              </blockquote>
            );
          default:
            return (
              <p key={k} className="whitespace-pre-wrap">
                <Lines lines={b.lines} k={k} />
              </p>
            );
        }
      })}
    </div>
  );
}

/** Every http(s) URL in a body, for link previews. */
export function linksIn(body: string): string[] {
  const found = body.match(/https?:\/\/[^\s<>"')\]]+/g) ?? [];
  return [...new Set(found.map((u) => u.replace(/[.,;:!?]+$/, "")))].slice(0, 3);
}
