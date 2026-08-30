# AP STATISTICS 3.4 Justifying a Claim Based on a Confidence Interval for a
# Population Proportion — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.4.A (interpret an interval and
# the confidence level in context), 3.4.B (justify a claim from an interval) and
# 3.4.C (the relationships among sample size, confidence level, margin of error
# and interval width).
#
# This is an INTERPRETATION topic, and interpretation is where the scoring is
# strictest. The CED fixes two distinct sentences and students merge them:
#
#   THE INTERVAL (EK 3.4.A.3): "We are C% confident that the interval from a to
#     b contains the true proportion of [response variable] for [population]."
#   THE CONFIDENCE LEVEL (EK 3.4.A.2): "In repeated random sampling with the
#     same sample size, approximately C% of the intervals constructed will
#     capture the population proportion."
#
# Four wrong readings are each given their own item, because each is a distinct
# error rather than a variant of one:
#   (a) a probability statement about the parameter -- the parameter is fixed,
#       so it is not 95% likely to lie anywhere;
#   (b) a statement about C% of the SAMPLE DATA falling in the interval;
#   (c) a statement about C% of future SAMPLE PROPORTIONS falling in it;
#   (d) a claim of certainty -- EK 3.4.A.1 says the computed interval MAY OR MAY
#       NOT contain the parameter, and one particular interval either does or
#       does not.
#
# Intervals used, all recomputed in verify_s3_4.py:
#   (0.52, 0.58) at 95% -- entirely above 0.50, so it supports a majority claim
#   (0.47, 0.55) at 95% -- straddles 0.50, so it does NOT
TOPIC = ("3.4", "Justifying a Claim Based on a Confidence Interval for a Population Proportion", 3)

