/**
 * Shared community-chat types and limits.
 *
 * Kept out of the server-action module because a `"use server"` file may only
 * export async functions — exporting a plain `const` from one is a build
 * error, and TypeScript does not catch it because the rule is Next's, not the
 * type system's. Interfaces would have been erased and survived; the numeric
 * limits would not, and the client needs them for its own validation.
 */

export const MAX_BODY = 4000;
export const PAGE_SIZE = 50;
/** Attachments per message. */
export const MAX_ATTACHMENTS = 4;
/** Messages one student may post per rolling minute. */
export const RATE_LIMIT_PER_MINUTE = 12;

export interface CommunityAuthor {
  id: string;
  name: string;
  isAdmin: boolean;
  isMe: boolean;
}

export interface CommunityAttachmentView {
  id: string;
  kind: "IMAGE" | "PDF" | "FILE";
  url: string;
  fileName: string;
  contentType: string;
  sizeBytes: number;
}

/** The emoji students may react with. A fixed set, enforced server-side, so
 *  the column can never hold arbitrary text and the picker stays scannable. */
export const REACTIONS = ["👍", "🎉", "🔥", "❤️", "😂", "🤔", "👀", "✅"] as const;
export type ReactionEmoji = (typeof REACTIONS)[number];

export interface ReactionSummary {
  emoji: string;
  count: number;
  /** Whether the signed-in student is one of them. */
  mine: boolean;
}

export interface CommunityMessageView {
  id: string;
  body: string;
  createdAt: string;
  editedAt: string | null;
  reactions: ReactionSummary[];
  /** Whether the signed-in user may edit it — author only, and not deleted. */
  canEdit: boolean;
  deleted: boolean;
  author: CommunityAuthor;
  attachments: CommunityAttachmentView[];
  mentionedMe: boolean;
  /** Enough of the parent to render a quoted preview. */
  replyTo: {
    id: string;
    authorName: string;
    excerpt: string;
    deleted: boolean;
  } | null;
  /** Whether the signed-in user may remove it. */
  canDelete: boolean;
}

export interface ChannelView {
  id: string;
  slug: string;
  name: string;
  description: string | null;
  isReadOnly: boolean;
  unread: number;
  mentionsUnread: number;
}

export interface NewAttachment {
  kind: "IMAGE" | "PDF" | "FILE";
  url: string;
  fileName: string;
  contentType: string;
  sizeBytes: number;
}
