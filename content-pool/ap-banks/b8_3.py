# AP BIOLOGY 8.3 Population Ecology
# CED effective Fall 2025, Unit 8 Ecology, Big Idea 3 Information Storage and
# Transmission.
# Learning objective 8.3.A, describe factors that influence growth dynamics of
# populations.
# Suggested skill 4.A, CONSTRUCT A GRAPH to represent the data, including the
# type of graph appropriate for the data, axis labeling with appropriate units
# and legend, scaling, accurately plotted data, and a trend line where
# appropriate.
#
# Essential knowledge relied on, in the framework's own terms:
#   8.3.A.1  populations comprise INDIVIDUAL ORGANISMS OF THE SAME SPECIES that
#            interact with one another and with the environment in complex ways.
#   8.3.A.2  many adaptations in organisms are related to OBTAINING AND USING
#            ENERGY AND MATTER in a particular environment.
#              i. population growth dynamics depend on BIRTH RATE, DEATH RATE,
#                 AND POPULATION SIZE.
#                 RELEVANT EQUATION: dN/dt = B minus D, where dt is the change
#                 in time, B the birth rate, D the death rate, N the population
#                 size and dN the change in population size.
#             ii. REPRODUCTION WITHOUT CONSTRAINTS results in the EXPONENTIAL
#                 GROWTH of a population.
#                 RELEVANT EQUATION: dN/dt = rmax times N, where rmax is the
#                 maximum per capita growth rate of the population.
#
# THE ARITHMETIC IS THE GATE. SCIENCE_BRIEF.md names this topic as one of the
# few in Biology where a machine can settle something, so every figure any key
# states -- a rate of change, a per capita rate, a difference between two
# populations, the size of a yearly increase -- is RECOMPUTED in
# verify_b8_3.py, from the table for the data items and by PARSING THE NUMBERS
# OUT OF THE STEM for the rest. Every calculation is one or two steps and
# calculator-free.
#
# NO GRAPH IS EVER REFERRED TO. The suggested skill for this topic is graph
# construction and the bank cannot show a figure, so the items about graphing
# ask what kind of graph the data call for and how its axes must be labelled --
# questions about a graph a student would draw, never about one the stem
# pretends to display. The growth data live in a table.
#
# DELIBERATE OMISSIONS, and this boundary is strict. CARRYING CAPACITY, the
# LOGISTIC MODEL, and DENSITY-DEPENDENT and DENSITY-INDEPENDENT limits are
# EK 8.4.A and are asked in b8_4. The symbol K appears NOWHERE in this module
# and no item here asks what slows or stops growth; the exponential items are
# keyed strictly to EK 8.3.A.2's own phrase, reproduction WITHOUT CONSTRAINTS.
# Changes in energy availability changing population size are EK 8.2.C.1 and
# are asked in b8_2.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset, so the equations are written out in words.
TOPIC = ("8.3", "Population Ecology", 8)

_T_BD = dict(
    headers=["Population", "Births recorded in one year", "Deaths recorded in one year"],
    rows=[["Population A", "120", "45"],
          ["Population B", "60", "60"],
          ["Population C", "30", "78"],
          ["Population D", "210", "150"]])

_T_EXP = dict(
    headers=["Year of the study", "Number of individuals counted"],
    rows=[["Year 1", "50"],
          ["Year 2", "100"],
          ["Year 3", "200"],
          ["Year 4", "400"]])

