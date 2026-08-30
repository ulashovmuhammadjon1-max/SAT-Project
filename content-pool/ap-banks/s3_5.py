# AP STATISTICS 3.5 Setting Up a Test for a Population Proportion — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.5.A (identify the procedure and
# the parameter in context), 3.5.B (state the null and alternative hypotheses)
# and 3.5.C (verify the conditions).
#
# The procedure is the ONE-SAMPLE z-TEST FOR A POPULATION PROPORTION.
#
# THE DETAIL THAT DISTINGUISHES THIS TOPIC FROM 3.2 AND 3.3, and that a student
# meets three times in Unit 3 with a different answer each time -- which value
# goes into the normality condition:
#     3.2  sampling distribution, p known         ->  np and n(1 - p)
#     3.3  confidence interval, p unknown         ->  the OBSERVED counts
#     3.5  hypothesis test, p0 assumed true       ->  n*p0 and n(1 - p0)
# A test assumes the null hypothesis while checking conditions, so it uses the
# HYPOTHESIZED p0, not the observed p-hat. Three items here turn on that.
#
# Rules for the hypotheses, from EK 3.5.B.1 through 3.5.B.3:
#   H0 always states equality at the hypothesized value p0, and is the status quo;
#   Ha states the claim being investigated, and is one-sided (< or >) or
#     two-sided (not equal);
#   hypotheses are about the PARAMETER p, never about the statistic p-hat -- a
#     hypothesis written about p-hat is the single most common setup error, and
#     it is wrong because p-hat is known once the data are in, so there is
#     nothing to hypothesize about.
TOPIC = ("3.5", "Setting Up a Test for a Population Proportion", 3)

