"use client";

import { useEffect, useRef, useState } from "react";
import { X } from "lucide-react";

import { Button } from "@/components/ui/button";

declare global {
  interface Window {
    Desmos?: { GraphingCalculator: (el: HTMLElement, opts?: Record<string, unknown>) => unknown };
  }
}

export function CalculatorPanel({ onClose }: { onClose: () => void }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    let cancelled = false;
    let calculator: { destroy?: () => void } | null = null;

    function mount() {
      if (cancelled || !containerRef.current || !window.Desmos) return;
      calculator = window.Desmos.GraphingCalculator(containerRef.current, {
        keypad: true,
        expressions: true,
        settingsMenu: false,
      }) as { destroy?: () => void };
    }

    if (window.Desmos) {
      mount();
    } else {
      const script = document.createElement("script");
      script.src = "https://www.desmos.com/api/v1.9/calculator.js";
      script.async = true;
      script.onload = mount;
      script.onerror = () => !cancelled && setFailed(true);
      document.body.appendChild(script);
    }

    return () => {
      cancelled = true;
      calculator?.destroy?.();
    };
  }, []);

  return (
    <div className="fixed bottom-4 right-4 z-40 w-[380px] overflow-hidden rounded-xl border border-border bg-background shadow-panel sm:w-[420px]">
      <div className="flex items-center justify-between border-b border-border bg-secondary px-3 py-2">
        <span className="text-sm font-medium">Graphing calculator</span>
        <Button variant="ghost" size="icon" className="h-7 w-7" onClick={onClose}>
          <X className="h-4 w-4" />
        </Button>
      </div>
      {failed ? (
        <p className="p-6 text-center text-sm text-muted-foreground">
          The calculator couldn&apos;t load (no network access). It will work normally once deployed with internet
          access to the Desmos API.
        </p>
      ) : (
        <div ref={containerRef} className="h-[420px] w-full" />
      )}
    </div>
  );
}
