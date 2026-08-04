import { NextResponse } from "next/server";
import { handleUpload, type HandleUploadBody } from "@vercel/blob/client";

import { auth } from "@/lib/auth";

// Client-side direct-to-blob upload: the browser uploads the PDF straight to
// Vercel Blob using a short-lived token minted here, bypassing the ~4.5MB
// request body limit Vercel's serverless functions impose on Server Actions
// and API routes. Only a short-lived token round-trips through this route.
export async function POST(request: Request): Promise<NextResponse> {
  const body = (await request.json()) as HandleUploadBody;

  try {
    const jsonResponse = await handleUpload({
      body,
      request,
      onBeforeGenerateToken: async () => {
        const session = await auth();
        if (session?.user?.role !== "ADMIN") {
          throw new Error("Not authorized.");
        }
        return {
          allowedContentTypes: ["application/pdf"],
          addRandomSuffix: true,
        };
      },
      onUploadCompleted: async () => undefined,
    });
    return NextResponse.json(jsonResponse);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Upload authorization failed." },
      { status: 400 }
    );
  }
}
