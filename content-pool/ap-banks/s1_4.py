# AP STATISTICS 1.4 Graphical Representations for One Categorical Variable — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.4.A (construct bar charts and pie
# charts), 1.4.B (justify a claim from them) and 1.4.C (compare two or more data
# sets with them).
#
# This bank carries no figures, so every chart is specified numerically: the pie
# chart questions work with central angles (360 times the relative frequency),
# and the bar chart questions work from the counts in a table. That is a fair
# substitute -- the CED's own essential knowledge defines a slice by its area as
# a fraction of the total and a bar by its height, both of which are numbers.
#
# Data sets:
#   D  pets in 500 households: Dog 210, Cat 150, Fish 60, Bird 30, None 50
#   E  music preference in two schools of different size:
#        School P (n = 400):  Pop 156, Rock  80, Hip-hop 120, Classical  44
#        School Q (n = 1000): Pop 350, Rock 250, Hip-hop 300, Classical 100
#      Hip-hop is deliberately the one genre with the same relative frequency in
#      both schools (0.30), and Pop is deliberately the genre with the larger
#      count in Q but the larger share in P -- that pair is the counts-versus-
#      proportions trap this topic exists to test.
# Every angle, proportion, percent and count keyed below is recomputed in
# verify_s1_4.py from these tables.
TOPIC = ("1.4", "Graphical Representations for One Categorical Variable", 1)

TABLE_D = dict(
    headers=["Pet owned", "Number of households"],
    rows=[["Dog", "210"], ["Cat", "150"], ["Fish", "60"], ["Bird", "30"],
          ["None", "50"], ["Total", "500"]])

TABLE_E = dict(
    headers=["Preferred genre", "School P", "School Q"],
    rows=[["Pop", "156", "350"], ["Rock", "80", "250"],
          ["Hip-hop", "120", "300"], ["Classical", "44", "100"],
          ["Total", "400", "1000"]])

