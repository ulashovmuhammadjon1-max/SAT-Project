# AP BIOLOGY 5.5 Environmental Effects on Phenotype
# CED effective Fall 2025, Unit 5 Heredity. Big idea 4 (Systems Interactions).
# Learning objective 5.5.A, explain how the same genotype can result in multiple
# phenotypes under different environmental conditions. Suggested skill 1.C,
# explain biological concepts and processes in APPLIED CONTEXTS.
#
# Essential knowledge relied on, in the framework's own words:
#   5.5.A.1  Environmental conditions influence gene expression and can lead to
#            phenotypic plasticity (e.g., the ability of individual genotypes to
#            produce different phenotypes).
#
# Illustrative examples the CED prints with EK 5.5.A.1, which are the content
# universe of this topic:
#     - height and weight in humans
#     - flower color based on soil pH
#     - seasonal fur color in arctic animals
#     - sex determination in reptiles
#     - effect of increased UV on melanin production in animals
#     - presence of the opposite mating type on pheromone production in yeast
#       and other fungi
#
# ON A ONE-STATEMENT TOPIC. This topic has a single essential knowledge
# statement, the situation SOCIAL_DEDUPE.md records for US Government 4.7, where
# thirty questions against one sentence pushed an author into a neighbouring
# topic's material. The answer used there was to CHAIN the statement to another
# topic's rather than to reach for new content, and the same answer is used here:
# the suggested skill is 1.C, explain concepts in applied contexts, so most items
# put real data in a table and ask what the data show about one genotype in more
# than one environment. Eight items chain EK 5.5.A.1 to EK 5.3.A.2.iii and
# EK 5.3.A.2.iv -- the genotype is the set of alleles inherited and the phenotype
# is the observable expression -- which is a question neither topic can ask
# alone, since 5.3 names no environment and 5.5 defines neither term.
#
# ON FIGURES. No stem refers to a picture. Every data set is in a table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX. Numeric
# ranges are written "from 26 to 34 degrees", never with a hyphen.
TOPIC = ("5.5", "Environmental Effects on Phenotype", 5)

# Cuttings of ONE hydrangea plant, rooted in pots of different soil pH.
_T_PH = dict(
    headers=["Soil pH of the pot", "Flower color of the cutting"],
    rows=[["4.5", "Blue"],
          ["5.5", "Blue"],
          ["6.5", "Purple"],
          ["7.0", "Pink"],
          ["7.5", "Pink"]])

# The same single plant, repotted between seasons.
_T_PHTIME = dict(
    headers=["Season", "Soil pH of the pot", "Flower color that season"],
    rows=[["First season", "5.0", "Blue"],
          ["Second season", "7.2", "Pink"],
          ["Third season", "5.0", "Blue"]])

# Arctic hares from one inbred line, held at different day lengths.
_T_HARE = dict(
    headers=["Hours of light per day", "Percent of hares with a white coat"],
    rows=[["8", "96"],
          ["10", "72"],
          ["12", "30"],
          ["14", "4"]])

# Eggs from one clutch, split among incubators.
_T_REPTILE = dict(
    headers=["Incubation temperature (degrees Celsius)",
             "Percent of hatchlings that are female"],
    rows=[["26", "4"],
          ["28", "22"],
          ["30", "55"],
          ["32", "88"],
          ["34", "97"]])

# Melanin content of skin samples after four weeks at fixed daily UV doses.
_T_UV = dict(
    headers=["Daily UV exposure (arbitrary units)",
             "Mean melanin content of skin samples (arbitrary units)"],
    rows=[["0", "12"],
          ["2", "20"],
          ["4", "29"],
          ["6", "38"],
          ["8", "48"]])

# Yeast cultures of one strain, grown alone and with the opposite mating type.
_T_YEAST = dict(
    headers=["Culture condition",
             "Pheromone produced (nanograms per million cells)"],
    rows=[["Mating type a cells grown alone", "2"],
          ["Mating type alpha cells grown alone", "3"],
          ["Mating type a and mating type alpha cells grown together", "41"]])

# Mean adult height in one population across four decades of improving diet.
_T_HEIGHT = dict(
    headers=["Decade", "Mean adult height in the population (centimeters)"],
    rows=[["1920s", "165"],
          ["1950s", "171"],
          ["1980s", "176"],
          ["2010s", "179"]])

