"""Verification for AP STATISTICS 1.1 Introducing Statistics.

Statistics is not symbolic algebra, so there is no sympy here. Each numeric key
is recomputed from the numbers in its own stem with plain Python and handed to
``Checker.check``, which additionally requires that the computed value matches
the keyed choice and *only* the keyed choice. Topic 1.1 is definitional, so most
items are declared conceptual with the CED essential-knowledge statement that
fixes the key.

Run: python3 verify_s1_1.py
"""
import s_verify_util as U

import s1_1

c = U.Checker(s1_1)

# --- computed keys -----------------------------------------------------------
# q10: 310 of 12,400 households sampled; the key is the sampling fraction as a
# percent, so the computed value is expressed in percent to match the choice text.
c.check(10, 310 / 12400 * 100)

# q11: a sample equal to 4% of an enrollment of 21,000.
c.check(11, 0.04 * 21000)

# q12: 96 surveyed members are 15% of the membership, so N = 96 / 0.15.
c.check(12, 96 / 0.15)

# q21: 234 of 7,800 packages inspected, again as a percent.
c.check(21, 234 / 7800 * 100)

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.1.A.1: a statistical study collects data from a sample to answer an investigative question about a larger population.")
c.conceptual(2, "EK 1.1.A.4: the population is all items or individuals of interest; the sample is only the measured subset.")
c.conceptual(3, "EK 1.1.A.4 and 1.1.A.5: N denotes the population size and n the sample size.")
c.conceptual(4, "EK 1.1.A.2: studies sample because a census is too large, difficult or costly, not because a sample beats a census for accuracy.")
c.conceptual(5, "EK 1.1.A.3: a datum is one piece of information about one individual; a collection of data is a data set.")
c.conceptual(6, "EK 1.1.A.6: reporting in context ties the number to the real-world quantity, its units and the individuals measured.")
c.conceptual(7, "EK 1.1.B.1: an investigative question has a purpose defined in advance and must not be changed on the basis of the results.")
c.conceptual(8, "EK 1.1.B.2: only the option naming a specific population and a measurable quantity can have the required data collected and analyzed.")
c.conceptual(9, "EK 1.1.A.4 and 1.1.A.5: the 18,500 bulbs produced are the population and the 150 tested are the sample.")
c.conceptual(13, "EK 1.1.A.4: the population is every individual the investigative question is about, not only the 45 actually captured.")
c.conceptual(14, "EK 1.1.A.5: the subset of the population that is measured is the sample.")
c.conceptual(15, "EK 1.1.A.5: a sample summary is generally unequal to the population value but is the basis for inference about it.")
c.conceptual(16, "EK 1.1.A.2: sampling exists because a census is impractical, so when complete records exist the population can be examined directly.")
c.conceptual(17, "EK 1.1.A.3: a collection of data about many individuals is a data set.")
c.conceptual(18, "EK 1.1.B.2: a question about moral right and wrong names no measurable quantity, so no data set can settle it.")
c.conceptual(19, "EK 1.1.A.1: the investigative question concerns the population the sample is meant to represent, here all registered voters in the state.")
c.conceptual(20, "EK 1.1.B.2: a usable question must define the population and time frame precisely enough for the data to be collected.")
c.conceptual(22, "EK 1.1.A.4: N is a property of the population, so drawing a larger sample changes n and leaves N alone.")
c.conceptual(23, "EK 1.1.A: an investigative question, a population, a sample and collected data are the components of a statistical study.")
c.conceptual(24, "EK 1.1.A.6: an in-context report names the quantity, its units, and the individuals and period it describes.")
c.conceptual(25, "EK 1.1.A.5: a statistic is evidence about the unknown parameter, not the parameter itself.")

c.finish()
