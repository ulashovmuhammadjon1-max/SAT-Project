# AP STATISTICS 2.1 Tabular and Graphical Representations for the Distributions
# of Two Categorical Variables — 25 questions
# CED: Fall 2026, Unit 2. Learning objectives 2.1.A (compare tabular and
# graphical representations of the relationship between two categorical
# variables) and 2.1.B (justify a claim from them). Essential knowledge 2.1.A.1
# (two-way / contingency tables, holding counts or relative frequencies),
# 2.1.A.2 (side-by-side bar charts, segmented bar charts, mosaic plots) and
# 2.1.A.3 (comparing one variable across the levels of the other to judge
# association).
#
# Table W, n = 500 households:
#                  owns a pet   no pet   total
#     apartment         48        152      200
#     house            162        138      300
#     total            210        290      500
# Chosen so the two conditional distributions are far apart -- 48/200 = 0.24 of
# apartment households own a pet against 162/300 = 0.54 of house households --
# which is what association looks like. Table Y is its counterpart with no
# association, so the two can be contrasted directly:
#                  yes   no   total
#     group 1       30    70    100
#     group 2       60   140    200
#     total         90   210    300
# with 30/100 = 0.30 and 60/200 = 0.30, equal despite very different counts.
#
# Every frequency, proportion and conditional proportion keyed below is
# recomputed from these tables in verify_s2_1.py.
TOPIC = ("2.1", "Tabular and Graphical Representations for the Distributions of Two Categorical Variables", 2)

TABLE_W = dict(
    headers=["Housing type", "Owns a pet", "Does not own a pet", "Total"],
    rows=[["Apartment", "48", "152", "200"],
          ["House", "162", "138", "300"],
          ["Total", "210", "290", "500"]])

TABLE_Y = dict(
    headers=["Group", "Yes", "No", "Total"],
    rows=[["Group 1", "30", "70", "100"],
          ["Group 2", "60", "140", "200"],
          ["Total", "90", "210", "300"]])

