# AP PSYCHOLOGY 2.8 Intelligence and Achievement — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition.
# Learning objectives 2.8.A (how modern and historical theories describe
# intelligence), 2.8.B (how intelligence is measured), 2.8.C (how systemic issues
# relate to the uses of intelligence assessments), 2.8.D (achievement compared to
# intelligence).
#
# Essential knowledge relied on: 2.8.A.1 consensus on defining and measuring
# intelligence remains elusive and can be subject to bias, and researchers debate
# whether intelligence is a general ability (g) or multiple abilities; 2.8.B.1
# early tests yielded an IQ dividing mental age by chronological age, and modern
# IQ scores are often used to identify students for educational services;
# 2.8.B.2 psychometric principles, with 2.8.B.2.i standardization (consistent
# procedures and environments), 2.8.B.2.ii validity -- construct and predictive --
# and 2.8.B.2.iii reliability -- test-retest and split-half; 2.8.B.3
# socio-culturally responsive assessment, stereotype threat, stereotype lift;
# 2.8.C.1 the Flynn effect and the societal factors behind it; 2.8.C.2 IQ varying
# more WITHIN groups than BETWEEN them, and poverty, discrimination, and
# educational inequities depressing scores; 2.8.C.3 the historical use of test
# scores to limit access to jobs, military ranks, educational institutions, and
# immigration to the US; 2.8.D.1 achievement tests (what someone knows) versus
# aptitude tests (predicting future performance); 2.8.D.2 fixed versus growth
# mindset.
#
# EXCLUSION STATEMENT respected, and it constrains this topic more than any other
# in Units 1-3: EK 2.8.B.1 places LABELING OR DESCRIBING cognitive abilities and
# disabilities outside the scope of the exam. No item names, defines, or asks a
# student to identify any category of cognitive ability or disability, and no
# score range is attached to any label.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_8.py.
TOPIC = ("2.8", "Intelligence and Achievement", 2)
QUESTIONS = [
 dict(q="According to the AP Psychology framework, consensus among researchers about how to define and measure intelligence", choices=[
   "continues to be elusive and can be subject to bias",
   "was settled early in the twentieth century",
   "exists for measurement but not for definition",
   "is unnecessary because intelligence cannot be measured at all"], ans=0,
   why="EK 2.8.A.1 states that throughout history, consensus about how to define and measure intelligence continues to be elusive and can be subject to bias."),
 dict(q="The debate referred to by the symbol g concerns whether intelligence is", choices=[
   "a single general ability or a set of multiple distinct abilities",
   "inherited or entirely learned",
   "measurable in children but not in adults",
   "the same as academic achievement"], ans=0,
   why="EK 2.8.A.1 states that researchers debate whether intelligence is a general ability, called g, or is comprised of multiple abilities."),
 dict(q="A researcher who argues that a person who performs well on one kind of mental task tends to perform well on others is defending", choices=[
   "the view that intelligence is a general ability",
   "the view that intelligence is comprised of multiple independent abilities",
   "the claim that intelligence tests are unreliable",
   "the claim that achievement and aptitude are identical"], ans=0,
   why="EK 2.8.A.1 frames the debate as general ability versus multiple abilities; consistent performance across different tasks is the observation the general-ability side rests on."),
 dict(q="Early formal intelligence tests produced an intelligence quotient calculated as", choices=[
   "mental age divided by chronological age",
   "chronological age divided by mental age",
   "the number of items answered correctly",
   "the difference between a person's score and the group mean"], ans=0,
   why="EK 2.8.B.1 states that early formal intelligence tests yielded an intelligence quotient which divided mental age by chronological age."),
 dict(q="According to the AP Psychology framework, modern IQ scores are often used to", choices=[
   "identify students for educational services",
   "assign employees to specific job titles",
   "determine which country a person may enter",
   "diagnose physical illnesses"], ans=0,
   why="EK 2.8.B.1 states that in modern times IQ scores are often used to identify students for educational services; the historical misuses in EK 2.8.C.3 are presented as misuses rather than as current purposes."),
 dict(q="A test is described as standardized when it is", choices=[
   "administered using consistent procedures and environments",
   "given to every student in a country",
   "scored by more than one person",
   "shown to predict future performance"], ans=0,
   why="EK 2.8.B.2.i states that a test is said to be standardized when it is administered using consistent procedures and environments."),
 dict(q="A test is considered valid when it", choices=[
   "measures what it is designed to measure",
   "yields similar results each time it is administered",
   "is administered the same way to everyone",
   "produces scores that are normally distributed"], ans=0,
   why="EK 2.8.B.2.ii states that a test is considered valid if it measures what it is designed to measure; consistency across administrations is reliability instead."),
 dict(q="A test is considered reliable when it", choices=[
   "yields similar results each time it is administered",
   "measures what it is designed to measure",
   "is free of any cultural content",
   "is short enough to be completed quickly"], ans=0,
   why="EK 2.8.B.2.iii states that a test is considered reliable if it yields similar results each time it is administered."),
 dict(q="Which statement correctly distinguishes validity from reliability?", choices=[
   "validity is whether a test measures the intended construct; reliability is whether it gives consistent results",
   "reliability is whether a test measures the intended construct; validity is whether it gives consistent results",
   "validity applies to intelligence tests and reliability to achievement tests",
   "the two terms describe the same property under different names"], ans=0,
   why="EK 2.8.B.2.ii and 2.8.B.2.iii define the two separately -- measuring the right thing versus measuring consistently -- and the first distractor is that definition reversed."),
 dict(q="A bathroom scale that reads exactly 12 pounds too heavy every single time is best described as", choices=[
   "reliable but not valid",
   "valid but not reliable",
   "both reliable and valid",
   "neither reliable nor valid"], ans=0,
   why="EK 2.8.B.2.iii's reliability is consistency across administrations, which a consistently wrong scale has; EK 2.8.B.2.ii's validity is measuring what it is designed to measure, which it does not."),
 dict(q="Test-retest reliability is established by", choices=[
   "giving the same test to the same people on two occasions and comparing the scores",
   "comparing scores on one half of a test with scores on the other half",
   "checking whether the test predicts later performance",
   "confirming that the test was administered in identical environments"], ans=0,
   why="EK 2.8.B.2.iii names test-retest and split-half as types of reliability; test-retest is the across-occasions method."),
 dict(q="Split-half reliability is established by", choices=[
   "comparing scores on one half of a test with scores on the other half",
   "giving the same test twice several weeks apart",
   "comparing the test against a different established test",
   "checking that the test measures the construct it names"], ans=0,
   why="EK 2.8.B.2.iii names split-half among the types of reliability; it compares two halves of a single administration rather than two separate administrations."),
 dict(q="Predictive validity is established by showing that a test", choices=[
   "forecasts later performance on the outcome it is meant to predict",
   "produces the same score when repeated",
   "captures the theoretical construct it claims to measure",
   "uses the same instructions for all test takers"], ans=0,
   why="EK 2.8.B.2.ii names construct and predictive validity as types of validity; the predictive type is defined by the test's relationship to a later outcome."),
 dict(q="Construct validity concerns whether a test", choices=[
   "actually captures the theoretical quality it claims to measure",
   "predicts a specific future outcome",
   "gives consistent scores across two administrations",
   "is administered under uniform conditions"], ans=0,
   why="EK 2.8.B.2.ii names construct validity as a type of validity; it concerns whether the test measures the construct itself, as opposed to whether it forecasts an outcome."),
 dict(q="Stereotype threat is best described as", choices=[
   "the impairment of performance that can occur when a person fears confirming a negative stereotype about a group they belong to",
   "the deliberate use of stereotypes to write test items",
   "the tendency of test scores to rise across generations",
   "the practice of administering a test under different conditions to different groups"], ans=0,
   why="EK 2.8.B.3 states that researchers strive to develop assessments that are socio-culturally responsive in order to reduce stereotype threat and potential inequity from stereotype lift."),
 dict(q="Stereotype lift is best described as", choices=[
   "a performance advantage that can arise from awareness of a negative stereotype about another group",
   "an improvement in test scores caused by practice",
   "the removal of culturally specific content from a test",
   "the rise in average IQ scores across the twentieth century"], ans=0,
   why="EK 2.8.B.3 pairs stereotype lift with stereotype threat as sources of potential inequity that socio-culturally responsive assessment aims to reduce; lift is the advantage side of the same comparison."),
 dict(q="Researchers develop socio-culturally responsive assessments primarily in order to", choices=[
   "reduce stereotype threat and the inequity that stereotype lift can create",
   "raise every test taker's score by the same amount",
   "eliminate the need for standardization",
   "replace validity with reliability as the standard of test quality"], ans=0,
   why="EK 2.8.B.3 states the purpose in exactly those terms: to reduce stereotype threat and potential inequity that may occur due to stereotype lift."),
 dict(q="The Flynn effect refers to the finding that", choices=[
   "IQ scores across much of the world have generally increased over time",
   "IQ scores decline steadily with age in individuals",
   "IQ scores vary more between groups than within them",
   "IQ scores are unrelated to educational opportunity"], ans=0,
   why="EK 2.8.C.1 states that IQ scores across much of the world have generally increased over time, which is the Flynn effect."),
 dict(q="The AP Psychology framework attributes the Flynn effect to", choices=[
   "societal factors such as higher socioeconomic status and better health care and nutrition",
   "changes in the scoring formula used by test publishers",
   "a decline in the difficulty of test items",
   "an increase in the number of people who take intelligence tests"], ans=0,
   why="EK 2.8.C.1 attributes the rise to societal factors, naming higher socioeconomic status and access to better health care and better nutrition."),
 dict(q="According to the AP Psychology framework, IQ scores tend to vary", choices=[
   "more within a group than between groups",
   "more between groups than within a group",
   "equally within and between groups",
   "only between groups defined by age"], ans=0,
   why="EK 2.8.C.2 states that IQ scores tend to vary more within a group than between groups, which is the finding that undercuts between-group comparisons."),
 dict(q="Which conclusion is best supported by the finding that IQ scores vary more within groups than between them?", choices=[
   "knowing a person's group membership tells you very little about that person's score",
   "group membership is the strongest predictor of an individual's score",
   "differences between groups cannot be measured at all",
   "IQ scores are identical for everyone within a group"], ans=0,
   why="EK 2.8.C.2's finding means the spread inside any group dwarfs the gap between group averages, so group membership is a weak basis for inferring an individual score."),
 dict(q="The AP Psychology framework identifies which of the following as able to negatively influence intelligence scores?", choices=[
   "poverty, discrimination, and educational inequities",
   "the number of siblings a person has",
   "the time of day a test is taken",
   "the length of the test booklet"], ans=0,
   why="EK 2.8.C.2 names poverty, discrimination, and educational inequities as factors that can negatively influence the intelligence scores of individuals and societal groups around the world."),
 dict(q="EK 2.8.C.3 documents that intelligence test scores have historically been used to", choices=[
   "limit access to jobs, military ranks, educational institutions, and immigration to the US",
   "guarantee equal access to higher education",
   "diagnose physical illness in military recruits",
   "set the pay scale for public employees"], ans=0,
   why="EK 2.8.C.3 states that scores from intelligence tests have been used to limit access to jobs, military ranks, educational institutions, and immigration to the US."),
 dict(q="An achievement test is designed to measure", choices=[
   "what a person currently knows",
   "how a person will perform in the future",
   "how quickly a person can learn something new",
   "a person's general ability across all domains"], ans=0,
   why="EK 2.8.D.1 states that some academic tests attempt to measure what someone knows, which are achievement tests."),
 dict(q="An aptitude test is designed to", choices=[
   "predict how a person will perform in the future",
   "measure what a person has already learned",
   "confirm that a test was administered consistently",
   "compare one half of a test with the other half"], ans=0,
   why="EK 2.8.D.1 states that some academic tests attempt to predict how someone will perform in the future, which are aptitude tests."),
 dict(q="An end-of-year exam covering the material taught in a chemistry course is best classified as", choices=[
   "an achievement test",
   "an aptitude test",
   "a reliability check",
   "a standardization sample"], ans=0,
   why="EK 2.8.D.1 assigns tests of what someone already knows to the achievement category, and a course-content exam measures exactly what was taught."),
 dict(q="A fixed mindset is the belief that intelligence is", choices=[
   "set from birth and not changeable through experience",
   "malleable and able to grow through effort and experience",
   "the same for every person",
   "impossible to measure with any test"], ans=0,
   why="EK 2.8.D.2 contrasts the belief that intelligence is fixed from birth with the belief that it is malleable due to experience."),
 dict(q="A growth mindset is the belief that intelligence is", choices=[
   "malleable and able to change through experience",
   "fixed from birth and unchangeable",
   "unrelated to academic achievement",
   "measured accurately only by aptitude tests"], ans=0,
   why="EK 2.8.D.2 defines the growth mindset as the belief that intelligence is malleable due to experience, and states that these beliefs can affect academic achievement."),
 dict(q="A researcher wants to test whether a brief lesson about the growth mindset improves later exam scores. Which design would support a causal conclusion?", choices=[
   "randomly assigning students to receive the lesson or a neutral lesson and comparing later exam scores",
   "surveying students about their beliefs and correlating the answers with their grades",
   "interviewing three high-achieving students in depth about their beliefs",
   "observing a classroom for a semester without intervening"], ans=0,
   why="Only a manipulated, randomly assigned independent variable licenses a causal conclusion; the survey, interview, and observation options are all non-experimental designs that can show association at most."),
 dict(q="A school proposes using a single IQ score to decide which students may enroll in advanced courses. Which framework-based objection is strongest?", choices=[
   "poverty, discrimination, and educational inequities can depress scores, and scores have historically been used to limit access",
   "intelligence tests are never administered under consistent conditions",
   "achievement and aptitude tests measure exactly the same thing",
   "IQ scores have decreased across generations, making them outdated"], ans=0,
   why="Science practice 4.B: EK 2.8.C.2 identifies poverty, discrimination, and educational inequities as depressing scores and EK 2.8.C.3 documents scores being used to limit access, which together bear directly on the proposal; the other options state things the framework contradicts."),
]
