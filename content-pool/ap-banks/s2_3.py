# AP STATISTICS 2.3 Estimating Probabilities Using Simulation — 25 questions
# CED: Fall 2026, Unit 2. Skill 3.C, calculating and estimating probabilities.
#
# A simulation estimates a probability as (number of trials with the outcome) /
# (total number of trials). Three things are tested here and each is a place
# students go wrong:
#
#   1. ASSIGNING DIGITS. To simulate a probability p with two-digit numbers
#      00-99 you need exactly 100p of the 100 equally likely labels. Off-by-one
#      is the classic error: 00-34 is THIRTY-FIVE labels, not thirty-four, so it
#      simulates 0.35 and not 0.34.
#   2. WHAT COUNTS AS ONE TRIAL. A trial is one complete repetition of the whole
#      scenario, not one digit. Simulating "how many of 4 free throws are made"
#      uses four digits per trial.
#   3. WHAT THE ESTIMATE IS AND IS NOT. It is an estimate; more trials make it
#      more reliable but no number of trials makes it exact, and a simulation
#      never proves the true probability.
#
# TABLE_SIM records 50 simulated trials of "number of heads in four tosses of a
# fair coin": 0 heads 3 times, 1 head 12, 2 heads 19, 3 heads 12, 4 heads 4.
# Every estimate keyed from it is recomputed in verify_s2_3.py, which also
# checks the digit-assignment counts by actually counting the labels.
TOPIC = ("2.3", "Estimating Probabilities Using Simulation", 2)

TABLE_SIM = dict(
    headers=["Number of heads in 4 tosses", "Number of trials"],
    rows=[["0", "3"], ["1", "12"], ["2", "19"], ["3", "12"], ["4", "4"],
          ["Total", "50"]])

