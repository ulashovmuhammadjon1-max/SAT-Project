# AP STATISTICS 2.5 Mutually Exclusive Events — 25 questions
# CED: Fall 2026, Unit 2. Learning objective 2.5.A, essential knowledge 2.5.A.1
# (joint probability is the probability of the intersection) and 2.5.A.2 (two
# events are mutually exclusive, or disjoint, if they cannot occur at the same
# time, which means P(A and B) = 0).
#
# The trap this topic sets, and the reason several items here are built around
# it: MUTUALLY EXCLUSIVE IS NOT THE SAME AS INDEPENDENT, and in fact two events
# with positive probability that are mutually exclusive are necessarily
# DEPENDENT. If A and B cannot both happen, then learning that B happened tells
# you A definitely did not, so P(A given B) = 0 while P(A) > 0. Students who
# have learned "disjoint means unrelated" get this exactly backwards. Topic 2.7
# takes up independence properly; here the point is made from the disjoint side.
#
# A second recurring error is adding probabilities that are not disjoint. Two
# items give events whose probabilities sum above 1, which is by itself proof
# they cannot be mutually exclusive.
#
# Every probability keyed below is enumerated or computed in verify_s2_5.py.
TOPIC = ("2.5", "Mutually Exclusive Events", 2)

QUESTIONS = [
 dict(q="The joint probability of two events A and B is",
   choices=[
     "the probability that at least one of them occurs",
     "the probability that both of them occur, that is, the probability of their intersection",
     "the sum of their individual probabilities",
     "the probability that neither occurs",
     "the probability of A divided by the probability of B"],
   ans=1,
   why="Joint probability is P(A and B), the probability of the intersection."),

 dict(q="Two events are mutually exclusive, also called disjoint, if",
   choices=[
     "they cannot occur at the same time",
     "they always occur together",
     "knowing one occurred does not change the probability of the other",
     "they have equal probabilities",
     "their probabilities sum to 1"],
   ans=0,
   why="Mutually exclusive means the two events have no outcome in common, so they cannot both happen on the same trial."),

 dict(q="If events A and B are mutually exclusive, then P(A and B) equals",
   choices=["0", "1", "P(A) + P(B)", "P(A) x P(B)", "P(A) - P(B)"],
   ans=0,
   why="There is no outcome belonging to both events, so the intersection is empty and its probability is 0."),

 dict(q="If A and B are mutually exclusive, then P(A or B) equals",
   choices=[
     "P(A) + P(B)",
     "P(A) + P(B) - P(A) x P(B)",
     "P(A) x P(B)",
     "P(A) - P(B)",
     "1 - P(A) - P(B)"],
   ans=0,
   why="The general addition rule subtracts P(A and B), which is 0 for disjoint events, leaving just the sum."),

 dict(q="Events A and B are mutually exclusive, with P(A) = 0.35 and P(B) = 0.40. What is P(A or B)?",
   choices=["0.05", "0.14", "0.40", "0.75", "0.89"],
   ans=3,
   why="For disjoint events the probabilities add: 0.35 + 0.40 = 0.75; 0.14 is the product, which would apply only to independent events."),

 dict(q="Events A and B are mutually exclusive, with P(A) = 0.35 and P(B) = 0.40. What is P(A and B)?",
   choices=["0", "0.14", "0.35", "0.40", "0.75"],
   ans=0,
   why="Mutually exclusive events have an empty intersection, so P(A and B) = 0 regardless of the individual probabilities."),

 dict(q="Events A and B are mutually exclusive, with P(A) = 0.35 and P(B) = 0.40. What is the probability that NEITHER A nor B occurs?",
   choices=["0.00", "0.25", "0.35", "0.60", "0.75"],
   ans=1,
   why="P(A or B) = 0.75, and 'neither' is the complement of 'at least one', so 1 - 0.75 = 0.25."),

 dict(q="A single card is drawn from a standard 52-card deck. Which pair of events is mutually exclusive?",
   choices=[
     "the card is a heart; the card is a king",
     "the card is a heart; the card is red",
     "the card is a heart; the card is a spade",
     "the card is a face card; the card is a king",
     "the card is red; the card is an ace"],
   ans=2,
   why="A card cannot be both a heart and a spade, while the other pairs all share at least one card, such as the king of hearts."),

 dict(q="A single card is drawn from a standard 52-card deck. What is the probability that it is a heart or a spade?",
   choices=["1/13", "1/4", "1/2", "8/13", "3/4"],
   ans=2,
   why="Hearts and spades are disjoint, so the probabilities add: 1/4 + 1/4 = 1/2."),

 dict(q="Drawing one card at random from a standard 52-card deck, what is the probability that the card is a heart AND a king?",
   choices=["0", "1/52", "1/26", "1/13", "17/52"],
   ans=1,
   why="Exactly one card, the king of hearts, is both, so the joint probability is 1/52 and the two events are NOT mutually exclusive."),

 dict(q="For one card drawn at random from a standard 52-card deck, what is the probability of getting a heart or a king?",
   choices=["1/4", "4/13", "17/52", "1/2", "16/13"],
   ans=1,
   why="These events overlap, so P(heart or king) = 13/52 + 4/52 - 1/52 = 16/52 = 4/13; adding without subtracting the overlap gives the wrong 17/52."),

 dict(q="Two fair six-sided dice are rolled. Which pair of events is mutually exclusive?",
   choices=[
     "the sum is 7; the first die shows 3",
     "the sum is 7; the sum is 11",
     "the sum is even; the first die shows 2",
     "the sum is at least 8; the sum is at least 10",
     "the two dice match; the sum is even"],
   ans=1,
   why="A single roll cannot have a sum that is both 7 and 11, whereas each other pair has outcomes belonging to both events."),

 dict(q="Two fair six-sided dice are rolled. What is the probability that the sum is 7 or 11?",
   choices=["1/9", "1/6", "2/9", "1/4", "8/11"],
   ans=2,
   why="Six outcomes give a sum of 7 and two give 11, and the events are disjoint, so (6 + 2)/36 = 8/36 = 2/9."),

 dict(q="Events A and B satisfy P(A) = 0.6 and P(B) = 0.7. It follows that A and B",
   choices=[
     "must be mutually exclusive",
     "cannot be mutually exclusive, because otherwise P(A or B) would be 1.3, which exceeds 1",
     "must be independent",
     "must have P(A and B) = 0.42",
     "cannot both occur"],
   ans=1,
   why="Disjoint events would force the probabilities to add, and 0.6 + 0.7 = 1.3 is impossible, so the two events must overlap."),

 dict(q="Events A and B satisfy P(A) = 0.6 and P(B) = 0.7. What is the smallest possible value of P(A and B)?",
   choices=["0.00", "0.30", "0.42", "0.60", "0.70"],
   ans=1,
   why="Since P(A or B) cannot exceed 1, P(A and B) = P(A) + P(B) - P(A or B) is at least 1.3 - 1 = 0.30."),

 dict(q="An event A has P(A) = 0.45. Are A and its complement mutually exclusive?",
   choices=[
     "Yes, because an event and its complement cannot both occur, so their joint probability is 0",
     "No, because their probabilities sum to 1",
     "Yes, but only because 0.45 is less than 0.5",
     "No, because every event overlaps its complement",
     "It cannot be determined without more information"],
   ans=0,
   why="'A occurs' and 'A does not occur' have no outcome in common, so they are always mutually exclusive, and they are also exhaustive."),

 dict(q="Two events A and B are mutually exclusive, and both have probability greater than 0. It follows that A and B are",
   choices=[
     "independent",
     "dependent, because knowing that B occurred tells you A definitely did not, changing A's probability from a positive number to 0",
     "independent only if P(A) = P(B)",
     "neither independent nor dependent",
     "always equally likely"],
   ans=1,
   why="Disjointness is the strongest possible form of dependence between two positive-probability events: one occurring rules the other out entirely."),

 dict(q="A student says, 'A and B are mutually exclusive, so they must be independent.' This reasoning is",
   choices=[
     "correct, since disjoint events do not affect one another",
     "incorrect: disjoint events with positive probability are dependent, because P(A given B) = 0 while P(A) > 0",
     "correct, but only when P(A) + P(B) = 1",
     "incorrect, because mutually exclusive events cannot have probabilities",
     "correct whenever the sample space is finite"],
   ans=1,
   why="Mutual exclusivity and independence are different ideas, and for events of positive probability they are in fact incompatible."),

 dict(q="For two events with P(A) = 0.30 and P(B) = 0.50, it is reported that P(A or B) = 0.80. This tells you that",
   choices=[
     "the events are mutually exclusive, since 0.30 + 0.50 = 0.80 leaves nothing to subtract",
     "the events overlap",
     "the events are independent",
     "the report must be in error",
     "P(A and B) = 0.15"],
   ans=0,
   why="The addition rule gives P(A and B) = 0.30 + 0.50 - 0.80 = 0, which is exactly the definition of mutually exclusive."),

 dict(q="For two events with P(A) = 0.30 and P(B) = 0.50, it is reported that P(A or B) = 0.65. The joint probability P(A and B) is",
   choices=["0.00", "0.15", "0.20", "0.35", "0.80"],
   ans=1,
   why="Rearranging the addition rule, P(A and B) = 0.30 + 0.50 - 0.65 = 0.15, so the events are not mutually exclusive."),

 dict(q="A spinner has 10 equal sectors numbered 1 through 10. Let A be 'the result is a multiple of 3' and B be 'the result is a multiple of 5'. Are A and B mutually exclusive?",
   choices=[
     "Yes, because no number from 1 to 10 is a multiple of both 3 and 5",
     "No, because 15 is a multiple of both",
     "Yes, because 3 and 5 are both prime",
     "No, because 10 is a multiple of 5",
     "It cannot be determined"],
   ans=0,
   why="Within 1 to 10 the multiples of 3 are 3, 6, 9 and of 5 are 5, 10, with no overlap; 15 would overlap but is outside the sample space."),

 dict(q="For that same spinner, what is the probability of getting a multiple of 3 or a multiple of 5?",
   choices=["0.2", "0.3", "0.5", "0.6", "0.8"],
   ans=2,
   why="Three sectors are multiples of 3 and two are multiples of 5, and the events are disjoint here, so (3 + 2)/10 = 0.5."),

 dict(q="Three events A, B and C are pairwise mutually exclusive with P(A) = 0.2, P(B) = 0.3 and P(C) = 0.4. What is the probability that none of the three occurs?",
   choices=["0.0", "0.1", "0.3", "0.9", "1.0"],
   ans=1,
   why="Disjoint events add, so P(A or B or C) = 0.9, and the complement gives 1 - 0.9 = 0.1."),

 dict(q="In a two-way table of two categorical variables, the events 'the unit falls in row 1' and 'the unit falls in row 2' are",
   choices=[
     "mutually exclusive, because each observational unit is counted in exactly one row",
     "independent, because rows and columns are separate",
     "neither mutually exclusive nor exhaustive",
     "always equally likely",
     "impossible to classify"],
   ans=0,
   why="A unit is cross-classified into exactly one row and one column, so distinct rows are disjoint events, and together the rows exhaust the table."),

 dict(q="The most reliable way to decide whether two events are mutually exclusive is to",
   choices=[
     "check whether their probabilities sum to 1",
     "determine whether any outcome belongs to both events, equivalently whether P(A and B) = 0",
     "check whether P(A given B) equals P(A)",
     "check whether the events have equal probabilities",
     "check whether the sample space is finite"],
   ans=1,
   why="Mutual exclusivity is exactly the statement that the intersection is empty; checking whether P(A given B) equals P(A) tests independence, which is a different property."),
]
