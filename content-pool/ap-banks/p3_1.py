# AP PSYCHOLOGY 3.1 Themes and Methods in Developmental Psychology — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objectives 3.1.A (how enduring themes inform developmental
# psychology) and 3.1.B (how cross-sectional and longitudinal research designs
# inform understanding).
#
# Essential knowledge relied on: 3.1.A.1 developmental psychology is concerned
# with chronological order of development and/or thematic issues across the
# lifespan, and the thematic issues named are STABILITY AND CHANGE, NATURE AND
# NURTURE, and CONTINUOUS AND DISCONTINUOUS STAGES of development. Objective
# 3.1.B is stated in the CED without accompanying essential-knowledge bullets, so
# every item on cross-sectional and longitudinal design below is keyed to what
# those designs are and what they can and cannot show -- the content of science
# practice 2.A, which the CED lists as this topic's suggested skill -- rather than
# to a claim the framework does not make.
#
# This topic is half themes and half methods, so the module is too: items 1-14
# cover the three thematic issues, items 15-30 the two designs and the design
# reasoning that goes with them. The cohort effect and attrition are treated as
# properties of the two designs rather than as free-standing terms, because that
# is how the CED frames the objective.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_1.py.
TOPIC = ("3.1", "Themes and Methods in Developmental Psychology", 3)
QUESTIONS = [
 dict(q="Developmental psychology is concerned with", choices=[
   "the chronological order of development and thematic issues across the lifespan",
   "childhood only, since development is complete by adolescence",
   "the treatment of psychological disorders across the lifespan",
   "the biological structures of the nervous system"], ans=0,
   why="EK 3.1.A.1 states that developmental psychology is concerned with both chronological order of development and thematic issues in development across the lifespan."),
 dict(q="Which set correctly names the thematic issues of interest to developmental psychologists in the AP Psychology framework?", choices=[
   "stability and change; nature and nurture; continuous and discontinuous development",
   "encoding, storage, and retrieval",
   "sensation, perception, and cognition",
   "reliability, validity, and standardization"], ans=0,
   why="EK 3.1.A.1 names exactly these three thematic issues; the other options list the memory stages from Topic 2.3, processes from Units 1 and 2, and the psychometric principles from EK 2.8.B.2."),
 dict(q="The stability-and-change theme asks whether", choices=[
   "a characteristic present early in life persists or is transformed later",
   "a characteristic is inherited or acquired through experience",
   "development proceeds in gradual increments or in distinct stages",
   "development can be studied without harming participants"], ans=0,
   why="EK 3.1.A.1 names stability and change among the thematic issues; it concerns whether traits endure across the lifespan or change."),
 dict(q="The nature-and-nurture theme in developmental psychology asks whether", choices=[
   "a characteristic arises from inherited predisposition or from experience",
   "a characteristic present in infancy persists into adulthood",
   "development proceeds in gradual increments or in distinct stages",
   "one age group can be compared with another at a single point in time"], ans=0,
   why="EK 3.1.A.1 names nature and nurture among the thematic issues, and EK 1.1.A.1 supplies its content: heredity and environmental factors interacting to shape behavior."),
 dict(q="The continuous-versus-discontinuous theme asks whether", choices=[
   "development proceeds as gradual accumulation or through a series of distinct stages",
   "a trait remains constant or changes over the lifespan",
   "a trait is inherited or learned",
   "a study follows one group over time or compares groups at one time"], ans=0,
   why="EK 3.1.A.1 names continuous and discontinuous stages of development among the thematic issues; the question is whether change is incremental or stage-like."),
 dict(q="A theorist who claims that children pass through a fixed sequence of qualitatively different stages is taking a position on", choices=[
   "the continuous-versus-discontinuous theme",
   "the stability-and-change theme",
   "the nature-and-nurture theme",
   "the reliability of developmental measures"], ans=0,
   why="EK 3.1.A.1's continuous/discontinuous theme is precisely the question of whether development is stage-like; a fixed sequence of qualitatively different stages is the discontinuous answer."),
 dict(q="A researcher reports that shy infants tend to become shy adults. This finding speaks most directly to", choices=[
   "the stability-and-change theme",
   "the continuous-versus-discontinuous theme",
   "the nature-and-nurture theme",
   "the ethics of developmental research"], ans=0,
   why="EK 3.1.A.1's stability and change theme asks whether an early characteristic persists; persistence of temperament from infancy to adulthood is a claim about stability."),
 dict(q="A researcher finds that a language difficulty appears only in children who both have a family history of it and grew up with little verbal interaction. This finding speaks most directly to", choices=[
   "the nature-and-nurture theme",
   "the stability-and-change theme",
   "the continuous-versus-discontinuous theme",
   "the standardization of language assessments"], ans=0,
   why="EK 3.1.A.1's nature and nurture theme, together with EK 1.1.A.1's interaction claim, covers an outcome that requires both an inherited predisposition and a particular environment."),
 dict(q="A theorist who describes vocabulary growth as a steady accumulation with no sharp transitions is taking which position?", choices=[
   "development is continuous",
   "development is discontinuous",
   "development is entirely determined by heredity",
   "early traits are unstable"], ans=0,
   why="EK 3.1.A.1's continuous/discontinuous theme: gradual accumulation without qualitative transitions is the continuous position, and stages would be the discontinuous one."),
 dict(q="Which question is a developmental psychologist asking when she studies whether a personality trait measured at age 5 predicts the same trait at age 40?", choices=[
   "a stability-and-change question",
   "a continuous-versus-discontinuous question",
   "a nature-and-nurture question",
   "a question about test-retest reliability of the trait measure"], ans=0,
   why="EK 3.1.A.1's stability and change theme concerns whether a characteristic endures across the lifespan, which is exactly what a 35-year prediction tests."),
 dict(q="Two developmental psychologists disagree about whether moral reasoning improves gradually or in identifiable jumps. Their disagreement is best described as being about", choices=[
   "whether development is continuous or discontinuous",
   "whether development is stable or changing",
   "whether development is shaped by nature or by nurture",
   "whether their measure is valid"], ans=0,
   why="EK 3.1.A.1's continuous/discontinuous theme is the framework's name for exactly this disagreement about the shape of developmental change."),
 dict(q="Which of the following is NOT one of the thematic issues named in the AP Psychology framework's account of developmental psychology?", choices=[
   "convergent and divergent thinking",
   "stability and change",
   "nature and nurture",
   "continuous and discontinuous development"], ans=0,
   why="EK 3.1.A.1 names three themes; convergent and divergent thinking belongs to EK 2.2.A.8's account of creativity in Unit 2."),
 dict(q="Saying that developmental psychology studies the \"chronological order\" of development means that it examines", choices=[
   "the sequence in which developments occur across the lifespan",
   "the exact age at which every person reaches each milestone",
   "only those changes that occur before adulthood",
   "the calendar year in which a person was born"], ans=0,
   why="EK 3.1.A.1 pairs chronological order with thematic issues as the two concerns of developmental psychology; order is a claim about sequence, and EK 3.2.B.1 adds explicitly that the timing of development can vary."),
 dict(q="Development across the lifespan, as the AP Psychology framework uses the phrase, includes", choices=[
   "changes occurring from before birth through late adulthood",
   "changes occurring only during infancy and childhood",
   "changes occurring only after a person reaches adulthood",
   "changes that can be observed in a single laboratory session"], ans=0,
   why="EK 3.1.A.1 states that developmental psychology's concerns run across the lifespan, and Topic 3.2's objectives cover prenatal development through adulthood."),
 dict(q="A cross-sectional study of development", choices=[
   "compares people of different ages at a single point in time",
   "follows the same people repeatedly over many years",
   "studies one individual in depth over a lifetime",
   "randomly assigns participants to different ages"], ans=0,
   why="Objective 3.1.B names cross-sectional and longitudinal designs as the methods of developmental psychology; the cross-sectional design compares different age groups measured at once."),
 dict(q="A longitudinal study of development", choices=[
   "follows the same participants over an extended period",
   "compares different age groups measured on the same day",
   "manipulates the age of the participants",
   "observes participants without measuring anything"], ans=0,
   why="Objective 3.1.B names longitudinal design as the other developmental method; it re-measures the same people across time."),
 dict(q="Which statement correctly distinguishes cross-sectional from longitudinal designs?", choices=[
   "a cross-sectional design compares different people of different ages at once; a longitudinal design re-measures the same people over time",
   "a longitudinal design compares different people of different ages at once; a cross-sectional design re-measures the same people over time",
   "cross-sectional designs are experiments and longitudinal designs are not",
   "the two designs differ only in how many participants they include"], ans=0,
   why="Objective 3.1.B's two designs differ in whether the same people are followed or different people are compared; the first distractor is that difference reversed, and neither design involves manipulation."),
 dict(q="A researcher tests 20-year-olds, 50-year-olds, and 80-year-olds on a reasoning task in the same week. This design is", choices=[
   "cross-sectional",
   "longitudinal",
   "experimental",
   "a case study"], ans=0,
   why="Different age groups measured at one point in time is the cross-sectional design named in objective 3.1.B; no one is followed over time and nothing is manipulated."),
 dict(q="A researcher tests the same 200 people at ages 20, 50, and 80. This design is", choices=[
   "longitudinal",
   "cross-sectional",
   "experimental",
   "naturalistic observation"], ans=0,
   why="Re-measuring the same participants across an extended period is the longitudinal design named in objective 3.1.B."),
 dict(q="The main practical advantage of a cross-sectional design over a longitudinal design is that it", choices=[
   "produces results in far less time",
   "eliminates the need for a comparison of any kind",
   "allows the researcher to assign participants to age groups",
   "guarantees that the groups differ only in age"], ans=0,
   why="A cross-sectional study collects all its data at one time rather than waiting years, which is its practical advantage; the last option names precisely what it cannot guarantee."),
 dict(q="A cross-sectional study finds that 80-year-olds score lower on a vocabulary test than 20-year-olds. Before concluding that vocabulary declines with age, a careful reader should note that", choices=[
   "the two groups grew up in different eras and may differ in schooling as well as in age",
   "vocabulary cannot be measured in older adults",
   "the study should have assigned participants to age groups at random",
   "the study has no dependent variable"], ans=0,
   why="Different age groups in a cross-sectional design are also different birth cohorts, so era-linked differences such as schooling are confounded with age; age cannot be randomly assigned, which is why the third option describes something impossible."),
 dict(q="The main weakness of a longitudinal design is that", choices=[
   "it takes a long time and participants may drop out along the way",
   "it cannot measure the same people more than once",
   "it confounds age with the era in which participants grew up",
   "it requires random assignment to age groups"], ans=0,
   why="Following the same people for years is slow and loses participants; confounding age with birth era is the cross-sectional weakness, not the longitudinal one."),
 dict(q="If the participants who drop out of a long-term study differ systematically from those who remain, the results may be misleading because", choices=[
   "the surviving sample is no longer representative of the group that started",
   "the study can no longer have an independent variable",
   "the remaining participants will forget the earlier sessions",
   "the study automatically becomes an experiment"], ans=0,
   why="Selective dropout changes who is left in the sample, so later measurements describe a different and possibly healthier or more motivated group than the one originally recruited."),
 dict(q="Neither a cross-sectional nor a longitudinal study can establish that aging CAUSES a change, because", choices=[
   "age cannot be manipulated or randomly assigned",
   "neither design measures any variable",
   "both designs use samples that are too small",
   "both designs are conducted outside the laboratory"], ans=0,
   why="Science practice 2: a causal conclusion requires a manipulated, randomly assigned independent variable, and no researcher can assign a participant an age."),
 dict(q="A researcher wants to know whether a reading skill develops in the same order for every child. The most appropriate design is", choices=[
   "a longitudinal study following the same children as the skill emerges",
   "a cross-sectional comparison of children of different ages on one day",
   "an experiment assigning children to develop the skill in different orders",
   "a survey of adults recalling how they learned to read"], ans=0,
   why="A claim about the ORDER in which developments occur within a person requires following individuals over time, which is what objective 3.1.B's longitudinal design does; a single-day comparison cannot observe a sequence within anyone."),
 dict(q="Which is the best operational definition of \"motor skill development\" for a developmental study?", choices=[
   "the number of seconds a child can balance on one foot, measured at each visit",
   "how physically capable the child appears to the researcher",
   "the child's overall level of physical development",
   "whether the child enjoys physical activity"], ans=0,
   why="An operational definition states a specific, repeatable measurement procedure; a timed balance measure is countable, while the alternatives restate the construct or measure enjoyment instead."),
 dict(q="A study recruits participants only from families who volunteer for a 20-year commitment. The strongest limitation is that", choices=[
   "the sample may differ systematically from families who would not volunteer",
   "the study cannot have a dependent variable",
   "longitudinal designs cannot measure change",
   "the results will apply only to the researchers"], ans=0,
   why="Self-selected volunteers for a long commitment may differ in stability, resources, and motivation, so the sample may not represent the wider population -- the generalizability question the exam's Article Analysis Question asks directly."),
 dict(q="A researcher plans a study of infants' responses to novel objects. Which step is most necessary for the study to meet ethical standards?", choices=[
   "obtaining informed consent from each infant's parent or guardian and ending a session if the infant becomes distressed",
   "concealing the study's purpose from the parents permanently",
   "guaranteeing in advance that the findings will be statistically significant",
   "recruiting only infants whose parents are also researchers"], ans=0,
   why="Science practice 2.D: infants cannot consent for themselves, so consent comes from a guardian, and protection from harm requires stopping a session that distresses the participant."),
 dict(q="A newspaper reports that a longitudinal study found that children who read more at age 6 had larger vocabularies at age 16, and concludes that reading builds vocabulary. The most accurate response is that", choices=[
   "the design shows the relationship holds over time but still does not establish that reading is the cause",
   "the design is an experiment and therefore does establish the cause",
   "no relationship between the two measures has been shown",
   "longitudinal designs cannot measure the same trait twice"], ans=0,
   why="A longitudinal design establishes temporal order but manipulates nothing, so a third variable such as home environment remains a live explanation; measuring earlier and later is not the same as assigning a condition."),
 dict(q="A student claims: \"Development is best understood as a series of distinct stages.\" Which piece of evidence would most directly challenge that claim?", choices=[
   "a longitudinal study showing that a skill improves in small steady increments with no identifiable transitions",
   "a cross-sectional study showing that older participants score higher than younger ones",
   "evidence that a trait measured in infancy predicts the same trait in adulthood",
   "evidence that both heredity and environment contribute to the skill"], ans=0,
   why="Science practice 4.B: the claim is the discontinuous side of EK 3.1.A.1's continuous/discontinuous theme, so the evidence that bears on it is evidence about the SHAPE of change; the other options address the other two themes instead."),
]
