/**
 * Shared community types and limits.
 *
 * Kept out of the server-action modules because a `"use server"` file may only
 * export async functions — exporting a plain `const` from one is a build
 * error. The client needs the limits for its own validation.
 */

export const MAX_BODY = 4000;
export const PAGE_SIZE = 50;
/** Attachments per message. */
export const MAX_ATTACHMENTS = 4;
/** Messages one student may post per rolling minute, across all channels. */
export const RATE_LIMIT_PER_MINUTE = 12;
/** Poll limits. */
export const POLL_MIN_OPTIONS = 2;
export const POLL_MAX_OPTIONS = 6;
export const MAX_TITLE = 140;
export const MAX_SUBJECT = 60;
/** Attachment ceiling, enforced by the upload route and re-checked on post. */
export const MAX_ATTACHMENT_BYTES = 10 * 1024 * 1024;

export const ATTACHMENT_TYPES = [
  "image/png",
  "image/jpeg",
  "image/webp",
  "image/gif",
  "image/heic",
  "application/pdf",
] as const;

export type MessageKind = "MESSAGE" | "QUESTION" | "RESOURCE" | "ACHIEVEMENT" | "POLL" | "ANNOUNCEMENT";

/** The kinds a student can choose in the composer. Announcements are admin-only. */
export const STUDENT_KINDS: MessageKind[] = ["MESSAGE", "QUESTION", "RESOURCE", "ACHIEVEMENT", "POLL"];

export interface CommunityAuthor {
  id: string;
  name: string;
  image: string | null;
  isAdmin: boolean;
  isMentor: boolean;
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

export const REACTIONS = ["👍", "🎉", "🔥", "❤️", "😂", "🤔", "👀", "✅"] as const;
export type ReactionEmoji = (typeof REACTIONS)[number];

export interface ReactionSummary {
  emoji: string;
  count: number;
  mine: boolean;
}

export interface PollView {
  options: { id: string; label: string; votes: number }[];
  totalVotes: number;
  myVote: string | null;
  closed: boolean;
}

export interface CommunityMessageView {
  id: string;
  channelSlug: string;
  kind: MessageKind;
  title: string | null;
  subject: string | null;
  linkUrl: string | null;
  body: string;
  createdAt: string;
  editedAt: string | null;
  deleted: boolean;
  author: CommunityAuthor;
  /** The reader has blocked the author: the client collapses the message. */
  authorBlocked: boolean;
  attachments: CommunityAttachmentView[];
  mentionedMe: boolean;
  replyTo: {
    id: string;
    authorName: string;
    excerpt: string;
    deleted: boolean;
    /** Set when the parent lives in a thread, so "jump to" opens it. */
    threadRootId: string | null;
  } | null;
  /** Thread data — present on main-stream messages. */
  threadRootId: string | null;
  replyCount: number;
  lastReplyAt: string | null;
  acceptedAnswerId: string | null;
  isAcceptedAnswer: boolean;
  pinned: boolean;
  bookmarked: boolean;
  following: "FOLLOWING" | "MUTED" | null;
  poll: PollView | null;
  reactions: ReactionSummary[];
  canEdit: boolean;
  canDelete: boolean;
  canPin: boolean;
  /** QUESTION root: the asker or an admin may accept an answer. */
  canAccept: boolean;
}

export interface ChannelView {
  id: string;
  slug: string;
  name: string;
  description: string | null;
  icon: string;
  isReadOnly: boolean;
  slowModeSeconds: number;
  categoryId: string | null;
  unread: number;
  mentionsUnread: number;
  muted: boolean;
}

export interface CategoryView {
  id: string | null;
  name: string;
  channels: ChannelView[];
}

export interface NewAttachment {
  kind: "IMAGE" | "PDF" | "FILE";
  url: string;
  fileName: string;
  contentType: string;
  sizeBytes: number;
}

export interface NotificationView {
  id: string;
  type:
    | "REPLY"
    | "MENTION"
    | "REACTION"
    | "THREAD_REPLY"
    | "ANSWER"
    | "ANSWER_ACCEPTED"
    | "ANNOUNCEMENT"
    | "DIRECT_MESSAGE"
    | "MODERATION";
  title: string;
  body: string;
  url: string;
  read: boolean;
  createdAt: string;
  actor: { name: string; image: string | null } | null;
}

export interface MemberProfileView {
  id: string;
  name: string;
  image: string | null;
  joined: string;
  isAdmin: boolean;
  isMentor: boolean;
  isMe: boolean;
  bio: string | null;
  interests: string[];
  helpsWith: string[];
  studying: string[];
  posts: number;
  acceptedAnswers: number;
  activeNow: boolean;
  canMessage: boolean;
  blockedByMe: boolean;
}

/** What the sync endpoint returns. */
export interface SyncPayload {
  now: string;
  notificationsUnread: number;
  latestNotificationAt: string | null;
  dmUnread: number;
  /** Changes whenever any main-stream message anywhere is posted. */
  communityVersion: string | null;
  /** Changes when anything visible in the requested channel changes. */
  channelVersion: string | null;
  threadVersion: string | null;
  conversationVersion: string | null;
}
