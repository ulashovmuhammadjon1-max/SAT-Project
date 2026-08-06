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
