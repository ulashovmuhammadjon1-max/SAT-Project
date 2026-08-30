# AP PSYCHOLOGY 3.6 Social-Emotional Development Across the Lifespan
# — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objective 3.6.A -- the largest single objective in Unit 3, carrying
# eight essential-knowledge statements.
#
# Essential knowledge relied on: 3.6.A.1 ecological systems theory and its five
# systems -- microsystem (groups in direct contact with the individual),
# mesosystem (relationships BETWEEN groups in the microsystem), exosystem
# (indirect factors), macrosystem (cultural events affecting the individual and
# others around them), chronosystem (the individual's current stage of life);
# 3.6.A.2 authoritarian, authoritative, and permissive parenting styles, with
# cultural differences in how they affect outcomes; 3.6.A.3 attachment styles --
# secure and insecure (avoidant, anxious, disorganized) -- varying by culture,
# with temperament related to how children attach; 3.6.A.3.i separation anxiety;
# 3.6.A.3.ii studies with monkeys demonstrating the importance of comfort over
# food; 3.6.A.4.i parallel and pretend play; 3.6.A.4.ii adolescents relying more
# on peers with age and showing an egocentrism expressed as the imaginary
# audience and the personal fable; 3.6.A.5.i culture determining when adulthood
# begins and when major life events occur (social clock), and emerging adulthood;
# 3.6.A.5.ii adult family or family-like relationships providing mutual support,
# with childhood attachment styles affecting adult attachment; 3.6.A.6 the stage
# theory of psychosocial development and its eight conflicts; 3.6.A.7 adverse
# childhood experiences (ACEs) and sociocultural differences in what counts as
# one; 3.6.A.8 identity through achievement, diffusion, foreclosure, and
# moratorium, and the identities adolescents develop, often through considering
# possible selves.
#
# EXCLUSION STATEMENT respected: EK 3.6.A.6 places the PSYCHOSEXUAL stage theory
# of development outside the scope of the exam. Item 25 keys that boundary; no
# item tests psychosexual content.
#
# NO THEORIST IS NAMED ANYWHERE IN THIS MODULE. The CED presents ecological
# systems theory, the monkey attachment studies, and the psychosocial stage
# theory without attributing any of them to a person. Keying an item to a name
# the framework does not print would test something the course does not teach.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_6.py.
TOPIC = ("3.6", "Social-Emotional Development Across the Lifespan", 3)
QUESTIONS = [
 dict(q="Ecological systems theory explores", choices=[
   "how the social environment influences development",
   "how genes determine behavior independently of experience",
   "how memories are consolidated during sleep",
   "how neurons transmit signals to one another"], ans=0,
   why="EK 3.6.A.1 states that the ecological systems theory explores how the social environment influences development, and organizes that environment into five systems."),
 dict(q="In ecological systems theory, the microsystem consists of", choices=[
   "the groups that have direct contact with the individual",
   "the relationships between groups that contact the individual",
   "cultural events affecting the individual and others",
   "the individual's current stage of life"], ans=0,
   why="EK 3.6.A.1 defines the microsystem as groups that have direct contact with the individual; each distractor is the definition of another of the five systems."),
 dict(q="In ecological systems theory, the mesosystem consists of", choices=[
   "the relationships between the groups that have direct contact with the individual",
   "the groups that have direct contact with the individual",
   "indirect factors in the individual's life",
   "the individual's current stage of life"], ans=0,
   why="EK 3.6.A.1 defines the mesosystem as the relationships between groups in the microsystem, which is what makes it one level up rather than a larger set of groups."),
 dict(q="A child's parents and teacher meet regularly to coordinate how they support her. In ecological systems theory this coordination belongs to the", choices=[
   "mesosystem",
   "microsystem",
   "exosystem",
   "chronosystem"], ans=0,
   why="EK 3.6.A.1 places relationships BETWEEN microsystem groups in the mesosystem; family and school are each microsystems, and the link between them is the mesosystem."),
 dict(q="A parent's workplace changes its schedule, which alters how much time the parent spends at home, though the child never visits the workplace. In ecological systems theory this is an example of the", choices=[
   "exosystem",
   "microsystem",
   "macrosystem",
   "mesosystem"], ans=0,
   why="EK 3.6.A.1 defines the exosystem as indirect factors in an individual's life; a setting the child never enters, but which shapes her circumstances, is indirect by definition."),
 dict(q="In ecological systems theory, cultural events that affect an individual and those around them belong to the", choices=[
   "macrosystem",
   "chronosystem",
   "exosystem",
   "microsystem"], ans=0,
   why="EK 3.6.A.1 defines the macrosystem as cultural events that affect the individuals and others around them."),
 dict(q="In ecological systems theory, the chronosystem refers to", choices=[
   "the individual's current stage of life",
   "the culture in which the individual lives",
   "the groups in direct contact with the individual",
   "the indirect factors in the individual's life"], ans=0,
   why="EK 3.6.A.1 defines the chronosystem as the individual's current stage of life."),
 dict(q="Which parenting styles does the AP Psychology framework name?", choices=[
   "authoritarian, authoritative, and permissive",
   "secure, avoidant, and anxious",
   "parallel, pretend, and cooperative",
   "achievement, diffusion, and moratorium"], ans=0,
   why="EK 3.6.A.2 states that research has identified different parenting styles of caregivers, including authoritarian, authoritative, and permissive; the distractors are attachment styles, play types, and identity processes from other EKs in this topic."),
 dict(q="A caregiver enforces strict rules, expects obedience without explanation, and rarely negotiates. This style is best described as", choices=[
   "authoritarian",
   "authoritative",
   "permissive",
   "avoidant"], ans=0,
   why="EK 3.6.A.2 names authoritarian among the parenting styles; high demand paired with little explanation or negotiation is what the term denotes, as distinct from the authoritative style."),
 dict(q="A caregiver sets clear expectations, explains the reasons behind rules, and is responsive to the child's point of view. This style is best described as", choices=[
   "authoritative",
   "authoritarian",
   "permissive",
   "disorganized"], ans=0,
   why="EK 3.6.A.2 names authoritative among the parenting styles; expectations combined with explanation and responsiveness are what separate it from the authoritarian style whose name it resembles."),
 dict(q="What does the AP Psychology framework say about how parenting styles affect outcomes?", choices=[
   "cultural differences exist in the ways these styles affect outcomes in caregivers and children",
   "each style produces the same outcome in every culture studied",
   "parenting style has no measurable effect on any outcome",
   "only the permissive style has been studied"], ans=0,
   why="EK 3.6.A.2 states explicitly that cultural differences exist in the ways these parenting styles affect outcomes in caregivers and children, which forbids a single universal ranking of the styles."),
 dict(q="Which attachment styles does the AP Psychology framework name?", choices=[
   "secure and insecure, with insecure comprising avoidant, anxious, and disorganized",
   "authoritarian, authoritative, and permissive",
   "trust, autonomy, and initiative",
   "parallel, pretend, and solitary"], ans=0,
   why="EK 3.6.A.3 states that the types of attachment infants and children display include secure and insecure (avoidant, anxious, and disorganized)."),
 dict(q="According to EK 3.6.A.3, what is related to how children attach to their caregivers?", choices=[
   "temperament",
   "vocabulary size",
   "birth order",
   "the number of hours the child sleeps"], ans=0,
   why="EK 3.6.A.3 states that temperament is related to how children attach to caregivers, which places some of the variation in the child rather than only in the caregiver."),
 dict(q="Separation anxiety, as the framework defines it, occurs when children", choices=[
   "express heightened anxiety or fear when away from a caregiver or in the presence of a stranger",
   "refuse to interact with peers of their own age",
   "show no preference between a caregiver and a stranger",
   "are unable to form any attachment at all"], ans=0,
   why="EK 3.6.A.3.i states that separation anxiety occurs when children express heightened anxiety or fear when away from a caregiver or in the presence of a stranger."),
 dict(q="Studies with monkeys are cited in the AP Psychology framework as demonstrating", choices=[
   "the importance of comfort over food in attachment",
   "that attachment forms only through feeding",
   "that monkeys cannot form attachments",
   "that attachment styles are identical across species"], ans=0,
   why="EK 3.6.A.3.ii states that studies with monkeys demonstrate the importance of comfort over food in attachment."),
 dict(q="The AP Psychology framework notes that attachment styles", choices=[
   "vary by culture",
   "are identical in every society studied",
   "are fixed at birth and never change",
   "cannot be observed in infants"], ans=0,
   why="EK 3.6.A.3 states that research has identified different attachment styles demonstrated by infants and children, WHICH VARY BY CULTURE."),
 dict(q="Two toddlers sit side by side, each absorbed in her own toy, occasionally glancing at the other but not playing together. This is best described as", choices=[
   "parallel play",
   "pretend play",
   "an insecure attachment",
   "the imaginary audience"], ans=0,
   why="EK 3.6.A.4.i names parallel and pretend play as the ways children engage with peers; playing alongside rather than with another child is what parallel play denotes."),
 dict(q="Children use a cardboard box as a spaceship and assign one another roles in an invented story. This is best described as", choices=[
   "pretend play",
   "parallel play",
   "the personal fable",
   "scaffolding"], ans=0,
   why="EK 3.6.A.4.i names pretend play alongside parallel play; using objects and roles symbolically in a shared invented scenario is what pretend play denotes."),
 dict(q="According to EK 3.6.A.4.ii, as adolescents age they", choices=[
   "gradually rely more on peer relationships",
   "gradually withdraw from all social relationships",
   "rely equally on peers and caregivers at every age",
   "stop forming new relationships entirely"], ans=0,
   why="EK 3.6.A.4.ii states that adolescents gradually rely more on peer relationships as they age."),
 dict(q="An adolescent is convinced that everyone at school noticed a small stain on his shirt and is still thinking about it. This best illustrates", choices=[
   "the imaginary audience",
   "the personal fable",
   "separation anxiety",
   "parallel play"], ans=0,
   why="EK 3.6.A.4.ii names the imaginary audience as one expression of adolescent egocentrism; believing oneself to be the object of others' constant attention is what it denotes."),
 dict(q="An adolescent drives dangerously, convinced that the accidents that happen to other people could not happen to her. This best illustrates", choices=[
   "the personal fable",
   "the imaginary audience",
   "an authoritarian upbringing",
   "the social clock"], ans=0,
   why="EK 3.6.A.4.ii names the personal fable alongside the imaginary audience as expressions of adolescent egocentrism; a belief in one's own uniqueness and invulnerability is what it denotes."),
 dict(q="The social clock refers to", choices=[
   "a culture's expectations about when adulthood begins and when major life events should occur",
   "the biological timing of puberty",
   "the twenty-four-hour cycle of sleep and waking",
   "the rate at which reaction time declines in adulthood"], ans=0,
   why="EK 3.6.A.5.i states that culture plays a role in determining when adulthood begins and when major life events occur, which it calls the social clock; the circadian rhythm distractor belongs to EK 1.5.A.2."),
 dict(q="Emerging adulthood, as the framework describes it, is", choices=[
   "a period some cultures allow as a transition from adolescence to adulthood",
   "a universal biological stage occurring in every society",
   "the final stage of the psychosocial theory",
   "the point at which attachment styles are fixed"], ans=0,
   why="EK 3.6.A.5.i states that SOME cultures allow for a time of emerging adulthood as a transition from adolescence to adulthood, so the framework presents it as culturally variable rather than universal."),
 dict(q="According to EK 3.6.A.5.ii, childhood attachment styles", choices=[
   "can affect how adults form attachments to other adults",
   "have no bearing on adult relationships",
   "determine adult relationships completely and unchangeably",
   "apply only to relationships with biological family members"], ans=0,
   why="EK 3.6.A.5.ii states that childhood attachment styles can affect how adults form attachments to other adults; 'can affect' is weaker than determination, which is why the third option overstates it."),
 dict(q="Which theory of development is explicitly excluded from the scope of the AP Psychology Exam?", choices=[
   "the psychosexual stage theory",
   "the psychosocial stage theory",
   "the ecological systems theory",
   "the theory that temperament relates to attachment"], ans=0,
   why="The exclusion statement under EK 3.6.A.6 places the psychosexual stage theory of development outside the scope of the exam, while the psychosocial stage theory is required content in that same EK."),
 dict(q="The stage theory of psychosocial development proposes that people must", choices=[
   "resolve a psychosocial conflict at each stage of the lifespan",
   "pass through four stages of cognitive reasoning",
   "acquire language before forming attachments",
   "achieve formal operational thinking to reach adulthood"], ans=0,
   why="EK 3.6.A.6 states that the stage theory of psychosocial development proposes that people must resolve psychosocial conflicts at each stage of the lifespan."),
 dict(q="Which pair is one of the eight psychosocial conflicts named in the AP Psychology framework?", choices=[
   "generativity and stagnation",
   "assimilation and accommodation",
   "primacy and recency",
   "convergent and divergent thinking"], ans=0,
   why="EK 3.6.A.6 lists eight conflicts, of which generativity and stagnation is one; the distractors are Piagetian processes, a Topic 2.4 effect, and a Topic 2.2 contrast."),
 dict(q="Which sequence gives the first four psychosocial conflicts in the order the framework lists them?", choices=[
   "trust and mistrust; autonomy and shame and doubt; initiative and guilt; industry and inferiority",
   "initiative and guilt; trust and mistrust; industry and inferiority; autonomy and shame and doubt",
   "identity and role confusion; intimacy and isolation; generativity and stagnation; integrity and despair",
   "industry and inferiority; initiative and guilt; autonomy and shame and doubt; trust and mistrust"], ans=0,
   why="EK 3.6.A.6 lists the eight conflicts in order beginning trust and mistrust, autonomy and shame and doubt, initiative and guilt, industry and inferiority; the third option gives the last four rather than the first four."),
 dict(q="What does the AP Psychology framework say about adverse childhood experiences?", choices=[
   "they affect relationships formed throughout the lifespan, and sociocultural differences exist in what counts as one",
   "they affect only the period of childhood in which they occur",
   "the same events count as adverse in every culture",
   "they have no relationship to later social development"], ans=0,
   why="EK 3.6.A.7 states that ACEs have effects on relationships people form throughout the lifespan and that sociocultural differences exist in what is considered an ACE and how ACEs affect outcomes."),
 dict(q="Which set names the processes through which the framework says adolescents develop a sense of identity?", choices=[
   "achievement, diffusion, foreclosure, and moratorium",
   "trust, autonomy, initiative, and industry",
   "secure, avoidant, anxious, and disorganized",
   "microsystem, mesosystem, exosystem, and macrosystem"], ans=0,
   why="EK 3.6.A.8 states that adolescents develop a sense of identity for who they will be as an adult through the processes of achievement, diffusion, foreclosure, and moratorium; the distractors are the psychosocial conflicts, the attachment styles, and four ecological systems."),
]
