"""Key audit for AP PSYCHOLOGY 3.4 Cognitive Development Across the Lifespan.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

THREE THINGS THIS MODULE DELIBERATELY DOES NOT DO, each of which is the standard
way a Piaget bank goes wrong:

1. NO STAGE IS GIVEN A NUMBER OF YEARS. The CED states the spans in words --
   "infancy through toddlerhood" (3.4.A.1.i), "toddlerhood through early
   childhood" (3.4.A.1.ii), "early through late childhood" (3.4.A.1.iii), "late
   childhood through adulthood" (3.4.A.1.iv) -- and never in ages. Test-prep
   material supplies "0-2, 2-7, 7-11, 11+"; the framework does not, and a key
   asserting those numbers would be asserting something the course does not
   teach. Item 19 tests the ORDER, which the framework does state.

2. THE FORMAL OPERATIONAL STAGE IS NOT PRESENTED AS UNIVERSAL. EK 3.4.A.1.iv
   says in so many words that Piaget proposed NOT ALL PEOPLE achieve formal
   operational thinking. Item 18 keys that directly, and no other item implies an
   endpoint everyone reaches.

3. NORMAL AGING IS NOT CONFUSED WITH DISORDER. EK 3.4.A.3 gives waning fluid
   intelligence as ordinary adult development and lists dementia separately as a
   cognitive DISORDER. Item 27's scenario matches the ordinary pattern and offers
   "the onset of a cognitive disorder" as a distractor for exactly that reason;
   item 28 keys dementia as a disorder rather than as a feature of aging.

A cross-unit note: assimilation and accommodation are DEFINED in EK 2.2.A.2, in
Unit 2, and invoked again by name in EK 3.4.A.1. Items 4 and 5 use the Unit 2
definitions in the Piagetian setting, and the claims cite both EKs, because
citing only one would misrepresent where the definition lives.

The preoperational stage carries the most content in the framework (symbols and
pretend play; conservation and reversibility as failures; animism and
egocentrism as exhibited characteristics; theory of mind beginning), so it
carries the most items here -- 6 through 14. That is proportionality to the EK,
not enthusiasm for the stage.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_4

CLAIMS = [
 ("continuous and discontinuous processes such as assimilation and accommodation",
  "EK 3.4.A.1, near verbatim: according to Piaget, children develop schemas via continuous and discontinuous processes such as assimilation and accommodation. Note that the framework says BOTH continuous and discontinuous, which connects this topic to EK 3.1.A.1's theme."),
 ("sensorimotor stage, during which object permanence develops",
  "EK 3.4.A.1.i: the sensorimotor stage occurs from infancy through toddlerhood, and object permanence develops during it. Each distractor pairs a real stage with an achievement the framework assigns to a different one."),
 ("continues to exist when it cannot be seen",
  "EK 3.4.A.1.i assigns object permanence to the sensorimotor stage. The distractors are conservation and reversibility (EK 3.4.A.1.ii) and theory of mind (same EK), so all four options are real course content."),
 ("assimilation",
  "EK 2.2.A.2 defines assimilation as taking in new information but NOT changing the schema; EK 3.4.A.1 names it as one of the processes by which Piagetian schemas develop. The stem states that she does not change the category, which is the clause that excludes accommodation."),
 ("accommodation",
  "EK 2.2.A.2 defines accommodation as taking in new information AND changing the schema; EK 3.4.A.1 names it as a Piagetian process. The stem states that she revises the category. Items 4 and 5 are the same child in sequence."),
 ("using mental symbols, including engaging in pretend play",
  "EK 3.4.A.1.ii: children become proficient in using mental symbols and engage in pretend play. This is the stage's positive content, as opposed to the failures the same EK says it is identified more by."),
 ("cognitive tasks children cannot yet perform and the errors they do exhibit",
  "EK 3.4.A.1.ii, and the wording is unusual enough to be worth testing: the preoperational stage is identified MORE BY cognitive tasks children CANNOT perform, such as conservation and reversibility, or by those they EXHIBIT, such as animism and egocentrism. This framing is also what item 30's criticism turns on."),
 ("quantity stays the same even when its appearance changes",
  "EK 3.4.A.1.ii names conservation among the tasks preoperational children cannot perform. The distractors are object permanence, egocentrism, and animism -- three more terms from the same stage."),
 ("conservation",
  "EK 3.4.A.1.ii. Judging quantity by the height of the column rather than by the amount poured is the standard demonstration that conservation is absent. Object permanence is excluded because nothing is hidden."),
 ("mentally undone to return to the starting state",
  "EK 3.4.A.1.ii lists reversibility beside conservation among the preoperational failures. The two are linked: mentally pouring the water back is what would show the quantity unchanged, which is why the framework names them together."),
 ("attributing lifelike qualities to inanimate objects",
  "EK 3.4.A.1.ii names animism among the characteristics preoperational children EXHIBIT, as distinct from the tasks they cannot perform."),
 ("difficulty taking a perspective other than one's own",
  "EK 3.4.A.1.ii names egocentrism among the exhibited characteristics. In Piaget's usage it is a limitation of PERSPECTIVE-TAKING, not selfishness -- the second distractor is the everyday meaning of the word, which is the misreading this item exists to catch."),
 ("egocentrism",
  "EK 3.4.A.1.ii. Holding the book so that only he can see it, while describing it to someone else, is failure to take the listener's visual perspective. Nothing in the stem involves attributing life to an object, which excludes animism."),
 ("beliefs, desires, and knowledge that may differ from one's own",
  "EK 3.4.A.1.ii states that children begin to develop a theory of mind during the preoperational stage. It concerns others' MENTAL STATES, which is what separates it from the three physical-world understandings offered as distractors."),
 ("correct the cognitive errors of the preoperational stage",
  "EK 3.4.A.1.iii: children in the concrete operational stage can generally correct the cognitive errors made in the preoperational stage and understand the world in logical, realistic, and straightforward ways."),
 ("struggle to think systematically",
  "EK 3.4.A.1.iii's own stated limitation, and the one that the formal operational stage removes. The other options describe deficits the framework places in earlier stages or nowhere at all."),
 ("think abstractly and hypothetically",
  "EK 3.4.A.1.iv: people in the formal operational stage gain the ability to think abstractly and hypothetically. The distractors are achievements EK 3.4.A.1.i-iii assign to earlier stages."),
 ("not all people achieve formal operational thinking",
  "EK 3.4.A.1.iv states this explicitly, and it is the framework's own hedge on the stage sequence. A bank that omitted it would leave students with a universal-endpoint picture the CED specifically declines to give."),
 ("sensorimotor, preoperational, concrete operational, formal operational",
  "The order of EK 3.4.A.1.i through 3.4.A.1.iv. The framework states the order and the spans in words; it never states ages, so this item tests sequence and no item in the module tests years."),
 ("formal operational stage",
  "EK 3.4.A.1.iv. Reasoning about the consequences of a change that has not occurred is hypothetical thought by definition, which EK 3.4.A.1.iii denies to concrete operational thinkers."),
 ("social learners, through interacting with other people within sociocultural contexts",
  "EK 3.4.A.2, near verbatim: according to Vygotsky, children are social learners who learn through interacting with and scaffolding by other people within sociocultural contexts."),
 ("support provided by a more capable person",
  "EK 3.4.A.2 names scaffolding by other people as the means of social learning. The support comes from someone more capable and is fitted to what the learner can currently do -- which is what links it to the zone of proximal development in item 23."),
 ("cannot yet do alone but can do with appropriate help",
  "EK 3.4.A.2: ideally learning occurs while the person is in their zone of proximal development. The second distractor -- what the learner can already do alone -- is the boundary the zone starts ABOVE, which is the distinction the term exists to make."),
 ("scaffolding within the zone of proximal development",
  "EK 3.4.A.2 pairs the two: support adjusted to a task the learner cannot yet do alone, then withdrawn as capability grows. The stem supplies both halves -- the hint and its withdrawal -- so the answer requires the pairing rather than either term alone."),
 ("Piaget emphasizes stages through which children develop schemas; Vygotsky emphasizes learning through social interaction",
  "EK 3.4.A.1 presents Piaget through schemas and stages; EK 3.4.A.2 presents Vygotsky through social learning, scaffolding, and sociocultural context. The first distractor swaps the two theorists, which is the error worth catching."),
 ("crystallized intelligence remains relatively stable while fluid intelligence tends to wane",
  "EK 3.4.A.3, verbatim in substance. The first distractor is that sentence with the two kinds of intelligence swapped."),
 ("stable crystallized intelligence alongside waning fluid intelligence",
  "EK 3.4.A.3 applied. Vocabulary and accumulated knowledge are crystallized; speed on unfamiliar problems is fluid. The 'onset of a cognitive disorder' distractor is there because EK 3.4.A.3 treats this pattern as ORDINARY adult development and lists dementia separately -- inferring disorder from the normal pattern is the error."),
 ("cognitive disorder that affects adults",
  "EK 3.4.A.3: cognitive disorders that affect adults include dementia. The framework lists it as a disorder, NOT as a feature of ordinary aging, which is what the second distractor asserts."),
 ("cross-sectional",
  "Objective 3.1.B's cross-sectional design: different age groups measured at one point in time. Age cannot be manipulated or assigned, so the study is not an experiment -- the same reasoning as Topic 3.1 item 24 and Topic 3.2 item 26."),
 ("identified more by the tasks children cannot perform, which makes stage placement depend on how the task is posed",
  "Science practice 4.B. EK 3.4.A.1.ii's own wording is the hinge: if a stage is identified by FAILURES on particular tasks, then a task that is easier to understand can reveal competence the original task concealed. The other three options are accurate framework content that bears on adulthood, on Vygotsky, and on the stage sequence's endpoint rather than on this criticism."),
]

psych_check.check(p3_4, CLAIMS, per_topic=30, n_choices=4)
