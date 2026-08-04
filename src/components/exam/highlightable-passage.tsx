"use client";

import { useCallback, useRef, useState } from "react";
import { Highlighter, StickyNote } from "lucide-react";

export function HighlightablePassage({ content }: { content: string }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [toolbar, setToolbar] = useState<{ x: number; y: number } | null>(null);

  const handleMouseUp = useCallback(() => {
    const selection = window.getSelection();
    if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
      setToolbar(null);
      return;
    }
    const range = selection.getRangeAt(0);
    if (!containerRef.current?.contains(range.commonAncestorContainer)) {
      setToolbar(null);
      return;
    }
    const rect = range.getBoundingClientRect();
    const containerRect = containerRef.current.getBoundingClientRect();
    setToolbar({ x: rect.left - containerRect.left + rect.width / 2, y: rect.top - containerRect.top - 36 });
  }, []);

  function wrapSelection(note?: string): HTMLElement | null {
    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) return null;
    const range = selection.getRangeAt(0);
    let mark: HTMLElement | null = null;
    try {
      mark = document.createElement("mark");
      mark.className = note ? "sat-highlight sat-note" : "sat-highlight";
      if (note) mark.title = note;
      range.surroundContents(mark);
    } catch {
      // Selection spans partial elements (e.g. crosses a <b> boundary) —
      // surroundContents can't wrap it cleanly; skip rather than corrupt the DOM.
      mark = null;
    }
    selection.removeAllRanges();
    setToolbar(null);
    return mark;
  }

  function applyHighlight() {
    wrapSelection();
  }

  function applyNote() {
    const note = window.prompt("Add a note for this selection:");
    if (note === null) return; // cancelled
    wrapSelection(note.trim() || undefined);
  }

  return (
    <div className="relative">
      {toolbar && (
        <div
          style={{ left: toolbar.x, top: toolbar.y }}
          className="absolute z-10 flex -translate-x-1/2 items-center gap-1 rounded-md bg-navy-900 p-1 text-xs font-medium text-white shadow-panel"
        >
          <button type="button" onClick={applyHighlight} className="flex items-center gap-1.5 rounded px-2 py-1 hover:bg-white/10">
            <Highlighter className="h-3.5 w-3.5" /> Highlight
          </button>
          <button type="button" onClick={applyNote} className="flex items-center gap-1.5 rounded px-2 py-1 hover:bg-white/10">
            <StickyNote className="h-3.5 w-3.5" /> Add note
          </button>
        </div>
      )}
      <div
        ref={containerRef}
        onMouseUp={handleMouseUp}
        className="select-text font-serif text-[16px] leading-relaxed text-navy-950"
        dangerouslySetInnerHTML={{ __html: content }}
      />
    </div>
  );
}
