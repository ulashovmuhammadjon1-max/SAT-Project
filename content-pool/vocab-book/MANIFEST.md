# Vocab book extraction — "Vocabook_130" (College Panda 400 Words, Sets 1-16)

Source: a "SATashkent Vocabook Version 3" PDF the user supplied in 3 chunks (`Vocabook_130.pdf` =
book pages 1-30, `Vocabook_3060.pdf` = pages 30-60, `Vocabook_60102.pdf` = pages 60-102). Only the
first section of this book — **"College Panda 400 Words," Sets 1-16** — was requested; the book
also contains Ivy Global 500 Words, Advanced Package Vocabulary, and SATashkent Words (Edition 8.0)
after that, which were **not** extracted (out of scope for this pass).

## What's in `college_panda_sets_extracted.json`
15 of the 16 sets (missing Set 9 — see gap below), each with:
- 25 words: term, definition, example sentence, antonym (transcribed verbatim from the book,
  including a couple of the book's own authoring quirks — see below)
- The set's "Reading Time" passage (title + full text)
- The set's "Fight Time" quiz: 10 fill-in-the-blank questions, 4 choices each

**The book's own answer key lives in a separate appendix (page 414+) not included in any of the
3 supplied PDF chunks.** Every quiz question's `correct` field was independently determined by
matching the sentence's context against the word's definition (a mini reading-comprehension pass,
same rigor as the math sympy-verification convention) — not copied from an answer key, since none
was available. Spot-check a few before trusting the whole set blindly, same as any first pass.

## Already inserted (Sets 1-5, both local dev and production DB)
Sets 1-5 are live now, gated in sequence (`VocabDeck.order`, `VocabSetQuizQuestion`,
`VocabDeckProgress` — see schema). A student must score ≥8/10 on a set's quiz to unlock the next
one, enforced server-side (`getVocabSetDetail` in `src/server/actions/student/vocab.ts` throws for
a locked deck — direct URL access 404s, not just hidden in the UI).

## NOT yet inserted — Sets 6, 7, 8, 10-16 (this file has the content, ready to go)
Continue by writing an insert script that reads `college_panda_sets_extracted.json` the same way
the original Sets 1-5 insert did (see git history for `insert_vocab_sets.mjs` / the production
equivalent using the Neon HTTP driver — both were one-off scripts, not committed, but the pattern
is: create `VocabDeck` with `order`/`passageTitle`/`passage`, create 25 `VocabWord` + `VocabDeckWord`
join rows per set, create 10 `VocabSetQuizQuestion` rows per set).

## Known gaps — read before inserting the rest
- **Set 9 is entirely missing.** The first supplied PDF chunk covering this range starts mid-way
  through Set 9's *passage* (already past the 25-word table), and the word table + passage title
  aren't on any page in any of the 3 supplied chunks — there's a gap around book pages 56-58 that
  was never uploaded. The Set 9 quiz questions that *are* present reference words never defined
  anywhere in the supplied material (e.g. "robust," "wayward," "dismal," "complacent," "melodramatic,"
  "conception," "judgmental") — do not guess at these; get the missing pages from the user first.
- **Set 16's quiz is incomplete.** The third PDF chunk ends at its own last page (book page 101)
  mid-way through question 3 — only Q1 and Q2 are complete and verified; Q3's choice D and
  questions 4-10 were never supplied. Set 16's 25 words and passage ARE complete and safe to use;
  only the quiz needs the missing pages (book pages ~102-104) before Set 16 can be gated like the
  others.
- **Set 15, quiz Q6 is logically inconsistent in the source itself** (not a transcription error):
  "His calm demeanor ______ his inner anxiety... His outward appearance did not reflect how he
  truly felt" — none of the 4 choices actually means "concealed," which is what the sentence
  needs. Marked `manifested` (A) as correct since it's the topically-closest option and the
  probable intended vocab word, but flag this to a human before shipping, or replace the question.
- **Set 11, word 22 "Incantation"** has antonym printed as "Impervious" in the source table — not
  a true antonym (a magic spell's opposite isn't "impervious to influence"). Transcribed verbatim
  per the project's "don't silently correct the source" convention; worth a human fix before
  shipping display copy, or just drop the antonym field for this one word.

## Passing threshold
Currently hardcoded at 8/10 (80%) in `src/lib/vocab-constants.ts`
(`VOCAB_SET_PASS_THRESHOLD`). The user was asked whether they wanted all-10 or a lower bar and
didn't give an explicit number before asking to just ship Sets 1-5 — 8/10 was picked as a
reasonable default. Revisit/confirm with the user before assuming it's final.
