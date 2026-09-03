# AP BIOLOGY 8.4 Effect of Density on Populations
# CED effective Fall 2025, Unit 8 Ecology, Big Idea 4 Systems Interactions.
# Learning objective 8.4.A, explain how the density of a population affects and
# is determined by resource availability in the environment.
# Suggested skill 5.A, PERFORM MATHEMATICAL CALCULATIONS, including
# (i) mathematical equations in the curriculum, (ii) means, (iii) rates,
# (iv) ratios, (v) percentages and percent changes.
#
# Essential knowledge relied on, in the framework's own terms:
#   8.4.A.1  CARRYING CAPACITY is the SUSTAINABLE ABUNDANCE of a species that
#            can be supported by the ecosystem's TOTAL AVAILABLE RESOURCES.
#   8.4.A.2  as limits to growth attributable to DENSITY-DEPENDENT AND
#            DENSITY-INDEPENDENT factors are imposed, a LOGISTIC GROWTH MODEL
#            TYPICALLY ENSUES.
#            RELEVANT EQUATION: dN/dt = rmax times N times the quantity K minus
#            N all divided by K, where dt is the change in time, N the
#            population size, dN the change in population size, rmax the
#            maximum per capita growth rate and K the CARRYING CAPACITY.
#
# WHAT THE CED NAMES AND DOES NOT DEFINE. EK 8.4.A.2 names density-dependent
# and density-independent factors and defines neither, exactly as EK 7.10.C.2
# names pre-zygotic and post-zygotic mechanisms without listing any. So no key
# here asserts that any particular factor is of one kind or the other on the
# framework's authority. The classification items supply, in the stimulus
# itself, whether the strength of a limit changes with the density of the
# population, and the key turns on the division the two words themselves make.
# Anything else would be inventing content, which SCIENCE_BRIEF.md forbids.
#
# THE ARITHMETIC IS THE GATE. SCIENCE_BRIEF.md names this topic as one of the
# few in Biology a machine can check, so every figure any key states is
# RECOMPUTED in verify_b8_4.py -- from the numbers PARSED OUT OF THE STEM for
# items 14 to 19, and from the table for items 20 to 28. Every calculation is
# one or two steps and calculator-free. In every stem the three quantities are
# given in the same order, carrying capacity then maximum per capita growth
# rate then current population size, so the check can read them positionally
# and still fail if a stem is edited.
#
# NO GROWTH CURVE IS EVER REFERRED TO. The logistic curve is the classic figure
# and the bank cannot show one, so the data live in a table of population sizes
# against rates of change and the verifier bars any phrase promising a picture.
#
# DELIBERATE OMISSIONS. The exponential model, the equation dN/dt = B minus D,
# and birth and death rates are EK 8.3.A and are asked in b8_3. Exactly ONE
# item here, q29, sets the two equations side by side, and it does so to
# identify the term the logistic model adds, which is this topic's own
# equation. Changes in energy availability changing population size are
# EK 8.2.C.1 and are asked in b8_2.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset, so the equation is written out in words.
TOPIC = ("8.4", "Effect of Density on Populations", 8)

_T_LOG = dict(
    headers=["Population size N", "Change in population size per unit time"],
    rows=[["100", "9"],
          ["500", "25"],
          ["900", "9"],
          ["1000", "0"]])

_T_FACTORS = dict(
    headers=["Limit on growth reported for a population",
             "Does the strength of this limit change as the population becomes more crowded?"],
    rows=[["Competition among individuals for a limited food supply", "Yes"],
          ["Spread of an infectious disease by contact between individuals", "Yes"],
          ["Accumulation of waste products in a crowded habitat", "Yes"],
          ["A frost that kills the same proportion of individuals whatever the population size", "No"]])

