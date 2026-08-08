# Project memory

## STANDING RULES FOR ALL NEW TESTS (set by the user — do not deviate)

These are permanent instructions, not one-off preferences. Re-read them at the start of any
test-building work.

### 1. Test 1 and Test 2 Math are the quality reference. Test 3 and Test 4 are NOT.
The user has inspected all four and reports Test 1/2 Math as error-free while Test 3/4 Math
carry defects (LaTeX problems, text running together without spacing). Match Test 1/2's house
style, and never copy Test 3/4's.

What Test 1/2 actually do differently — verified by diffing live production stems:
- **Stems are bare HTML, not wrapped in `<p>…</p>`.** Test 3/4 wrapped every stem in `<p>`; Test
  1/2 don't. Follow Test 1/2. (Fixed: 113 single-paragraph Test 3/4 Math stems have since been
  unwrapped by `content-pool/test-6-7-build/fix_math_style.mjs`. The 17 left wrapped are
  genuinely multi-block — an equation block then prose, or prose then a table then prose — and
  must stay that way; unwrapping those joins two paragraphs.)
- **Simple inline math stays plain text.** Test 1 writes `f(x)=6(2x+4)`, `17h+45=164`, `90°F`
  as ordinary text. Reserve `\( … \)` for things that genuinely need typesetting — fractions,
  exponents, radicals, subscripts. Wrapping everything is what makes Test 3/4 look inconsistent.
- **Real `<table>` markup for every data table** (see the style block later in this file).
- **`°` and similar go in as HTML entities** (`&deg;`), not raw glyphs.

### 2. Never bulk auto-convert Math text to LaTeX. Type it by hand.
`mathify.mjs` / `mathify2.py` are the root cause of every Test 3/4 Math defect. Each fixing
round found a new edge case the regex didn't handle. Do not run them on new content, and do not
write a replacement. Hand-write `\( \)` / `\frac{}{}` per question as it is transcribed.

Specific LaTeX rules that a converter got wrong and a human must get right:
- Function names are escaped: `\cos`, `\sin`, `\tan`, `\log`, `\ln`. Bare `cos(A)` inside math
  mode renders as three italic variables `c·o·s`, not a function.
- Always leave a space either side of an inline span: `… length of \(AB\) is …`, never
  `…length of\(AB\)is…`.
- Never wrap prose in math mode. KaTeX drops whitespace between bare tokens, so an answer
  choice like `\(-1 and 4\)` renders as run-on text. Prose choices are plain `<p>` text.
- Systems of equations get stacked with `<br/>`, never crammed onto one line with `"; "`.

### 2b. Verify house style against the DATABASE, never against your own source file.
`verify_math_m2easy.py` and `verify_math_authored_mc.py` check only the questions authored in
their own directory. Test 6 shipped 18 Math questions rendering literal `^`, `sqrt()`, `*`,
`3/5`, `2\pi`, `x != 0` and `sin(theta)` because those came from
`content-pool/new-source-transcripts/` as plain text and **no verifier ever read them**. Every
authored question passed; the bug lived entirely in the content nothing was checking.

**Before publishing any test, run the DB-wide audit against local and production:**
```
DATABASE_URL='postgresql://...' node content-pool/test-6-7-build/audit_math_rendering.mjs
```
It exits non-zero on any `ERROR` finding. Things it checks that a stem-only or authored-only
check will miss:
- `^`, `sqrt(`, `*`-as-multiply, `N/M` slash fractions outside a `\( \)` / `\[ \]` span
- a **LaTeX macro outside a math span** — `2\pi` renders as literal backslash-p-i
- ASCII `!=`, `<=`, `>=`, which should be `\ne`, `\le`, `\ge`
- bare `sin(`/`cos(`/`tan(`/`log(` and Greek spelled out as `theta`/`alpha`
- `pi` as a word, using the `(?<![A-Za-z])pi(?![A-Za-z])` lookaround, never `\bpi\b`

