import { NextResponse } from "next/server";
import { handleUpload, type HandleUploadBody } from "@vercel/blob/client";

import { auth } from "@/lib/auth";

/**
 * Upload token for community chat attachments.
 *
 * Uploads go from the browser straight to Blob storage rather than through a
 * server action, because a phone screenshot routinely exceeds the 4.5MB body
 * limit on a serverless function — routing it through the app would fail on
 * exactly the attachment students most want to post.
 *
 * Separate from the admin figure-upload route: this one is open to any signed
 * in student, so it is deliberately narrow — a fixed content-type allowlist
 * and a size ceiling, both enforced here where the client cannot reach them.
 */

const ALLOWED = [
  "image/png",
  "image/jpeg",
  "image/webp",
  "image/gif",
  "image/heic",
  "application/pdf",
];

/** 10MB — comfortably above a phone screenshot, well below a video. */
const MAX_BYTES = 10 * 1024 * 1024;

export async function POST(request: Request): Promise<NextResponse> {
  const body = (await request.json()) as HandleUploadBody;

  try {
    const jsonResponse = await handleUpload({
      body,
      request,
      onBeforeGenerateToken: async () => {
        const session = await auth();
        if (!session?.user?.id) throw new Error("Sign in to attach a file.");
        return {
          allowedContentTypes: ALLOWED,
          maximumSizeInBytes: MAX_BYTES,
          // Random suffix: two students uploading "screenshot.png" must not
          // collide, and a guessable path would let one overwrite another's.
          addRandomSuffix: true,
        };
      },
      onUploadCompleted: async () => undefined,
    });
    return NextResponse.json(jsonResponse);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Upload failed." },
      { status: 400 }
    );
  }
}
