/**
 * Storage for Writing Task 1 prompt images.
 *
 * A Task 1 prompt *is* a picture — a chart, a table, a process diagram — so a
 * student bringing their own Task 1 has to bring the figure with it, or there
 * is nothing to describe and nothing a reviewer can mark against.
 *
 * Mirrors `audio-storage.ts`: Vercel Blob when configured, private local disk
 * otherwise, with an unguessable stored name and a route that checks the
 * requester before streaming a byte. The existing `/api/blob-upload-image`
 * route is admin-only and Blob-only, so it cannot serve this.
 */
import { mkdir, readFile, writeFile } from "fs/promises";
import path from "path";
import { nanoid } from "nanoid";
import { put, get } from "@vercel/blob";

import {
  ACCEPTED_IMAGE_TYPES, MAX_IMAGE_BYTES, extensionFor,
} from "@/lib/ielts/image-types";

export * from "@/lib/ielts/image-types";

const ROOT = path.join(process.cwd(), "storage", "ielts-images");
export const blobConfigured = Boolean(
  process.env.BLOB_READ_WRITE_TOKEN || process.env.BLOB_STORE_ID
);


/**
 * Store a student's Task 1 figure.
 *
 * The type and size are re-checked here rather than trusted from the form: the
 * action is callable without the form, and this is a file written to disk.
 */
export async function savePromptImage(file: File, userId: string): Promise<string> {
  const contentType = (file.type || "").split(";")[0].trim().toLowerCase();
  if (!ACCEPTED_IMAGE_TYPES.includes(contentType)) {
    throw new Error("Upload a PNG, JPEG, WebP or GIF image.");
  }
  if (file.size > MAX_IMAGE_BYTES) {
    throw new Error("That image is larger than 8 MB. Try a smaller one.");
  }

  const buffer = Buffer.from(await file.arrayBuffer());
  const name = `${userId.slice(0, 6)}-${nanoid(20)}.${extensionFor(contentType)}`;

  if (blobConfigured) {
    const blob = await put(`ielts-images/${name}`, buffer, {
      access: "private",
      contentType,
    });
    return blob.pathname;
  }

  await mkdir(ROOT, { recursive: true });
  await writeFile(path.join(ROOT, name), buffer);
  return name;
}

export async function readPromptImage(stored: string): Promise<Buffer> {
  if (blobConfigured) {
    const blob = await get(stored, { access: "private" });
    if (!blob) throw new Error("Image not found.");
    return Buffer.from(await new Response(blob.stream).arrayBuffer());
  }
  const full = path.join(ROOT, stored);
  // `stored` comes from the database rather than a request, but a traversal
  // here would read arbitrary files off the server and the check costs nothing.
  if (!full.startsWith(ROOT)) throw new Error("Invalid image path.");
  return readFile(full);
}
