"use client";

import { useCallback, useRef, useState } from "react";
import { Highlighter } from "lucide-react";

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

  function applyHighlight() {
    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) return;
    const range = selection.getRangeAt(0);
    try {
      const mark = document.createElement("mark");
      mark.className = "sat-highlight";
      range.surroundContents(mark);
    } catch {
      // Selection spans partial elements (e.g. crosses a <b> boundary) —
      // surroundContents can't wrap it cleanly; skip rather than corrupt the DOM.
    }
    selection.removeAllRanges();
    setToolbar(null);
  }

  return (
    <div className="relative">
      {toolbar && (
        <button
          type="button"
          onClick={applyHighlight}
          style={{ left: toolbar.x, top: toolbar.y }}
          className="absolute z-10 flex -translate-x-1/2 items-center gap-1.5 rounded-md bg-navy-900 px-2.5 py-1.5 text-xs font-medium text-white shadow-panel"
        >
          <Highlighter className="h-3.5 w-3.5" /> Highlight
        </button>
      )}
      <div
        ref={containerRef}
        onMouseUp={handleMouseUp}
        className="select-text text-[15px] leading-relaxed"
        dangerouslySetInnerHTML={{ __html: content }}
      />
    </div>
  );
}
