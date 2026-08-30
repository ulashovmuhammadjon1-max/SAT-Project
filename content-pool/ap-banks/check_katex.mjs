/**
 * Parse every \( ... \) span produced by mathfmt.py with KaTeX itself.
 *
 *   node check_katex.mjs spans.json
 *
 * A span the site's renderer cannot parse is a span that would reach a student
 * as raw backslashes, so it is a defect even though the round-trip gate is
 * happy with it. `throwOnError: false` is what MathContent uses in production,
 * which means a broken span renders as red source text instead of throwing --
 * so the check has to run with throwOnError TRUE to see the failure at all.
 * That difference is the whole reason this file exists.
 */
import katex from "katex";
import { readFileSync } from "fs";

const spans = JSON.parse(readFileSync(process.argv[2], "utf8"));

// Positive and negative controls, so a green run means something. If KaTeX
// ever stops rejecting the broken one, this check has quietly become a no-op.
const CONTROL_OK = String.raw`\frac{x^{2}}{\sqrt{y}} + \int_{0}^{1} f\left(t\right)\,dt`;
const CONTROL_BAD = String.raw`\frac{1}{`;
try {
  katex.renderToString(CONTROL_OK, { throwOnError: true });
} catch (e) {
  console.error("CONTROL FAILED: KaTeX rejected known-good LaTeX:", e.message);
  process.exit(2);
}
let rejectedBad = false;
try {
  katex.renderToString(CONTROL_BAD, { throwOnError: true });
} catch {
  rejectedBad = true;
}
if (!rejectedBad) {
  console.error("CONTROL FAILED: KaTeX accepted known-broken LaTeX");
  process.exit(2);
}

let bad = 0;
const seen = new Set();
for (const [where, tex] of spans) {
  if (seen.has(tex)) continue;
  seen.add(tex);
  try {
    katex.renderToString(tex, { throwOnError: true, strict: false });
  } catch (e) {
    bad++;
    if (bad <= 40) console.log(`${where}\n   ${tex}\n   -> ${e.message}`);
  }
}
console.log(`${spans.length} spans (${seen.size} distinct); ${bad} rejected by KaTeX`);
process.exit(bad ? 1 : 0);
