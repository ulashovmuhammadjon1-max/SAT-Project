# AP STATISTICS 3.8 Potential Errors When Performing Tests — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.8.A (identify Type I and Type II
# errors and define power), 3.8.B (calculate their probabilities), 3.8.C (the
# four factors that raise power) and 3.8.D (interpret the two errors and weigh
# their consequences).
#
# This is the PRIMARY treatment of Type I and Type II error and power in this
# bank. Units 4 and 5 raise the same ideas wherever a decision about a mean
# needs them; this module is the fuller one and is where the definitions,
# the probabilities and the four factors are all established.
#
# The definitions, from EK 3.8.A.1 through 3.8.A.3, stated as decisions rather
# than as beliefs, because that is what makes them checkable:
#
#                              H0 is actually true      H0 is actually false
#     reject H0                TYPE I ERROR             correct (power)
#     fail to reject H0        correct                  TYPE II ERROR
#
#   P(Type I error)  = alpha, fixed BEFORE the data are collected (EK 3.8.B.1)
#   P(Type II error) = 1 - power                        (EK 3.8.B.2)
#
# The four things that raise power (EK 3.8.C.1), each with its own item:
#   a larger sample size; a smaller standard error; a true parameter farther
#   from the null value; a larger significance level.
#
# The trade-off worth stating plainly, and the reason alpha is a judgement call
# rather than a convention: lowering alpha reduces Type I error and RAISES Type
# II error. Which matters more depends on the consequences, which is EK 3.8.D.1,
# and several items give a context where one error is clearly the worse one.
TOPIC = ("3.8", "Potential Errors When Performing Tests", 3)

