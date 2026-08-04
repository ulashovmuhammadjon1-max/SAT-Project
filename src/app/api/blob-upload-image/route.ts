import { NextResponse } from "next/server";
import { handleUpload, type HandleUploadBody } from "@vercel/blob/client";

import { auth } from "@/lib/auth";

// Token route for question/passage figure uploads (graphs, diagrams, tables
// rendered as images) — separate from /api/blob-upload since these need to
// be publicly viewable in the exam UI, unlike source PDFs.
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
          allowedContentTypes: ["image/png", "image/jpeg", "image/webp", "image/gif", "image/svg+xml"],
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
