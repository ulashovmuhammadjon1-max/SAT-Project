# AP BIOLOGY 7.2 Natural Selection
# CED effective Fall 2025, Unit 7 Natural Selection. Big idea 1 (Evolution).
# Learning objectives 7.2.A, describe the importance of phenotypic variation in
# a population, and 7.2.B, explain how variation in molecules within cells
# connects to the fitness of an organism. Suggested skill 1.B, explain
# biological concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   7.2.A.1  Natural selection acts on PHENOTYPIC VARIATIONS in populations.
#   7.2.A.2  Environments CHANGE and APPLY SELECTIVE PRESSURES to populations.
#   7.2.A.3  Some phenotypic variations can INCREASE OR DECREASE the fitness of
#            an organism IN PARTICULAR ENVIRONMENTS.
#   7.2.B.1  Variation in the NUMBER AND TYPES OF MOLECULES WITHIN CELLS can
#            provide populations a greater ability to survive and reproduce in
#            DIFFERENT ENVIRONMENTS.
#
# ON THE ILLUSTRATIVE EXAMPLES. The CED prints flowering time in relation to
# global climate change beside EK 7.2.A.2, and sickle cell anemia and DDT
# resistance in insects beside EK 7.2.A.3. Illustrative examples are teaching
# suggestions rather than assessable content, so no key here depends on knowing
# one. Two data items are built on the SHAPES two of those examples describe --
# a population's flowering date tracking an earlier spring, and survival of a
# treatment rising across generations of exposure -- without naming a species,
# a chemical or a disease.
#
# DIVISION OF LABOUR ACROSS 7.1 TO 7.4 is set out in the header of b7_1.py.
# 7.1 owns the causes and the definitions, including that fitness is measured by
# reproductive success and that fluctuating environments change the rate and
# direction of evolution. This topic owns the VARIATION selection acts on. The
# two topics both concern environments changing, and the asks are kept apart:
# 7.1 asks what a fluctuation does to the rate and direction of evolution, and
# 7.2 asks what a changed environment does to a population that already varies.
#
# DELIBERATE OMISSIONS. The effect of a population's overall GENETIC DIVERSITY
# on its risk of decline or extinction is EK 7.11.A.1 and is asked in b7_11; no
# key here makes a claim about extinction risk. Hardy-Weinberg is 7.5's and no
# allele frequency is computed here.
#
# ON FIGURES. No stem refers to a graph. Every data set is a table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("7.2", "Natural Selection", 7)

# Three variants of one trait, before and after a new pressure.
_T_PRESSURE = dict(
    headers=["Phenotypic variant", "Percent of the population before the pressure",
             "Percent of the population after ten generations of the pressure"],
    rows=[["Variant 1", "62", "14"],
          ["Variant 2", "30", "24"],
          ["Variant 3", "8", "62"]])

# Survival of a repeated treatment, measured in successive generations.
_T_RESIST = dict(
    headers=["Generation of exposure to the treatment",
             "Percent of the population surviving the treatment"],
    rows=[["Generation 1", "4"],
          ["Generation 5", "19"],
          ["Generation 10", "55"],
          ["Generation 15", "88"]])

# Spring onset and flowering date in one plant population, by decade.
_T_FLOWER = dict(
    headers=["Decade", "Mean day of the year on which spring temperatures arrived",
             "Mean day of the year on which the population flowered"],
    rows=[["First decade", "95", "118"],
          ["Second decade", "89", "113"],
          ["Third decade", "82", "106"],
          ["Fourth decade", "76", "99"]])

# Three forms of one enzyme, each assayed at two temperatures.
_T_ENZYME = dict(
    headers=["Form of the enzyme carried by an individual",
             "Activity at 10 degrees Celsius (arbitrary units)",
             "Activity at 35 degrees Celsius (arbitrary units)"],
    rows=[["Form X", "82", "11"],
          ["Form Y", "14", "79"],
          ["Form Z", "46", "44"]])

# Three phenotypes, each scored for offspring in three habitats.
_T_THREEENV = dict(
    headers=["Phenotype", "Mean offspring in the wet habitat",
             "Mean offspring in the dry habitat", "Mean offspring in the shaded habitat"],
    rows=[["Phenotype 1", "5.2", "1.1", "2.0"],
          ["Phenotype 2", "1.4", "4.9", "1.8"],
          ["Phenotype 3", "2.1", "2.0", "5.5"]])

