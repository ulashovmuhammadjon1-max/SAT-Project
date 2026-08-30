# AP STATISTICS 2.7 Independent Events and Unions of Events — 25 questions
# CED: Fall 2026, Unit 2. Learning objective 2.7.A, essential knowledge 2.7.A.1
# (A and B are independent if and only if knowing whether A occurred does not
# change the probability of B, equivalently P(A given B) = P(A)), 2.7.A.2 (the
# union is "A or B, or both") and 2.7.A.3 (the general addition rule,
# P(A or B) = P(A) + P(B) - P(A and B)).
#
# Topic 2.5 attacked the mutually-exclusive/independent confusion from the
# disjoint side. This module attacks it from the independence side, and adds the
# two errors specific to unions:
#   using P(A) + P(B) when the events overlap, which double-counts the overlap;
#   using P(A) x P(B) for a joint probability when the events are NOT independent.
#
# The independence TEST is treated as a computation, not a feeling: multiply the
# marginals and compare with the joint. Two items give a two-way table and ask
# for that comparison, one where independence holds exactly and one where it
# fails, so the same procedure has to produce opposite verdicts.
#
# All values are recomputed in verify_s2_7.py.
TOPIC = ("2.7", "Independent Events and Unions of Events", 2)

# Independence holds exactly: every cell equals row total x column total / grand.
TABLE_IND = dict(
    headers=["", "Column 1", "Column 2", "Total"],
    rows=[["Row 1", "24", "36", "60"],
          ["Row 2", "16", "24", "40"],
          ["Total", "40", "60", "100"]])

# Independence fails.
TABLE_DEP = dict(
    headers=["", "Column 1", "Column 2", "Total"],
    rows=[["Row 1", "35", "25", "60"],
          ["Row 2", "5", "35", "40"],
          ["Total", "40", "60", "100"]])

