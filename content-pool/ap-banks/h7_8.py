# AP CHEMISTRY 7.8 Representations of Equilibrium
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.8.A: represent a system undergoing a reversible reaction with a
# particulate model. Suggested skill 3.C, represent visually the relationship between the
# structures and interactions across multiple levels or scales.
#
# Essential knowledge relied on, in the framework's own words:
#   7.8.A.1  Particulate representations can be used to describe the relative numbers of
#            reactant and product particles present prior to and at equilibrium, and the
#            value of the equilibrium constant.
#
# HOW THE PARTICULATE MODEL IS CARRIED WITHOUT A PICTURE. This bank cannot show images,
# and SCIENCE_BRIEF.md forbids a stem that describes a figure the student cannot see. So
# every particulate representation here is given as a COUNT OF PARTICLES in a table, with
# the stem stating that each particle stands for 1.0 mol and the container holds 1.0 L.
# That makes the count and the molar concentration numerically equal, which is exactly the
# relationship a particulate diagram is drawn to convey, and it leaves nothing to be read
# off a picture. No item below says "shown", "diagram" or "figure".
#
# SCOPE. 7.4 owns obtaining K from measured concentrations and 7.7 owns solving for
# equilibrium amounts from initial conditions. Every item here is about what a set of
# particle counts BEFORE and AT equilibrium can and cannot be made to say.
#
# ARITHMETIC. Every constant below is recomputed in verify_h7_8.py from the tabulated
# counts alone.
#
# NOTATION. export_units.py does not typeset Chemistry; the few spans below are
# hand-written.
TOPIC = ("7.8", "Representations of Equilibrium", 7)

_T_AB = dict(
    headers=["Container", "Particles of A", "Particles of B"],
    rows=[["Before any reaction", "12", "0"],
          ["At equilibrium", "3", "9"]])

_T_DIMER = dict(
    headers=["Container", "Particles of X", "Particles of Y"],
    rows=[["Before any reaction", "12", "0"],
          ["At equilibrium", "4", "4"]])

_T_EXCHANGE = dict(
    headers=["Container", "Particles of A2", "Particles of B2", "Particles of AB"],
    rows=[["Before any reaction", "6", "6", "0"],
          ["At equilibrium", "2", "2", "8"]])

_T_TIME = dict(
    headers=["Time", "Particles of A", "Particles of B"],
    rows=[["0 minutes", "16", "0"],
          ["1 minute", "10", "6"],
          ["2 minutes", "8", "8"],
          ["3 minutes", "8", "8"]])

_T_CANDIDATES = dict(
    headers=["Container", "Particles of A", "Particles of B"],
    rows=[["P", "4", "8"],
          ["Q", "8", "4"],
          ["R", "6", "6"],
          ["S", "2", "10"]])

_T_SPLIT = dict(
    headers=["Container", "Particles of X", "Particles of Y"],
    rows=[["Before any reaction", "10", "0"],
          ["At equilibrium", "8", "4"]])

