# AP STATISTICS 2.6 Conditional Probability — 25 questions
# CED: Fall 2026, Unit 2. Learning objective 2.6.A, essential knowledge 2.6.A.1
# (P(A given B) = P(A and B) / P(B)) and 2.6.A.2 (the general multiplication
# rule, P(A and B) = P(A) x P(B given A)).
#
# The error this topic exists to expose is REVERSING THE CONDITION. P(A given B)
# and P(B given A) are different numbers, and the screening-test table below is
# built so the gap between them is impossible to miss: the test catches 85% of
# those who have the disease, yet fewer than half of those who test positive
# actually have it. Students read the first figure and report the second.
#
# TABLE_Z, 1,000 people screened:
#                 has disease   no disease   total
#     positive         85            90        175
#     negative         15           810        825
#     total           100           900       1000
#   P(positive given disease) = 85/100  = 0.85
#   P(disease given positive) = 85/175  = 0.486
#   P(negative given no disease) = 810/900 = 0.90
#
# The without-replacement items are the other half of the topic: the second
# draw's probability depends on the first, which is the general multiplication
# rule made concrete. All values are recomputed in verify_s2_6.py.
TOPIC = ("2.6", "Conditional Probability", 2)

TABLE_Z = dict(
    headers=["Test result", "Has the disease", "Does not have the disease", "Total"],
    rows=[["Positive", "85", "90", "175"],
          ["Negative", "15", "810", "825"],
          ["Total", "100", "900", "1000"]])

