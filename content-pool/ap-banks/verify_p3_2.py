"""Key audit for AP PSYCHOLOGY 3.2 Physical Development Across the Lifespan.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

EXCLUSION STATEMENT, checked first in any review of this module: EK 3.2.A.1
places the STAGES of prenatal development -- zygote, embryo, and fetus -- outside
the scope of the AP Psychology Exam. Those three words appear nowhere in this
module, as keys or as distractors. Prenatal content here is confined to what EK
3.2.A.1 does state: the factors that can influence prenatal milestones.

Two framework statements that a writer is likely to overstate, and which the
keys here deliberately do not:

1. EK 3.2.B.1 says development happens in generally the same ORDER but that the
   TIMING can vary. Items 3, 4 and 30 all turn on holding those two apart. The
   easy error is to key "every child develops at the same age", which is the
   opposite of what the EK says and is exactly the belief item 4's worried parent
   holds.

2. EK 3.2.B.4 confines IMPRINTING to "some non-human animals". Item 16 makes
   that limit the answer. A key extending imprinting to human infants would
   assert something the framework does not, and human attachment is treated
   separately in Topic 3.6, so the two are kept apart here.

Coverage is spread across the four objectives roughly in proportion to their
essential knowledge: 3.2.A prenatal, items 1-2; 3.2.B infancy and childhood,
items 3-16 (the largest, with four EKs); 3.2.C adolescence, items 17-20; 3.2.D
adulthood, items 21-24; and items 25-30 are the cross-cutting design, data, and
claim items the CED's suggested skills 3.C and 4.A call for. Every result those
items use is stated in the stem as prose -- there are no figures in this bank.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_2

CLAIMS = [
 ("reach a developing organism before birth and disrupt development",
  "EK 3.2.A.1 names teratogens first among the factors that can influence the major physical and psychological milestones of prenatal development. The definition given is what the term denotes in the course; the excluded stage words are not used."),
 ("teratogens, maternal illness, genetic mutations",
  "EK 3.2.A.1 lists teratogens, maternal illness, genetic mutations, hormonal, and environmental factors. The distractors are Unit 2 content -- the serial position effect and chunking (2.4), reliability types (2.8.B.2), interference (2.7.A.2) -- so all four options are real course terms."),
 ("generally the same order, though the timing can vary",
  "EK 3.2.B.1, near verbatim: physical development in infancy and childhood happens in generally the same order, but the timing of the development can vary. Both halves are load-bearing and the key keeps both."),
 ("order of motor milestones is consistent across children, but the timing varies",
  "EK 3.2.B.1 applied. The parent's worry treats an off-average TIME as a departure from the ORDER, and the EK separates exactly those. The second distractor is the belief the item exists to correct."),
 ("large movements such as walking, running, and climbing",
  "EK 3.2.B.1 names the development of fine and gross motor coordination among the milestones of infancy and childhood; gross coordination is the large-movement half of that pair."),
 ("small precise movements",
  "EK 3.2.B.1's other half. Items 5 and 6 are adjacent so the pair must be known in both directions."),
 ("critical skills needed to become more independent",
  "EK 3.2.B.1 states that these physical skills develop as children mature, allowing children to develop critical skills needed to become more independent. That is the framework's own reason for treating motor development as psychological and not merely physical."),
 ("infant reflex indicating on-track physical and psychological milestone development",
  "EK 3.2.B.2, near verbatim: infants possess reflexes, like the rooting reflex, that indicate on-track physical and psychological milestone development. The first distractor calls it learned, which contradicts 'possess'."),
 ("milestone development is on track",
  "EK 3.2.B.2 gives reflexes a diagnostic role -- their presence indicates development is on track -- which is why a clinician checks for them. This item asks what the reflexes INDICATE, where item 8 asks what the rooting reflex IS."),
 ("early ability to perceive depth",
  "EK 3.2.B.3, verbatim in substance: research using the visual cliff apparatus demonstrates an early ability in infants to perceive depth."),
 ("innovative way to assess infant responses",
  "EK 3.2.B.3's second clause, which is a METHODOLOGICAL credit rather than a finding. The framework names both, and a module that keyed only the depth finding would drop half of the EK."),
 ("cannot report what they perceive, so researchers must infer it from behavior",
  "EK 3.2.B.3 calls the apparatus an innovative way to ASSESS INFANT RESPONSES, and the reason such innovation is needed is that a preverbal participant's perception has to be read from behavior. This is the item that explains why 3.2.B.3's methodological clause is in the framework at all."),
 ("window in development during which an experience has an especially strong effect",
  "EK 3.2.B.4: research suggests that critical or sensitive periods in infancy and childhood have strong developmental effects. The framework's hedge -- 'research suggests' -- is why the key describes the window rather than asserting a hard boundary."),
 ("language",
  "EK 3.2.B.4 names language specifically: critical or sensitive periods have strong developmental effects, especially for skills such as language. The distractors are all learned academic skills the framework does not name."),
 ("non-human animals will attach to the first object they encounter",
  "EK 3.2.B.4, near verbatim: some non-human animals will imprint on the first object they encounter as a means of survival. Both qualifiers -- 'some' and 'non-human' -- are in the key."),
 ("describes imprinting in some non-human animals, not in humans",
  "EK 3.2.B.4 confines imprinting to some non-human animals. Extending it to human infants asserts what the framework does not, and human attachment is Topic 3.6's subject instead. This item exists because the extension is the standard popular misreading."),
 ("adolescent growth spurt and puberty",
  "EK 3.2.C.1, verbatim: the main physical and psychological milestones that occur in adolescence are the adolescent growth spurt and puberty. The distractors pair milestones from the other three periods."),
 ("development of reproductive ability",
  "EK 3.2.C.1 defines puberty as the period in which reproductive ability develops. That is what separates it from the growth spurt, which occurs alongside it and is about size rather than reproduction."),
 ("sex characteristics developing during adolescence",
  "EK 3.2.C.1: adolescents develop primary and secondary sex characteristics during this time, such as menarche and spermarche. The framework offers both terms together, so the key names the category they exemplify."),
 ("adolescent growth spurt",
  "EK 3.2.C.1. Rapid gain in height within a year is the growth spurt rather than puberty, which the same EK defines by reproductive ability -- the two co-occur but are not the same milestone."),
 ("leveling off followed by a varying decline",
  "EK 3.2.D.1, near verbatim: adulthood spans most of the lifespan and is characterized by a general leveling off and then a varying decline. The 'no measurable change' and 'continued rapid growth' distractors are the two ways to get the shape wrong."),
 ("reproductive ability, mobility, flexibility, reaction time, and sensory acuity",
  "EK 3.2.D.1 names exactly these: reproductive ability (menopause), mobility, flexibility, reaction time, and visual and auditory sensory acuity. Vocabulary and general knowledge are NOT on the framework's decline list, which is why the second option is wrong rather than merely unlisted."),
 ("decline in reproductive ability that occurs during adulthood",
  "EK 3.2.D.1 gives menopause as its parenthetical example of declining reproductive ability in adulthood."),
 ("extent and rate of decline differ from person to person",
  "EK 3.2.D.1 says 'a VARYING decline'. The adjective is doing work: the framework asserts that the pattern is not uniform across individuals, which is what rules out both a fixed schedule and no decline at all."),
 ("prenatal, infancy and childhood, adolescence, adulthood",
  "Learning objectives 3.2.A, 3.2.B, 3.2.C, and 3.2.D are organized in exactly this order, which is also the chronological order EK 3.1.A.1 makes one of developmental psychology's two concerns."),
 ("cross-sectional",
  "Objective 3.1.B's cross-sectional design: different age groups measured at a single point in time. Age cannot be manipulated or assigned, so this is not an experiment -- the same reasoning as item 24 of Topic 3.1."),
 ("responded differently to the two sides, which is consistent with early depth perception",
  "EK 3.2.B.3 credits the visual cliff with demonstrating early depth perception, and a large behavioural difference between the shallow and deep sides is what licenses that inference. The key says 'consistent with' rather than 'proves', and the distractors propose explanations the stated result gives no evidence for."),
 ("no one may ethically be assigned to be exposed to a suspected harmful substance",
  "Science practice 2.D. Assigning a participant to a suspected harm violates the obligation to protect participants, so human evidence about the teratogens named in EK 3.2.A.1 necessarily comes from non-experimental designs."),
 ("number of stairs a child can climb unassisted",
  "An operational definition states the countable procedure. A stair count is measurable; 'appears advanced', 'general level of coordination', and liking to move around restate the construct or measure preference rather than ability."),
 ("general order while its timing varies",
  "Science practice 4.B. The parent infers a general deficit from off-average timing, and EK 3.2.B.1 is precisely the statement that separates order from timing. The other three options are accurate framework content about other periods of life and bear on the claim not at all."),
]

psych_check.check(p3_2, CLAIMS, per_topic=30, n_choices=4)
