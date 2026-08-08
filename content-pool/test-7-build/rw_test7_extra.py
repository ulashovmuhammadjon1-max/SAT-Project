#!/usr/bin/env python3
"""
Reading & Writing items authored to close the last gap in the Test 7 pool.

The unused pool covers every block's quota except Command of Evidence, which
runs one short across the three modules. Command of Evidence is also the safest
reading block to author: correctness turns on whether a quotation actually
states the claim, which is checkable by reading, rather than on a judgement call
about tone or emphasis.

Answers are derived here, never assumed — the `why` field records the reasoning
for the key and why each distractor fails. That is the Test 5 lesson: a source
answer key is not evidence, and 6 of 81 banked R&W answers were wrong.

Same dict shape as the transcribed rw_*.py modules, so the assembler treats
these identically.
"""

SOURCE = "AUTHORED-T7"
MODULE = "RW"

QUESTIONS = [
 dict(
   num="T7-CE1",
   skill="Command of Evidence",
   passage=(
     "In the 1920s the archaeologist Dorothy Garrod excavated a series of caves at Mount Carmel, "
     "in what is now Israel. Garrod employed an almost entirely female workforce drawn from "
     "nearby villages, an unusual arrangement for the period. Some later commentators have "
     "characterised this choice as a purely practical response to a shortage of available male "
     "labourers. A researcher studying Garrod&rsquo;s field notebooks, however, has argued that "
     "Garrod deliberately recruited and trained the women because she judged them better suited "
     "to the delicate work of clearing fragile deposits."
   ),
   stem=(
     "Which quotation from Garrod&rsquo;s notebooks, if genuine, would most directly support the "
     "researcher&rsquo;s argument?"
   ),
   choices=[
     "&ldquo;The men of the district being occupied with the harvest, I was obliged to look "
     "elsewhere for hands.&rdquo;",
     "&ldquo;I have set the women to the sieving, having found their touch far surer than any "
     "I could teach a labourer, and mean to keep them at it.&rdquo;",
     "&ldquo;The season has been fine, and the trenches are dry enough that work has gone "
     "forward without interruption.&rdquo;",
     "&ldquo;Wages here are low, and I am able to engage a great many more hands than the "
     "budget would allow in England.&rdquo;",
   ],
   answer="B",
   why=(
     "The researcher's claim has two parts: the recruitment was deliberate, and the reason was "
     "the women's suitability for delicate work. B carries both — 'having found their touch far "
     "surer' gives the judgement of suitability, and 'mean to keep them at it' makes it a "
     "choice rather than a necessity. A supports the opposing 'shortage of men' reading. C is "
     "about weather and says nothing about the workforce. D explains the size of the workforce "
     "by cost, not the choice of women by skill."
   ),
 ),

 # Spare, so the pool is not left with zero slack in this block.
 dict(
   num="T7-CE2",
   skill="Command of Evidence",
   passage=(
     "Ecologist Mireia Sol&agrave; has proposed that the reintroduction of beavers to a river "
     "catchment reduces the severity of downstream flooding, because the dams the animals build "
     "hold back water during heavy rain and release it slowly. Critics of the proposal note that "
     "beaver dams are small and frequently breached, and argue that any effect on a large "
     "catchment would be negligible. Sol&agrave; is preparing a study to test her hypothesis."
   ),
   stem=(
     "Which finding from Sol&agrave;&rsquo;s study, if true, would most directly support her "
     "hypothesis?"
   ),
   choices=[
     "Beaver dams in the catchment were rebuilt within days of being breached during storms.",
     "The number of beavers in the catchment increased steadily over the study period.",
     "Peak river levels downstream of the dammed reaches were substantially lower after "
     "reintroduction than before it, for storms of comparable rainfall.",
     "Water held behind the dams was clearer than water in undammed stretches of the river.",
   ],
   answer="C",
   why=(
     "The hypothesis is specifically about downstream flood severity, so the supporting finding "
     "has to measure that, and has to hold rainfall comparable so the comparison means "
     "something — which is exactly C. A answers the critics' point about breaching but does not "
     "itself show any flood effect. B measures the population, not the flooding. D is about "
     "water quality, a different outcome entirely."
   ),
 ),
]

DROPPED = {}