QUESTIONS = [
 dict(q="The conditional probability of event A given that event B has occurred is defined as",
   choices=[
     "P(A and B) divided by P(B)",
     "P(A and B) divided by P(A)",
     "P(A) multiplied by P(B)",
     "P(A) plus P(B) minus P(A and B)",
     "P(B) divided by P(A and B)"],
   ans=0,
   why="Conditioning on B restricts attention to the outcomes in B, so the joint probability is rescaled by dividing by P(B)."),

 dict(q="The general multiplication rule states that P(A and B) equals",
   choices=[
     "P(A) x P(B)",
     "P(A) x P(B given A)",
     "P(A) + P(B given A)",
     "P(A given B) divided by P(B)",
     "P(A) + P(B) - 1"],
   ans=1,
   why="The joint probability is the probability of the first event times the conditional probability of the second given the first; the plain product requires independence."),

 dict(q="Events A and B have P(A and B) = 0.18 and P(B) = 0.45. What is P(A given B)?",
   choices=["0.081", "0.180", "0.400", "0.450", "2.500"],
   ans=2,
   why="P(A given B) = 0.18/0.45 = 0.40."),

 dict(q="Events A and B have P(A and B) = 0.18 and P(A) = 0.30. What is P(B given A)?",
   choices=["0.054", "0.180", "0.300", "0.600", "1.667"],
   ans=3,
   why="P(B given A) = 0.18/0.30 = 0.60, which is a different number from P(A given B) computed from the same joint probability."),

 dict(q="Events A and B have P(A) = 0.40 and P(B given A) = 0.25. What is P(A and B)?",
   choices=["0.100", "0.150", "0.250", "0.400", "0.650"],
   ans=0,
   why="By the general multiplication rule, P(A and B) = 0.40 x 0.25 = 0.10."),

 dict(q="A screening test was given to 1,000 people, with results shown. What is the probability that a randomly chosen person from this group tests positive?",
   table=TABLE_Z,
   choices=["0.085", "0.100", "0.175", "0.486", "0.825"],
   ans=2,
   why="175 of the 1,000 people tested positive, and 175/1000 = 0.175."),

 dict(q="For the screening data, what is the probability that a randomly chosen person from this group has the disease?",
   table=TABLE_Z,
   choices=["0.085", "0.100", "0.175", "0.486", "0.900"],
   ans=1,
   why="100 of the 1,000 people have the disease, and 100/1000 = 0.100."),

 dict(q="For the screening data, what is the probability that a randomly chosen person both has the disease and tests positive?",
   table=TABLE_Z,
   choices=["0.085", "0.100", "0.175", "0.486", "0.850"],
   ans=0,
   why="85 of the 1,000 people are in that single cell, and 85/1000 = 0.085."),

 dict(q="Among the people who HAVE the disease, what proportion test positive?",
   table=TABLE_Z,
   choices=["0.085", "0.150", "0.486", "0.850", "0.900"],
   ans=3,
   why="Restricting to the 100 people with the disease, 85 test positive, and 85/100 = 0.85."),

 dict(q="Among the people who test POSITIVE, what proportion actually have the disease?",
   table=TABLE_Z,
   choices=["0.085", "0.100", "0.486", "0.850", "0.914"],
   ans=2,
   why="Restricting to the 175 who test positive, 85 have the disease, and 85/175 = 0.486; this is not the same as the 0.85 who test positive among those with the disease."),

 dict(q="The values 0.85 and 0.486 from the screening data differ because",
   table=TABLE_Z,
   choices=[
     "one of the calculations must be wrong",
     "they condition on different events: one restricts to those with the disease, the other to those who test positive",
     "the table is inconsistent",
     "0.486 is the complement of 0.85",
     "conditional probabilities are only approximate"],
   ans=1,
   why="P(positive given disease) and P(disease given positive) have different denominators, 100 and 175, so there is no reason for them to agree."),

 dict(q="Among the people who do NOT have the disease, what proportion test negative?",
   table=TABLE_Z,
   choices=["0.810", "0.900", "0.914", "0.982", "0.990"],
   ans=1,
   why="Restricting to the 900 without the disease, 810 test negative, and 810/900 = 0.90."),

 dict(q="Among the people who test NEGATIVE, what proportion do not have the disease?",
   table=TABLE_Z,
   choices=["0.810", "0.900", "0.918", "0.982", "1.000"],
   ans=3,
   why="Restricting to the 825 who test negative, 810 do not have the disease, and 810/825 = 0.982."),

 dict(q="For the screening data, what is the probability that a person tests positive given that they do NOT have the disease?",
   table=TABLE_Z,
   choices=["0.090", "0.100", "0.150", "0.486", "0.514"],
   ans=1,
   why="Restricting to the 900 people without the disease, 90 test positive, and 90/900 = 0.100; the distractor 0.090 divides by the 1,000 people screened instead of by the 900 being conditioned on."),

 dict(q="A bag contains 5 red marbles and 3 blue marbles. Two marbles are drawn at random without replacement. What is the probability that the second marble is red, given that the first was red?",
   choices=["3/8", "4/8", "4/7", "5/8", "5/7"],
   ans=2,
   why="After a red marble is removed, 4 of the remaining 7 marbles are red, so the conditional probability is 4/7."),

 dict(q="From that same bag of 5 red and 3 blue marbles, two are drawn without replacement. What is the probability that BOTH are red?",
   choices=["5/28", "5/14", "25/64", "5/8", "9/14"],
   ans=1,
   why="By the multiplication rule, (5/8)(4/7) = 20/56 = 5/14; squaring 5/8 would incorrectly treat the draws as independent."),

 dict(q="Drawing two marbles without replacement from that same bag of 5 red and 3 blue, what is the probability that the first is red and the second is blue?",
   choices=["3/28", "15/56", "15/64", "5/14", "3/8"],
   ans=1,
   why="(5/8)(3/7) = 15/56, since after one red is removed 3 of the 7 remaining marbles are blue."),

 dict(q="Two cards are drawn without replacement from a standard 52-card deck. What is the probability that both are hearts?",
   choices=["1/17", "1/16", "1/13", "13/204", "1/4"],
   ans=0,
   why="(13/52)(12/51) = 156/2652 = 1/17; treating the draws as independent would give the incorrect (1/4)(1/4)."),

 dict(q="Two cards are drawn WITH replacement from a standard 52-card deck, the first being returned and the deck shuffled before the second draw. What is the probability that both are hearts?",
   choices=["1/17", "1/16", "1/8", "1/4", "1/2"],
   ans=1,
   why="Replacing the card restores the original deck, so the draws are independent and the probability is (1/4)(1/4) = 1/16."),

 dict(q="When drawing without replacement, the outcome of the first draw affects the second because",
   choices=[
     "the composition of what remains has changed, so the conditional probability of the second draw differs from its unconditional probability",
     "the two draws are always mutually exclusive",
     "probabilities cannot be computed for repeated draws",
     "the sample space grows after each draw",
     "the first draw has probability 1"],
   ans=0,
   why="Removing an item changes both the numerator and the denominator for the next draw, which is precisely dependence."),

 dict(q="A student computes P(A given B) and obtains 1.4. This result",
   choices=[
     "is possible when A and B overlap heavily",
     "must be an error, because a conditional probability is still a probability and cannot exceed 1",
     "means A and B are independent",
     "means A and B are mutually exclusive",
     "should be reported as 0.4"],
   ans=1,
   why="A conditional probability obeys the same rules as any probability, so a value above 1 signals a mistake, most often dividing by the joint probability instead of by P(B)."),

 dict(q="If P(B) = 0, then P(A given B) is",
   choices=[
     "0",
     "1",
     "undefined, because the definition requires dividing by P(B)",
     "equal to P(A)",
     "equal to P(A and B)"],
   ans=2,
   why="Conditioning on an event that cannot occur has no meaning, and the formula would require division by zero."),

 dict(q="In a class, 60% of students take Spanish, and among the Spanish students 25% also take Art. What percent of the whole class takes both Spanish and Art?",
   choices=["15%", "25%", "35%", "60%", "85%"],
   ans=0,
   why="By the general multiplication rule, 0.60 x 0.25 = 0.15, so 15 percent of the class takes both."),

 dict(q="In a shipment, 8% of items are defective. Among defective items, 70% are detected by inspection. What proportion of all items are defective AND detected?",
   choices=["0.056", "0.070", "0.080", "0.114", "0.780"],
   ans=0,
   why="0.08 x 0.70 = 0.056, again the general multiplication rule with the conditional probability supplied directly."),

 dict(q="A newspaper reports that 90% of people who develop a certain illness had eaten a particular food, and concludes that eating the food makes illness very likely. The flaw is that the report gives",
   choices=[
     "P(ate the food given ill) when the claim requires P(ill given ate the food), and these are different quantities",
     "a probability greater than 1",
     "a joint probability instead of a marginal one",
     "the complement of the quantity of interest",
     "no probability at all"],
   ans=0,
   why="Almost everyone may eat that food, in which case a high P(ate it given ill) says nothing about the risk of illness for someone who eats it; the conditions must not be swapped."),
]
