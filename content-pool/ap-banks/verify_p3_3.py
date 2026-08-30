"""Key audit for AP PSYCHOLOGY 3.3 Gender and Sexual Orientation.

THIS TOPIC HAS NO ESSENTIAL KNOWLEDGE IN THE CED, and that fact governs every
claim below, so it is stated first.

Topic 3.3 as printed in the Course and Exam Description consists of exactly one
line of required course content: learning objective 3.3.A, "Describe how sex and
gender influence socialization and other aspects of development." There are no
EK bullets beneath it. This was verified by extracting Course Framework page 77
from the CED PDF in isolation rather than reading it out of a longer text dump,
because a missing column in an extraction would look identical to a genuinely
empty one. The UNIT AT A GLANCE table corroborates it: 3.3 is allotted ONE
instructional period, the fewest of any topic in the course, and carries a single
suggested skill, 2.C.

Therefore NO claim in this file cites an EK number for this topic, because there
are none to cite. Each claim says what it actually rests on:

  * "objective 3.3.A" -- the objective's own wording;
  * "standard course definition" -- the meaning the term carries in an
    introductory psychology course, where the CED supplies the term but not a
    definition;
  * "science practice 2.C" (or 2.B, 2.D) -- design reasoning, which is what the
    CED attaches to this topic and what its own sample activity for 3.3 asks for:
    take a published gender-roles study, identify its research method, evaluate
    its ethics, and design a follow-up.

A fabricated EK citation would be worse here than no citation, since a reader
checking it would find nothing. That is the whole reason for this note.

Two boundaries kept deliberately:

1. Gender identity and sexual orientation ARE named in the framework, but in
   EK 3.6.A.8, as identities adolescents develop. Identity FORMATION therefore
   belongs to Topic 3.6. This module defines the two constructs and separates
   them from each other (items 4-6) and otherwise stays on socialization and on
   method.
2. No item asserts a contested empirical claim about any group, and none asks a
   student to explain a difference between groups. With no essential knowledge
   printed, the framework supplies no basis for either, and inventing one would
   be exactly the kind of unchecked assertion this verification file exists to
   prevent. Item 30 makes the limits of an over-strong inference the answer.

Weighting follows the CED's own emphasis: items 1-14 are terminology and the
objective's scope, items 15-30 are research design, methodology, and ethics.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_3

CLAIMS = [
 ("biological characteristics",
  "Standard course definition: sex refers to biological characteristics, gender to socially constructed roles and expectations. The CED uses both words in objective 3.3.A without defining either, so the definition is the discipline's rather than a quotation."),
 ("socially constructed roles, behaviors, and expectations",
  "Standard course definition of gender. The social content is what makes gender capable of influencing SOCIALIZATION, which is what objective 3.3.A asks about -- a purely biological reading of the term would make the objective incoherent."),
 ("sex refers to biological characteristics; gender refers to socially constructed roles",
  "The sex/gender distinction stated head-on, with the reversal as the first distractor. The third distractor -- that the terms are interchangeable -- is ruled out by objective 3.3.A itself, which names both."),
 ("own internal sense of their gender",
  "Standard course definition. The framework names gender identity in EK 3.6.A.8 among the identities adolescents develop but does not define it; identity FORMATION is Topic 3.6's subject, and this item only fixes the construct."),
 ("enduring pattern of romantic or sexual attraction",
  "Standard course definition. EK 3.6.A.8 lists sexual orientation separately from gender identity, so the framework treats them as different constructs; this item states what the difference is."),
 ("gender identity is a person's sense of their own gender; sexual orientation is their pattern of attraction",
  "One construct concerns the self, the other attraction to others. EK 3.6.A.8 lists them separately, which is the framework's own warrant for treating them as distinct. The first distractor is the definition reversed -- the specific confusion this item exists to catch."),
 ("society's expectations about how people of a given gender should behave",
  "Standard course definition. Gender roles are the social-expectation construct, which is the mechanism by which gender can influence socialization under objective 3.3.A."),
 ("learns the expectations, norms, and behaviors of their society",
  "Objective 3.3.A names socialization as what sex and gender influence. Socialization is the process of acquiring a society's norms; the fourth distractor is conformity, a Unit 4 topic, which is a different construct that shares a social flavour."),
 ("children learn the gender-related expectations of their culture",
  "Standard course definition, and the specific case objective 3.3.A points at: socialization carrying gender-related content."),
 ("gender socialization through differential adult response",
  "Objective 3.3.A concerns how gender influences socialization. Adults responding differently according to a child's gender is a concrete transmission mechanism. The scenario is written so that the differential response, not the toys' existence, is what is being asked about."),
 ("traits traditionally considered masculine and traits traditionally considered feminine",
  "Standard course definition of androgyny: a combination of traditionally masculine and traditionally feminine characteristics in one person. It is a description of gender-role traits, which is what rules out the 'biological condition' distractor."),
 ("differ across cultures and change over historical time",
  "A reasoning item rather than a definition: anything transmitted by socialization varies with the society transmitting it, so cross-cultural and historical variation is the observable prediction a social account makes and a purely biological one does not. This sets up item 30, which then tests the LIMIT of that inference."),
 ("socialization and other aspects of development",
  "Learning objective 3.3.A, verbatim. The distractors are the subjects of Topics 1.2-1.4, 2.8, and 2.5, so the item fixes this topic's scope against three real neighbours."),
 ("culture's gender expectations shape the way children are raised",
  "Objective 3.3.A's scope. The distractors belong to Topic 1.4 (the cerebellum), Topic 2.7 (interference), and EK 2.8.B.2.iii (split-half reliability) -- all real course content outside this topic."),
 ("naturalistic observation",
  "Science practice 2.C. Recording behavior as it occurs with no intervention is naturalistic observation; nothing is manipulated, one teacher is not the unit, and no one is followed over time."),
 ("cannot be manipulated or randomly assigned",
  "Science practice 2: an experiment requires a manipulated, randomly assigned independent variable, and a participant characteristic cannot be assigned. This is why the CED gives Topic 3.3 the NON-experimental skill (2.C) as its only suggested skill -- the constraint is substantive, not incidental."),
 ("relationship exists between the two variables, with the cause undetermined",
  "Science practice 2.C. Number of siblings was not assigned, so both causal directions and third-variable explanations stay open. The item offers BOTH causal directions as distractors so that rejecting one is not enough."),
 ("gender the adults are told the infant is",
  "Science practice 2.B: the independent variable is the manipulated, randomly assigned condition -- the label supplied to the adults. The adults' OWN genders appear as a distractor because they are a participant characteristic that cannot be assigned, which is the distinction item 20 develops."),
 ("infant's actual behavior, rather than the label, could explain",
  "A confounding variable changes alongside the manipulation and offers a rival explanation. Holding the video constant leaves the supplied label as the only difference between conditions."),
 ("label given to the adults, not any participant's own gender",
  "This is the item that resolves the tension set up by item 16. Gender cannot be assigned, but INFORMATION ABOUT gender can be, so an experimental design is available after all -- by manipulating what observers are told rather than what participants are. It is the standard route into experimental work on an otherwise unassignable variable."),
 ("answer in the way they believe is socially expected",
  "A validity threat specific to self-report on a socially sensitive subject. The remaining options misdescribe surveys -- they collect from many people, they do not require random assignment, and they can be scored consistently."),
 ("generalizability, since one community's expectations may not represent others",
  "Generalizability concerns whether the sample resembles the population the claim covers. Because gender expectations are transmitted by particular cultures (item 12's reasoning), a single-community sample constrains the claim especially sharply. The distractors name reliability, random assignment, and confounding -- three real design concepts that do not fit this criticism."),
 ("observation, survey, and correlational designs rather than experiments",
  "The CED lists 2.C as this topic's only suggested skill. That fits a subject whose central variables are participant characteristics: the evidence is largely non-experimental by necessity. The third distractor inverts the relationship between design and causal inference and is false."),
 ("observers who knew the children's genders could be influenced by their own expectations",
  "Observer expectancy: when the person recording data knows the grouping, their expectations can shape what they record, and keeping observers unaware is the standard safeguard. The third distractor proposes randomly assigning children to genders, which is impossible -- the same impossibility item 16 establishes."),
 ("number of activities from a fixed list",
  "An operational definition states a countable procedure. A count from a fixed list is measurable; 'seems open-minded', 'general attitude', and having a favourite toy restate the construct or measure something else."),
 ("informed consent, keeping responses confidential, and allowing participants to decline",
  "Science practice 2.D. With personal questions, confidentiality and the right to decline or withdraw are the applicable protections. The second distractor -- reporting answers to the school -- is an active violation, not merely an omission, which is why it is the tempting wrong answer for a student who reads 'safeguard' as 'oversight'."),
 ("recruiting language selects a sample unlike the wider population",
  "How participants are recruited determines who is in the sample. Advertising for parents interested in a named position selects for families who hold it, so the sample is systematically unlike the population the conclusions would cover."),
 ("show that the two go together but cannot establish which causes which",
  "Science practice 2.C. Without manipulation and random assignment, both the direction of influence and third variables remain open. The second distractor overcorrects -- correlational studies do detect relationships -- which is the error a student makes after being taught only 'correlation is not causation'."),
 ("each method has different strengths and limitations",
  "Observation records behavior but not reasons; survey accesses self-report but invites socially expected answering (item 21). Neither dominates, so a discrepancy between them is informative about method as well as about the question -- which is what science practice 2.C asks a student to be able to say."),
 ("shows that experience matters but does not by itself rule out other influences",
  "Science practice 4.B. Cross-cultural variation is evidence that environment contributes -- item 12's prediction confirmed -- but 'entirely learned' is a stronger claim than the observation supports. EK 1.1.A.1's interaction of heredity and environment is the framework's standing caution against either extreme, and the key stops exactly where the evidence does."),
]

psych_check.check(p3_3, CLAIMS, per_topic=30, n_choices=4)
