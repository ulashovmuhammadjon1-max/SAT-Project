# AP STATISTICS 2.8 Introduction to Random Variables and Probability
# Distributions — 25 questions
# CED: Fall 2026, Unit 2. Learning objective 2.8.A, essential knowledge 2.8.A.1
# (a random variable takes numerical values from a random phenomenon), 2.8.A.2
# (a discrete probability distribution gives a probability to every possible
# value, and those probabilities sum to 1), 2.8.A.3 (it can be found by the
# rules of probability or estimated by simulation), 2.8.A.4 (it can be shown as
# a graph, a table or a function) and 2.8.A.5 (a cumulative distribution gives
# P(X <= x) at each value).
#
# Two distributions carry the computation.
#   PETS, complete:  P(0)=0.22, P(1)=0.35, P(2)=0.25, P(3)=0.13, P(4)=0.05
#     cumulative:         0.22       0.57       0.82       0.95       1.00
#   CALLS, one value missing, to be recovered from the fact that the
#     probabilities must total 1.
#
# The recurring error this module targets is reading a cumulative value as a
# single-value probability, and the boundary slip between P(X <= 2) and
# P(X < 2): for a discrete variable those differ by exactly P(X = 2), and
# several items are keyed to numbers that separate them.
TOPIC = ("2.8", "Introduction to Random Variables and Probability Distributions", 2)

TABLE_PETS = dict(
    headers=["Number of pets, x", "P(X = x)"],
    rows=[["0", "0.22"], ["1", "0.35"], ["2", "0.25"], ["3", "0.13"], ["4", "0.05"]])

TABLE_PETS_CUM = dict(
    headers=["Number of pets, x", "P(X <= x)"],
    rows=[["0", "0.22"], ["1", "0.57"], ["2", "0.82"], ["3", "0.95"], ["4", "1.00"]])

TABLE_CALLS = dict(
    headers=["Calls in an hour, x", "P(X = x)"],
    rows=[["0", "0.10"], ["1", "0.24"], ["2", "0.31"], ["3", "?"], ["4", "0.17"]])

