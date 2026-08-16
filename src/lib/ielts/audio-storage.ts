/**
 * Storage for Speaking recordings.
 *
 * A student's voice is private. Recordings never go to a public path and are
 * never named predictably: the stored name carries a random id so possession
 * of a student id and a date cannot be turned into a URL. Serving is done by
 * `/api/ielts/audio/[recordingId]`, which checks the requester against the
 * submission before streaming a byte.
 *
 * Mirrors `lib/storage.ts` — Vercel Blob when configured, private local disk
 * otherwise — rather than forking it, because the fallback logic is the part
 * that makes local development work without credentials.
 */
import { mkdir, readFile, writeFile } from "fs/promises";
import path from "path";
import { nanoid } from "nanoid";
import { put, get } from "@vercel/blob";

const ROOT = path.join(process.cwd(), "storage", "ielts-audio");
export const blobConfigured = Boolean(
  process.env.BLOB_READ_WRITE_TOKEN || process.env.BLOB_STORE_ID
);

/** Types a browser's MediaRecorder actually produces. */
const EXT: Record<string, string> = {
  "audio/webm": "webm",
  "audio/ogg": "ogg",
  "audio/mp4": "m4a",
  "audio/mpeg": "mp3",
  "audio/wav": "wav",
};

export function extensionFor(mime: string): string {
  const base = (mime || "").split(";")[0].trim().toLowerCase();
  return EXT[base] ?? "webm";
}

export interface StoredAudio {
  /** What goes in `IeltsSpeakingRecording.audioUrl` — a key, not a URL. */
  path: string;
  size: number;
  contentType: string;
}

export async function saveAudioRecording(file: File, userId: string): Promise<StoredAudio> {
  const contentType = file.type || "audio/webm";
  const buffer = Buffer.from(await file.arrayBuffer());
  // The user id is hashed into the name only as a coarse shard; the random
  // component is what makes the name unguessable.
  const name = `${userId.slice(0, 6)}-${nanoid(20)}.${extensionFor(contentType)}`;

  if (blobConfigured) {
    const blob = await put(`ielts-audio/${name}`, buffer, {
      access: "private",
      contentType,
    });
    return { path: blob.pathname, size: buffer.byteLength, contentType };
  }

  await mkdir(ROOT, { recursive: true });
  await writeFile(path.join(ROOT, name), buffer);
  return { path: name, size: buffer.byteLength, contentType };
}

export async function readAudioRecording(stored: string): Promise<Buffer> {
  if (blobConfigured) {
    const blob = await get(stored, { access: "private" });
    if (!blob) throw new Error("Recording not found.");
    return Buffer.from(await new Response(blob.stream).arrayBuffer());
  }
  const full = path.join(ROOT, stored);
  // Refuse anything that escapes the audio directory. `stored` comes from the
  // database rather than a request, but a traversal here would read arbitrary
  // files off the server and the check costs nothing.
  if (!full.startsWith(ROOT)) throw new Error("Invalid recording path.");
  return readFile(full);
}

export function contentTypeFor(stored: string): string {
  const ext = stored.split(".").pop()?.toLowerCase() ?? "webm";
  const found = Object.entries(EXT).find(([, e]) => e === ext);
  return found?.[0] ?? "audio/webm";
}
