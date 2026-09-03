# AP BIOLOGY 3.2 Environmental Impacts on Enzyme Function
# CED effective Fall 2025, Unit 3 Cellular Energetics. Big Idea 2 Energetics.
# Learning objectives 3.2.A (explain how changes to the structure of an enzyme
# may affect its function) and 3.2.B (explain how the cellular environment
# affects enzyme activity). Suggested skill 6.E, predict the causes or effects
# of a change in, or disruption to, one or more components in a biological
# system.
#
# Essential knowledge, in the framework's own terms:
#   3.2.A.1    Change to the molecular structure of a component in an enzymatic
#              system may result in a change to its function or efficiency.
#     i.       DENATURATION of proteins, such as enzymes, occurs when the
#              protein structure is disrupted by a change in temperature, pH,
#              or chemical environment, ELIMINATING the ability to catalyze
#              reactions.
#     ii.      Environmental temperatures and pH OUTSIDE THE OPTIMAL RANGE for
#              a given enzyme will cause changes to its structure (BY
#              DISRUPTING THE HYDROGEN BONDS), altering the efficiency with
#              which it catalyzes reactions.
#   3.2.A.2    In some cases, enzyme denaturation is REVERSIBLE, allowing the
#              enzyme to regain activity.
#   3.2.B.1    The RELATIVE CONCENTRATIONS of substrates and products determine
#              how efficiently an enzymatic reaction proceeds.
#   3.2.B.2    Higher environmental temperatures increase the average speed of
#              movement of molecules in a solution, increasing the FREQUENCY OF
#              COLLISIONS between enzymes and substrates and therefore
#              increasing the rate of reaction UNTIL THE OPTIMAL TEMPERATURE IS
#              ACHIEVED.
#   3.2.B.3    COMPETITIVE inhibitor molecules can bind REVERSIBLY to the ACTIVE
#              SITE of the enzyme. NONCOMPETITIVE inhibitors can bind to
#              ALLOSTERIC SITES, changing the activity of the enzyme.
#
# BOUNDARY WITH 3.1, HELD DELIBERATELY. Activation energy, the identity of
# enzymes as proteins, the shape-and-charge compatibility rule and the
# experimental-design skill 3.C belong to topic 3.1 and carry no key here.
# What is left to 3.2 is the environment: temperature, pH, chemical
# environment, inhibitors and the relative concentrations of substrate and
# product.
#
# ONE CHAINED INFERENCE, DECLARED. The framework does not print the sentence
# "excess substrate overcomes competitive inhibition". Items 11 and 16 reach it
# by chaining two statements the framework does print -- EK 3.2.B.3 (a
# competitive inhibitor binds REVERSIBLY to the ACTIVE SITE, the same site the
# substrate must occupy) and EK 3.2.B.1 (the RELATIVE concentrations of
# substrates determine how efficiently the reaction proceeds) -- and both keys
# are worded as occupancy of the active site, which is what those two sentences
# jointly say.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("3.2", "Environmental Impacts on Enzyme Function", 3)

_T_TEMP = dict(
    headers=["Temperature (degrees Celsius)",
             "Reaction rate (hypothetical, micromoles of product per minute)"],
    rows=[["10", "4"],
          ["20", "9"],
          ["30", "18"],
          ["37", "30"],
          ["45", "12"],
          ["55", "0"]])

_T_PH = dict(
    headers=["pH of the reaction mixture",
             "Rate for enzyme J (hypothetical, micromoles per minute)",
             "Rate for enzyme K (hypothetical, micromoles per minute)"],
    rows=[["2", "28", "0"],
          ["4", "14", "2"],
          ["6", "3", "12"],
          ["8", "0", "30"],
          ["10", "0", "9"]])

_T_INHIB = dict(
    headers=["Substrate concentration (millimolar)",
             "Rate with no inhibitor (hypothetical, micromoles per minute)",
             "Rate with inhibitor L (hypothetical, micromoles per minute)",
             "Rate with inhibitor M (hypothetical, micromoles per minute)"],
    rows=[["1", "10", "3", "5"],
          ["2", "18", "6", "9"],
          ["5", "32", "17", "16"],
          ["10", "40", "32", "20"],
          ["20", "44", "43", "22"]])

