# AP PSYCH 5.2 Positive Psychology — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, p. 116.
# EK 5.2.A.1 positive psychology seeks to identify factors that lead to
#   well-being, resilience, positive emotions, and psychological health;
# EK 5.2.B.1 expressing gratitude increases subjective well-being;
# EK 5.2.B.2 people who exercise their signature strengths or virtues report
#   higher happiness and subjective well-being; the classification of character
#   strengths is built around SIX categories of virtues -- wisdom, courage,
#   humanity, justice, temperance, and transcendence;
# EK 5.2.B.3 posttraumatic growth may result after the experience of trauma or
#   stress.
#
# Positive psychology is NEW in the redesigned framework -- the pre-2024 course
# did not contain it -- so older test-prep material offers nothing to check
# against here.
#
# TONE: EK 5.2.B.3 says posttraumatic growth MAY result. Items are written so
# that nothing implies growth is guaranteed, expected of anyone, or a reason to
# regard trauma as beneficial; one item tests that precision directly.
#
# No sympy: every key's claim is stated item by item in verify_p5_2.py.
TOPIC = ("5.2", "Positive Psychology", 5)
QUESTIONS = [
 dict(q="Positive psychology is best described as the study of", choices=[
   "the biological basis of sensation and perception",
   "the factors that lead to well-being, resilience, positive emotions, and psychological health",
   "the classification and diagnosis of psychological disorders",
   "the unconscious conflicts that shape personality"
], ans=1,
   why="EK 5.2.A.1, in substance verbatim: positive psychology seeks to identify factors that lead to well-being, resilience, positive emotions, and psychological health."),

 dict(q="Positive psychology differs from much of the rest of clinical psychology mainly in that it asks", choices=[
   "which medications are most effective for depression",
   "what makes people function well, rather than only what goes wrong",
   "whether psychological disorders exist at all",
   "how to classify disorders more precisely"
], ans=1,
   why="EK 5.2.A.1 defines the field by what it seeks: the factors producing well-being and psychological health. The shift is in the QUESTION asked, not a denial that disorders exist -- an important distinction given the field's aims."),

 dict(q="Resilience, one of the outcomes positive psychology studies, refers to", choices=[
   "the ability to avoid stressful situations entirely",
   "a permanent immunity to psychological disorder",
   "the capacity to adapt and recover in the face of adversity",
   "the tendency never to experience negative emotion"
], ans=2,
   why="EK 5.2.A.1 names resilience among the outcomes the field studies. Resilience is about recovery and adaptation under adversity, not about escaping adversity or never feeling distress."),

 dict(q="Subjective well-being refers to", choices=[
   "a person's measured physical health status",
   "the absence of any diagnosable psychological disorder",
   "a person's own evaluation of their life satisfaction and emotional experience",
   "an observer's rating of how well a person appears to be doing"
], ans=2,
   why="EK 5.2.B.1 and 5.2.B.2 both use subjective well-being as an outcome. The word subjective marks it as the person's OWN appraisal, which is what distinguishes it from an observer rating or a health measure."),

 dict(q="According to the framework, expressing gratitude", choices=[
   "has no measurable effect on well-being",
   "only affects well-being in people already experiencing distress",
   "increases subjective well-being",
   "decreases subjective well-being by drawing attention to dependence on others"
], ans=2,
   why="EK 5.2.B.1 states it directly: expressing gratitude, a positive subjective experience, increases subjective well-being."),

 dict(q="A person who ends each day by writing down three things she is thankful for and reports feeling more satisfied with her life over the following weeks illustrates", choices=[
   "the exercise of the virtue of justice",
   "resilience in the face of a specific trauma",
   "the effect of expressing gratitude on subjective well-being",
   "posttraumatic growth following adversity"
], ans=2,
   why="EK 5.2.B.1. The practice is the deliberate expression of gratitude and the reported outcome is raised life satisfaction, which is the framework's claim. Nothing in the stem involves trauma or a fairness-related strength."),

 dict(q="Signature strengths are best described as", choices=[
   "the weaknesses a person most needs to correct",
   "the character strengths most central to a particular person",
   "the skills a person has been formally trained in",
   "the traits an employer values most in any employee"
], ans=1,
   why="EK 5.2.B.2 refers to people who exercise THEIR signature strengths or virtues, which marks them as the strengths characteristic of that individual rather than a universal list or a set of trained skills."),

 dict(q="According to the framework, people who regularly exercise their signature strengths or virtues report", choices=[
   "lower levels of happiness because of the effort required",
   "higher income but not greater happiness",
   "higher levels of happiness and subjective well-being",
   "no change in happiness compared with people who do not"
], ans=2,
   why="EK 5.2.B.2 states that people who exercise their signature strengths or virtues report higher levels of positive experiences such as happiness and subjective well-being."),

 dict(q="The classification of character strengths used in positive psychology is organized around how many categories of virtues?", choices=[
   "ten",
   "six",
   "three",
   "five"
], ans=1,
   why="EK 5.2.B.2 states the classification has been developed around SIX categories of virtues: wisdom, courage, humanity, justice, temperance, and transcendence."),

 dict(q="Which set correctly names the six categories of virtues in this classification?", choices=[
   "wisdom, ambition, humanity, justice, temperance, creativity",
   "loyalty, courage, humanity, justice, temperance, transcendence",
   "wisdom, courage, humanity, justice, temperance, transcendence",
   "wisdom, courage, humility, justice, patience, transcendence"
], ans=2,
   why="EK 5.2.B.2 names exactly these six. Humility, patience, ambition, creativity, and loyalty are not category names in the classification, though several are strengths that fall WITHIN a category."),

 dict(q="A person known for curiosity, love of learning, and sound judgment is exercising strengths belonging to which virtue category?", choices=[
   "courage",
   "temperance",
   "justice",
   "wisdom"
], ans=3,
   why="EK 5.2.B.2 names wisdom among the six categories; curiosity, love of learning, and judgment are knowledge-related strengths that fall under it."),

 dict(q="A person who persists at a difficult goal despite repeated setbacks and speaks honestly when it is costly to do so is exercising strengths belonging to which virtue category?", choices=[
   "humanity",
   "wisdom",
   "courage",
   "temperance"
], ans=2,
   why="EK 5.2.B.2 names courage among the six categories; perseverance and honesty in the face of cost are strengths of courage rather than of restraint or of interpersonal warmth."),

 dict(q="A person consistently noted for kindness and for reading other people's feelings accurately is exercising strengths belonging to which virtue category?", choices=[
   "justice",
   "courage",
   "transcendence",
   "humanity"
], ans=3,
   why="EK 5.2.B.2 names humanity among the six categories; kindness and social intelligence are its characteristic strengths. Justice concerns fairness in the treatment of groups, which is a different focus."),

 dict(q="A person known for treating everyone fairly, working well on a team, and leading a group equitably is exercising strengths belonging to which virtue category?", choices=[
   "humanity",
   "temperance",
   "wisdom",
   "justice"
], ans=3,
   why="EK 5.2.B.2 names justice among the six categories; fairness, teamwork, and leadership are its characteristic strengths. Humanity concerns one-to-one warmth, while justice concerns the person's conduct within groups."),

 dict(q="A person noted for forgiveness, self-regulation, and restraint from excess is exercising strengths belonging to which virtue category?", choices=[
   "courage",
   "justice",
   "humanity",
   "temperance"
], ans=3,
   why="EK 5.2.B.2 names temperance among the six categories; forgiveness, humility, prudence, and self-regulation are the strengths that protect against excess."),

 dict(q="A person noted for a deep appreciation of beauty, an enduring sense of hope, and a feeling of connection to something larger than themselves is exercising strengths belonging to which virtue category?", choices=[
   "transcendence",
   "wisdom",
   "temperance",
   "justice"], ans=0,
   why="EK 5.2.B.2 names transcendence among the six categories; appreciation of beauty and excellence, hope, and a sense of connection to something larger are its characteristic strengths."),

 dict(q="Posttraumatic growth refers to", choices=[
   "the return to exactly the level of functioning present before a trauma",
   "the absence of any distress following a traumatic event",
   "positive psychological change that may follow the experience of trauma or stress",
   "the gradual fading of traumatic memories over time"
], ans=2,
   why="EK 5.2.B.3: posttraumatic growth, a positive subjective experience, MAY result after the experience of trauma or stress. It is a change beyond the prior baseline, not a fading of memory or a simple return to it."),

 dict(q="What is the clearest difference between resilience and posttraumatic growth?", choices=[
   "Resilience is recovering to prior functioning, while posttraumatic growth involves positive change beyond that prior level",
   "Resilience involves positive change beyond prior functioning, while posttraumatic growth is a return to it",
   "Resilience occurs only in adults, while posttraumatic growth occurs only in children",
   "Resilience is measured physiologically, while posttraumatic growth cannot be measured"], ans=0,
   why="EK 5.2.A.1 names resilience and EK 5.2.B.3 names posttraumatic growth as separate constructs. Bouncing back is not the same as being changed for the better, and the reversed statement is the trap."),

 dict(q="A person who, in the years after a serious illness, reports a changed sense of priorities and closer relationships than before is describing", choices=[
   "the resistance phase of the general adaptation syndrome",
   "an emotion-focused coping strategy",
   "the exercise of a signature strength of justice",
   "posttraumatic growth"
], ans=3,
   why="EK 5.2.B.3. The reported change goes beyond the prior baseline and follows a serious stressor, which is what the construct names."),

 dict(q="Which statement about posttraumatic growth is most accurate given the framework's wording?", choices=[
   "Anyone who does not experience growth after trauma has coped incorrectly",
   "Trauma should be sought out because of the growth it can produce",
   "Growth may follow trauma for some people, but trauma is not thereby beneficial and growth is not expected of anyone",
   "Trauma reliably produces growth in nearly everyone who experiences it"
], ans=2,
   why="EK 5.2.B.3 says growth MAY result -- a possibility, not a rule. Reading it as an expectation turns a finding about some people into a standard others are judged against, which the framework's hedged wording does not support and which would be harmful in a clinical setting."),

 dict(q="Positive psychology's relationship to the treatment of psychological disorders is best described as", choices=[
   "identical, since well-being is simply the absence of symptoms",
   "complementary, since building well-being addresses a question distinct from reducing symptoms",
   "a replacement, since building well-being makes treatment of disorders unnecessary",
   "unrelated, since well-being and disorder have nothing in common"
], ans=1,
   why="EK 5.2.A.1 defines the field by the factors producing well-being and psychological health. Raising well-being and reducing symptoms are different targets, so the field adds to rather than substitutes for treatment -- and well-being is not merely the absence of disorder."),

 dict(q="To test whether a gratitude practice raises well-being, the strongest design would be to", choices=[
   "ask people who already keep gratitude journals how happy they are",
   "compare the well-being of people who describe themselves as grateful with those who do not",
   "interview people about whether they think gratitude would help them",
   "randomly assign participants to a gratitude-journaling condition or a neutral-writing condition and compare well-being scores afterward"
], ans=3,
   why="Research-methods item (Science Practice 2.B). Random assignment to a manipulated condition with an active comparison group is what licenses a causal claim; every other option leaves grateful and non-grateful participants differing before the study began."),

 dict(q="A study reports that people scoring higher on a strengths inventory also report higher life satisfaction. The strongest conclusion available is that", choices=[
   "exercising strengths causes higher life satisfaction",
   "life satisfaction causes people to develop strengths",
   "the two variables are unrelated",
   "strengths scores and life satisfaction are associated in this sample"
], ans=3,
   why="Research-methods item (Science Practice 2.C). Both variables were measured rather than manipulated, so only an association is established; EK 5.2.B.2's own wording is likewise that people 'report' higher levels."),

 dict(q="A limitation of measuring well-being entirely by self-report is that", choices=[
   "responses may reflect what participants think they should say as well as how they actually feel",
   "well-being cannot be expressed as a number",
   "self-reports can only be collected in a laboratory",
   "well-being is not a psychological variable"], ans=0,
   why="Research-methods item. Self-report is subject to social desirability. Note this is a limitation and not a fatal objection -- subjective well-being is BY DEFINITION the person's own appraisal (EK 5.2.B.1), so self-report cannot simply be replaced by an observer measure."),

 dict(q="Which finding would most directly SUPPORT the claim that expressing gratitude raises subjective well-being?", choices=[
   "Most people say they believe gratitude is important",
   "Grateful people are rated as more likeable by others",
   "Participants randomly assigned to write weekly gratitude letters report higher well-being afterward than those assigned to write about daily events",
   "People who report being happy also report feeling grateful"
], ans=2,
   why="Argumentation item (Science Practice 4.B). EK 5.2.B.1 makes a causal claim, so supporting evidence needs a manipulation with random assignment and a comparison condition. The other findings are correlational, attitudinal, or about a different outcome entirely."),

 dict(q="Which finding would most directly WEAKEN the claim that exercising signature strengths raises well-being?", choices=[
   "People high in strengths also report strong social networks",
   "Strengths inventories produce consistent scores when retaken",
   "Different cultures emphasize different strengths",
   "Participants randomly assigned to use their top strengths daily show no more improvement in well-being than a comparison group"
], ans=3,
   why="Argumentation item (Science Practice 4.B). A well-controlled manipulation producing no advantage over a comparison group cuts directly against the causal claim. Consistent retest scores speak to reliability, and cultural variation in emphasis does not bear on whether exercising one's own strengths helps."),

 dict(q="A student loses a season to injury, works steadily through rehabilitation, and returns to her previous level of play with her outlook unchanged. This is best described as", choices=[
   "posttraumatic growth",
   "eustress",
   "the exercise of the virtue of transcendence",
   "resilience"
], ans=3,
   why="EK 5.2.A.1 names resilience; EK 5.2.B.3 names posttraumatic growth. The stem specifies a return to the PREVIOUS level with an unchanged outlook, which is recovery rather than change beyond baseline."),

 dict(q="A person reports no diagnosable disorder but also little sense of purpose, engagement, or satisfaction. Positive psychology would regard this as evidence that", choices=[
   "the absence of disorder guarantees psychological health",
   "well-being is more than the absence of disorder and is worth studying in its own right",
   "the person must have an undiagnosed disorder",
   "well-being cannot be assessed in people without disorders"
], ans=1,
   why="EK 5.2.A.1 makes well-being and psychological health the objects of study, which presupposes they are not simply what remains when symptoms are subtracted. This case is the standard illustration of that gap."),

 dict(q="A person thanks a mentor in a detailed letter describing the specific difference the mentor made. According to the framework this action is expected to", choices=[
   "affect the recipient's well-being but not the writer's",
   "have an effect only if the mentor replies",
   "increase the writer's own subjective well-being",
   "decrease the writer's well-being by creating a sense of obligation"
], ans=2,
   why="EK 5.2.B.1 attributes the increase in subjective well-being to EXPRESSING gratitude, so the benefit accrues to the person expressing it and does not depend on the recipient's response."),

 dict(q="A wellness program that helps participants identify their characteristic strengths, build a gratitude practice, and develop skills for recovering from setbacks is targeting which set of outcomes?", choices=[
   "well-being, positive emotions, and resilience",
   "the diagnostic criteria for a specific disorder",
   "the reduction of medication side effects",
   "the accuracy of participants' self-assessments"], ans=0,
   why="EK 5.2.A.1 names well-being, resilience, positive emotions, and psychological health as what positive psychology seeks to produce, and each program component maps onto one: strengths (EK 5.2.B.2), gratitude (EK 5.2.B.1), and recovery from setbacks (resilience)."),
]
