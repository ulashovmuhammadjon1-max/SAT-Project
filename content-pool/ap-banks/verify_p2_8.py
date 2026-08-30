"""Key audit for AP PSYCHOLOGY 2.8 Intelligence and Achievement.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

THE EXCLUSION STATEMENT CONSTRAINS THIS TOPIC MORE THAN ANY OTHER IN UNITS 1-3,
and it is the first thing to check in any review of this module. EK 2.8.B.1
places LABELING OR DESCRIBING cognitive abilities and disabilities outside the
scope of the AP Psychology Exam. Accordingly:

  * no item names or defines any category of cognitive ability or disability;
  * no score or score range is attached to any label anywhere in the module;
  * item 5 keys the framework's stated modern use of IQ -- identifying students
    for educational services -- without naming any category of student.

A general intelligence bank would ordinarily carry several items of exactly the
kind the exclusion forbids, so their absence here is deliberate rather than
accidental, and this note exists so a later editor does not "fill the gap".

Three further points of care:

1. EK 2.8.B.2 supplies a two-by-two that students routinely collapse -- validity
   (construct, predictive) against reliability (test-retest, split-half). Items
   7-14 cover all four sub-types plus the head-on distinction, and item 10 is
   the case that separates them cleanly: a consistently wrong instrument is
   reliable and invalid at the same time.

2. EK 2.8.C.2's finding is directional and easy to reverse: scores vary MORE
   WITHIN a group than BETWEEN groups. Item 20 states it and item 21 asks what
   follows from it, because the finding matters only through its consequence.

3. EK 2.8.C.3 records the historical use of test scores to LIMIT access. Item 23
   states that history and item 30 applies it. Neither presents it as a current
   endorsed use, which would contradict EK 2.8.B.1.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_8

CLAIMS = [
 ("elusive and can be subject to bias",
  "EK 2.8.A.1, near verbatim: throughout history, consensus about how to define and measure intelligence continues to be elusive and can be subject to bias."),
 ("single general ability or a set of multiple distinct abilities",
  "EK 2.8.A.1: researchers debate whether intelligence is a general ability (called g) or is comprised of multiple abilities. The heredity/environment distractor is a real debate from Topic 1.1 and a different one."),
 ("intelligence is a general ability",
  "EK 2.8.A.1. Consistent performance across different kinds of task is the observation the general-ability side of the debate rests on; the multiple-abilities side predicts the opposite pattern, which is why it is the first distractor."),
 ("mental age divided by chronological age",
  "EK 2.8.B.1, verbatim in substance: early formal intelligence tests yielded an intelligence quotient which divided mental age by chronological age. The first distractor is that ratio inverted."),
 ("identify students for educational services",
  "EK 2.8.B.1 states this as the modern use. The remaining options are drawn from EK 2.8.C.3's list of historical MISUSES (jobs, immigration), which the framework records as harms rather than as purposes -- so the item separates the stated current use from the documented past abuse."),
 ("consistent procedures and environments",
  "EK 2.8.B.2.i, verbatim: a test is said to be standardized when it is administered using consistent procedures and environments. Note that this is about ADMINISTRATION, not about how many people take the test."),
 ("measures what it is designed to measure",
  "EK 2.8.B.2.ii, verbatim. The first distractor is the definition of reliability from the next EK, so the item turns entirely on which of the two properties is being named."),
 ("yields similar results each time it is administered",
  "EK 2.8.B.2.iii, verbatim. Paired with item 7 so the two definitions are each available in isolation before item 9 asks for the contrast."),
 ("validity is whether a test measures the intended construct; reliability is whether it gives consistent results",
  "EK 2.8.B.2.ii and 2.8.B.2.iii stated together. The first distractor is that contrast reversed; the last denies there is a difference, which is the misconception the pair exists to correct."),
 ("reliable but not valid",
  "EK 2.8.B.2.iii's reliability is consistency across administrations, which a scale that is wrong by the SAME amount every time satisfies; EK 2.8.B.2.ii's validity is measuring what it is designed to measure, which it fails. This is the case that proves the two properties are independent rather than two words for accuracy."),
 ("same test to the same people on two occasions",
  "EK 2.8.B.2.iii names test-retest among the types of reliability; it is the across-occasions method. The first distractor is split-half, the other named type."),
 ("one half of a test with scores on the other half",
  "EK 2.8.B.2.iii names split-half among the types of reliability; it compares two halves of a SINGLE administration, which is what distinguishes it from test-retest."),
 ("forecasts later performance",
  "EK 2.8.B.2.ii names construct and predictive validity as the two types; predictive validity is defined by the relationship to a later outcome. This also connects to EK 2.8.D.1's aptitude tests, which are the tests that live or die by it."),
 ("captures the theoretical quality it claims to measure",
  "EK 2.8.B.2.ii's other named type. Construct validity concerns the thing itself rather than a downstream outcome, which is the contrast with item 13."),
 ("fears confirming a negative stereotype about a group they belong to",
  "EK 2.8.B.3 names stereotype threat as one of the two effects socio-culturally responsive assessment aims to reduce. The Flynn effect is offered as a distractor because it also concerns score patterns, but across generations rather than within a testing situation."),
 ("performance advantage that can arise from awareness of a negative stereotype about another group",
  "EK 2.8.B.3 pairs stereotype lift with stereotype threat as sources of potential inequity. Lift is the advantage side of the same comparison, which is why the framework names both rather than only the threat."),
 ("reduce stereotype threat and the inequity that stereotype lift can create",
  "EK 2.8.B.3, near verbatim: researchers strive to develop assessments of intelligence that are socio-culturally responsive to reduce stereotype threat and potential inequity that may occur due to stereotype lift. The purpose is equity, not uniformly higher scores."),
 ("generally increased over time",
  "EK 2.8.C.1: IQ scores across much of the world have generally increased over time, which is the Flynn effect. The third distractor is EK 2.8.C.2's finding stated backwards, so two real framework facts are in play."),
 ("societal factors such as higher socioeconomic status",
  "EK 2.8.C.1 attributes the rise to societal factors, naming higher socioeconomic status and access to better health care and better nutrition. The framework gives a social explanation, not a psychometric artifact, which is what the distractors offer."),
 ("more within a group than between groups",
  "EK 2.8.C.2, verbatim in substance. The first distractor is the same sentence reversed, and it is the version that would support between-group comparisons -- which is exactly why the direction matters."),
 ("tells you very little about that person's score",
  "EK 2.8.C.2's finding means the spread inside any group is larger than the gap between group averages, so group membership is a weak basis for inferring an individual's score. This item asks for the consequence, since the finding is only meaningful through it. Note the key does not overclaim: it says 'very little', not 'nothing'."),
 ("poverty, discrimination, and educational inequities",
  "EK 2.8.C.2 names exactly these three as able to negatively influence the intelligence scores of individuals and societal groups around the world."),
 ("limit access to jobs, military ranks, educational institutions, and immigration",
  "EK 2.8.C.3, verbatim in substance. The framework records this as documented historical use; the key reports it as history, and nothing in the module presents it as a legitimate current purpose."),
 ("what a person currently knows",
  "EK 2.8.D.1: some academic tests attempt to measure what someone knows -- achievement tests. The first distractor is the aptitude definition from the same EK."),
 ("predict how a person will perform in the future",
  "EK 2.8.D.1: other tests attempt to predict how someone will perform in the future -- aptitude tests. Items 24 and 25 are adjacent so the pair must be known in both directions."),
 ("an achievement test",
  "EK 2.8.D.1. A course-content exam measures what was already taught and learned, which is the achievement side; nothing about it forecasts later performance."),
 ("set from birth and not changeable",
  "EK 2.8.D.2 contrasts the belief that intelligence is fixed from birth with the belief that it is malleable due to experience."),
 ("malleable and able to change through experience",
  "EK 2.8.D.2's other half, plus its consequence: these beliefs can affect academic achievement. Paired with item 27."),
 ("randomly assigning students to receive the lesson or a neutral lesson",
  "Science practice 2.B: only a manipulated, randomly assigned independent variable supports a causal conclusion. The survey, the depth interview, and the semester of observation are all non-experimental and can establish association at most."),
 ("can depress scores, and scores have historically been used to limit access",
  "Science practice 4.B. EK 2.8.C.2 (poverty, discrimination, educational inequities depress scores) and EK 2.8.C.3 (scores used to limit access) bear directly on the proposal. Each distractor asserts something the framework contradicts: EK 2.8.B.2.i makes standardization achievable, EK 2.8.D.1 separates achievement from aptitude, and EK 2.8.C.1's Flynn effect has scores rising, not falling."),
]

psych_check.check(p2_8, CLAIMS, per_topic=30, n_choices=4)
