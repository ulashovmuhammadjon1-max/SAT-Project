import { mkdir, readFile, writeFile } from "fs/promises";
import path from "path";
import { nanoid } from "nanoid";

// Local-disk storage for uploaded PDFs, kept outside `public/` so raw source
// documents (often licensed test content) are never served unauthenticated.
// Swap this module for an S3/Vercel Blob client in production — nothing else
// in the ingestion pipeline depends on the storage mechanism.

const STORAGE_ROOT = path.join(process.cwd(), "storage", "uploads");

function sanitizeFileName(name: string): string {
  return name.replace(/[^a-zA-Z0-9._-]/g, "_").slice(-120);
}

export async function saveUploadedFile(
  file: File
): Promise<{ storedPath: string; fileName: string; fileSize: number }> {
  await mkdir(STORAGE_ROOT, { recursive: true });

  const fileName = sanitizeFileName(file.name || "upload.pdf");
  const storedName = `${nanoid(12)}-${fileName}`;
  const storedPath = path.join(STORAGE_ROOT, storedName);

  const arrayBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);
  await writeFile(storedPath, buffer);

  return { storedPath: storedName, fileName, fileSize: buffer.byteLength };
}

export async function readUploadedFile(storedName: string): Promise<Buffer> {
  const fullPath = path.join(STORAGE_ROOT, storedName);
  if (!fullPath.startsWith(STORAGE_ROOT)) {
    throw new Error("Invalid storage path.");
  }
  return readFile(fullPath);
}
