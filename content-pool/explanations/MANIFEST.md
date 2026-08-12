# Explanations — Tests 1–5

Authoring 735 explanations (330 Math, 405 R&W) for the first five tests, which
had **3 explanations between them** before this run.

## Why it is built this way

The risk with generated explanations is not bad prose, it is an explanation
that confidently argues for the **wrong answer**. A student believes it and
learns the error, which is strictly worse than the blank page they had before.

So every agent derives the answer independently and records *its own* answer,
never the marked key. `verify.mjs` compares the two and rejects any mismatch,
which routes it to human review instead of to students. That doubles as an
answer-key audit — this project has form here: Test 5's audit found 6 wrong
answers in 81 banked R&W questions.

## Durability

Work is append-only JSONL, one line per finished explanation, written the
moment it is done. An agent that stops — context exhausted, usage limit,
crash — loses at most the line it was mid-write on. A replacement resumes by
skipping the ids already in the file. `status.mjs` drops a truncated final
line rather than failing the read.

`insert.mjs` is idempotent (upsert on the unique `questionId`) and can run
repeatedly *while agents are still working*, so finished work goes live
progressively instead of waiting for a single end-of-run batch.

## Files

| file | role |
|---|---|
| `export_questions.mjs` | one-off export of Tests 1–5 from production → `input/` |
| `slices.mjs` | deterministic disjoint split into six agent slices |
| `BRIEF.md` | the shared authoring brief — style, format, durability rules |
| `status.mjs` | progress across all agents; safe against partial lines |
| `verify.mjs` | the gate: answer match, distractor coverage, house style |
| `insert.mjs` | idempotent upsert into `Explanation`; `--apply` to write |
| `out/*.slice.json` | each agent's assigned questions |
| `out/*.jsonl` | each agent's output, append-only |

## Split

| agent | n | tests |
|---|---|---|
| math-a | 110 | 1, 2 |
| math-b | 110 | 2, 3, 4 |
| math-c | 110 | 4, 5 |
| rw-a | 135 | 1, 2 |
| rw-b | 135 | 2, 3, 4 |
| rw-c | 135 | 4, 5 |

Split by subject first: Math and R&W explanations read differently, and an
agent that stays inside one subject keeps one voice.

## Running it

```
node content-pool/explanations/status.mjs     # progress
node content-pool/explanations/verify.mjs     # gate; exits non-zero on failures
PROD_URL=… node content-pool/explanations/insert.mjs           # dry run
PROD_URL=… node content-pool/explanations/insert.mjs --apply   # write
```