QUESTIONS = [
 dict(q="On a bar chart for a single categorical variable, the height or length of each bar corresponds to",
   choices=[
     "the number of categories in the variable",
     "the frequency or relative frequency of the observational units in that category",
     "the total number of observational units in the study",
     "the width of the category",
     "the mean of the observational units in that category"],
   ans=1,
   why="Each bar stands for one category and its height gives that category's count or proportion."),

 dict(q="On a pie chart, the area of each slice as a fraction of the total area corresponds to",
   choices=[
     "the count of observational units in that category",
     "the relative frequency of observational units falling in that category",
     "the number of categories",
     "the square root of the category's count",
     "the difference between that category and the largest category"],
   ans=1,
   why="A slice's share of the pie's area is that category's relative frequency, which is why the slices together make up the whole."),

 dict(q="For a correctly drawn pie chart of one categorical variable, the areas of all the slices together must equal",
   choices=[
     "0.5, or 50% of the total area",
     "1, or 100% of the total area",
     "the sample size n",
     "360, regardless of the data",
     "the number of categories"],
   ans=1,
   why="Every observational unit falls in exactly one category, so the slices exhaust the circle and their areas sum to 1, or 100 percent."),

 dict(q="Which of the following is true of bar charts for a single categorical variable?",
   choices=[
     "They can display frequencies but never relative frequencies",
     "They can display relative frequencies but never frequencies",
     "They can display either frequencies or relative frequencies",
     "They can only be used when there are exactly two categories",
     "They require the categories to be placed in numerical order"],
   ans=2,
   why="A bar chart's vertical scale may be counts or proportions; both are standard."),

 dict(q="Five hundred households reported which pet they own. What is the relative frequency of households owning a dog?",
   table=TABLE_D,
   choices=["0.06", "0.10", "0.12", "0.30", "0.42"],
   ans=4,
   why="210 of the 500 households own a dog, and 210/500 = 0.42."),

 dict(q="If the pet-ownership data are displayed in a pie chart, the central angle of the Dog slice is",
   table=TABLE_D,
   choices=["21.6 degrees", "36.0 degrees", "43.2 degrees", "108.0 degrees", "151.2 degrees"],
   ans=4,
   why="The Dog slice takes 0.42 of the circle, and 0.42 times 360 degrees is 151.2 degrees."),

 dict(q="In that same pie chart of pet ownership, the central angle of the Fish slice is",
   table=TABLE_D,
   choices=["12.0 degrees", "21.6 degrees", "43.2 degrees", "60.0 degrees", "108.0 degrees"],
   ans=2,
   why="Fish accounts for 60/500 = 0.12 of the households, and 0.12 times 360 degrees is 43.2 degrees."),

 dict(q="One slice of the pet-ownership pie chart has a central angle of 36 degrees. That slice represents which category?",
   table=TABLE_D,
   choices=["Dog", "Cat", "Fish", "Bird", "None"],
   ans=4,
   why="A 36-degree slice is 36/360 = 0.10 of the circle, and the category with relative frequency 0.10 is None, with 50 of the 500 households."),

 dict(q="A pie chart slice accounts for 25% of a distribution. Its central angle is",
   choices=["25 degrees", "45 degrees", "72 degrees", "90 degrees", "100 degrees"],
   ans=3,
   why="A quarter of the full 360 degrees is 90 degrees."),

 dict(q="A slice of a pie chart has a central angle of 72 degrees. The relative frequency of that category is",
   choices=["0.10", "0.20", "0.25", "0.36", "0.72"],
   ans=1,
   why="72/360 = 0.20, so one fifth of the observational units fall in that category."),

 dict(q="Among the 500 households surveyed about pets, how many own either a cat or a fish?",
   table=TABLE_D,
   choices=["60", "90", "150", "210", "360"],
   ans=3,
   why="150 households own a cat and 60 own a fish, and 150 + 60 = 210."),

 dict(q="On a bar chart of the pet-ownership counts, which category has the tallest bar?",
   table=TABLE_D,
   choices=["Dog", "Cat", "Fish", "Bird", "None"],
   ans=0,
   why="Dog has the largest count, 210, so its bar is the tallest."),

 dict(q="A frequency bar chart and a relative frequency bar chart are both drawn for the same pet-ownership data. Compared with each other, the two charts will",
   table=TABLE_D,
   choices=[
     "have completely different shapes, because proportions and counts are unrelated",
     "have the same shape, because every count is divided by the same total, so the bars keep the same relative heights",
     "have the same shape only if every category has the same count",
     "differ in which category is tallest",
     "be identical, including the numbers on the vertical scale"],
   ans=1,
   why="Dividing every count by the same total 500 rescales all the bars by one factor, so the picture is unchanged apart from the vertical scale."),

 dict(q="What percent of the 500 surveyed households own no pet at all?",
   table=TABLE_D,
   choices=["5%", "6%", "10%", "12%", "50%"],
   ans=2,
   why="50 of the 500 households reported no pet, and 50/500 = 0.10, which is 10 percent."),

 dict(q="Students at two schools of different sizes reported a preferred music genre. Which genre has the same relative frequency at School P as at School Q?",
   table=TABLE_E,
   choices=["Pop", "Rock", "Hip-hop", "Classical", "No genre has the same relative frequency at both schools"],
   ans=2,
   why="Hip-hop is 120/400 = 0.30 at School P and 300/1000 = 0.30 at School Q; every other genre differs."),

 dict(q="For the music-preference data, Rock is preferred by a larger share of students at",
   table=TABLE_E,
   choices=[
     "School P, because 80 is smaller than 250",
     "School P, because 0.20 exceeds 0.25",
     "School Q, because 0.25 exceeds 0.20",
     "School Q, because 250 is more than three times 80",
     "neither school, because the two shares are equal"],
   ans=2,
   why="Rock's share is 80/400 = 0.20 at School P and 250/1000 = 0.25 at School Q, so it is proportionally more popular at School Q."),

 dict(q="Which statement about Pop in the music-preference data is correct?",
   table=TABLE_E,
   choices=[
     "School Q has both the larger number and the larger share of Pop listeners",
     "School P has both the larger number and the larger share of Pop listeners",
     "School Q has the larger number of Pop listeners, but School P has the larger share",
     "School P has the larger number of Pop listeners, but School Q has the larger share",
     "The two schools have the same number and the same share of Pop listeners"],
   ans=2,
   why="School Q has 350 Pop listeners against School P's 156, but Q's share is 0.35 against P's 0.39, so the larger count belongs to the school with the smaller share."),

 dict(q="To compare the music preferences of School P and School Q fairly using bar charts, it is best to draw",
   table=TABLE_E,
   choices=[
     "frequency bar charts, because counts are exact",
     "relative frequency bar charts, because the two schools have very different enrollments",
     "a single bar chart of the combined totals",
     "pie charts of the counts rather than the proportions",
     "bar charts with the categories in alphabetical order"],
   ans=1,
   why="Because School Q is two and a half times the size of School P, only proportions put the two distributions on a comparable scale."),

 dict(q="A pie chart is a reasonable display choice when the goal is to",
   choices=[
     "show how a single categorical variable's observational units divide up a whole among a small number of categories",
     "display the relationship between two quantitative variables",
     "show the shape of a continuous distribution",
     "compare the medians of several groups",
     "display data for a variable with several dozen categories"],
   ans=0,
   why="A pie chart shows parts of a single whole and becomes unreadable once there are many categories or the variable is quantitative."),

 dict(q="A bar chart for a categorical variable is conventionally drawn with gaps between the bars because",
   choices=[
     "the gaps represent observational units that were not classified",
     "the categories are distinct labels rather than adjoining intervals of a number line",
     "the gaps are required to make the bar heights readable",
     "the widths of the bars carry meaning",
     "the categories must be shown in increasing numerical order"],
   ans=1,
   why="Categories are separate labels with nothing between them, unlike the touching intervals of a histogram for a quantitative variable."),

 dict(q="A pie chart is presented with slices labeled 30%, 25%, 25%, and 25%. The chart cannot be correct because",
   choices=[
     "a pie chart may have at most three slices",
     "the labeled percentages total 105%, but the slices of a pie chart must total 100%",
     "no slice may exceed 25%",
     "the percentages should be reported as counts",
     "three slices are not allowed to be equal"],
   ans=1,
   why="30 + 25 + 25 + 25 = 105, and the slices of a pie chart must account for exactly 100 percent of the data."),

 dict(q="A club president claims, 'Dogs are owned by more households than cats and fish put together.' Using the pet-ownership data, this claim is",
   table=TABLE_D,
   choices=[
     "correct, because 210 exceeds 150 + 60",
     "correct, because dogs have the tallest bar",
     "incorrect, because 210 equals 150 + 60",
     "incorrect, because 210 is less than 150 + 60",
     "impossible to evaluate without the relative frequencies"],
   ans=2,
   why="Cats and fish together account for 150 + 60 = 210 households, exactly equal to the 210 dog-owning households, so 'more than' is false."),

 dict(q="In a pie chart of School Q's music preferences alone, the central angle of the Rock slice is",
   table=TABLE_E,
   choices=["25 degrees", "72 degrees", "90 degrees", "108 degrees", "250 degrees"],
   ans=2,
   why="Rock is 250/1000 = 0.25 of School Q's students, and 0.25 times 360 degrees is 90 degrees."),

 dict(q="Two students draw bar charts of the same categorical data but arrange the categories along the horizontal axis in different orders. It follows that",
   choices=[
     "one of the two charts must be wrong, since only one order is valid",
     "both charts can be correct, because the categories of a categorical variable have no inherent numerical order",
     "the two charts will show different relative frequencies",
     "the taller bars will change height when the order changes",
     "the categories must always be arranged from largest count to smallest"],
   ans=1,
   why="A categorical variable's categories are labels with no built-in order, so rearranging them changes the picture's arrangement but none of its heights."),

 dict(q="A relative frequency bar chart for a categorical variable is drawn, and one bar reaches 0.35 while another reaches 0.15. This tells you that",
   choices=[
     "the first category contains exactly 35 observational units",
     "the first category's share of the data is 0.20 larger than the second category's share",
     "the first category contains 35% more observational units than the second",
     "the sample size must be 100",
     "the two categories together account for all the data"],
   ans=1,
   why="The bars give shares, so the difference 0.35 - 0.15 = 0.20 is a difference in proportions, and no count can be read off without the total."),
]
