"""Key audit for AP PSYCHOLOGY 3.1 Themes and Methods in Developmental Psychology.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

A NOTE ON THIS TOPIC'S SECOND HALF, because it changes what a key can rest on.
Learning objective 3.1.B -- "Describe ways cross-sectional and longitudinal
research design methods used in developmental psychology inform understanding
about behavior and mental processes" -- is printed in the CED WITHOUT any
essential-knowledge bullets beneath it. There is therefore no framework sentence
to quote for the properties of those designs. Items 15-30 are consequently keyed
only to what the two designs ARE and what a design of that shape can and cannot
support, which is the content of science practice 2.A, the skill the CED itself
attaches to this topic. Nothing here attributes to the framework a claim the
framework does not print. That distinction is the reason this note exists: an
EK-style citation on those items would be a fabrication.

The three themes of EK 3.1.A.1 are a closed list -- stability and change, nature
and nurture, continuous and discontinuous stages -- and items 3-12 work through
them. Because all three are pairs of opposites with similar grammar, every
scenario item is built so that exactly one theme has anything to act on:

    item 7   a trait persists from infancy to adulthood   -> stability/change
    item 8   an outcome needs BOTH predisposition and
             a particular environment                     -> nature/nurture
    item 9   growth is steady with no transitions         -> continuous/discont.

Item 12 tests the boundary of the list itself, with a real term from Unit 2
(convergent and divergent thinking, EK 2.2.A.8) as the intruder.

Two design facts kept straight throughout, since they are opposite weaknesses
and students attach them to the wrong design: the COHORT problem -- age
confounded with the era participants grew up in -- belongs to the cross-sectional
design (items 21, 22); ATTRITION and elapsed time belong to the longitudinal
design (items 22, 23). Item 24 makes the point that neither design can support a
causal claim about aging, because age cannot be assigned; item 21's third
distractor offers random assignment to age groups precisely because it is
impossible.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_1

CLAIMS = [
 ("chronological order of development and thematic issues",
  "EK 3.1.A.1, near verbatim: developmental psychology is concerned with both chronological order of development and/or thematic issues in development across the lifespan."),
 ("stability and change; nature and nurture; continuous and discontinuous",
  "EK 3.1.A.1 names exactly these three thematic issues. The distractors are the memory stages (2.3-2.7), processes from Units 1-2, and the psychometric principles of EK 2.8.B.2 -- all real course content on other lists."),
 ("present early in life persists or is transformed",
  "EK 3.1.A.1 names stability and change among the themes; it is the question of whether an early characteristic endures. The other two options are the framework's other two themes, so the item discriminates within the closed list."),
 ("inherited predisposition or from experience",
  "EK 3.1.A.1 names nature and nurture among the themes, and EK 1.1.A.1 supplies its content -- heredity and environmental factors interacting to shape behavior and mental processes."),
 ("gradual accumulation or through a series of distinct stages",
  "EK 3.1.A.1 names continuous and discontinuous stages of development among the themes: the question is whether change is incremental or stage-like."),
 ("continuous-versus-discontinuous theme",
  "EK 3.1.A.1. A fixed sequence of QUALITATIVELY DIFFERENT stages is the discontinuous position; the word 'stages' in the stem is the signal, and nothing in the scenario concerns persistence or origin."),
 ("stability-and-change theme",
  "EK 3.1.A.1. Shyness persisting from infancy to adulthood is a claim about whether an early characteristic endures. Nothing in the stem concerns the shape of change or its origin, so the other two themes have nothing to act on."),
 ("nature-and-nurture theme",
  "EK 3.1.A.1 plus EK 1.1.A.1's interaction claim. The stem requires BOTH a family history and a particular environment, which is the interaction of heredity and experience rather than a claim about persistence or stages."),
 ("development is continuous",
  "EK 3.1.A.1. Steady accumulation with no sharp transitions is the continuous side; the stem's 'no sharp transitions' is what excludes the discontinuous reading."),
 ("stability-and-change question",
  "EK 3.1.A.1. Whether a trait at 5 predicts the same trait at 40 is the persistence question. The fourth distractor -- test-retest reliability, EK 2.8.B.2.iii -- is included because a 35-year re-measurement superficially resembles it, but reliability concerns the instrument, not the person."),
 ("whether development is continuous or discontinuous",
  "EK 3.1.A.1. 'Gradually or in identifiable jumps' is that theme stated in ordinary words, which is how the disagreement would actually be voiced."),
 ("convergent and divergent thinking",
  "EK 3.1.A.1's list has exactly three members. Convergent and divergent thinking belongs to EK 2.2.A.8's account of creativity in Unit 2, so it is real course content in the wrong place -- which is what makes it a fair intruder rather than a giveaway."),
 ("sequence in which developments occur",
  "EK 3.1.A.1 pairs chronological ORDER with the thematic issues. Order is a claim about sequence, not about exact ages -- and EK 3.2.B.1 says so explicitly: physical development happens in generally the same order, but the timing can vary. That EK is what rules out the second option."),
 ("from before birth through late adulthood",
  "EK 3.1.A.1 says 'across the lifespan', and Topic 3.2's own objectives run from prenatal development (3.2.A) through adulthood (3.2.D), which fixes what the phrase covers in this course."),
 ("compares people of different ages at a single point in time",
  "Objective 3.1.B names cross-sectional and longitudinal as the developmental methods. This is what a cross-sectional design is. The last distractor -- assigning participants to ages -- is impossible, and it recurs deliberately at item 21."),
 ("follows the same participants over an extended period",
  "Objective 3.1.B. This is what a longitudinal design is: the same people re-measured across time."),
 ("compares different people of different ages at once; a longitudinal design re-measures the same people",
  "The two designs of objective 3.1.B differ in exactly this. The first distractor reverses it; the third is false because neither design manipulates anything, which is the point item 24 develops."),
 ("cross-sectional",
  "Three age groups measured in one week is the cross-sectional shape: different people, one time point, no manipulation."),
 ("longitudinal",
  "The same 200 people measured at three ages is the longitudinal shape. Items 19 and 20 are adjacent so the pair must be recognised in both directions."),
 ("produces results in far less time",
  "The practical trade-off between the two designs: a cross-sectional study collects everything at once instead of waiting decades. The fourth option -- that it guarantees the groups differ only in age -- names precisely what a cross-sectional design CANNOT guarantee, which item 21 then makes the subject of its own question."),
 ("grew up in different eras and may differ in schooling",
  "The cohort problem. In a cross-sectional design, age groups are also different birth cohorts, so anything that changed across eras -- schooling, nutrition, test familiarity -- varies alongside age. Note the third distractor proposes random assignment to age groups, which is impossible; that impossibility is the subject of item 24."),
 ("takes a long time and participants may drop out",
  "The longitudinal trade-off: elapsed time and attrition. The third option is the CROSS-SECTIONAL weakness from item 21, placed here on purpose -- the two designs have opposite characteristic problems and students attach them to the wrong one."),
 ("no longer representative of the group that started",
  "Selective attrition: if dropouts differ systematically from stayers, later measurements describe a different -- often healthier or more motivated -- sample than the one recruited, so change over time is confounded with change in who remains."),
 ("age cannot be manipulated or randomly assigned",
  "Science practice 2: a causal conclusion requires a manipulated, randomly assigned independent variable. No researcher can assign a participant an age, so BOTH developmental designs are non-experimental by necessity rather than by choice. This is the item that unifies 21-23."),
 ("longitudinal study following the same children as the skill emerges",
  "A claim about the ORDER in which developments occur WITHIN a person requires observing a sequence within individuals, which only re-measurement over time provides. A one-day comparison of different children cannot observe any individual's sequence, and the third option proposes assigning a developmental order, which is not something a researcher can do."),
 ("number of seconds a child can balance on one foot",
  "An operational definition states a specific, repeatable measurement procedure. A timed balance is countable; 'appears capable', 'overall level of physical development', and enjoyment are unmeasurable as stated or measure a different construct."),
 ("may differ systematically from families who would not volunteer",
  "Generalizability: volunteers for a 20-year commitment are self-selected and may differ in stability, resources, and motivation from the population the conclusions are meant to cover. This is the skill the exam's AAQ tests directly."),
 ("informed consent from each infant's parent or guardian",
  "Science practice 2.D. Infants cannot consent for themselves, so consent comes from a guardian, and protection from harm requires ending a session that distresses the participant. The 'guarantee significant findings' distractor describes a bias rather than a safeguard."),
 ("relationship holds over time but still does not establish that reading is the cause",
  "A longitudinal design establishes temporal order -- the earlier measure really did precede the later one -- but manipulates nothing, so home environment or another third variable remains a live explanation. Temporal order is necessary for causation and not sufficient for it, which is the specific reasoning error the newspaper makes."),
 ("improves in small steady increments with no identifiable transitions",
  "Science practice 4.B. The student's claim is the DISCONTINUOUS side of EK 3.1.A.1's continuous/discontinuous theme, so only evidence about the SHAPE of change bears on it. The other options are evidence about the other two themes -- stability, and nature and nurture -- and leave the stage claim untouched."),
]

psych_check.check(p3_1, CLAIMS, per_topic=30, n_choices=4)
