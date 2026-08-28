import { NextResponse } from "next/server";
import { handleUpload, type HandleUploadBody } from "@vercel/blob/client";

import { auth } from "@/lib/auth";

/**
 * Upload token for classroom files — a student's handed-in work and a
 * teacher's worksheet both come through here.
 *
 * Uploads go from the browser straight to Blob storage rather than through a
 * server action, because Vercel caps a serverless request body at ~4.5MB and
 * a scanned worksheet or a photographed page routinely exceeds that. Only a
 * short-lived token round-trips through this route; the limits live here,
 * where the client cannot reach them.
 *
 * The stored blob URL is public-but-unguessable (random suffix), the same
 * tradeoff community chat attachments already make; who may *discover* a
 * URL is decided by the class-scoped download routes.
 */

const ALLOWED = ["application/pdf", "image/png", "image/jpeg", "image/webp"];

/** 10MB — a scanned worksheet, comfortably; never a video. */
const MAX_BYTES = 10 * 1024 * 1024;

export async function POST(request: Request): Promise<NextResponse> {
  const body = (await request.json()) as HandleUploadBody;

  try {
    const jsonResponse = await handleUpload({
      body,
      request,
      onBeforeGenerateToken: async () => {
        const session = await auth();
        if (!session?.user?.id) throw new Error("Sign in to upload a file.");
        return {
          allowedContentTypes: ALLOWED,
          maximumSizeInBytes: MAX_BYTES,
          // Two students uploading "homework.pdf" must not collide, and a
          // guessable path would let one overwrite another's work.
          addRandomSuffix: true,
        };
      },
      onUploadCompleted: async () => undefined,
    });
    return NextResponse.json(jsonResponse);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Upload authorization failed." },
      { status: 400 },
    );
  }
}
