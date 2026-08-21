import { buildSegments, annotationIsIntact, type SegmentAnnotation } from "@/lib/ielts/essay-segments";

const text = "Although public transport plays a crucial role in reducing urban congestion, it needs funding.";
const ann = (id: string, category: SegmentAnnotation["category"], quote: string): SegmentAnnotation => {
  const startOffset = text.indexOf(quote);
  return { id, category, subtype: "s", quote, startOffset, endOffset: startOffset + quote.length,
           explanation: "e", ieltsValue: null, pattern: null };
};

// Deliberately overlapping, exactly the case the brief calls out.
const annotations = [
  ann("g", "GRAMMAR", "Although public transport plays a crucial role in reducing urban congestion"),
  ann("c", "COLLOCATION", "plays a crucial role"),
  ann("v", "VOCABULARY", "urban congestion"),
];

let pass = 0, fail = 0;
const check = (name: string, got: unknown, want: unknown) => {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  ok ? pass++ : fail++;
  console.log(`${ok ? "PASS" : "FAIL"}  ${name}${ok ? "" : `\n        got  ${JSON.stringify(got)}\n        want ${JSON.stringify(want)}`}`);
};

const segs = buildSegments(text, annotations);

// THE critical invariant: the essay must render exactly as written.
check("segments reproduce the essay byte-for-byte", segs.map(s => s.text).join(""), text);
check("segments are contiguous",
  segs.every((s, i) => i === 0 || segs[i-1].end === s.start), true);
check("segments are in order",
  segs.every((s, i) => i === 0 || segs[i-1].start < s.start), true);

// Overlap resolution.
const collocationSeg = segs.find(s => s.text === "plays a crucial role")!;
check("overlapping span sees BOTH annotations", collocationSeg.annotations.length, 2);
check("collocation outranks grammar on the shared span", collocationSeg.annotations[0].category, "COLLOCATION");

const vocabSeg = segs.find(s => s.text === "urban congestion")!;
check("vocabulary span sees both too", vocabSeg.annotations.length, 2);
check("grammar outranks vocabulary", vocabSeg.annotations[0].category, "GRAMMAR");

// Toggling a category off must remove it and still reproduce the text.
const only = buildSegments(text, annotations, new Set(["VOCABULARY" as const]));
check("filtered still reproduces the essay", only.map(s => s.text).join(""), text);
check("filtered shows only vocabulary",
  [...new Set(only.flatMap(s => s.annotations.map(a => a.category)))], ["VOCABULARY"]);
const none = buildSegments(text, annotations, new Set([]));
check("all categories off = one clean segment", none.length, 1);
check("  ...and it is the whole essay", none[0].text, text);

// A corrupt row must not blank the page.
const bad: SegmentAnnotation = { id: "x", category: "GRAMMAR", subtype: "s", quote: "zzz",
  startOffset: 5000, endOffset: 5010, explanation: "e", ieltsValue: null, pattern: null };
const withBad = buildSegments(text, [...annotations, bad]);
check("out-of-range annotation ignored, essay intact", withBad.map(s => s.text).join(""), text);

check("intact annotation detected", annotationIsIntact(text, annotations[1]), true);
check("drifted annotation detected", annotationIsIntact(text, { ...annotations[1], startOffset: 3 }), false);
check("empty essay yields no segments", buildSegments("", []).length, 0);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