_T_RECOVER = dict(
    headers=["Treatment of the enzyme sample",
             "Rate during the treatment (hypothetical, micromoles per minute)",
             "Rate after return to the starting conditions (hypothetical, micromoles per minute)"],
    rows=[["Sample 1, held at the optimal temperature throughout", "25", "25"],
          ["Sample 2, warmed briefly above the optimal temperature", "6", "24"],
          ["Sample 3, boiled for ten minutes", "0", "0"]])

QUESTIONS = [
 dict(q="According to the framework, what happens to an enzyme when it is denatured?",
   choices=[
     "Its protein structure is disrupted and it loses the ability to catalyze reactions",
     "Its protein structure is unchanged but it becomes bound to its product",
     "It is converted into a nucleic acid with a new function",
     "It becomes able to act on a wider range of substrates than before",
     "It gains the ability to catalyze its reaction without an active site"],
   ans=0,
   why="EK 3.2.A.1.i states that denaturation of proteins such as enzymes occurs when the protein structure is disrupted, eliminating the ability to catalyze reactions. Loss of structure and loss of catalysis are the two halves of that sentence."),

 dict(q="Which set of environmental changes does the framework name as capable of denaturing a protein?",
   choices=[
     "A change in temperature, in pH, or in the chemical environment",
     "A change in the abundance of the substrate only",
     "A change in the number of ribosomes in the cell",
     "A change in how many products the reaction forms",
     "A change in the volume of the compartment the enzyme occupies"],
   ans=0,
   why="EK 3.2.A.1.i names exactly three: a change in temperature, pH, or chemical environment disrupts the protein structure. Substrate abundance affects efficiency under EK 3.2.B.1 but is not listed as a cause of denaturation."),

 dict(q="What does the framework identify as the bonds disrupted when temperature or pH moves outside an enzyme's optimal range?",
   choices=[
     "Hydrogen bonds",
     "Peptide bonds between adjacent amino acids",
     "The bonds joining nucleotides in a chromosome",
     "The bonds holding phospholipids in a bilayer",
     "The bonds between an enzyme and its allosteric inhibitor"],
   ans=0,
   why="EK 3.2.A.1.ii states in parentheses that the structural change is caused by disrupting the hydrogen bonds. The peptide backbone is not what the statement names."),

 dict(q="Raising the temperature of a reaction mixture from well below an enzyme's optimum toward that optimum increases the reaction rate. What accounts for the increase?",
   choices=[
     "Molecules move faster, so enzymes and substrates collide more frequently",
     "The enzyme's active site becomes larger as the solution warms",
     "The activation energy of the reaction falls as the solution warms",
     "The enzyme begins to catalyze several different reactions at once",
     "Product molecules are removed from the mixture as it warms"],
   ans=0,
   why="EK 3.2.B.2 states that higher environmental temperatures increase the average speed of movement of molecules in a solution, increasing the frequency of collisions between enzymes and substrates and therefore increasing the rate of reaction."),

 dict(q="Beyond an enzyme's optimal temperature, further warming lowers the reaction rate rather than raising it. Why does the trend reverse?",
   choices=[
     "Temperature outside the optimal range changes the enzyme's structure, so it catalyzes less efficiently",
     "Collisions between enzyme and substrate stop occurring above the optimum",
     "The substrate is converted to a different molecule above the optimum",
     "The enzyme starts binding product instead of substrate above the optimum",
     "The reaction runs backward above the optimum"],
   ans=0,
   why="EK 3.2.B.2 makes collision frequency rise only UNTIL the optimal temperature is achieved, and EK 3.2.A.1.ii says temperature outside the optimal range changes the enzyme's structure and alters the efficiency with which it catalyzes reactions. Beyond the optimum the second effect dominates."),

 dict(q="In some cases an enzyme that has been denatured can be returned to conditions in its optimal range and will work again. What does the framework say about this?",
   choices=[
     "Denaturation is reversible in some cases, allowing the enzyme to regain activity",
     "Denaturation is reversible in every case without exception",
     "Denaturation is never reversible under any conditions",
     "A denatured enzyme regains activity only if its substrate is also denatured",
     "A denatured enzyme regains activity only by being replaced with a new molecule"],
   ans=0,
   why="EK 3.2.A.2 states that in some cases enzyme denaturation is reversible, allowing the enzyme to regain activity. The qualifier is part of the statement, so neither the always nor the never reading is supported."),

 dict(q="Where does a competitive inhibitor bind, and how firmly?",
   choices=[
     "To the active site, and reversibly",
     "To an allosteric site, and reversibly",
     "To the active site, and permanently",
     "To an allosteric site, and permanently",
     "To the substrate rather than to the enzyme"],
   ans=0,
   why="EK 3.2.B.3 states that competitive inhibitor molecules can bind reversibly to the active site of the enzyme. Binding to an allosteric site is what the same statement assigns to noncompetitive inhibitors."),

 dict(q="Where does a noncompetitive inhibitor bind, and with what result?",
   choices=[
     "To an allosteric site, changing the activity of the enzyme",
     "To the active site, blocking substrate entry",
     "To the substrate, changing its shape",
     "To the product, preventing its release",
     "To the enzyme's gene, preventing its expression"],
   ans=0,
   why="EK 3.2.B.3 states that noncompetitive inhibitors can bind to allosteric sites, changing the activity of the enzyme. Occupying the active site is what the same statement assigns to competitive inhibitors."),

 dict(q="What is the key structural difference between how competitive and noncompetitive inhibitors act on an enzyme?",
   choices=[
     "One occupies the site the substrate must use, and the other binds a different site on the enzyme",
     "One binds the enzyme and the other binds the substrate",
     "One binds reversibly and the other cannot bind at all",
     "One acts only at high temperature and the other only at low temperature",
     "One is a protein and the other is a carbohydrate"],
   ans=0,
   why="EK 3.2.B.3 distinguishes them by binding location: the active site for competitive inhibitors and allosteric sites for noncompetitive inhibitors. Both bind the enzyme, so the site is the distinction."),

 dict(q="An enzyme is exposed to a competitive inhibitor, and then the substrate concentration in the mixture is raised sharply. What is the most reasonable prediction about the fraction of active sites occupied by substrate?",
   choices=[
     "It rises, because substrate and inhibitor compete for the same reversibly occupied site",
     "It falls, because more substrate attracts more inhibitor to the enzyme",
     "It is unchanged, because the inhibitor binds a site the substrate never uses",
     "It falls to zero, because a competitive inhibitor binds permanently",
     "It is unchanged, because relative concentrations do not affect an enzymatic reaction"],
   ans=0,
   why="EK 3.2.B.3 places the competitive inhibitor at the active site and describes its binding as reversible, and EK 3.2.B.1 makes the relative concentrations of substrates determine how efficiently the reaction proceeds. Two molecules reversibly contesting one site is decided by their relative amounts."),

 dict(q="According to the framework, what determines how efficiently an enzymatic reaction proceeds inside a cell, apart from conditions such as temperature and pH?",
   choices=[
     "The relative concentrations of the substrates and the products",
     "The total mass of the cell in which the reaction occurs",
     "The number of different enzymes the cell contains in total",
     "The distance between the enzyme and the plasma membrane",
     "The order in which the cell's organelles were assembled"],
   ans=0,
   why="EK 3.2.B.1 states that the relative concentrations of substrates and products determine how efficiently an enzymatic reaction proceeds. Cell mass, enzyme inventory and organelle order are not part of that statement."),

 dict(q="Product accumulates in a compartment where an enzymatic reaction is running and is not removed. What does the framework's account predict about the reaction?",
   choices=[
     "Its efficiency changes, because the relative concentrations of substrate and product have shifted",
     "Its efficiency is unaffected, because only substrate concentration matters",
     "The enzyme is denatured by the accumulated product",
     "The enzyme begins to act on a different substrate",
     "The activation energy of the reaction rises as product builds up"],
   ans=0,
   why="EK 3.2.B.1 makes the RELATIVE concentrations of substrates AND products the determinant of how efficiently the reaction proceeds, so a shift in the balance between them changes the efficiency without requiring any structural change to the enzyme."),

 dict(q="Reaction rates were measured for one enzyme across a range of temperatures, with the results shown. What is the optimal temperature for this enzyme, and how is it identified?",
   table=_T_TEMP,
   choices=[
     "The temperature at which the measured rate is highest",
     "The lowest temperature tested, because the enzyme is not yet damaged there",
     "The highest temperature tested, because molecules move fastest there",
     "The temperature at which the rate first begins to rise",
     "The temperature at which the rate has fallen to zero"],
   ans=0,
   why="EK 3.2.B.2 makes the rate rise with temperature only until the optimal temperature is achieved, so the optimum is the peak of the curve. In this table the rate rises to a single maximum and then falls."),

 dict(q="Using the same temperature series, which explanation best accounts for the behavior on each side of the peak?",
   table=_T_TEMP,
   choices=[
     "Below the peak, faster movement means more collisions; above it, the enzyme's structure is being changed",
     "Below the peak and above it, the same cause is at work in both directions",
     "Below the peak the enzyme is denatured and above it the enzyme recovers",
     "Below the peak the substrate is absent and above it the substrate returns",
     "The rise and the fall are both caused by changes in substrate concentration"],
   ans=0,
   why="EK 3.2.B.2 supplies the rising limb through collision frequency and EK 3.2.A.1.ii supplies the falling limb through structural change outside the optimal range. Two different mechanisms produce the two sides of one curve."),

 dict(q="Two enzymes were assayed across a range of pH values with the results shown. What do these data indicate?",
   table=_T_PH,
   choices=[
     "The two enzymes have different optimal pH values",
     "The two enzymes have the same optimal pH value",
     "Neither enzyme is affected by the pH of its surroundings",
     "Both enzymes work best at the highest pH tested",
     "Both enzymes work best at the lowest pH tested"],
   ans=0,
   why="Each enzyme peaks at a different pH in the table, which is EK 3.2.A.1.ii's statement that pH outside the optimal range FOR A GIVEN ENZYME alters its structure and efficiency; the range is a property of the particular enzyme."),

 dict(q="An enzyme was assayed at several substrate concentrations alone and in the presence of two different inhibitors, with the results shown. Which inhibitor behaves as a competitive inhibitor?",
   table=_T_INHIB,
   choices=[
     "Inhibitor L, because raising the substrate concentration nearly restores the uninhibited rate",
     "Inhibitor M, because raising the substrate concentration nearly restores the uninhibited rate",
     "Inhibitor L, because it reduces the rate by a constant number of micromoles per minute at every concentration",
     "Inhibitor M, because it reduces the rate to about half the uninhibited value at every concentration",
     "Neither inhibitor, because the two produce the same rate at every concentration tested"],
   ans=0,
   why="EK 3.2.B.3 puts the competitive inhibitor reversibly at the active site and EK 3.2.B.1 makes relative concentrations decide occupancy, so raising substrate should restore the rate. In the table one inhibited curve converges on the uninhibited one and the other does not."),

 dict(q="An enzyme with an optimal pH near two is moved into a compartment held near pH seven, with everything else unchanged. What is the most reasonable prediction?",
   choices=[
     "Its structure changes and it catalyzes its reaction less efficiently than before",
     "Its structure changes and it catalyzes its reaction more efficiently than before",
     "Its structure is unaffected, because pH acts only on substrates",
     "It begins to act as a competitive inhibitor of other enzymes",
     "It gains a second active site suited to the new pH"],
   ans=0,
   why="EK 3.2.A.1.ii states that pH outside the optimal range for a given enzyme causes changes to its structure by disrupting the hydrogen bonds, altering the efficiency with which it catalyzes reactions. Moving five pH units from the optimum is such a change."),

 dict(q="A chemical is added to a cell and an enzyme in that cell loses all catalytic activity, with no change in temperature or pH. Which explanation is consistent with the framework?",
   choices=[
     "The change in chemical environment disrupted the enzyme's structure",
     "A change in chemical environment cannot affect an enzyme's structure",
     "The enzyme was converted into its own substrate",
     "The chemical raised the enzyme's optimal temperature above the cell's temperature",
     "The chemical increased the number of active sites beyond what the enzyme can support"],
   ans=0,
   why="EK 3.2.A.1.i names the chemical environment alongside temperature and pH as a cause of denaturation, in which the protein structure is disrupted and the ability to catalyze reactions is eliminated."),

 dict(q="Three enzyme samples were treated as described and assayed during and after treatment, with the results shown. Which sample shows reversible denaturation?",
   table=_T_RECOVER,
   choices=[
     "The sample whose rate fell during treatment and returned to nearly its starting value afterward",
     "The sample whose rate was unchanged throughout the experiment",
     "The sample whose rate fell to zero and stayed at zero afterward",
     "Every sample, because denaturation is always reversible",
     "No sample, because denaturation is never reversible"],
   ans=0,
   why="EK 3.2.A.2 states that in some cases enzyme denaturation is reversible, allowing the enzyme to regain activity. The signature is a fall during the treatment followed by recovery afterward, which one sample in the table shows and the others do not."),

 dict(q="A student says that an enzyme working slowly at a low temperature has been denatured. What is the best correction?",
   choices=[
     "At a low temperature the molecules simply collide less often, which is not the same as a disrupted structure",
     "The student is right, because any departure from the optimum denatures an enzyme",
     "At a low temperature the enzyme has been converted to a different protein",
     "At a low temperature the substrate has been denatured instead of the enzyme",
     "At a low temperature the enzyme has bound an allosteric inhibitor"],
   ans=0,
   why="EK 3.2.B.2 attributes a low rate at low temperature to reduced collision frequency between enzymes and substrates, while EK 3.2.A.1.i reserves denaturation for a disruption of protein structure that eliminates catalysis. Slow is not the same as denatured."),

 dict(q="Which observation would distinguish an enzyme that is merely slowed by cold from one that has been denatured by heat?",
   choices=[
     "Whether activity returns when the sample is brought back to the optimal temperature",
     "Whether the enzyme is a protein",
     "Whether the substrate is present in the mixture",
     "Whether the reaction has an activation energy",
     "Whether the enzyme is found inside a membrane-bound compartment"],
   ans=0,
   why="EK 3.2.A.1.i makes denaturation the elimination of catalytic ability through structural disruption, and EK 3.2.A.2 allows recovery only in some cases. Restoring the optimal conditions and re-assaying is the observation that separates a slowed enzyme from a destroyed one."),

 dict(q="The framework says a change to the molecular structure of a COMPONENT in an enzymatic system may change its function or efficiency. Which change fits that description besides a change to the enzyme itself?",
   choices=[
     "A change to the structure of the substrate the enzyme acts on",
     "A change to the temperature at which the reaction is run",
     "A change to the volume of the reaction mixture",
     "A change to how long the reaction is allowed to proceed",
     "A change to the number of times the mixture is stirred"],
   ans=0,
   why="EK 3.2.A.1 refers to a component in an enzymatic system rather than to the enzyme alone, and the substrate is such a component. Temperature, volume, duration and stirring are conditions rather than molecular structures."),

 dict(q="An organism living in a hot spring has enzymes that function at temperatures which would inactivate the same enzymes from a mammal. What does the framework's language accommodate here?",
   choices=[
     "The optimal range is specified for a given enzyme, so different enzymes have different ranges",
     "Every enzyme in every organism has the same optimal temperature",
     "Denaturation occurs at exactly the same temperature for every protein",
     "Hot-spring organisms have no enzymes and rely on uncatalyzed reactions",
     "Temperature has no effect on enzymes in any organism"],
   ans=0,
   why="EK 3.2.A.1.ii is written as temperatures outside the optimal range FOR A GIVEN ENZYME, which makes the range a property of the individual enzyme rather than a single universal value."),

 dict(q="A noncompetitive inhibitor is added to a reaction mixture and the substrate concentration is then raised sharply. What is the most reasonable prediction?",
   choices=[
     "The inhibition largely persists, because the inhibitor is not occupying the site the substrate uses",
     "The inhibition disappears entirely, because substrate always displaces any inhibitor",
     "The inhibitor is converted into substrate as concentrations rise",
     "The enzyme is denatured by the extra substrate",
     "The reaction rate falls to zero as substrate is added"],
   ans=0,
   why="EK 3.2.B.3 places noncompetitive inhibitors at allosteric sites rather than at the active site, so raising the substrate does not contest the inhibitor's binding. The change in activity that the allosteric binding produces remains."),

 dict(q="Which statement about enzymes and their environment is NOT supported by the framework?",
   choices=[
     "An enzyme held far outside its optimal pH will catalyze its reaction more efficiently",
     "Denaturation can be caused by a change in the chemical environment",
     "Higher temperature increases the frequency of enzyme and substrate collisions",
     "A competitive inhibitor binds reversibly to the active site",
     "Relative concentrations of substrate and product affect how efficiently a reaction proceeds"],
   ans=0,
   why="EK 3.2.A.1.ii says conditions outside the optimal range alter the efficiency by disrupting the enzyme's structure, and EK 3.2.A.1.i says severe disruption eliminates catalysis; neither supports an increase. The other four restate EK 3.2.A.1.i, EK 3.2.B.2, EK 3.2.B.3 and EK 3.2.B.1."),

 dict(q="A cell responds to a signal by producing a molecule that binds an allosteric site on a metabolic enzyme. What is the framework's account of the consequence?",
   choices=[
     "The activity of that enzyme changes without the molecule ever entering the active site",
     "The enzyme is permanently denatured by the binding event",
     "The enzyme's substrate is converted into the binding molecule",
     "The enzyme's optimal temperature shifts to match the cell's temperature",
     "The enzyme loses its identity as a protein"],
   ans=0,
   why="EK 3.2.B.3 states that noncompetitive inhibitors can bind to allosteric sites, changing the activity of the enzyme. A change in activity through a site other than the active site is precisely what the statement describes."),

 dict(q="Using the pH results for the two enzymes, which claim about enzyme K is supported?",
   table=_T_PH,
   choices=[
     "Its rate rises to a maximum and then falls as pH continues to increase",
     "Its rate falls steadily across the whole range of pH tested",
     "Its rate is highest at the lowest pH tested",
     "Its rate is unchanged across the whole range of pH tested",
     "Its rate is identical to that of enzyme J at every pH tested"],
   ans=0,
   why="Skill 4.B asks students to describe trends in data. Enzyme K's column rises to a single maximum and then declines, which is the shape EK 3.2.A.1.ii predicts on either side of an optimal range."),

 dict(q="An investigator wants to justify the claim that a substance is acting as a noncompetitive inhibitor rather than a competitive one. Which evidence would justify that claim?",
   choices=[
     "Raising the substrate concentration fails to restore the uninhibited reaction rate",
     "The substance lowers the reaction rate at a single substrate concentration",
     "The substance is a smaller molecule than the substrate",
     "The substance is present in the cell at low concentration",
     "The reaction still has an activation energy when the substance is present"],
   ans=0,
   why="Skill 6.C asks for reasoning that connects evidence to a claim. EK 3.2.B.3 separates the two inhibitor types by binding site, and only the substrate-competition test distinguishes them, since a substance that lowers the rate at one concentration could be either kind."),

 dict(q="An enzyme is briefly exposed to a temperature above its optimum and then returned to its optimal temperature, and activity is restored. Which statement best describes what occurred?",
   choices=[
     "The structural disruption was reversible, so catalytic activity was regained",
     "The enzyme was never affected by the raised temperature at all",
     "The enzyme was replaced by newly synthesized molecules within seconds",
     "The substrate rather than the enzyme was disrupted and then repaired",
     "The reaction proceeded without an enzyme during the exposure"],
   ans=0,
   why="EK 3.2.A.2 states that in some cases enzyme denaturation is reversible, allowing the enzyme to regain activity, and EK 3.2.A.1.ii supplies the disruption of hydrogen bonds that raised temperature produces."),

 dict(q="Summarizing the topic, which pair of factors does the framework treat as acting on the ENZYME'S STRUCTURE, and which as acting without changing it?",
   choices=[
     "Temperature and pH act on the structure; the relative concentrations of substrate and product act without changing it",
     "The relative concentrations of substrate and product act on the structure; temperature and pH act without changing it",
     "All four act on the structure in the same way",
     "None of the four has any effect on an enzymatic reaction",
     "Only the chemical environment has any effect on an enzymatic reaction"],
   ans=0,
   why="EK 3.2.A.1.i and EK 3.2.A.1.ii attribute structural change to temperature, pH and the chemical environment, while EK 3.2.B.1 makes the relative concentrations of substrate and product a matter of how efficiently the reaction proceeds rather than of the enzyme's structure."),
]
