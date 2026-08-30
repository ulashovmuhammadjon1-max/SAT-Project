# AP STATISTICS 1.3 Tabular Representation and Summary Statistics for One
# Categorical Variable — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.3.A (construct categorical
# one-variable tabular representations) and 1.3.B (describe them with summary
# statistics).
#
# Three data sets carry the computational items and are reused across questions:
#   A  favorite sport, n = 200: Soccer 64, Basketball 52, Tennis 36, Swimming 48
#   B  blood type,     n = 250: O 110, A 88, B 37, AB 15
#   C  commute mode,   n = 400: Car 220, Bus 96, Bicycle 44, Walk 40
# Every count in every table sums to the stated total, and every relative
# frequency, percent, ratio and count keyed below is recomputed from these tables
# in verify_s1_3.py. The remaining items are definitional and are documented
# there as conceptual.
TOPIC = ("1.3", "Tabular Representation and Summary Statistics for One Categorical Variable", 1)

TABLE_A = dict(
    headers=["Favorite sport", "Number of students"],
    rows=[["Soccer", "64"], ["Basketball", "52"], ["Tennis", "36"],
          ["Swimming", "48"], ["Total", "200"]])

TABLE_B = dict(
    headers=["Blood type", "Number of donors"],
    rows=[["O", "110"], ["A", "88"], ["B", "37"], ["AB", "15"],
          ["Total", "250"]])

TABLE_C = dict(
    headers=["Commute mode", "Number of employees"],
    rows=[["Car", "220"], ["Bus", "96"], ["Bicycle", "44"], ["Walk", "40"],
          ["Total", "400"]])

