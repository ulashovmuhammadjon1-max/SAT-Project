import { mkdir, readFile, writeFile, unlink } from "fs/promises";
import path from "path";
import { nanoid } from "nanoid";
import { put, get, del } from "@vercel/blob";

// Uploaded PDFs are kept out of any public path so raw source documents
// (often licensed test content) are never served unauthenticated. On Vercel,
// the deployment filesystem is read-only outside /tmp and /tmp isn't shared
// across invocations, so when a Blob store is configured (BLOB_READ_WRITE_TOKEN
// is set — see the Storage tab in the Vercel dashboard) uploads go there as
// private blobs instead. Local dev without that token falls back to disk.

const STORAGE_ROOT = path.join(process.cwd(), "storage", "uploads");
// A Blob store connected through the Vercel dashboard authenticates via OIDC
// (BLOB_STORE_ID + an auto-injected VERCEL_OIDC_TOKEN) rather than the older
// static BLOB_READ_WRITE_TOKEN, so check for either.
export const blobConfigured = Boolean(process.env.BLOB_READ_WRITE_TOKEN || process.env.BLOB_STORE_ID);
const useBlob = blobConfigured;

function sanitizeFileName(name: string): string {
  return name.replace(/[^a-zA-Z0-9._-]/g, "_").slice(-120);
}

export async function saveUploadedFile(
  file: File
): Promise<{ storedPath: string; fileName: string; fileSize: number }> {
  const fileName = sanitizeFileName(file.name || "upload.pdf");
  const storedName = `${nanoid(12)}-${fileName}`;
  const arrayBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);

  if (useBlob) {
    const blob = await put(`uploads/${storedName}`, buffer, {
      access: "private",
      contentType: "application/pdf",
    });
    return { storedPath: blob.pathname, fileName, fileSize: buffer.byteLength };
  }

  await mkdir(STORAGE_ROOT, { recursive: true });
  const storedPath = path.join(STORAGE_ROOT, storedName);
  await writeFile(storedPath, buffer);
  return { storedPath: storedName, fileName, fileSize: buffer.byteLength };
}

export async function readUploadedFile(storedName: string): Promise<Buffer> {
  if (useBlob) {
    const blob = await get(storedName, { access: "private" });
    if (!blob) throw new Error("Uploaded file not found in blob storage.");
    const arrayBuffer = await new Response(blob.stream).arrayBuffer();
    return Buffer.from(arrayBuffer);
  }

  const fullPath = path.join(STORAGE_ROOT, storedName);
  if (!fullPath.startsWith(STORAGE_ROOT)) {
    throw new Error("Invalid storage path.");
  }
  return readFile(fullPath);
}

export async function deleteUploadedFile(storedName: string): Promise<void> {
  if (useBlob) {
    await del(storedName).catch(() => undefined);
    return;
  }

  const fullPath = path.join(STORAGE_ROOT, storedName);
  if (!fullPath.startsWith(STORAGE_ROOT)) return;
  await unlink(fullPath).catch(() => undefined);
}