Two lessons about the checks themselves: it **strips `<img>` tags first**, because base64
payloads match every pattern above; and a check that under-matches is worse than none — the
asterisk pattern originally required a digit on the left, so `k*tan(...)` slipped through, and
six more broken questions only appeared once it was widened.

### 3. Every question needs a real figure, never a prose description of one.
Test 3 shipped stems like "a line of best fit is shown, with points scattered around a mildly
increasing trend from about (1,3) to (9,4.5)" — the description substitutes for the picture and
leaks the answer. If a stem says table/graph/figure/shown/chart/plot, it must have a real
`<table>` or an `imageUrl`. Build the figure (matplotlib → base64 PNG) from data already
verified for that question; never invent numbers.

### 4. Math Module 2 (Easy): write most questions ORIGINALLY, don't transcribe them.
The user's explicit instruction. For every new test's Math Module 2 (Easy), author the
questions rather than pulling them from a source PDF. Requirements:
- Verify every answer programmatically with sympy before it ships. No exceptions.
- Check each one against **every question already in the database** — not just the test being
  built — and reject anything that repeats a problem *template* with only the numbers changed,
  not just exact duplicates.
- Keep them genuinely easy: Module 2 (Easy) is the lower branch of the adaptive split.
- Still cap free-response at 3 per module.

### 5. Standing content rules that already applied and still do
- 6 modules per test: R&W 27/27/27 (Standard, M2 Easy, M2 Hard), Math 22/22/22. No undersized
  modules.
- ≤3 free-response per Math module; target exactly 3.
- `correctAnswerFR` is a JSON-encoded array string: `'["40"]'`, never `'40'`.
- Look Domain/Skill up by `code`, never by `name`.
- Insert as `DRAFT`; the user publishes from the admin panel.
- Verify in the real exam interface (`/exam/{attemptId}`), not just the admin preview.

## Efficient test-building playbook — read this before starting any new test work
This section exists because Claude Code sessions do **not** carry memory between separate
conversations — only what's committed to files in this repo persists. If a session ever says "I
don't remember the last conversation," that's expected, not a bug: this file (and the rest of
`content-pool/`) *is* the memory. Keep it current after any nontrivial content-build session.

### Getting database access without re-pasting the URL every session
The production DB URL must never be written into any committed file (secrets don't belong in git
history) — but it also doesn't need to be re-pasted every session. The fix is a **persistent
environment variable on the Claude Code environment itself** (not a file in this repo):
1. Go to `claude.ai/code` and open the environment this project runs in (see
   https://code.claude.com/docs/en/claude-code-on-the-web for how environments work).
2. Find that environment's settings / environment variables section.
3. Add a variable named `DATABASE_URL` with the Neon connection string as its value.
4. Save. Every *future* session's container picks this up automatically at startup as
   `process.env.DATABASE_URL` — no copy-pasting, and it still never touches a file in the repo.
   (A session already running when the variable is added won't see it — env vars are injected at
   container start, so it only applies going forward.)
This sandbox also blocks raw Postgres (port 5432) and only allows outbound HTTPS, so even with
`DATABASE_URL` set, use `@neondatabase/serverless`'s `neon()` HTTP-based tagged-template driver for
production reads/writes, not Prisma's normal TCP client (which only works against the local dev
Postgres, started via `service postgresql start` after `apt-get install postgresql` once per
session — Docker's daemon isn't available in this sandbox either).

