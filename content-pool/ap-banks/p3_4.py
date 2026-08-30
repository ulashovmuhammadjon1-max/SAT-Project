# AP PSYCHOLOGY 3.4 Cognitive Development Across the Lifespan — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objective 3.4.A.
#
# Essential knowledge relied on: 3.4.A.1 Piaget -- children develop schemas via
# continuous and discontinuous processes such as assimilation and accommodation;
# 3.4.A.1.i the sensorimotor stage, infancy through toddlerhood, in which object
# permanence develops; 3.4.A.1.ii the preoperational stage, toddlerhood through
# early childhood, in which children become proficient with mental symbols and
# pretend play, and which the framework says is identified MORE BY WHAT CHILDREN
# CANNOT DO (conservation, reversibility) AND BY WHAT THEY EXHIBIT (animism,
# egocentrism), with theory of mind beginning to develop; 3.4.A.1.iii the
# concrete operational stage, early through late childhood, in which the
# preoperational errors are generally corrected and thinking is logical,
# realistic, and straightforward but not yet systematic; 3.4.A.1.iv the formal
# operational stage, late childhood through adulthood, bringing abstract and
# hypothetical thought, with Piaget's own proposal that NOT ALL PEOPLE achieve
# it; 3.4.A.2 Vygotsky -- children as social learners, scaffolding by others
# within sociocultural contexts, and the zone of proximal development; 3.4.A.3
# crystallized intelligence remaining relatively stable through adulthood while
# fluid intelligence tends to wane, and dementia among the cognitive disorders
# affecting adults.
#
# THE AGE RANGES ARE THE FRAMEWORK'S OWN and are stated in words, not in years:
# "infancy through toddlerhood", "toddlerhood through early childhood", "early
# through late childhood", "late childhood through adulthood". No item here
# attaches a specific year to a stage, because the CED does not.
#
# Assimilation and accommodation are defined in EK 2.2.A.2 (Unit 2) and invoked
# again in EK 3.4.A.1; item 4 keys the Piagetian use and cross-references both.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_4.py.
TOPIC = ("3.4", "Cognitive Development Across the Lifespan", 3)
QUESTIONS = [
 dict(q="According to Piaget, children develop schemas through", choices=[
   "continuous and discontinuous processes such as assimilation and accommodation",
   "reinforcement and punishment delivered by adults",
   "the maturation of the sensory organs alone",
   "imitation of peers without any adult involvement"], ans=0,
   why="EK 3.4.A.1 states that according to Piaget, children develop schemas via continuous and discontinuous processes such as assimilation and accommodation."),
 dict(q="Which of Piaget's stages does the AP Psychology framework place first, and what develops during it?", choices=[
   "the sensorimotor stage, during which object permanence develops",
   "the preoperational stage, during which conservation develops",
   "the concrete operational stage, during which pretend play develops",
   "the formal operational stage, during which reversibility develops"], ans=0,
   why="EK 3.4.A.1.i states that the sensorimotor stage occurs from infancy through toddlerhood and that object permanence develops during this stage."),
 dict(q="Object permanence is the understanding that", choices=[
   "an object continues to exist when it cannot be seen",
   "the amount of a substance stays the same when its shape changes",
   "an action can be mentally reversed",
   "other people can hold beliefs different from one's own"], ans=0,
   why="EK 3.4.A.1.i assigns object permanence to the sensorimotor stage; the distractors are conservation and reversibility from EK 3.4.A.1.ii and theory of mind from the same EK."),
 dict(q="A child who has a schema for \"bird\" sees a bat and calls it a bird without changing her category. In Piaget's terms this is", choices=[
   "assimilation",
   "accommodation",
   "conservation",
   "scaffolding"], ans=0,
   why="EK 2.2.A.2 defines assimilation as taking in new information but not changing the schema, and EK 3.4.A.1 names assimilation as one of the processes by which Piagetian schemas develop."),
 dict(q="Told that a bat is not a bird, the same child revises her \"bird\" category to exclude it. In Piaget's terms this is", choices=[
   "accommodation",
   "assimilation",
   "egocentrism",
   "the zone of proximal development"], ans=0,
   why="EK 2.2.A.2 defines accommodation as taking in new information and changing the schema to incorporate it, and EK 3.4.A.1 names it as a Piagetian process."),
 dict(q="During the preoperational stage, children become proficient in", choices=[
   "using mental symbols, including engaging in pretend play",
   "thinking abstractly about hypothetical situations",
   "conserving quantity across changes in appearance",
   "reasoning systematically through all possible combinations"], ans=0,
   why="EK 3.4.A.1.ii states that in the preoperational stage children become proficient in using mental symbols and engage in pretend play; the distractors are abilities the framework assigns to later stages."),
 dict(q="According to the AP Psychology framework, the preoperational stage is identified more by", choices=[
   "the cognitive tasks children cannot yet perform and the errors they do exhibit",
   "the age at which a child begins speaking",
   "the child's score on an intelligence test",
   "the number of schemas a child has accommodated"], ans=0,
   why="EK 3.4.A.1.ii states that the preoperational stage is identified more by cognitive tasks children cannot perform, such as conservation and reversibility, or by those they exhibit, such as animism and egocentrism."),
 dict(q="Conservation is the understanding that", choices=[
   "a quantity stays the same even when its appearance changes",
   "an object still exists when it is hidden",
   "other people see things from their own point of view",
   "inanimate objects have feelings"], ans=0,
   why="EK 3.4.A.1.ii names conservation among the tasks preoperational children cannot yet perform; the distractors are object permanence, egocentrism reversed, and animism."),
 dict(q="A child watches water poured from a short wide glass into a tall narrow one and says the tall glass now has more water. According to Piaget, this child has not yet mastered", choices=[
   "conservation",
   "object permanence",
   "animism",
   "theory of mind"], ans=0,
   why="EK 3.4.A.1.ii lists conservation among the tasks preoperational children cannot perform; judging quantity by appearance is the standard demonstration of its absence."),
 dict(q="Reversibility, as Piaget used the term, is the understanding that", choices=[
   "an action or operation can be mentally undone to return to the starting state",
   "objects continue to exist when out of sight",
   "other people can hold false beliefs",
   "living things grow and change over time"], ans=0,
   why="EK 3.4.A.1.ii lists reversibility alongside conservation among the tasks preoperational children cannot yet perform; the two are closely linked, since undoing the pour mentally is what reveals the quantity is unchanged."),
 dict(q="Animism, as the term appears in Piaget's account of the preoperational stage, is", choices=[
   "attributing lifelike qualities to inanimate objects",
   "the belief that objects cease to exist when hidden",
   "difficulty taking another person's visual perspective",
   "the ability to reason about hypothetical situations"], ans=0,
   why="EK 3.4.A.1.ii names animism among the characteristics preoperational children exhibit; the distractors are the absence of object permanence, egocentrism, and formal operational thought."),
 dict(q="Egocentrism, in Piaget's account, refers to", choices=[
   "difficulty taking a perspective other than one's own",
   "selfishness in sharing with other children",
   "the belief that inanimate objects are alive",
   "the inability to remember events from infancy"], ans=0,
   why="EK 3.4.A.1.ii names egocentrism among the characteristics preoperational children exhibit; in Piaget's usage it is a limitation of perspective-taking rather than a moral trait."),
 dict(q="A four-year-old holding a picture book faces it toward himself while describing the pictures to a listener across the table. This behavior best illustrates", choices=[
   "egocentrism",
   "animism",
   "conservation",
   "object permanence"], ans=0,
   why="EK 3.4.A.1.ii's egocentrism is difficulty taking a perspective other than one's own, which is what failing to turn the book toward the listener demonstrates."),
 dict(q="Theory of mind is best described as the understanding that", choices=[
   "other people have beliefs, desires, and knowledge that may differ from one's own",
   "objects continue to exist when they are hidden",
   "quantity is unchanged by a change in shape",
   "a mental operation can be reversed"], ans=0,
   why="EK 3.4.A.1.ii states that children begin to develop a theory of mind during the preoperational stage; it concerns the mental states of others rather than physical quantities."),
 dict(q="In the concrete operational stage, children generally", choices=[
   "correct the cognitive errors of the preoperational stage and reason in logical, realistic, straightforward ways",
   "acquire object permanence for the first time",
   "become able to reason about purely hypothetical situations",
   "lose the ability to use mental symbols"], ans=0,
   why="EK 3.4.A.1.iii states that children in the concrete operational stage can generally correct the cognitive errors made in the preoperational stage and understand the world in logical, realistic, and straightforward ways."),
 dict(q="What limitation does the AP Psychology framework attribute to concrete operational thinkers?", choices=[
   "they struggle to think systematically",
   "they cannot use language",
   "they have not yet developed object permanence",
   "they cannot distinguish living from nonliving things"], ans=0,
   why="EK 3.4.A.1.iii states that concrete operational children understand the world logically and realistically but struggle to think systematically, which is the limitation the formal operational stage removes."),
 dict(q="The formal operational stage is characterized by the ability to", choices=[
   "think abstractly and hypothetically",
   "conserve quantity across changes in appearance",
   "take another person's visual perspective",
   "recognize that a hidden object still exists"], ans=0,
   why="EK 3.4.A.1.iv states that people in the formal operational stage gain the ability to think abstractly and hypothetically; the distractors are achievements of earlier stages."),
 dict(q="What did Piaget himself propose about the formal operational stage?", choices=[
   "not all people achieve formal operational thinking",
   "every person reaches it by the age of twelve",
   "it is reached before the concrete operational stage",
   "it disappears again in late adulthood"], ans=0,
   why="EK 3.4.A.1.iv states explicitly that Piaget proposed that not all people achieve formal operational thinking, which is why the stage sequence is not a guarantee of an endpoint."),
 dict(q="Which sequence gives Piaget's stages in the order the AP Psychology framework presents them?", choices=[
   "sensorimotor, preoperational, concrete operational, formal operational",
   "preoperational, sensorimotor, formal operational, concrete operational",
   "sensorimotor, concrete operational, preoperational, formal operational",
   "formal operational, concrete operational, preoperational, sensorimotor"], ans=0,
   why="EK 3.4.A.1.i through 3.4.A.1.iv present the stages in this order, each with its own span from infancy through adulthood."),
 dict(q="An adolescent can consider what would follow if a law were changed, without any change actually occurring. According to Piaget this reasoning belongs to", choices=[
   "the formal operational stage",
   "the concrete operational stage",
   "the preoperational stage",
   "the sensorimotor stage"], ans=0,
   why="EK 3.4.A.1.iv assigns abstract and hypothetical thought to the formal operational stage; reasoning about a situation that does not exist is hypothetical by definition."),
 dict(q="According to Vygotsky, children learn primarily", choices=[
   "as social learners, through interacting with other people within sociocultural contexts",
   "by passing through fixed stages regardless of who is present",
   "through trial and error without any guidance",
   "only after they have achieved formal operational thought"], ans=0,
   why="EK 3.4.A.2 states that according to Vygotsky, children are social learners who learn through interacting with and scaffolding by other people within sociocultural contexts."),
 dict(q="Scaffolding, in Vygotsky's account, refers to", choices=[
   "support provided by a more capable person that is adjusted to what the learner can currently do",
   "the fixed sequence of stages every child passes through",
   "the physical environment in which learning occurs",
   "a child's tendency to imitate a peer exactly"], ans=0,
   why="EK 3.4.A.2 names scaffolding by other people as the means through which social learning occurs, which is support supplied by someone more capable."),
 dict(q="The zone of proximal development is best described as the range of tasks a learner", choices=[
   "cannot yet do alone but can do with appropriate help",
   "can already do without any assistance",
   "will never be able to do at any age",
   "has already been formally tested on"], ans=0,
   why="EK 3.4.A.2 states that ideally learning occurs while the person is in their zone of proximal development, which is the region between independent capability and what help makes possible."),
 dict(q="A teacher gives a student just enough of a hint to solve a problem the student could not solve alone, then withdraws the hint on the next problem. This practice is best described in Vygotsky's terms as", choices=[
   "scaffolding within the zone of proximal development",
   "assimilation of a new schema",
   "conservation of quantity",
   "a demonstration of egocentrism"], ans=0,
   why="EK 3.4.A.2 pairs scaffolding with the zone of proximal development: support adjusted to a task the learner cannot yet do alone, and withdrawn as capability grows."),
 dict(q="Which statement correctly contrasts Piaget's and Vygotsky's accounts as the AP Psychology framework presents them?", choices=[
   "Piaget emphasizes stages through which children develop schemas; Vygotsky emphasizes learning through social interaction within a sociocultural context",
   "Vygotsky emphasizes stages through which children develop schemas; Piaget emphasizes learning through social interaction",
   "both theorists describe development as entirely biological",
   "both theorists deny that children's thinking changes with age"], ans=0,
   why="EK 3.4.A.1 presents Piaget in terms of schemas and stages while EK 3.4.A.2 presents Vygotsky in terms of social learning, scaffolding, and sociocultural context; the first distractor swaps the two."),
 dict(q="According to the AP Psychology framework, how do crystallized and fluid intelligence change across adulthood?", choices=[
   "crystallized intelligence remains relatively stable while fluid intelligence tends to wane",
   "fluid intelligence remains relatively stable while crystallized intelligence tends to wane",
   "both decline at the same rate from early adulthood",
   "both increase steadily throughout adulthood"], ans=0,
   why="EK 3.4.A.3 states that crystallized intelligence remains relatively stable through adulthood while fluid intelligence tends to wane as people age."),
 dict(q="An adult finds that her vocabulary and accumulated knowledge remain strong while her speed at solving unfamiliar puzzles has declined. This pattern matches the framework's account of", choices=[
   "stable crystallized intelligence alongside waning fluid intelligence",
   "stable fluid intelligence alongside waning crystallized intelligence",
   "the onset of a cognitive disorder",
   "a failure of object permanence"], ans=0,
   why="EK 3.4.A.3 attributes exactly this pattern to normal adult development, which is why the scenario does not warrant the inference of a disorder."),
 dict(q="Dementia is named in the AP Psychology framework as", choices=[
   "a cognitive disorder that affects adults",
   "a normal feature of aging that everyone experiences",
   "a stage in Piaget's sequence",
   "a form of scaffolding"], ans=0,
   why="EK 3.4.A.3 states that cognitive disorders that affect adults include dementia, listing it as a disorder rather than as part of ordinary aging."),
 dict(q="A researcher gives children of different ages the same conservation task on a single afternoon and compares performance across the age groups. This design is", choices=[
   "cross-sectional",
   "longitudinal",
   "experimental",
   "a case study"], ans=0,
   why="Comparing different age groups at one point in time is the cross-sectional design of objective 3.1.B; age is not manipulated, so the study is not an experiment."),
 dict(q="A critic argues that Piaget's stage descriptions underestimate what young children can do, citing studies in which simplified tasks reveal earlier competence. Which framework content most directly supports treating that criticism seriously?", choices=[
   "EK 3.4.A.1.ii's statement that the preoperational stage is identified more by the tasks children cannot perform, which makes stage placement depend on how the task is posed",
   "EK 3.4.A.3's account of crystallized and fluid intelligence in adulthood",
   "EK 3.4.A.2's account of the zone of proximal development",
   "EK 3.4.A.1.iv's statement that not all people achieve formal operational thought"], ans=0,
   why="Science practice 4.B: if a stage is identified by failures on particular tasks, then a task that is easier to understand may reveal ability the original task concealed, which is exactly the criticism's logic."),
]