QUESTIONS = [

 dict(q="A rigid 1.0 L container is charged with substance A for the reaction A(g) to "
        "B(g). Each particle counted in the table stands for 1.0 mol. What is the value "
        "of the equilibrium constant?",
      table=_T_AB,
      choices=["K = 3.0", "K = 0.33", "K = 9.0", "K = 0.75", "K = 12"],
      ans=0,
      why="EK 7.8.A.1 states that a particulate representation can describe the value of "
          "the equilibrium constant as well as the relative numbers of particles. With "
          "1.0 mol per particle in 1.0 L, the equilibrium concentrations are 9 M of B "
          "and 3 M of A, so the constant is nine divided by three, which is three."),

 dict(q="In the same 1.0 L container for A(g) to B(g), what fraction of the original "
        "particles of A has been converted by the time equilibrium is reached?",
      table=_T_AB,
      choices=["Three quarters of them", "One quarter of them", "One third of them",
               "All of them", "One ninth of them"],
      ans=0,
      why="EK 7.8.A.1 makes the counts before and at equilibrium comparable. Twelve "
          "particles of A fall to three, so nine of the twelve, which is three quarters, "
          "have been converted, and three of the twelve remain."),

 dict(q="A rigid 1.0 L container is charged with substance X for the reaction 2 X(g) to "
        "Y(g), with each particle standing for 1.0 mol. What is the equilibrium "
        "constant?",
      table=_T_DIMER,
      choices=["K = 0.25", "K = 1.0", "K = 4.0", "K = 0.50", "K = 16"],
      ans=0,
      why="The equilibrium concentrations are 4 M of X and 4 M of Y, and the coefficient "
          "of two puts the concentration of X into the expression as a square. Four "
          "divided by sixteen is 0.25. Ignoring the coefficient would give one instead, "
          "which is the error the particulate count is meant to expose."),

 dict(q="For the same reaction 2 X(g) to Y(g), the counts before reaction and at "
        "equilibrium are tabulated. How many particles of X were consumed for every "
        "particle of Y that formed?",
      table=_T_DIMER,
      choices=["Two particles of X for each particle of Y",
               "One particle of X for each particle of Y",
               "Four particles of X for each particle of Y",
               "One particle of X for every two particles of Y",
               "Three particles of X for each particle of Y"],
      ans=0,
      why="The count of X falls from twelve to four, a loss of eight, while the count of "
          "Y rises from zero to four. Eight lost for four gained is a ratio of two to "
          "one, which is exactly the ratio of coefficients in the balanced equation, and "
          "EK 7.8.A.1 makes that comparison the point of a particulate representation."),

 dict(q="A rigid 1.0 L container holds A2(g) and B2(g) for the reaction A2(g) + B2(g) to "
        "2 AB(g), with each particle standing for 1.0 mol. What is the equilibrium "
        "constant?",
      table=_T_EXCHANGE,
      choices=["K = 16", "K = 4.0", "K = 2.0", "K = 8.0", "K = 64"],
      ans=0,
      why="The equilibrium concentrations are 2 M of A2, 2 M of B2 and 8 M of AB. The "
          "product carries a coefficient of two, so its concentration is squared: 64 "
          "divided by the product of two and two is 16. Failing to square the product "
          "term would give four."),

 dict(q="In that same exchange reaction, what evidence in the two rows of counts shows "
        "that atoms have been conserved?",
      table=_T_EXCHANGE,
      choices=[
        "Twelve diatomic particles are present before reaction and twelve after it, "
        "since four of each reactant became eight of the product",
        "The number of particles of AB at equilibrium equals the number of particles of "
        "A2 before reaction",
        "Every count in the equilibrium row is smaller than the corresponding count in "
        "the row before reaction",
        "The total number of particles has doubled, which is what conservation of atoms "
        "requires for this equation",
        "The counts of A2 and B2 remain equal to each other, which is the only "
        "conservation requirement"],
      ans=0,
      why="Before reaction there are six A2 and six B2, twelve particles in all; at "
          "equilibrium there are two A2, two B2 and eight AB, again twelve. The equation "
          "makes two particles from two, so the total count cannot change, and EK "
          "7.8.A.1 makes the counts the thing a particulate representation reports."),

 dict(q="Counts of particles in a rigid 1.0 L container are recorded at four times for "
        "the reaction A(g) to B(g). At which time has the system first reached "
        "equilibrium?",
      table=_T_TIME,
      choices=["At 2 minutes", "At 0 minutes", "At 1 minute", "At 3 minutes",
               "It has not reached equilibrium at any tabulated time"],
      ans=0,
      why="The counts change between every earlier pair of rows and then stop changing "
          "between 2 minutes and 3 minutes. EK 7.8.A.1 makes the relative numbers of "
          "particles the observable, and constant relative numbers is what a particulate "
          "representation of equilibrium looks like."),

 dict(q="Using the same four sets of counts for A(g) to B(g), what is the equilibrium "
        "constant?",
      table=_T_TIME,
      choices=["K = 1.0", "K = 8.0", "K = 0.60", "K = 16", "K = 2.0"],
      ans=0,
      why="Once the counts stop changing they are eight of A and eight of B, so with "
          "1.0 mol per particle in 1.0 L the constant is eight divided by eight, which "
          "is one. Reading the counts at one minute instead would give 0.60, which is a "
          "reaction quotient rather than the constant."),

 dict(q="Which container in the table could be at equilibrium for the reaction A(g) to "
        "B(g) if the equilibrium constant is 2.0? Each particle stands for 1.0 mol in a "
        "1.0 L container.",
      table=_T_CANDIDATES,
      choices=["Container P", "Container Q", "Container R", "Container S",
               "None of the four containers"],
      ans=0,
      why="The four containers give ratios of B to A of 2.0, 0.50, 1.0 and 5.0. Only the "
          "first equals the stated constant, and EK 7.8.A.1 makes the value of the "
          "equilibrium constant something a particulate count can be tested against."),

 dict(q="Using the same four containers and the same reaction A(g) to B(g), which "
        "container has the LARGEST reaction quotient?",
      table=_T_CANDIDATES,
      choices=["Container S", "Container P", "Container Q", "Container R",
               "All four have the same reaction quotient"],
      ans=0,
      why="The ratios of B to A are 2.0, 0.50, 1.0 and 5.0 for the four containers, so "
          "the largest is the one holding two particles of A and ten of B. EK 7.8.A.1 "
          "makes such a comparison of relative numbers the purpose of a particulate "
          "representation."),

 dict(q="A rigid 1.0 L container is charged with X(g) alone for the reaction X(g) to "
        "2 Y(g), with each particle standing for 1.0 mol. What is the equilibrium "
        "constant?",
      table=_T_SPLIT,
      choices=["K = 2.0", "K = 0.50", "K = 8.0", "K = 4.0", "K = 0.25"],
      ans=0,
      why="The equilibrium concentrations are 8 M of X and 4 M of Y, and the coefficient "
          "of two squares the concentration of Y: sixteen divided by eight is two. "
          "Omitting the square would give 0.50."),

 dict(q="In that same reaction X(g) to 2 Y(g), the count of X falls by two while the "
        "count of Y rises by four. What does that pairing of changes establish?",
      table=_T_SPLIT,
      choices=[
        "The changes are in the ratio of the coefficients in the balanced equation",
        "The reaction has gone to completion, since Y outnumbers the X consumed",
        "The equilibrium constant must be smaller than one for this reaction",
        "The total number of particles in the container has been conserved",
        "The two substances must have equal concentrations once equilibrium is reached"],
      ans=0,
      why="One X becomes two Y, so a fall of two in X must accompany a rise of four in "
          "Y. EK 7.8.A.1 makes those relative numbers the content of a particulate "
          "representation. The total count rises here rather than being conserved, and "
          "eight particles of X remain, so nothing has gone to completion."),

 dict(q="What does a particulate representation of a system at equilibrium show about "
        "the forward and reverse reactions?",
      choices=[
        "The counts of each species stay constant while particles continue to react in "
        "both directions",
        "The counts of each species stay constant because all reaction has ceased",
        "The counts of each species become equal to one another once equilibrium is "
        "reached",
        "The count of product always exceeds the count of reactant at equilibrium",
        "The counts oscillate visibly between two sets of values once equilibrium is "
        "reached"],
      ans=0,
      why="EK 7.8.A.1 has the representation describe the relative numbers of particles "
          "at equilibrium, and those numbers are constant because the two opposing "
          "reactions occur at equal rates rather than because they have stopped. Equal "
          "counts are a special case set by the value of K, not a general feature."),

 dict(q="Two rigid containers of the same volume hold the same reaction at the same "
        "temperature. One was charged with reactant alone and the other with product "
        "alone. What must their particle counts have in common at equilibrium?",
      choices=[
        "The ratio of product particles to reactant particles required by the "
        "equilibrium constant",
        "The total number of particles present in each container",
        "The number of product particles present in each container",
        "The number of reactant particles present in each container",
        "Nothing at all, since they began from opposite starting mixtures"],
      ans=0,
      why="The equilibrium constant is fixed by the temperature, so both containers must "
          "reach counts in the ratio it requires, which EK 7.8.A.1 says a particulate "
          "representation can display. The absolute counts depend on how much material "
          "was charged and so need not agree."),

 dict(q="A rigid container is charged with 20 particles of A for A(g) to B(g), and the "
        "equilibrium constant is 4.0. How many particles of B are present at "
        "equilibrium?",
      choices=["16 particles of B", "4 particles of B", "5 particles of B",
               "10 particles of B", "20 particles of B"],
      ans=0,
      why="One particle of A becomes one of B, so the two counts must sum to twenty, and "
          "the constant requires four times as many B as A. Sixteen and four satisfy "
          "both conditions, and EK 7.8.A.1 makes those relative numbers what a "
          "particulate representation displays."),

 dict(q="A rigid container is charged with 15 particles of C for C(g) to D(g), and the "
        "equilibrium constant is 0.50. How many particles of C remain at equilibrium?",
      choices=["10 particles of C", "5 particles of C", "7 particles of C",
               "8 particles of C", "12 particles of C"],
      ans=0,
      why="The counts must sum to fifteen and the ratio of D to C must be one half, so "
          "the counts are ten of C and five of D. A constant below one leaves more "
          "reactant than product, which is the check on the split."),

 dict(q="A student proposes a set of counts for a system at equilibrium in which the "
        "reactant count is zero and the product count is twenty. What is wrong with that "
        "proposal?",
      choices=[
        "A count of zero for the reactant would make the equilibrium expression "
        "undefined, so some reactant must remain",
        "The counts of reactant and product must always be equal at equilibrium",
        "The product count may never exceed the reactant count in any representation",
        "The total count of particles must be an even number for the expression to be "
        "evaluated",
        "Nothing is wrong with it, since a large equilibrium constant consumes all the "
        "reactant"],
      ans=0,
      why="The equilibrium expression divides by the reactant term, so a reactant count "
          "of zero has no value of K attached to it. EK 7.8.A.1 ties the representation "
          "to a value of the equilibrium constant, and a very large constant leaves the "
          "reactant few in number rather than absent."),

 dict(q="For the reaction A(g) to B(g) in a rigid container, which pair of counts "
        "represents a system with an equilibrium constant much larger than one?",
      choices=["2 particles of A and 18 particles of B",
               "18 particles of A and 2 particles of B",
               "10 particles of A and 10 particles of B",
               "12 particles of A and 8 particles of B",
               "20 particles of A and 0 particles of B"],
      ans=0,
      why="A constant much larger than one requires the product term to be much larger "
          "than the reactant term, which is a count of product far exceeding the count "
          "of reactant. EK 7.8.A.1 states that a particulate representation can describe "
          "the value of the equilibrium constant in exactly this way."),

 dict(q="Two particulate representations of the same reaction at the same temperature "
        "give different absolute counts but the same ratio of product to reactant. What "
        "does that agreement establish?",
      choices=[
        "Both containers are at equilibrium for that reaction at that temperature",
        "Both containers were charged with the same total amount of material",
        "The two containers must be at different temperatures after all",
        "One container is at equilibrium and the other is not",
        "The reaction has gone to completion in both containers"],
      ans=0,
      why="The equilibrium constant is the required ratio at a given temperature, so two "
          "containers matching it are both at equilibrium, whatever their absolute "
          "counts. EK 7.8.A.1 links the relative numbers, not the absolute numbers, to "
          "the value of the constant."),

 dict(q="A container charged with reactant alone is examined at several times, and the "
        "count of product rises quickly at first and then more slowly until it stops "
        "changing. What accounts for the slowing?",
      choices=[
        "The reverse reaction speeds up as product accumulates, so the net change "
        "shrinks toward zero",
        "The forward reaction stops entirely once half the reactant has been consumed",
        "The reactant particles become too large to react as the container fills with "
        "product",
        "The temperature of the container must be falling as the reaction proceeds",
        "The equilibrium constant decreases steadily as the count of product rises"],
      ans=0,
      why="A particulate account of approach to equilibrium has the reverse process "
          "becoming faster as product particles accumulate, until the two opposing "
          "processes match and the counts stop changing. EK 7.8.A.1 makes those "
          "unchanging relative numbers the mark of equilibrium; K is fixed by "
          "temperature and does not drift as the counts change."),

 dict(q="For 2 X(g) to Y(g) in a rigid 1.0 L container with 1.0 mol per particle, a "
        "representation shows 2 particles of X and 8 particles of Y at equilibrium. What "
        "is the equilibrium constant?",
      choices=["K = 2.0", "K = 4.0", "K = 0.50", "K = 16", "K = 0.25"],
      ans=0,
      why="The concentration of X enters as a square because of its coefficient of two, "
          "so the constant is eight divided by the square of two, which is eight divided "
          "by four, or two. Dividing eight by two without squaring would give four."),

 dict(q="Why can a single particulate representation of one container at equilibrium NOT "
        "establish how fast that equilibrium was reached?",
      choices=[
        "Because the counts describe the composition at one moment and say nothing about "
        "the time taken to arrive at it",
        "Because rate and equilibrium constant are numerically identical quantities",
        "Because a representation at equilibrium always describes an instantaneous "
        "reaction",
        "Because the counts at equilibrium are the same for every reaction at a given "
        "temperature",
        "Because the equilibrium constant is defined only for reactions that are slow"],
      ans=0,
      why="EK 7.8.A.1 assigns the representation the relative numbers of particles before "
          "and at equilibrium and the value of the constant. None of those is a rate: a "
          "composition at one moment carries no information about the interval that "
          "produced it."),

 dict(q="A representation of a system before reaction shows 10 particles of A and 10 of "
        "B for the reaction A(g) to B(g). At equilibrium the same container shows 5 "
        "particles of A. What is the equilibrium constant?",
      choices=["K = 3.0", "K = 1.0", "K = 0.33", "K = 2.0", "K = 5.0"],
      ans=0,
      why="Five particles of A have been converted, so B rises from ten to fifteen while "
          "A falls to five. The constant is fifteen divided by five, which is three. "
          "Starting counts of both species are permitted; only the equilibrium counts "
          "enter the expression."),

 dict(q="For A(g) to B(g), a first container holds 4 particles of A and 8 of B, and a "
        "second holds 8 particles of A and 16 of B. Which statement comparing the two is "
        "correct?",
      choices=[
        "Both have the same reaction quotient, because the ratio of the counts is the "
        "same in each",
        "The second has twice the reaction quotient of the first, because every count "
        "is doubled",
        "The second has four times the reaction quotient of the first",
        "The first has the larger reaction quotient, because it holds fewer particles",
        "The two cannot be compared without knowing the temperature of each container"],
      ans=0,
      why="For a reaction converting one particle into one particle, the quotient is the "
          "ratio of the two counts, and doubling both counts leaves that ratio at two. "
          "EK 7.8.A.1 ties the constant to the RELATIVE numbers of particles, which is "
          "why the absolute counts can differ."),

 dict(q="A representation of a rigid container shows the same total number of particles "
        "before reaction and at equilibrium. Which reaction is consistent with that "
        "observation?",
      choices=["A(g) + B(g) to C(g) + D(g)", "A(g) to 2 B(g)", "2 A(g) to B(g)",
               "A(g) + 2 B(g) to C(g)", "2 A(g) + B(g) to 3 C(g) + D(g)"],
      ans=0,
      why="The total count is preserved only when the number of particles on the two "
          "sides of the equation is equal, and two reactants giving two products is the "
          "one equation listed for which that holds. Each of the others changes the "
          "particle count as the reaction proceeds."),

 dict(q="Which comparison between a representation before reaction and one at "
        "equilibrium is the best evidence that the equilibrium constant is small?",
      choices=[
        "Only a few reactant particles have been replaced by product particles",
        "Every reactant particle has been replaced by a product particle",
        "The total number of particles has decreased sharply",
        "The reactant and product particles have become equal in number",
        "The number of particles of each kind has changed by the same amount"],
      ans=0,
      why="A small constant means the product term is small compared with the reactant "
          "term at equilibrium, so most of the reactant remains and only a few particles "
          "have been converted. EK 7.8.A.1 makes this before-and-at comparison the way a "
          "particulate representation carries the value of K."),

 dict(q="A representation is claimed to show the reaction 2 A(g) to B(g) at equilibrium "
        "with 6 particles of A and 3 of B, starting from 12 particles of A alone. Is the "
        "claim internally consistent?",
      choices=[
        "Yes, because six particles of A remain and the six consumed give three of B",
        "No, because the count of B should equal the count of A consumed",
        "No, because no particles of A should remain once B has formed",
        "Yes, but only if the container volume is exactly 1.0 L",
        "No, because the total number of particles must stay at twelve"],
      ans=0,
      why="Twelve particles of A fall to six, so six were consumed, and two A give one B, "
          "so three particles of B is exactly what those six produce. EK 7.8.A.1 makes "
          "the before-and-at counts comparable in just this way; the total count falls "
          "here because the equation makes one particle from two."),

 dict(q="At a higher temperature the same reaction is represented with more product "
        "particles and fewer reactant particles at equilibrium than before. What does "
        "that comparison establish?",
      choices=[
        "The equilibrium constant is larger at the higher temperature",
        "The equilibrium constant is unchanged, since only the counts differ",
        "The reaction has become faster but its constant cannot be compared",
        "The total number of particles must have increased with temperature",
        "The reaction has gone to completion at the higher temperature"],
      ans=0,
      why="EK 7.8.A.1 ties the relative numbers of particles at equilibrium to the value "
          "of the equilibrium constant, so a larger ratio of product to reactant at "
          "equilibrium is a larger constant. A change in the ratio at equilibrium is not "
          "a statement about speed."),

 dict(q="For A(g) to B(g) a container is charged with 24 particles of A, and at "
        "equilibrium 6 particles of A remain. What is the equilibrium constant?",
      choices=["K = 3.0", "K = 4.0", "K = 0.25", "K = 6.0", "K = 18"],
      ans=0,
      why="Eighteen of the twenty-four particles have become B, leaving six of A, so the "
          "constant is eighteen divided by six, which is three. Dividing the original "
          "twenty-four by six would give four, which uses the wrong row of counts."),

 dict(q="Which limitation applies to reading an equilibrium constant off a set of "
        "particle counts for a reaction involving a pure solid?",
      choices=[
        "The particles of the pure solid must be left out of the expression, so their "
        "count cannot enter the constant",
        "The particles of the pure solid must be counted twice, once for each phase "
        "present",
        "The constant cannot be evaluated at all when any solid is present in the "
        "container",
        "The count of solid particles replaces the count of every gaseous product",
        "The solid particles must be equal in number to the gaseous particles for "
        "equilibrium to exist"],
      ans=0,
      why="A pure solid has a concentration that does not depend on how much is present, "
          "so it is left out of the equilibrium expression and its count contributes "
          "nothing to the value. EK 7.8.A.1 lets a representation carry the value of the "
          "constant, but only through the species the expression actually contains."),

]
