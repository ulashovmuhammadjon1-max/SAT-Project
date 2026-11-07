import {
  ATTACHMENT_TYPES,
  MAX_ATTACHMENTS,
  MAX_ATTACHMENT_BYTES,
  type NewAttachment,
} from "@/lib/community/types";

/**
 * Server-side check of attachments a client says it uploaded.
 *
 * The browser uploads straight to Vercel Blob and then hands the server a URL.
 * Without this check a crafted request could attach any external URL as an
 * "image" and have every reader's browser load it. Only URLs on this project's
 * own public Blob store are accepted.
 *
 * The store is identified from BLOB_READ_WRITE_TOKEN
 * (`vercel_blob_rw_<storeId>_<secret>`): its hostname is
 * `<storeId>.public.blob.vercel-storage.com`. With no token configured nothing
 * can be uploaded anyway, so every URL is refused.
 */
const BLOB_SUFFIX = ".public.blob.vercel-storage.com";

function storeHostPrefix(): string | null {
  const token = process.env.BLOB_READ_WRITE_TOKEN ?? "";
  const m = /^vercel_blob_rw_([A-Za-z0-9]+)_/.exec(token);
  return m ? m[1].toLowerCase() : null;
}

export function isOwnBlobUrl(raw: string): boolean {
  let url: URL;
  try {
    url = new URL(raw);
  } catch {
    return false;
  }
  if (url.protocol !== "https:" || url.username || url.password || url.port) return false;
  const host = url.hostname.toLowerCase();
  if (!host.endsWith(BLOB_SUFFIX)) return false;
  const store = storeHostPrefix();
  // A test hook for local development only, never set in production.
  if (!store) return process.env.COMMUNITY_ALLOW_ANY_BLOB_HOST === "1";
  return host === `${store}${BLOB_SUFFIX}`;
}

function kindFor(contentType: string): NewAttachment["kind"] {
  if (contentType.startsWith("image/")) return "IMAGE";
  if (contentType === "application/pdf") return "PDF";
  return "FILE";
}

export function validateAttachments(
  input: unknown,
): { ok: true; attachments: NewAttachment[] } | { ok: false; error: string } {
  if (input == null) return { ok: true, attachments: [] };
  if (!Array.isArray(input)) return { ok: false, error: "Attachments are malformed." };
  if (input.length > MAX_ATTACHMENTS) return { ok: false, error: `Attach at most ${MAX_ATTACHMENTS} files.` };

  const out: NewAttachment[] = [];
  for (const raw of input) {
    if (!raw || typeof raw !== "object") return { ok: false, error: "Attachments are malformed." };
    const a = raw as Record<string, unknown>;
    const url = String(a.url ?? "");
    const contentType = String(a.contentType ?? "").split(";")[0].trim().toLowerCase();
    const sizeBytes = Number(a.sizeBytes ?? 0);
    const fileName = String(a.fileName ?? "file").slice(0, 200) || "file";
    if (!isOwnBlobUrl(url)) return { ok: false, error: "That attachment did not come from Scholarly's uploader." };
    if (!(ATTACHMENT_TYPES as readonly string[]).includes(contentType)) {
      return { ok: false, error: "Attach images (PNG, JPEG, WebP, GIF, HEIC) or PDFs only." };
    }
    if (!Number.isFinite(sizeBytes) || sizeBytes <= 0 || sizeBytes > MAX_ATTACHMENT_BYTES) {
      return { ok: false, error: "Each attachment must be under 10 MB." };
    }
    // The kind is derived here, never taken from the client.
    out.push({ url, contentType, sizeBytes: Math.round(sizeBytes), fileName, kind: kindFor(contentType) });
  }
  return { ok: true, attachments: out };
}
