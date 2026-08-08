"use client";

import { useEffect } from "react";

/**
 * Close-on-Escape for the exam's overlays.
 *
 * Several of them (the Highlights & Notes popup, the Line Reader) cover the
 * question with a full-screen catcher, so without this the only way out is the
 * mouse — which fails the keyboard-navigation requirement for the test UI.
 *
 * Deliberately not used by the calculator: it is a persistent tool the student
 * types into, and yanking it away on Escape mid-expression would be hostile.
 */
export function useEscape(active: boolean, onEscape: () => void) {
  useEffect(() => {
    if (!active) return;
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") {
        e.stopPropagation();
        onEscape();
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [active, onEscape]);
}