### Math content: prefer original, sympy-verified questions over PDF transcription
Building Test 3/4's Math sections from transcribed "clumsy" source PDFs cost three separate
bug-fixing passes after the initial build (see the MANIFEST.md follow-up sections in
`content-pool/test-3-4-build/`) — first ~16 stems that fell back to plain text, then a further 20
questions found only after a full regex audit (systemic KaTeX spacing bugs, raw un-converted
fractions, crammed systems of equations, a broken math wrapper), plus real correctness defects
(a duplicate-equivalent answer choice, two answer choices literally shipped as
`"[cut off in source PDF]"`, an unresolvably ambiguous answer with no source image to check
against, `CONFLICT`-flagged answers where the transcript's own verification note disagreed with
the parsed official key). Root cause: a regex-based plain-text-to-LaTeX auto-converter
(`mathify2.py`) trying to reverse-engineer author intent from noisy OCR'd text — every fix round
found a new edge case it didn't handle, and the source PDFs' own answer keys were frequently
unreliable to parse in the first place.
**Recommendation for future Math content**: default to writing original, SAT-style questions with
`\( \)`/`\frac{}{}` LaTeX **typed correctly by hand from the start** (no bulk auto-conversion
step) and every answer verified programmatically with sympy before it ships — this is strictly
more reliable than transcribing from a source PDF and running it through a converter, and it's
what CLAUDE.md already mandates as the fallback when transcribed content runs short (see
"Math modules" rules below) — just prefer it as the default for Math, not only the fallback.
Reading & Writing is a different story *for markup*: it's mostly prose/HTML, doesn't go through a
LaTeX converter, and has never had the rendering problem. **But R&W transcription has its own,
worse failure mode: the answer keys.** Test 5 found 6 wrong answers in 81 banked R&W questions
(7.4%), and the October papers' R&W keys disagreed with a careful reading on 7 of 18 spot-checked
— while the same papers' Math keys were clean. So R&W PDF transcription is fine for the *content*
and not to be trusted for the *answers*: every R&W question must be answered independently before
it ships. See "Test 5 is built and PUBLISHED in production" below.

### If you do transcribe Math from a PDF anyway — audit checklist (run proactively, don't wait for a user report)
Before shipping, grep every Math stem/choice (excluding `<img>` tags, whose base64 data will
false-positive on every regex below) for:
- Raw `/` division outside any `\frac{}{}` — e.g. `\bfrac\{[^}]*\}` is present but a *separate*
  `\d+\s*/\s*\d+`-shaped pattern also appears. Convert every one to `\frac{}{}`.
- `^` exponent characters sitting *outside* any `\(...\)` span (find all `\(...\)` spans first,
  then check every `^` for whether it falls inside one) — a sign the converter closed the math
  wrapper in the wrong place (this happened right before a thousands-comma: `\(f(x)=3\),000...^x`).
- A stem containing the literal phrase `"system of"` alongside 2+ separate `\(...\)` equation
  spans — those need to be visually **stacked** (`<br/>` between them), not crammed onto one line
  with a `"; "` separator. Don't stack every pair of `\(...\)` spans blindly though — many stems
  legitimately state two separate facts in one sentence (e.g. "QR = 16 and TU = 12") and should
  stay as prose.
- Any answer choice fully wrapped in `\( ... \)` that contains 3+ real English words (not just
  5+, that threshold missed short ones like `\(-1 and 4\)`) — KaTeX drops whitespace between bare
  tokens in math mode, so prose sentences (or even short two-item lists) wrapped in math mode
  render as run-on text with no spaces between words. Unwrap to plain `<p>` text.
- `\(x:\d,\d,\frac\{\d+\}\{y\}:...\)` or similar — a telltale sign the converter misread a
  `column / column` separator as a division and produced a nonsense fraction. These are always
  "which table" questions; convert the choices to real per-choice `<table>` HTML instead.
- Any question whose stem says "table"/"graph"/"figure"/"shown"/"chart"/"plot" but whose HTML has
  neither a real `<table>` nor an `<img>` tag — it's a text description standing in for a real
  visual. Build one (matplotlib chart embedded as base64 PNG on `Question.imageUrl`, or a real
  `<table>` per the standard style block below) using only data already verified correct for that
  question — never invent numbers.