QUESTIONS = [
 dict(q="According to the course framework, what does a population comprise?",
   choices=[
     "Individual organisms of the same species that interact with one another and with the environment",
     "All the organisms of every species living in one place",
     "The non-living components of one habitat",
     "Every species that shares a common ancestor",
     "One organism observed over its whole lifetime"], ans=0,
   why="EK 8.3.A.1 states that populations comprise individual organisms of the same species that interact with one another and with the environment in complex ways. Organisms of many species in one place are a community, which EK 8.2.B.1 lists as a separate level."),

 dict(q="According to the framework, many adaptations in organisms are related to what?",
   choices=[
     "Obtaining and using energy and matter in a particular environment",
     "Increasing the number of chromosomes an organism carries",
     "Reducing the number of individuals in the population",
     "Preventing any interaction between individuals",
     "Ensuring that birth rate and death rate are always equal"], ans=0,
   why="EK 8.3.A.2 states that many adaptations in organisms are related to obtaining and using energy and matter in a particular environment. That is what connects the adaptations of individuals to the growth dynamics of the population they make up."),

 dict(q="According to the framework, population growth dynamics depend on which quantities?",
   choices=[
     "Birth rate, death rate, and population size",
     "Birth rate alone",
     "Death rate alone",
     "The number of species sharing the habitat",
     "The age of the habitat"], ans=0,
   why="EK 8.3.A.2 states that population growth dynamics depend on birth rate, death rate, and population size. All three appear in the equations the framework prints for this topic."),

 dict(q="In the population growth equation the framework prints, what does the quantity dN/dt represent?",
   choices=[
     "The change in population size per unit of time",
     "The number of individuals in the population",
     "The birth rate alone",
     "The maximum per capita growth rate",
     "The length of time over which the population was studied"], ans=0,
   why="The CED defines dN as the change in population size and dt as the change in time, so dN/dt is the change in population size per unit time. N alone is the population size and rmax the maximum per capita growth rate."),

 dict(q="In the equation stating that dN/dt equals B minus D, what do B and D represent?",
   choices=[
     "The birth rate and the death rate",
     "The population size at the beginning and at the end",
     "The maximum and minimum growth rates",
     "The biomass and the density of the population",
     "The number of births and the number of species"], ans=0,
   why="The CED defines B as the birth rate and D as the death rate in the population growth equation it prints for this topic. Population size is N, and the maximum per capita growth rate is rmax in the other equation."),

 dict(q="Under the framework's equation, what is true of a population whose birth rate exceeds its death rate?",
   choices=[
     "Its change in population size per unit time is positive, so the population is growing",
     "Its change in population size per unit time is negative, so the population is shrinking",
     "Its population size does not change",
     "Its per capita growth rate must be zero",
     "Its birth rate must fall to match its death rate immediately"], ans=0,
   why="The framework prints dN/dt equal to B minus D, so a birth rate larger than the death rate makes that difference positive. A positive change in population size per unit time is growth."),

 dict(q="Under the framework's equation, what is true of a population whose birth rate equals its death rate?",
   choices=[
     "Its change in population size per unit time is zero, so its size is not changing",
     "Its population size is falling",
     "Its population size is rising",
     "It contains no individuals at all",
     "No births or deaths are occurring in it"], ans=0,
   why="The framework prints dN/dt equal to B minus D, and equal rates make that difference zero. A zero change in population size per unit time does not mean that nothing is happening, only that births and deaths offset each other."),

 dict(q="Under the framework's equation, what is true of a population whose death rate exceeds its birth rate?",
   choices=[
     "Its change in population size per unit time is negative, so the population is shrinking",
     "Its change in population size per unit time is positive, so the population is growing",
     "Its population size stays the same",
     "Its birth rate must be zero",
     "Its per capita growth rate must be at its maximum"], ans=0,
   why="The framework prints dN/dt equal to B minus D, so a death rate larger than the birth rate makes that difference negative. A negative change in population size per unit time is a decline."),

 dict(q="According to the framework, what results from reproduction without constraints?",
   choices=["Exponential growth of the population", "A population size that does not change",
            "A steady decline in population size", "A birth rate equal to the death rate",
            "An immediate change in the species present"], ans=0,
   why="EK 8.3.A.2 states that reproduction without constraints results in the exponential growth of a population, and prints the equation dN/dt equal to rmax times N for it."),

 dict(q="In the exponential growth equation the framework prints, what does rmax represent?",
   choices=[
     "The maximum per capita growth rate of the population",
     "The total number of individuals added in one year",
     "The population size at the start of the study",
     "The difference between the birth rate and the death rate in absolute numbers",
     "The length of time the population has existed"], ans=0,
   why="The CED defines rmax as the maximum per capita growth rate of population in the exponential growth equation. Per capita means per individual, which is why it is multiplied by N to give a total rate of change."),

 dict(q="In the exponential growth equation, rmax is held fixed while the population size N increases. What happens to the change in population size per unit time?",
   choices=[
     "It increases, because the same per capita rate is applied to more individuals",
     "It decreases, because each individual contributes less",
     "It stays the same, because rmax is fixed",
     "It becomes negative once the population is large",
     "It cannot be determined without knowing the death rate separately"], ans=0,
   why="The framework prints dN/dt equal to rmax times N, a product. Holding one factor fixed and raising the other raises the product, which is why exponential growth adds more individuals per unit time as the population gets larger."),

 dict(q="What is the difference between a per capita growth rate and the change in population size per unit time?",
   choices=[
     "The per capita rate is measured for each individual, while the change per unit time counts the whole population's increase",
     "They are two names for the same quantity",
     "The per capita rate counts the whole population's increase, while the change per unit time is measured per individual",
     "The per capita rate can only be negative",
     "The change per unit time is measured without reference to time"], ans=0,
   why="The CED defines rmax as a per capita rate and dN as the change in population size, and its equation multiplies the first by N to obtain the second. Two populations can share a per capita rate and differ greatly in how many individuals they add."),

 dict(q="A population records 120 births and 45 deaths in one year, with no individuals entering or leaving. What is the change in population size for that year?",
   choices=["75 individuals", "165 individuals", "45 individuals",
            "120 individuals", "3 individuals"], ans=0,
   why="The framework prints dN/dt equal to B minus D. Subtracting the deaths from the births over the same year gives the change in population size for that year, and adding them instead is what the largest distractor does."),

 dict(q="A population of 400 individuals grows without constraints at a maximum per capita growth rate of 0.05 per year. How many individuals are added in one year?",
   choices=["20 individuals", "80 individuals", "400 individuals",
            "8000 individuals", "5 individuals"], ans=0,
   why="The framework prints dN/dt equal to rmax times N for reproduction without constraints. Multiplying the per capita rate by the population size gives the number added per unit time."),

 dict(q="A population of 200 individuals grows by 30 individuals in one year. What is its per capita growth rate for that year?",
   choices=["0.15 per individual per year", "0.30 per individual per year",
            "0.60 per individual per year", "1.50 per individual per year",
            "0.03 per individual per year"], ans=0,
   why="The framework's exponential equation makes the change in population size per unit time the product of the per capita rate and the population size, so dividing the change by the population size recovers the per capita rate."),

 dict(q="A population of 500 individuals reproduces without constraints at a maximum per capita growth rate of 0.02 per year. How many individuals does it add in one year?",
   choices=["10 individuals", "25 individuals", "500 individuals",
            "20 individuals", "1000 individuals"], ans=0,
   why="The framework prints dN/dt equal to rmax times N. The per capita rate multiplied by the population size gives the number of individuals added over the year."),

 dict(q="The table records the births and deaths in one year for four populations, none of which gained or lost individuals by movement. What was the change in size of Population A over that year?",
   table=_T_BD,
   choices=["An increase of 75 individuals", "An increase of 165 individuals",
            "A decrease of 75 individuals", "An increase of 45 individuals",
            "No change in size"], ans=0,
   why="The framework prints dN/dt equal to B minus D. The named row supplies both counts for the same year, and the difference between them is the change in population size."),

 dict(q="Using the same table of births and deaths, which population did not change in size over the year?",
   table=_T_BD,
   choices=["Population B", "Population A", "Population C", "Population D",
            "All four populations changed in size"], ans=0,
   why="The framework prints dN/dt equal to B minus D, so a population whose two counts are equal has a change of zero. Equal counts do not mean that no births and no deaths occurred, only that they offset."),

 dict(q="Using the same table of births and deaths, which population declined over the year?",
   table=_T_BD,
   choices=["Population C", "Population A", "Population B", "Population D",
            "None of the four populations declined"], ans=0,
   why="The framework prints dN/dt equal to B minus D, so a population whose deaths exceed its births has a negative change in size. Exactly one row of the table records more deaths than births."),

 dict(q="Using the same table of births and deaths, which population grew by the largest number of individuals over the year?",
   table=_T_BD,
   choices=["Population A", "Population B", "Population C", "Population D",
            "Two populations grew by the same largest amount"], ans=0,
   why="The framework prints dN/dt equal to B minus D, so the largest growth belongs to the row with the largest excess of births over deaths. The row with the most births is not automatically that row, which is what the design of the table tests."),

 dict(q="Using the same table of births and deaths, by how many individuals did the growth of Population A exceed the growth of Population D?",
   table=_T_BD,
   choices=["15 individuals", "60 individuals", "90 individuals",
            "75 individuals", "105 individuals"], ans=0,
   why="Skill 5.A includes differences. Each named row yields its own change in size as births minus deaths, and the answer is the difference between those two changes."),

 dict(q="The table gives the number of individuals counted in a population in each of four successive years. What happens to the count from one year to the next?",
   table=_T_EXP,
   choices=["It doubles", "It rises by the same number of individuals each year",
            "It halves", "It stays the same", "It rises and then falls"], ans=0,
   why="Skill 4.B calls for describing the trend. Dividing each year's count by the previous year's gives the same value at every step, which is a constant multiplication rather than a constant addition."),

 dict(q="Using the same four yearly counts, by how many individuals did the population increase between Year 3 and Year 4?",
   table=_T_EXP,
   choices=["200 individuals", "100 individuals", "50 individuals",
            "400 individuals", "800 individuals"], ans=0,
   why="Skill 4.B includes identifying specific data points and skill 5.A the arithmetic. Subtracting the earlier count from the later one gives the increase over that interval."),

 dict(q="In those same four yearly counts, the number of individuals added each year grows even though the population multiplies by the same factor every year. Which statement best explains that?",
   table=_T_EXP,
   choices=[
     "The same per capita rate applied to a larger population adds more individuals",
     "The per capita rate must be rising from year to year",
     "The per capita rate must be falling from year to year",
     "Births are rising while deaths are falling to zero",
     "The counts must have been made with different methods each year"], ans=0,
   why="The framework prints dN/dt equal to rmax times N. A constant multiplying factor means a constant per capita rate, and multiplying that fixed rate by a growing N necessarily yields a growing number added per year."),

 dict(q="Which pattern of growth do those four yearly counts illustrate?",
   table=_T_EXP,
   choices=["Exponential growth", "Growth that has stopped",
            "Growth by a constant number of individuals per year",
            "Decline in population size", "No growth of any kind"], ans=0,
   why="EK 8.3.A.2 states that reproduction without constraints results in the exponential growth of a population, and prints dN/dt equal to rmax times N. A count that multiplies by the same factor each year is that pattern."),

 dict(q="A student must present yearly counts of a population against time. Which kind of graph is most appropriate for these data, and why?",
   choices=[
     "A line graph, because the counts are made at successive times and the trend between them is the point",
     "A pie chart, because the counts sum to a total",
     "A bar graph of a single bar, because only one population was studied",
     "A box and whisker plot, because the counts are numbers",
     "No graph, because population counts cannot be plotted"], ans=0,
   why="Skill 4.A asks for the type of graph appropriate for the data. Counts recorded at successive times are a series in which the change from one time to the next is what the data are about, and a line graph is the form that shows it."),

 dict(q="Under the framework's graphing skill, what must the axes of that population graph carry?",
   choices=[
     "Labels including appropriate units, with a scale chosen so the data fit",
     "Labels only, since units can be inferred by the reader",
     "Units only, since the reader can infer what is plotted",
     "Neither labels nor units, provided the data are plotted accurately",
     "A trend line in place of any labelling"], ans=0,
   why="Skill 4.A lists axis labeling including appropriate units and legend, and scaling, among the components a graph should include. A trend line is listed separately and only where appropriate, so it does not replace labelling."),

 dict(q="The framework's exponential growth equation is introduced with the phrase reproduction WITHOUT CONSTRAINTS. What does that phrase indicate about when the equation applies?",
   choices=[
     "It describes growth during a period in which nothing is restraining reproduction",
     "It describes growth in every population at every time",
     "It describes only populations that are declining",
     "It applies only to populations whose birth rate is zero",
     "It applies only after a population has stopped growing"], ans=0,
   why="EK 8.3.A.2 states that reproduction without constraints results in exponential growth. The qualifying phrase is part of the statement, so the equation is offered for the unconstrained case rather than as a description of every population."),

 dict(q="Two populations have the same maximum per capita growth rate, but one contains far more individuals than the other. Under the framework's equation, what follows?",
   choices=[
     "The larger population adds more individuals per unit time than the smaller one",
     "The two populations add the same number of individuals per unit time",
     "The smaller population adds more individuals per unit time",
     "The larger population must have a lower birth rate",
     "Neither population can grow, because their rates are equal"], ans=0,
   why="The framework prints dN/dt equal to rmax times N. With rmax equal for both, the change in population size per unit time is proportional to N, so the larger population adds more individuals even though each individual contributes the same."),

 dict(q="Taken together, what do the two equations the framework prints for this topic require in order to be used?",
   choices=[
     "The first requires a birth rate and a death rate; the second requires a per capita rate and a population size",
     "Both require only the population size",
     "Both require only the birth rate",
     "The first requires a per capita rate; the second requires a birth rate and a death rate",
     "Neither requires any measured quantity"], ans=0,
   why="The CED prints dN/dt equal to B minus D, defining B as the birth rate and D as the death rate, and dN/dt equal to rmax times N, defining rmax as the maximum per capita growth rate and N as the population size. The fourth option exchanges the two sets of inputs."),
]
