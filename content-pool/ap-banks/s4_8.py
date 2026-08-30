# AP STATISTICS 4.8 Justifying a Claim Based on a Confidence Interval for the
# Difference Between Two Population Means - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objective 4.8: interpret a two-sample t-interval in context and justify a
# claim from it.
# Three ideas carry almost all the student error here, and each is tested more
# than once below: whether 0 lies inside the interval decides whether a
# difference is supported; the ORDER OF SUBTRACTION decides which population the
# interval says is larger; and "95 percent confident" describes the long-run
# capture rate of the method, not a probability for the one interval in hand.
# Every width, endpoint, midpoint and count is recomputed in verify_s4_8.py.
TOPIC = ("4.8", "Justifying a Claim Based on a Confidence Interval for the Difference Between Two Population Means", 4)
QUESTIONS = [

 dict(q="A 95 percent confidence interval for mu1 - mu2, the difference in mean annual rainfall between region 1 and region 2, is (3.2, 11.8) cm. What is the best justified claim?", choices=[
   "There is convincing evidence that region 1 has a greater mean annual rainfall than region 2",
   "There is convincing evidence that region 2 has a greater mean annual rainfall than region 1",
   "There is no convincing evidence of a difference in mean annual rainfall",
   "There is convincing evidence that the mean difference is exactly 7.5 cm",
   "Ninety-five percent of years in region 1 are between 3.2 and 11.8 cm wetter than in region 2"], ans=0,
   why="Every plausible value of mu1 - mu2 is positive, so the interval supports region 1 having the larger mean; it does not single out the midpoint and it says nothing about individual years."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is (-2.4, 6.1). What conclusion is justified?", choices=[
   "There is no convincing evidence that the two population means differ, because 0 is a plausible value",
   "There is convincing evidence that the two population means are equal",
   "There is convincing evidence that mu1 is larger, because most of the interval is positive",
   "There is convincing evidence that mu2 is larger, because the lower endpoint is negative",
   "The interval is invalid, because a difference cannot be negative"], ans=0,
   why="An interval containing 0 leaves equality among the plausible values; failing to rule out equality is not the same as establishing it."),

 dict(q="A 90 percent confidence interval for mu_A - mu_B, the difference in mean recovery time between treatment A and treatment B, is (-8.2, -1.6) days. Which claim is supported?", choices=[
   "Treatment A has the shorter mean recovery time",
   "Treatment B has the shorter mean recovery time",
   "The two treatments have equal mean recovery times",
   "Treatment A has the shorter mean recovery time for every patient",
   "No claim is supported, because the interval contains only negative values"], ans=0,
   why="With A minus B entirely negative, every plausible value has mu_A below mu_B, so A's mean recovery time is shorter; the interval is about means, not about every patient."),

 dict(q="Independent random samples of 30 observations each give a difference in sample means of 4, with s1 = 5 and s2 = 6. Using the conservative degrees of freedom, what are the 95 percent and 90 percent confidence intervals for mu1 - mu2?", choices=[
   "(1.084, 6.916) and (1.577, 6.423)",
   "(1.577, 6.423) and (1.084, 6.916)",
   "(1.084, 6.916) and (0.070, 7.930)",
   "(2.574, 5.426) and (2.788, 5.212)",
   "(1.084, 6.916) and (1.084, 6.916)"], ans=0,
   why="The standard error is sqrt(25/30 + 36/30) = 1.426 and the conservative df is 29, so t* is 2.045 at 95 percent and 1.699 at 90 percent, giving margins of error 2.916 and 2.423; the lower confidence level gives the narrower interval."),

 dict(q="Two hundred pairs of independent random samples are taken from the same two populations, and a 95 percent confidence interval for mu1 - mu2 is built from each pair. About how many of those intervals are expected to contain the true difference?", choices=[
   "5",
   "10",
   "95",
   "190",
   "200"], ans=3,
   why="The confidence level is the long-run capture rate of the procedure, so about 0.95 x 200 = 190 intervals capture mu1 - mu2 and about 10 miss it."),

 dict(q="A 99 percent confidence interval for mu1 - mu2 is (-8.2, -1.6). What are the point estimate and the margin of error?", choices=[
   "point estimate -4.9, margin of error 3.3",
   "point estimate -4.9, margin of error 6.6",
   "point estimate -3.3, margin of error 4.9",
   "point estimate -8.2, margin of error 6.6",
   "point estimate 4.9, margin of error 3.3"], ans=0,
   why="The point estimate is the midpoint (-8.2 + -1.6)/2 = -4.9, and the margin of error is half the width, (-1.6 - (-8.2))/2 = 3.3."),

 dict(q="A researcher reports: 'We are 95 percent confident that the difference in the two sample means lies between 1.2 and 4.8.' What is wrong?", choices=[
   "The interval estimates the difference in the two POPULATION means; the difference in sample means is known exactly and is the interval's midpoint",
   "Nothing is wrong, since the sample means are what were measured",
   "The confidence level should be stated as a probability",
   "The endpoints should be reported in the opposite order",
   "A confidence interval cannot be built for a difference"], ans=0,
   why="A confidence interval estimates an unknown parameter; the difference in sample means was computed from the data and sits at 3.0, the center of this interval."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is (0.5, 9.5). A colleague says this means there is a 95 percent probability that mu1 - mu2 falls between 0.5 and 9.5. What is the error?", choices=[
   "The parameter is a fixed number and the interval is already computed, so the 95 percent describes how often the method captures the parameter in repeated sampling",
   "The probability should be stated as 0.05 rather than 0.95",
   "The interval should have been built at a 99 percent level for a probability statement",
   "Nothing is wrong, provided both samples were random",
   "The error is that the interval should be centered at 0"], ans=0,
   why="Once the endpoints are computed, the interval either contains the parameter or it does not; the confidence level is a property of the procedure across repeated samples."),

 dict(q="A 95 percent confidence interval for mu_treatment - mu_control is (1.4, 6.0), from a randomized experiment. Which conclusion is best?", choices=[
   "There is convincing evidence that the treatment causes a higher mean response, because the units were randomly assigned and the interval lies entirely above 0",
   "There is convincing evidence of an association but not of causation, since no experiment can establish causation",
   "There is no convincing evidence of a difference, because the interval is narrow",
   "There is convincing evidence that every treated unit responds more strongly",
   "The interval cannot support a causal claim without a larger sample"], ans=0,
   why="Random assignment is what licenses a causal conclusion, and an interval lying entirely above 0 rules out no difference among the plausible values."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is (2.0, 8.0). Which value is NOT a plausible value of the difference in population means at this level?", choices=[
   "1.5",
   "2.5",
   "4.0",
   "6.0",
   "7.5"], ans=0,
   why="Plausible values are exactly those inside the interval, and 1.5 lies below the lower endpoint 2.0; the other four values are all inside."),

 dict(q="Which change would make a two-sample confidence interval for a difference in means narrower without altering the confidence level?", choices=[
   "Increase both sample sizes",
   "Increase the confidence level from 95 percent to 99 percent",
   "Use the conservative degrees of freedom instead of technology's",
   "Report the endpoints to fewer decimal places",
   "Combine the two samples into one sample"], ans=0,
   why="The margin of error is t* sqrt(s1^2/n1 + s2^2/n2); larger sample sizes shrink both terms, while a higher confidence level or the conservative df raises the critical value, and combining the samples estimates a different parameter entirely."),

 dict(q="A 95 percent confidence interval for mu_boys - mu_girls in mean reading score is (-0.9, 3.7). A newspaper reports 'Boys read better than girls.' What is the most accurate assessment?", choices=[
   "The report is unjustified, because 0 lies inside the interval and no difference remains plausible",
   "The report is justified, because most of the interval is positive",
   "The report is justified, because the point estimate is positive",
   "The report is unjustified, because the interval should be reported for girls minus boys",
   "The report is justified only at the 90 percent confidence level"], ans=0,
   why="A point estimate on one side of 0 is not evidence when the interval straddles 0; the data cannot distinguish a boys' advantage from a girls' advantage here."),

 dict(q="Two 95 percent confidence intervals for the same difference mu1 - mu2 are computed from two different pairs of samples: (1.0, 9.0) and (3.0, 7.0). What most likely explains why the second is narrower?", choices=[
   "The second study used larger samples or found less variability within its samples",
   "The second study used a higher confidence level",
   "The second study's populations have means that are closer together",
   "The second study made a computational error, since intervals for the same parameter must match",
   "The second study used the conservative degrees of freedom"], ans=0,
   why="Width is t* sqrt(s1^2/n1 + s2^2/n2), which depends on the sample sizes, the sample standard deviations and the critical value, not on how far apart the population means happen to be."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is (-5.0, -0.2). At the 95 percent level, which of the following differences is a plausible value?", choices=[
   "-1.0",
   "-6.0",
   "0.0",
   "0.5",
   "1.0"], ans=0,
   why="Only -1.0 lies between -5.0 and -0.2; 0.0 lies just outside the upper endpoint, which is exactly why this interval supports a real difference."),

 dict(q="Which interpretation of a 90 percent confidence interval (2.5, 7.9) for the difference in mean commute time between two cities, city A minus city B, is correct?", choices=[
   "We are 90 percent confident that the interval from 2.5 to 7.9 minutes contains the true difference in mean commute time between all commuters in city A and all commuters in city B",
   "Ninety percent of commuters in city A take between 2.5 and 7.9 minutes longer than commuters in city B",
   "There is a 0.90 probability that the true difference is between 2.5 and 7.9 minutes",
   "Ninety percent of samples from these cities have differences in sample means between 2.5 and 7.9 minutes",
   "We are 90 percent confident that the difference in sample means is between 2.5 and 7.9 minutes"], ans=0,
   why="The interpretation names the two populations, the response variable and the parameter, and it states confidence rather than probability."),

 dict(q="A researcher computes a 95 percent interval for mu_A - mu_B as (1.1, 4.9). A second researcher computes the interval for mu_B - mu_A from the same data. What should it be?", choices=[
   "(-4.9, -1.1)",
   "(1.1, 4.9)",
   "(-1.1, -4.9)",
   "(-4.9, 1.1)",
   "(4.9, 1.1)"], ans=0,
   why="Reversing the order of subtraction negates both endpoints and swaps them, so the interval that supports A being larger becomes an interval that supports B being smaller by the same amounts."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is (0.02, 0.06) kilograms, from samples of 5,000 each. Which comment is best?", choices=[
   "The interval gives convincing evidence of a difference, but the difference may be too small to matter in practice",
   "The interval gives no evidence of a difference, since the endpoints are close to 0",
   "The interval proves that the difference is exactly 0.04 kilograms",
   "The very large samples make the interval unreliable",
   "The interval should be widened to include 0 because the difference is small"], ans=0,
   why="Very large samples make the interval short enough to exclude 0 even for a tiny difference; statistical evidence of a difference and practical importance are separate questions."),

 dict(q="From an earlier study a 95 percent interval for mu1 - mu2 was (1.2, 8.8). A follow-up quadruples both sample sizes and finds the same sample means and standard deviations. Approximately what will the new 95 percent interval be?", choices=[
   "(3.1, 6.9)",
   "(1.2, 8.8)",
   "(2.15, 7.85)",
   "(-2.6, 12.6)",
   "(4.05, 5.95)"], ans=0,
   why="The point estimate stays at the midpoint 5.0 and the margin of error 3.8 is roughly halved by quadrupling both sample sizes, giving about 5.0 +/- 1.9."),

 dict(q="A 99 percent confidence interval for mu1 - mu2 built from a sample contains 0, while the 90 percent interval from the same sample does not. Which statement is correct?", choices=[
   "This is possible, because the 99 percent interval is wider and can reach past 0 when the 90 percent interval does not",
   "This is impossible, because both intervals have the same center",
   "This is impossible, because a higher confidence level gives a narrower interval",
   "This shows a computational error, since confidence level does not affect width",
   "This means the samples were not independent"], ans=0,
   why="Both intervals share a center, and the 99 percent interval is longer, so it can straddle 0 while the shorter 90 percent interval does not; the strength of the evidence depends on the level chosen."),

 dict(q="A 95 percent confidence interval for the difference in mean scores, method 1 minus method 2, is (-1.2, 0.4). A teacher concludes that the two methods produce identical mean scores. What is the flaw?", choices=[
   "Failing to rule out a zero difference is not evidence that the difference is zero; every value from -1.2 to 0.4 is equally plausible",
   "The teacher should have used a 99 percent interval to conclude equality",
   "The interval should have been reported as method 2 minus method 1",
   "There is no flaw, because 0 is inside the interval",
   "The flaw is that a negative endpoint makes the interval meaningless"], ans=0,
   why="An interval that contains 0 also contains many nonzero values; it establishes only that the data cannot distinguish among them, which is not evidence of equality."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is (3.4, 3.6). Which claim is best supported?", choices=[
   "There is convincing evidence of a difference, and the difference is estimated quite precisely",
   "There is no convincing evidence of a difference, because the interval is so narrow",
   "The difference is exactly 3.5",
   "The narrow interval shows the sample sizes were small",
   "The interval must be wrong, because a real interval cannot be this short"], ans=0,
   why="Excluding 0 supports a real difference, and a short interval means a precise estimate, which comes from large samples or small within-sample variability."),

 dict(q="Two independent random samples give a difference in sample means of 3.1 with a 95 percent margin of error of 2.7. What is the interval, and is a claim of no difference supported?", choices=[
   "(0.4, 5.8); no difference is not plausible, since 0 lies outside the interval",
   "(0.4, 5.8); no difference is plausible, since the lower endpoint is near 0",
   "(-2.7, 2.7); no difference is plausible",
   "(3.1, 5.8); no difference is not plausible",
   "(0.4, 5.8); nothing can be concluded without the sample sizes"], ans=0,
   why="The interval is 3.1 +/- 2.7 = (0.4, 5.8), and 0 lies below the lower endpoint, so a zero difference is not among the plausible values."),

 dict(q="A 95 percent confidence interval for mu1 - mu2 is reported from two independent samples of sizes 8 and 9, both of which are strongly skewed. What is the most serious problem with justifying any claim from it?", choices=[
   "The conditions for the procedure were not met, so the interval's stated 95 percent capture rate cannot be relied on",
   "The sample sizes are unequal, which biases the point estimate",
   "The interval is too wide to be useful",
   "The interval should have used a z critical value",
   "Nothing is wrong, because t procedures are robust to any skewness"], ans=0,
   why="With both sample sizes below 30 the sample distributions must be free from strong skewness and outliers; when they are not, the interval no longer has the advertised long-run capture rate and no claim from it is secure."),

 dict(q="Comparing a 90 percent and a 99 percent confidence interval for the same difference mu1 - mu2 from the same data, which pair of statements is correct?", choices=[
   "The 99 percent interval is wider and captures the parameter more often in repeated sampling",
   "The 90 percent interval is wider and captures the parameter more often",
   "The 99 percent interval is narrower and captures the parameter more often",
   "Both intervals have the same width but different centers",
   "The 90 percent interval is more likely to be correct for this particular sample"], ans=0,
   why="Higher confidence buys a higher long-run capture rate at the cost of a larger critical value and a wider interval; the two properties always move together."),

 dict(q="A 95 percent confidence interval for the difference in mean weight loss, program 1 minus program 2, is (-0.4, 5.6) kilograms. A magazine reports that program 1 is better. What should be said instead?", choices=[
   "The data do not give convincing evidence that either program produces a greater mean weight loss, since a difference of 0 is plausible",
   "The data give convincing evidence that program 1 is better, since the point estimate is 2.6",
   "The data give convincing evidence that program 2 is better",
   "The data prove that the two programs are equally effective",
   "The comparison is impossible because the interval contains a negative endpoint"], ans=0,
   why="The interval spans 0, so the plausible values include both a program 1 advantage and a small program 2 advantage; that is a failure to distinguish them, not proof that they are equal."),
]
