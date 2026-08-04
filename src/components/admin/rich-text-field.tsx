"use client";

import { useRef } from "react";
import { Underline } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

// Digital SAT "Standard English Conventions" / "Boundaries" questions often
// underline a specific span of a passage or stem that the student must
// evaluate. PDF text extraction can't recover that formatting, so this gives
// admins a way to mark it by hand: select text, click Underline, and the
// span gets wrapped in <u> — the same HTML the stem/passage is already
// rendered with everywhere else (exam view, review, etc.).
export function RichTextField({
  value,
  onChange,
  rows = 3,
  className,
  placeholder,
}: {
  value: string;
  onChange: (value: string) => void;
  rows?: number;
  className?: string;
  placeholder?: string;
}) {
  const ref = useRef<HTMLTextAreaElement>(null);

  function toggleUnderline() {
    const el = ref.current;
    if (!el) return;
    const { selectionStart, selectionEnd } = el;
    if (selectionStart === selectionEnd) return;

    const before = value.slice(0, selectionStart);
    const selected = value.slice(selectionStart, selectionEnd);
    const after = value.slice(selectionEnd);
    const alreadyWrapped = selected.startsWith("<u>") && selected.endsWith("</u>");
    const next = alreadyWrapped ? before + selected.slice(3, -4) + after : before + `<u>${selected}</u>` + after;

    onChange(next);
    requestAnimationFrame(() => {
      el.focus();
      const newEnd = alreadyWrapped ? selectionEnd - 7 : selectionEnd + 7;
      el.setSelectionRange(selectionStart, newEnd);
    });
  }

  return (
    <div className="space-y-1.5">
      <Button type="button" variant="outline" size="sm" onClick={toggleUnderline} className="h-7 px-2 text-xs">
        <Underline className="h-3.5 w-3.5" /> Underline selection
      </Button>
      <Textarea
        ref={ref}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        rows={rows}
        className={className}
        placeholder={placeholder}
      />
    </div>
  );
}
