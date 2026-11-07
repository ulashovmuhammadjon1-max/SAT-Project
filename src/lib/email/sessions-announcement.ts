import { button, layout, para, type EmailMessage } from "@/lib/email";

/**
 * "New 1-on-1 sessions are open" — sent from Announcements to the most active
 * students. Times are given in Tashkent time with UTC alongside, because an
 * email cannot know the reader's timezone; the booking page shows their own.
 */

export interface AnnouncedSession {
  title: string | null;
  subject: string | null;
  startsAt: Date;
  hostName: string | null;
}

const esc = (s: string) =>
  s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]!);
const firstName = (n: string | null) => n?.trim().split(/\s+/)[0] || "";

function when(d: Date) {
  const local = d.toLocaleString("en-GB", {
    timeZone: "Asia/Tashkent",
    weekday: "short",
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  const utc = d.toLocaleString("en-GB", { timeZone: "UTC", hour: "2-digit", minute: "2-digit", hour12: false });
  return `${local} Tashkent (${utc} UTC)`;
}

export function buildSessionsAnnouncement(input: {
  to: string;
  name: string | null;
  sessions: AnnouncedSession[];
  instagram: string;
  telegram: string;
  contactEmail: string;
  origin: string;
}): EmailMessage {
  const name = firstName(input.name) || "there";
  const book = `${input.origin.replace(/\/$/, "")}/booking`;
  const lines = input.sessions.map((s) => ({
    title: s.title ?? "1-on-1 session",
    subject: s.subject ?? "SAT",
    host: firstName(s.hostName) || "a Scholarly mentor",
    when: when(s.startsAt),
  }));
  const n = lines.length;
  const subject = `${n} new 1-on-1 ${n === 1 ? "session is" : "sessions are"} open on Scholarly`;
  const unsubscribe = input.contactEmail
    ? `Do not want these updates? Write to ${input.contactEmail} and we will stop.`
    : "Do not want these updates? Reply and we will stop.";

  const text =
    `Hi ${name},\n\n` +
    `New 1-on-1 sessions were just published on Scholarly, and as one of our most active students you are hearing first.\n\n` +
    lines.map((l) => `- ${l.title} (${l.subject}) with ${l.host}: ${l.when}`).join("\n") +
    `\n\nEach session is one hour, just you and your mentor, and has one seat, so they go first come, first served. ` +
    `Sessions are booked with Scholarly coins, not money; the booking page shows your exact price and your balance.\n\n` +
    `Book here: ${book}\n\n` +
    `Before booking, follow ${input.instagram} on Instagram and join ${input.telegram} on Telegram. Reviewers check this before approving.\n\n` +
    `See you there,\nScholarly\n\n` +
    `You are getting this because you are one of the most active students on Scholarly. ${unsubscribe}`;

  const rows = lines
    .map(
      (l) =>
        `<tr><td style="padding:10px 0;border-top:1px solid #1e2b4a;">` +
        `<div style="color:#ffffff;font-weight:600;font-size:15px;">${esc(l.title)}</div>` +
        `<div style="color:#8a97b1;font-size:13px;margin-top:2px;">${esc(l.subject)} · with ${esc(l.host)}</div>` +
        `<div style="color:#c9d3e6;font-size:13px;margin-top:2px;">${esc(l.when)}</div></td></tr>`,
    )
    .join("");

  const html = layout(
    para(`Hi ${esc(name)},`) +
      para(
        `New <strong style="color:#ffffff;">1-on-1 sessions</strong> were just published on Scholarly, and as one of our most active students you are hearing first.`,
      ) +
      `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 16px;">${rows}</table>` +
      para(
        `Each session is one hour, just you and your mentor, and has <strong style="color:#ffffff;">one seat</strong>, so they go first come, first served. Sessions are booked with Scholarly coins, not money.`,
      ) +
      button(book, "See the sessions") +
      para(
        `<span style="color:#8a97b1;font-size:13px;">Before booking, follow <strong style="color:#c9d3e6;">${esc(input.instagram)}</strong> on Instagram and join <strong style="color:#c9d3e6;">${esc(input.telegram)}</strong> on Telegram. Reviewers check this before approving.</span>`,
      ) +
      para(
        `<span style="color:#5d6a85;font-size:12px;">You are getting this because you are one of the most active students on Scholarly. ${esc(unsubscribe)}</span>`,
      ),
  );

  return { to: input.to, subject, text, html };
}