QUESTIONS = [
 dict(q="A 95% confidence interval for the proportion of a city's residents who support a policy is (0.52, 0.58). The correct interpretation of this INTERVAL is",
   choices=[
     "We are 95% confident that the interval from 0.52 to 0.58 contains the true proportion of all city residents who support the policy",
     "There is a 95% probability that the true proportion is between 0.52 and 0.58",
     "95% of city residents support the policy at a level between 0.52 and 0.58",
     "95% of all samples will have a sample proportion between 0.52 and 0.58",
     "The true proportion is certainly between 0.52 and 0.58"],
   ans=0,
   why="An interval interpretation names the confidence level, the interval, the parameter, the response variable and the population, and says the interval captures the parameter."),

 dict(q="The correct interpretation of the CONFIDENCE LEVEL of 95% is that",
   choices=[
     "95% of the sample data lie inside the interval",
     "in repeated random sampling with the same sample size, approximately 95% of the intervals constructed will capture the population proportion",
     "the population proportion changes 95% of the time",
     "there is a 95% chance the sample proportion is correct",
     "95% of the population is represented by the sample"],
   ans=1,
   why="The confidence level describes the long-run success rate of the METHOD across many samples, not any single interval."),

 dict(q="A student says, 'There is a 95% probability that the population proportion lies between 0.52 and 0.58.' The problem with this statement is that",
   choices=[
     "the interval is too narrow for such a claim",
     "the population proportion is a fixed number, so it either lies in this particular interval or it does not; the 95% describes the method, not this interval",
     "probabilities cannot be expressed as percentages",
     "the sample size is not given",
     "there is nothing wrong with it"],
   ans=1,
   why="Once the data are collected, the interval is fixed and so is the parameter; the randomness that the 95% describes lies in which sample was drawn."),

 dict(q="A student says, 'About 95% of the sampled residents gave answers between 0.52 and 0.58.' This is wrong because",
   choices=[
     "a confidence interval describes a plausible range for the population PARAMETER, not the spread of the individual data values",
     "the percentage should be 90%",
     "the sample size is too small",
     "the interval should be wider",
     "individual responses cannot be numeric"],
   ans=0,
   why="Each individual either supports the policy or does not; the interval estimates the population proportion, and says nothing about where individual observations fall."),

 dict(q="A student says, 'About 95% of future sample proportions will fall between 0.52 and 0.58.' This is wrong because",
   choices=[
     "the interval is built to capture the population proportion, not to predict where future sample proportions will land",
     "future samples are impossible to take",
     "sample proportions never repeat",
     "the confidence level would have to be 99%",
     "it is actually correct"],
   ans=0,
   why="An interval centred on one sample's p-hat is not a prediction interval for other samples' statistics; it is an estimate of the parameter."),

 dict(q="According to the CED, a computed confidence interval for a population proportion",
   choices=[
     "always contains the population proportion",
     "never contains the population proportion",
     "may or may not contain the population proportion",
     "contains exactly 95% of the population",
     "contains the sample proportion 95% of the time"],
   ans=2,
   why="Any single interval either captures the parameter or misses it; the confidence level tells you how often the procedure succeeds, not whether this one did."),

 dict(q="A 95% confidence interval for the proportion of residents supporting a policy is (0.52, 0.58). Does this provide convincing evidence that a majority of residents support the policy?",
   choices=[
     "Yes, because the entire interval lies above 0.50, so every plausible value is a majority",
     "No, because 0.58 is less than 1",
     "No, because the interval contains 0.55",
     "Yes, because the interval is narrow",
     "It cannot be determined from an interval"],
   ans=0,
   why="A claim of a majority means p is greater than 0.50, and the interval rules out every value at or below 0.50 as implausible."),

 dict(q="A 95% confidence interval for the proportion of residents supporting a policy is (0.47, 0.55). Does this provide convincing evidence that a majority support the policy?",
   choices=[
     "Yes, because the midpoint 0.51 exceeds 0.50",
     "No, because the interval contains 0.50, so a value at or below one half remains plausible",
     "Yes, because more of the interval lies above 0.50 than below it",
     "No, because 0.47 is less than 0.45",
     "Yes, because the sample proportion is 0.51"],
   ans=1,
   why="An interval that straddles 0.50 leaves both a majority and a minority plausible, so it does not settle the question, whatever its midpoint is."),

 dict(q="A 95% confidence interval for a population proportion is (0.31, 0.39). A researcher claims that p = 0.35. This interval",
   choices=[
     "proves the claim is true",
     "is consistent with the claim, since 0.35 lies inside the interval, though it does not prove it",
     "contradicts the claim",
     "shows the claim is 95% likely",
     "cannot be used to assess the claim"],
   ans=1,
   why="A value inside the interval is a plausible value for the parameter, which supports but does not establish the claim."),

 dict(q="For that same 95% interval of (0.31, 0.39), a different researcher claims that p = 0.45. Assessed against the interval, this claim",
   choices=[
     "is supported, since 0.45 is fairly close to the interval",
     "is contradicted by the data, since 0.45 lies outside the interval of plausible values",
     "is proved false beyond any doubt",
     "cannot be assessed using a confidence interval",
     "is shown to be 95% likely to be true"],
   ans=1,
   why="A value outside the interval is implausible at this confidence level, which is evidence against the claim without amounting to proof."),

 dict(q="For a given sample, increasing the confidence level causes the critical value to",
   choices=["increase", "decrease", "stay the same", "become zero", "become negative"],
   ans=0,
   why="More confidence requires reaching further into the tails of the standard normal, so z* grows."),

 dict(q="For a given sample, increasing the confidence level causes the margin of error to",
   choices=["increase", "decrease", "stay the same", "become zero", "depend on the population size"],
   ans=0,
   why="The margin of error is z* times the standard error, and only z* changes when the confidence level does."),

 dict(q="For a given sample, increasing the confidence level causes the width of the interval to",
   choices=["increase", "decrease", "stay the same", "halve", "become undefined"],
   ans=0,
   why="The width is twice the margin of error, so it moves with the margin of error."),

 dict(q="Holding the confidence level fixed, increasing the sample size causes the standard error to",
   choices=["increase", "decrease", "stay the same", "become negative", "equal the margin of error"],
   ans=1,
   why="The standard error has n under a square root in the denominator, so it falls as the sample grows."),

 dict(q="Holding the confidence level and sample proportion fixed, increasing the sample size tends to make the confidence interval",
   choices=["wider", "narrower", "unchanged in width", "centred on a different value", "impossible to compute"],
   ans=1,
   why="A smaller standard error gives a smaller margin of error and so a narrower interval, at the same confidence level."),

 dict(q="A 90% and a 99% confidence interval are computed from the SAME sample. Which is wider, and why?",
   choices=[
     "The 90% interval, because lower confidence needs more room",
     "The 99% interval, because a higher confidence level requires a larger critical value",
     "They are the same width, since the sample is the same",
     "The 90% interval, because it uses a larger standard error",
     "It depends on the sample proportion"],
   ans=1,
   why="The two intervals share a standard error and differ only in z*, which is 1.645 against 2.576."),

 dict(q="A researcher wants a narrower confidence interval without lowering the confidence level. The appropriate change is to",
   choices=[
     "increase the sample size",
     "decrease the sample size",
     "raise the confidence level",
     "report the sample proportion instead",
     "round the endpoints"],
   ans=0,
   why="A larger sample shrinks the standard error, which narrows the interval while the confidence level is left alone."),

 dict(q="A 95% confidence interval for a population proportion is (0.42, 0.50). The sample proportion that produced it is",
   choices=["0.42", "0.46", "0.48", "0.50", "0.08"],
   ans=1,
   why="The sample proportion is the centre of the interval, and the midpoint of 0.42 and 0.50 is 0.46."),

 dict(q="A 95% confidence interval for a population proportion is (0.42, 0.50). The margin of error is",
   choices=["0.02", "0.04", "0.08", "0.46", "0.92"],
   ans=1,
   why="The margin of error is half the width, and half of 0.50 - 0.42 = 0.08 is 0.04."),

 dict(q="A 99% confidence interval for a population proportion is (0.634, 0.766). The sample proportion and margin of error are",
   choices=[
     "0.700 and 0.132",
     "0.700 and 0.066",
     "0.634 and 0.132",
     "0.766 and 0.066",
     "0.132 and 0.700"],
   ans=1,
   why="The centre is (0.634 + 0.766)/2 = 0.700 and the margin of error is half the width, (0.766 - 0.634)/2 = 0.066."),

 dict(q="Which of the following would make a confidence interval for a proportion both narrower AND keep the confidence level at 95%?",
   choices=[
     "Lowering the confidence level to 90%",
     "Quadrupling the sample size",
     "Raising the confidence level to 99%",
     "Using a smaller sample",
     "Rounding the sample proportion to one decimal place"],
   ans=1,
   why="Quadrupling n halves the margin of error while the confidence level, and so the critical value, is untouched."),

 dict(q="A political consultant reports a 95% confidence interval of (0.48, 0.56) and concludes 'our candidate will win a majority'. The most accurate criticism is that",
   choices=[
     "the interval includes values at or below 0.50, so a majority is not established",
     "the interval is too wide to compute",
     "confidence intervals cannot be used for elections",
     "the confidence level should be 100%",
     "the consultant should have used the midpoint 0.52"],
   ans=0,
   why="Plausible values run from 0.48 to 0.56, and several of them are not majorities, so the data do not settle the question."),

 dict(q="Two 95% confidence intervals for the same proportion are (0.40, 0.60) from one study and (0.46, 0.54) from another. The second study most likely",
   choices=[
     "used a larger sample",
     "used a smaller sample",
     "used a higher confidence level",
     "made an arithmetic error",
     "sampled a different population"],
   ans=0,
   why="At the same confidence level and similar p-hat, a narrower interval comes from a smaller standard error, which comes from a larger sample."),

 dict(q="Which statement about a single computed 95% confidence interval is correct?",
   choices=[
     "It contains the parameter with probability 0.95",
     "It either contains the parameter or it does not; the 95% refers to how often the procedure succeeds over repeated samples",
     "It contains 95% of the sample data",
     "It will contain the next sample's proportion 95% of the time",
     "It becomes wider as more data are collected"],
   ans=1,
   why="Once computed, there is nothing random left in the interval; the confidence level is a property of the procedure that produced it."),

 dict(q="A complete interpretation of a confidence interval for a population proportion must include",
   choices=[
     "only the two endpoints",
     "the confidence level, the interval, and the parameter described in context with its population",
     "the sample size and the standard error",
     "the critical value",
     "the p-value"],
   ans=1,
   why="EK 3.4.A.3 requires naming the confidence level, the interval, and what the parameter is a proportion OF, in context."),
]