QUESTIONS = [
 dict(q="The appropriate procedure for testing a claim about a single population proportion is",
   choices=[
     "a one-sample z-test for a population proportion",
     "a one-sample t-test for a population mean",
     "a two-sample z-test for a difference of proportions",
     "a one-sample z-interval for a population proportion",
     "a chi-square goodness-of-fit test"],
   ans=0,
   why="A single proportion tested against a claimed value calls for the one-sample z-test; the z-interval estimates rather than tests."),

 dict(q="The null hypothesis in a hypothesis test is",
   choices=[
     "the statement about a parameter assumed correct unless there is convincing evidence otherwise",
     "the claim the researcher hopes to establish",
     "always the statement that the parameter is large",
     "a statement about the sample statistic",
     "the conclusion of the test"],
   ans=0,
   why="H0 is the status quo, held until the data give convincing evidence against it."),

 dict(q="The alternative hypothesis in a hypothesis test is",
   choices=[
     "the status quo condition",
     "the claim or belief about the parameter for which evidence is being sought",
     "always a statement of equality",
     "a statement about the sample proportion",
     "the same as the null hypothesis"],
   ans=1,
   why="Ha is what the researcher is investigating, and the test asks whether the data give convincing evidence for it."),

 dict(q="The null hypothesis of a one-sample z-test for a population proportion always",
   choices=[
     "contains an equality reference at the hypothesized value p0",
     "contains a strict inequality",
     "refers to the sample proportion p-hat",
     "states that p equals 0.5",
     "states that the sample is random"],
   ans=0,
   why="In AP Statistics the null is tested at the boundary of equality, so it is written H0: p = p0 even when the alternative is one-sided."),

 dict(q="Hypotheses in a test for a population proportion must be written in terms of",
   choices=[
     "the sample proportion p-hat",
     "the population proportion p",
     "the sample size n",
     "the z test statistic",
     "the p-value"],
   ans=1,
   why="p-hat is known once the sample is collected, so there is nothing to hypothesize about; the unknown being tested is the population parameter p."),

 dict(q="A manufacturer claims that at most 5% of its parts are defective. An inspector suspects the true rate is higher. The appropriate hypotheses are",
   choices=[
     "H0: p = 0.05 and Ha: p > 0.05",
     "H0: p = 0.05 and Ha: p < 0.05",
     "H0: p = 0.05 and Ha: p not equal to 0.05",
     "H0: p-hat = 0.05 and Ha: p-hat > 0.05",
     "H0: p > 0.05 and Ha: p = 0.05"],
   ans=0,
   why="The suspicion that the rate is higher is the claim being investigated, so it becomes the one-sided alternative, and the null sits at the boundary value 0.05."),

 dict(q="A researcher believes that fewer than 40% of a town's households own a bicycle. The appropriate hypotheses are",
   choices=[
     "H0: p = 0.40 and Ha: p < 0.40",
     "H0: p = 0.40 and Ha: p > 0.40",
     "H0: p < 0.40 and Ha: p = 0.40",
     "H0: p = 0.40 and Ha: p not equal to 0.40",
     "H0: p-hat = 0.40 and Ha: p-hat < 0.40"],
   ans=0,
   why="'Fewer than' points one way, so the alternative is one-sided with a less-than sign and the null holds equality at 0.40."),

 dict(q="A quality engineer wants to know whether the proportion of defective items differs from the historical 8%, in either direction. The appropriate hypotheses are",
   choices=[
     "H0: p = 0.08 and Ha: p > 0.08",
     "H0: p = 0.08 and Ha: p < 0.08",
     "H0: p = 0.08 and Ha: p not equal to 0.08",
     "H0: p not equal to 0.08 and Ha: p = 0.08",
     "H0: p-hat = 0.08 and Ha: p-hat not equal to 0.08"],
   ans=2,
   why="'Differs, in either direction' is a two-sided alternative, written with a not-equal sign."),

 dict(q="An alternative hypothesis written with a not-equal sign is called",
   choices=["one-sided", "two-sided", "null", "conservative", "invalid"],
   ans=1,
   why="A not-equal alternative looks for a departure in either direction, so it is two-sided; < or > alternatives are one-sided."),

 dict(q="A student writes H0: p-hat = 0.60 for a test about a population proportion. The error is that",
   choices=[
     "the value 0.60 is not allowed in a null hypothesis",
     "a hypothesis must be a statement about the population parameter p, not about the sample statistic p-hat",
     "the null hypothesis must use an inequality",
     "the null must be about the sample size",
     "there is no error"],
   ans=1,
   why="The sample proportion is computed from the data and is not in doubt; the test concerns the unknown population proportion."),

 dict(q="A student writes Ha: p = 0.45 as the alternative hypothesis. The error is that",
   choices=[
     "the alternative must state a departure from the null value, using <, >, or not equal, rather than an equality",
     "0.45 is too small",
     "the alternative must be about p-hat",
     "the alternative must always be two-sided",
     "there is no error"],
   ans=0,
   why="Equality belongs in the null; the alternative expresses the direction of the departure being investigated."),

 dict(q="Which of the following is NOT one of the three conditions for a one-sample z-test for a population proportion?",
   choices=[
     "The data were collected using a random sample",
     "When sampling without replacement, the population is at least ten times the sample size",
     "The expected counts under the null hypothesis are each at least 10",
     "The population distribution is normal",
     "All three of the other conditions are required"],
   ans=3,
   why="No assumption is made about the shape of the population; the normality condition concerns the sampling distribution of p-hat."),

 dict(q="For a one-sample z-test of H0: p = p0, the normality condition is checked using",
   choices=[
     "the observed number of successes and failures",
     "n times p0 and n times (1 - p0), the counts EXPECTED if the null hypothesis is true",
     "the sample proportion p-hat only",
     "the sample size alone, which must exceed 30",
     "the population size"],
   ans=1,
   why="A test proceeds by assuming the null is true, so the condition is checked at the hypothesized value p0 rather than at the observed p-hat."),

 dict(q="Why does a hypothesis test use p0 in the normality condition while a confidence interval uses the observed counts?",
   choices=[
     "Because a test assumes the null hypothesis while checking conditions, whereas an interval has no hypothesized value to assume",
     "Because a test is more accurate",
     "Because p0 is always larger than p-hat",
     "Because intervals do not require conditions",
     "Because the two conditions are actually identical"],
   ans=0,
   why="The whole logic of a test is conditional on H0 being true, so the expected counts are computed from p0; an interval has no such value to work from."),

 dict(q="A test of H0: p = 0.30 uses a random sample of n = 250. Checking the normality condition gives",
   choices=[
     "expected counts of 75 and 175, both at least 10, so the condition is met",
     "expected counts of 0.30 and 0.70, so the condition fails",
     "an expected count of 250, so the condition is met",
     "expected counts of 75 only, so the condition fails",
     "the condition cannot be checked without p-hat"],
   ans=0,
   why="250(0.30) = 75 expected successes and 250(0.70) = 175 expected failures, both comfortably above 10."),

 dict(q="A test of H0: p = 0.02 uses a random sample of n = 300. Does the normality condition hold?",
   choices=[
     "Yes, because n = 300 is large",
     "No, because the expected number of successes is 6, which is below 10, even though the expected failures number 294",
     "No, because the expected number of failures is below 10",
     "Yes, because both expected counts exceed 10",
     "The condition does not apply to tests"],
   ans=1,
   why="A large n is not enough when p0 is very small: 300(0.02) = 6 expected successes leaves the null distribution too skewed for the normal approximation."),

 dict(q="A random sample of 400 is drawn without replacement from a population of 3,000 for a test of a proportion. Does the 10% condition hold?",
   choices=[
     "Yes, because 400 is less than 3,000",
     "No, because 400 exceeds 10% of 3,000, which is 300",
     "Yes, because 3,000 is more than ten times 10",
     "No, because 400 is too large a sample",
     "The condition applies only to confidence intervals"],
   ans=1,
   why="Ten percent of 3,000 is 300, and a sample of 400 exceeds it, so the draws are not close enough to independent."),

 dict(q="Stated in context, the parameter for a test about whether more than 60% of a school's students walk to school is",
   choices=[
     "the proportion of the sampled students who walk to school",
     "the proportion of all students at that school who walk to school",
     "the number of students who walk to school",
     "the sample size",
     "the z test statistic"],
   ans=1,
   why="The parameter must name the proportion, the response variable and the population, and it describes the population rather than the sample."),

 dict(q="A survey is conducted by asking volunteers at a shopping centre. For a one-sample z-test for a proportion, this violates",
   choices=[
     "the randomization condition",
     "the 10% condition",
     "the normality condition",
     "no condition at all",
     "the requirement that p0 be known"],
   ans=0,
   why="Volunteers are not a random sample, and no arithmetic later in the procedure repairs a biased selection."),

 dict(q="A political scientist wants to test whether a candidate has support above one half. The correct hypotheses are",
   choices=[
     "H0: p = 0.50 and Ha: p > 0.50",
     "H0: p = 0.50 and Ha: p < 0.50",
     "H0: p > 0.50 and Ha: p = 0.50",
     "H0: p = 0.50 and Ha: p not equal to 0.50",
     "H0: p-hat = 0.50 and Ha: p-hat > 0.50"],
   ans=0,
   why="Support above one half is the claim being investigated, so it is the one-sided alternative and the null sits at the boundary 0.50."),

 dict(q="For a test of H0: p = 0.50 with n = 64, the expected counts under the null are",
   choices=["32 and 32", "50 and 50", "64 and 64", "0.5 and 0.5", "32 and 64"],
   ans=0,
   why="64(0.50) = 32 expected successes and 64(0.50) = 32 expected failures, both above 10."),

 dict(q="A researcher decides on a two-sided alternative only AFTER seeing that the sample proportion came out above the null value. This is a problem because",
   choices=[
     "two-sided alternatives are never allowed",
     "the hypotheses must be chosen before examining the data, or the test's error rate is no longer what it claims to be",
     "the sample proportion cannot exceed the null value",
     "a two-sided alternative requires a larger sample",
     "it is not a problem"],
   ans=1,
   why="Choosing the hypotheses to fit the data is the same fault as changing an investigative question after analysis: the stated probabilities no longer describe the procedure actually used."),

 dict(q="Which pair of hypotheses is stated correctly for a one-sample z-test for a proportion?",
   choices=[
     "H0: p = 0.25, Ha: p > 0.25",
     "H0: p > 0.25, Ha: p = 0.25",
     "H0: p-hat = 0.25, Ha: p-hat > 0.25",
     "H0: p = 0.25, Ha: p = 0.30",
     "H0: p not equal to 0.25, Ha: p = 0.25"],
   ans=0,
   why="The null holds equality at the hypothesized value and the alternative states the direction of departure, both written about the parameter p."),

 dict(q="A test is set up with H0: p = 0.35 and Ha: p < 0.35. Which sample result would count as evidence in the direction of the alternative?",
   choices=[
     "a sample proportion noticeably below 0.35",
     "a sample proportion noticeably above 0.35",
     "a sample proportion exactly equal to 0.35",
     "any sample proportion, since the test is two-sided",
     "a large sample size"],
   ans=0,
   why="Evidence points toward Ha when the statistic falls on the alternative's side of the null value, which here means below 0.35."),

 dict(q="Before any data are collected, the null hypothesis in a test for a proportion is",
   choices=[
     "assumed to be true for the purpose of the analysis",
     "assumed to be false",
     "proved true",
     "chosen to match the sample proportion",
     "irrelevant to the calculation"],
   ans=0,
   why="Every step of the test, from the conditions to the test statistic to the p-value, is computed under the assumption that H0 holds."),
]