Then **verify in the actual exam-taking interface**, not just the admin editor preview — seed a
throwaway `Attempt`/`ModuleAttempt` row pointing at the module in question (mirrors
`startAttempt()` in `src/server/actions/student/attempts.ts`), load `/exam/{attemptId}` as the
student user via Playwright, screenshot every affected question, and delete the attempt afterward.
The admin preview and the real exam page have rendered identically in every case so far, but the
exam page is what the user actually sees and is the only check that matters.

### Applying a fix to both databases without breaking anything
Local dev question/choice IDs are **not** the same as production IDs (different insert runs,
different ID schemes — cuid-style locally, UUID in production) — never assume a hardcoded ID
matches across environments. The pattern that's worked every time: match each target row by
`(test title, subject, module order, difficulty, question order)` via a small join query, then —
critically — **assert a distinctive content substring is present in the fetched row before
writing to it**, every single time, even when you're confident about the position. A single
hardcoded-position mistake this session (targeting question order 14 instead of 15 in a module
where two adjacent questions coincidentally had near-identical stems) briefly overwrote an
already-correct question; it was only caught because of exactly this kind of substring check
run *after* the fact. Do the check *before* writing, not after, and it's a non-issue instead of a
scramble. Apply to local first, screenshot-verify, then production, with the same assertion
gating every production write individually (not just once for the whole batch).