QUESTIONS = [
 dict(q="A Type I error occurs when",
   choices=[
     "there is convincing evidence that the alternative hypothesis is true, but it is not",
     "there is not convincing evidence that the alternative hypothesis is true, but it is",
     "the null hypothesis is correctly rejected",
     "the sample is not random",
     "the conditions for the test are not met"],
   ans=0,
   why="A Type I error is rejecting a null hypothesis that is in fact true, that is, finding an effect that is not there."),

 dict(q="A Type II error occurs when",
   choices=[
     "there is convincing evidence that the alternative hypothesis is true, but it is not",
     "there is not convincing evidence that the alternative hypothesis is true, but it is",
     "the null hypothesis is correctly retained",
     "the p-value is computed incorrectly",
     "the sample size is too large"],
   ans=1,
   why="A Type II error is failing to reject a null hypothesis that is in fact false, that is, missing an effect that is really there."),

 dict(q="The power of a hypothesis test is",
   choices=[
     "the probability of rejecting a true null hypothesis",
     "the probability that a test will correctly reject a false null hypothesis",
     "the probability that the null hypothesis is true",
     "the significance level",
     "the p-value"],
   ans=1,
   why="Power is the probability of detecting an effect that is genuinely present."),

 dict(q="The probability of making a Type I error is",
   choices=[
     "the p-value",
     "the significance level alpha, set before the data are collected",
     "1 minus the power",
     "the power",
     "always 0.05"],
   ans=1,
   why="Alpha is by definition the probability of rejecting a true null, and it is chosen in advance rather than read off the data."),

 dict(q="The probability of making a Type II error equals",
   choices=[
     "alpha",
     "1 minus alpha",
     "1 minus the power",
     "the power",
     "the p-value"],
   ans=2,
   why="Power is the probability of correctly rejecting a false null, so its complement is the probability of failing to do so."),

 dict(q="A test is conducted at alpha = 0.05. If the null hypothesis is actually true, the probability of rejecting it is",
   choices=["0.00", "0.05", "0.50", "0.95", "1.00"],
   ans=1,
   why="Rejecting a true null is precisely a Type I error, whose probability is the significance level 0.05."),

 dict(q="A test has power 0.80. The probability of a Type II error is",
   choices=["0.05", "0.20", "0.80", "0.95", "1.00"],
   ans=1,
   why="P(Type II error) = 1 - power = 1 - 0.80 = 0.20."),

 dict(q="A test has a Type II error probability of 0.35. Its power is",
   choices=["0.05", "0.35", "0.65", "0.95", "1.35"],
   ans=2,
   why="Power = 1 - P(Type II error) = 1 - 0.35 = 0.65."),

 dict(q="A researcher rejects the null hypothesis, and unknown to her the null hypothesis is actually true. She has made",
   choices=[
     "a Type I error",
     "a Type II error",
     "no error",
     "both types of error",
     "an error in arithmetic"],
   ans=0,
   why="Rejecting a true null is a Type I error, and no test can reveal which errors have occurred in any single study."),

 dict(q="A researcher fails to reject the null hypothesis, and unknown to her the null hypothesis is actually false. She has made",
   choices=[
     "a Type I error",
     "a Type II error",
     "no error",
     "both types of error",
     "a conditions violation"],
   ans=1,
   why="Failing to reject a false null is a Type II error: the effect was there and the test missed it."),

 dict(q="A researcher rejects the null hypothesis, and the null hypothesis is in fact false. She has",
   choices=[
     "made a Type I error",
     "made a Type II error",
     "reached a correct decision, an outcome whose probability is the power of the test",
     "proved the alternative hypothesis",
     "made no decision"],
   ans=2,
   why="Correctly rejecting a false null is the successful outcome, and its probability is what power measures."),

 dict(q="A researcher wants to raise the power of a planned test. Holding everything else fixed, which change accomplishes that?",
   choices=[
     "Decreasing the sample size",
     "Increasing the sample size",
     "Decreasing the significance level alpha",
     "Increasing the standard error",
     "Moving the true parameter closer to the null value"],
   ans=1,
   why="A larger sample sharpens the test's ability to detect a real departure from the null."),

 dict(q="Power also responds to the spread of the sampling distribution. Holding everything else fixed, which change raises it?",
   choices=[
     "Increasing the standard error",
     "Decreasing the standard error",
     "Lowering alpha from 0.05 to 0.01",
     "Choosing a two-sided alternative instead of a one-sided one",
     "Reducing the sample size"],
   ans=1,
   why="A smaller standard error concentrates the sampling distribution, which makes a real departure easier to detect."),

 dict(q="Power depends on the truth as well as on the design. Holding everything else fixed, power is higher when",
   choices=[
     "the true parameter value is farther from the null hypothesized value",
     "the true parameter value is closer to the null hypothesized value",
     "the true parameter value equals the null hypothesized value",
     "the significance level is smaller",
     "the sample is smaller"],
   ans=0,
   why="A large true effect is easier to detect than a small one, so power rises as the truth moves away from the null value."),

 dict(q="The significance level affects power too. Holding everything else fixed, which change to alpha raises the power of a test?",
   choices=[
     "Raising alpha from 0.01 to 0.05",
     "Lowering alpha from 0.05 to 0.01",
     "Decreasing the sample size",
     "Increasing the standard error",
     "Nothing can increase power"],
   ans=0,
   why="A larger alpha makes rejection easier, which raises power at the cost of a higher Type I error rate."),

 dict(q="Lowering the significance level from 0.05 to 0.01 has what effect on the two error probabilities?",
   choices=[
     "Both decrease",
     "Both increase",
     "The Type I error probability decreases and the Type II error probability increases",
     "The Type I error probability increases and the Type II error probability decreases",
     "Neither changes"],
   ans=2,
   why="Demanding stronger evidence before rejecting makes a false alarm rarer and a missed effect more common; the trade-off is why alpha is a judgement rather than a convention."),

 dict(q="A test's power is 0.90 when the true proportion is 0.60 and the null value is 0.50. If the true proportion were instead 0.55, the power would be",
   choices=[
     "greater than 0.90",
     "less than 0.90, because the true value is closer to the null and so harder to detect",
     "exactly 0.90",
     "exactly 0.10",
     "impossible to compare"],
   ans=1,
   why="Power depends on how far the truth lies from the null value, and 0.55 is a smaller departure than 0.60."),

 dict(q="A medical screening test is evaluated with H0: the patient does not have the disease. In this framing, a Type I error means",
   choices=[
     "telling a healthy patient they have the disease",
     "telling a patient with the disease that they are healthy",
     "correctly identifying a healthy patient",
     "correctly identifying a sick patient",
     "failing to run the test"],
   ans=0,
   why="Rejecting a true null here means concluding disease when there is none, which is a false positive."),

 dict(q="For that same screening test with H0: the patient does not have the disease, a Type II error means",
   choices=[
     "telling a healthy patient they have the disease",
     "telling a patient who has the disease that they are healthy",
     "correctly identifying a healthy patient",
     "running the test twice",
     "setting alpha too high"],
   ans=1,
   why="Failing to reject a false null here means missing a disease that is present, which is a false negative."),

 dict(q="For a screening test for a serious but treatable disease, a Type II error is usually judged more serious than a Type I error. A reasonable response is to",
   choices=[
     "use a smaller alpha, making rejection harder",
     "use a larger alpha, making rejection easier, so that fewer genuine cases are missed",
     "use no significance level at all",
     "reverse the hypotheses after seeing the data",
     "reduce the sample size"],
   ans=1,
   why="Since the consequences of missing a case outweigh those of a false alarm, the design should tolerate more Type I error in exchange for higher power."),

 dict(q="A manufacturer tests whether a safety component fails more often than the permitted rate, with H0: the failure rate equals the permitted rate. A Type I error would mean",
   choices=[
     "concluding the failure rate is too high when it is not, leading to an unnecessary and costly recall",
     "concluding the failure rate is acceptable when it is not, leaving unsafe parts in service",
     "correctly recalling a faulty component",
     "using the wrong test",
     "sampling too many components"],
   ans=0,
   why="Rejecting a true null here means acting on an effect that is not there, and the consequence is the cost of an unnecessary recall."),

 dict(q="For that same safety test, a Type II error would mean",
   choices=[
     "an unnecessary recall",
     "leaving an unsafe component in service because the test failed to detect the elevated failure rate",
     "correctly clearing a safe component",
     "a p-value that is too small",
     "an alpha that is too large"],
   ans=1,
   why="Failing to reject a false null here means the elevated failure rate goes undetected, which is the more dangerous of the two outcomes."),

 dict(q="Which statement about the consequences of the two errors is correct?",
   choices=[
     "A Type I error is always more serious than a Type II error",
     "A Type II error is always more serious than a Type I error",
     "Which error is more serious depends on the context, and should be considered before the study is conducted",
     "The two errors always have equal consequences",
     "Consequences are irrelevant to the choice of alpha"],
   ans=2,
   why="The CED is explicit that the relative seriousness varies by study and that the consequences should shape the choice of significance level in advance."),

 dict(q="A researcher wants to reduce BOTH error probabilities at once. The only way to do this is to",
   choices=[
     "lower alpha",
     "raise alpha",
     "increase the sample size",
     "use a one-sided alternative",
     "it is impossible to reduce both"],
   ans=2,
   why="Changing alpha trades one error against the other; only more information, in the form of a larger sample, can lower both at the same time."),

 dict(q="After a test, a researcher states 'we did not make a Type I error'. This claim",
   choices=[
     "is verifiable from the p-value",
     "cannot be verified, because whether an error occurred depends on the unknown truth about the parameter",
     "is always true when the null is rejected",
     "is always true when the null is not rejected",
     "means the power was 1"],
   ans=1,
   why="Knowing which error was made would require knowing the parameter, which is exactly what the study set out to learn."),
]
