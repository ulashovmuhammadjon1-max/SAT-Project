/**
 * Seed one Band 8.5 Task 2 essay with a full analysis, for testing the library
 * without an API key.
 *
 * The annotations go through `resolveAnalysis` — the identical code path a real
 * model response takes — so this exercises quote location, occurrence
 * disambiguation and the drop-what-cannot-be-found rule against real prose,
 * rather than writing offsets straight into the database and proving nothing.
 *
 *   npx tsx scripts/seed-essay-demo.ts
 */
import { PrismaClient } from "@prisma/client";

import { hashEssayText, countWords, resolveAnalysis } from "@/lib/ielts/essay-analysis";

const prisma = new PrismaClient();

const QUESTION =
  "Some people believe that governments should invest more money in public transportation, " +
  "while others argue that this money would be better spent on building new roads. " +
  "Discuss both views and give your own opinion.";

// Deliberately contains a phrase that repeats — "plays a vital role" appears
// twice — so the occurrence field is actually load-bearing here.
const ESSAY = `The question of how limited transport budgets should be allocated divides opinion sharply. While some maintain that constructing additional roads is the more practical solution, I would argue that sustained investment in public transport plays a vital role in addressing congestion more durably.

Those who favour road building point to an immediate and visible benefit. Widening arterial routes and adding bypasses can relieve bottlenecks within months, whereas a metro line takes a decade to deliver. Furthermore, in sparsely populated regions where demand is too diffuse to sustain a bus network, roads are the only realistic means of connecting communities. This argument has genuine force, particularly in countries whose rural populations remain substantial.

Nevertheless, the evidence from large cities suggests that road expansion offers only temporary relief. Because additional capacity tends to attract additional drivers, a phenomenon known as induced demand, congestion typically returns to its previous level within a few years. Public transport, by contrast, moves far more people per unit of road space. A single light rail corridor can carry the equivalent of several motorway lanes, which makes it a considerably more efficient use of scarce urban land.

There is also the environmental dimension to consider. Transport accounts for a substantial share of carbon emissions, and shifting journeys away from private vehicles is among the few measures that can reduce those emissions at scale. Although building rail infrastructure is itself carbon-intensive, the emissions are recovered over the decades the system operates. Investment in public transport therefore plays a vital role in meeting climate commitments that road construction cannot match.

In conclusion, while new roads remain necessary in specific rural contexts, I believe governments should prioritise public transport in urban areas. It uses land more efficiently, mitigates environmental damage, and offers a durable answer to congestion rather than a temporary one.`;

// What a careful analysis of this essay looks like. Conservative on purpose:
// the last two entries are deliberate failures, to prove they get dropped.
const MODEL_OUTPUT = {
  annotations: [
    {
      category: "GRAMMAR" as const, subtype: "concessive_clause",
      quote: "While some maintain that constructing additional roads is the more practical solution",
      occurrence: 1,
      explanation: "A concessive clause introduced by 'While', conceding the opposing view before the writer states their own.",
      ieltsValue: "Conceding a point before countering it shows the examiner you can handle both sides within one sentence.",
      pattern: "While + clause, + main clause", confidence: 0.94,
    },
    {
      category: "COLLOCATION" as const, subtype: "high_value_phrase",
      quote: "plays a vital role", occurrence: 2,
      explanation: "A precise academic phrase for something being essential to an outcome.",
      ieltsValue: "A natural alternative to 'is very important', which is over-used at Band 6.",
      pattern: "play a vital role in + noun/gerund", confidence: 0.91,
    },
    {
      category: "VOCABULARY" as const, subtype: "topic_specific",
      quote: "induced demand", occurrence: 1,
      explanation: "The effect where new road capacity attracts extra traffic until congestion returns.",
      ieltsValue: "A precise technical term that demonstrates genuine subject knowledge on transport questions.",
      pattern: null, confidence: 0.96,
    },
    {
      category: "COHESION" as const, subtype: "contrast",
      quote: "Nevertheless", occurrence: 1,
      explanation: "Signals that the paragraph will now contradict the concession just made.",
      ieltsValue: "Marks the pivot from the opposing view to your own, which is the structural turn Task 2 rewards.",
      pattern: null, confidence: 0.89,
    },
    {
      category: "COHESION" as const, subtype: "reference",
      quote: "This argument has genuine force", occurrence: 1,
      explanation: "'This argument' refers back to the whole preceding point rather than a single noun — cohesion by reference, not by linking word.",
      ieltsValue: "Referencing across sentences is what separates Band 8 cohesion from a list of connectives.",
      pattern: null, confidence: 0.87,
    },
    {
      category: "GRAMMAR" as const, subtype: "reduced_relative_clause",
      quote: "a phenomenon known as induced demand", occurrence: 1,
      explanation: "A reduced relative clause — 'which is known as' has been shortened to 'known as'.",
      ieltsValue: "Reducing relative clauses tightens academic prose and shows grammatical range.",
      pattern: "noun + past participle + …", confidence: 0.9,
    },
    {
      category: "COLLOCATION" as const, subtype: "high_value_phrase",
      quote: "mitigates environmental damage", occurrence: 1,
      explanation: "A formal way of saying something reduces harm to the environment.",
      ieltsValue: "'Mitigate' is far more precise than 'make less bad' and transfers to many environment questions.",
      pattern: "mitigate + noun", confidence: 0.92,
    },
    {
      category: "VOCABULARY" as const, subtype: "sophisticated",
      quote: "carbon-intensive", occurrence: 1,
      explanation: "Describes an activity that releases a large amount of carbon relative to its output.",
      ieltsValue: "A compound adjective that compresses a whole clause into two words.",
      pattern: null, confidence: 0.88,
    },
    // Deliberate failures — must be dropped with a warning, never guessed at.
    {
      category: "VOCABULARY" as const, subtype: "sophisticated",
      quote: "hydrogen fuel cells", occurrence: 1,
      explanation: "Not in the essay at all.", ieltsValue: "n/a", pattern: null, confidence: 0.4,
    },
    {
      category: "COLLOCATION" as const, subtype: "high_value_phrase",
      quote: "plays a vital role", occurrence: 7,
      explanation: "Occurrence 7 does not exist — only two.", ieltsValue: "n/a", pattern: null, confidence: 0.3,
    },
  ],
  ideas: [
    {
      claim: "Road building relieves congestion only temporarily because extra capacity attracts extra drivers.",
      explanation: "Additional lanes lower the cost of driving, so more people drive until the road is as congested as before.",
      consequence: "Congestion returns to roughly its previous level within a few years.",
      example: null,
      anchorQuote: "congestion typically returns to its previous level within a few years",
    },
    {
      claim: "Public transport uses scarce urban land far more efficiently than roads.",
      explanation: "A rail corridor moves many more people per unit of road space than private vehicles can.",
      consequence: "Cities gain capacity without surrendering more land to traffic.",
      example: "A single light rail corridor carrying the equivalent of several motorway lanes.",
      anchorQuote: "A single light rail corridor can carry the equivalent of several motorway lanes",
    },
    {
      claim: "Shifting journeys off private vehicles is one of the few ways to cut transport emissions at scale.",
      explanation: "Transport is a large share of total emissions and most of it is private road travel.",
      consequence: "Public transport investment becomes a climate policy, not only a transport one.",
      example: null,
      anchorQuote: "shifting journeys away from private vehicles",
    },
  ],
};

