import { Badge } from "@/components/ui/badge";
import { MathContent } from "@/components/shared/math-content";
import type { PreviewQuestion } from "@/server/actions/teacher/question-sets";

/**
 * A question set rendered in full for the teacher — stem, passage, figure,
 * choices with the key marked, free-response answers. Server-renderable: the
 * passage fold is a native <details>, no client state needed.
 */
export function QuestionList({ questions }: { questions: PreviewQuestion[] }) {
  return (
    <ul className="divide-y divide-border/60">
      {questions.map((q, i) => (
        <li key={q.id} className="px-4 py-4 sm:px-5">
          <div className="flex items-start gap-3">
            <span className="mt-0.5 w-6 shrink-0 text-sm tabular-nums text-muted-foreground">
              {i + 1}.
            </span>
            <div className="min-w-0 flex-1">
              <div className="flex flex-wrap items-center gap-1.5">
                <Badge variant="outline" className="text-[10px]">{q.skillName}</Badge>
                <Badge variant="secondary" className="text-[10px]">
                  {q.difficulty.charAt(0) + q.difficulty.slice(1).toLowerCase()}
                </Badge>
              </div>

              {q.passage && (
                <details className="mt-2 rounded-lg bg-secondary/40">
                  <summary className="cursor-pointer select-none px-3 py-2 text-xs font-medium text-muted-foreground">
                    Passage
                  </summary>
                  <div className="max-h-64 overflow-y-auto px-3 pb-3 text-sm leading-relaxed">
                    <MathContent html={q.passage} />
                  </div>
                </details>
              )}

              <div className="mt-2 text-sm leading-relaxed [&_table]:my-2 [&_table]:text-xs">
                <MathContent html={q.stem} />
              </div>

              {q.imageUrl && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={q.imageUrl} alt="" className="mt-2 max-h-56 rounded-md" />
              )}

              {q.choices.length > 0 ? (
                <ul className="mt-2 space-y-1 text-sm">
                  {q.choices.map((c) => (
                    <li
                      key={c.label}
                      className={c.isCorrect ? "font-medium text-success" : "text-muted-foreground"}
                    >
                      <span className="mr-1.5">{c.label}.</span>
                      <MathContent html={c.content} />
                      {c.isCorrect && <span className="ml-1.5 text-xs">← answer</span>}
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="mt-2 text-sm">
                  <span className="text-muted-foreground">Student-produced response. Answer: </span>
                  <span className="font-medium text-success">{frAnswer(q.correctAnswerFR)}</span>
                </p>
              )}
            </div>
          </div>
        </li>
      ))}
    </ul>
  );
}

/** `correctAnswerFR` is a JSON-encoded array string, e.g. '["40"]'. */
function frAnswer(raw: string | null): string {
  if (!raw) return "—";
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed.join(" or ") : String(parsed);
  } catch {
    return raw;
  }
}
