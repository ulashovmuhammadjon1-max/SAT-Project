# Project memory

## SAT Reading & Writing (EBRW) module question order — MUST FOLLOW

When building, reordering, or regenerating any Reading & Writing module (Module 1, Module 2
Easy, Module 2 Hard, or any future module) for the mock SAT tests, every module MUST follow
this exact domain-block sequence, with no exceptions:

1. **Words in Context** — fill-in-the-blank vocab ("...completes the text with the most
   logical and precise word or phrase?") — about 4–5 questions
2. **Words in Context (underlined-word meaning)** — ("As used in the text, what does the
   word X most nearly mean?") — 1–2 questions
3. **Text Structure / Purpose** — ("...function of the underlined...", "main purpose of the
   text") — 1–2 questions
4. **Cross-Text Connections** (Text 1 / Text 2 questions) — 0–1 questions, optional
5. **Central Ideas & Details** (main idea, "according to the text...") — 1–2 questions
6. **Command of Evidence — Quotation** ("which quotation...") — 1–2 questions
7. **Command of Evidence — Graph/Table** ("uses data from the graph/table...") — 1–2 questions
8. **Command of Evidence — Support the hypothesis** ("which finding, if true, would most
   directly support/weaken...") — placed immediately before Inference — 1–2 questions
9. **Inference** ("most logically completes the text", "what can most reasonably be
   concluded") — 1–2 questions. **Inference is always the LAST reading question.**

Then, and only then, the writing section follows, in this order:

10. **Standard English Conventions** (grammar — "...conforms to the conventions of Standard
    English?")
11. **Transitions** ("...most logical transition?")
12. **Rhetorical Synthesis / Student Notes** (bulleted notes / "given sentences", always last)

### Hard rules
- **No reading-domain question (1–9) may ever appear after a writing-domain question
  (10–12) has started.** Verify this programmatically (classify every question, confirm the
  category sequence is monotonic) before shipping — don't eyeball it.
- Reading section should total **at most ~14–15 questions** in a 27-question module (writing
  fills the rest); scale proportionally for smaller modules.
- Each R&W module (Module 1, Module 2 Easy, Module 2 Hard) should be a **full, real
  27-question module** — don't ship undersized modules (e.g. 16/20) unless the user
  explicitly accepts a reduced size.
- When content supply is short for a domain (Rhetorical Synthesis and Transitions are
  chronically scarce in the transcribed source tests), pool ALL available questions across
  every test/module (not per-test silos) and distribute with a largest-remainder method so
  scarcity is spread fairly — never let one module get zero of a domain while another hoards
  the supply.

### Math modules (same test package)
- Each Math module (Module 1, Module 2 Easy, Module 2 Hard) should be a full **22-question**
  module.
- **At most 3 free-response (student-produced response) questions per module.**
- No question may repeat anywhere in the package, including the same problem template with
  only the numbers changed (e.g. `JuneV1` and `JuneV2` sources in this project's raw pool are
  the SAME test transcribed twice — treat them as one source, not two, when deduping).
- If real transcribed content isn't enough to fill a module, write original SAT-style
  questions rather than shipping an undersized module or reusing content — verify every
  original question's answer programmatically (e.g. with sympy) before including it.

## Test 1 — reference structure & schema conventions (read before building any new test)

Test 1 (`id: cgoufc8pycadafwlv6yal4f1`, status `PUBLISHED`) is the working reference
implementation. Every fact below was pulled directly from the live production DB, not
assumed — when building Test 2+, match this structure exactly and diff against it before
shipping.

### Module shape (6 modules per full test)
| subject | order | difficulty | questions | time limit |
|---|---|---|---|---|
| READING_WRITING | 1 | STANDARD | 27 | 32 min |
| READING_WRITING | 2 | EASY | 27 | 32 min |
| READING_WRITING | 2 | HARD | 27 | 32 min |
| MATH | 1 | STANDARD | 22 | 35 min |
| MATH | 2 | EASY | 22 | 35 min |
| MATH | 2 | HARD | 22 | 35 min |

- `Module` identity is `@@unique([testId, subject, order, difficulty])` — that's the real key,
  not a `name`/`title` field (Module has no `name` column, only an optional `title`).
- `Question.order` is **1-indexed and contiguous** per module (1..27 or 1..22, no gaps, no
  duplicates) — this is what the palette/review-grid numbering relies on.
- Every Math module has **exactly 19 MULTIPLE_CHOICE + 3 FREE_RESPONSE** questions in Test 1 —
  treat 3 as the target, not just a ceiling, unless content supply genuinely can't support it.

### Domain/Skill — always look up by `code`, never by `name`
`Domain.code` and `Skill.code` are the real unique keys (`Domain.name`/`Skill.name` are
display strings, not identifiers — matching on name risks silently creating duplicate rows on
a typo or phrasing drift). Full table, taken from the live DB:

```
READING_WRITING
  INI  Information and Ideas      → INI-CI Central Ideas and Details, INI-IE Inferences, INI-CE Command of Evidence
  CAS  Craft and Structure        → CAS-WV Words in Context, CAS-TS Text Structure and Purpose, CAS-CT Cross-Text Connections
  EOI  Expression of Ideas        → EOI-RS Rhetorical Synthesis, EOI-TR Transitions
  SEC  Standard English Conventions → SEC-BS Boundaries, SEC-FS Form, Structure, and Sense
MATH
  ALG  Algebra                    → ALG-LE Linear Equations and Systems, ALG-LF Linear Functions, ALG-LI Linear Inequalities
  ADV  Advanced Math              → ADV-NF Nonlinear Functions, ADV-EQ Equivalent Expressions, ADV-NE Nonlinear Equations and Systems
  PSDA Problem-Solving and Data Analysis → PSDA-RP Ratios/Rates/Proportions, PSDA-ST Statistics and Probability, PSDA-DI Data Interpretation
  GT   Geometry and Trigonometry  → GT-AV Area and Volume, GT-LA Lines/Angles/Triangles, GT-TR Trigonometry
```

Note `ALG-LI` (Linear Inequalities) and `GT-TR` (Trigonometry) exist as skills but are barely
used in Test 1 (Trigonometry has only 1 question across the whole test) — don't force-fill
them, just don't forget they exist when classifying.

### Content HTML conventions (must match exactly, or rendering breaks)
- **Math notation**: `\( ... \)` for inline, `\[ ... \]` for display/block math — rendered by
  KaTeX in `MathContent` (`src/components/shared/math-content.tsx`). Anything outside those
  delimiters is plain HTML. Never use `$...$`, markdown, or plain-text fractions/exponents.
- **Italics**: `<em>...</em>` only. Never leave markdown `*asterisks*` uninverted — they render
  as literal asterisks (this was a real bug in Test 1, since fixed).
- **Underline** (for Boundaries/Text-Structure "underlined portion" questions): `<u>...</u>`
  inline inside the passage `content`.
- **Fill-in-the-blank (Words in Context)**: the blank is a literal `_____` (5 underscores)
  written inline in the passage HTML — not a placeholder token, not italics.
- **Tables**: inline-styled, matches the site's existing look —
  `<table style="border-collapse:collapse;margin:0.75rem 0;">` with
  `<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">`
  header cells and plain `<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">` body
  cells. Reuse this exact style block for every new table so tables look consistent across
  tests.
- **Cross-Text Connections passages**: both texts live in a **single** `Passage.content`
  field as `<p><strong>Text 1</strong></p>...<p><strong>Text 2</strong></p>...` — never split
  across two `Passage` rows for one question.
- **Bulleted student notes (Rhetorical Synthesis)**: real `<ul><li>...</li></ul>` markup, never
  flattened into a run-on paragraph.
- `Passage.title` is fine as `null` — Test 1 leaves it unset throughout; not a required field.

### `correctAnswerFR` — MUST be a JSON-encoded array string
Canonical format confirmed against every real consumer (grading in
`src/server/actions/student/attempts.ts`, `practice/[questionId]/page.tsx`,
`review/[attemptId]/page.tsx` — all do `JSON.parse(...)`): e.g. `'["40"]'`, `'["-19"]'`,
`'["1/3"]'`. **Never** store a bare string like `'40'` — that parses to a number and crashes
`.some()` at grading time (this exact bug shipped once and broke every FR submission).

### Images
`imageUrl` on `Question`/`Passage` is rendered directly as `<img src={imageUrl}>` with no
transformation — both a Blob path (`/api/images/{blobPathname}`) and a raw
`data:image/jpeg;base64,...` URI work, since it's just an opaque `src` string. Test 1 uses
base64 data URIs throughout (inserted without `BLOB_READ_WRITE_TOKEN` access) — either is
fine, but don't mix a broken/relative path in.

### Known gap in Test 1 — do not treat as the template
Test 1 currently has **zero** `Explanation` rows (0 of 147 questions). This is a real content
gap, not an intentional convention — don't copy "no explanations" into new tests; flag it if
asked to improve Test 1, and try to include explanations when building new tests from scratch
if content/time allows.

### Before shipping any new test
Run the same verification passes used for Test 1: confirm the R&W domain-block sequence is
monotonic per module (see rule above), confirm every Math module has ≤3 FR and no duplicate
questions, confirm every `correctAnswerFR` is JSON-array-encoded, confirm every question has
a passage/image where the stem implies one needs it, and confirm no bare markdown asterisks
or un-converted plain-text math slipped through.
