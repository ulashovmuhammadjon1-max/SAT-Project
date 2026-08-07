# New source transcripts — Math content for Test 3+

Raw, sympy/logic-verified Math transcriptions from 4 newly-supplied source PDFs. These are
**not yet classified by Domain/Skill, deduped against each other, or inserted into the DB** —
this directory is a staging area, parallel to `content-pool/test-3-4-5-reading-writing/`
(which already covers R&W for Test 3/4/5 in full).

## Status by source

| source | file(s) | questions | status |
|---|---|---|---|
| `2024_May_IntA_EliteXSAT.pdf` | `may_inta_math_m1.json`, `may_inta_math_m2.json` | 22 + 21 = 43 | Done. No official answer key in this PDF — verified by sympy/logic only. |
| `2024_March_IntB_EliteXSAT.pdf` (Test 1 of file) | `march_intb_test1_math_m1.json`, `march_intb_test1_math_m2.json` | 22 + 22 = 44 | Done. Official answer key found (pages 93-95) and cross-checked — see conflicts below. |
| `2024_June_V2_EliteXSAT.pdf` | `junev2_math_m1.json`, `junev2_math_m2.json` | 19 + 22 = 41 | Done. Module 1's on-screen question badges genuinely skip 16, 18, 20 (confirmed by paging through the source screen-recording frame by frame — those 3 questions were simply never captured/photographed in this PDF), so only 19 of the real 22 are recoverable here. A compiled multi-test answer key was found at the end of the PDF but did NOT reliably align to this transcript (see note below) — most answers are cross-checked against the source's own circled/highlighted selections instead. |
| `2023_Dec_IntB_EliteXSAT.pdf` | *(not started)* | unknown | Not yet transcribed. May contain the Math section missing from the earlier partial Dec2023 R&W-only capture. |

Every item uses this schema:
```json
{
  "source": "MayIntA" | "MarchIntB_T1",
  "module": "MATH_M1" | "MATH_M2",
  "num": <1-indexed question number within that module as captured in the source>,
  "type": "MULTIPLE_CHOICE" | "FREE_RESPONSE",
  "problem": "...", "choices": [...], "correct": "...",
  "verified": "explanation of sympy/logic derivation, plus any conflict notes"
}
```

## Items requiring human follow-up before use in a shipped test

- **`may_inta_math_m1.json` Q18** — triangle geometry figure (points U,T,V,R,S) could not be
  reliably reconstructed from text; `correct` is `"UNVERIFIED"`. Needs the original page image.
- **`may_inta_math_m2.json` Q12** — star-cluster mass graph reading is approximate (visual
  estimate, not precise pixel/gridline reading). Re-verify against the actual image.
- **`may_inta_math_m2.json` Q14** — my derived answer (D) disagrees with the source's own
  circled/highlighted selection (A). I believe D is mathematically correct (y-intercept
  interpretation) and the highlight is a capture artifact, but flagged for a human double-check.
- **`may_inta_math_m2.json` Q7** — answer choices C/D text was lost to a page-break cutoff in
  the source capture; only A and B were legible. Answer (B) was derived independently, but exact
  wording of C/D is unknown.
- **`march_intb_test1_math_m1.json`** — 3 flagged items, all conflicts between my sympy/logic
  verification and my own parse of the official answer key string (a compressed, delimiter-free
  format that's genuinely hard to parse reliably): Q8, Q10, Q12/Q13/Q15 area. Q4 specifically:
  my algebra on the transcribed equation gives a different answer than BOTH the key AND the
  source's own circled selection (which agree with each other) — likely a transcription error
  in the stem's numbers on my part; used the key/selection-agreed answer (B) instead of my own.
- **`march_intb_test1_math_m2.json`** — 10 flagged items (of 22), the highest conflict rate of
  any file so far:
  - Q3, Q5, Q8, Q9, Q13, Q16, Q19, Q22 — my sympy/logic answer disagrees with my parse of the
    official key at that position. Kept my own (sympy/logic + source's circled selection where
    available) as primary, with the key's conflicting value noted for human re-verification.
  - Q15 — could not independently verify (imprecise graph reading of a line); used the key's
    answer (270) as the recorded value since I have no independent derivation to trust over it,
    but this is **not sympy-verified**, only key-sourced.
  - Q21 — source text too garbled/OCR-mangled to reconstruct the problem stem at all;
    `correct` is `"UNVERIFIED"`, with the key's value (17/32) noted for reference only.

  The unusually high conflict rate for this specific module (10/22, vs 3/22 for the same PDF's
  Module 1) suggests either a systematic key-parsing misalignment for this section specifically,
  or several genuine stem-transcription errors clustered in this module — a human should re-parse
  the raw key string (`"1-10 DDCAD A 16 B 33 C 11-20 7 DBC 270 149/9 B 18 A C 21-22 17/32 D"`)
  directly against the source image before trusting either side blindly.

- **`junev2_math_m1.json` Q1** — a parallel-lines-cut-by-transversal angle figure (138° given,
  find x) could not be reliably reconstructed from the extracted image; `correct` is
  `"UNVERIFIED"`. A compiled answer key found at the end of the PDF (covering 5 different "June"
  test date-variants in one document) gives 164 for this position, but that key showed a
  structural mismatch against this transcript starting around position 5 (expected a numeric
  free-response answer, the key showed a multiple-choice letter instead), strongly suggesting
  the key document was NOT compiled for this exact question set/order — so its value was
  **not** adopted here. Needs the original page image.
- **`junev2_math_m2.json` Q4** — inequality graph: the line's equation was estimated from
  approximate grid-point positions in the image (~(2,8) and ~(8,-4)), not exact coordinates.
  Answer (D) follows from that estimate; re-verify against the original image.
- **`junev2_math_m2.json` Q6** — population growth graph: the year-over-year ratio was read
  visually (not precise gridline positions), giving an approximate match to choice C (1.5x).
  Re-verify against the original image.
- The compiled answer key found at the end of `2024_June_V2_EliteXSAT.pdf` (covers "6月第1-5套"
  — 5 different June test date-variants) was cross-checked against `junev2_math_m1.json` and
  showed real structural disagreement (not just answer-letter mismatches) starting a few
  questions in, so it was treated as unreliable for this specific transcript and not used as a
  primary source — most `junev2` answers instead rely on independent sympy/logic verification,
  cross-checked against the source PDF's own circled/highlighted selections where visible.

## Not yet done
- Dec_IntB Math transcription (1 of 4 source PDFs remains).
- Cross-source dedup (especially June_V2, which shares R&W history with existing Test 1/2
  content — need to confirm no Math item here is a repeat of anything already used).
- Domain/Skill classification (ALG/ADV/PSDA/GT) for all items in this directory.
- Final assembly into an actual Test 3 module structure (22 MC+FR per module, ≤3 FR each,
  domain-block ordering per CLAUDE.md) — not started.
