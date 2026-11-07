/**
 * Community notification email: "someone replied to you", or several of those
 * in one message, or the daily digest.
 *
 * Everything a student wrote is HTML-escaped before it goes anywhere near the
 * template. Names are first name plus last initial; no email address or other
 * account detail of the person who replied is ever included.
 *
 * Table layout with inline styles because that is what mail clients render;
 * a single 560px column that shrinks to the screen keeps it readable on a phone.
 */

export interface EmailItem {
  type: string;
  title: string;
  excerpt: string;
  /** The message being replied to, when there is one. */
  context: string | null;
  channel: string | null;
  url: string;
}

export function escapeHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

const C = {
  canvas: "#eef1f6",
  card: "#ffffff",
  ink: "#0f1a2e",
  body: "#3b4659",
  muted: "#6b7689",
  line: "#e3e8f0",
  brand: "#2f5be8",
  brandSoft: "#eef2fe",
  quote: "#f5f7fb",
};

function firstName(name: string | null): string {
  const first = (name ?? "").trim().split(/\s+/)[0];
  return first ? escapeHtml(first) : "there";
}

function label(type: string): string {
  switch (type) {
    case "REPLY":
      return "Reply";
    case "MENTION":
      return "Mention";
    case "ANSWER":
      return "Answer";
    case "THREAD_REPLY":
      return "Discussion";
    case "DIRECT_MESSAGE":
      return "Message";
    case "ANNOUNCEMENT":
      return "Announcement";
    case "ANSWER_ACCEPTED":
      return "Accepted";
    case "REACTION":
      return "Reaction";
    default:
      return "Update";
  }
}

