"""Key audit for AP PSYCHOLOGY 3.6 Social-Emotional Development Across the
Lifespan.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

FOUR THINGS THIS MODULE DELIBERATELY DOES NOT DO:

1. NO THEORIST IS NAMED, anywhere, as a key or as a distractor. The CED presents
   ecological systems theory (3.6.A.1), the monkey attachment studies
   (3.6.A.3.ii), and the stage theory of psychosocial development (3.6.A.6)
   without attributing any of them to a person. Test-prep material supplies
   names; the framework does not, and keying an item to a name the course never
   prints would test something outside the course.

2. NO PSYCHOSOCIAL STAGE IS GIVEN AN AGE. EK 3.6.A.6 lists eight conflicts in
   order and attaches no ages to them. Item 28 tests the ORDER, which the
   framework does state.

3. NO PARENTING STYLE IS RANKED AS BEST. EK 3.6.A.2 says explicitly that
   CULTURAL DIFFERENCES EXIST in the ways these styles affect outcomes, and
   EK 3.6.A.3 says attachment styles VARY BY CULTURE. Items 11 and 16 make those
   two qualifications the answer rather than burying them. A bank that keyed
   "authoritative parenting produces the best outcomes" would contradict the
   framework's own sentence.

4. NO PSYCHOSEXUAL CONTENT APPEARS. The exclusion statement under EK 3.6.A.6
   places that theory outside the exam; item 25 keys the exclusion itself, which
   is the only appearance of the word in the module.

This objective carries eight EKs, more than any other in Unit 3, so coverage is
allocated in proportion: ecological systems 1-7, parenting 8-11, attachment
12-16, peers and adolescence 17-21, adulthood 22-24, psychosocial 25-28, ACEs 29,
identity 30.

One naming trap worth recording: AUTHORITARIAN and AUTHORITATIVE differ by three
letters and name nearly opposite styles. Items 9 and 10 are adjacent, each
scenario specifies whether reasons are explained and whether the child's view is
heard, and each item carries the other term as its first distractor.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_6

CLAIMS = [
 ("social environment influences development",
  "EK 3.6.A.1: the ecological systems theory explores how the social environment influences development. The framework names the theory but no theorist, and neither does this item."),
 ("groups that have direct contact with the individual",
  "EK 3.6.A.1's definition of the microsystem, verbatim. Every distractor is the framework's definition of one of the other four systems, so the item is a within-list discrimination."),
 ("relationships between the groups that have direct contact",
  "EK 3.6.A.1: the mesosystem is the relationships BETWEEN groups in the microsystem. The distinction from the microsystem is a level, not a size -- which is exactly what the first distractor tests."),
 ("mesosystem",
  "EK 3.6.A.1. Family and school are each microsystems; the coordination BETWEEN them is the mesosystem. The scenario is built so that two microsystem groups are named and the relationship between them is what the question asks about."),
 ("exosystem",
  "EK 3.6.A.1 defines the exosystem as indirect factors in an individual's life. The stem states that the child never visits the workplace, which is the clause making the influence indirect and ruling out the microsystem."),
 ("macrosystem",
  "EK 3.6.A.1 defines the macrosystem as cultural events that affect the individuals and others around them."),
 ("current stage of life",
  "EK 3.6.A.1 defines the chronosystem as the individual's current stage of life. Note that the framework's definition is about the individual's stage, not about historical time -- which is how the term is often loosely explained elsewhere."),
 ("authoritarian, authoritative, and permissive",
  "EK 3.6.A.2 names these three parenting styles. The distractors are the attachment styles (3.6.A.3), the play types (3.6.A.4.i), and the identity processes (3.6.A.8) -- three other closed lists from this same objective, which is what makes the item a real test of which list a term belongs to."),
 ("authoritarian",
  "EK 3.6.A.2. Strict rules with obedience expected and little explanation is what the term denotes. The stem specifies that reasons are not given and negotiation does not occur, which is precisely the clause that excludes the authoritative style."),
 ("authoritative",
  "EK 3.6.A.2. Clear expectations PLUS explanation PLUS responsiveness is the authoritative pattern. Items 9 and 10 are adjacent because the two words differ by three letters and name nearly opposite styles; each stem specifies the explanation-and-responsiveness variable so exactly one answer fits."),
 ("cultural differences exist in the ways these styles affect outcomes",
  "EK 3.6.A.2 states this explicitly. It forbids a universal ranking of the styles, which is why no item in this module keys one style as producing the best outcomes -- that would contradict the framework's own sentence."),
 ("secure and insecure, with insecure comprising avoidant, anxious, and disorganized",
  "EK 3.6.A.3: the types of attachment infants and children display include secure and insecure (avoidant, anxious, and disorganized). The key preserves the nesting -- three subtypes UNDER insecure -- rather than listing four coordinate styles."),
 ("temperament",
  "EK 3.6.A.3 states that temperament is related to how children attach to caregivers. This locates some of the variation in the child rather than entirely in the caregiver, which is a substantive claim and not a throwaway."),
 ("heightened anxiety or fear when away from a caregiver or in the presence of a stranger",
  "EK 3.6.A.3.i, verbatim in substance. The framework's definition covers BOTH the absence of the caregiver and the presence of a stranger, and the key keeps both halves."),
 ("importance of comfort over food",
  "EK 3.6.A.3.ii: studies with monkeys demonstrate the importance of comfort over food in attachment. The framework names no researcher, and neither does the item. The second distractor is the feeding account the studies were designed to test against."),
 ("vary by culture",
  "EK 3.6.A.3 states that the attachment styles vary by culture. Together with EK 3.6.A.2's parallel statement about parenting, this is the framework's standing caution against reading either taxonomy as a universal ranking."),
 ("parallel play",
  "EK 3.6.A.4.i names parallel and pretend play as how children engage with peers. Playing ALONGSIDE rather than WITH is what parallel play denotes, and the stem states the side-by-side, non-joint arrangement."),
 ("pretend play",
  "EK 3.6.A.4.i's other named form. Symbolic use of objects and assigned roles in a shared invented scenario is what pretend play denotes; the stem supplies both the symbolic object and the roles."),
 ("gradually rely more on peer relationships",
  "EK 3.6.A.4.ii, verbatim in substance: adolescents gradually rely more on peer relationships as they age. The framework says 'more', not 'exclusively', which is why the withdrawal and cessation distractors overstate."),
 ("imaginary audience",
  "EK 3.6.A.4.ii names the imaginary audience as one expression of adolescent egocentrism: believing oneself to be the object of others' attention. The stem is about what OTHERS are thought to notice, which is what separates it from the personal fable."),
 ("personal fable",
  "EK 3.6.A.4.ii names the personal fable alongside the imaginary audience. It is a belief about one's own uniqueness and invulnerability -- about the SELF rather than about others' attention. Items 20 and 21 are adjacent because the two terms come from one sentence and are routinely swapped."),
 ("culture's expectations about when adulthood begins and when major life events should occur",
  "EK 3.6.A.5.i: culture plays a role in determining when adulthood begins and when major life events occur -- the social clock. The circadian-rhythm distractor is real course content from EK 1.5.A.2 and is included because both terms involve timing."),
 ("period some cultures allow as a transition",
  "EK 3.6.A.5.i says SOME cultures allow for a time of emerging adulthood. The framework presents it as culturally variable, so the 'universal biological stage' distractor contradicts the EK rather than merely differing from it."),
 ("can affect how adults form attachments to other adults",
  "EK 3.6.A.5.ii states that childhood attachment styles CAN AFFECT how adults form attachments to other adults. 'Can affect' is weaker than determination, which is why the third option -- complete and unchangeable determination -- overstates the framework."),
 ("psychosexual stage theory",
  "The exclusion statement under EK 3.6.A.6 places the psychosexual stage theory of development outside the scope of the exam, while the PSYCHOSOCIAL stage theory in the same EK is required content. The two names differ by two letters, which is what makes the boundary worth testing."),
 ("resolve a psychosocial conflict at each stage",
  "EK 3.6.A.6: the stage theory of psychosocial development proposes that people must resolve psychosocial conflicts at each stage of the lifespan. The distractors are Piaget's stages (3.4.A.1) and claims the framework does not make."),
 ("generativity and stagnation",
  "EK 3.6.A.6 lists eight conflicts, and this is the seventh. The distractors are Piagetian processes (2.2.A.2 / 3.4.A.1), the serial position effect (2.4.A.5), and the creativity contrast (2.2.A.8) -- all real course content that is not a psychosocial conflict."),
 ("trust and mistrust; autonomy and shame and doubt; initiative and guilt; industry and inferiority",
  "EK 3.6.A.6 lists the eight in this order and attaches no ages to any of them. The third distractor gives the LAST four in correct order, which is the tempting wrong answer for a student who knows the list but not where it starts."),
 ("throughout the lifespan, and sociocultural differences exist in what counts as one",
  "EK 3.6.A.7 makes both claims: ACEs affect relationships people form throughout the lifespan, AND sociocultural differences exist in what is considered an ACE and how ACEs affect outcomes. The key keeps both, since dropping the second would present the category as culturally fixed."),
 ("achievement, diffusion, foreclosure, and moratorium",
  "EK 3.6.A.8 names these four processes through which adolescents develop a sense of identity. The distractors are the first four psychosocial conflicts (3.6.A.6), the attachment styles (3.6.A.3), and four of the ecological systems (3.6.A.1) -- so a student must know which of this objective's several four-item lists is being asked for."),
]

psych_check.check(p3_6, CLAIMS, per_topic=30, n_choices=4)