QUESTIONS = [
 dict(q="Events A and B are independent if and only if",
   choices=[
     "they cannot occur at the same time",
     "knowing whether A has occurred does not change the probability that B will occur",
     "their probabilities are equal",
     "their probabilities sum to 1",
     "P(A and B) = 0"],
   ans=1,
   why="Independence is about information: learning that one event happened leaves the other's probability unchanged."),

 dict(q="If A and B are independent, then P(A given B) equals",
   choices=["0", "1", "P(A)", "P(B)", "P(A) x P(B)"],
   ans=2,
   why="That equality is the definition of independence written as a conditional probability."),

 dict(q="If A and B are independent, then P(A and B) equals",
   choices=[
     "0",
     "P(A) + P(B)",
     "P(A) x P(B)",
     "P(A) + P(B) - 1",
     "P(A) divided by P(B)"],
   ans=2,
   why="Substituting P(B given A) = P(B) into the general multiplication rule leaves the plain product."),

 dict(q="The general addition rule states that P(A or B) equals",
   choices=[
     "P(A) + P(B)",
     "P(A) + P(B) - P(A and B)",
     "P(A) x P(B)",
     "P(A) + P(B) + P(A and B)",
     "1 - P(A) - P(B)"],
   ans=1,
   why="Adding the two probabilities counts the overlap twice, so the joint probability is subtracted once to correct it."),

 dict(q="In probability, the event 'A or B' means",
   choices=[
     "A occurs, or B occurs, or both occur",
     "exactly one of A and B occurs",
     "A occurs but B does not",
     "both A and B occur",
     "neither A nor B occurs"],
   ans=0,
   why="The union in probability is inclusive: it includes the case where both events happen."),

 dict(q="Events A and B are independent with P(A) = 0.4 and P(B) = 0.5. What is P(A and B)?",
   choices=["0.05", "0.10", "0.20", "0.45", "0.90"],
   ans=2,
   why="For independent events the joint probability is the product, 0.4 x 0.5 = 0.20."),

 dict(q="Events A and B are independent with P(A) = 0.4 and P(B) = 0.5. What is P(A or B)?",
   choices=["0.20", "0.60", "0.70", "0.90", "1.10"],
   ans=2,
   why="P(A or B) = 0.4 + 0.5 - 0.20 = 0.70; the answer 0.90 forgets to subtract the overlap."),

 dict(q="Events A and B have P(A) = 0.3, P(B) = 0.6, and P(A and B) = 0.18. Are A and B independent?",
   choices=[
     "Yes, because P(A) x P(B) = 0.18, which equals the given joint probability",
     "No, because P(A) is not equal to P(B)",
     "Yes, because 0.18 is less than both 0.3 and 0.6",
     "No, because P(A and B) is not 0",
     "It cannot be determined without P(A or B)"],
   ans=0,
   why="The test is whether the joint probability equals the product of the marginals, and here 0.3 x 0.6 = 0.18 exactly."),

 dict(q="Events A and B have P(A) = 0.3, P(B) = 0.6, and P(A and B) = 0.25. Are A and B independent?",
   choices=[
     "Yes, because both probabilities are between 0 and 1",
     "No, because P(A) x P(B) = 0.18, which does not equal the given joint probability of 0.25",
     "Yes, because 0.25 is close to 0.18",
     "No, because the events are mutually exclusive",
     "It cannot be determined"],
   ans=1,
   why="The product of the marginals is 0.18 and the actual joint probability is 0.25, so knowing one event occurred does change the other's probability."),

 dict(q="For events with P(A) = 0.3, P(B) = 0.6, and P(A and B) = 0.25, what is P(A or B)?",
   choices=["0.18", "0.65", "0.72", "0.90", "1.15"],
   ans=1,
   why="P(A or B) = 0.3 + 0.6 - 0.25 = 0.65."),

 dict(q="Events A and B have P(A) = 0.5, P(B) = 0.4, and P(A or B) = 0.7. What is P(A and B)?",
   choices=["0.00", "0.10", "0.20", "0.30", "0.90"],
   ans=2,
   why="Rearranging the addition rule, P(A and B) = 0.5 + 0.4 - 0.7 = 0.20."),

 dict(q="For those same events with P(A) = 0.5, P(B) = 0.4, and P(A or B) = 0.7, the events are",
   choices=[
     "mutually exclusive",
     "independent, because P(A) x P(B) = 0.20 equals the joint probability found from the addition rule",
     "dependent, because the joint probability is not 0",
     "impossible to classify",
     "both independent and mutually exclusive"],
   ans=1,
   why="The addition rule gives P(A and B) = 0.20, and 0.5 x 0.4 = 0.20 as well, so the independence test is satisfied."),

 dict(q="A two-way table of 100 observations is shown. Multiplying the marginal proportions and comparing with the joint proportion for Row 1 and Column 1 shows that the two variables are",
   table=TABLE_IND,
   choices=[
     "independent, because 0.60 x 0.40 = 0.24 matches the joint proportion 24/100 = 0.24",
     "dependent, because 24 is not equal to 40",
     "independent, because the totals are round numbers",
     "dependent, because the row totals differ",
     "impossible to assess from counts"],
   ans=0,
   why="Row 1 is 0.60 of the table and Column 1 is 0.40, and their product 0.24 is exactly the observed joint proportion, and the same holds in every other cell."),

 dict(q="A different two-way table of 100 observations is shown. Applying the same independence check to Row 1 and Column 1 shows that the two variables are",
   table=TABLE_DEP,
   choices=[
     "independent, because 0.60 x 0.40 = 0.24 matches the joint proportion",
     "dependent, because 0.60 x 0.40 = 0.24 but the joint proportion is 35/100 = 0.35",
     "independent, because both tables have the same margins",
     "dependent, because the table has four cells",
     "impossible to assess without a third variable"],
   ans=1,
   why="The margins are the same as in the previous table, but the joint proportion 0.35 is well above the 0.24 independence would require, so the variables are associated."),

 dict(q="A fair coin is tossed twice. The events 'the first toss is heads' and 'the second toss is heads' are",
   choices=[
     "mutually exclusive",
     "independent, because the result of the first toss does not change the probability for the second",
     "dependent, because both involve the same coin",
     "dependent, because the tosses happen in sequence",
     "neither independent nor dependent"],
   ans=1,
   why="Nothing about the coin changes between tosses, so the first result carries no information about the second."),

 dict(q="Two cards are drawn without replacement from a standard deck. The events 'the first card is a heart' and 'the second card is a heart' are",
   choices=[
     "independent, because the deck is well shuffled",
     "dependent, because removing the first card changes the composition of the deck for the second draw",
     "mutually exclusive",
     "independent, because both have probability 1/4",
     "impossible to compare"],
   ans=1,
   why="Once a heart is removed, 12 of 51 remaining cards are hearts rather than 13 of 52, so the first draw changes the second draw's probability."),

 dict(q="A student writes 'A and B are mutually exclusive, therefore P(A and B) = P(A) x P(B).' This is",
   choices=[
     "correct, because mutually exclusive events are independent",
     "incorrect, because P(A and B) = 0 for mutually exclusive events, while the product rule applies to independent events",
     "correct, provided P(A) and P(B) are both less than 0.5",
     "incorrect, because the product rule never holds",
     "correct only when P(A) = P(B)"],
   ans=1,
   why="The two conditions belong to different rules, and unless one of the events has probability 0 they cannot both hold at once."),

 dict(q="A component fails with probability 0.2, independently of the others. Three such components are used. What is the probability that all three fail?",
   choices=["0.008", "0.060", "0.200", "0.488", "0.600"],
   ans=0,
   why="Independence lets the probabilities multiply, so 0.2 x 0.2 x 0.2 = 0.008."),

 dict(q="A component fails with probability 0.2, independently of the others. For three such components, what is the probability that at least one fails?",
   choices=["0.008", "0.200", "0.488", "0.512", "0.600"],
   ans=2,
   why="It is easier to compute the complement: all three work with probability 0.8 cubed = 0.512, so at least one fails with probability 1 - 0.512 = 0.488."),

 dict(q="For three components that each fail with probability 0.2, independently of one another, what is the probability that NONE of them fails?",
   choices=["0.008", "0.200", "0.488", "0.512", "0.800"],
   ans=3,
   why="Each works with probability 0.8, and independence lets them multiply: 0.8 cubed = 0.512."),

 dict(q="Two events each have probability 0.5. If they are independent, P(A or B) is 0.75; if they are mutually exclusive, P(A or B) is 1.00. This shows that",
   choices=[
     "independence and mutual exclusivity give the same answer",
     "the union depends on the joint probability, which is 0.25 under independence and 0 under mutual exclusivity",
     "one of the two calculations must be wrong",
     "mutually exclusive events always have a smaller union",
     "the addition rule does not apply to independent events"],
   ans=1,
   why="Both use P(A) + P(B) - P(A and B); only the joint probability differs, and that is exactly what distinguishes the two assumptions."),

 dict(q="If P(A) = 0.5 and P(B) = 0.5 and the events are independent, what is the probability that NEITHER occurs?",
   choices=["0.00", "0.25", "0.50", "0.75", "1.00"],
   ans=1,
   why="Neither occurring means both complements occur, and independence gives 0.5 x 0.5 = 0.25; equivalently 1 - 0.75."),

 dict(q="Events A and B are independent. It follows that the complement of A and the event B are",
   choices=[
     "also independent",
     "mutually exclusive",
     "dependent",
     "equally likely",
     "impossible to relate"],
   ans=0,
   why="If knowing B tells you nothing about whether A occurred, it equally tells you nothing about whether A failed to occur, so independence carries over to the complement."),

 dict(q="Which of the following is the correct way to test whether two events are independent, given a two-way table of counts?",
   choices=[
     "Check whether any cell is empty",
     "Check whether the joint proportion equals the product of the two corresponding marginal proportions",
     "Check whether the row totals equal the column totals",
     "Check whether the counts are all even",
     "Check whether the grand total is at least 100"],
   ans=1,
   why="Independence is precisely the statement that every joint proportion factors into the product of its marginals, which is a calculation the table supports directly."),

 dict(q="For two events with P(A) = 0.7 and P(B) = 0.2, a student reports P(A or B) = 0.9 and also P(A and B) = 0.14. These two reports together imply that",
   choices=[
     "the events are independent and mutually exclusive at once",
     "the reports are inconsistent, since the addition rule with P(A and B) = 0.14 gives P(A or B) = 0.76, not 0.9",
     "the events are certainly independent",
     "P(A or B) must be 1.0",
     "the reports are consistent"],
   ans=1,
   why="The two reports cannot both be right: 0.7 + 0.2 - 0.14 = 0.76, and 0.9 is what you get by forgetting to subtract the overlap."),
]
