/**
 * Typeset every math span in Test 31 with the same KaTeX the exam uses and
 * fail on any span KaTeX cannot parse.
 *
 * Why this exists: the exam renders a span through
 * src/components/shared/math-content.tsx, which calls katex.renderToString
 * with throwOnError:false. A malformed span therefore does not crash — it
 * renders as red error text inside the question, and no Python style check
 * can see that. Two questions already live in production (Test 5 M2H Q11 and
 * Test 6 M2H Q12) write `&lt;` inside a math span, which KaTeX reads as an
 * alignment `&` followed by the letters `lt;`. This check catches that class
 * of defect; `\lt` and `\gt` are the correct spellings.
 *
 * Run after verify_math_test31.py, which writes math_spans.json:
 *   node katex_check.mjs
 */
import katex from "katex";
import { readFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const spans = JSON.parse(readFileSync(path.join(HERE, "math_spans.json"), "utf8"));

const failures = [];
for (const { tag, tex } of spans) {
  try {
    katex.renderToString(tex, { throwOnError: true, output: "html" });
  } catch (err) {
    failures.push(`${tag}: ${JSON.stringify(tex)} -> ${err.message}`);
  }
  // throwOnError:true covers parse errors; a stray `&` outside an environment
  // is reported by KaTeX as a parse error too, so the one check is enough.
}

console.log(`katex: ${spans.length} math spans typeset, ${failures.length} failed`);
for (const f of failures) console.log("  -", f);
process.exit(failures.length ? 1 : 0);