QUESTIONS = [
 dict(q="A table that shows the number of observational units falling in each category of a categorical variable is called a",
   choices=[
     "frequency table",
     "relative frequency table",
     "quantitative summary table",
     "residual table",
     "sampling frame"],
   ans=0,
   why="A frequency table records counts; a relative frequency table records the proportions those counts represent."),

 dict(q="A table that shows the proportion of observational units in each category of a categorical variable is called a",
   choices=[
     "frequency table",
     "relative frequency table",
     "census",
     "parameter table",
     "list of observational units"],
   ans=1,
   why="Relative frequency is the proportion in each category, so a table of those proportions is a relative frequency table."),

 dict(q="If a relative frequency table is constructed correctly for a single categorical variable with no missing data, the sum of all its relative frequencies must equal",
   choices=["0", "0.5", "1", "100", "the sample size n"],
   ans=2,
   why="Every observational unit falls in exactly one category, so the proportions account for the whole sample and add to 1."),

 dict(q="Two hundred students each named a favorite sport, with results shown. What is the relative frequency of Soccer?",
   table=TABLE_A,
   choices=["0.18", "0.24", "0.26", "0.32", "0.64"],
   ans=3,
   why="Soccer's relative frequency is 64/200 = 0.32; 0.64 comes from mistakenly dividing by 100."),

 dict(q="For the favorite-sport data, what percent of the students chose Tennis?",
   table=TABLE_A,
   choices=["3.6%", "18%", "24%", "26%", "36%"],
   ans=1,
   why="36 of the 200 students chose Tennis, and 36/200 = 0.18, which is 18 percent."),

 dict(q="Among the 200 students surveyed about favorite sport, how many more chose Soccer than chose Tennis?",
   table=TABLE_A,
   choices=["12", "16", "28", "36", "100"],
   ans=2,
   why="64 chose Soccer and 36 chose Tennis, and 64 - 36 = 28."),

 dict(q="What proportion of the 200 students chose either Soccer or Basketball as their favorite sport?",
   table=TABLE_A,
   choices=["0.26", "0.32", "0.42", "0.58", "0.84"],
   ans=3,
   why="Soccer and Basketball together account for 64 + 52 = 116 students, and 116/200 = 0.58."),

 dict(q="For the favorite-sport data, the ratio of the number of students choosing Basketball to the number choosing Swimming is",
   choices=["3 to 4", "12 to 13", "13 to 12", "4 to 3", "13 to 25"],
   table=TABLE_A,
   ans=2,
   why="The ratio is 52 to 48, and dividing both by 4 gives 13 to 12."),

 dict(q="How many of the 200 surveyed students did NOT choose Soccer as their favorite sport?",
   table=TABLE_A,
   choices=["64", "84", "116", "136", "164"],
   ans=3,
   why="200 - 64 = 136 students chose something other than Soccer."),

 dict(q="A student claims that 'fewer than one in five of these students chose Swimming.' Using the favorite-sport table, this claim is",
   table=TABLE_A,
   choices=[
     "correct, because 48/200 = 0.24, which is less than 0.20",
     "correct, because 48 is fewer than 200/5",
     "incorrect, because 48/200 = 0.24, which is greater than 0.20",
     "incorrect, because 48 students is more than half the sample",
     "impossible to evaluate without knowing the population size"],
   ans=2,
   why="One in five is 0.20 and the relative frequency for Swimming is 48/200 = 0.24, so more than one in five chose it."),

 dict(q="A blood bank recorded the blood type of 250 donors. What is the relative frequency of type A?",
   table=TABLE_B,
   choices=["0.060", "0.148", "0.352", "0.440", "0.880"],
   ans=2,
   why="88 of the 250 donors were type A, and 88/250 = 0.352."),

 dict(q="For the blood-donor data, what percent of donors had type AB blood?",
   table=TABLE_B,
   choices=["1.5%", "6%", "14.8%", "15%", "60%"],
   ans=1,
   why="15 of the 250 donors were type AB, and 15/250 = 0.06, which is 6 percent."),

 dict(q="What proportion of the 250 donors had either type O or type A blood?",
   table=TABLE_B,
   choices=["0.352", "0.440", "0.588", "0.792", "0.940"],
   ans=3,
   why="Types O and A account for 110 + 88 = 198 donors, and 198/250 = 0.792."),

 dict(q="How many of the 250 donors did NOT have type O blood?",
   table=TABLE_B,
   choices=["37", "110", "125", "140", "213"],
   ans=3,
   why="250 - 110 = 140 donors had a type other than O."),

 dict(q="For the blood-donor data, the number of type O donors is how many times the number of type AB donors?",
   table=TABLE_B,
   choices=["1.5", "3.0", "7.3", "22.0", "95.0"],
   ans=2,
   why="110 divided by 15 is about 7.3, so there were roughly 7.3 times as many type O donors as type AB donors."),

 dict(q="Suppose only the relative frequency table for the 250 blood donors is available, with type B at 0.148. To recover the number of type B donors you should",
   table=TABLE_B,
   choices=[
     "add 0.148 to 250",
     "multiply 0.148 by 250, giving 37 donors",
     "divide 250 by 0.148",
     "subtract 0.148 from 1 and multiply by 250",
     "conclude that the count cannot be recovered from a relative frequency"],
   ans=1,
   why="A relative frequency times the total gives the count back, and 0.148 times 250 is 37."),

 dict(q="Four hundred employees reported how they commute to work. What percent commute by car?",
   table=TABLE_C,
   choices=["11%", "24%", "45%", "55%", "220%"],
   ans=3,
   why="220 of the 400 employees drive, and 220/400 = 0.55, which is 55 percent."),

 dict(q="What proportion of the 400 employees commute either by bicycle or on foot?",
   table=TABLE_C,
   choices=["0.10", "0.11", "0.21", "0.35", "0.45"],
   ans=2,
   why="Bicycle and walking account for 44 + 40 = 84 employees, and 84/400 = 0.21."),

 dict(q="What is the relative frequency of employees who commute by some means other than a car?",
   table=TABLE_C,
   choices=["0.21", "0.24", "0.45", "0.55", "0.79"],
   ans=2,
   why="180 of the 400 employees do not drive, and 180/400 = 0.45; equivalently 1 - 0.55."),

 dict(q="A manager claims that 'more than a quarter of our employees take the bus.' Using the commute-mode table, this claim is",
   table=TABLE_C,
   choices=[
     "correct, because 96 is more than 25",
     "correct, because 96/400 = 0.24, which exceeds 0.25",
     "incorrect, because 96/400 = 0.24, which is less than 0.25",
     "incorrect, because the bus category has the smallest count",
     "impossible to evaluate from a frequency table"],
   ans=2,
   why="A quarter of 400 is 100, and only 96 employees take the bus, so the relative frequency 0.24 falls just short of 0.25."),

 dict(q="Using the commute-mode data, the number of employees who drive exceeds the number who take the bus by what percent of the 400 employees?",
   table=TABLE_C,
   choices=["24%", "31%", "44%", "55%", "124%"],
   ans=1,
   why="220 - 96 = 124 employees, and 124/400 = 0.31, which is 31 percent of the workforce."),

 dict(q="Which of the following statements about percentages, relative frequencies, proportions, and ratios for a categorical variable is correct?",
   choices=[
     "They convey different information and cannot be converted into one another",
     "They all convey the same information about the distribution, expressed in different forms",
     "Only counts can be used to justify a claim about a categorical variable",
     "A percentage can be computed but a proportion cannot when the total is unknown",
     "A ratio is the only one of these that requires the sample size"],
   ans=1,
   why="Proportions, percentages, relative frequencies and ratios are alternative expressions of the same distributional information."),

 dict(q="A frequency table for a categorical variable reports counts of 45, 30, and 25 for its three categories. Without any further information, the relative frequency of the first category is",
   choices=["0.25", "0.30", "0.45", "0.55", "1.80"],
   ans=2,
   why="The three counts total 100, so the first category's relative frequency is 45/100 = 0.45."),

 dict(q="Two schools each report the distribution of students' preferred lunch option. School X has 300 students and School Y has 1,200. To compare the two distributions fairly, it is best to compare",
   choices=[
     "the raw counts, because counts are exact",
     "the relative frequencies, because they adjust for the very different totals",
     "the totals only",
     "the number of categories in each table",
     "the largest count in each school"],
   ans=1,
   why="Counts cannot be compared across groups of different sizes, but relative frequencies express each category as a share of its own total."),

 dict(q="Which of the following can be determined from a relative frequency table alone, with the total number of observational units NOT given?",
   choices=[
     "The exact count in each category",
     "The number of observational units that fall in the two largest categories combined",
     "The proportion of observational units in the largest category",
     "The number of categories that contain more than 50 observational units",
     "The sample size n"],
   ans=2,
   why="Relative frequencies give shares directly, but recovering any count requires the total, which is not provided."),
]
