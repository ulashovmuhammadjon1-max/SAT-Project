# AP STATISTICS 2.9 Parameters of Random Variables — 25 questions
# CED: Fall 2026, Unit 2. Learning objectives 2.9.A (calculate the mean and
# standard deviation of a discrete random variable) and 2.9.B (interpret them in
# the context of a specific population). Essential knowledge 2.9.A.1 (these are
# PARAMETERS, single fixed values), 2.9.A.2 (E(X) = sum of x times P(x)) and
# 2.9.A.3 (SD(X) = square root of the sum of (x - mu) squared times P(x)).
#
# Note for anyone extending this bank: the Fall 2026 CED has NO topic on
# combining random variables. Topic 2.9 is only 2.9.A and 2.9.B; the mean and
# standard deviation of a sum or difference of independent random variables was
# old 4.9-4.10 and is not in the current framework. See AP_STATS_CED.md.
#
# Three misconceptions drive the item selection:
#   1. the expected value need not be a possible value of X, and often is not --
#      an "expected" 0.75 defects when only whole numbers can occur;
#   2. the standard deviation is the square root of the weighted sum, so the
#      variance is the intermediate quantity, and each is offered against the
#      other as a distractor;
#   3. these are parameters, fixed by the distribution, not statistics that vary
#      from sample to sample.
#
# Distributions used, all verified to sum to 1 in verify_s2_9.py:
#   A defects: P(0)=0.50, P(1)=0.30, P(2)=0.15, P(3)=0.05  mu=0.75  sd=0.8874
#   B a game:  P(-2)=0.6, P(1)=0.3, P(8)=0.1               mu=-0.10 sd=3.0150
#   C a fair six-sided die                                  mu=3.5   sd=1.7078
TOPIC = ("2.9", "Parameters of Random Variables", 2)

TABLE_A = dict(
    headers=["Defects, x", "P(X = x)"],
    rows=[["0", "0.50"], ["1", "0.30"], ["2", "0.15"], ["3", "0.05"]])

TABLE_B = dict(
    headers=["Net winnings in dollars, w", "P(W = w)"],
    rows=[["-2", "0.6"], ["1", "0.3"], ["8", "0.1"]])

