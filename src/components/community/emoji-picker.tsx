"use client";

import { useState } from "react";

import { cn } from "@/lib/utils";

/**
 * A small curated picker. No library and no network: these are characters,
 * typed into the message like any other text.
 */
const GROUPS: { label: string; emoji: string[] }[] = [
  { label: "Smileys", emoji: ["😀", "😄", "😁", "😂", "🙂", "😊", "😍", "🤩", "😎", "🤔", "🫡", "😅", "😮", "😢", "😭", "😤", "😴", "🥳", "🤯", "🙃"] },
  { label: "Gestures", emoji: ["👍", "👎", "👏", "🙌", "🙏", "🤝", "💪", "✌️", "👌", "🤞", "👋", "✋", "👀", "🫶", "❤️", "💯"] },
  { label: "Study", emoji: ["📚", "📖", "✏️", "📝", "📐", "📏", "🧮", "🧪", "🔬", "🧠", "💡", "🎓", "🏫", "🗂️", "📊", "📈", "⏰", "☕", "🌙", "🎯"] },
  { label: "Celebrate", emoji: ["🎉", "🏆", "🥇", "🥈", "🥉", "⭐", "🌟", "✨", "🔥", "🚀", "🎊", "👑", "💎", "🍀", "🌈", "✅"] },
  { label: "Symbols", emoji: ["❓", "❗", "⚠️", "✔️", "❌", "➕", "➖", "➗", "✖️", "∞", "π", "√", "≈", "≠", "≤", "≥", "°", "→", "←", "⇒"] },
];

export function EmojiPicker({ onPick, className }: { onPick: (e: string) => void; className?: string }) {
  const [tab, setTab] = useState(0);
  return (
    <div className={cn("w-72 max-w-[calc(100vw-1.5rem)] rounded-xl border border-border bg-popover p-2 shadow-xl", className)}>
      <div className="mb-2 flex gap-1 overflow-x-auto no-scrollbar" role="tablist">
        {GROUPS.map((g, i) => (
          <button
            key={g.label}
            type="button"
            role="tab"
            aria-selected={tab === i}
            onClick={() => setTab(i)}
            className={cn(
              "shrink-0 rounded-md px-2 py-1 text-xs font-medium transition-colors",
              tab === i ? "bg-primary/10 text-primary" : "text-muted-foreground hover:bg-secondary",
            )}
          >
            {g.label}
          </button>
        ))}
      </div>
      <div className="grid grid-cols-8 gap-0.5">
        {GROUPS[tab].emoji.map((e) => (
          <button
            key={e}
            type="button"
            onClick={() => onPick(e)}
            className="flex h-8 w-8 items-center justify-center rounded-md text-lg transition-transform hover:scale-110 hover:bg-secondary"
            aria-label={e}
          >
            {e}
          </button>
        ))}
      </div>
    </div>
  );
}
