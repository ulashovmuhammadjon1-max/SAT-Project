# Test 5 — Reading & Writing answer audit

Every one of the 81 R&W questions was answered independently, from the question text alone,
before its recorded answer was looked at. This was not optional diligence: the banked pool's
recorded answers come from source-PDF answer keys that had already proved unreliable during the
top-up pass (the October papers' R&W keys disagreed with a careful reading on 7 of 18 questions
checked, and in 4 of those 7 the student's own on-screen selection in the source capture agreed
with the reading, not with the key). The Math keys from the same papers were fine — 22/22 on Oct
IntB — so this is specifically an R&W-key problem.

Result: **6 wrong answers out of 81 (7.4%)**, plus 2 questions that could not be repaired and
were replaced, plus 1 skill mislabel.

## Wrong answers, corrected

All six are in `ANSWER_FIXES` in `format_rw.py`, keyed by `(module, raw index)` with the full
reasoning; `format_rw.py` stamps each corrected question with an `answerCorrected` note so the
change is traceable in `test5_rw.json`.

| Module | Final order | Source | Recorded | Correct | Why |
|---|---|---|---|---|---|
| RW_M1 | 10 | Dec2023E | D | **B** | Only Poland has more insect than fungus species (25/105). D describes Poland as "105 fungus species and only 10 insect species" — it contradicts its own table, which reads 25 fungi / 105 insects / 10 trees. |
| RW_M1 | 15 | Dec2023E 21 | C | **A** | Boundaries. Both halves are independent clauses, so a conjunctive adverb alone can't join them: C (`however all`) and D (`however, all`) are comma splices, B drops the boundary. Only A (`however. All`) closes the first sentence. |
| RW_M2_EASY | 8 | Dec2023E 8 | B | **C** | The hyperpop passage ends on vocal manipulation inviting reflection "on the extent to which digital technology mediates the human experience today" — a commentary on contemporary social conditions (C). B claims continuity of experience *despite* social and historical change; the text says the opposite. |
| RW_M2_HARD | 11 | Nov2023 | A | **B** | The claim is that some lakes saw an *increase* in ice duration. A (Näckten 177 → 134) is a decrease. Spirit Lake goes 102 → 126; B states that. |
| RW_M2_HARD | 14 | March2024B 13 | A | **C** | The conclusion is that *net* CO₂ rises with earlier snow melt. C has early melt both cutting plant growth (less absorption) and raising heterotrophic respiration (more output) — both push net CO₂ up. A has it suppressing respiration, which pulls the other way, so A can't establish an increase. |
| RW_M2_HARD | 16 | Dec2023E 18 | C | **B** | Boundaries. Nothing belongs before the restrictive participle in "units of measurement used to record length and volume, respectively". C (`measurement. Used`) strands a subjectless fragment; A misplaces a comma; D leaves the participle dangling off "were … units of measurement". |

Two of the six (RW_M1 10, RW_M2_HARD 11) were caught earlier in the build, when the hand-built
tables were checked against their own questions. The other four came out of this full pass — i.e.
the table check alone would have shipped four wrong answers.

## Questions dropped and replaced

Neither could be repaired: in both cases the source PDF was not kept, so there is nothing to
check the transcript against. Both are in `UNUSABLE` in `format_rw.py` with the reason, and both
replacements are hand-transcribed from the October IntB page images (which *are* kept) and chosen
to carry the same skill, so the modules' domain mix and block ordering are unchanged.

| Dropped | Why | Replaced by |
|---|---|---|
| RW_M1, Nov2023 16 (theremin) | The stem was mistranscribed — it reads "Which choice completes the text with the most logical transition?" while all four choices are apostrophe/plural variants of "hands between the two antennas", i.e. a Standard English item wearing a neighbouring question's stem. The passage's punctuation around the blank is inconsistent with every choice's terminal punctuation as well. | OctIntB M1 Q21 (p018), Boundaries, answer **D** — nothing belongs between the subject "Ann Quinby of Kentucky" and its verb "played". |
| RW_M2_HARD, Nov2023 13 (Persad) | Asks which choice "best describes data from the table", but no table survives: the transcript kept only a structural description of it, with none of the numbers. The percentages scattered through the four choices could be assembled into a plausible table, but which row each belongs to is guesswork, and a wrong reconstruction would silently make a distractor correct. | OctIntB M2 Q9 (p032), Command of Evidence (quotation), answer **C** — the claim is about restorative sleep and C is the only quotation about sleep. |

Four other questions were already dropped earlier in the build for the same class of reason (two
line graphs whose source was not kept, a Boundaries item whose distinguishing comma was under a
watermark, and a choice hidden behind a cursor icon). Total dropped: 6 of 87 banked; all six
backfilled, so all three modules ship at a full 27.

## Skill mislabel, corrected

`RW_M2_HARD` order 9 (Nov2023 7, the alpine-soil microorganism question) was filed as *Central
Ideas and Details*, but its stem is "It can most reasonably be inferred from the text that …",
the canonical *Inferences* phrasing. Corrected via `SKILL_FIXES`. This matters twice over: skill
drives the question bank's filters, and the module's question order is derived from the skill,
so a mislabelled Inferences question sorts into the wrong block.

## What was checked and found clean

- All 81 answers re-derived independently (the 75 not listed above matched their recorded answer).
- Domain-block sequence monotonic in all three modules; no reading question after the writing
  block starts; reading counts 14 / 11 / 15, all within the ~15 cap.
- All three modules at exactly 27 questions, orders 1..27 contiguous.
- Every question that mentions a table/graph/figure has a real `<table>` or an image — the one
  regex hit (`RW_M2_EASY` 18) is the phrase "as researcher Yen-Ping Hsueh has *shown*", not a
  visual reference.
- No markdown asterisks, no prose wrapped in math mode, no missing spaces around inline math
  spans, no unescaped function names, no raw `/` division inside math mode, no carets outside a
  math wrapper (the two regex hits are `\[ … \]` display blocks, which the checker didn't track).
- Math side re-checked at the same time: 22 questions per module, 19 MC + 3 FR each, every
  `correctAnswerFR` a JSON-encoded array, all six figure files present on disk.