QUESTIONS = [
 dict(q="A simulation estimates the probability of an outcome as",
   choices=[
     "the number of trials in which the outcome occurred, divided by the total number of trials",
     "the total number of trials divided by the number of successes",
     "the number of digits used in each trial",
     "the largest result observed in any trial",
     "one divided by the number of possible outcomes"],
   ans=0,
   why="An estimated probability from a simulation is the observed relative frequency of the outcome across the trials."),

 dict(q="In a simulation, one trial is",
   choices=[
     "one random digit",
     "one complete repetition of the entire scenario being modelled",
     "one success",
     "the whole simulation",
     "one row of a random number table"],
   ans=1,
   why="A trial reproduces the whole situation once, so a scenario involving four free throws needs four random digits to make a single trial."),

 dict(q="A simulation is run 100 times and then 10,000 times. Compared with the estimate from 100 trials, the estimate from 10,000 trials will",
   choices=[
     "be exactly equal to the true probability",
     "tend to be closer to the true probability, though it is still an estimate",
     "tend to be further from the true probability",
     "be identical to the estimate from 100 trials",
     "have a larger sample-to-sample variability"],
   ans=1,
   why="More trials reduce the variability of the estimate around the true probability, but a simulation never delivers the exact value."),

 dict(q="To simulate an event with probability 0.35 using two-digit random numbers 00 through 99, a correct assignment is to count as a success the numbers",
   choices=["00 to 34", "00 to 35", "01 to 34", "01 to 36", "35 to 99"],
   ans=0,
   why="The labels 00 through 34 number thirty-five in all, which is exactly 35 of the 100 equally likely two-digit labels; 00 through 35 would be thirty-six."),

 dict(q="Using two-digit random numbers 00 through 99, how many labels must be assigned to 'success' to simulate a probability of 0.62?",
   choices=["6", "38", "61", "62", "63"],
   ans=3,
   why="Each of the 100 labels carries probability 0.01, so 62 of them are needed."),

 dict(q="Using single random digits 0 through 9, an event with probability 0.30 can be simulated by counting as a success the digits",
   choices=["0, 1, and 2", "0, 1, 2, and 3", "1, 2, and 3, only", "3 only", "0 through 6"],
   ans=0,
   why="Three of the ten equally likely digits give probability 0.3, and 0, 1, 2 is such a set; 0 through 3 is four digits, giving 0.4."),

 dict(q="A basketball player makes 70% of her free throws. To simulate one free throw with a single random digit 0 through 9, a correct assignment is",
   choices=[
     "digits 0 through 6 are a make, 7 through 9 are a miss",
     "digits 0 through 7 are a make, 8 and 9 are a miss",
     "digit 7 is a make, all others a miss",
     "digits 1 through 7 are a make, 8, 9 and 0 are a miss, with 0 discarded",
     "digits 0 through 6 are a miss, 7 through 9 are a make"],
   ans=0,
   why="Digits 0 through 6 are seven of the ten equally likely digits, which is the 0.7 required; assigning the three digits to a make would simulate 0.3 instead."),

 dict(q="To simulate the number of free throws that player makes out of four attempts, one trial should consist of",
   choices=[
     "one random digit",
     "four random digits, one for each attempt",
     "seven random digits",
     "ten random digits",
     "as many digits as it takes to get a make"],
   ans=1,
   why="A trial must reproduce the whole scenario once, and the scenario involves four attempts."),

 dict(q="A simulation of an event using two-digit numbers assigns 00 through 07 to success and ignores nothing. The probability being simulated is",
   choices=["0.07", "0.08", "0.70", "0.80", "0.93"],
   ans=1,
   why="The labels 00, 01, 02, 03, 04, 05, 06, and 07 are eight labels out of 100, so the probability simulated is 0.08."),

 dict(q="Fifty trials were run simulating the number of heads in four tosses of a fair coin, with results shown. Based on this simulation, what is the estimated probability of getting exactly 2 heads?",
   table=TABLE_SIM,
   choices=["0.06", "0.24", "0.32", "0.38", "0.50"],
   ans=3,
   why="Exactly 2 heads occurred in 19 of the 50 trials, and 19/50 = 0.38."),

 dict(q="From that same simulation, what is the estimated probability of getting at least 3 heads in four tosses?",
   table=TABLE_SIM,
   choices=["0.08", "0.24", "0.32", "0.38", "0.70"],
   ans=2,
   why="Three heads occurred 12 times and four heads 4 times, so 16 of 50 trials, and 16/50 = 0.32."),

 dict(q="From that same simulation, what is the estimated probability of getting at most 1 head?",
   table=TABLE_SIM,
   choices=["0.06", "0.24", "0.30", "0.38", "0.62"],
   ans=2,
   why="Zero heads occurred 3 times and one head 12 times, so 15 of 50 trials, and 15/50 = 0.30."),

 dict(q="From that same simulation, what is the estimated probability of getting 4 heads?",
   table=TABLE_SIM,
   choices=["0.04", "0.06", "0.08", "0.24", "0.40"],
   ans=2,
   why="Four heads occurred in 4 of the 50 trials, and 4/50 = 0.08."),

 dict(q="From that same simulation, what is the estimated probability of getting at least 1 head?",
   table=TABLE_SIM,
   choices=["0.06", "0.30", "0.70", "0.94", "0.97"],
   ans=3,
   why="Zero heads occurred in 3 trials, so at least one head occurred in 47 of 50, and 47/50 = 0.94."),

 dict(q="The theoretical probability of exactly 2 heads in four tosses of a fair coin is 0.375, while this simulation estimated 0.38. The small difference is best explained as",
   table=TABLE_SIM,
   choices=[
     "an error in the simulation",
     "ordinary variability, since a simulation estimates a probability rather than computing it exactly",
     "evidence that the coin is not fair",
     "evidence that 50 trials is too few for any conclusion",
     "a rounding mistake in the theoretical value"],
   ans=1,
   why="An estimate from 50 trials will not land exactly on the theoretical value, and 0.38 against 0.375 is well within the variation such a simulation produces."),

 dict(q="A researcher wants to simulate drawing a card and getting a heart, where the probability is 0.25. Using two-digit numbers 00 through 99, which assignment is correct?",
   choices=[
     "00 through 24 is a heart",
     "00 through 25 is a heart",
     "01 through 24 is a heart",
     "25 through 99 is a heart",
     "any number ending in 5 is a heart"],
   ans=0,
   why="00 through 24 is twenty-five labels out of a hundred, giving exactly 0.25; 00 through 25 is twenty-six."),

 dict(q="Using a random number table to simulate an event with probability 1/3, a student decides to use single digits and let 0, 1, 2 be a success and ignore nothing else. This assignment simulates a probability of",
   choices=["0.30", "0.33", "1/3 exactly", "0.20", "0.10"],
   ans=0,
   why="Three of the ten digits gives exactly 0.30, not 1/3; simulating 1/3 exactly with single digits requires discarding a digit, for example using 1, 2, 3 for success, 4, 5, 6 for one failure type, 7, 8, 9 for another, and ignoring 0."),

 dict(q="To simulate an event with probability 1/3 using single random digits, the standard fix is to",
   choices=[
     "use digits 0, 1, 2 and accept the small error",
     "assign three digits to success, three to failure, three to a second failure, and IGNORE the tenth digit, re-drawing whenever it appears",
     "use only the digit 3",
     "use two-digit numbers 00 through 33",
     "declare that 1/3 cannot be simulated"],
   ans=1,
   why="Discarding one digit leaves nine equally likely outcomes, three of which are successes, which is exactly 1/3."),

 dict(q="Which of the following is NOT a required part of describing a simulation?",
   choices=[
     "How random digits or numbers are assigned to outcomes",
     "What constitutes one trial",
     "How many trials will be run",
     "How the estimated probability will be calculated from the results",
     "The exact theoretical probability the simulation is expected to produce"],
   ans=4,
   why="A simulation is used precisely when the theoretical value is unknown or hard to compute, so stating it in advance is not part of the description."),

 dict(q="A simulation of 500 trials estimates a probability as 0.164. The best interpretation is that",
   choices=[
     "the true probability is exactly 0.164",
     "in about 16.4% of the simulated trials the outcome occurred, which is an estimate of the true probability",
     "82 trials were run",
     "the simulation should be discarded because 0.164 is not a round number",
     "the true probability is between 0.163 and 0.165"],
   ans=1,
   why="The figure is the observed relative frequency across the trials and stands as an estimate, with no claim of exactness."),

 dict(q="In a simulation of 500 trials that produced an estimated probability of 0.164, how many trials contained the outcome of interest?",
   choices=["16", "41", "82", "164", "336"],
   ans=2,
   why="0.164 times 500 is 82 trials."),

 dict(q="A student simulates whether at least one of three randomly chosen people shares a birth month, using digits 1 through 9 for the first nine months and discarding 0. The main flaw is that",
   choices=[
     "three people is too few to simulate",
     "months 10, 11 and 12 can never appear, so the simulation does not model the real situation",
     "birthdays cannot be simulated",
     "the student should have used 500 trials",
     "digits should never be discarded"],
   ans=1,
   why="A correct simulation must give every possible outcome its right chance, and this scheme makes three of the twelve months impossible."),

 dict(q="Two students run the same correctly designed simulation of 200 trials each and obtain estimated probabilities of 0.41 and 0.45. The best conclusion is that",
   choices=[
     "one of them made a mistake",
     "the true probability is 0.43",
     "both are reasonable estimates of the same true probability, differing because of the randomness inherent in simulation",
     "the simulation design must be wrong",
     "the true probability lies between 0.41 and 0.45 with certainty"],
   ans=2,
   why="Independent runs of a correct simulation give different estimates; the spread between them reflects sampling variability, and averaging them is not guaranteed to give the true value."),

 dict(q="A simulation is used to estimate the probability that a randomly assembled committee of 5 people from a group of 12 contains at least 2 engineers. In this simulation, sampling should be done",
   choices=[
     "with replacement, since random digits repeat",
     "without replacement, because a single person cannot be selected twice for the same committee",
     "either way, since it makes no difference",
     "without any randomization",
     "only if the group size is a multiple of 5"],
   ans=1,
   why="The simulation must mirror the real process, and a committee cannot contain the same person twice, so a repeated label within a trial must be discarded and redrawn."),

 dict(q="Which statement about a simulation's estimated probability is correct?",
   choices=[
     "It is a parameter, since it comes from a random process",
     "It is a statistic, and like any statistic it varies from one run of the simulation to the next",
     "It cannot vary once the design is fixed",
     "It equals the theoretical probability whenever at least 100 trials are used",
     "It has no relationship to the theoretical probability"],
   ans=1,
   why="An estimated probability is computed from the simulated data, so it is a statistic with its own sampling variability, centred on the true probability when the design is correct."),
]