QUESTIONS = [
 dict(q="A random variable is",
   choices=[
     "a variable whose values are numerical outcomes of a random phenomenon",
     "any variable that changes",
     "a category label assigned at random",
     "the number of trials in an experiment",
     "a variable whose value is chosen by the researcher"],
   ans=0,
   why="A random variable attaches a number to each outcome of a random process."),

 dict(q="For a discrete random variable, the sum of the probabilities over all possible values must equal",
   choices=["0", "0.5", "1", "the number of possible values", "the largest probability"],
   ans=2,
   why="The possible values exhaust everything that can happen, so their probabilities account for all of the probability."),

 dict(q="A probability distribution for a discrete random variable may be represented as",
   choices=[
     "a graph, a table, or a function",
     "a table only",
     "a graph only",
     "a single number",
     "a two-way table only"],
   ans=0,
   why="All three representations carry the same information: which values are possible and with what probability."),

 dict(q="A cumulative probability distribution for a discrete random variable shows",
   choices=[
     "the probability of each individual value",
     "the probability of being less than or equal to each value of the random variable",
     "the probability of being greater than each value",
     "the mean of the distribution",
     "the number of trials"],
   ans=1,
   why="A cumulative distribution accumulates probability from the smallest value up to and including each value."),

 dict(q="Which of the following is a discrete random variable?",
   choices=[
     "The exact time in seconds a runner takes to finish a race",
     "The number of cars that pass an intersection in an hour",
     "The precise mass of a randomly chosen apple",
     "The temperature at noon tomorrow",
     "The exact length of a randomly chosen leaf"],
   ans=1,
   why="A count takes whole-number values and so is discrete; times, masses, temperatures and lengths are measured and can take any value in an interval."),

 dict(q="Which of the following is a continuous random variable?",
   choices=[
     "The number of heads in ten coin tosses",
     "The number of defective items in a shipment",
     "The amount of rainfall, in millimetres, at a station tomorrow",
     "The number of students absent today",
     "The number of times a die shows a six in twenty rolls"],
   ans=2,
   why="Rainfall can take any value in an interval, while all the others are counts."),

 dict(q="The probability distribution of X, the number of pets a randomly chosen household owns, is shown. What is P(X = 2)?",
   table=TABLE_PETS,
   choices=["0.13", "0.22", "0.25", "0.35", "0.82"],
   ans=2,
   why="The table gives the probability of each value directly, and P(X = 2) = 0.25; 0.82 is the cumulative probability P(X <= 2)."),

 dict(q="For the pet distribution, what is P(X <= 2)?",
   table=TABLE_PETS,
   choices=["0.25", "0.57", "0.60", "0.82", "0.95"],
   ans=3,
   why="Adding the probabilities for 0, 1 and 2 gives 0.22 + 0.35 + 0.25 = 0.82."),

 dict(q="For the pet distribution, what is P(X < 2)?",
   table=TABLE_PETS,
   choices=["0.22", "0.35", "0.57", "0.60", "0.82"],
   ans=2,
   why="Strictly fewer than 2 means 0 or 1, so 0.22 + 0.35 = 0.57; including X = 2 would give 0.82, and for a discrete variable the two differ by exactly P(X = 2)."),

 dict(q="For the pet distribution, what is P(X >= 2)?",
   table=TABLE_PETS,
   choices=["0.18", "0.25", "0.43", "0.57", "0.82"],
   ans=2,
   why="Either add 0.25 + 0.13 + 0.05 = 0.43, or take 1 - P(X <= 1) = 1 - 0.57 = 0.43."),

 dict(q="For the pet distribution, what is P(X > 2)?",
   table=TABLE_PETS,
   choices=["0.05", "0.13", "0.18", "0.43", "0.75"],
   ans=2,
   why="More than 2 means 3 or 4, so 0.13 + 0.05 = 0.18; 0.43 would include X = 2 as well."),

 dict(q="For the pet distribution, what is the probability that a household owns either 1 or 2 pets?",
   table=TABLE_PETS,
   choices=["0.25", "0.35", "0.57", "0.60", "0.82"],
   ans=3,
   why="These are distinct values of X and therefore disjoint events, so the probabilities add: 0.35 + 0.25 = 0.60."),

 dict(q="For the pet distribution, what is the probability that a household owns at least one pet?",
   table=TABLE_PETS,
   choices=["0.22", "0.35", "0.43", "0.78", "0.95"],
   ans=3,
   why="Using the complement, 1 - P(X = 0) = 1 - 0.22 = 0.78."),

 dict(q="Verify the pet distribution: the five listed probabilities sum to",
   table=TABLE_PETS,
   choices=["0.82", "0.95", "1.00", "1.05", "5.00"],
   ans=2,
   why="0.22 + 0.35 + 0.25 + 0.13 + 0.05 = 1.00, as any valid probability distribution must."),

 dict(q="The cumulative probability distribution of the same pet variable X is shown. What is P(X = 3)?",
   table=TABLE_PETS_CUM,
   choices=["0.05", "0.13", "0.18", "0.82", "0.95"],
   ans=1,
   why="An individual probability is the jump in the cumulative distribution, so P(X = 3) = 0.95 - 0.82 = 0.13."),

 dict(q="From that cumulative table for the pet variable, what is P(X = 1)?",
   table=TABLE_PETS_CUM,
   choices=["0.13", "0.22", "0.35", "0.57", "0.79"],
   ans=2,
   why="P(X = 1) = P(X <= 1) - P(X <= 0) = 0.57 - 0.22 = 0.35."),

 dict(q="From that cumulative table for the pet variable, what is P(X > 3)?",
   table=TABLE_PETS_CUM,
   choices=["0.05", "0.13", "0.18", "0.95", "1.00"],
   ans=0,
   why="P(X > 3) = 1 - P(X <= 3) = 1 - 0.95 = 0.05."),

 dict(q="The last entry of any correctly constructed cumulative probability distribution for a discrete random variable must be",
   choices=["0", "0.5", "1", "the largest individual probability", "the number of values"],
   ans=2,
   why="By the largest value, all of the probability has been accumulated."),

 dict(q="The number of support calls received in an hour has the distribution shown, with one probability missing. What is the missing probability P(X = 3)?",
   table=TABLE_CALLS,
   choices=["0.08", "0.18", "0.22", "0.28", "0.82"],
   ans=1,
   why="The probabilities must total 1, so the missing value is 1 - (0.10 + 0.24 + 0.31 + 0.17) = 0.18."),

 dict(q="For the support-call distribution, once the missing probability is found, what is P(X <= 1)?",
   table=TABLE_CALLS,
   choices=["0.10", "0.24", "0.34", "0.65", "0.90"],
   ans=2,
   why="P(X <= 1) = 0.10 + 0.24 = 0.34, which needs none of the missing value."),

 dict(q="For the support-call distribution, what is P(X >= 3)?",
   table=TABLE_CALLS,
   choices=["0.17", "0.18", "0.35", "0.65", "0.83"],
   ans=2,
   why="With the missing probability equal to 0.18, P(X >= 3) = 0.18 + 0.17 = 0.35."),

 dict(q="A student proposes a probability distribution assigning 0.30, 0.25, 0.20, and 0.15 to the four possible values of a discrete random variable. This is not a valid distribution because",
   choices=[
     "the probabilities are not all equal",
     "the probabilities sum to 0.90 rather than 1",
     "there are only four values",
     "0.30 is too large",
     "the values are not listed in order"],
   ans=1,
   why="Every possible value must be covered, so the probabilities must account for all of the probability, and 0.10 is unaccounted for."),

 dict(q="A student proposes a probability distribution assigning 0.5, 0.4, and -0.1 to three values. This is not valid because",
   choices=[
     "the probabilities sum to 0.8",
     "a probability cannot be negative",
     "three values is too few",
     "the largest probability should come last",
     "it is actually valid"],
   ans=1,
   why="Although these three numbers sum to 0.8 and so fail on that ground too, the decisive objection is that -0.1 is not a legal probability at all."),

 dict(q="A probability distribution for a discrete random variable can be obtained by",
   choices=[
     "applying the rules of probability, or by estimating it with a simulation",
     "the rules of probability only",
     "simulation only",
     "measuring the variable once",
     "assuming every value is equally likely"],
   ans=0,
   why="Either route is legitimate: a theoretical derivation gives exact probabilities, and a simulation estimates them."),

 dict(q="For a discrete random variable, the difference between P(X <= 2) and P(X < 2) is",
   choices=[
     "always 0",
     "exactly P(X = 2)",
     "always 1",
     "the mean of the distribution",
     "P(X > 2)"],
   ans=1,
   why="The two events differ by the single outcome X = 2, so their probabilities differ by that value's probability; for a continuous variable the difference would be 0, which is why the distinction matters here."),
]
