# AP STATISTICS 2.2 Summary Statistics for Two Categorical Variables — 25 questions
# CED: Fall 2026, Unit 2. Learning objectives 2.2.A (calculate summary statistics
# from two-way tables), 2.2.B (compare them for evidence of association) and
# 2.2.C (justify a claim from them). Essential knowledge 2.2.A.1 (joint relative
# frequency: a cell divided by the grand total), 2.2.A.2 (marginal: a row or
# column total divided by the grand total) and 2.2.A.3 (conditional: computed
# after restricting to one row or one column).
#
# The three are distinguished ONLY by what sits in the denominator, and that is
# the whole difficulty of the topic. Every computational item here names its
# denominator implicitly through its wording, and the module deliberately asks
# for the same cell three different ways -- as a joint, as a conditional on its
# row, and as a conditional on its column -- so the three answers differ and a
# student who reaches for the grand total every time is caught.
#
# Table X, n = 300 students:
#                    passed   failed   total
#     flashcards       144       36      180
#     rereading         66       54      120
#     total            210       90      300
#   joint:       144/300 = 0.48, 36/300 = 0.12, 66/300 = 0.22, 54/300 = 0.18
#   marginal:    flashcards 0.60, rereading 0.40, passed 0.70, failed 0.30
#   conditional: pass given flashcards 144/180 = 0.80
#                pass given rereading   66/120 = 0.55
#                flashcards given pass 144/210 = 0.686
#                flashcards given fail   36/90 = 0.40
# Every one of these is recomputed in verify_s2_2.py.
TOPIC = ("2.2", "Summary Statistics for Two Categorical Variables", 2)

TABLE_X = dict(
    headers=["Study method", "Passed", "Failed", "Total"],
    rows=[["Flashcards", "144", "36", "180"],
          ["Rereading", "66", "54", "120"],
          ["Total", "210", "90", "300"]])

