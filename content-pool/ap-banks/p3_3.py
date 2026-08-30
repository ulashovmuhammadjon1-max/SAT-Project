# AP PSYCHOLOGY 3.3 Gender and Sexual Orientation — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
#
# READ THIS BEFORE EDITING. In the CED, Topic 3.3 consists of learning objective
# 3.3.A -- "Describe how sex and gender influence socialization and other aspects
# of development" -- and NOTHING ELSE. There are no essential-knowledge bullets
# printed beneath it (verified by extracting Course Framework page 77 from the
# CED PDF on its own). It is the shortest topic in the course: the UNIT AT A
# GLANCE table gives it ONE instructional period, and its single suggested skill
# is 2.C, evaluating the appropriate use of research design elements in
# non-experimental methodologies. The CED's own sample instructional activity for
# this topic asks students to take a published gender-roles study and identify
# its research method, evaluate its ethics, summarize its results, and design a
# follow-up.
#
# Two consequences follow, and both shape this module:
#
# 1. No key here can cite an EK number, because there are none. Definitional
#    items are keyed to the standard meaning the terms carry in an introductory
#    psychology course, and verify_p3_3.py says so explicitly for each one rather
#    than inventing a citation.
# 2. The weighting follows the CED's own: roughly half the module is research
#    design, methodology, and ethics -- the topic's stated skill -- rather than
#    terminology.
#
# The related term list the framework does supply appears in EK 3.6.A.8, which
# names gender identity and sexual orientation among the identities adolescents
# develop. That EK is Topic 3.6's, so identity FORMATION is left to 3.6 and this
# module stays on socialization and on method.
#
# Items state only definitions and design reasoning. No item asserts a contested
# empirical claim about any group, and no item asks a student to explain a
# difference between groups -- the framework provides no basis for either.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
TOPIC = ("3.3", "Gender and Sexual Orientation", 3)
QUESTIONS = [
 dict(q="In psychology, the term sex most commonly refers to", choices=[
   "a person's biological characteristics",
   "the roles and expectations a society attaches to being a man or a woman",
   "a person's internal sense of who they are",
   "a person's pattern of attraction to others"], ans=0,
   why="Introductory psychology distinguishes sex, the biological characteristics, from gender, the socially constructed roles and expectations; the remaining options define gender identity and sexual orientation."),
 dict(q="In psychology, the term gender most commonly refers to", choices=[
   "the socially constructed roles, behaviors, and expectations associated with being a man or a woman",
   "a person's biological characteristics",
   "the age at which puberty begins",
   "the number of children in a family"], ans=0,
   why="Gender names the social dimension -- roles, behaviors, and expectations -- which is what makes it distinguishable from sex and what allows learning objective 3.3.A to ask how it influences socialization."),
 dict(q="Which statement correctly distinguishes sex from gender as psychologists ordinarily use the terms?", choices=[
   "sex refers to biological characteristics; gender refers to socially constructed roles and expectations",
   "gender refers to biological characteristics; sex refers to socially constructed roles and expectations",
   "the two terms are interchangeable in psychological research",
   "sex applies to children and gender applies to adults"], ans=0,
   why="The distinction is between the biological and the social; the first distractor reverses it, and the third denies a distinction that learning objective 3.3.A depends on by naming both."),
 dict(q="Gender identity refers to", choices=[
   "a person's own internal sense of their gender",
   "the biological characteristics recorded at birth",
   "a society's expectations about how people should behave",
   "a person's pattern of romantic or sexual attraction"], ans=0,
   why="Gender identity is the person's own sense of their gender; the framework names it among the identities adolescents develop in EK 3.6.A.8, and it is distinct from both social expectations and attraction."),
 dict(q="Sexual orientation refers to", choices=[
   "a person's enduring pattern of romantic or sexual attraction to others",
   "a person's internal sense of their own gender",
   "the biological characteristics recorded at birth",
   "the roles a society expects a person to fill"], ans=0,
   why="Sexual orientation concerns the pattern of attraction, which is what distinguishes it from gender identity; EK 3.6.A.8 lists the two separately among developing identities, so the framework treats them as different constructs."),
 dict(q="Which statement correctly distinguishes gender identity from sexual orientation?", choices=[
   "gender identity is a person's sense of their own gender; sexual orientation is their pattern of attraction to others",
   "sexual orientation is a person's sense of their own gender; gender identity is their pattern of attraction to others",
   "the two terms describe the same thing at different ages",
   "gender identity applies only to adolescents and sexual orientation only to adults"], ans=0,
   why="One concerns the self and the other concerns attraction to others; EK 3.6.A.8 lists them as separate identities, and the first distractor is the definition reversed."),
 dict(q="Gender roles are best described as", choices=[
   "a society's expectations about how people of a given gender should behave",
   "the biological differences between males and females",
   "an individual's private sense of their own gender",
   "the stages through which physical maturation proceeds"], ans=0,
   why="Gender roles are social expectations rather than biological facts or private senses of self, which is why they are the mechanism through which gender can influence socialization in learning objective 3.3.A."),
 dict(q="Socialization, as the term is used in learning objective 3.3.A, refers to", choices=[
   "the process by which a person learns the expectations, norms, and behaviors of their society",
   "the amount of time a person spends with friends",
   "the biological maturation of the nervous system",
   "the tendency to conform to a group in a laboratory experiment"], ans=0,
   why="Learning objective 3.3.A asks how sex and gender influence socialization; socialization is the process of learning a society's norms and expectations, which is what makes gender roles capable of influencing it."),
 dict(q="Gender socialization refers to", choices=[
   "the process through which children learn the gender-related expectations of their culture",
   "the biological onset of puberty",
   "a child's ability to identify which objects are heavier",
   "a decline in gender differences with age"], ans=0,
   why="Gender socialization is the specific case of socialization that transmits gender-related expectations, and it is the process learning objective 3.3.A points at."),
 dict(q="A preschool offers a toy kitchen and a toy tool bench, and adults praise children more warmly when they choose the toy typically associated with their gender. This situation illustrates", choices=[
   "gender socialization through differential adult response",
   "the biological determination of toy preference",
   "the development of object permanence",
   "the operation of a critical period for language"], ans=0,
   why="Learning objective 3.3.A concerns how gender influences socialization; adults responding differently according to the child's gender is a mechanism through which cultural expectations are transmitted."),
 dict(q="Androgyny, in psychology, refers to", choices=[
   "possessing both traits traditionally considered masculine and traits traditionally considered feminine",
   "having no gender identity at all",
   "a biological condition present from birth",
   "an inability to identify one's own emotions"], ans=0,
   why="Androgyny names a combination of traditionally masculine and traditionally feminine characteristics in one person, which is a description of gender-role traits rather than of biology."),
 dict(q="Because gender roles are learned expectations rather than biological facts, psychologists predict that they will", choices=[
   "differ across cultures and change over historical time",
   "be identical in every society ever studied",
   "be fixed at birth and unchangeable",
   "have no observable effect on behavior"], ans=0,
   why="Anything transmitted through socialization varies with the society doing the transmitting, which is the observable consequence that distinguishes a social account of gender roles from a biological one."),
 dict(q="Learning objective 3.3.A asks students to describe how sex and gender influence", choices=[
   "socialization and other aspects of development",
   "the structure of the nervous system",
   "the reliability of psychological tests",
   "the stages of memory storage"], ans=0,
   why="This is the objective's own wording: describe how sex and gender influence socialization and other aspects of development."),
 dict(q="Which question falls within the scope of Topic 3.3 as the CED states it?", choices=[
   "How do a culture's gender expectations shape the way children are raised?",
   "Which brain structure controls balance?",
   "What is the difference between proactive and retroactive interference?",
   "How is split-half reliability calculated?"], ans=0,
   why="Learning objective 3.3.A concerns the influence of sex and gender on socialization and development; the distractors belong to Topics 1.4, 2.7, and 2.8 respectively."),
 dict(q="A researcher records how often teachers call on students of different genders during class, without intervening in any way. This design is", choices=[
   "naturalistic observation",
   "an experiment",
   "a case study of one teacher",
   "a longitudinal study"], ans=0,
   why="Science practice 2.C: recording behavior as it occurs without intervening is naturalistic observation; nothing is manipulated and no one is followed across time."),
 dict(q="Why can a researcher not conduct a true experiment on the effects of a participant's own gender?", choices=[
   "a participant's gender cannot be manipulated or randomly assigned",
   "gender cannot be measured in any way",
   "experiments require at least three conditions",
   "such research is uninteresting to psychologists"], ans=0,
   why="An experiment requires a manipulated, randomly assigned independent variable; a participant characteristic cannot be assigned, which is exactly why the CED attaches non-experimental methodology (2.C) to this topic."),
 dict(q="A study finds that children in a particular school who have more older siblings hold less rigid views about gender roles. The strongest supported conclusion is that", choices=[
   "a relationship exists between the two variables, with the cause undetermined",
   "having older siblings causes less rigid views",
   "less rigid views cause parents to have more children",
   "the two variables are unrelated"], ans=0,
   why="Nothing was manipulated and no one was assigned a number of siblings, so the design is correlational; both proposed causal readings, and a third-variable explanation, remain open."),
 dict(q="A researcher wants to know whether adults describe the same infant's behavior differently depending on what they are told the infant's gender is. She randomly assigns adults to be told one gender or the other and shows all of them the same video. The independent variable is", choices=[
   "the gender the adults are told the infant is",
   "how the adults describe the infant's behavior",
   "the video, which is identical for all participants",
   "the adults' own genders"], ans=0,
   why="Science practice 2.B: the independent variable is the manipulated, randomly assigned condition, which here is the label supplied to the adults; the adults' own genders are a participant characteristic that cannot be assigned."),
 dict(q="In that study, showing every participant the SAME video is essential because", choices=[
   "otherwise the infant's actual behavior, rather than the label, could explain any difference in descriptions",
   "otherwise the study would have no dependent variable",
   "it makes the sample representative of all adults",
   "it converts the experiment into a correlational study"], ans=0,
   why="A variable that changes alongside the manipulation and offers a rival explanation is a confounding variable; holding the video constant leaves the supplied label as the only thing that differs."),
 dict(q="Why is the study described above an experiment even though gender cannot be assigned to a participant?", choices=[
   "what is manipulated is the label given to the adults, not any participant's own gender",
   "the researcher measured more than one variable",
   "the participants were observed in a natural setting",
   "the study followed participants over several years"], ans=0,
   why="The manipulated variable is the information supplied to observers, which can be randomly assigned; this is the standard way an otherwise unassignable topic is brought into an experimental design."),
 dict(q="A survey asks respondents to report their agreement with statements about gender roles. A limitation specific to this method is that", choices=[
   "respondents may answer in the way they believe is socially expected rather than truthfully",
   "surveys cannot collect data from more than one person",
   "surveys always require random assignment",
   "surveys cannot be scored consistently"], ans=0,
   why="Self-report on a socially sensitive topic invites answers shaped by perceived expectations, which is a validity threat specific to survey methods rather than to design in general."),
 dict(q="Researchers studying gender roles in a single community and generalizing to all cultures would be criticized most directly on grounds of", choices=[
   "generalizability, since one community's expectations may not represent others",
   "reliability, since the measure would give different results each time",
   "random assignment, since participants chose their own community",
   "confounding, since two variables were manipulated at once"], ans=0,
   why="Generalizability concerns whether the sample resembles the population a claim covers, and gender expectations are transmitted by particular cultures, so a single-community sample constrains the claim severely."),
 dict(q="The CED's suggested skill for Topic 3.3 is evaluating research design elements in non-experimental methodologies. This is appropriate because", choices=[
   "much of the evidence in this area comes from observation, survey, and correlational designs rather than experiments",
   "experiments have never been conducted in psychology",
   "non-experimental designs establish causation more reliably than experiments do",
   "the topic contains no research findings at all"], ans=0,
   why="The CED lists 2.C as this topic's only suggested skill, which fits a subject where the central variables are participant characteristics that cannot be manipulated."),
 dict(q="A published study measured children's play behavior by having observers who knew each child's gender rate how \"typical\" the play was. The clearest methodological weakness is that", choices=[
   "observers who knew the children's genders could be influenced by their own expectations",
   "play behavior cannot be observed at all",
   "the study should have randomly assigned children to genders",
   "the study needed a longitudinal design to measure anything"], ans=0,
   why="Observer expectancy is a threat whenever the person recording the data knows the condition; keeping observers unaware of the grouping is the standard safeguard, and the third option proposes something impossible."),
 dict(q="Which is the best operational definition of \"gender-role flexibility\" for a study of children?", choices=[
   "the number of activities from a fixed list that a child says either boys or girls could enjoy",
   "how open-minded the child seems to the researcher",
   "the child's general attitude toward gender",
   "whether the child has a favorite toy"], ans=0,
   why="An operational definition states a countable measurement procedure; a count from a fixed list is measurable, while the alternatives restate the construct or measure something else."),
 dict(q="A researcher plans to interview adolescents about gender identity and sexual orientation. Which safeguard is most necessary for the study to meet ethical standards?", choices=[
   "obtaining informed consent, keeping responses confidential, and allowing participants to decline any question",
   "reporting each participant's answers to their school",
   "requiring every participant to answer every question",
   "guaranteeing in advance that the results will be publishable"], ans=0,
   why="Science practice 2.D: confidentiality and the right to decline or withdraw are the applicable protections when the questions are personal, and disclosing individual answers to a third party would violate them."),
 dict(q="A study of gender socialization is conducted entirely with families who volunteered after seeing an advertisement seeking \"parents interested in gender equality.\" The clearest limitation is that", choices=[
   "the recruiting language selects a sample unlike the wider population of families",
   "volunteer samples cannot be measured reliably",
   "the study cannot have an operational definition",
   "the study automatically becomes an experiment"], ans=0,
   why="How participants are recruited determines who is in the sample; wording that names the topic and a position on it selects for families who already hold that position, which limits generalizability."),
 dict(q="A journalist writes that a correlational study \"proves\" that a parenting practice causes children's attitudes about gender. The most accurate correction is that", choices=[
   "a correlational study can show that the two go together but cannot establish which causes which",
   "correlational studies cannot detect relationships at all",
   "the journalist should have described the study as an experiment",
   "attitudes about gender cannot be measured"], ans=0,
   why="Without manipulation and random assignment, direction of influence and third variables both remain open, which is the limit science practice 2.C exists to teach."),
 dict(q="Two studies of the same question reach different conclusions, one using naturalistic observation and one using a survey. The most reasonable interpretation is that", choices=[
   "each method has different strengths and limitations, so the discrepancy is worth investigating rather than resolved by preferring one",
   "the survey must be correct because it collected more responses",
   "the observation must be correct because it recorded real behavior",
   "one of the studies must have been fabricated"], ans=0,
   why="Observation records behavior but cannot access reasons; surveys access self-report but are subject to socially expected answering. Neither dominates, so a discrepancy is evidence about method as well as about the question."),
 dict(q="A student claims: \"Because gender roles differ between two cultures, they must be entirely learned.\" The most accurate response is that", choices=[
   "cross-cultural variation shows that experience matters but does not by itself rule out other influences",
   "cross-cultural variation proves nothing about any influence",
   "the claim is fully established by the observation",
   "cultures cannot be compared on any psychological variable"], ans=0,
   why="Science practice 4.B: variation across cultures is evidence that environment contributes, which is a weaker conclusion than 'entirely learned' -- and EK 1.1.A.1's interaction of heredity and environment is the framework's standing caution against either extreme."),
]
