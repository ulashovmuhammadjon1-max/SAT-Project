"use client";

import { useMemo } from "react";
import katex from "katex";

/**
 * Renders question/passage/choice content that may contain a mix of HTML
 * and LaTeX math. Matches Bluebook's own typeset math (stacked fractions,
 * true superscript/subscript exponents, radicals) instead of plain-text
 * approximations like "A/P - 1" or "x^2".
 *
 * Math segments are delimited the standard LaTeX way:
 *   \( ... \)  inline math (renders in the flow of the sentence)
 *   \[ ... \]  block/display math (its own centered line)
 * Everything outside those delimiters is treated as regular HTML, exactly
 * like the rest of the stem/passage content already is.
 */

const MATH_DELIMITER = /\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)/g;

function renderMathContent(raw: string): string {
  if (!raw) return "";
  if (!raw.includes("\\(") && !raw.includes("\\[")) return raw;

  return raw.replace(MATH_DELIMITER, (match, display: string | undefined, inline: string | undefined) => {
    const isDisplay = display !== undefined;
    const tex = (isDisplay ? display : inline) ?? "";
    try {
      return katex.renderToString(tex, {
        throwOnError: false,
        displayMode: isDisplay,
        output: "html",
      });
    } catch {
      // Malformed LaTeX from a bad extraction/edit shouldn't blank the
      // question -- fall back to showing the raw source instead.
      return match;
    }
  });
}

export function MathContent({ html, className }: { html: string; className?: string }) {
  const rendered = useMemo(() => renderMathContent(html), [html]);
  return <span className={className} dangerouslySetInnerHTML={{ __html: rendered }} />;
}