function itemHtml(item: EmailItem, primary: boolean): string {
  const context = item.context
    ? `<tr><td style="padding:0 0 10px;">
         <div style="font-size:12px;color:${C.muted};margin:0 0 4px;">In reply to</div>
         <div style="background:${C.quote};border-left:3px solid ${C.line};border-radius:6px;padding:10px 12px;font-size:14px;line-height:1.5;color:${C.muted};">${escapeHtml(item.context)}</div>
       </td></tr>`
    : "";
  return `
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 ${primary ? 8 : 18}px;">
    <tr><td style="padding:0 0 8px;">
      <span style="display:inline-block;background:${C.brandSoft};color:${C.brand};font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:3px 8px;border-radius:999px;">${label(item.type)}</span>
      ${item.channel ? `<span style="font-size:12px;color:${C.muted};padding-left:6px;">#${escapeHtml(item.channel)}</span>` : ""}
    </td></tr>
    <tr><td style="padding:0 0 10px;font-size:${primary ? 18 : 15}px;line-height:1.35;font-weight:700;color:${C.ink};">${escapeHtml(item.title)}</td></tr>
    ${context}
    <tr><td style="padding:0 0 12px;">
      <div style="background:${C.card};border:1px solid ${C.line};border-left:3px solid ${C.brand};border-radius:6px;padding:12px 14px;font-size:15px;line-height:1.55;color:${C.body};">${escapeHtml(item.excerpt)}</div>
    </td></tr>
    <tr><td>
      <a href="${escapeHtml(item.url)}" style="display:inline-block;background:${primary ? C.brand : C.card};color:${primary ? "#ffffff" : C.brand};border:1px solid ${C.brand};text-decoration:none;padding:${primary ? "12px 22px" : "8px 14px"};border-radius:10px;font-weight:600;font-size:${primary ? 15 : 13}px;">${primary ? "View conversation" : "Open"}</a>
    </td></tr>
  </table>`;
}

export function renderCommunityEmail(input: {
  name: string | null;
  items: EmailItem[];
  digest: boolean;
  settingsUrl: string;
  inboxUrl: string;
}): { subject: string; text: string; html: string } {
  const { items } = input;
  const shown = items.slice(0, 5);
  const more = items.length - shown.length;
  const single = items.length === 1;

  const subject = input.digest
    ? `Your Scholarly community digest: ${items.length} new ${items.length === 1 ? "update" : "updates"}`
    : single
      ? items[0].type === "REPLY" || items[0].type === "ANSWER"
        ? `Someone replied to your message on Scholarly`
        : items[0].title.slice(0, 110)
      : `${items.length} new replies and mentions on Scholarly`;

  const intro = input.digest
    ? "Here is what happened in the Scholarly community since your last digest."
    : single
      ? items[0].channel
        ? `There is something new for you in <strong style="color:${C.ink};">#${escapeHtml(items[0].channel)}</strong>.`
        : "There is something new for you on Scholarly."
      : "A few things happened while you were away.";

  const html = `<!doctype html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>${escapeHtml(subject)}</title></head>
<body style="margin:0;padding:0;background:${C.canvas};font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,Helvetica,Arial,sans-serif;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">${escapeHtml(items[0]?.excerpt ?? "")}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:${C.canvas};"><tr><td align="center" style="padding:28px 12px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;">
    <tr><td style="padding:0 4px 16px;">
      <table role="presentation" cellpadding="0" cellspacing="0"><tr>
        <td style="background:${C.ink};border-radius:9px;width:30px;height:30px;text-align:center;vertical-align:middle;color:#ffffff;font-weight:800;font-size:15px;">S</td>
        <td style="padding-left:10px;font-size:17px;font-weight:700;color:${C.ink};letter-spacing:-.01em;">Scholarly <span style="font-weight:500;color:${C.muted};">Community</span></td>
      </tr></table>
    </td></tr>
    <tr><td style="background:${C.card};border:1px solid ${C.line};border-radius:16px;overflow:hidden;">
      <div style="height:4px;background:linear-gradient(90deg,${C.brand},#7c5ce8);"></div>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="padding:26px 26px 8px;">
        <p style="margin:0 0 6px;font-size:16px;color:${C.ink};font-weight:600;">Hello ${firstName(input.name)},</p>
        <p style="margin:0 0 22px;font-size:15px;line-height:1.6;color:${C.body};">${intro}</p>
        ${shown.map((it, i) => itemHtml(it, single && i === 0)).join(`<div style="height:1px;background:${C.line};margin:4px 0 18px;"></div>`)}
        ${more > 0 ? `<p style="margin:0 0 18px;font-size:14px;color:${C.muted};">…and ${more} more. <a href="${escapeHtml(input.inboxUrl)}" style="color:${C.brand};">See all notifications</a></p>` : ""}
        <p style="margin:8px 0 22px;font-size:14px;line-height:1.6;color:${C.muted};">Continue learning and sharing with your Scholarly community.</p>
      </td></tr></table>
    </td></tr>
    <tr><td style="padding:16px 8px 0;font-size:12px;line-height:1.6;color:${C.muted};text-align:center;">
      You are getting this because of activity on your posts on Scholarly.<br>
      <a href="${escapeHtml(input.settingsUrl)}" style="color:${C.muted};text-decoration:underline;">Change which emails you get</a>
    </td></tr>
  </table>
</td></tr></table>
</body></html>`;

  const text = [
    `Hello ${(input.name ?? "").trim().split(/\s+/)[0] || "there"},`,
    "",
    input.digest ? "Here is what happened in the Scholarly community." : "There is something new for you on Scholarly.",
    "",
    ...shown.flatMap((it) => [
      it.title + (it.channel ? ` (#${it.channel})` : ""),
      ...(it.context ? [`  In reply to: ${it.context}`] : []),
      `  ${it.excerpt}`,
      `  ${it.url}`,
      "",
    ]),
    ...(more > 0 ? [`…and ${more} more: ${input.inboxUrl}`, ""] : []),
    "Continue learning and sharing with your Scholarly community.",
    "",
    `Change which emails you get: ${input.settingsUrl}`,
  ].join("\n");

  return { subject, text, html };
}