## Vocab Sets feature — Sets 1-5 live, Sets 6-16 extracted but not yet inserted
Gated vocabulary sets ("Set 1".."Set 16", 25 words + a passage + a 10-question quiz each, must
pass a set's quiz at ≥8/10 to unlock the next) are a real shipped feature — see `VocabDeck.order`,
`VocabSetQuizQuestion`, `VocabDeckProgress` in the schema, and
`src/app/(student)/vocabulary/sets/`. **Sets 1-5 are live in both local dev and production.**
Sets 6-16 (minus a gap at Set 9) are already transcribed and verified — see
`content-pool/vocab-book/MANIFEST.md` for exactly what's ready to insert, what's missing (Set 9
entirely, part of Set 16's quiz), and the two source-content quirks flagged for human review
before shipping. Don't re-transcribe from the PDFs again; that work is already done and sitting in
`content-pool/vocab-book/college_panda_sets_extracted.json`.

## Test 3 and Test 4 are built and live in the DB as DRAFT
Both are fully inserted (147 questions each: 27/27/27 R&W, 22/22/22 Math) — see
`content-pool/test-3-4-build/MANIFEST.md` for exact IDs, what was deduped, and known gaps
(a few graph-reference questions render a text description instead of a real chart image, ~16
Math stems fall back to plain unstyled text instead of full KaTeX rendering because the
auto-converter's safety check judged the wrap risky, 4 Math questions carry an `APPROXIMATE`
graph-reading note, 0 Explanation rows). **Both are DRAFT, not PUBLISHED** — review in the
admin panel before flipping status. `content-pool/test-3-4-build/full_build.json` is the exact
content that was inserted; `insert.mjs` in that same directory is idempotent (skips any
Test/Module that already exists) if it ever needs to be re-run.

Reminder: this environment's sandbox blocks the raw Postgres port (5432) and only allows
outbound HTTPS, so the normal Prisma/pg client can't reach the DB directly from here — use
Neon's HTTP query API (`@neondatabase/serverless`'s `neon()` tagged-template function) instead,
same as `insert.mjs` does. Never write the DB connection string into any file — pass it via
`process.env.DATABASE_URL` only.

## Test 5 is built and PUBLISHED in production
`Test 5` (`5537a8d3-602e-43ab-b973-1bc607d3f37c`), 147 questions, R&W 27/27/27 + Math 22/22/22.
Math Module 2 (Easy) is 22 originally authored, sympy-verified questions per the standing rule
above; Math M1 / M2 Hard come from the October IntB / USB / USC papers; R&W comes from the
banked pool plus October top-ups. Everything is documented in
`content-pool/test-5-build/MANIFEST.md`, with the answer audit in `rw_answer_audit.md`.

**The lesson from Test 5 worth carrying forward: R&W answer keys lie, Math answer keys mostly
don't.** All 81 R&W answers were re-answered by hand before shipping and **6 were wrong** —
and only 2 of those 6 were catchable from a printed data table. The other 4 needed the question
actually read and reasoned. Two further questions were unrepairable (a mistranscribed stem, a
table that no longer exists) and were replaced from source page images. The same papers' Math
keys were clean (Oct IntB: 22/22). So: for any future R&W module, budget a full read-and-answer
pass before shipping — `content-pool/test-5-build/dump_rw.py "<module>" <lo> <hi>` renders
questions for exactly that — and never treat a source R&W key as authoritative.

Source pools left over: `content-pool/new-source-transcripts/` still has unused, classified Math
questions, but not enough for a full 3×22 Math build on their own. `content-pool/test-3-4-5-
reading-writing/` is now fully consumed across Tests 3, 4 and 5. The October IntB and USB papers
still have unused R&W Module 1 questions (both papers, ~27 each) and unused Module 2 reading
questions — the top-up passes only harvested the writing tail. Test 6 needs either more Math
source material or explicit OK to author original Math questions.


## Tests 7-18 are built and PUBLISHED — 18 tests, 2,646 questions live
Every test is 147 questions (R&W 27/27/27, Math 22/22/22 with 19 MC + 3 FR per module). All
Math and, from Test 8 on, all R&W is **originally authored** — the transcribed source pools are
spent. Per-test build directories are `content-pool/test-N-build/`.

The pipeline that works, in order: `math_testN.py` + `verify_math_testN.py` → `rw_testN.py` →
`balance_rw.py` → `assemble_testN.py` → `insert_test.mjs` (local) → `audit_math_rendering.mjs`
→ `insert_test.mjs --publish`. Two shared dedupe corpora feed it: `rw_authored_corpus.json` at
the `content-pool/` root (809 R&W passages, every authored and transcribed pool) and
`prod_math_stems.json` per build directory (a snapshot of every live Math stem).

### Authoring several tests in parallel: agents converge, and territory is the fix
Subagents handed the same reference template independently write the **same question** — three
once produced `f(x)=x²−4x` with `g(x)=3x+2`. It cost Tests 13 and 14 a repair pass each.
Two things prevent it, and both are needed:
1. **Assign each test a disjoint thematic territory** (Test 16 got maritime/textiles/printing/
   glass, Test 17 surveying/railways/forestry/dairying, Test 18 aviation/brewing/watchmaking/
   quarrying) and name the siblings' territories in each brief so they steer clear.
2. **Point each agent at a different existing test as its structural template.**
With both in place, cross-sibling overlap came out at 0.56 for Math and 0.18 for R&W passages,
against thresholds of 0.75 and 0.50 — no repair pass needed.

### A similarity threshold decides what to READ, not what to accept
Test 18's Math pass found **nine** questions scoring *below* 0.75 that were still genuine
template repeats once the nearest banked stem was actually read — a linear `f(x+3)−f(x)`, a
guy-wire Pythagoras, a "no solution, find k" system, a circle-equation radius. Read every match
above ~0.45. Conversely, two Test 18 items had perfectly distinct maths but **reused the setting
of a Module 1 item**; since a student sees Module 1 plus one Module 2 branch, the Easy branch
would have shown the same hop kiln twice. Check settings across modules, not just stems.

### R&W answer keys skew hard when hand-authored — always rebalance
Raw distributions came in at A45/B22/C13/D1, A42/B29/C9/D1 and A70/B8/C3/D0. `balance_rw.py`
rotates them to 21/20/20/20. It refuses to rotate any question whose rationale names an option
**by letter**, so every `why` must name options by their content.

### The `LETTER_REF` bug, fixed — do not reintroduce it
The old pattern matched any bare A-D followed by whitespace, which also matched the **article
"A"** starting a sentence: "A complete sentence stands in front of the blank" read as a
reference to option A and silently locked that question against rebalancing. It bit three
builds before it was found. The pattern now requires an explicit marker (`Option B`, `(C)`) or a
following verb. Same family of bug as the `\bpi\b` one below — a word-boundary check that looks
right and silently under- or over-matches.

### Per-question difficulty must be written through, not hardcoded
`insert_test.mjs` writes `q.difficulty`; the older `insert_test6.mjs` hardcoded `'MEDIUM'`,
which is why 392 questions across Tests 3-6 misreported their level in the Question Bank badge
and filter. Backfilled by `content-pool/test-15-build/backfill_difficulty.mjs`; production now
reads 882/882/882 across STANDARD/EASY/HARD with zero mismatches. Use the newer inserter.

## Test 6 is built and PUBLISHED; Test 7 needs 38 Math MC and nothing else
`Test 6` (`b7cf096a-090d-4286-a128-9ec428e6de32`), 147 questions, live on satforge.org. Full
detail in `content-pool/test-6-7-build/MANIFEST.md`.

**The finding that matters most for any future build: the EliteXSAT corpus recycles heavily.**
The three October papers (IntB, USB, USC) are parallel forms of one administration and share
questions outright — Oct USC Module 2 is close to a straight clone of Oct USB Module 2. And the
August papers overlap both the October set and the material already shipped: a lexical check
found 30 of 67 August pages already live. 33 R&W questions were rejected as duplicates across
this build. **Always dedupe a new paper against every other paper in the same batch, not just
against production.**

The practical consequence: the source PDFs supplied only 128 of the 162 R&W questions two tests
need. The other 34 were authored (`rw_authored.py`), weighted to the writing domains because
writing is always the binding constraint and because grammar items are the safest to author —
correctness follows from a stated convention, the same property that makes sympy verification
work for Math. Math Module 2 (Easy) for both tests is authored and sympy-verified
(`math_m2easy.py`), and 24 medium/hard Math MC questions were authored too
(`math_authored_mc.py`) because the transcribed pool yielded only 18 usable MC.

Every verifier in that directory is runnable and passing: `verify_math_m2easy.py`,
`verify_authored_rw.py`, `verify_math_authored_mc.py`, and `assemble_test6.py` itself, which
enforces the R&W block order by sorting on block rank so the writing block opens at question 15
in every module.

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

### `mathify.mjs` — the plain-text-to-LaTeX converter has two known fixed bugs
Located at `scratchpad/neon-check/mathify.mjs` in this session's scratchpad (not checked into
the repo — it's a build-time content tool, not app code). Two real rendering bugs were found
live in **both** Test 1 and Test 2 and fixed in the converter itself:
- **The literal word "pi" never became the `π` glyph/`\pi`.** `\bpi\b` doesn't work as the
  boundary check — a digit and a letter are both `\w`, so "3pi" has no `\b` between "3" and
  "p" and the replacement silently no-ops. Fixed with a letter-specific lookaround:
  `(?<![A-Za-z])pi(?![A-Za-z])`. Any future text-processing step that needs to treat "pi" as a
  standalone math token must use this same lookaround, not `\b`.
- **Answer choices only got KaTeX-wrapped when they contained a fraction/exponent/inequality/
  sqrt.** A plain sibling choice like `x - 3` stayed unwrapped, plain-text, non-italic, sitting
  next to a KaTeX-italicized `x^2 - 3` in the same 4-choice list — individually correct, but
  visually inconsistent. Fixed by widening the whole-string-wrap trigger to any digit/operator/
  π (not just `^ / ≤ ≥ ≠ sqrt √`), while still requiring `looksLikePureMath()` to pass so a
  short plain-English choice like "One"/"Two"/"Zero" (which contains no digit or operator)
  never gets sent through math mode by mistake.

**If you ever need to re-fix rendered Math content after it's already live: do NOT regenerate
stems from the original source JSON/pool.** That source is a point-in-time snapshot from
before insertion — it does not reflect manual post-processing fixes (e.g. `<table>` HTML for
data tables, `<br/><br/>` line breaks between stacked equations) that get applied directly to
the live DB afterward and never get written back to the source file. Regenerating a stem from
that stale source silently destroys those fixes (this almost happened while fixing the "pi"
bug above — caught by diffing before applying, not by looking at the source). Instead, patch
the **current live DB value** directly and narrowly: choices are short and safe to reprocess
in place; stems are not — touch only the specific substring that needs fixing (e.g. a plain
string replace) and leave the rest of the stem's HTML untouched.

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

### More real bugs found and fixed while building Test 2 (don't reintroduce these)
- **Deduping/matching by `(source, num)` is NOT safe.** `num` is only unique *within* one
  source PDF's own module — the same `(source, num)` pair legitimately collides across
  different modules pulled from the same source pool (verified: `March|14`, `JuneV1|10`, and
  `May|3` each hit two unrelated questions). Any per-question override (special passage
  formatting, manual classification fix, etc.) must match on distinctive **content**
  (a unique substring of the actual stem/passage, checked for uniqueness against the whole
  pool first) — never on `(source, num)` alone.
- **The Rhetorical Synthesis classifier missed the "given sentences" phrasing.** Real
  Rhetorical Synthesis stems come in at least two forms: "The student wants to... Which choice
  most effectively uses relevant information from **the notes**..." and "Which choice most
  effectively uses information from **the given sentences**...". The original classifier regex
  only matched `student.{0,15}(wants|notes)|relevant information from the notes`, silently
  misfiling every "given sentences" question as `Information and Ideas / Central Ideas and
  Details`. This was live in **Test 1** too (2 questions) and has been fixed there directly;
  the classifier itself was fixed to also match `given sentences`. If a module's Rhetorical
  Synthesis count looks short, grep for `"given sentences"` in stems before assuming supply is
  actually short.
- **The Boundaries vs. Form/Structure/Sense classifier can't work off stem text alone.** Real
  SAT Boundaries questions never literally say "comma"/"semicolon"/etc. in the stem — the only
  signal is which punctuation mark differs between the four answer **choices** (comma vs.
  semicolon vs. colon vs. period vs. comma+FANBOYS). A regex over the stem/passage will default
  everything to Form/Structure/Sense (this happened for both Test 1 and, before being caught,
  Test 2's first classification pass). Every SEC question needs its choices read by eye (or a
  choices-aware heuristic) to tell the two apart — don't trust a stem-only classifier for this
  domain.
- **Verify transcribed math answers, not just originally-authored ones.** One real transcribed
  question (a similar-triangles problem, Test 2 Math Module 1) had its two side lengths swapped
  in transcription, making the marked-correct choice mathematically impossible for any of the 4
  answer choices (verified with sympy: correct EF ≈ 26.7, not among 12/15/18/24). This was the
  only error found across 66 transcribed Math questions, but it means transcribed content is
  not automatically trustworthy — spot-check FR answers with sympy and hand-verify MC answers
  for at least the geometry/word-problem items, the same as the rule already in place for
  originally-authored questions.
- **A markdown-bracket directive can have more than one shape.** The `[UNDERLINED: ...]` source
  convention sometimes carries an annotation before the colon, e.g.
  `[UNDERLINED (colored, likely emphasis): ...]`. Match the opening marker with a regex
  (`\[UNDERLINED[^:\]]*:`), not a literal `'[UNDERLINED:'` string, or some instances silently
  pass through unconverted (found live in a Test 2 answer choice, not just a passage — brackets
  can appear in choice text too, so run the same conversion there).
