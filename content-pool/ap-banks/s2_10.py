# AP STATISTICS 2.10 The Binomial Distribution — 25 questions
# CED: Fall 2026, Unit 2. Skills 3.C, 3.D, 4.B and 4.D: calculate binomial
# probabilities, calculate the mean and standard deviation of the distribution,
# justify a claim from it, and interpret the result.
#
# The binomial setting has four requirements, and every one of them is the
# subject of at least one item, because recognizing the setting is what the exam
# actually tests:
#   a FIXED number of trials n;
#   each trial has two outcomes, success and failure;
#   the trials are INDEPENDENT;
#   the probability of success p is the SAME on every trial.
#
# The geometric distribution is NOT a topic in the Fall 2026 CED (see
# AP_STATS_CED.md), so no item here asks a student to compute a geometric
# probability. It does appear as the natural FOIL in the setting-recognition
# items: "keep rolling until the first six" fails the fixed-n requirement, and
# noticing that is squarely within 2.10.
#
# Formulas, written in the plain-text style this bank uses throughout:
#   P(X = k) = C(n, k) x p^k x (1 - p)^(n - k)
#   mean = np,  standard deviation = sqrt(n p (1 - p))
# Every probability, mean and standard deviation keyed below is recomputed in
# verify_s2_10.py with scipy.stats.binom, and the pmf is independently
# cross-checked against the closed-form formula.
TOPIC = ("2.10", "The Binomial Distribution", 2)

