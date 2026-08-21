import { locateQuote, resolveAnalysis, countWords, hashEssayText } from "@/lib/ielts/essay-analysis";

const essay = `Public transport plays a crucial role in modern cities.
Although it requires investment, it plays a crucial role in cutting emissions.
Governments should therefore expand it, because it plays a crucial role long term.`;

let pass = 0, fail = 0;
const check = (name: string, got: unknown, want: unknown) => {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  ok ? pass++ : fail++;
  console.log(`${ok ? "PASS" : "FAIL"}  ${name}${ok ? "" : `\n        got  ${JSON.stringify(got)}\n        want ${JSON.stringify(want)}`}`);
};
const at = (s: { startOffset: number; endOffset: number } | null) =>
  s ? essay.slice(s.startOffset, s.endOffset) : null;

// The repeated-phrase case the spec calls out: "plays a crucial role" x3.
const occ1 = locateQuote(essay, "plays a crucial role", 1);
const occ2 = locateQuote(essay, "plays a crucial role", 2);
const occ3 = locateQuote(essay, "plays a crucial role", 3);
check("occurrence 1 resolves", at(occ1), "plays a crucial role");
check("occurrence 2 resolves", at(occ2), "plays a crucial role");
check("occurrence 3 resolves", at(occ3), "plays a crucial role");
check("the three occurrences are DIFFERENT spans",
  new Set([occ1!.startOffset, occ2!.startOffset, occ3!.startOffset]).size, 3);
check("occurrence 2 is after occurrence 1", occ2!.startOffset > occ1!.startOffset, true);
check("occurrence 3 is after occurrence 2", occ3!.startOffset > occ2!.startOffset, true);

// A quote the model reproduced across a line break in the essay.
const across = locateQuote(essay, "modern cities. Although it requires investment", 1);
check("whitespace-insensitive match across a newline", across !== null, true);
check("  ...and lands on real text", at(across)?.includes("Although"), true);

// Things that must be rejected rather than guessed.
check("absent quote returns null", locateQuote(essay, "carbon capture technology", 1), null);
check("empty quote returns null", locateQuote(essay, "   ", 1), null);
// Occurrence 9 of an AMBIGUOUS phrase (3 instances) must be dropped, not
// guessed at — placing it on the first would highlight the wrong sentence
// while looking entirely convincing.
check("over-count on a repeated phrase is DROPPED",
  locateQuote(essay, "plays a crucial role", 9), null);
// The same miscount on a phrase that occurs exactly once is safe to correct:
// there is no other instance it could wrongly land on.
check("over-count on a unique phrase is corrected",
  at(locateQuote(essay, "Governments should therefore expand it", 4)),
  "Governments should therefore expand it");

// resolveAnalysis: quote is rewritten to the true text, bad ones dropped.
const resolved = resolveAnalysis(essay, {
  annotations: [
    { category: "COLLOCATION", subtype: "high_value_phrase", quote: "plays a crucial role",
      occurrence: 2, explanation: "e", ieltsValue: "v", pattern: null, confidence: 0.9 },
    { category: "GRAMMAR", subtype: "concessive_clause", quote: "Although it requires investment",
      occurrence: 1, explanation: "e", ieltsValue: "v", pattern: null, confidence: 0.8 },
    { category: "VOCABULARY", subtype: "topic_specific", quote: "nuclear fusion",
      occurrence: 1, explanation: "e", ieltsValue: "v", pattern: null, confidence: 0.7 },
    // exact duplicate of the first — same category, same span
    { category: "COLLOCATION", subtype: "high_value_phrase", quote: "plays a crucial role",
      occurrence: 2, explanation: "e2", ieltsValue: "v2", pattern: null, confidence: 0.6 },
  ],
  ideas: [{ claim: "c", explanation: "e", consequence: null, example: null,
            anchorQuote: "Governments should therefore expand it" }],
});
check("hallucinated quote dropped", resolved.annotations.length, 2);
check("drop is reported to the admin", resolved.warnings.length, 1);
check("warning names the essay-absent reason",
  /not found in the essay/.test(resolved.warnings[0]), true);
check("duplicate span collapsed", resolved.annotations.filter(a => a.category === "COLLOCATION").length, 1);
check("annotations sorted by position",
  resolved.annotations.map(a => a.startOffset).every((v, i, arr) => i === 0 || arr[i-1] <= v), true);
check("idea anchored", resolved.ideas[0].startOffset !== null, true);

// EVERY stored quote must equal the text at its own offsets — the invariant the
// whole highlight layer depends on.
check("stored quote === essay.slice(start,end) for all",
  resolved.annotations.every(a => essay.slice(a.startOffset, a.endOffset) === a.quote), true);

check("countWords", countWords("  one two   three \n four "), 4);
check("hash is stable", hashEssayText(essay) === hashEssayText(essay), true);
check("hash changes on edit", hashEssayText(essay) === hashEssayText(essay + "."), false);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
