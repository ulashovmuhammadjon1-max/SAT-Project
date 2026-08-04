import type { AIExtractionProvider } from "@/lib/ai/types";
import { HeuristicExtractionProvider } from "@/lib/ai/providers/heuristic-provider";

let cached: AIExtractionProvider | null = null;

// Pluggable by design: with no ANTHROPIC_API_KEY set, the pipeline runs
// end-to-end on the heuristic provider so the admin flow is fully testable
// without credentials. Setting the key swaps in the real Claude Opus 5
// extraction provider with no other code changes.
export function getExtractionProvider(): AIExtractionProvider {
  if (cached) return cached;

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (apiKey) {
    // Lazy import so the SDK is never bundled/initialized when unused.
    const { ClaudeExtractionProvider } = require("@/lib/ai/providers/claude-provider") as typeof import("@/lib/ai/providers/claude-provider");
    cached = new ClaudeExtractionProvider(apiKey);
  } else {
    cached = new HeuristicExtractionProvider();
  }

  return cached;
}
