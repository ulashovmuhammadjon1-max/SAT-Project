# AP PSYCH 4.6 Motivation — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 103-104.
# EK 4.6.A.1 drive-reduction theory (homeostasis) and arousal theory
#   (optimal arousal, the Yerkes-Dodson Law);
# EK 4.6.A.2 self-determination theory (intrinsic vs extrinsic) and incentive theory;
# EK 4.6.A.3 instincts in non-human animals, and that humans do not seem to
#   demonstrate instinctual behavior or mental processes;
# EK 4.6.A.4 Lewin's motivational conflicts theory: approach-approach,
#   approach-avoidance, avoidance-avoidance;
# EK 4.6.A.5 sensation-seeking theory: experience seeking, thrill or adventure
#   seeking, disinhibition, boredom susceptibility;
# EK 4.6.B.1 eating -- ghrelin and leptin, regulated by the hypothalamus via the
#   pituitary gland -- plus external factors.
#
# SCOPE: Maslow's hierarchy of needs is excluded by EK 4.4.B.1 and does not
# appear here, even though older material routinely teaches it as the centrepiece
# of the motivation unit. Unlike the theories of EMOTION in 4.7, the motivation
# theories above ARE named in the required content, so items may key on their
# names.
#
# No sympy: every key's claim is stated item by item in verify_p4_6.py.
TOPIC = ("4.6", "Motivation", 4)
QUESTIONS = [
 dict(q="Drive-reduction theory explains motivation as the result of", choices=[
   "an inherited fixed pattern of behavior released by a specific stimulus",
   "a physiological need creating a drive that behavior acts to reduce, restoring homeostasis",
   "a search for the level of stimulation a person finds most comfortable",
   "the pull of rewards available in the environment"
], ans=1,
   why="EK 4.6.A.1: drive-reduction theory addresses how certain behaviors help maintain homeostasis. Need creates drive, and the behavior that reduces the drive is the motivated one."),

 dict(q="A hiker who has not drunk anything for hours begins searching intently for a water source. Drive-reduction theory explains this behavior as", choices=[
   "action aimed at restoring the body's internal balance",
   "the pursuit of an optimal level of physiological arousal",
   "an intrinsically motivated activity pursued for its own sake",
   "a fixed action pattern triggered by the sight of terrain"], ans=0,
   why="EK 4.6.A.1. Dehydration is a departure from homeostasis, the resulting drive energizes behavior, and drinking reduces it -- the exact sequence drive-reduction theory describes."),

 dict(q="Arousal theory differs from drive-reduction theory principally in claiming that people", choices=[
   "act to eliminate all physiological arousal whenever possible",
   "have no stable motivational tendencies across situations",
   "seek an optimal level of arousal, which can mean increasing stimulation rather than reducing it",
   "are motivated only by biological needs such as hunger and thirst"
], ans=2,
   why="EK 4.6.A.1: arousal theory addresses how people seek an OPTIMAL level of arousal. That is why drive-reduction theory cannot explain curiosity or thrill-seeking, where people deliberately raise stimulation."),

 dict(q="According to the Yerkes-Dodson Law, performance is generally best at", choices=[
   "a moderate level of arousal",
   "the lowest level of arousal a person can achieve",
   "the highest level of arousal a person can tolerate",
   "a level of arousal that does not vary with the task"], ans=0,
   why="EK 4.6.A.1 cites the Yerkes-Dodson Law as the demonstration of optimal arousal: the relationship is an inverted U, so performance falls off at both very low and very high arousal."),

 dict(q="The Yerkes-Dodson Law also predicts that the arousal level producing the best performance", choices=[
   "matters only for physical tasks, not mental ones",
   "is lower for difficult or unfamiliar tasks than for simple, well-practiced ones",
   "is higher for difficult tasks than for simple ones",
   "is identical for every task a person performs"
], ans=1,
   why="EK 4.6.A.1. The refinement students most often miss: the optimum shifts with task difficulty. A complex task is disrupted by arousal that would still help performance on an easy, well-learned one."),

 dict(q="A person who takes up rock climbing, describing the fear itself as the appeal, is best explained by", choices=[
   "arousal theory, because the person is raising stimulation toward a preferred level",
   "drive-reduction theory, because the climb reduces a physiological need",
   "incentive theory, because a tangible reward is offered for climbing",
   "instinct theory, because climbing is an inherited fixed pattern"], ans=0,
   why="EK 4.6.A.1. Deliberately INCREASING arousal is precisely what drive-reduction theory cannot accommodate, and it is the observation arousal theory was formulated to handle."),

 dict(q="Intrinsic motivation refers to engaging in an activity", choices=[
   "for the satisfaction of the activity itself",
   "in order to obtain a reward or avoid a punishment",
   "only when a physiological need is present",
   "because an authority figure has instructed you to"], ans=0,
   why="EK 4.6.A.2: self-determination theory proposes people are motivated by intrinsic (internal) or extrinsic (external) motivations; intrinsic motivation arises from the activity itself."),

 dict(q="Extrinsic motivation refers to engaging in an activity", choices=[
   "purely for the interest or enjoyment it provides",
   "because it restores the body to homeostasis",
   "because it produces an optimal level of arousal",
   "to obtain an outcome separate from the activity, such as a reward or a grade"
], ans=3,
   why="EK 4.6.A.2. Extrinsic motivation is driven by consequences external to the activity; EK 4.6.A.2 names rewards specifically as an extrinsic motivation."),

 dict(q="A student who reads history books in her free time because she finds the subject fascinating, and a classmate who reads them only to raise his course grade, differ in that", choices=[
   "the first is intrinsically motivated and the second extrinsically motivated",
   "the first is extrinsically motivated and the second intrinsically motivated",
   "the first is responding to a drive and the second to an instinct",
   "the first has higher arousal and the second lower arousal"], ans=0,
   why="EK 4.6.A.2. The discriminator is where the satisfaction lies: in the activity itself, or in a separable outcome the activity secures."),

 dict(q="Incentive theory explains motivation by pointing to", choices=[
   "an inherited response released by a particular stimulus",
   "the pull of external rewards available in the environment",
   "the push of an internal physiological need",
   "the level of stimulation a person finds most comfortable"
], ans=1,
   why="EK 4.6.A.2 states that incentive theory explores the role of rewards, an extrinsic motivation, in motivating behavior. It is a pull account, in contrast to the push of a drive."),

 dict(q="Children who already enjoy drawing are given a certificate every time they draw. When the certificates stop, they draw less than children who were never given any. This result suggests that", choices=[
   "the children's arousal level was too low during the reward period",
   "an external reward can weaken motivation that was previously intrinsic",
   "external rewards always strengthen the behavior they follow",
   "the children never found drawing interesting to begin with"
], ans=1,
   why="EK 4.6.A.2 sets intrinsic against extrinsic motivation and names rewards as extrinsic. Once the activity is reframed as something done FOR the certificate, removing the certificate removes the reason -- which a pure reinforcement account would not predict."),

 dict(q="What does the AP Psychology framework say about instinct as an explanation of human behavior?", choices=[
   "Many non-human animals are motivated by instincts, but humans do not appear to demonstrate instinctual behavior",
   "Instincts explain most human motivation, particularly hunger and thirst",
   "Instincts are found in humans but not in other animals",
   "Instincts are learned patterns acquired through repeated reinforcement"], ans=0,
   why="EK 4.6.A.3 states this directly: instincts are innate, typically fixed patterns of behavior in animals in response to certain stimuli, and humans do not seem to demonstrate instinctual behavior or mental processes. The final option contradicts the definition, since an instinct is innate rather than learned."),

 dict(q="A graduate must choose between two job offers she finds equally attractive. According to Lewin's motivational conflicts theory this is", choices=[
   "not a motivational conflict, since both outcomes are positive",
   "an approach-approach conflict",
   "an avoidance-avoidance conflict",
   "an approach-avoidance conflict"
], ans=1,
   why="EK 4.6.A.4. Two desirable options and only one can be taken: approach-approach. It is still a conflict, because choosing one forfeits the other, though it is typically the least distressing of the three."),

 dict(q="A homeowner must either pay for an expensive roof repair or accept ongoing water damage, and finds both prospects unpleasant. This is", choices=[
   "an avoidance-avoidance conflict",
   "an approach-approach conflict",
   "an approach-avoidance conflict",
   "a social trap"], ans=0,
   why="EK 4.6.A.4. Two undesirable options with no attractive alternative is avoidance-avoidance, the conflict most associated with delay and attempts to escape the choice entirely."),

 dict(q="A candidate is offered a promotion that brings higher pay along with much longer hours and relocation. This single option that is both attractive and unattractive creates", choices=[
   "an approach-approach conflict",
   "an avoidance-avoidance conflict",
   "cognitive dissonance about the current job",
   "an approach-avoidance conflict"
], ans=3,
   why="EK 4.6.A.4. Approach-avoidance involves ONE goal carrying both positive and negative features, which is what distinguishes it from the other two conflicts, each of which involves two separate options."),

 dict(q="What is the structural difference between an approach-avoidance conflict and the other two conflicts Lewin's theory describes?", choices=[
   "Approach-avoidance involves a single option with both positive and negative features, while the others involve a choice between two separate options",
   "Approach-avoidance involves two options, while the others involve a single option",
   "Approach-avoidance is the only conflict that can be resolved",
   "Approach-avoidance occurs only in the workplace"], ans=0,
   why="EK 4.6.A.4 names all three. Counting the options is the fastest reliable test: two attractive, two unattractive, or one mixed."),

 dict(q="Sensation-seeking theory proposes that motivation is grounded in", choices=[
   "the reduction of unmet physiological needs",
   "the size of the reward a behavior is expected to produce",
   "the unconscious conflicts a person carries from childhood",
   "a person's level of need for varied or novel experiences"
], ans=3,
   why="EK 4.6.A.5 states it directly: sensation-seeking theory proposes that one's level of need for varied or novel experiences is the basis of motivation."),

 dict(q="A person who takes up skydiving and whitewater rafting specifically for the physical risk involved is displaying which type of sensation seeking?", choices=[
   "thrill or adventure seeking",
   "experience seeking",
   "disinhibition",
   "boredom susceptibility"], ans=0,
   why="EK 4.6.A.5 names four types. Thrill or adventure seeking is the pursuit of risky PHYSICAL activity, which is what both examples are."),

 dict(q="A person who travels to unfamiliar countries, seeks out unusual art, and prefers an unconventional lifestyle is displaying which type of sensation seeking?", choices=[
   "disinhibition",
   "boredom susceptibility",
   "experience seeking",
   "thrill or adventure seeking"
], ans=2,
   why="EK 4.6.A.5. Experience seeking pursues novelty through the mind and senses -- travel, art, unconventional living -- rather than through physical risk."),

 dict(q="A person who becomes restless and irritable when a task is repetitive and unvarying is displaying which type of sensation seeking?", choices=[
   "disinhibition",
   "boredom susceptibility",
   "experience seeking",
   "thrill or adventure seeking"
], ans=1,
   why="EK 4.6.A.5. Boredom susceptibility is a low tolerance for repetition and monotony; it is defined by the aversive reaction to sameness rather than by an appetite for any particular activity."),

 dict(q="Among the four types of sensation seeking, disinhibition refers to seeking stimulation through", choices=[
   "an intolerance for repetitive tasks",
   "uninhibited social activity and release of ordinary restraints",
   "risky physical activities such as climbing or diving",
   "novel travel and unconventional living"
], ans=1,
   why="EK 4.6.A.5 names disinhibition as one of the four types; it is the social-behavioral form, marked by loosened restraint in social settings, as opposed to the other three."),

 dict(q="Ghrelin contributes to the regulation of eating by", choices=[
   "increasing feelings of hunger",
   "signaling that the body has had enough to eat",
   "slowing the rate at which the stomach empties",
   "converting stored fat into usable energy"], ans=0,
   why="EK 4.6.B.1.i names ghrelin and leptin as hormones regulating hunger and satiety. Ghrelin is the hunger signal; reversing the two hormones is the single most common error on this content."),

 dict(q="Leptin contributes to the regulation of eating by", choices=[
   "raising body temperature after a meal",
   "signaling satiety, which reduces further food intake",
   "signaling hunger, which prompts food seeking",
   "triggering the release of digestive enzymes"
], ans=1,
   why="EK 4.6.B.1.i. Leptin is the satiety signal, the counterpart to ghrelin's hunger signal."),

 dict(q="Which brain structure does the AP Psychology framework identify as regulating the hormones involved in hunger and satiety?", choices=[
   "the hypothalamus, acting via the pituitary gland",
   "the hippocampus, acting via the thalamus",
   "the cerebellum, acting via the brainstem",
   "the amygdala, acting via the corpus callosum"], ans=0,
   why="EK 4.6.B.1.i states parenthetically that ghrelin and leptin are regulated by the hypothalamus via the pituitary gland."),

 dict(q="What is the clearest functional difference between ghrelin and leptin?", choices=[
   "Ghrelin is a neurotransmitter while leptin is a neurotransmitter of the same type",
   "Ghrelin promotes eating while leptin suppresses it",
   "Ghrelin suppresses eating while leptin promotes it",
   "Ghrelin acts during the day and leptin only during sleep"
], ans=1,
   why="EK 4.6.B.1.i. The two hormones act in opposite directions on food intake, which is exactly why an item that reverses them is so hard to catch by feel."),

 dict(q="A person who has just finished a large meal eats several slices of cake because it is a colleague's birthday and everyone is sharing it. This behavior most directly illustrates", choices=[
   "an approach-avoidance conflict about the cake",
   "the influence of external factors on eating",
   "a rise in circulating ghrelin",
   "a failure of the pituitary gland to release leptin"
], ans=1,
   why="EK 4.6.B.1.ii: external factors like the presence of food, time of day, or social gatherings around meals also influence the behavior of eating. The person is full, so the internal hunger signal is not what is driving the behavior."),

 dict(q="Which of the following is the best operational definition of 'motivation to exercise' for use in a study?", choices=[
   "the participant's underlying drive toward physical fitness",
   "whether the participant has a naturally athletic disposition",
   "the number of minutes a participant spends exercising during a recorded two-week period",
   "how much a participant genuinely wants to be healthy"
], ans=2,
   why="Research-methods item (Science Practice 2.B). An operational definition states the specific, observable procedure by which a variable is measured. The other three restate the construct in words that specify no measurement."),

 dict(q="A researcher wants to know whether paying people to complete puzzles changes how long they keep working on puzzles once payment ends. The strongest design would be to", choices=[
   "randomly assign participants to a paid or unpaid condition, then measure puzzle time in a later free-choice period with no payment available",
   "pay everyone and compare how long each person works during the paid period",
   "ask people who enjoy puzzles whether payment would change their interest",
   "compare people who have accepted paid puzzle work with people who have not"], ans=0,
   why="Research-methods item (Science Practice 2.B). The question is about behavior AFTER payment stops, so a free-choice measure taken with no reward available is the only measure that answers it, and random assignment is what makes the comparison causal."),

 dict(q="An employee finds her work genuinely interesting, is paid well for it, must choose between two appealing projects, and performs best under moderate deadline pressure. Which theory best explains the deadline observation specifically?", choices=[
   "Lewin's motivational conflicts theory",
   "arousal theory",
   "self-determination theory",
   "incentive theory"
], ans=1,
   why="Each clause maps to a different theory, and the question asks about only one. Performance peaking at moderate pressure is the inverted-U of arousal theory and the Yerkes-Dodson Law (EK 4.6.A.1); the other three clauses belong to the other three theories named."),

 dict(q="Which observation would most directly challenge drive-reduction theory as a complete account of motivation?", choices=[
   "Animals eat more when food is more readily available",
   "Animals stop eating once they are full",
   "Well-fed, comfortable animals will work to explore a novel environment with no reward available",
   "Animals deprived of water will press a lever to obtain it"
], ans=2,
   why="Argumentation item (Science Practice 4.B). Drive-reduction theory explains behavior as the reduction of an existing need, so behavior in the ABSENCE of any unmet need and with no reward is what it cannot account for -- and it is the observation arousal theory addresses (EK 4.6.A.1). The other three findings are consistent with drive reduction."),
]