QUESTIONS = [
 dict(q="A table used to summarize data for two categorical variables at once, with one variable's categories as rows and the other's as columns, is called",
   choices=[
     "a two-way table, also called a contingency table",
     "a frequency table",
     "a five-number summary",
     "a stem-and-leaf plot",
     "a relative frequency histogram"],
   ans=0,
   why="A two-way, or contingency, table cross-classifies the observational units by both categorical variables."),

 dict(q="The entries in the cells of a two-way table may be",
   choices=[
     "counts only",
     "relative frequencies only",
     "either counts or relative frequencies",
     "means of a quantitative variable",
     "z-scores"],
   ans=2,
   why="A two-way table may be presented with frequencies or with the proportions those frequencies represent."),

 dict(q="Which of the following is NOT a standard graphical display for showing the relationship between two categorical variables?",
   choices=[
     "A side-by-side bar chart",
     "A segmented bar chart",
     "A mosaic plot",
     "A histogram",
     "A bar chart of conditional relative frequencies"],
   ans=3,
   why="A histogram displays the distribution of one quantitative variable; the other four all display two categorical variables together."),

 dict(q="In a segmented bar chart of relative frequencies, each bar represents one category of a variable and is divided so that",
   choices=[
     "each segment's share of the bar is the conditional relative frequency of a category of the other variable",
     "each segment has the same height",
     "the bar's total height equals the sample size",
     "the segments show a quantitative variable's mean",
     "the segments are ordered from largest to smallest count"],
   ans=0,
   why="A segmented bar of relative frequencies is a picture of one conditional distribution, so its segments are conditional relative frequencies summing to 1."),

 dict(q="Five hundred households were classified by housing type and pet ownership, as shown. How many households live in an apartment and own a pet?",
   table=TABLE_W,
   choices=["48", "152", "162", "200", "210"],
   ans=0,
   why="The cell in the apartment row and the pet-owning column holds 48 households."),

 dict(q="For the housing and pet data, how many of the 500 households live in a house?",
   table=TABLE_W,
   choices=["138", "162", "200", "290", "300"],
   ans=4,
   why="The house row totals 162 + 138 = 300 households."),

 dict(q="For the housing and pet data, how many of the 500 households own a pet?",
   table=TABLE_W,
   choices=["48", "162", "200", "210", "290"],
   ans=3,
   why="The pet-owning column totals 48 + 162 = 210 households."),

 dict(q="What proportion of all 500 households live in an apartment AND own a pet?",
   table=TABLE_W,
   choices=["0.096", "0.240", "0.400", "0.420", "0.540"],
   ans=0,
   why="48 of the 500 households fall in that single cell, and 48/500 = 0.096."),

 dict(q="What proportion of all 500 households live in an apartment?",
   table=TABLE_W,
   choices=["0.096", "0.240", "0.400", "0.420", "0.600"],
   ans=2,
   why="The apartment row holds 200 of the 500 households, and 200/500 = 0.40."),

 dict(q="Among the apartment households only, what proportion own a pet?",
   table=TABLE_W,
   choices=["0.096", "0.229", "0.240", "0.420", "0.540"],
   ans=2,
   why="Restricting to the 200 apartment households, 48 own a pet, and 48/200 = 0.24."),

 dict(q="Among the house households only, what proportion own a pet?",
   table=TABLE_W,
   choices=["0.240", "0.324", "0.420", "0.540", "0.771"],
   ans=3,
   why="Restricting to the 300 house households, 162 own a pet, and 162/300 = 0.54."),

 dict(q="Among the pet-owning households only, what proportion live in an apartment?",
   table=TABLE_W,
   choices=["0.096", "0.229", "0.240", "0.400", "0.771"],
   ans=1,
   why="Restricting to the 210 pet-owning households, 48 live in an apartment, and 48/210 = 0.229."),

 dict(q="How many of the 500 households live in a house and do NOT own a pet?",
   table=TABLE_W,
   choices=["48", "138", "152", "162", "290"],
   ans=1,
   why="The cell in the house row and the no-pet column holds 138 households."),

 dict(q="What proportion of all 500 households do NOT own a pet?",
   table=TABLE_W,
   choices=["0.276", "0.304", "0.420", "0.580", "0.760"],
   ans=3,
   why="The no-pet column totals 152 + 138 = 290, and 290/500 = 0.58; equivalently 1 - 0.42."),

 dict(q="Comparing the two housing types in the pet data, the conditional proportions owning a pet are 0.24 for apartments and 0.54 for houses. This comparison suggests that",
   table=TABLE_W,
   choices=[
     "there is an association between housing type and pet ownership, since the proportion owning a pet differs substantially between the two housing types",
     "there is no association, since both proportions are less than 1",
     "housing type causes pet ownership",
     "the two variables are independent, since 500 households were surveyed",
     "no comparison is possible without the marginal totals"],
   ans=0,
   why="Association between two categorical variables shows up as conditional distributions that differ across the levels of the other variable; 0.24 against 0.54 is a large difference."),

 dict(q="A second study produced the two-way table shown. Among Group 1, 30 of 100 answered yes; among Group 2, 60 of 200 answered yes. These data suggest that",
   table=TABLE_Y,
   choices=[
     "there is a strong association, because Group 2 has twice as many yes answers as Group 1",
     "there is no apparent association, because the conditional proportion answering yes is 0.30 in both groups",
     "Group 1 is more likely to answer yes",
     "Group 2 is more likely to answer yes",
     "association cannot be assessed from a two-way table"],
   ans=1,
   why="The raw counts differ only because the groups differ in size; the conditional proportions are identical at 0.30, which is what no association looks like."),

 dict(q="In the second study's table, why is comparing the raw counts 30 and 60 misleading?",
   table=TABLE_Y,
   choices=[
     "Because counts can never be compared",
     "Because Group 2 contains twice as many people as Group 1, so a larger count of yes answers is expected even with identical rates",
     "Because 30 and 60 are both even numbers",
     "Because the totals do not add up correctly",
     "Because the table has too few cells"],
   ans=1,
   why="Group sizes of 100 and 200 make the counts incomparable; only the conditional proportions put the two groups on the same footing."),

 dict(q="If two categorical variables show NO association, then segmented bar charts of the conditional distributions across the levels of one variable will",
   choices=[
     "have segments in the same proportions in every bar",
     "have bars of different total heights",
     "contain no segments at all",
     "always show one bar entirely filled by a single segment",
     "be impossible to draw"],
   ans=0,
   why="No association means the conditional distribution is the same at every level, so every bar is divided in the same proportions."),

 dict(q="A side-by-side bar chart differs from a segmented bar chart in that a side-by-side chart",
   choices=[
     "places the bars for the categories of one variable next to one another rather than stacking them within a single bar",
     "can only display one variable",
     "shows means rather than frequencies",
     "requires the two variables to be quantitative",
     "always uses relative frequencies while segmented charts always use counts"],
   ans=0,
   why="The two displays carry the same information; they differ in whether the categories are placed alongside each other or stacked into one bar."),

 dict(q="In a mosaic plot of two categorical variables, the WIDTH of each column typically represents",
   choices=[
     "the marginal relative frequency of that category of the column variable",
     "the number of categories in the row variable",
     "the conditional relative frequency of the row variable",
     "the sample size",
     "nothing; the widths are always equal"],
   ans=0,
   why="A mosaic plot scales column width by how large that category is overall and column height by the conditional distribution within it, so area represents joint relative frequency."),

 dict(q="A researcher claims from the housing data that 'most pet-owning households live in a house.' Using the table, this claim is",
   table=TABLE_W,
   choices=[
     "correct, because 162 of the 210 pet-owning households, or about 77%, live in a house",
     "correct, because 162 exceeds 152",
     "incorrect, because only 54% of house households own a pet",
     "incorrect, because 210 is less than 290",
     "impossible to evaluate from a two-way table"],
   ans=0,
   why="Restricting to pet owners, 162 of 210 live in a house, which is about 77 percent and so is indeed most of them."),

 dict(q="A student looks at the housing data and concludes that living in a house CAUSES people to own pets. This conclusion is",
   table=TABLE_W,
   choices=[
     "justified, because the difference in conditional proportions is large",
     "justified, because 500 households is a large sample",
     "not justified, because these are observational data with no random assignment, so a variable such as available space could explain the difference",
     "not justified, because the two variables are independent",
     "justified only if the households were randomly selected"],
   ans=2,
   why="A two-way table can establish association but never causation; nothing was assigned, so confounding variables such as living space or household income remain available explanations."),

 dict(q="Which of the following is true of the totals in the margins of a two-way table?",
   choices=[
     "The row totals and the column totals must each add to the same grand total",
     "The row totals must add to more than the column totals",
     "The margins are optional and carry no information",
     "The margins give the conditional distributions",
     "The margins must all be equal to one another"],
   ans=0,
   why="Every observational unit is counted once in exactly one row and one column, so both sets of margins sum to the same overall total."),

 dict(q="For the housing and pet data, adding the four cell counts 48, 152, 162, and 138 gives",
   table=TABLE_W,
   choices=["200", "210", "290", "300", "500"],
   ans=4,
   why="The four cells partition all of the households, so they total the grand total of 500."),

 dict(q="Comparing conditional distributions is the right way to look for association between two categorical variables because",
   choices=[
     "conditional distributions remove the effect of the two groups having different sizes, so the levels can be compared on the same footing",
     "conditional distributions are always easier to compute than counts",
     "conditional distributions prove causation",
     "raw counts cannot be computed from a two-way table",
     "conditional distributions always sum to the grand total"],
   ans=0,
   why="Association is a question about whether the distribution of one variable changes across the levels of the other, and only proportions within each level answer it fairly."),
]