QUESTIONS = [
 dict(q="The expected value of a discrete random variable X is calculated as",
   choices=[
     "the sum, over all values, of x multiplied by P(x)",
     "the sum of all the values of x, divided by how many there are",
     "the largest value of x",
     "the value of x with the largest probability",
     "the sum of all the probabilities"],
   ans=0,
   why="Each value is weighted by its probability, which is what makes the expected value a probability-weighted average rather than a plain one."),

 dict(q="The standard deviation of a discrete random variable X is calculated as",
   choices=[
     "the sum of (x - mu) times P(x)",
     "the square root of the sum of (x - mu) squared times P(x)",
     "the sum of (x - mu) squared times P(x)",
     "the square root of the largest value of x",
     "the square root of mu"],
   ans=1,
   why="The weighted sum of squared deviations is the variance, and the standard deviation is its square root."),

 dict(q="The mean and standard deviation of a probability distribution are",
   choices=[
     "statistics, because they are computed from data",
     "parameters, each a single fixed value determined by the distribution",
     "variables, because they change from trial to trial",
     "estimates that improve with more trials",
     "always equal to one another"],
   ans=1,
   why="They are fixed properties of the distribution itself, not quantities that vary from one sample to the next."),

 dict(q="The number of defects X in a randomly chosen item has the distribution shown. What is the expected value of X?",
   table=TABLE_A,
   choices=["0.50", "0.75", "1.00", "1.50", "2.00"],
   ans=1,
   why="E(X) = 0(0.50) + 1(0.30) + 2(0.15) + 3(0.05) = 0.75."),

 dict(q="For the defect distribution, what is the variance of X?",
   table=TABLE_A,
   choices=["0.5625", "0.7500", "0.7875", "0.8874", "1.5750"],
   ans=2,
   why="Summing (x - 0.75) squared times P(x) gives 0.28125 + 0.01875 + 0.234375 + 0.253125 = 0.7875."),

 dict(q="For the defect distribution, what is the standard deviation of X?",
   table=TABLE_A,
   choices=["0.7500", "0.7875", "0.8874", "1.1270", "1.5750"],
   ans=2,
   why="The standard deviation is the square root of the variance, and the square root of 0.7875 is 0.8874; 0.7875 itself is the variance."),

 dict(q="The expected number of defects for that distribution is 0.75, yet no item can have 0.75 defects. This is",
   table=TABLE_A,
   choices=[
     "an error in the calculation",
     "expected: an expected value is a long-run average and need not be a possible value of the random variable",
     "a sign that the distribution is invalid",
     "a reason to round the answer to 1",
     "possible only because the probabilities are decimals"],
   ans=1,
   why="The expected value is the mean of many repetitions, which can fall between the achievable whole-number outcomes."),

 dict(q="Interpreted in context, the expected value of 0.75 for the defect distribution means that",
   table=TABLE_A,
   choices=[
     "every item has 0.75 defects",
     "over a very large number of items, the average number of defects per item would be about 0.75",
     "75% of items are defective",
     "the most common number of defects is 0.75",
     "three quarters of items have exactly one defect"],
   ans=1,
   why="An expected value is a long-run average per item, not a statement about any single item and not a percentage."),

 dict(q="A game pays the net winnings shown, in dollars. What is the expected net winning per play?",
   table=TABLE_B,
   choices=["-2.00", "-0.10", "0.00", "0.10", "2.33"],
   ans=1,
   why="E(W) = (-2)(0.6) + 1(0.3) + 8(0.1) = -1.2 + 0.3 + 0.8 = -0.10 dollars."),

 dict(q="For that game, the expected net winning is -0.10 dollars per play. Over many plays, a player should expect to",
   table=TABLE_B,
   choices=[
     "lose about 10 cents per play on average",
     "win about 10 cents per play on average",
     "break even",
     "lose exactly 10 cents on every single play",
     "win 10 cents on 10% of the plays"],
   ans=0,
   why="A negative expected value is an average loss per play in the long run; no individual play produces exactly -0.10."),

 dict(q="For that game, what is the standard deviation of the net winnings, to four decimal places?",
   table=TABLE_B,
   choices=["0.1000", "1.7078", "3.0150", "3.0500", "9.0900"],
   ans=2,
   why="The variance is 3.61(0.6) + 1.21(0.3) + 65.61(0.1) = 9.09, and the square root of 9.09 is 3.0150; 9.09 is the variance, not the standard deviation."),

 dict(q="For that game, what is the variance of the net winnings?",
   table=TABLE_B,
   choices=["-0.10", "3.0150", "9.0000", "9.0900", "10.0000"],
   ans=3,
   why="Summing (w + 0.10) squared times P(w) gives 2.166 + 0.363 + 6.561 = 9.09."),

 dict(q="A single fair six-sided die is rolled and X is the number showing. What is E(X)?",
   choices=["3.0", "3.5", "4.0", "6.0", "21.0"],
   ans=1,
   why="Each face has probability 1/6, so E(X) = (1 + 2 + 3 + 4 + 5 + 6)/6 = 21/6 = 3.5."),

 dict(q="For a single roll of a fair six-sided die, what is the standard deviation of the number showing, to four decimal places?",
   choices=["1.4142", "1.7078", "2.5000", "2.9167", "3.5000"],
   ans=1,
   why="The variance is 2.9167, computed as the average of (x - 3.5) squared over the six faces, and its square root is 1.7078."),

 dict(q="A random variable X has E(X) = 3.5, which is not one of its possible values. The most accurate description of E(X) is that it is",
   choices=[
     "the value X takes most often",
     "the middle value of X",
     "the long-run average value of X over many repetitions",
     "the largest value X can take",
     "impossible, since E(X) must be attainable"],
   ans=2,
   why="The expected value is the balance point of the distribution, which need not coincide with any achievable outcome."),

 dict(q="If every value of a discrete random variable is the same number, then its standard deviation is",
   choices=["0", "1", "equal to that number", "undefined", "equal to the number of values"],
   ans=0,
   why="Every deviation from the mean is 0, so the weighted sum of squared deviations is 0 and so is its square root."),

 dict(q="Two discrete random variables have the same expected value, but the first has a much larger standard deviation. This means the first variable's values",
   choices=[
     "are on average larger",
     "are spread further from their common mean",
     "are all larger than the second variable's values",
     "have a larger probability of being negative",
     "sum to more than 1"],
   ans=1,
   why="An equal expected value fixes the centre; the standard deviation describes how far the values typically fall from that centre."),

 dict(q="In computing the standard deviation of a discrete random variable, the squared deviations are weighted by",
   choices=[
     "the number of possible values",
     "the probability of each value",
     "the expected value",
     "1 divided by the number of trials",
     "nothing; they are simply added"],
   ans=1,
   why="A value that occurs rarely should contribute little to the typical deviation, which is exactly what weighting by P(x) achieves."),

 dict(q="A random variable takes the values 1, 2, 3, 4, and 5, each with probability 0.2. Its expected value is",
   choices=["2.0", "2.5", "3.0", "3.5", "5.0"],
   ans=2,
   why="With equal probabilities the expected value is the ordinary average, (1 + 2 + 3 + 4 + 5)/5 = 3."),

 dict(q="For that same variable taking 1 through 5 each with probability 0.2, the standard deviation is closest to",
   choices=["1.14", "1.41", "1.58", "2.00", "2.24"],
   ans=1,
   why="The variance is the average of (x - 3) squared, which is (4 + 1 + 0 + 1 + 4)/5 = 2, and the square root of 2 is about 1.41."),

 dict(q="An insurance policy pays out 10,000 dollars with probability 0.002 and nothing otherwise. What is the expected payout per policy?",
   choices=["2", "20", "200", "2000", "10000"],
   ans=1,
   why="E = 10,000(0.002) + 0(0.998) = 20 dollars, which is what the insurer must average per policy before expenses and profit."),

 dict(q="A carnival game charges 3 dollars to play and has an expected payout of 2.20 dollars. The expected net result per play for the player is",
   choices=["-2.20", "-0.80", "0.00", "0.80", "2.20"],
   ans=1,
   why="The player pays 3 and receives on average 2.20, so the expected net result is 2.20 - 3 = -0.80 dollars per play."),

 dict(q="Which statement about the expected value of a discrete random variable is correct?",
   choices=[
     "It must be one of the possible values of the variable",
     "It must lie between the smallest and largest possible values",
     "It must be positive",
     "It must be a whole number",
     "It equals the most likely value"],
   ans=1,
   why="A probability-weighted average of the values cannot fall outside their range, but it need not be attainable, positive, whole, or the most probable value."),

 dict(q="An interpretation of a standard deviation of 0.887 defects for the defect distribution is that",
   table=TABLE_A,
   choices=[
     "every item differs from the mean by 0.887 defects",
     "the number of defects on an item typically differs from the mean of 0.75 by about 0.887 defects",
     "0.887 of all items are defective",
     "the variance is 0.887",
     "88.7% of items have at least one defect"],
   ans=1,
   why="A standard deviation is a typical distance from the mean, stated in the variable's own units, and it is not a proportion."),

 dict(q="A student computes the standard deviation of a discrete random variable and obtains a negative number. This",
   choices=[
     "is possible when the expected value is negative",
     "must be an error, since a standard deviation is a square root of a sum of non-negative terms",
     "means the distribution is skewed left",
     "should be reported as its absolute value without further checking",
     "means the probabilities do not sum to 1"],
   ans=1,
   why="Each squared deviation is non-negative and each probability is non-negative, so the sum and its square root cannot be negative."),
]
