"""Verification for AP STATISTICS 1.2 Variables.

Topic 1.2 is a classification topic: observational units, variables, parameters
and statistics, then categorical against quantitative and discrete against
continuous. Almost nothing here is computable, so almost every item is declared
conceptual with the CED essential-knowledge statement that fixes its key.

The one item that carries numbers (q15) is the parameter-versus-statistic
discrimination, and it is checked numerically: the stem says 0.29 is the value
for all 40,000 adults and 0.34 came from the 500 sampled, so the key must be the
choice reading 0.29. ``Checker.check`` also confirms no other choice carries that
same number, which is the guard against an unanswerable question.

Run: python3 verify_s1_2.py
"""
import s_verify_util as U

import s1_2

c = U.Checker(s1_2)

# --- computed key ------------------------------------------------------------
# q15: the parameter is the population value. The stem states that 0.29 of all
# 40,000 adults own a bicycle, so the parameter is 0.29 and 0.34 (from the
# sample of 500) is the statistic. Recomputed here as the population figure.
POP_TOTAL, POP_OWNERS = 40000, 0.29 * 40000
c.check(15, POP_OWNERS / POP_TOTAL)

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.2.A.1: an observational unit is the item or individual a datum is collected from.")
c.conceptual(2, "EK 1.2.A.2: a variable is a characteristic that may change from one observational unit to another.")
c.conceptual(3, "EK 1.2.A.4: a parameter is a numerical attribute or summary of the variable of interest for a population.")
c.conceptual(4, "EK 1.2.A.5: a statistic is a numerical attribute or summary of the variable of interest for a sample.")
c.conceptual(5, "EK 1.2.B.1: a categorical (qualitative) variable takes values that are category names or group labels.")
c.conceptual(6, "EK 1.2.B.2: a quantitative (numerical) variable takes numerical values for a measured or counted quantity and generally has units.")
c.conceptual(7, "EK 1.2.C.1: a discrete quantitative variable takes a countable number of values, finite or countably infinite.")
c.conceptual(8, "EK 1.2.C.2: a continuous quantitative variable takes infinitely many values within an interval, including every value between any two of them.")
c.conceptual(9, "EK 1.2.A.1: data are collected from each dog, so the individual dogs are the observational units.")
c.conceptual(10, "EK 1.2.B and 1.2.C: breed is a group label, weight is measured so continuous, and a count of vaccinations is a whole number so discrete.")
c.conceptual(11, "EK 1.2.B.1: a ZIP code is written with digits but labels an area rather than measuring an amount, so it is categorical and averaging it is meaningless.")
c.conceptual(12, "EK 1.2.C.2: elapsed time takes every value in an interval, so it is continuous; the alternatives are counts, labels or yes/no answers.")
c.conceptual(13, "EK 1.2.C.1: a count of seeds is a whole number so discrete, while heights and masses are measured and continuous.")
c.conceptual(14, "EK 1.2.A.4: the 46% comes from complete records of every student in the population of interest, so it is a parameter.")
c.conceptual(16, "EK 1.2.A.5: a value computed from the sample of 500 is a statistic whether or not it happens to be close to the parameter.")
c.conceptual(17, "EK 1.2.A.4 and 1.2.A.5: Greek letters such as mu denote population parameters, while x-bar, s and p-hat are computed from samples.")
c.conceptual(18, "EK 1.2.A.5: the hat notation marks a sample proportion, a statistic estimating the population proportion p.")
c.conceptual(19, "EK 1.2.A.2: the variable is the characteristic that changes from bearing to bearing, namely the diameter; the mean of the sample is a statistic.")
c.conceptual(20, "EK 1.2.A.5: the mean of the 60 measured bearings is a numerical summary of the sample, hence a statistic.")
c.conceptual(21, "EK 1.2.B.1: numbering ordered labels does not make them measured amounts, so the ratings remain a categorical variable.")
c.conceptual(22, "EK 1.2.B.1 and 1.2.B.2: a jersey number identifies a player rather than measuring anything, while points scored is a genuine count.")
c.conceptual(23, "EK 1.2.A.1: data are collected from each tree, so an individual oak is the observational unit; the 80 measured trees are the sample.")
c.conceptual(24, "EK 1.2.A.4 and 1.2.A.5: the population value is a single fixed number, while the sample value changes with the sample drawn.")
c.conceptual(25, "EK 1.2.B.1 and 1.2.B.2: blood type is a group label and resting heart rate is a counted quantity with units.")

c.finish()