QUESTIONS = [
 dict(q="Which of the following is NOT a requirement of a binomial setting?",
   choices=[
     "There is a fixed number of trials",
     "Each trial has only two possible outcomes",
     "The trials are independent",
     "The probability of success is the same on every trial",
     "The number of successes is at least half the number of trials"],
   ans=4,
   why="The four requirements are a fixed n, two outcomes per trial, independence, and a constant p; nothing is required of how many successes actually occur."),

 dict(q="For a binomial random variable X with n trials, probability of success p, and probability of failure q, the probability of exactly k successes is",
   choices=[
     "C(n, k) x p^k x q^(n - k)",
     "p^k x q^(n - k)",
     "C(n, k) x p^n",
     "n x p x k",
     "k x p x q"],
   ans=0,
   why="The binomial coefficient counts the orders in which k successes can occur, and each such order has probability p^k times q^(n-k)."),

 dict(q="For a binomial random variable with n trials, success probability p, and failure probability q, the mean is",
   choices=["p", "np", "nq", "sqrt(npq)", "npq"],
   ans=1,
   why="The expected number of successes in n trials each succeeding with probability p is np."),

 dict(q="Writing q for the probability of failure, the standard deviation of a binomial random variable with n trials and success probability p is",
   choices=["np", "npq", "sqrt(np)", "sqrt(npq)", "p x sqrt(n)"],
   ans=3,
   why="The variance is npq and the standard deviation is its square root."),

 dict(q="Which of the following describes a binomial setting?",
   choices=[
     "Rolling a fair die repeatedly until a six appears, and counting the rolls needed",
     "Selecting 12 items at random with replacement from a large batch and counting how many are defective",
     "Measuring the exact weight of each of 20 packages",
     "Drawing cards one at a time from a deck without replacement until an ace appears",
     "Recording the time until a machine fails"],
   ans=1,
   why="Twelve is a fixed number of trials, each item is defective or not, replacement keeps the trials independent with a constant probability, and the variable counts successes."),

 dict(q="A student rolls a fair die repeatedly until the first six appears and records how many rolls were needed. This is NOT a binomial setting because",
   choices=[
     "the trials are not independent",
     "the number of trials is not fixed in advance",
     "there are more than two outcomes on each roll",
     "the probability of success changes from roll to roll",
     "the variable is continuous"],
   ans=1,
   why="Each roll is independent with a constant probability of 1/6 and can be classified as six or not-six, but the process runs until a success occurs, so n is random rather than fixed."),

 dict(q="Ten cards are dealt one at a time WITHOUT replacement from a standard deck, and X counts how many are hearts. Why is X not exactly binomial?",
   choices=[
     "There is no fixed number of trials",
     "The probability of a heart changes from draw to draw, so the trials are not independent",
     "There are four suits rather than two outcomes",
     "The mean cannot be computed",
     "Ten is too small a number of trials"],
   ans=1,
   why="Dealing without replacement changes the composition of the deck, so the success probability is not constant and the draws are dependent."),

 dict(q="A binomial random variable has n = 10 and p = 0.3. What is P(X = 3), to three decimal places?",
   choices=["0.027", "0.200", "0.267", "0.300", "0.383"],
   ans=2,
   why="C(10,3)(0.3)^3(0.7)^7 = 120 x 0.027 x 0.0823543 = 0.267; 0.383 is P(X <= 2) and 0.027 is p cubed alone."),

 dict(q="A binomial random variable has n = 10 and p = 0.3. What is its mean?",
   choices=["0.3", "2.1", "3.0", "7.0", "10.0"],
   ans=2,
   why="The mean is np = 10(0.3) = 3.0 successes."),

 dict(q="A binomial random variable has n = 10 and p = 0.3. What is its standard deviation, to three decimal places?",
   choices=["0.458", "1.449", "2.100", "3.000", "4.583"],
   ans=1,
   why="The variance is np(1-p) = 10(0.3)(0.7) = 2.1, and the square root of 2.1 is 1.449; 2.1 itself is the variance."),

 dict(q="A binomial random variable has n = 10 and p = 0.3. What is P(X <= 2), to three decimal places?",
   choices=["0.028", "0.121", "0.233", "0.383", "0.617"],
   ans=3,
   why="Adding P(X = 0), P(X = 1) and P(X = 2) gives 0.028 + 0.121 + 0.233 = 0.383."),

 dict(q="A quality inspector checks 8 randomly selected components, each defective with probability 0.25, independently. What is the probability that exactly 2 are defective, to three decimal places?",
   choices=["0.063", "0.250", "0.311", "0.367", "0.500"],
   ans=2,
   why="C(8,2)(0.25)^2(0.75)^6 = 28 x 0.0625 x 0.177979 = 0.311."),

 dict(q="For those 8 components each defective with probability 0.25, what is the probability that at most 1 is defective, to three decimal places?",
   choices=["0.100", "0.267", "0.311", "0.367", "0.633"],
   ans=3,
   why="P(X = 0) + P(X = 1) = 0.100 + 0.267 = 0.367."),

 dict(q="For those 8 components each defective with probability 0.25, what is the expected number of defectives?",
   choices=["0.25", "1.50", "2.00", "6.00", "8.00"],
   ans=2,
   why="The mean is np = 8(0.25) = 2.00 defective components."),

 dict(q="For those 8 components each defective with probability 0.25, what is the standard deviation of the number defective, to three decimal places?",
   choices=["1.225", "1.500", "2.000", "2.449", "6.000"],
   ans=0,
   why="The variance is 8(0.25)(0.75) = 1.5, and the square root of 1.5 is 1.225; 1.5 is the variance."),

 dict(q="A basketball player makes 60% of her free throws, independently. She attempts 12. What is the expected number she makes?",
   choices=["0.60", "4.80", "6.00", "7.20", "12.00"],
   ans=3,
   why="The mean is np = 12(0.6) = 7.2 free throws; 4.8 is the expected number missed."),

 dict(q="For that player attempting 12 free throws with success probability 0.6, what is the standard deviation of the number made, to three decimal places?",
   choices=["1.697", "2.121", "2.880", "3.394", "7.200"],
   ans=0,
   why="The variance is 12(0.6)(0.4) = 2.88, and the square root of 2.88 is 1.697; 2.88 is the variance."),

 dict(q="For that player attempting 12 free throws with success probability 0.6, what is the probability she makes exactly 8, to three decimal places?",
   choices=["0.128", "0.213", "0.240", "0.600", "0.667"],
   ans=1,
   why="C(12,8)(0.6)^8(0.4)^4 = 495 x 0.01679616 x 0.0256 = 0.213."),

 dict(q="A machine part fails on any given day with probability 0.4, independently across days. Over 5 days, what is the probability that it fails on at least one day, to three decimal places?",
   choices=["0.078", "0.400", "0.600", "0.922", "2.000"],
   ans=3,
   why="Use the complement: P(no failures) = (0.6)^5 = 0.0778, so P(at least one) = 1 - 0.0778 = 0.922."),

 dict(q="A fair six-sided die is rolled 6 times and X counts the number of sixes. What is the mean of X?",
   choices=["0.167", "1.000", "3.000", "3.500", "6.000"],
   ans=1,
   why="The mean is np = 6(1/6) = 1.00 six, on average, in six rolls."),

 dict(q="A fair six-sided die is rolled 6 times and X counts the number of sixes. What is P(X = 2), to three decimal places?",
   choices=["0.028", "0.161", "0.201", "0.333", "0.402"],
   ans=2,
   why="C(6,2)(1/6)^2(5/6)^4 = 15 x 0.027778 x 0.482253 = 0.201."),

 dict(q="A survey selects 20 people at random from a very large population in which 50% hold a certain view, and X counts how many hold it. The standard deviation of X is",
   choices=["2.236", "2.500", "5.000", "10.000", "20.000"],
   ans=0,
   why="The variance is 20(0.5)(0.5) = 5, and the square root of 5 is 2.236; 5 is the variance and 10 is the mean."),

 dict(q="Sampling 20 people WITHOUT replacement from a population of 30 people is not well modelled as binomial, but sampling 20 without replacement from a population of 300,000 usually is. The reason is that",
   choices=[
     "larger populations always have a different probability of success",
     "when the sample is a tiny fraction of the population, removing sampled individuals barely changes the success probability, so the trials are very nearly independent",
     "binomial distributions require populations of at least 100,000",
     "20 is only binomial for large populations",
     "the mean formula fails for small populations"],
   ans=1,
   why="The binomial model needs a constant p; drawing 20 from 300,000 changes the composition so slightly that the approximation is excellent, while drawing 20 from 30 does not."),

 dict(q="If X is binomial with n = 12 and p = 0.6, then the number of FAILURES is",
   choices=[
     "not a random variable",
     "binomial with n = 12 and p = 0.4",
     "binomial with n = 12 and p = 0.6",
     "binomial with n = 7.2 and p = 0.4",
     "not binomial at all"],
   ans=1,
   why="Relabelling which outcome counts as a success leaves a fixed n, two outcomes, independence and a constant probability, now 1 - 0.6 = 0.4."),

 dict(q="For a binomial random variable, increasing n while holding p fixed",
   choices=[
     "increases the mean and increases the standard deviation",
     "increases the mean and decreases the standard deviation",
     "leaves the mean unchanged and increases the standard deviation",
     "increases the mean and leaves the standard deviation unchanged",
     "decreases both the mean and the standard deviation"],
   ans=0,
   why="The mean np grows in proportion to n and the standard deviation sqrt(np(1-p)) grows in proportion to the square root of n, so both increase."),
]