QUESTIONS = [
 dict(q="According to the course framework, what is carrying capacity?",
   choices=[
     "The sustainable abundance of a species that can be supported by the ecosystem's total available resources",
     "The largest number of individuals a species has ever reached anywhere",
     "The number of individuals born in an ecosystem in one year",
     "The maximum per capita growth rate of a population",
     "The number of species an ecosystem contains"], ans=0,
   why="EK 8.4.A.1 gives that definition in as many words. Carrying capacity is a property of the ecosystem's resources and the species together, not a record of past abundance and not a growth rate."),

 dict(q="According to the framework, what supports the carrying capacity of a species in an ecosystem?",
   choices=["The ecosystem's total available resources", "The number of predators present alone",
            "The area of the ecosystem alone", "The maximum per capita growth rate of the species",
            "The number of individuals currently present"], ans=0,
   why="EK 8.4.A.1 states that carrying capacity is the sustainable abundance that can be supported by the ecosystem's TOTAL AVAILABLE RESOURCES. The current population size is what carrying capacity is compared against, not what sets it."),

 dict(q="The framework calls carrying capacity a SUSTAINABLE abundance. What does that word add to the definition?",
   choices=[
     "The abundance is one the available resources can go on supporting rather than one reached briefly",
     "The abundance is the smallest a population can fall to and recover",
     "The abundance can never be exceeded even for a moment",
     "The abundance is measured only in the absence of resources",
     "The abundance is the same for every species in the ecosystem"], ans=0,
   why="EK 8.4.A.1 defines carrying capacity as the sustainable abundance that can be supported by the ecosystem's total available resources. Sustainable points to what the resources can go on supporting, which is why a momentary peak is not the same quantity."),

 dict(q="According to the framework, what typically follows once limits to growth are imposed on a population?",
   choices=["A logistic growth model", "An exponential growth model",
            "A model in which population size never changes",
            "A model in which the population declines to zero",
            "No model, because limited populations cannot be modelled"], ans=0,
   why="EK 8.4.A.2 states that as limits to growth attributable to density-dependent and density-independent factors are imposed, a logistic growth model typically ensues. Exponential growth is what EK 8.3.A.2 assigns to reproduction without constraints."),

 dict(q="EK 8.4.A.2 says a logistic growth model TYPICALLY ensues. What does that qualifier allow?",
   choices=[
     "That the logistic model is the usual result of imposing limits, not an outcome guaranteed in every case",
     "That the logistic model applies to every population at every time",
     "That the logistic model never applies to real populations",
     "That limits to growth are never actually imposed",
     "That the model applies only when no limits are imposed"], ans=0,
   why="The framework writes typically rather than always. A stated tendency describes the usual outcome and leaves room for cases that depart from it, which is why an absolute reading of the statement is wrong."),

 dict(q="In the logistic growth equation the framework prints, what does K represent?",
   choices=["The carrying capacity", "The current population size",
            "The maximum per capita growth rate", "The change in population size",
            "The length of the time interval"], ans=0,
   why="The CED defines K as the carrying capacity in the logistic growth equation for this topic. The current population size is N, the maximum per capita growth rate is rmax and the change in population size is dN."),

 dict(q="A population's maximum per capita growth rate and its current size both stay the same, but the carrying capacity of its ecosystem falls while remaining above the population size. What does the logistic equation predict for the change in population size per unit time?",
   choices=[
     "It falls, because the unused share of the carrying capacity is smaller",
     "It rises, because the population is now closer to its carrying capacity",
     "It is unchanged, because the per capita rate and the population size are unchanged",
     "It becomes negative, because the carrying capacity has fallen",
     "It cannot be predicted without knowing the birth rate and the death rate separately"], ans=0,
   why="The framework prints dN/dt equal to rmax times N times the quantity K minus N all divided by K. Holding rmax and N fixed and lowering K shrinks the last factor, so the product shrinks; the factor stays positive because the stem keeps the population below the carrying capacity."),

 dict(q="In the logistic equation, what happens to the quantity K minus N all divided by K when the population is very small compared with the carrying capacity?",
   choices=[
     "It approaches one, so the growth term is close to what unconstrained growth would give",
     "It approaches zero, so growth nearly stops",
     "It becomes negative, so the population declines",
     "It becomes larger than one, so growth exceeds the unconstrained rate",
     "It cannot be evaluated when the population is small"], ans=0,
   why="With N small compared with K, the numerator K minus N is nearly K, so the quotient is nearly one and the whole expression is nearly rmax times N. That is the same product the framework's exponential equation gives."),

 dict(q="In the logistic equation, what is the value of the quantity K minus N all divided by K when the population size equals the carrying capacity?",
   choices=["Zero, so the change in population size per unit time is zero",
            "One, so growth continues at the maximum rate",
            "A negative value, so the population declines rapidly",
            "A value that depends on rmax",
            "A value that cannot be determined without the birth rate"], ans=0,
   why="If N equals K then K minus N is zero, so the quotient is zero and the whole product is zero whatever rmax and N are. That is how the model represents a population at its carrying capacity."),

 dict(q="What does the logistic equation give for the change in population size per unit time if the population size exceeds the carrying capacity?",
   choices=["A negative value, so the model predicts a decline",
            "A positive value, so the model predicts continued growth",
            "Zero, because the model stops at the carrying capacity",
            "A value equal to rmax times N",
            "A value that depends only on K"], ans=0,
   why="If N exceeds K then K minus N is negative, so the quotient is negative and the product rmax times N times that quotient is negative. This is what the printed equation yields; the framework does not describe the case separately."),

 dict(q="What distinguishes a density-dependent limit on growth from a density-independent one?",
   choices=[
     "Whether the strength of the limit changes as the population becomes more crowded",
     "Whether the limit acts on plants or on animals",
     "Whether the limit is caused by living or by non-living components",
     "Whether the limit occurs in summer or in winter",
     "Whether the limit can be measured at all"], ans=0,
   why="EK 8.4.A.2 names density-dependent and density-independent factors and defines neither, so the division the framework itself supplies is the one the two words make: whether the effect depends on the density of the population it acts on."),

 dict(q="As a population becomes more crowded, individuals in it compete more intensely for a limited supply of a resource, so the limit on growth grows stronger. This limit is best described as",
   choices=["density-dependent", "density-independent",
            "a carrying capacity", "a maximum per capita growth rate",
            "an exponential growth model"], ans=0,
   why="EK 8.4.A.2 names density-dependent factors without listing any, so the classification rests on the division the term itself makes. The scenario states that the strength of the limit rises with crowding, which is dependence on density."),

 dict(q="A frost removes the same proportion of a population whether that population is sparse or crowded. This limit is best described as",
   choices=["density-independent", "density-dependent",
            "a carrying capacity", "a per capita growth rate",
            "the unused fraction of the carrying capacity"], ans=0,
   why="EK 8.4.A.2 names density-independent factors without listing any, so the classification rests on the division the term makes. The scenario states that the proportion removed does not change with density, which is independence of density."),

 dict(q="A population lives in an ecosystem with a carrying capacity of 1000 individuals, has a maximum per capita growth rate of 0.10 per year, and currently numbers 200 individuals. What does the logistic equation give for its change in population size per unit time?",
   choices=["16 individuals per year", "20 individuals per year", "80 individuals per year",
            "4 individuals per year", "200 individuals per year"], ans=0,
   why="The framework prints dN/dt equal to rmax times N times the quantity K minus N all divided by K. Multiplying the per capita rate by the population size and then by the unused fraction of the carrying capacity gives the answer; omitting the last factor gives one of the distractors."),

 dict(q="A second population lives where the carrying capacity is 800 individuals, has a maximum per capita growth rate of 0.20 per year, and currently numbers 400 individuals. What does the logistic equation give for its change in population size per unit time?",
   choices=["40 individuals per year", "80 individuals per year", "20 individuals per year",
            "160 individuals per year", "400 individuals per year"], ans=0,
   why="The framework prints dN/dt equal to rmax times N times the quantity K minus N all divided by K. This population sits at half its carrying capacity, so the last factor is one half and the product is half of rmax times N."),

 dict(q="A third population lives where the carrying capacity is 500 individuals, has a maximum per capita growth rate of 0.30 per year, and currently numbers 500 individuals. What does the logistic equation give for its change in population size per unit time?",
   choices=["Zero individuals per year", "150 individuals per year", "500 individuals per year",
            "75 individuals per year", "250 individuals per year"], ans=0,
   why="If N equals K then K minus N is zero, so the last factor of the printed equation is zero and the whole product is zero however large rmax and N may be. A population at its carrying capacity does not change in size under this model."),

 dict(q="An ecosystem has a carrying capacity of 2000 individuals of one species and currently holds 500 of them. What is the value of the quantity K minus N all divided by K for this population?",
   choices=["0.75", "0.25", "0.50", "1.50", "0.30"], ans=0,
   why="Subtracting the current size from the carrying capacity and dividing by the carrying capacity gives the share of the carrying capacity that is still unused. That share is the factor the logistic equation multiplies the unconstrained growth term by."),

 dict(q="A fourth population lives where the carrying capacity is 600 individuals, has a maximum per capita growth rate of 0.40 per year, and currently numbers 150 individuals. What does the logistic equation give for its change in population size per unit time?",
   choices=["45 individuals per year", "60 individuals per year", "90 individuals per year",
            "30 individuals per year", "150 individuals per year"], ans=0,
   why="The framework prints dN/dt equal to rmax times N times the quantity K minus N all divided by K. The per capita rate times the population size gives the unconstrained term, and multiplying by the unused share of the carrying capacity gives the answer."),

 dict(q="An ecosystem has a carrying capacity of 1200 individuals of one species and currently holds 300 of them. The population is at what percentage of its carrying capacity?",
   choices=["25 percent", "75 percent", "30 percent", "40 percent", "4 percent"], ans=0,
   why="Skill 5.A includes percentages. Dividing the current population size by the carrying capacity and expressing the result as a percentage gives the answer; the complement of that figure is the unused share the logistic equation uses."),

 dict(q="The table gives the change in population size per unit time at four population sizes for one population whose carrying capacity is 1000 individuals and whose maximum per capita growth rate is 0.10 per year. At which of the listed sizes is the change in population size per unit time greatest?",
   table=_T_LOG,
   choices=["500 individuals", "100 individuals", "900 individuals",
            "1000 individuals", "The change is the same at all four sizes"], ans=0,
   why="The logistic equation multiplies a term that grows with N by a term that shrinks as N approaches K, so the product peaks between the two extremes. The table records the largest change at that intermediate size."),

 dict(q="Why does the table record a change of zero at the largest population size listed?",
   table=_T_LOG,
   choices=[
     "The population size equals the carrying capacity, so the quantity K minus N all divided by K is zero",
     "The maximum per capita growth rate has fallen to zero",
     "No individuals are being born or dying at that size",
     "The carrying capacity has been exceeded, so the population is declining",
     "The table is incomplete at that size"], ans=0,
   why="The stem gives the carrying capacity, and the largest listed size equals it. The printed equation then makes the last factor zero, so the whole product is zero however large rmax and N are; that is not the same as no births and no deaths occurring."),

 dict(q="Which two of the population sizes in that table give the same change in population size per unit time?",
   table=_T_LOG,
   choices=["100 individuals and 900 individuals", "100 individuals and 500 individuals",
            "500 individuals and 900 individuals", "500 individuals and 1000 individuals",
            "No two of the sizes give the same change"], ans=0,
   why="The logistic equation multiplies a factor rising with N by a factor falling as N approaches K, so two sizes placed symmetrically about the midpoint give the same product. The two sizes in the key are equally far from the midpoint of the carrying capacity."),

 dict(q="Using the same table, what is the change in population size per unit time when the population numbers 100 individuals?",
   table=_T_LOG,
   choices=["9 individuals per year", "25 individuals per year", "10 individuals per year",
            "90 individuals per year", "Zero individuals per year"], ans=0,
   why="Skill 4.B, identifying a specific data point, checked against skill 5.A: the printed equation applied to that size, the stated carrying capacity and the stated per capita rate reproduces the value the table records."),

 dict(q="Using the same table, what happens to the change in population size per unit time as the population rises from the middle of the range toward the carrying capacity?",
   table=_T_LOG,
   choices=["It falls", "It continues to rise", "It stays the same",
            "It rises and then falls again", "It becomes negative"], ans=0,
   why="The logistic equation's last factor shrinks toward zero as N approaches K, and beyond the midpoint that shrinking outweighs the growth of the term rising with N. The table records exactly that fall across its upper sizes."),

 dict(q="What do the values in that table show about a population approaching its carrying capacity?",
   table=_T_LOG,
   choices=[
     "Its rate of increase falls toward zero, so its size levels off rather than continuing to climb",
     "Its rate of increase keeps rising without limit",
     "Its rate of increase stays constant at every size",
     "Its size falls back to where it started",
     "Its carrying capacity rises to match its size"], ans=0,
   why="EK 8.4.A.2 states that a logistic growth model typically ensues once limits are imposed, and the printed equation drives the change in population size to zero as N approaches K. The table's final entries record that approach."),

 dict(q="The table lists four limits on the growth of a population and records whether the strength of each changes as the population becomes more crowded. How many of the four are density-dependent limits?",
   table=_T_FACTORS,
   choices=["Three", "One", "Two", "Four", "Zero"], ans=0,
   why="EK 8.4.A.2 names density-dependent factors without listing any, so the classification must rest on the division the term itself makes. Counting the rows the table records as changing in strength with crowding gives the number."),

 dict(q="Which of the limits listed in that table is a density-independent limit?",
   table=_T_FACTORS,
   choices=[
     "The frost that kills the same proportion of individuals whatever the population size",
     "Competition among individuals for a limited food supply",
     "The spread of an infectious disease by contact between individuals",
     "The accumulation of waste products in a crowded habitat",
     "All four limits are density-independent"], ans=0,
   why="EK 8.4.A.2 names density-independent factors and defines none, so the classification rests on the division the term makes. Exactly one row of the table records a limit whose strength does not change as the population becomes more crowded."),

 dict(q="What property of a limit does the second column of that table report, and why does it settle the classification?",
   table=_T_FACTORS,
   choices=[
     "Whether the limit's strength changes with crowding, which is exactly what the two terms divide on",
     "Whether the limit is caused by a living component, which is what the two terms divide on",
     "Whether the limit occurs in winter, which is what the two terms divide on",
     "How many individuals the limit removes, which is what the two terms divide on",
     "Nothing relevant, since the classification depends on the species involved"], ans=0,
   why="EK 8.4.A.2 names the two kinds of factor and defines neither, so the only division the framework itself supplies is the one carried in the terms: dependence or independence with respect to the density of the population. That is what the column reports."),

 dict(q="How does the logistic growth equation differ from the exponential growth equation the framework prints?",
   choices=[
     "The logistic equation multiplies the same product of per capita rate and population size by the unused share of the carrying capacity",
     "The logistic equation replaces the per capita growth rate with the birth rate",
     "The logistic equation removes the population size from the calculation",
     "The logistic equation applies only when there is no carrying capacity",
     "The two equations are identical in every respect"], ans=0,
   why="The framework prints dN/dt equal to rmax times N for reproduction without constraints and dN/dt equal to rmax times N times the quantity K minus N all divided by K once limits are imposed. The second is the first multiplied by one additional factor."),

 dict(q="Taken together, what do the framework's statements about density and population growth assert?",
   choices=[
     "Carrying capacity is the sustainable abundance an ecosystem's resources can support, and once limits attributable to density-dependent and density-independent factors are imposed a logistic growth model typically ensues",
     "Carrying capacity is the largest population ever recorded, and growth is always exponential",
     "Carrying capacity varies with the maximum per capita growth rate, and growth always stops abruptly",
     "Density has no effect on the growth of any population",
     "Only density-independent factors impose limits on growth"], ans=0,
   why="EK 8.4.A.1 defines carrying capacity as the sustainable abundance supported by the ecosystem's total available resources, and EK 8.4.A.2 states that a logistic growth model typically ensues once limits attributable to both kinds of factor are imposed. Each distractor contradicts one of those two sentences."),
]