# Two genetically distinct plant lines, each grown at two temperatures.
_T_NORM = dict(
    headers=["Plant line", "Mean height at 18 degrees Celsius (centimeters)",
             "Mean height at 28 degrees Celsius (centimeters)"],
    rows=[["Line 1", "30", "52"],
          ["Line 2", "44", "46"]])

# Cuttings of one plant, half in shade and half in full sun, four replicates.
_T_MEAN = dict(
    headers=["Replicate", "Leaf area in shade (square centimeters)",
             "Leaf area in full sun (square centimeters)"],
    rows=[["1", "48", "26"],
          ["2", "52", "30"],
          ["3", "50", "28"],
          ["4", "54", "32"]])

QUESTIONS = [
 dict(q="A gardener takes many cuttings from a single plant and grows them at several altitudes. The cuttings differ in height, leaf thickness and flowering date. What does this result illustrate?",
   choices=[
     "Phenotypic plasticity, the ability of one genotype to produce different phenotypes under different conditions",
     "Natural selection, because the conditions at each altitude favored different individuals",
     "Mutation, because a new set of alleles arose in the cuttings grown at each altitude",
     "Independent assortment, because the traits appeared in new combinations at each altitude",
     "Codominance, because more than one version of each trait was expressed in the group"], ans=0,
   why="EK 5.5.A.1 states that environmental conditions influence gene expression and can lead to phenotypic plasticity, which the framework glosses as the ability of individual genotypes to produce different phenotypes. Cuttings from one plant share a genotype, so the differences among them cannot be differences in alleles."),
 dict(q="Cuttings from one hydrangea plant were rooted in pots of soil differing only in pH, and the flowers were scored the following summer. Which conclusion do these data support?",
   table=_T_PH,
   choices=[
     "One genotype produced more than one flower color, because the soil pH differed among the pots",
     "The cuttings differed in the alleles they carried for flower color, because their flowers differed",
     "Soil pH selected the cuttings with alleles for blue flowers and removed the others",
     "Flower color is determined by soil pH and not by any gene of the plant",
     "The cuttings with pink flowers had mutated in response to the alkaline soil"], ans=0,
   why="Flower color based on soil pH is one of the illustrative examples the CED prints with EK 5.5.A.1. Every cutting came from one plant and therefore carries one genotype, so the only variable across the pots is the environment; the low-pH pots gave blue flowers and the high-pH pots pink ones. A phenotype still requires genes to produce the pigment, so the environment influences the expression rather than replacing the genotype."),
 dict(q="Hares from a single inbred line were housed at four day lengths and their coats were scored in midwinter. Which statement is best supported by the data in the table?",
   table=_T_HARE,
   choices=[
     "The proportion of hares with a white coat falls steadily as the hours of light per day increase",
     "The proportion of hares with a white coat rises steadily as the hours of light per day increase",
     "Day length has no measurable effect on coat color in these hares",
     "The hares at each day length must carry different alleles for coat color",
     "Coat color is fixed at birth, so the day length recorded here is a coincidence"], ans=0,
   why="Seasonal fur color in arctic animals is one of the illustrative examples the CED prints with EK 5.5.A.1. The four values fall from 96 percent to 4 percent as light rises from 8 to 14 hours, which is a steady decline; and because the hares are one inbred line, the differences among the groups cannot be differences in alleles."),
 dict(q="Eggs from a single clutch of a reptile were divided among five incubators held at different temperatures, and the hatchlings were sexed. Which incubation temperature in the table gives the sex ratio closest to equal numbers of females and males?",
   table=_T_REPTILE,
   choices=[
     "30 degrees Celsius",
     "26 degrees Celsius",
     "28 degrees Celsius",
     "32 degrees Celsius",
     "34 degrees Celsius"], ans=0,
   why="Sex determination in reptiles is one of the illustrative examples the CED prints with EK 5.5.A.1. An equal sex ratio is 50 percent female, and the five recorded percentages are 4, 22, 55, 88 and 97; the value nearest 50 is 55, recorded at the middle temperature."),
 dict(q="Skin samples from genetically identical laboratory animals were exposed to five daily doses of ultraviolet light for four weeks. About how many times as much melanin did the samples at the highest dose contain compared with the samples receiving no ultraviolet light?",
   table=_T_UV,
   choices=[
     "About four times as much",
     "About twice as much",
     "About eight times as much",
     "About the same amount",
     "About half as much"], ans=0,
   why="The effect of increased ultraviolet light on melanin production in animals is one of the illustrative examples the CED prints with EK 5.5.A.1. The mean melanin content rises from 12 units with no exposure to 48 units at the highest dose, and 48 divided by 12 is 4."),
 dict(q="A single strain of yeast was grown in three ways and the amount of pheromone released was measured. What do the data in the table show about the conditions under which this strain produces pheromone?",
   table=_T_YEAST,
   choices=[
     "Pheromone production rises sharply only when cells of the opposite mating type are present",
     "Pheromone production is the same whichever cells are present, so the culture condition does not matter",
     "Pheromone production is highest when each mating type is grown by itself",
     "Only one of the two mating types is capable of producing any pheromone at all",
     "Pheromone production falls when the two mating types are grown together"], ans=0,
   why="The presence of the opposite mating type affecting pheromone production in yeast and other fungi is one of the illustrative examples the CED prints with EK 5.5.A.1. Each mating type alone releases 2 or 3 nanograms per million cells, while the mixed culture releases 41, so the presence of the other cell type is the condition that turns production up."),
 dict(q="The table reports the mean adult height of one population across four decades during which nutrition improved markedly. Which explanation of the trend is best supported?",
   table=_T_HEIGHT,
   choices=[
     "Improved conditions during growth raised the height that the population's genotypes produced",
     "Alleles for greater height replaced alleles for shorter height in the population over these decades",
     "The people measured in the later decades were a different species from those measured earlier",
     "Height is not affected by the environment, so the four means must have been measured incorrectly",
     "Mutation raised the height of every individual in the population by the same amount each decade"], ans=0,
   why="Height and weight in humans is one of the illustrative examples the CED prints with EK 5.5.A.1, which states that environmental conditions influence gene expression. The mean rises 14 centimeters across about 90 years, roughly three generations, and the stem supplies a change in conditions during growth; nothing here reports a change in the alleles the population carries."),
 dict(q="Two plants of identical genotype are raised in different greenhouses and grow to very different sizes. Which statement about the two plants is correct?",
   choices=[
     "They have the same genotype and different phenotypes, because the observable expression depends on conditions as well as on alleles",
     "They have different genotypes, because a genotype is defined by the traits an organism actually shows",
     "They have the same phenotype, because phenotype refers to the alleles an organism inherited",
     "They have different genotypes and different phenotypes, since a change in size requires a change in alleles",
     "Neither term applies, because genotype and phenotype describe populations rather than individuals"], ans=0,
   why="EK 5.3.A.2.iii defines the genotype as the set of alleles inherited and EK 5.3.A.2.iv defines the phenotype as the observable expression of the inherited traits; EK 5.5.A.1 adds that environmental conditions influence gene expression. Size is observable and so belongs to the phenotype, while the inherited alleles are unchanged by the greenhouse."),
 dict(q="A researcher wants to test whether a plant species shows phenotypic plasticity for leaf shape. Which experimental design is best suited to the question?",
   choices=[
     "Grow cuttings taken from one parent plant under several different conditions and compare their leaves",
     "Grow seedlings from many different parent plants under one condition and compare their leaves",
     "Collect leaves from wild plants growing in several habitats and compare their shapes",
     "Compare the leaf shapes of two related species grown in the same greenhouse",
     "Sequence the leaf shape gene in plants from several habitats and compare the sequences"], ans=0,
   why="EK 5.5.A.1 defines phenotypic plasticity as the ability of individual genotypes to produce different phenotypes, so the genotype has to be held constant while the environment varies. Cuttings from one parent share a genotype; seedlings from many parents and wild plants from several habitats both confound genotype with environment, and comparing two species changes the genotype deliberately."),
 dict(q="An arctic animal's coat turns white in winter and brown in summer, year after year. Why is this change not described as a mutation?",
   choices=[
     "The DNA sequence of the animal is unchanged; what changes is which genes are expressed and how strongly",
     "The change is too small to count as a mutation, since only one trait is affected",
     "Mutations occur only in gametes, and coat color is a trait of the body",
     "The change reverses each year, and a mutation must occur in every cell to be detected",
     "Mutations affect only traits that are inherited, and coat color is not inherited"], ans=0,
   why="EK 5.5.A.1 locates the effect in gene expression: environmental conditions influence gene expression and can lead to phenotypic plasticity. A mutation is an alteration in a DNA sequence, which is not what this describes; the same alleles are present in both seasons and are being expressed differently."),
 dict(q="In a variable environment, a population of one plant species shows a wide range of heights. Which further observation would show that the range is caused by phenotypic plasticity rather than by differences among the plants' alleles?",
   choices=[
     "Cuttings from a single plant, grown across the same range of conditions, reproduce the whole range of heights",
     "The tallest plants in the field produce the most seeds",
     "The plants in the field differ from one another at many genes",
     "The height of each plant stays the same from year to year in its own spot",
     "Plants grown from seed collected in the field are taller than their parents"], ans=0,
   why="EK 5.5.A.1 makes plasticity a property of a single genotype producing more than one phenotype, so the discriminating evidence is a constant genotype across varying conditions. Cuttings from one plant hold the genotype fixed; every other listed observation leaves genotype and environment varying together."),
 dict(q="EK 5.5.A.1 says that environmental conditions influence gene expression. What does that add to the statement that an organism's phenotype depends on its genotype?",
   choices=[
     "The phenotype depends on which of the inherited genes are expressed, and conditions outside the organism affect that",
     "The phenotype depends only on conditions outside the organism, so the genotype can be ignored",
     "The environment supplies additional alleles that the organism did not inherit from its parents",
     "The environment changes the genotype so that the new phenotype can be inherited by the offspring",
     "The phenotype is set at fertilization, and later conditions only change how it is measured"], ans=0,
   why="EK 5.5.A.1 names gene expression as the point of contact between the environment and the phenotype, and EK 5.3.A.2.iv makes the phenotype the observable expression of inherited traits. The environment can therefore change what is observed without supplying or altering any allele, which is what the framework means by phenotypic plasticity."),
 dict(q="One hydrangea plant was kept for three seasons and repotted between them, as recorded in the table. What property of this plant's response to soil pH do the data show?",
   table=_T_PHTIME,
   choices=[
     "The response is reversible, because returning the plant to the original pH restored the original flower color",
     "The response is permanent, because the flower color changed once and then remained fixed",
     "The response is inherited, because the change persisted into a later season",
     "The response is random, because the flower color differed from one season to the next",
     "The response is a mutation, because the plant's flowers changed color during its lifetime"], ans=0,
   why="EK 5.5.A.1 places the environment's effect on gene expression rather than on the DNA sequence, which allows the phenotype to track conditions in both directions. The single plant flowered blue at the lower pH, pink after being moved to the higher pH, and blue again on being returned, so the change follows the condition rather than persisting."),
 dict(q="A gardener takes two cuttings from a blue-flowered hydrangea, plants one in acidic soil and one in alkaline soil, and asks what color each will flower. What is the best prediction and its reason?",
   choices=[
     "The colors will differ, because the two cuttings share a genotype but not an environment",
     "Both will be blue, because a cutting keeps the flower color of the plant it came from",
     "Both will be blue, because flower color is determined only by the alleles the cutting carries",
     "The colors will differ, because the two cuttings received different alleles when they were taken",
     "The colors cannot be predicted, because the effect of soil on flowers is unrelated to gene expression"], ans=0,
   why="Flower color based on soil pH is one of the illustrative examples printed with EK 5.5.A.1, and the statement says environmental conditions influence gene expression. Cuttings from one plant are genetically identical, so the only variable left is the soil, and the phenotype is expected to follow it."),
 dict(q="A conservation team incubates all of the eggs it rescues at one temperature, chosen because hatching success is highest there. In a species with temperature-dependent sex determination, what risk does this practice create?",
   choices=[
     "The hatchlings may be strongly biased toward one sex, because incubation temperature determines sex in this species",
     "The hatchlings may carry new mutations, because a constant temperature damages DNA",
     "The hatchlings will all be genetically identical, because they developed under identical conditions",
     "The hatchlings will be unable to reproduce, because sex is determined by alleles they did not inherit",
     "There is no risk, because sex is determined at fertilization in every vertebrate species"], ans=0,
   why="Sex determination in reptiles is one of the illustrative examples the CED prints with EK 5.5.A.1: the environmental condition, not an inherited pair of sex chromosomes, sets the phenotype. Holding every clutch at one temperature therefore fixes the environmental input that decides sex, and a single-sex cohort is the predictable result."),
 dict(q="Which of the following is the clearest evidence that an environmental factor, rather than a difference in alleles, is producing a difference in phenotype?",
   choices=[
     "Genetically identical individuals split between two conditions develop different phenotypes",
     "Individuals in two different habitats differ in phenotype and also differ at many genes",
     "A phenotype appears in one family and not in another family of the same species",
     "A phenotype becomes more common in a population over many generations",
     "Two species living in the same habitat show the same phenotype"], ans=0,
   why="EK 5.5.A.1 defines phenotypic plasticity as the ability of INDIVIDUAL GENOTYPES to produce different phenotypes, so an experiment must hold the genotype constant to isolate the environment. Every other listed observation leaves genotype and environment free to vary together, and a phenotype spreading over generations is a change in the population rather than in one genotype."),
 dict(q="Two genetically distinct plant lines were each grown at two temperatures, with the results in the table. Which statement is best supported?",
   table=_T_NORM,
   choices=[
     "Line 1 responds far more strongly to the temperature change than Line 2 does",
     "Line 2 responds far more strongly to the temperature change than Line 1 does",
     "The two lines respond to the temperature change by the same amount",
     "Neither line responds to temperature, since both grew at both temperatures",
     "Line 1 is taller than Line 2 at both temperatures tested"], ans=0,
   why="EK 5.5.A.1 makes plasticity a property of individual genotypes, which allows one genotype to be more plastic than another. The first line grows from 30 to 52 centimeters, a change of 22, while the second grows from 44 to 46, a change of 2; the ranking of the two lines also reverses between the temperatures, so neither line is taller at both."),
 dict(q="A student concludes from an experiment on plasticity that a plant line grown in shade produces larger leaves than the same line grown in sun. What must the experiment have held constant for this conclusion to be sound?",
   choices=[
     "The genotype of the plants, so that only the light conditions differ between the groups",
     "The number of leaves counted, so that both groups contribute the same total leaf area",
     "The time of day at which the leaves were measured, so that the leaves are the same age",
     "The species of the plants, so that the comparison is not between two different species",
     "The light conditions, so that both groups experience the same amount of sun"], ans=0,
   why="EK 5.5.A.1 defines plasticity as one genotype producing different phenotypes, so the genotype is the variable that must be held constant while the environmental factor is varied. Holding the light conditions constant would remove the very comparison the conclusion rests on, and using one species is not enough because individuals of a species differ at many genes."),
 dict(q="Cuttings from one plant were split between shade and full sun, and leaf area was measured in four replicates of each, as reported in the table. What is the mean leaf area in each condition?",
   table=_T_MEAN,
   choices=[
     "51 square centimeters in shade and 29 square centimeters in full sun",
     "29 square centimeters in shade and 51 square centimeters in full sun",
     "48 square centimeters in shade and 26 square centimeters in full sun",
     "54 square centimeters in shade and 32 square centimeters in full sun",
     "40 square centimeters in each condition, since the two means must be equal"], ans=0,
   why="A mean is the sum of the values divided by their number. The four shade replicates 48, 52, 50 and 54 sum to 204, and 204 divided by 4 is 51; the four sun replicates 26, 30, 28 and 32 sum to 116, and 116 divided by 4 is 29. The other listed pairs report single replicates rather than means."),
 dict(q="An animal that spends a summer in bright sunlight develops darker skin, and its offspring, raised indoors, do not. What accounts for this?",
   choices=[
     "The offspring inherited the parent's alleles, not the melanin the parent produced in response to sunlight",
     "The offspring inherited a different set of alleles, because the parent's exposure to sunlight changed its gametes",
     "The offspring will darken later, because an environmentally produced phenotype takes a generation to appear",
     "The parent's skin color was a mutation, and mutations are never passed to the next generation",
     "Melanin production is unrelated to the environment, so the parent's darkening was a coincidence"], ans=0,
   why="The effect of increased ultraviolet light on melanin production is one of the illustrative examples printed with EK 5.5.A.1, and that statement puts the effect on gene expression. What EK 5.3.A.2.iii says is inherited is the set of alleles, so the offspring receive the capacity to make melanin in sunlight rather than the melanin their parent made."),
 dict(q="In the yeast example, cells begin producing a pheromone when cells of the opposite mating type are nearby. Which description of this response is most accurate?",
   choices=[
     "A condition outside the cell changes the expression of genes the cell already carries",
     "A condition outside the cell inserts new genes for pheromone production into the cell",
     "The cell mutates its pheromone genes each time the opposite mating type appears",
     "The cell inherits pheromone production from the neighboring cells of the opposite mating type",
     "The cell produces pheromone at a constant rate that the neighboring cells make easier to detect"], ans=0,
   why="EK 5.5.A.1 states that environmental conditions influence gene expression, and lists the presence of the opposite mating type affecting pheromone production in yeast and other fungi among its illustrative examples. The genes are already present in the genome; what the neighboring cells change is whether and how strongly they are expressed."),
 dict(q="Two fields are sown with seed from the same genetically uniform variety. One field is irrigated and the other is not, and the irrigated field yields taller plants with more seed. A farmer concludes that the irrigated field's seed is genetically superior. What is wrong with the conclusion?",
   choices=[
     "The two fields received the same genotype, so the difference in yield must come from the difference in conditions",
     "The two fields received different genotypes, so the comparison cannot be made at all",
     "Yield is not a phenotype, so it cannot be compared between the two fields",
     "The irrigated plants must have mutated, so their seed is genetically different after all",
     "Nothing is wrong; a taller plant always carries alleles for greater height"], ans=0,
   why="EK 5.5.A.1 states that environmental conditions influence gene expression and can lead to phenotypic plasticity, and EK 5.3.A.2.iii makes the genotype the set of alleles inherited. A genetically uniform variety supplies one genotype to both fields, so no genetic difference is available to explain the result, and yield is observable and therefore part of the phenotype."),
 dict(q="Which observation would show that a difference between two groups of organisms is a change in the population's alleles rather than a plastic response to conditions?",
   choices=[
     "The difference persists when individuals from both groups are raised together in one common environment",
     "The difference is larger in the wild than it is in the laboratory",
     "The difference appears in the first generation after the environment changes",
     "The difference disappears when individuals from both groups are raised in one common environment",
     "The difference is observed in a trait that can be measured precisely"], ans=0,
   why="EK 5.5.A.1 makes plasticity a response of one genotype to conditions, so removing the difference in conditions removes a plastic difference. A difference that survives a common environment cannot be attributed to the environment that is no longer differing, which is why the common-garden result is the discriminating one."),
 dict(q="A student says that because soil pH changes hydrangea flower color, flower color in hydrangeas has no genetic basis. How should this claim be corrected?",
   choices=[
     "The plant's genes encode the pigment and the machinery that responds to pH, so both the genotype and the conditions are required",
     "The claim is correct, because a trait controlled by the environment cannot also be controlled by genes",
     "The claim is correct, because pH acts on the flower directly without involving any gene",
     "The claim should be strengthened, because the pH of the soil is itself inherited from the parent plant",
     "The claim is wrong because soil pH does not in fact affect hydrangea flower color"], ans=0,
   why="EK 5.5.A.1 says environmental conditions influence GENE EXPRESSION, which presupposes genes to express. The illustrative example of flower color based on soil pH is therefore an interaction: the alleles supply the capacity and the condition determines which phenotype that capacity produces."),
 dict(q="Sex in some reptiles is set by incubation temperature, while sex in many mammals is set by which sex chromosome the sperm carries. What does the comparison illustrate?",
   choices=[
     "The same kind of trait can be determined by an environmental condition in one species and by inheritance in another",
     "Environmental sex determination and chromosomal sex determination cannot occur in the same kind of trait",
     "Reptiles have no genes involved in sexual development, since temperature does the work instead",
     "Mammals show phenotypic plasticity for sex determination and reptiles do not",
     "Temperature changes the sex chromosomes that a reptile embryo carries"], ans=0,
   why="Sex determination in reptiles is one of the illustrative examples printed with EK 5.5.A.1 for the influence of environmental conditions on gene expression, while EK 5.4.A.2 covers traits determined by genes on sex chromosomes. Temperature acts on the expression of genes the embryo already carries; it does not change which chromosomes are present."),
 dict(q="An investigator raises clones of one genotype at five temperatures and plots mean body size against temperature. What does the resulting set of measurements describe?",
   choices=[
     "The range of phenotypes that this one genotype produces across the conditions tested",
     "The range of genotypes present in the population from which the clones were taken",
     "The rate at which new alleles arise as temperature increases",
     "The proportion of the population expected to survive at each temperature",
     "The number of genes that contribute to body size in this species"], ans=0,
   why="EK 5.5.A.1 glosses phenotypic plasticity as the ability of individual genotypes to produce different phenotypes. Holding the genotype constant and varying the temperature therefore measures exactly that range of phenotypes, and it can say nothing about how many genotypes, alleles or genes exist because none of those is being varied."),
 dict(q="Why can two people with very similar genotypes for the genes affecting height still differ in adult height?",
   choices=[
     "Conditions during growth, such as nutrition, influence the expression of those genes",
     "Height is not affected by genes at all, so genotype is irrelevant to it",
     "One of them must carry a mutation that arose during adulthood",
     "Height is determined entirely at fertilization and cannot be measured reliably later",
     "Adult height is inherited only from the mother, so similar genotypes are not comparable"], ans=0,
   why="Height and weight in humans is one of the illustrative examples the CED prints with EK 5.5.A.1, which states that environmental conditions influence gene expression. Similar genotypes leave the environment as the remaining source of difference, and the framework identifies gene expression as where that difference acts."),
 dict(q="A biologist studying an arctic mammal moves several animals to a laboratory with a constant twelve hours of light and constant temperature. After a year the animals no longer change coat color between seasons. What does this result show?",
   choices=[
     "The seasonal coat change requires an environmental cue that the constant conditions removed",
     "The animals lost the alleles for the white coat during their year in the laboratory",
     "The seasonal coat change is inherited independently of any environmental condition",
     "The animals mutated in response to the constant conditions of the laboratory",
     "Coat color in this species is determined at birth and the field observations were mistaken"], ans=0,
   why="Seasonal fur color in arctic animals is one of the illustrative examples printed with EK 5.5.A.1, which places the effect of conditions on gene expression. Holding the conditions constant removes the varying input, so the expression no longer varies; the alleles are unchanged, which is why the response returns if the cue is restored."),
 dict(q="A grower wants to select the plants with the best alleles for fruit size from a field in which soil quality varies a great deal from one corner to another. Why is selecting simply the largest fruits a poor method?",
   choices=[
     "Fruit size reflects both the alleles and the growing conditions, so the largest fruits may come from the best soil rather than the best genotypes",
     "Fruit size is not heritable at all, so no selection on it can succeed",
     "Fruit size is determined by soil quality alone, so every plant in the field has the same genotype",
     "The largest fruits come from plants that have mutated, and mutations cannot be selected",
     "Selection can only be applied to traits that are invisible, such as root depth"], ans=0,
   why="EK 5.5.A.1 states that environmental conditions influence gene expression, so an observed phenotype confounds the genotype with the conditions that produced it. EK 5.3.A.2.iii makes the alleles the thing the offspring will inherit, and a large fruit grown in the best corner of the field carries no guarantee of them; a common environment or replication across the field is what separates the two contributions."),
 dict(q="Which of the following is NOT an example of an environmental condition producing more than one phenotype from one genotype?",
   choices=[
     "A population comes to contain more individuals with a dark coat over many generations of predation",
     "Cuttings of one plant flower blue in acidic soil and pink in alkaline soil",
     "Hares of one inbred line grow a white coat under short day lengths and a brown coat under long ones",
     "Eggs from one clutch hatch mostly female at a high incubation temperature and mostly male at a low one",
     "Yeast cells of one strain release pheromone only when the opposite mating type is present"], ans=0,
   why="EK 5.5.A.1 concerns one genotype producing different phenotypes under different conditions. The four illustrative examples listed with it all hold a genotype constant across conditions. A population coming to contain more dark individuals over generations is a change in which genotypes are present, which is the subject of unit 7 rather than of phenotypic plasticity."),
]