# Two populations tested across the same four environments.
_T_MOLEC = dict(
    headers=["Population", "Number of different forms of the enzyme present in the population",
             "Number of the four test environments in which the population persisted"],
    rows=[["Population 1", "1", "1"],
          ["Population 2", "4", "4"]])

# One favoured variation followed while a pressure continues.
_T_OVERGEN = dict(
    headers=["Generation", "Percent of the population carrying the favored variation"],
    rows=[["Generation 1", "6"],
          ["Generation 3", "17"],
          ["Generation 5", "38"],
          ["Generation 7", "64"],
          ["Generation 9", "83"]])

QUESTIONS = [
 dict(q="On what does natural selection act, according to the framework?",
   choices=[
     "Phenotypic variations in populations",
     "The alleles of a single individual, which it edits directly",
     "The environment, which it changes to suit the population",
     "Traits an individual acquires during its own lifetime",
     "The genetic code, which it alters so that new proteins can be made"], ans=0,
   why="EK 7.2.A.1 states that natural selection acts on phenotypic variations in populations. It acts on what is observable and on differences among individuals rather than editing alleles directly, and the genetic code is shared across nearly all organisms under EK 6.4.A.3.iv."),
 dict(q="A population is completely uniform for a particular trait: every individual shows the identical phenotype. What does the framework imply about natural selection on that trait?",
   choices=[
     "There is no phenotypic variation for selection to act on with respect to that trait",
     "Selection will create the variation it needs and then act on it",
     "Selection will act more strongly, because uniformity makes differences easier to detect",
     "Selection will act on the environment instead until variation appears",
     "Selection will act on the trait in the same way as in a varying population"], ans=0,
   why="EK 7.2.A.1 states that natural selection acts on phenotypic variations in populations, so variation is what selection requires as its material. New variation comes from mutation under EK 6.7.B.1.ii rather than from selection itself."),
 dict(q="What does the framework say environments do to populations?",
   choices=[
     "They change and apply selective pressures to populations",
     "They remain constant, which is what allows selection to proceed",
     "They supply the new phenotypic variations that selection then acts on",
     "They change the genetic code that a population uses",
     "They act on individuals but not on populations"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations. Both clauses are the framework's: environments are not constant, and what they do to a population is apply a pressure rather than supply new variation."),
 dict(q="What does the framework say some phenotypic variations can do?",
   choices=[
     "Increase or decrease the fitness of an organism in particular environments",
     "Increase the fitness of an organism in every environment it lives in",
     "Decrease the fitness of an organism in every environment it lives in",
     "Change the environment so that the organism's fitness rises",
     "Determine an organism's fitness independently of its environment"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism in particular environments. Both directions are named, and the qualifier IN PARTICULAR ENVIRONMENTS is what prevents the effect from being read as a property of the variation alone."),
 dict(q="Why does the framework attach the words in particular environments to its statement about phenotypic variations and fitness?",
   choices=[
     "Because the same variation can raise fitness under one set of conditions and lower it under another",
     "Because a variation affects fitness only in the environment where it first arose",
     "Because a variation affects fitness only in environments that are not changing",
     "Because fitness cannot be measured outside a laboratory environment",
     "Because each variation is found in only one environment"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism in particular environments, and EK 7.2.A.2 states that environments change. Taken together the effect on fitness is relative to conditions, which is why the same variation can act in either direction."),
 dict(q="Three variants of one trait were measured before a new pressure was applied and again ten generations later, as reported in the table. Which variant increased in fitness under this pressure?",
   table=_T_PRESSURE,
   choices=[
     "Variant 3, which rose from a small minority of the population to a majority",
     "Variant 1, which was the most common variant before the pressure was applied",
     "Variant 2, which changed the least of the three",
     "All three variants equally, since all three were present before and after",
     "None of them, since the percentages must always sum to one hundred"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism in particular environments, and a variation whose bearers leave more offspring becomes more common. One variant rises from 8 to 62 percent while the other two fall, so the pressure favoured that one."),
 dict(q="A population was treated repeatedly and the proportion surviving each treatment was recorded, as reported in the table. Which explanation of the trend is consistent with the framework?",
   table=_T_RESIST,
   choices=[
     "The treatment applied a selective pressure, and individuals already carrying a variation that survives it left more offspring in each generation",
     "The treatment caused the individuals that needed it to develop a variation that survives it",
     "The individuals became used to the treatment during their own lifetimes and passed that on",
     "The treatment removed the selective pressure, which is why survival rose",
     "The rise happened by chance, since a treatment cannot affect which individuals reproduce"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations, and EK 7.2.A.1 has selection act on phenotypic variations already present. Survival rises from 4 to 88 percent across fifteen generations, which is the pressure sorting existing variation; EK 6.7.B.1 makes mutations random rather than produced on demand."),
 dict(q="The table reports, by decade, the day of the year on which spring temperatures arrived and the day on which one plant population flowered. What do these data show?",
   table=_T_FLOWER,
   choices=[
     "The population's flowering date moved earlier as the arrival of spring moved earlier",
     "The population's flowering date moved later as the arrival of spring moved earlier",
     "The population's flowering date did not change across the four decades",
     "The arrival of spring did not change across the four decades",
     "The population flowered before spring temperatures arrived in every decade"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations. Across the four decades the arrival of spring moves from day 95 to day 76 and flowering moves from day 118 to day 99, so both move earlier together and flowering follows spring rather than preceding it."),
 dict(q="What does the framework say variation in the number and types of molecules within cells can provide?",
   choices=[
     "A greater ability for populations to survive and reproduce in different environments",
     "A greater ability for individuals to change their own molecules when conditions change",
     "A guarantee that every individual will survive whatever the environment",
     "A means by which populations change the environments they live in",
     "A reduction in the variation available for natural selection to act on"], ans=0,
   why="EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments. The claim is about a population's ability across a range of environments, not a guarantee for any individual."),
 dict(q="Three forms of one enzyme found in a population were assayed at two temperatures, with the results in the table. What advantage does a population containing all three forms have?",
   table=_T_ENZYME,
   choices=[
     "Some individuals retain high enzyme activity at the cold temperature and others at the warm one, so the population can function across both",
     "Every individual retains high enzyme activity at both temperatures, so no individual is disadvantaged",
     "The population has no advantage, since one form is always better than the others",
     "The population can change which form each individual carries when the temperature changes",
     "The population can change the temperature of its environment to suit whichever form is present"], ans=0,
   why="EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments. In the table the first form is far more active in the cold and the second far more active in the warm, so no single form covers both and the coverage comes from the population containing more than one."),
 dict(q="Three phenotypes were scored for mean offspring in three habitats, as reported in the table. Which phenotype has the greatest fitness in the dry habitat?",
   table=_T_THREEENV,
   choices=[
     "Phenotype 2, which leaves the most offspring in that habitat",
     "Phenotype 1, which leaves the most offspring in the wet habitat",
     "Phenotype 3, which leaves the most offspring in the shaded habitat",
     "All three equally, since all three leave some offspring in the dry habitat",
     "None of them, since fitness cannot be compared between habitats"], ans=0,
   why="EK 7.1.B.1 measures evolutionary fitness by reproductive success and EK 7.2.A.3 makes the effect of a variation specific to particular environments, so the comparison must be made within one habitat. In the dry column the three means are 1.1, 4.9 and 2.0, and the largest belongs to the second phenotype even though a different phenotype leads in each of the other habitats."),
 dict(q="Using the same three habitats, what does the pattern across all three columns illustrate?",
   table=_T_THREEENV,
   choices=[
     "Each phenotype leaves the most offspring in a different habitat, so no phenotype is fittest everywhere",
     "One phenotype leaves the most offspring in every habitat, so that phenotype is fittest everywhere",
     "The three phenotypes leave the same number of offspring in every habitat",
     "Fitness depends only on the phenotype and not at all on the habitat",
     "The habitat determines the phenotype each individual develops"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism in particular environments. Reading down each column, the largest mean belongs to a different phenotype in each of the three habitats, which is exactly the qualifier the statement attaches."),
 dict(q="A population is moved from its original habitat to a new one in which conditions differ. Which framework statement predicts what will happen to its composition?",
   choices=[
     "Environments apply selective pressures to populations, and variations that raise fitness in the new conditions become more common",
     "Environments supply new variations to populations, and those new variations become common",
     "Environments act on individuals only, so the composition of the population is unchanged",
     "Environments determine the genotype of each individual directly",
     "Environments have no effect until the population has been present for many generations"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations, and EK 7.2.A.3 makes the effect of a variation on fitness specific to particular environments. Selection acts on the variation already present under EK 7.2.A.1; the environment does not supply new variation."),
 dict(q="Which of the following is a selective pressure in the framework's sense?",
   choices=[
     "A change in the environment that causes individuals with some phenotypes to leave more offspring than others",
     "A change in the environment that affects every individual of a population identically",
     "A change in an individual's phenotype during its own lifetime",
     "A change in the genetic code used by a population",
     "A change in the number of chromosomes an individual carries"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations, and EK 7.2.A.3 has phenotypic variations increase or decrease fitness in particular environments. A pressure that fell identically on every individual would produce no difference in reproductive success and so would not sort the variation."),
 dict(q="Natural selection acts on phenotypic variations, but what is passed to the next generation is not the phenotype itself. What is passed on?",
   choices=[
     "The alleles that the surviving individuals inherited and transmit to their offspring",
     "The phenotype exactly as the parent displayed it, including any change during its life",
     "The selective pressure the parent experienced",
     "The environment in which the parent lived",
     "Nothing, since each generation begins with a new set of variations"], ans=0,
   why="EK 7.2.A.1 has selection act on phenotypic variations, and EK 5.3.A.2.iii makes the set of alleles what an organism inherits, with EK 5.3.A.2.iv making the phenotype the observable expression of those inherited traits. EK 7.1.A.2 has favourable traits passed on to subsequent generations through reproduction."),
 dict(q="The proportion of a population carrying one favored variation was recorded over nine generations of continued pressure, as reported in the table. What do the data show?",
   table=_T_OVERGEN,
   choices=[
     "The favored variation became steadily more common while the pressure continued",
     "The favored variation became steadily less common while the pressure continued",
     "The favored variation stayed at the same frequency throughout",
     "The favored variation disappeared and then reappeared during the nine generations",
     "The favored variation was already present in every individual at the first generation"], ans=0,
   why="EK 7.2.A.2 has environments apply selective pressures to populations and EK 7.2.A.3 has some variations increase fitness in particular environments. The recorded percentages rise at every step from 6 to 83, and the first value shows the variation was present in only a small minority to begin with."),
 dict(q="Two populations were tested across the same four environments, with the results in the table. Which claim do these data support?",
   table=_T_MOLEC,
   choices=[
     "The population containing more different forms of the enzyme persisted in more of the environments",
     "The population containing fewer different forms of the enzyme persisted in more of the environments",
     "The number of forms of the enzyme made no difference to the number of environments a population persisted in",
     "Both populations persisted in all four environments, so no comparison can be made",
     "The population containing more forms of the enzyme changed the environments to suit itself"], ans=0,
   why="EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments. One population carries one form and persisted in one environment while the other carries four and persisted in four, which is that claim in data."),
 dict(q="A student says that natural selection creates the variations that make organisms better suited to their environments. How should this be corrected?",
   choices=[
     "Selection acts on phenotypic variations already present in the population; new variation arises by mutation",
     "Selection does create those variations, so the student is correct",
     "Selection removes all variation from a population, so no variation remains for it to act on",
     "Selection acts only on variations that appeared during the lifetime of the individuals concerned",
     "Selection acts on the environment rather than on the population"], ans=0,
   why="EK 7.2.A.1 states that natural selection acts on phenotypic variations in populations, which presupposes that the variation is there. EK 6.7.B.1 makes mutations the random source of new variation and EK 6.7.B.1.ii calls mutations a source of genetic variation."),
 dict(q="A phenotypic variation is common in a population living in one habitat and rare in a population of the same species living in another. Which framework statement best accounts for the difference?",
   choices=[
     "Some phenotypic variations can increase or decrease the fitness of an organism in particular environments",
     "Phenotypic variations arise only in the habitats where they are useful",
     "Natural selection acts on the environment rather than on the population",
     "Variation in the number and types of molecules within cells removes phenotypic differences between habitats",
     "Populations of one species must have the same composition wherever they live"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism in particular environments, so the same variation can be favoured in one habitat and not in another. Mutations arise randomly under EK 6.7.B.1 rather than where they would be useful."),
 dict(q="What is the difference between phenotypic variation and environmental variation, in the framework's account?",
   choices=[
     "Phenotypic variation is differences among the individuals of a population; environmental variation is differences in the conditions those individuals experience",
     "Phenotypic variation is differences in the conditions; environmental variation is differences among individuals",
     "The two are the same thing, since a phenotype is a feature of the environment",
     "Phenotypic variation applies to populations and environmental variation to species",
     "Phenotypic variation exists only where the environment does not vary"], ans=0,
   why="EK 7.2.A.1 locates the variation selection acts on among the individuals of a population, and EK 7.2.A.2 makes the environment the thing that changes and applies a pressure to them. The two are the two sides of the process the framework describes."),
 dict(q="Why does the framework describe variation in the number and types of molecules within cells as providing an ability to survive and reproduce in different environments, rather than in one environment?",
   choices=[
     "Because different molecular variants suit different conditions, so a population carrying several is covered across a range of conditions",
     "Because a single molecular variant works equally well in every condition",
     "Because molecular variation prevents the environment from changing",
     "Because molecular variation guarantees the survival of every individual in every condition",
     "Because a population carrying several variants can discard the ones it does not need"], ans=0,
   why="EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in DIFFERENT environments. The plural is the point: the advantage is coverage across conditions, not a guarantee within any one of them."),
 dict(q="A researcher wants to show that a particular environmental change is applying a selective pressure to a population. Which observation would support that claim?",
   choices=[
     "Individuals with one phenotype leave more offspring than individuals with another after the change, and the proportions in the population shift accordingly",
     "Every individual in the population is affected by the change to the same degree",
     "The population contains no variation for the trait concerned",
     "The change occurred too recently for any generation to have passed",
     "The individuals alter their own phenotypes in response to the change"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations, and EK 7.2.A.3 makes the pressure's effect a difference in fitness between variations. A pressure falling equally on every individual sorts nothing, and an individual altering its own phenotype is the plasticity of EK 5.5.A.1."),
 dict(q="A phenotypic variation decreases an organism's fitness in the environment its population currently occupies. What does the framework predict for that variation?",
   choices=[
     "Individuals carrying it leave fewer offspring, so it becomes less common in that environment",
     "Individuals carrying it leave more offspring, so it becomes more common in that environment",
     "It disappears from the population within a single generation",
     "It is removed from the individuals carrying it during their lifetimes",
     "It becomes less common in every environment, whatever the conditions"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism in particular environments, and EK 7.1.B.1 measures fitness by reproductive success. A variation whose bearers leave fewer offspring becomes less common, but the qualifier confines the prediction to that environment."),
 dict(q="A variation is present in only a small fraction of a population when a new selective pressure begins. What does the framework allow to be predicted?",
   choices=[
     "If the variation raises fitness under the new pressure, its frequency can rise over generations even from a small starting fraction",
     "The variation cannot spread, because a small starting fraction cannot increase",
     "The variation will spread within one generation to the whole population",
     "The variation will be created anew in the individuals that lack it",
     "The variation's frequency is fixed, since selection acts only on common variations"], ans=0,
   why="EK 7.2.A.1 has selection act on the phenotypic variations present and EK 7.2.A.3 makes some of them increase fitness in particular environments. Nothing in the framework restricts selection to common variations, and the change accumulates across generations under EK 7.1.A.2 rather than within one."),
 dict(q="Why does the framework speak of selection acting on variations in POPULATIONS rather than in individuals?",
   choices=[
     "An individual has one phenotype, so a difference between phenotypes exists only among the individuals of a population",
     "Individuals do not have phenotypes, which are properties of populations only",
     "Selection acts on populations of different species rather than within one species",
     "Individuals cannot reproduce, so only populations can pass traits on",
     "A population has a single phenotype that selection acts on directly"], ans=0,
   why="EK 7.2.A.1 states that natural selection acts on phenotypic variations in populations. EK 5.3.A.2.iv makes the phenotype an individual's observable expression, so a variation is a difference between individuals and exists only where more than one is present."),
 dict(q="An investigator observes that a trait's distribution in a population has shifted over twenty generations while the habitat was changing. Which framework statement most directly connects the two observations?",
   choices=[
     "Environments change and apply selective pressures to populations",
     "Natural selection is a major mechanism of evolution",
     "Evolutionary fitness is measured by reproductive success",
     "Variation in the number and types of molecules within cells provides an ability to survive in different environments",
     "The genetic code is shared by nearly all living organisms"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations, which is the statement joining a changing habitat to a change in a population. The other statements are true of the framework but concern the status of selection, the measure of fitness, molecular variation and the code."),
 dict(q="A population contains several forms of a transport protein, each working best under a different salt concentration. How does this connect to the fitness of the organisms, in the framework's terms?",
   choices=[
     "Variation in the types of molecules within their cells gives the population a greater ability to survive and reproduce across different salt concentrations",
     "Variation in the types of molecules within their cells removes the differences in fitness among the individuals",
     "Variation in the types of molecules within their cells allows each individual to switch between forms as the salt concentration changes",
     "Variation in the types of molecules within their cells changes the salt concentration of the environment",
     "Variation in the types of molecules within their cells has no connection to fitness"], ans=0,
   why="EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments, which is the connection the question asks for. The statement concerns the population's coverage of a range of conditions rather than an individual switching between forms."),
 dict(q="Which pair of framework statements together explains why a population that varies can persist through an environmental change that a uniform population could not?",
   choices=[
     "That natural selection acts on phenotypic variations in populations, and that some variations increase fitness in particular environments",
     "That environments never change, and that selection therefore acts in one direction",
     "That selection creates new variations, and that those variations suit the new environment",
     "That fitness is measured by lifespan, and that longer-lived individuals survive change",
     "That the genetic code is shared, and that all organisms therefore respond alike"], ans=0,
   why="EK 7.2.A.1 makes phenotypic variation what selection acts on and EK 7.2.A.3 makes some variations raise fitness in particular environments, so a varying population can contain individuals suited to the new conditions. EK 7.2.A.2 supplies the change itself, and EK 6.7.B.1 rather than selection supplies new variation."),
 dict(q="A student claims that because a phenotypic variation raises fitness in a population's current habitat, it must raise fitness in every habitat that species occupies. How should this be corrected?",
   choices=[
     "The framework says such effects hold in particular environments, so the same variation may lower fitness elsewhere",
     "The framework says such effects hold in every environment, so the student is correct",
     "The framework says such effects hold only where the environment is not changing",
     "The framework says fitness cannot be compared between habitats at all",
     "The framework says a variation's effect on fitness is fixed by its molecular form alone"], ans=0,
   why="EK 7.2.A.3 states that some phenotypic variations can increase or decrease the fitness of an organism IN PARTICULAR ENVIRONMENTS, which is exactly the qualifier the claim drops. EK 7.2.A.2 adds that environments change, so the conditions under which a variation was measured need not persist."),
 dict(q="Which account of a population changing under a new selective pressure is consistent with everything the framework states in this topic?",
   choices=[
     "The population already varied; the changed environment applied a pressure; variations that raised fitness under the new conditions became more common over generations",
     "The changed environment created new variations in the individuals that needed them, and those individuals then reproduced",
     "The individuals altered their own phenotypes to suit the new conditions and passed those alterations on",
     "The population was uniform, and selection produced variation from that uniformity",
     "The population changed the environment back to its original state, so no variation was needed"], ans=0,
   why="Each clause of the keyed option is one of the framework's statements: EK 7.2.A.1 for selection acting on the phenotypic variation present, EK 7.2.A.2 for the environment changing and applying a pressure, and EK 7.2.A.3 for some variations raising fitness in those particular conditions. Each rejected account has the environment or the individual supply the variation, which EK 6.7.B.1 assigns to random mutation."),
]