QUESTIONS = [
 dict(q="A joint relative frequency in a two-way table is",
   choices=[
     "a cell frequency divided by the total for the entire table",
     "a row total divided by the total for the entire table",
     "a cell frequency divided by its own row total",
     "a cell frequency divided by its own column total",
     "the sum of two cell frequencies"],
   ans=0,
   why="A joint relative frequency answers 'what share of everybody falls in this cell', so the denominator is the grand total."),

 dict(q="A marginal relative frequency in a two-way table is",
   choices=[
     "a cell frequency divided by the total for the entire table",
     "a row total or a column total divided by the total for the entire table",
     "a cell frequency divided by its own row total",
     "the difference between two conditional relative frequencies",
     "the largest cell in the table divided by the smallest"],
   ans=1,
   why="A marginal relative frequency describes one variable on its own, using a margin total over the grand total."),

 dict(q="A conditional relative frequency in a two-way table is computed by",
   choices=[
     "dividing a cell frequency by the total for the entire table",
     "dividing a row total by the grand total",
     "restricting to one row or one column and dividing a cell frequency by that row's or column's total",
     "adding all the cells in a row",
     "subtracting a marginal relative frequency from 1"],
   ans=2,
   why="Conditioning means throwing away everything outside the chosen level, so the denominator becomes that level's total."),

 dict(q="In a two-way table with no missing data, the sum of all the joint relative frequencies is",
   choices=["0", "0.5", "1", "the number of cells", "the grand total"],
   ans=2,
   why="Every observational unit falls in exactly one cell, so the cells' shares of the whole account for all of it."),

 dict(q="For a fixed row of a two-way table, the conditional relative frequencies across that row sum to",
   choices=["0", "0.5", "1", "the row total", "the grand total"],
   ans=2,
   why="Once attention is restricted to one row, that row is the whole of what is being described, so its conditional relative frequencies account for all of it."),

 dict(q="Three hundred students were classified by study method and exam result, as shown. What is the joint relative frequency of using flashcards and passing?",
   table=TABLE_X,
   choices=["0.120", "0.220", "0.480", "0.686", "0.800"],
   ans=2,
   why="The cell holds 144 students out of the 300 in the whole table, and 144/300 = 0.48."),

 dict(q="For the study method data, what is the joint relative frequency of rereading and failing?",
   table=TABLE_X,
   choices=["0.120", "0.180", "0.220", "0.450", "0.600"],
   ans=1,
   why="The cell holds 54 students out of 300, and 54/300 = 0.18."),

 dict(q="For the study method data, what is the marginal relative frequency of using flashcards?",
   table=TABLE_X,
   choices=["0.400", "0.480", "0.600", "0.700", "0.800"],
   ans=2,
   why="The flashcards row totals 180 students out of 300, and 180/300 = 0.60."),

 dict(q="For the study method data, what is the marginal relative frequency of passing?",
   table=TABLE_X,
   choices=["0.300", "0.480", "0.600", "0.700", "0.800"],
   ans=3,
   why="The passed column totals 210 students out of 300, and 210/300 = 0.70."),

 dict(q="Among the students who used flashcards, what proportion passed?",
   table=TABLE_X,
   choices=["0.480", "0.550", "0.686", "0.700", "0.800"],
   ans=4,
   why="Restricting to the 180 flashcard users, 144 passed, and 144/180 = 0.80."),

 dict(q="Among the students who reread their notes, what proportion passed?",
   table=TABLE_X,
   choices=["0.220", "0.314", "0.400", "0.550", "0.700"],
   ans=3,
   why="Restricting to the 120 who reread, 66 passed, and 66/120 = 0.55."),

 dict(q="Among the students who passed, what proportion used flashcards?",
   table=TABLE_X,
   choices=["0.400", "0.480", "0.600", "0.686", "0.800"],
   ans=3,
   why="Restricting to the 210 who passed, 144 used flashcards, and 144/210 = 0.686."),

 dict(q="Among the students who failed, what proportion used flashcards?",
   table=TABLE_X,
   choices=["0.120", "0.180", "0.400", "0.600", "0.686"],
   ans=2,
   why="Restricting to the 90 who failed, 36 used flashcards, and 36/90 = 0.40."),

 dict(q="Among the students who used flashcards, what proportion failed?",
   table=TABLE_X,
   choices=["0.120", "0.200", "0.300", "0.400", "0.550"],
   ans=1,
   why="Restricting to the 180 flashcard users, 36 failed, and 36/180 = 0.20, which is also 1 - 0.80."),

 dict(q="The value 144/300 = 0.48, the value 144/180 = 0.80, and the value 144/210 = 0.686 all come from the same cell of the table. They differ because",
   table=TABLE_X,
   choices=[
     "one of the three calculations must be wrong",
     "they use different denominators: the whole table, the flashcards row, and the passed column respectively",
     "the cell frequency changes depending on the question",
     "relative frequencies are only approximate",
     "the table contains an error"],
   ans=1,
   why="Joint, row-conditional and column-conditional relative frequencies all take the same numerator and differ only in what population they are a share of."),

 dict(q="For the study method data, the four joint relative frequencies are 0.48, 0.12, 0.22, and 0.18. Their sum is",
   table=TABLE_X,
   choices=["0.60", "0.70", "0.90", "1.00", "3.00"],
   ans=3,
   why="The four cells partition all 300 students, so their shares of the whole must total 1."),

 dict(q="For the study method data, what is the marginal relative frequency of failing?",
   table=TABLE_X,
   choices=["0.180", "0.200", "0.300", "0.400", "0.700"],
   ans=2,
   why="The failed column totals 90 students out of 300, and 90/300 = 0.30; equivalently 1 - 0.70."),

 dict(q="Comparing the conditional proportions who passed, 0.80 for flashcard users against 0.55 for rereaders, the appropriate statistical conclusion is that",
   table=TABLE_X,
   choices=[
     "study method and exam result appear to be associated in these data",
     "study method and exam result appear to be independent in these data",
     "using flashcards causes students to pass",
     "no conclusion can be drawn from conditional proportions",
     "the two variables must be quantitative"],
   ans=0,
   why="The conditional distribution of the result changes across the levels of study method, which is evidence of association; causation would require random assignment."),

 dict(q="If study method and exam result were completely unassociated in these data, then the conditional proportion passing among flashcard users would equal",
   table=TABLE_X,
   choices=[
     "0.48, the joint relative frequency of flashcards and passing",
     "0.60, the marginal relative frequency of using flashcards",
     "0.70, the marginal relative frequency of passing",
     "0.80, the value actually observed",
     "1.00"],
   ans=2,
   why="Under no association the conditional distribution of the result is the same in every study-method group and therefore equals the overall marginal distribution of the result."),

 dict(q="Under no association, the expected count in the flashcards-and-passed cell would be the flashcards total times the marginal proportion passing. That expected count is",
   table=TABLE_X,
   choices=["108", "126", "144", "150", "180"],
   ans=1,
   why="180 flashcard users times the overall passing proportion 0.70 gives 126, noticeably fewer than the 144 actually observed."),

 dict(q="Comparing the observed count of 144 in the flashcards-and-passed cell with the 126 expected under no association shows that",
   table=TABLE_X,
   choices=[
     "more flashcard users passed than would be expected if the two variables were unassociated",
     "fewer flashcard users passed than would be expected if the two variables were unassociated",
     "exactly as many passed as expected",
     "the table must contain an arithmetic error",
     "the two variables are independent"],
   ans=0,
   why="144 exceeds 126, so this cell is over-represented relative to what no association would produce, which is the same association the conditional proportions showed."),

 dict(q="A student computes 144/300 = 0.48 and reports it as 'the proportion of flashcard users who passed'. The error is that",
   table=TABLE_X,
   choices=[
     "0.48 is the joint relative frequency for the whole table, whereas the proportion of flashcard users who passed requires dividing by the 180 flashcard users",
     "0.48 should have been rounded to 0.5",
     "the numerator should have been 180",
     "joint relative frequencies cannot be computed from this table",
     "there is no error"],
   ans=0,
   why="The phrase 'of flashcard users' names the group being conditioned on, which fixes the denominator at 180 rather than 300."),

 dict(q="For the study method data, the conditional proportion passing among flashcard users is 0.80 and among rereaders is 0.55. Adding these gives 1.35, which exceeds 1. This is",
   table=TABLE_X,
   choices=[
     "an error, since relative frequencies can never sum above 1",
     "expected, because these two proportions come from different conditional distributions and are not parts of one whole",
     "evidence that the table is inconsistent",
     "evidence of a very strong association",
     "impossible"],
   ans=1,
   why="Conditional relative frequencies sum to 1 within a single level, not across levels; 0.80 and 0.20 sum to 1, and so do 0.55 and 0.45."),

 dict(q="Which pair of numbers from the study method table sums to exactly 1?",
   table=TABLE_X,
   choices=[
     "the proportion who used flashcards and the proportion who passed",
     "the proportion who passed among flashcard users and the proportion who failed among flashcard users",
     "the proportion who passed among flashcard users and the proportion who passed among rereaders",
     "the joint relative frequency of flashcards-and-passed and the marginal relative frequency of passing",
     "the proportion who used flashcards among those who passed and the proportion who passed among flashcard users"],
   ans=1,
   why="Passing and failing exhaust the possibilities within the flashcards group, so 0.80 and 0.20 sum to 1; the other pairs mix different denominators."),

 dict(q="A tutor claims from these data that 'flashcards work better than rereading for this exam'. The most defensible version of this claim is that",
   table=TABLE_X,
   choices=[
     "among the students in this study, a higher proportion of flashcard users passed than of rereaders, but because students were not randomly assigned to a method, the difference may be due to other differences between the groups",
     "flashcards cause a higher pass rate for all students",
     "the two methods are equally effective",
     "no comparison between the two methods is possible",
     "the claim is proved because 144 is larger than 66"],
   ans=0,
   why="The data support an association among these students; without random assignment, stronger students may simply have been more likely to choose flashcards."),
]
