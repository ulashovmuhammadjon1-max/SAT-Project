"use client";

import { useEffect, useRef, useState, type PointerEvent as ReactPointerEvent } from "react";
import { GripHorizontal, MoveDiagonal2, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface DesmosInstance {
  destroy?: () => void;
  resize?: () => void;
}

declare global {
  interface Window {
    Desmos?: {
      GraphingCalculator: (el: HTMLElement, opts?: Record<string, unknown>) => DesmosInstance;
      ScientificCalculator: (el: HTMLElement, opts?: Record<string, unknown>) => DesmosInstance;
    };
  }
}

type Mode = "graphing" | "scientific";

const DEFAULT_WIDTH = 400;
const DEFAULT_HEIGHT = 480;
const MIN_WIDTH = 320;
const MIN_HEIGHT = 340;

// Desmos now requires an apiKey query param on every request — omitting it
// returns a 403 and the calculator never loads. This is Desmos's public demo
// key (fine for prototyping); swap in a real key via NEXT_PUBLIC_DESMOS_API_KEY
// once one is registered at desmos.com/api, since the demo key isn't licensed
// for production/commercial use.
const DESMOS_API_KEY = process.env.NEXT_PUBLIC_DESMOS_API_KEY || "dcb31709b452b1cf9dc26972add0fda6";

function clamp(value: number, min: number, max: number) {
  return Math.min(Math.max(value, min), max);
}

export function CalculatorPanel({ onClose }: { onClose: () => void }) {
  const panelRef = useRef<HTMLDivElement>(null);
  const mountRef = useRef<HTMLDivElement>(null);
  const calculatorRef = useRef<DesmosInstance | null>(null);
  const [mode, setMode] = useState<Mode>("graphing");
  const [failed, setFailed] = useState(false);
  // null = anchored to the default bottom-right corner via CSS; set once the
  // student drags the panel so it switches to explicit pixel positioning.
  const [pos, setPos] = useState<{ x: number; y: number } | null>(null);
  const [size, setSize] = useState({ width: DEFAULT_WIDTH, height: DEFAULT_HEIGHT });

  // (Re)mount the Desmos calculator whenever the mode changes, reusing the
  // already-loaded script after the first mount.
  useEffect(() => {
    let cancelled = false;

    function mount() {
      if (cancelled || !mountRef.current) return;
      if (!window.Desmos) {
        // The script tag itself can "load" even when Desmos responds with an
        // error body (e.g. a rejected/missing apiKey) rather than real JS, so
        // window.Desmos never gets defined — treat that the same as a load failure.
        setFailed(true);
        return;
      }
      mountRef.current.innerHTML = "";
      const factory = mode === "graphing" ? window.Desmos.GraphingCalculator : window.Desmos.ScientificCalculator;
      if (!factory) return;
      calculatorRef.current = factory(
        mountRef.current,
        mode === "graphing" ? { keypad: true, expressions: true, settingsMenu: false } : { keypad: true }
      );
    }

    if (window.Desmos) {
      mount();
    } else {
      const script = document.createElement("script");
      script.src = `https://www.desmos.com/api/v1.12/calculator.js?apiKey=${DESMOS_API_KEY}`;
      script.async = true;
      script.onload = mount;
      script.onerror = () => !cancelled && setFailed(true);
      document.body.appendChild(script);
    }

    return () => {
      cancelled = true;
      calculatorRef.current?.destroy?.();
      calculatorRef.current = null;
    };
  }, [mode]);

  // Desmos renders onto an internal canvas that doesn't auto-follow CSS size
  // changes, so nudge it whenever the panel is resized.
  useEffect(() => {
    calculatorRef.current?.resize?.();
  }, [size.width, size.height]);

  function startDrag(event: ReactPointerEvent<HTMLDivElement>) {
    if ((event.target as HTMLElement).closest("[data-drag-ignore]")) return;
    const rect = panelRef.current?.getBoundingClientRect();
    if (!rect) return;
    const startX = event.clientX;
    const startY = event.clientY;
    const origX = pos?.x ?? rect.left;
    const origY = pos?.y ?? rect.top;

    function onMove(e: PointerEvent) {
      const nextX = clamp(origX + (e.clientX - startX), 0, window.innerWidth - 60);
      const nextY = clamp(origY + (e.clientY - startY), 0, window.innerHeight - 40);
      setPos({ x: nextX, y: nextY });
    }
    function onUp() {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
    }
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
  }

  function startResize(event: ReactPointerEvent<HTMLDivElement>) {
    event.preventDefault();
    event.stopPropagation();
    const startX = event.clientX;
    const startY = event.clientY;
    const startW = size.width;
    const startH = size.height;
    const rect = panelRef.current?.getBoundingClientRect();
    const maxWidth = Math.min(900, window.innerWidth - (rect?.left ?? 16) - 8);
    const maxHeight = Math.min(800, window.innerHeight - (rect?.top ?? 16) - 8);

    function onMove(e: PointerEvent) {
      setSize({
        width: clamp(startW + (e.clientX - startX), MIN_WIDTH, maxWidth),
        height: clamp(startH + (e.clientY - startY), MIN_HEIGHT, maxHeight),
      });
    }
    function onUp() {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
    }
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
  }

  return (
    <div
      ref={panelRef}
      style={{
        position: "fixed",
        ...(pos ? { left: pos.x, top: pos.y } : { right: 16, bottom: 70 }),
        width: size.width,
        height: size.height,
      }}
      className="relative z-40 flex flex-col overflow-hidden rounded-md border border-exam-border bg-white shadow-examPopup"
    >
      <div
        onPointerDown={startDrag}
        className="flex shrink-0 cursor-move select-none items-center justify-between border-b border-exam-divider bg-exam-header px-3 py-2"
      >
        <div className="flex items-center gap-1.5">
          <GripHorizontal className="h-3.5 w-3.5 text-exam-muted" />
          <span className="text-[13px] font-semibold text-exam-text">Calculator</span>
        </div>
        <Button
          variant="ghost"
          size="icon"
          data-drag-ignore
          className="h-6 w-6 text-exam-muted hover:bg-exam-hover hover:text-exam-text"
          onClick={onClose}
          aria-label="Close Calculator"
        >
          <X className="h-4 w-4" />
        </Button>
      </div>

      <div
        data-drag-ignore
        className="flex shrink-0 items-center gap-1 border-b border-exam-divider px-2 py-1.5"
      >
        {(["graphing", "scientific"] as const).map((m) => (
          <button
            key={m}
            type="button"
            onClick={() => setMode(m)}
            className={cn(
              "rounded px-2.5 py-1 text-[12px] font-medium capitalize transition-colors",
              mode === m ? "bg-exam-blue text-white" : "text-exam-muted hover:bg-exam-hover hover:text-exam-text"
            )}
          >
            {m}
          </button>
        ))}
      </div>

      {failed ? (
        <p className="p-6 text-center text-[13px] leading-[1.6] text-exam-muted">
          The calculator couldn&apos;t load (no network access). It will work normally once deployed with internet
          access to the Desmos API.
        </p>
      ) : (
        <div ref={mountRef} className="min-h-0 w-full flex-1" />
      )}

      <div
        onPointerDown={startResize}
        data-drag-ignore
        className="absolute bottom-0.5 right-0.5 flex h-4 w-4 cursor-nwse-resize items-center justify-center text-exam-muted hover:text-exam-text"
        aria-label="Resize calculator"
      >
        <MoveDiagonal2 className="h-3 w-3" />
      </div>
    </div>
  );
}
