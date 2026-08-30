# AP PSYCHOLOGY 3.2 Physical Development Across the Lifespan — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objectives 3.2.A (prenatal), 3.2.B (infancy and childhood), 3.2.C
# (adolescence), 3.2.D (adulthood).
#
# Essential knowledge relied on: 3.2.A.1 teratogens, maternal illness, genetic
# mutations, hormonal and environmental factors influencing prenatal milestones;
# 3.2.B.1 physical development happening in generally the same ORDER while the
# TIMING varies, and fine and gross motor coordination among the milestones;
# 3.2.B.2 infant reflexes, with the rooting reflex as the framework's example,
# indicating on-track milestone development; 3.2.B.3 the visual cliff apparatus
# as evidence of early depth perception and as an innovative way to assess infant
# responses; 3.2.B.4 critical or sensitive periods with strong developmental
# effects, especially for language, and imprinting in some non-human animals;
# 3.2.C.1 the adolescent growth spurt and puberty, primary and secondary sex
# characteristics, menarche and spermarche; 3.2.D.1 adulthood as a general
# leveling off then varying decline in reproductive ability (menopause),
# mobility, flexibility, reaction time, and visual and auditory sensory acuity.
#
# EXCLUSION STATEMENT respected: EK 3.2.A.1 places the STAGES of prenatal
# development -- zygote, embryo, fetus -- outside the scope of the exam. Those
# three words appear nowhere in this module, as keys or as distractors.
#
# The CED lists 3.C (interpret data) and 4.A (propose a defensible claim) among
# this topic's suggested skills, so several items work from a result stated in
# prose. There are no figures anywhere in this bank.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_2.py.
TOPIC = ("3.2", "Physical Development Across the Lifespan", 3)
QUESTIONS = [
 dict(q="A teratogen is best described as", choices=[
   "an agent that can reach a developing organism before birth and disrupt development",
   "a reflex present at birth that fades during the first year",
   "a hormone released during the adolescent growth spurt",
   "an apparatus used to test depth perception in infants"], ans=0,
   why="EK 3.2.A.1 names teratogens first among the factors that can influence the major physical and psychological milestones of prenatal development."),
 dict(q="Which of the following does the AP Psychology framework name as able to influence prenatal development?", choices=[
   "teratogens, maternal illness, genetic mutations, and hormonal and environmental factors",
   "the serial position effect and chunking",
   "test-retest reliability and split-half reliability",
   "proactive and retroactive interference"], ans=0,
   why="EK 3.2.A.1 lists teratogens, maternal illness, genetic mutations, hormonal and environmental factors; the distractors are drawn from Unit 2's memory and psychometrics topics."),
 dict(q="Physical development in infancy and childhood is described in the AP Psychology framework as happening", choices=[
   "in generally the same order, though the timing can vary from child to child",
   "at exactly the same ages in every healthy child",
   "in a different order for each individual child",
   "only after a child begins to use language"], ans=0,
   why="EK 3.2.B.1 states that physical development in infancy and childhood happens in generally the same order, but the timing of the development can vary."),
 dict(q="A parent worries because her 14-month-old is not yet walking, although her neighbor's child walked at 11 months. According to the AP Psychology framework, the most accurate response is that", choices=[
   "the order of motor milestones is consistent across children, but the timing varies",
   "any deviation from the average age indicates a developmental problem",
   "motor milestones occur in a different order for every child",
   "walking is unrelated to motor development"], ans=0,
   why="EK 3.2.B.1's claim is precisely that order is general while timing varies, which is what separates a difference in timing from a difference in sequence."),
 dict(q="Gross motor coordination refers to control of", choices=[
   "large movements such as walking, running, and climbing",
   "small precise movements such as grasping a crayon",
   "the muscles of the face during emotional expression",
   "involuntary processes such as heart rate"], ans=0,
   why="EK 3.2.B.1 names the development of fine and gross motor coordination among the milestones of infancy and childhood; gross coordination is the large-movement half of that pair."),
 dict(q="Fine motor coordination refers to control of", choices=[
   "small precise movements such as picking up a small object with the fingers",
   "large whole-body movements such as running",
   "the timing of the sleep-wake cycle",
   "the reflexes present at birth"], ans=0,
   why="EK 3.2.B.1 names fine and gross motor coordination together; fine coordination is the small-precise-movement half."),
 dict(q="According to the AP Psychology framework, why do developing motor skills matter psychologically as well as physically?", choices=[
   "they allow children to develop critical skills needed to become more independent",
   "they determine a child's eventual adult height",
   "they replace the need for language development",
   "they eliminate the infant reflexes"], ans=0,
   why="EK 3.2.B.1 states that these physical skills develop as children mature, allowing children to develop critical skills needed to become more independent."),
 dict(q="The rooting reflex is cited in the AP Psychology framework as an example of", choices=[
   "an infant reflex indicating on-track physical and psychological milestone development",
   "a learned response acquired through repeated feeding",
   "a critical period for language acquisition",
   "imprinting on a caregiver"], ans=0,
   why="EK 3.2.B.2 states that infants possess reflexes, like the rooting reflex, that indicate on-track physical and psychological milestone development."),
 dict(q="What does the presence of expected reflexes in a newborn indicate, according to the framework?", choices=[
   "that physical and psychological milestone development is on track",
   "that the infant has already begun to learn from experience",
   "that a critical period has closed",
   "that the infant has imprinted on a caregiver"], ans=0,
   why="EK 3.2.B.2 gives reflexes exactly this diagnostic role: they indicate on-track milestone development, which is why their absence is informative to a clinician."),
 dict(q="The visual cliff apparatus was used to demonstrate that infants", choices=[
   "have an early ability to perceive depth",
   "can recognize their own reflection",
   "prefer the faces of their caregivers to those of strangers",
   "acquire language through imitation"], ans=0,
   why="EK 3.2.B.3 states that research using the visual cliff apparatus demonstrates an early ability in infants to perceive depth."),
 dict(q="Besides its finding about depth, the AP Psychology framework highlights the visual cliff as", choices=[
   "an innovative way to assess infant responses",
   "the first true experiment in psychology",
   "an example of an unethical research procedure",
   "a test of language comprehension"], ans=0,
   why="EK 3.2.B.3 credits the visual cliff both with demonstrating early depth perception and with being an innovative way to assess infant responses, which is a methodological point rather than a content one."),
 dict(q="Why is an apparatus like the visual cliff needed to study infant perception at all?", choices=[
   "infants cannot report what they perceive, so researchers must infer it from behavior",
   "infants cannot see until several months after birth",
   "infants' perception cannot be studied by any means",
   "infants are too easily distracted to be observed"], ans=0,
   why="EK 3.2.B.3 calls the visual cliff an innovative way to ASSESS INFANT RESPONSES, which is the problem it solves: a preverbal participant's perception has to be read from what she does."),
 dict(q="A critical or sensitive period is best described as", choices=[
   "a window in development during which an experience has an especially strong effect",
   "the interval between two measurements in a longitudinal study",
   "the time it takes an infant reflex to disappear",
   "the period of most rapid physical growth in adolescence"], ans=0,
   why="EK 3.2.B.4 states that research suggests critical or sensitive periods in infancy and childhood have strong developmental effects."),
 dict(q="Which skill does the AP Psychology framework name as especially subject to critical or sensitive periods?", choices=[
   "language",
   "arithmetic",
   "handwriting",
   "map reading"], ans=0,
   why="EK 3.2.B.4 states that critical or sensitive periods have strong developmental effects, especially for skills such as language."),
 dict(q="Imprinting, as described in the AP Psychology framework, refers to the fact that", choices=[
   "some non-human animals will attach to the first object they encounter, as a means of survival",
   "human infants form an attachment to whoever feeds them most often",
   "a memory becomes permanent once it has been rehearsed enough",
   "a reflex becomes a voluntary movement with practice"], ans=0,
   why="EK 3.2.B.4 states that some non-human animals will imprint on the first object they encounter as a means of survival; the framework attributes imprinting to non-human animals specifically."),
 dict(q="A researcher claims that human infants imprint on their mothers in the same way that goslings do. The most accurate framework-based response is that", choices=[
   "the framework describes imprinting in some non-human animals, not in humans",
   "imprinting has never been observed in any species",
   "human imprinting occurs but only after the first year",
   "imprinting and the rooting reflex are the same process"], ans=0,
   why="EK 3.2.B.4 confines imprinting to some NON-HUMAN animals; extending it to humans goes beyond what the framework states, and human attachment is treated separately in Topic 3.6."),
 dict(q="The two main physical milestones of adolescence named in the AP Psychology framework are", choices=[
   "the adolescent growth spurt and puberty",
   "the rooting reflex and gross motor coordination",
   "menopause and declining reaction time",
   "imprinting and the critical period for language"], ans=0,
   why="EK 3.2.C.1 states that the main physical and psychological milestones occurring in adolescence are the adolescent growth spurt and puberty, in which reproductive ability develops."),
 dict(q="Puberty is defined in the AP Psychology framework primarily by", choices=[
   "the development of reproductive ability",
   "the attainment of adult height",
   "the completion of brain development",
   "the disappearance of infant reflexes"], ans=0,
   why="EK 3.2.C.1 describes puberty as the period in which reproductive ability develops, which is what distinguishes it from the growth spurt occurring alongside it."),
 dict(q="Menarche and spermarche are cited in the AP Psychology framework as examples of", choices=[
   "sex characteristics developing during adolescence",
   "reflexes present at birth",
   "declines associated with adulthood",
   "critical periods for language"], ans=0,
   why="EK 3.2.C.1 states that adolescents develop primary and secondary sex characteristics during this time, such as menarche and spermarche."),
 dict(q="A 13-year-old grows several inches in a single year. This is best described as", choices=[
   "the adolescent growth spurt",
   "the onset of menopause",
   "a critical period for motor development",
   "the rooting reflex"], ans=0,
   why="EK 3.2.C.1 names the adolescent growth spurt among the main physical milestones of adolescence, alongside puberty."),
 dict(q="Adulthood is characterized in the AP Psychology framework as", choices=[
   "a general leveling off followed by a varying decline in several capacities",
   "a period of no measurable physical change",
   "a period of continued rapid physical growth",
   "the completion of all developmental change"], ans=0,
   why="EK 3.2.D.1 states that adulthood spans most of the lifespan and is characterized by a general leveling off and then a varying decline."),
 dict(q="Which capacities does the AP Psychology framework name as declining in adulthood?", choices=[
   "reproductive ability, mobility, flexibility, reaction time, and sensory acuity",
   "vocabulary, general knowledge, and reading comprehension",
   "the rooting and grasping reflexes",
   "fine and gross motor coordination in infancy"], ans=0,
   why="EK 3.2.D.1 names reproductive ability (menopause), mobility, flexibility, reaction time, and visual and auditory sensory acuity as the capacities that level off and then decline."),
 dict(q="Menopause is cited in the AP Psychology framework as an example of", choices=[
   "the decline in reproductive ability that occurs during adulthood",
   "a milestone of adolescence",
   "a critical period",
   "a teratogenic effect"], ans=0,
   why="EK 3.2.D.1 gives menopause as its example of the decline in reproductive ability characterizing adulthood."),
 dict(q="The word \"varying\" in the framework's description of decline during adulthood indicates that", choices=[
   "the extent and rate of decline differ from person to person",
   "decline reverses itself periodically",
   "decline occurs in only one capacity at a time",
   "no decline occurs in most adults"], ans=0,
   why="EK 3.2.D.1 describes a general leveling off and then a VARYING decline, which is a statement that the pattern is not uniform across individuals."),
 dict(q="Which sequence correctly orders the framework's four periods of physical development?", choices=[
   "prenatal, infancy and childhood, adolescence, adulthood",
   "infancy and childhood, prenatal, adolescence, adulthood",
   "prenatal, adolescence, infancy and childhood, adulthood",
   "adolescence, prenatal, adulthood, infancy and childhood"], ans=0,
   why="Learning objectives 3.2.A through 3.2.D are organized in exactly this order: physical development before birth, in infancy and childhood, in adolescence, and in adulthood."),
 dict(q="A study reports that adults aged 60 have slower average reaction times than adults aged 25, based on testing both groups in one week. This design is", choices=[
   "cross-sectional",
   "longitudinal",
   "experimental",
   "a case study"], ans=0,
   why="Comparing different age groups at a single point in time is the cross-sectional design from objective 3.1.B, and age cannot be manipulated so the study is not an experiment."),
 dict(q="A researcher reports that infants in a study crossed the shallow side of a visual cliff 90 percent of the time and the deep side 8 percent of the time. The most defensible interpretation is that", choices=[
   "the infants responded differently to the two sides, which is consistent with early depth perception",
   "the infants were afraid of the researchers",
   "the infants could not see the surface at all",
   "the infants had learned to avoid heights from previous falls"], ans=0,
   why="EK 3.2.B.3 credits the visual cliff with demonstrating early depth perception; a large behavioral difference between the two sides is what supports that inference, and nothing in the result speaks to fear of researchers or prior falls."),
 dict(q="A researcher wants to study whether a particular substance harms prenatal development in humans. Why can this not be studied with a true experiment?", choices=[
   "no one may ethically be assigned to be exposed to a suspected harmful substance",
   "prenatal development cannot be measured",
   "experiments require more than two groups",
   "the effects would be too large to detect"], ans=0,
   why="Science practice 2.D: assigning a person to a suspected harm violates the ethical obligation to protect participants, so evidence about teratogens in humans comes from non-experimental designs."),
 dict(q="Which is the best operational definition of \"gross motor development\" for a study of toddlers?", choices=[
   "the number of stairs a child can climb unassisted in one attempt",
   "how physically advanced the child appears",
   "the child's general level of coordination",
   "whether the child likes to move around"], ans=0,
   why="An operational definition states the countable procedure; a stair count is measurable, while the alternatives restate the construct or measure preference instead of ability."),
 dict(q="A parent claims: \"Because my child began walking later than average, she will be behind in everything.\" Which framework content most directly challenges that claim?", choices=[
   "EK 3.2.B.1's statement that development follows a general order while its timing varies",
   "EK 3.2.B.4's account of critical periods for language",
   "EK 3.2.D.1's description of decline in adulthood",
   "EK 3.2.C.1's account of the adolescent growth spurt"], ans=0,
   why="Science practice 4.B: the parent infers a general deficit from off-average timing, and EK 3.2.B.1 is the statement that timing varies while the order is general -- the other options concern other periods of life entirely."),
]
