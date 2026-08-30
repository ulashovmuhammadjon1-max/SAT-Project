# AP STATISTICS 2.4 Introduction to Probability — 25 questions
# CED: Fall 2026, Unit 2. Learning objective 2.4.A, essential knowledge 2.4.A.1
# (sample space, whose probability is 1), 2.4.A.2 (equally likely outcomes give
# P(E) = favourable / total), 2.4.A.3 (0 <= P <= 1) and 2.4.A.4 (complement:
# P(not E) = 1 - P(E)).
#
# The counting-based items all use processes whose sample spaces are small
# enough to enumerate completely, and verify_s2_4.py enumerates them -- two dice
# (36 outcomes), two coin tosses, a standard 52-card deck, a spinner. Nothing is
# taken from a remembered result: P(sum of 7) is counted, not recalled.
#
# Notation used throughout, since this bank renders as plain text:
#   P(A)      probability of A
#   P(not A)  probability of the complement of A
#   A and B   the intersection, both occur
#   A or B    the union, at least one occurs
TOPIC = ("2.4", "Introduction to Probability", 2)

QUESTIONS = [
 dict(q="The sample space of a random process is",
   choices=[
     "the set of all possible nonoverlapping outcomes",
     "the most likely outcome",
     "the number of trials performed",
     "the set of outcomes that actually occurred",
     "the average of all the outcomes"],
   ans=0,
   why="The sample space lists every outcome the process can produce, with no two of them overlapping."),

 dict(q="The probability of the entire sample space is always",
   choices=["0", "0.5", "1", "the number of outcomes", "undefined"],
   ans=2,
   why="Some outcome in the sample space must occur, so the sample space has probability 1."),

 dict(q="The probability of any event must be a number",
   choices=[
     "between 0 and 1, inclusive",
     "between -1 and 1, inclusive",
     "greater than 1",
     "equal to the number of favourable outcomes",
     "between 0 and 100, exclusive"],
   ans=0,
   why="Probabilities run from 0, for an impossible event, to 1, for a certain one."),

 dict(q="If all outcomes in a sample space are equally likely, the theoretical probability of an event E is",
   choices=[
     "the number of outcomes in E divided by the total number of outcomes in the sample space",
     "the total number of outcomes divided by the number of outcomes in E",
     "the number of outcomes in E",
     "1 divided by the number of outcomes in E",
     "the number of outcomes in E multiplied by the total number of outcomes"],
   ans=0,
   why="With equally likely outcomes each carries the same weight, so the event's probability is its share of the sample space."),

 dict(q="If P(E) = 0.28, then the probability of the complement of E is",
   choices=["0.28", "0.36", "0.72", "1.28", "3.57"],
   ans=2,
   why="The complement of E is everything else in the sample space, so its probability is 1 - 0.28 = 0.72."),

 dict(q="An event has probability 0.15. The probability that the event does NOT occur is",
   choices=["0.15", "0.30", "0.85", "0.95", "1.15"],
   ans=2,
   why="P(not E) = 1 - P(E) = 1 - 0.15 = 0.85."),

 dict(q="Which of the following could NOT be the probability of an event?",
   choices=["0", "0.001", "0.5", "1", "1.4"],
   ans=4,
   why="No probability can exceed 1, so 1.4 is impossible; 0 and 1 are both allowed."),

 dict(q="Two fair six-sided dice are rolled. How many outcomes are in the sample space?",
   choices=["6", "12", "21", "36", "216"],
   ans=3,
   why="Each of the 6 results on the first die pairs with each of the 6 on the second, giving 6 x 6 = 36 equally likely outcomes."),

 dict(q="Two fair six-sided dice are rolled. What is the probability that the sum of the two dice is 7?",
   choices=["1/12", "1/9", "1/6", "7/36", "1/3"],
   ans=2,
   why="Six of the 36 equally likely outcomes give a sum of 7, and 6/36 = 1/6."),

 dict(q="Two fair six-sided dice are rolled. What is the probability that the sum is 2?",
   choices=["1/36", "1/18", "1/12", "1/9", "1/6"],
   ans=0,
   why="Only the outcome (1, 1) gives a sum of 2, so the probability is 1/36."),

 dict(q="Two fair six-sided dice are rolled. What is the probability that the sum is NOT 7?",
   choices=["1/6", "5/6", "29/36", "31/36", "35/36"],
   ans=1,
   why="Using the complement, 1 - 1/6 = 5/6; equivalently 30 of the 36 outcomes do not sum to 7."),

 dict(q="Two fair six-sided dice are rolled. What is the probability that the two dice show the same number?",
   choices=["1/36", "1/12", "1/6", "1/3", "1/2"],
   ans=2,
   why="The six doubles among 36 equally likely outcomes give 6/36 = 1/6."),

 dict(q="Two fair six-sided dice are rolled. What is the probability that the sum is at least 10?",
   choices=["1/12", "1/6", "5/36", "1/4", "1/3"],
   ans=1,
   why="Sums of 10, 11 and 12 arise in 3 + 2 + 1 = 6 of the 36 outcomes, and 6/36 = 1/6."),

 dict(q="A fair coin is tossed twice. What is the probability of getting exactly one head?",
   choices=["0.25", "0.33", "0.50", "0.67", "0.75"],
   ans=2,
   why="The sample space is HH, HT, TH, TT, and two of those four equally likely outcomes have exactly one head."),

 dict(q="A fair coin is tossed twice. What is the probability of getting at least one head?",
   choices=["0.25", "0.50", "0.67", "0.75", "1.00"],
   ans=3,
   why="Only TT has no head, so the answer is 1 - 1/4 = 3/4, which is the complement rule doing the work."),

 dict(q="One card is drawn at random from a standard 52-card deck. What is the probability that it is a heart?",
   choices=["1/52", "1/13", "1/4", "1/3", "1/2"],
   ans=2,
   why="There are 13 hearts among 52 cards, and 13/52 = 1/4."),

 dict(q="A single card is drawn at random from a standard 52-card deck. What is the probability that the card is a king?",
   choices=["1/52", "1/26", "1/13", "1/4", "4/13"],
   ans=2,
   why="Four kings among 52 cards give 4/52 = 1/13."),

 dict(q="From a standard 52-card deck, one card is drawn at random. Taking the face cards to be the jack, queen and king of each suit, what is the probability that the card is NOT a face card?",
   choices=["3/13", "4/13", "9/13", "10/13", "12/13"],
   ans=3,
   why="There are 12 face cards, so 52 - 12 = 40 are not, and 40/52 = 10/13."),

 dict(q="A spinner has 8 equal sectors numbered 1 through 8. What is the probability of landing on a number greater than 5?",
   choices=["1/8", "1/4", "3/8", "1/2", "5/8"],
   ans=2,
   why="The numbers 6, 7 and 8 are three of the eight equally likely sectors, so the probability is 3/8."),

 dict(q="A spinner has 8 equal sectors numbered 1 through 8. What is the probability of NOT landing on a multiple of 3?",
   choices=["1/4", "3/8", "1/2", "5/8", "3/4"],
   ans=4,
   why="The multiples of 3 among 1 to 8 are 3 and 6, so 2 of 8 sectors, and 1 - 2/8 = 6/8 = 3/4."),

 dict(q="An event has probability 0. This means the event",
   choices=[
     "is certain to occur",
     "cannot occur",
     "occurs about half the time",
     "has not been observed yet but may occur",
     "has an undefined probability"],
   ans=1,
   why="Probability 0 is the probability of an impossible event, the opposite end of the scale from probability 1."),

 dict(q="A weather forecast states that the probability of rain tomorrow is 0.30. The probability that it does not rain tomorrow is",
   choices=["0.30", "0.50", "0.60", "0.70", "1.30"],
   ans=3,
   why="Rain and no rain are complements, so their probabilities sum to 1 and P(no rain) = 0.70."),

 dict(q="A random process has four possible outcomes with probabilities 0.20, 0.35, 0.15, and p. The value of p must be",
   choices=["0.10", "0.20", "0.30", "0.35", "0.70"],
   ans=2,
   why="The probabilities of all outcomes in a sample space sum to 1, so p = 1 - (0.20 + 0.35 + 0.15) = 0.30."),

 dict(q="A student claims that a probability model assigns probabilities 0.4, 0.3, 0.2, and 0.2 to the four outcomes of a random process. This model is",
   choices=[
     "valid, because every probability is between 0 and 1",
     "invalid, because the four probabilities sum to 1.1 rather than 1",
     "invalid, because two outcomes cannot have the same probability",
     "valid, because there are four outcomes",
     "valid, because the largest probability is less than 0.5"],
   ans=1,
   why="Each value being a legal probability is not enough; the outcomes of a sample space must also account for exactly all of the probability."),

 dict(q="Using the complement rule is most helpful when the event of interest is described using the words",
   choices=[
     "'exactly one'",
     "'at least one', because its complement, 'none', is usually far simpler to count",
     "'the first one'",
     "'equally likely'",
     "'independent'"],
   ans=1,
   why="'At least one' spans many cases while its complement 'none' is a single case, so computing the complement and subtracting from 1 is much less work."),
]
