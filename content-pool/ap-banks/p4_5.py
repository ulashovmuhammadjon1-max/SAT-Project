# AP PSYCH 4.5 Social-Cognitive and Trait Theories of Personality — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, p. 102.
# EK 4.5.A.1 social-cognitive theory: reciprocal determinism shapes personality;
#   reciprocal determinism explores self-concept, and self-efficacy and
#   self-esteem both contribute to self-concept.
# EK 4.5.B.1 trait theories: personality is a set of enduring characteristics
#   that lead to typical responses to stimuli.
# EK 4.5.B.2 the Big Five, and factor analysis as the method behind the
#   inventories that measure it.
#
# NAMING, and it is the thing to get right on this topic: the CED's own Big Five
# list is "agreeableness, openness to experience, extraversion, conscientiousness,
# and EMOTIONAL STABILITY". Most material outside the framework names the fifth
# factor by its opposite pole, neuroticism. Items here key on the CED's term, and
# one item addresses the two names directly rather than leaving a student to
# collide with it on the exam.
#
# No sympy: every key's claim is stated item by item in verify_p4_5.py.
TOPIC = ("4.5", "Social-Cognitive and Trait Theories of Personality", 4)
QUESTIONS = [
 dict(q="Social-cognitive theory holds that personality is shaped by reciprocal determinism, meaning that", choices=[
   "the environment determines behavior, and behavior has no effect in return",
   "personal factors, behavior, and the environment each influence the other two",
   "personality is fixed by inherited temperament and changes little afterward",
   "conscious choices are ultimately determined by unconscious conflict"
], ans=1,
   why="EK 4.5.A.1: reciprocal determinism shapes personality. The word reciprocal is the whole point -- influence runs in every direction, not one way from environment to person."),

 dict(q="A student who enjoys debate joins a debate club, and the club's demanding practice further sharpens her argumentative confidence, which leads her to enter more competitions. This cycle best illustrates", choices=[
   "an enduring trait expressed identically in every situation",
   "the mere exposure effect",
   "reciprocal determinism",
   "an unconscious defense mechanism"
], ans=2,
   why="EK 4.5.A.1. Her disposition selects an environment, the environment changes her, and the change alters her behavior again -- influence circulating among person, behavior, and setting."),

 dict(q="Self-concept, as used in social-cognitive theory, refers to", choices=[
   "how a person views themselves, including in relation to others",
   "a person's unconscious image of an idealized parent",
   "the accuracy with which a person predicts their own test scores",
   "the set of traits an observer would assign to a person"], ans=0,
   why="EK 4.5.A.1 defines self-concept as how one views themselves and in relation to others, and states that self-efficacy and self-esteem both contribute to it."),

 dict(q="Self-efficacy is best defined as a person's belief about", choices=[
   "their capability to carry out a particular task successfully",
   "their overall worth as a human being",
   "whether outcomes in life are controlled by luck or by effort",
   "how much other people generally like them"], ans=0,
   why="EK 4.5.A.1. Self-efficacy is a capability judgment attached to a specific task or domain; the option about luck versus effort describes locus of control, a different construct from Topic 4.1."),

 dict(q="Self-esteem is best defined as", choices=[
   "a person's tendency to compare themselves with others",
   "a person's habitual explanation of good and bad events",
   "a person's overall evaluation of their own worth",
   "a person's confidence about one specific skill"
], ans=2,
   why="EK 4.5.A.1 names self-esteem alongside self-efficacy as a contributor to self-concept; self-esteem is the global worth judgment, not a task-specific one."),

 dict(q="What is the clearest difference between self-efficacy and self-esteem?", choices=[
   "Self-efficacy is a global judgment of worth, while self-esteem is a belief about a specific capability",
   "Self-efficacy can be measured but self-esteem cannot",
   "Self-efficacy is unconscious, while self-esteem is conscious",
   "Self-efficacy is a belief about capability in a specific domain, while self-esteem is a global judgment of one's worth"
], ans=3,
   why="EK 4.5.A.1 lists both as separate contributors to self-concept. Specificity is the discriminator: a person can hold low self-efficacy for public speaking while maintaining high overall self-esteem."),

 dict(q="A violinist who doubts she can master a difficult passage but practices it daily and gradually succeeds shows a rise in", choices=[
   "unconditional regard",
   "self-efficacy for that piece",
   "external locus of control",
   "openness to experience"
], ans=1,
   why="EK 4.5.A.1. Repeated successful performance raises the belief that one is capable of that particular task, which is a domain-specific efficacy judgment."),

 dict(q="A student who says, 'I am not good at chemistry, but I am a worthwhile person and good at plenty of other things,' is reporting", choices=[
   "low self-efficacy in one domain alongside intact self-esteem",
   "low self-esteem alongside high self-efficacy in every domain",
   "an external locus of control",
   "a pessimistic explanatory style"], ans=0,
   why="EK 4.5.A.1. The statement separates a specific capability judgment from a global worth judgment, which is exactly the distinction between the two constructs."),

 dict(q="Trait theories of personality conclude that personality consists of", choices=[
   "a tendency toward growth that unfolds when conditions permit",
   "enduring characteristics that produce typical responses to stimuli",
   "unconscious conflicts formed early in life",
   "the sum of a person's reinforcement history"
], ans=1,
   why="EK 4.5.B.1, in substance verbatim: trait theories conclude that personality involves a set of enduring characteristics that lead to typical responses to stimuli."),

 dict(q="Which set correctly names the Big Five traits as the AP Psychology framework lists them?", choices=[
   "agreeableness, openness to experience, extraversion, conscientiousness, emotional stability",
   "agreeableness, optimism, extraversion, conscientiousness, emotional stability",
   "achievement, openness to experience, extraversion, conscientiousness, empathy",
   "agreeableness, openness to experience, egocentrism, conscientiousness, emotional stability"], ans=0,
   why="EK 4.5.B.2 lists exactly these five. Optimism, achievement, empathy, and egocentrism are not Big Five factors, and each distractor swaps in one of them."),

 dict(q="The AP Psychology framework names the fifth Big Five factor emotional stability, while many other sources name the same dimension neuroticism. The relationship between the two labels is that", choices=[
   "emotional stability applies to adults and neuroticism to children",
   "neuroticism is a clinical diagnosis while emotional stability is a personality trait",
   "they name opposite ends of one dimension, so a high score on one corresponds to a low score on the other",
   "they are two separate factors that happen to correlate"
], ans=2,
   why="EK 4.5.B.2 names emotional stability. Neuroticism is the same dimension scored from the other pole -- an important thing for a student to know before meeting either label, and not a second factor."),

 dict(q="A person who seeks out unfamiliar music, enjoys abstract ideas, and readily changes routines for the sake of novelty is highest in", choices=[
   "emotional stability",
   "openness to experience",
   "conscientiousness",
   "agreeableness"
], ans=1,
   why="EK 4.5.B.2. Openness to experience covers imagination, intellectual curiosity, and preference for variety, which is what novelty-seeking across several domains indicates."),

 dict(q="A person who keeps a detailed schedule, meets deadlines well ahead of time, and is relied on for follow-through is highest in", choices=[
   "agreeableness",
   "conscientiousness",
   "extraversion",
   "openness to experience"
], ans=1,
   why="EK 4.5.B.2. Conscientiousness covers organization, discipline, and dependability -- the planning and follow-through described here."),

 dict(q="A person who is energized by large gatherings, speaks readily to strangers, and seeks out social activity is highest in", choices=[
   "agreeableness",
   "openness to experience",
   "conscientiousness",
   "extraversion"
], ans=3,
   why="EK 4.5.B.2. Extraversion covers sociability and the tendency to draw energy from social contact."),

 dict(q="A person who is consistently cooperative, trusting, and quick to help colleagues is highest in", choices=[
   "extraversion",
   "conscientiousness",
   "emotional stability",
   "agreeableness"
], ans=3,
   why="EK 4.5.B.2. Agreeableness covers warmth, cooperation, and trust in dealings with other people."),

 dict(q="A person who stays calm under pressure, recovers quickly from setbacks, and is rarely rattled by criticism is highest in", choices=[
   "agreeableness",
   "conscientiousness",
   "openness to experience",
   "emotional stability"
], ans=3,
   why="EK 4.5.B.2 names emotional stability as the fifth factor; calmness and resilience under stress are its high pole."),

 dict(q="A colleague is highly organized and dependable but blunt, uncooperative, and hard to work with. In Big Five terms this person is", choices=[
   "low in both conscientiousness and agreeableness",
   "high in conscientiousness and low in agreeableness",
   "high in agreeableness and low in conscientiousness",
   "high in both conscientiousness and agreeableness"
], ans=1,
   why="EK 4.5.B.2 treats the five as independent dimensions, so they can take any combination. Organization loads on conscientiousness and interpersonal warmth on agreeableness -- the pairing students most often collapse into one 'good employee' factor."),

 dict(q="A person who is talkative, always at the center of a gathering, and also dismissive and quick to pick arguments is best described as", choices=[
   "low in extraversion and low in agreeableness",
   "high in both extraversion and agreeableness",
   "high in extraversion and low in agreeableness",
   "high in agreeableness and low in extraversion"
], ans=2,
   why="EK 4.5.B.2. Sociability is extraversion and cooperativeness is agreeableness; being outgoing says nothing about being pleasant, which is why these two are worth separating explicitly."),

 dict(q="An artist full of unconventional ideas who never finishes a project and keeps no schedule is best described as", choices=[
   "low in both openness to experience and conscientiousness",
   "high in openness to experience and low in conscientiousness",
   "high in conscientiousness and low in openness to experience",
   "high in both openness to experience and conscientiousness"
], ans=1,
   why="EK 4.5.B.2. Imagination and unconventionality load on openness; planning and follow-through load on conscientiousness, and the two vary independently."),

 dict(q="Factor analysis is used in building personality inventories in order to", choices=[
   "identify clusters of items that correlate with one another and so reflect a smaller number of underlying dimensions",
   "determine whether a treatment caused a change in personality",
   "confirm that a test's items were written at an appropriate reading level",
   "assign each respondent to one of several personality types"], ans=0,
   why="EK 4.5.B.2 states the Big Five traits are measured by specialized personality inventories that use factor analysis to organize item responses; the technique reduces many correlated items to a few dimensions."),

 dict(q="How does a personality inventory differ from a projective test?", choices=[
   "An inventory measures unconscious material, while a projective test measures conscious attitudes",
   "An inventory uses standardized items with fixed response options, while a projective test uses ambiguous stimuli and open-ended responses",
   "An inventory uses ambiguous stimuli, while a projective test uses standardized items",
   "An inventory can be scored, while a projective test cannot be scored at all"
], ans=1,
   why="EK 4.5.B.2 describes inventories as specialized and standardized; EK 4.4.A.3 describes projective tests as probes of preconscious and unconscious material through ambiguity. The last option reverses both."),

 dict(q="A frequently raised limitation of self-report personality inventories is that", choices=[
   "they cannot be administered to more than one person at a time",
   "they produce scores that cannot be compared across respondents",
   "they require the researcher to interpret every answer subjectively",
   "respondents may answer in ways that present themselves favorably rather than accurately"
], ans=3,
   why="Research-methods item. Social desirability is the standard threat to self-report validity. Subjective interpretation is the criticism of PROJECTIVE tests, not of standardized inventories, and is the distractor to beat."),

 dict(q="A critic argues that trait theory struggles to explain why a person is talkative at home and reserved at work. The strongest response available to a trait theorist is that", choices=[
   "traits are fixed at birth and cannot vary with context",
   "the person must have been misclassified by the inventory",
   "situations have no measurable effect on behavior",
   "traits describe a person's average tendency across many situations rather than their behavior on any single occasion"
], ans=3,
   why="EK 4.5.B.1 defines traits as enduring characteristics leading to TYPICAL responses. Typical is an aggregate claim, so situational variation around an average does not contradict it -- while the other options defend positions trait theory does not hold."),

 dict(q="The clearest difference between the trait and social-cognitive accounts of personality is that", choices=[
   "trait theory emphasizes the environment, while social-cognitive theory emphasizes inherited characteristics",
   "trait theory studies unconscious material, while social-cognitive theory studies conscious material",
   "trait theory applies to adults, while social-cognitive theory applies to children",
   "trait theory describes stable characteristics a person carries across settings, while social-cognitive theory emphasizes the ongoing interplay of person, behavior, and environment"
], ans=3,
   why="EK 4.5.B.1 defines traits as enduring characteristics; EK 4.5.A.1 puts reciprocal influence at the center of the social-cognitive account. Neither theory is about unconscious material, which belongs to Topic 4.4."),

 dict(q="A researcher reports that conscientiousness scores correlate positively with workplace performance ratings across many occupations. The strongest conclusion available from this evidence is that", choices=[
   "being conscientious causes better job performance",
   "employers should hire only applicants scoring high in conscientiousness",
   "performance ratings cause people to become more conscientious",
   "higher conscientiousness scores are associated with higher performance ratings"
], ans=3,
   why="Research-methods item (Science Practice 2.C). A correlation supports an associational statement only; neither causal direction is established, and a hiring policy is a recommendation the data cannot license."),

 dict(q="To test whether a brief training program raises self-efficacy for public speaking, the strongest design would", choices=[
   "measure self-efficacy in people who have already chosen to take the training",
   "interview graduates of the training about how it helped them",
   "compare self-efficacy scores of speakers with a large audience against those with a small one",
   "randomly assign volunteers to the training or to a comparison activity and compare self-efficacy scores afterward"
], ans=3,
   why="Research-methods item (Science Practice 2.B). Random assignment to a manipulated condition with a comparison group is what permits a causal claim; the self-selected and retrospective options both leave the groups differing before the training began."),

 dict(q="A first-year employee is given a small project, succeeds, and is then trusted with larger ones, each success raising her confidence and drawing further opportunities. A social-cognitive theorist would emphasize that", choices=[
   "her behavior, her beliefs about her capability, and the opportunities her environment offers are shaping one another",
   "an enduring trait present since childhood is simply becoming visible",
   "an unconscious conflict is being resolved through her work",
   "the environment alone accounts for the change, with her beliefs playing no role"], ans=0,
   why="EK 4.5.A.1. This is reciprocal determinism with self-efficacy as the personal factor: performance changes belief, belief changes behavior, and behavior changes what the environment offers next."),

 dict(q="Two people score identically on a trait inventory but behave very differently at a large party. Social-cognitive theory would explain the difference primarily by pointing to", choices=[
   "differences in the unconscious conflicts each person carries",
   "an error in the inventory, since identical scores must produce identical behavior",
   "differences in inherited temperament that traits fail to capture",
   "differences in what each person expects will happen and how each has learned to act in that setting"
], ans=3,
   why="EK 4.5.A.1. The social-cognitive account gives personal cognition and the specific environment a causal role alongside disposition, so equal trait scores need not produce equal behavior in a particular setting."),

 dict(q="Which finding would most directly WEAKEN a strict trait account of personality?", choices=[
   "People who score high in conscientiousness are rated as dependable by their coworkers",
   "A person's behavior is predicted far better by the specific situation than by their trait scores",
   "Trait scores measured in adolescence correlate strongly with trait scores measured in adulthood",
   "Factor analysis of a new inventory recovers five dimensions in several countries"
], ans=1,
   why="Argumentation item (Science Practice 4.B). EK 4.5.B.1 claims enduring characteristics produce typical responses, so evidence that situations predict behavior better than dispositions cuts against it; the other three findings all support the trait account."),

 dict(q="A workplace program that helps employees build confidence in specific job skills, and also redesigns the tasks those employees are given, is intervening on", choices=[
   "both the personal and the environmental components of reciprocal determinism",
   "the personal component only, since confidence is internal",
   "the environmental component only, since tasks are external",
   "neither component, since reciprocal determinism cannot be influenced deliberately"], ans=0,
   why="EK 4.5.A.1 names person, behavior, and environment as mutually influencing. Building task-specific confidence targets the personal factor and redesigning tasks targets the environment, so the program acts on both at once."),
]
