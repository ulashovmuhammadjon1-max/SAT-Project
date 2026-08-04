"use client";

import { useCallback, useState, type MouseEvent as ReactMouseEvent } from "react";
import { ChevronsDownUp, ChevronsUpDown, X } from "lucide-react";

/**
 * Bluebook's Line Reader: a movable clear band with the rest of the screen
 * masked, so the student can isolate a few lines of a passage at a time.
 */
export function LineReader({ onClose }: { onClose: () => void }) {
  const [top, setTop] = useState(() => Math.round(window.innerHeight * 0.4));
  const [height, setHeight] = useState(72);

  const startDrag = useCallback(
    (event: ReactMouseEvent) => {
      event.preventDefault();
      const offset = event.clientY - top;
      function onMove(e: MouseEvent) {
        setTop(Math.max(0, Math.min(window.innerHeight - height, e.clientY - offset)));
      }
      function onUp() {
        window.removeEventListener("mousemove", onMove);
        window.removeEventListener("mouseup", onUp);
      }
      window.addEventListener("mousemove", onMove);
      window.addEventListener("mouseup", onUp);
    },
    [top, height]
  );

  return (
    <div className="pointer-events-none fixed inset-0 z-30">
      <div className="absolute inset-x-0 top-0 bg-exam-strip/45" style={{ height: top }} />
      <div className="absolute inset-x-0 bottom-0 bg-exam-strip/45" style={{ top: top + height }} />

      <div
        onMouseDown={startDrag}
        className="pointer-events-auto absolute inset-x-0 cursor-grab border-y-2 border-exam-blue active:cursor-grabbing"
        style={{ top, height }}
      />

      <div
        className="pointer-events-auto absolute right-4 flex items-center gap-0.5 rounded-md border border-exam-border bg-white p-1 shadow-examPopup"
        style={{ top: top + height + 8 }}
      >
        <button
          type="button"
          onClick={() => setHeight((h) => Math.max(36, h - 16))}
          title="Fewer lines"
          className="flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
        >
          <ChevronsDownUp className="h-3.5 w-3.5" />
        </button>
        <button
          type="button"
          onClick={() => setHeight((h) => Math.min(320, h + 16))}
          title="More lines"
          className="flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
        >
          <ChevronsUpDown className="h-3.5 w-3.5" />
        </button>
        <span className="mx-1 h-4 w-px bg-exam-divider" />
        <button
          type="button"
          onClick={onClose}
          title="Close Line Reader"
          className="flex h-6 w-6 items-center justify-center rounded text-exam-muted hover:bg-exam-hover hover:text-exam-text"
        >
          <X className="h-3.5 w-3.5" />
        </button>
      </div>
    </div>
  );
}
