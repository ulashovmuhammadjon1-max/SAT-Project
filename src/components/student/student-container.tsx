"use client";

import { usePathname } from "next/navigation";

import { cn } from "@/lib/utils";

/**
 * The width of a student page.
 *
 * Every page is centred at `max-w-6xl`, which is right for a dashboard read
 * top-to-bottom and wrong for a chat: it left the community channel squeezed
 * into a column with a sidebar beside it and empty space either side. Chat
 * wants the room, so it opts out here rather than every other page opting in.
 */
export function StudentContainer({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const wide = pathname?.startsWith("/community");

  return (
    <div className={cn("animate-fade-in mx-auto", wide ? "max-w-none" : "max-w-6xl")}>
      {children}
    </div>
  );
}