async function main() {
  const analysis = resolveAnalysis(ESSAY, MODEL_OUTPUT);

  console.log(`located ${analysis.annotations.length} of ${MODEL_OUTPUT.annotations.length} annotations`);
  for (const w of analysis.warnings) console.log(`  dropped: ${w}`);

  // Every stored quote must equal the text at its own offsets.
  const bad = analysis.annotations.filter(
    (a) => ESSAY.slice(a.startOffset, a.endOffset) !== a.quote
  );
  console.log(bad.length === 0 ? "all offsets verified" : `!!! ${bad.length} BAD OFFSETS`);

  // Both occurrences of the repeated phrase must be distinguishable.
  const vital = analysis.annotations.find((a) => a.quote === "plays a vital role");
  const firstAt = ESSAY.indexOf("plays a vital role");
  console.log(
    vital && vital.startOffset !== firstAt
      ? `repeated phrase resolved to occurrence 2 (offset ${vital.startOffset}, not ${firstAt})`
      : "!!! repeated phrase did not resolve to the second occurrence"
  );

  const admin = await prisma.user.findFirst({ where: { role: "ADMIN" }, select: { id: true } });

  await prisma.ieltsEssay.deleteMany({ where: { title: "Public transport vs new roads (demo)" } });
  const essay = await prisma.ieltsEssay.create({
    data: {
      title: "Public transport vs new roads (demo)",
      question: QUESTION,
      essayText: ESSAY,
      band: 8.5,
      topic: "Transport",
      subtopic: "Urban planning",
      tags: ["discuss-both-views", "cities"],
      wordCount: countWords(ESSAY),
      status: "NEEDS_REVIEW",
      analyzedTextHash: hashEssayText(ESSAY),
      createdById: admin?.id ?? null,
      annotations: {
        create: analysis.annotations.map((a) => ({
          category: a.category, subtype: a.subtype, quote: a.quote,
          startOffset: a.startOffset, endOffset: a.endOffset,
          explanation: a.explanation, ieltsValue: a.ieltsValue, pattern: a.pattern,
          confidence: a.confidence, source: "AI" as const, reviewed: false,
        })),
      },
      ideas: {
        create: analysis.ideas.map((i, order) => ({
          claim: i.claim, explanation: i.explanation, consequence: i.consequence,
          example: i.example, startOffset: i.startOffset, endOffset: i.endOffset,
          order, source: "AI" as const, reviewed: false,
        })),
      },
    },
    select: { id: true, wordCount: true },
  });

  console.log(`\nseeded essay ${essay.id} (${essay.wordCount} words, status NEEDS_REVIEW)`);
  console.log(`  admin:   /admin/ielts/essays/${essay.id}`);
  console.log(`  student: /ielts/essays/${essay.id}  (after publishing)`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exitCode = 1;
  })
  .finally(() => prisma.$disconnect());
