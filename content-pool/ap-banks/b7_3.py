# AP BIOLOGY 7.3 Artificial Selection
# CED effective Fall 2025, Unit 7 Natural Selection. Big idea 1 (Evolution).
# Learning objective 7.3.A, explain how humans can affect diversity within a
# population. Suggested skill 4.B, DESCRIBE DATA FROM A TABLE OR GRAPH,
# including (i) identifying specific data points, (ii) describing trends and
# patterns in the data, and (iii) describing relationships between variables.
# The CED also lists the AP Biology Lab Manual's Artificial Selection Lab as an
# available resource for this topic.
#
# Essential knowledge relied on, in the framework's own words:
#   7.3.A.1  Through ARTIFICIAL SELECTION, humans AFFECT VARIATION in other
#            species.
#
# ONE STATEMENT, THIRTY QUESTIONS -- AND WHY THAT IS NOT PADDING HERE.
# SOCIAL_DEDUPE.md records what happens when a topic with a single essential
# knowledge statement is given thirty slots: US Government 4.7 reached into two
# neighbouring topics and shipped a byte-identical repeat. The answer used there
# was to chain the lone statement to another topic's rather than to invent
# material, and this topic has a second and better answer available: its
# suggested skill is 4.B, which is describing data from a table, and the CED
# points at a lab in which students breed a population and record what happens.
# So the bulk of this module is DATA. Thirteen items carry a table and ask what
# the table shows -- a specific value, a trend, a relationship between two
# variables -- which is the skill the CED names, and each of those items is a
# different question because each table holds different data. The remaining
# items chain EK 7.3.A.1 to EK 7.2.A.1 and EK 7.2.A.2, which is a question
# neither topic can ask alone: 7.2 names the environment as what applies the
# selective pressure and never mentions humans, and 7.3 names humans and never
# mentions the variation they act on.
#
# DELIBERATE OMISSIONS. The consequences of low genetic diversity for a
# population's resilience are EK 7.11.A.1 and belong to b7_11; no key here makes
# a claim about a population's risk of decline. Nothing here names a breed, a
# crop variety or a domesticated species, because the framework names none.
#
# ON FIGURES. The suggested skill mentions graphs; this bank cannot show one, so
# every data set is a table= and no stem refers to a plot.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX. Ranges are
# written "from 41 to 139", never hyphenated.
TOPIC = ("7.3", "Artificial Selection", 7)

# One population bred for larger seeds over eight generations.
_T_SEED = dict(
    headers=["Generation of selective breeding",
             "Mean seed mass of the population (milligrams)"],
    rows=[["Generation 0", "120"],
          ["Generation 2", "139"],
          ["Generation 4", "161"],
          ["Generation 6", "178"],
          ["Generation 8", "195"]])

# Two lines bred in opposite directions from one starting population.
_T_DIVERGE = dict(
    headers=["Generation",
             "Mean bristle number in the line bred for more bristles",
             "Mean bristle number in the line bred for fewer bristles"],
    rows=[["Generation 0", "36", "36"],
          ["Generation 3", "44", "29"],
          ["Generation 6", "51", "23"],
          ["Generation 9", "57", "19"]])

# The spread of one trait before and after a long programme of breeding.
_T_RANGE = dict(
    headers=["Population", "Smallest value observed (grams)",
             "Largest value observed (grams)", "Mean value (grams)"],
    rows=[["Before selective breeding", "41", "139", "88"],
          ["After twenty generations of selective breeding", "96", "134", "117"]])

# Yield of one stock measured at three points in a breeding programme.
_T_YIELD = dict(
    headers=["Stock", "Mean yield per animal (kilograms per year)"],
    rows=[["Unselected stock", "3800"],
          ["After five generations of selection", "5100"],
          ["After ten generations of selection", "6200"]])

# One population bred for larger fruit, with a second trait also recorded.
_T_TRADEOFF = dict(
    headers=["Generation of selection for larger fruit", "Mean mass of one fruit (grams)",
             "Mean number of fruits per plant"],
    rows=[["Generation 0", "52", "46"],
          ["Generation 4", "78", "33"],
          ["Generation 8", "104", "21"]])

# Three starting populations differing in how much the trait varied in them.
_T_RESPONSE = dict(
    headers=["Starting population", "Range of the trait in the starting population (units)",
             "Change in the mean after ten generations of selection (units)"],
    rows=[["Population A", "2", "1"],
          ["Population B", "11", "9"],
          ["Population C", "24", "19"]])

# A selected line and an unselected line kept side by side.
_T_CONTROL = dict(
    headers=["Line", "Selective breeding applied", "Mean trait value at generation 0",
             "Mean trait value at generation 10"],
    rows=[["Line 1", "Yes", "50", "83"],
          ["Line 2", "No", "50", "51"]])

# Several varieties derived by breeders from one wild species.
_T_VARIETIES = dict(
    headers=["Variety", "Trait emphasized by the breeders",
             "Value of that trait relative to the wild form"],
    rows=[["Wild form", "None", "1.0 times"],
          ["Variety 1", "Leaf size", "4.2 times"],
          ["Variety 2", "Stem thickness", "3.6 times"],
          ["Variety 3", "Flower cluster size", "5.1 times"]])

QUESTIONS = [
 dict(q="What does the framework say humans do through artificial selection?",
   choices=[
     "They affect variation in other species",
     "They create new species from nothing",
     "They change the genetic code that other species use",
     "They prevent other species from varying at all",
     "They alter their own species rather than any other"], ans=0,
   why="EK 7.3.A.1 states that through artificial selection humans affect variation in other species. The framework's verb is affect and its object is variation in another species, which is narrower than creating species and different from altering the code, which EK 6.4.A.3.iv makes shared across nearly all organisms."),
 dict(q="In natural selection the environment applies the selective pressure. What takes that role in artificial selection?",
   choices=[
     "Humans, who decide which individuals breed and so affect variation in the species",
     "The environment, which continues to be the only source of selective pressure",
     "The individuals of the species themselves, which choose which traits to develop",
     "Nothing, since artificial selection does not involve any selective pressure",
     "Mutation, which supplies the direction as well as the variation"], ans=0,
   why="EK 7.2.A.2 states that environments change and apply selective pressures to populations, and EK 7.3.A.1 states that through artificial selection humans affect variation in other species. Substituting the human choice of which individuals breed for the environmental pressure is what distinguishes the two, and EK 6.7.B.1 makes mutation random and so directionless."),
 dict(q="A breeder wants to increase a trait in a population but every individual in it shows the identical value of that trait. What does the framework imply?",
   choices=[
     "There is no variation in that trait for the breeder to select among",
     "The breeder can create the variation needed by choosing which individuals breed",
     "The breeder can select on the trait as effectively as in a varying population",
     "The trait will vary spontaneously once breeding begins",
     "Artificial selection works only on traits that show no variation"], ans=0,
   why="EK 7.3.A.1 has humans affect variation in other species, and EK 7.2.A.1 makes phenotypic variation what selection acts on. Choosing among individuals requires differences among them to choose between; new variation arises from mutation under EK 6.7.B.1 rather than from the act of selecting."),
 dict(q="The table reports the mean seed mass of one population across eight generations of breeding for larger seeds. What was the mean seed mass at generation 4?",
   table=_T_SEED,
   choices=[
     "161 milligrams",
     "139 milligrams",
     "178 milligrams",
     "120 milligrams",
     "195 milligrams"], ans=0,
   why="This is the first part of suggested skill 4.B, identifying a specific data point. The row for the fourth generation of breeding records a mean of 161 milligrams; the neighbouring values belong to the second and sixth generations and the extreme values to the start and end of the programme."),
 dict(q="Using the same seed mass data, how would the trend across the eight generations be described?",
   table=_T_SEED,
   choices=[
     "The mean rose at every recorded generation, from 120 to 195 milligrams",
     "The mean fell at every recorded generation, from 195 to 120 milligrams",
     "The mean rose and then fell, ending near where it began",
     "The mean stayed the same across all the recorded generations",
     "The mean changed without any consistent direction from one generation to the next"], ans=0,
   why="This is the second part of suggested skill 4.B, describing a trend. The five recorded means are 120, 139, 161, 178 and 195 milligrams, which increase at every step, and EK 7.3.A.1 attributes such a change to humans affecting variation in the species through artificial selection."),
 dict(q="Using the same seed mass data, what was the total change in the mean across the eight generations, and about how much was that per generation?",
   table=_T_SEED,
   choices=[
     "A rise of 75 milligrams in total, which is a little over 9 milligrams per generation",
     "A rise of 75 milligrams in total, which is a little over 15 milligrams per generation",
     "A rise of 195 milligrams in total, which is a little over 24 milligrams per generation",
     "A rise of 39 milligrams in total, which is a little under 5 milligrams per generation",
     "No change in total, since the mean returned to its starting value"], ans=0,
   why="The mean rises from 120 milligrams at the start to 195 at the eighth generation, a total of 75 milligrams, and 75 divided by the 8 generations is about 9.4 milligrams per generation. Dividing by the number of rows rather than the number of generations gives the wrong denominator."),
 dict(q="Two lines were bred from one starting population, one for more bristles and one for fewer, with the results in the table. What do the data show?",
   table=_T_DIVERGE,
   choices=[
     "The two lines began at the same mean and moved apart in opposite directions",
     "The two lines began at different means and converged on the same value",
     "The two lines began at the same mean and both rose together",
     "The two lines began at the same mean and neither changed",
     "The two lines began at different means and both fell together"], ans=0,
   why="EK 7.3.A.1 states that through artificial selection humans affect variation in other species. Both lines start at a mean of 36 bristles; by the ninth generation one reads 57 and the other 19, so they have moved in opposite directions from a common starting point."),
 dict(q="Using the same two lines, what does the fact that both began at the same mean allow a reader to conclude?",
   table=_T_DIVERGE,
   choices=[
     "The difference between the lines at generation 9 arose during the breeding programme rather than being present at the start",
     "The difference between the lines at generation 9 was present at the start and merely became easier to measure",
     "The two lines must have come from different species",
     "The breeding programme had no effect, since the two lines were once alike",
     "The line bred for fewer bristles must have been given a different diet"], ans=0,
   why="Both lines record a mean of 36 bristles at generation 0, so nothing distinguished them then, and by generation 9 they differ by 38 bristles. EK 7.3.A.1 attributes such an effect on variation to the artificial selection applied, and a common starting point is what rules out the difference having been there already."),
 dict(q="The table reports the smallest value, the largest value and the mean of one trait before and after twenty generations of breeding. What happened to the spread of the trait?",
   table=_T_RANGE,
   choices=[
     "The spread narrowed, from a range of 98 grams to a range of 38 grams",
     "The spread widened, from a range of 38 grams to a range of 98 grams",
     "The spread was unchanged, since both populations contain a range of values",
     "The spread cannot be worked out, because the number of individuals is not given",
     "The spread narrowed to zero, since every individual now shows the mean value"], ans=0,
   why="A range is the largest value less the smallest. Before breeding that is 139 less 41, which is 98 grams; after it is 134 less 96, which is 38. EK 7.3.A.1 states that humans affect variation in other species through artificial selection, and a narrowing of the spread is one such effect."),
 dict(q="Using the same before and after data, what happened to the mean while the spread was changing?",
   table=_T_RANGE,
   choices=[
     "The mean rose from 88 to 117 grams while the spread narrowed",
     "The mean fell from 117 to 88 grams while the spread narrowed",
     "The mean was unchanged while the spread narrowed",
     "The mean rose while the spread also widened",
     "The mean cannot be compared, because the two populations are different species"], ans=0,
   why="This is skill 4.B applied to two variables at once. The recorded means are 88 grams before and 117 grams after, a rise, while the range falls from 98 to 38 grams; the two populations are the same population at two times, which is what makes the comparison meaningful."),
 dict(q="The table reports the mean yield of one stock at three points in a breeding programme. By about what percentage did the mean yield rise from the unselected stock to the tenth generation?",
   table=_T_YIELD,
   choices=[
     "By about 63 percent",
     "By about 24 percent",
     "By about 163 percent",
     "By about 38 percent",
     "By about 6 percent"], ans=0,
   why="A percentage increase is the change divided by the starting value. The mean rises from 3800 to 6200 kilograms per year, a change of 2400, and 2400 divided by 3800 is about 0.63, so about 63 percent. The value near 163 percent is the final figure as a percentage of the first rather than the increase."),
 dict(q="Using the same yield data, what is the trend across the three recorded points?",
   table=_T_YIELD,
   choices=[
     "The mean yield rose at each recorded point in the programme",
     "The mean yield fell at each recorded point in the programme",
     "The mean yield rose and then fell back toward its starting value",
     "The mean yield was the same at all three recorded points",
     "The mean yield rose only after the tenth generation"], ans=0,
   why="This is skill 4.B's second part, describing a trend. The three recorded means are 3800, 5100 and 6200 kilograms per year, which increase at each step, and EK 7.3.A.1 attributes an effect of this kind to humans acting on variation in the species."),
 dict(q="One population was bred for larger fruit and a second trait was recorded alongside, as reported in the table. What relationship between the two variables do the data show?",
   table=_T_TRADEOFF,
   choices=[
     "As the mean mass of one fruit rose, the mean number of fruits per plant fell",
     "As the mean mass of one fruit rose, the mean number of fruits per plant also rose",
     "The mean number of fruits per plant did not change as the mean mass rose",
     "The mean mass of one fruit did not change while the number per plant fell",
     "Neither variable changed across the eight generations"], ans=0,
   why="This is the third part of suggested skill 4.B, describing a relationship between variables. Mean fruit mass rises from 52 to 104 grams while mean fruits per plant falls from 46 to 21, so the two move in opposite directions across the same generations."),
 dict(q="Using the same fruit data, which statement stays within describing the data rather than explaining them?",
   table=_T_TRADEOFF,
   choices=[
     "Mean fruit mass doubled across the eight generations while mean fruits per plant fell by more than half",
     "Selecting for larger fruit caused the plants to divert resources away from making more fruits",
     "The breeders should have selected for fruit number instead of fruit mass",
     "The plants would produce both larger and more numerous fruits if given more water",
     "The relationship between the two traits is the same in every plant species"], ans=0,
   why="Skill 4.B is describing data from a table, which is reporting what the numbers say. Mass rises from 52 to 104, which is a doubling, and number falls from 46 to 21, which is more than half. The other options offer a cause, a recommendation, a prediction about untested conditions, or a generalization beyond the data, none of which the table settles."),
 dict(q="Three starting populations were selected for the same number of generations, with the results in the table. What relationship do the data show?",
   table=_T_RESPONSE,
   choices=[
     "The wider the range of the trait in the starting population, the larger the change achieved by selection",
     "The wider the range of the trait in the starting population, the smaller the change achieved by selection",
     "The change achieved by selection was the same for all three starting populations",
     "The change achieved by selection was unrelated to the range in the starting population",
     "Only the population with the narrowest range responded to selection at all"], ans=0,
   why="This is skill 4.B's third part, describing a relationship between variables. The three starting ranges are 2, 11 and 24 units and the corresponding changes are 1, 9 and 19 units, which rise together; EK 7.2.A.1 makes phenotypic variation what selection acts on, which is consistent with a population that varies more responding more."),
 dict(q="Using the same three populations, what happened in the population whose trait varied least at the start?",
   table=_T_RESPONSE,
   choices=[
     "It changed the least of the three, by one unit over the ten generations",
     "It changed the most of the three, since less variation makes selection easier",
     "It did not change at all, since selection requires variation",
     "It changed by the same amount as the other two populations",
     "It changed in the opposite direction to the other two populations"], ans=0,
   why="Skill 4.B's first part is identifying a specific data point. The population with the narrowest starting range, 2 units, records a change of 1 unit, which is the smallest of the three recorded changes and is not zero."),
 dict(q="A selected line and an unselected line were kept side by side, with the results in the table. What do the data allow a reader to conclude?",
   table=_T_CONTROL,
   choices=[
     "The change in the selected line is attributable to the selective breeding, since the unselected line barely moved",
     "The change in the selected line would have happened anyway, since the unselected line also changed",
     "Neither line changed, so selective breeding had no effect",
     "The unselected line changed more than the selected line",
     "The two lines began at different values, so no comparison is possible"], ans=0,
   why="Both lines start at a mean of 50; after ten generations the bred line reads 83 and the unselected line 51. The unselected line is the comparison that shows the change was not simply what happens with time, and EK 7.3.A.1 attributes such an effect on variation to the artificial selection applied."),
 dict(q="Why does a breeding experiment of this kind include a line to which no selection is applied?",
   choices=[
     "To show what the trait does over the same number of generations without selection, so the effect of the selection can be separated from it",
     "To provide extra individuals for the selected line to breed with",
     "To increase the variation available in the selected line",
     "To demonstrate that the trait cannot change without human intervention",
     "Because the framework requires two lines in every breeding programme"], ans=0,
   why="EK 7.3.A.1 attributes an effect on variation to artificial selection, and attributing an observed change to it requires knowing what would have happened without it. An unselected line supplies exactly that comparison over the same span of generations."),
 dict(q="The table reports three varieties derived by breeders from one wild species. What do these data show about how humans have affected this species?",
   table=_T_VARIETIES,
   choices=[
     "Different traits were emphasized in different varieties, so one species has been made to vary in several directions",
     "The same trait was emphasized in every variety, so the species has been made to vary in one direction",
     "The varieties are unchanged from the wild form in every trait recorded",
     "The wild form exceeds all three varieties in the traits recorded",
     "The three varieties belong to three different species"], ans=0,
   why="EK 7.3.A.1 states that through artificial selection humans affect variation in other species. Each variety is recorded against a different emphasized trait, and each exceeds the wild form on the trait it was bred for, so the effect on the species runs in several directions at once."),
 dict(q="Using the same varieties, which variety exceeds the wild form by the largest factor on the trait its breeders emphasized?",
   table=_T_VARIETIES,
   choices=[
     "The variety bred for flower cluster size, at 5.1 times the wild form",
     "The variety bred for leaf size, at 4.2 times the wild form",
     "The variety bred for stem thickness, at 3.6 times the wild form",
     "The wild form, which is the standard the others are measured against",
     "All three varieties equally, since all three exceed the wild form"], ans=0,
   why="This is skill 4.B's first part, identifying a specific data point. The three recorded factors are 4.2, 3.6 and 5.1 times the wild form, and the largest belongs to the variety bred for flower cluster size; the wild form is recorded at 1.0 times, which is the baseline rather than a competitor."),
 dict(q="What is the essential difference between natural selection and artificial selection, as the framework's statements describe them?",
   choices=[
     "In natural selection the environment applies the pressure; in artificial selection humans decide which individuals breed",
     "In natural selection variation is required; in artificial selection it is not",
     "In natural selection traits are inherited; in artificial selection they are acquired during life",
     "In natural selection the population changes; in artificial selection only individuals change",
     "In natural selection fitness is measured by reproductive success; in artificial selection it is measured by lifespan"], ans=0,
   why="EK 7.2.A.2 makes the environment what applies selective pressures to populations, and EK 7.3.A.1 makes humans the agent through which artificial selection affects variation in other species. Both act on the variation EK 7.2.A.1 describes and both work through which individuals leave offspring, so the agent is what differs."),
 dict(q="A breeder selects the largest individuals of each generation as parents for the next. Over many generations the mean size of the population rises. Which framework statement does this illustrate?",
   choices=[
     "That through artificial selection humans affect variation in other species",
     "That environments change and apply selective pressures to populations",
     "That mutations are a source of genetic variation",
     "That evolutionary fitness is measured by reproductive success",
     "That the genetic code is shared by nearly all living organisms"], ans=0,
   why="EK 7.3.A.1 states that through artificial selection humans affect variation in other species, which is what choosing the parents of each generation and observing the population change amounts to. The other statements are the framework's but concern the environment, the origin of variation, the measure of fitness and the code."),
 dict(q="Why can artificial selection change a population only in directions the population's existing variation allows?",
   choices=[
     "Selection of any kind acts on the phenotypic variation present, and a breeder can only choose among the individuals that exist",
     "Selection of any kind creates the variation it needs, so the existing variation is irrelevant",
     "Breeders can select only traits that are invisible to the environment",
     "Existing variation is removed at the start of a breeding programme",
     "A population's variation is fixed permanently at the moment it is founded"], ans=0,
   why="EK 7.2.A.1 states that natural selection acts on phenotypic variations in populations, and a breeder choosing parents is choosing among the individuals in front of them. EK 7.3.A.1 has humans affect that variation rather than supply it; new variation comes from mutation under EK 6.7.B.1."),
 dict(q="A breeder finds that after many generations of selection a population responds less and less to further selection on the same trait. Which explanation is best supported by the data in this topic?",
   choices=[
     "The variation in that trait among the remaining individuals has narrowed, and the data show that a narrower starting range gives a smaller response",
     "Selection has changed the genetic code the population uses",
     "The individuals have become resistant to being selected",
     "The trait has become acquired during life rather than inherited",
     "The breeder's choices no longer affect which individuals reproduce"], ans=0,
   why="Two tables in this topic supply the reasoning: one shows the range of a trait narrowing across twenty generations of breeding, and another shows that populations with narrower starting ranges change less over the same number of generations. EK 7.2.A.1 makes phenotypic variation what selection acts on, so less of it leaves less to act on."),
 dict(q="A researcher reports that in one breeding programme the mean of a trait rose while its range narrowed. Which of these statements describes the data, and which goes beyond them?",
   choices=[
     "The rise in the mean and the narrowing of the range describe the data; a claim about what will happen in the next twenty generations goes beyond them",
     "The rise in the mean describes the data; the narrowing of the range goes beyond them",
     "Both statements go beyond the data, since a table cannot report a change",
     "Both statements describe the data, including any prediction drawn from them",
     "Neither statement can be made, since means and ranges are not data"], ans=0,
   why="Suggested skill 4.B is describing data from a table, which covers both a value and a trend the recorded numbers show. Extending the pattern to generations that were not measured is a prediction rather than a description, and nothing in the table settles it."),
 dict(q="What does the learning objective for this topic ask students to explain?",
   choices=[
     "How humans can affect diversity within a population",
     "How populations affect the humans that breed them",
     "How mutations arise during a breeding programme",
     "How the genetic code differs between wild and bred populations",
     "How an individual's phenotype changes during its own lifetime"], ans=0,
   why="Learning objective 7.3.A is to explain how humans can affect diversity within a population, and EK 7.3.A.1 supplies the mechanism: through artificial selection humans affect variation in other species. An individual's own phenotype changing during life is EK 5.5.A.1's plasticity."),
 dict(q="Two breeders start from the same population. One selects for a larger value of a trait and the other for a smaller value. What does the framework predict?",
   choices=[
     "The two resulting populations can come to differ in that trait, because each breeder affects the variation in a different direction",
     "The two resulting populations must end up the same, since they began the same",
     "Neither population can change, since they began from the same variation",
     "Both populations will move in the same direction, whichever way each breeder selects",
     "The two populations will exchange individuals until their means are equal"], ans=0,
   why="EK 7.3.A.1 states that through artificial selection humans affect variation in other species, and the direction of that effect follows from which individuals the breeder allows to reproduce. This module's divergence data show exactly that outcome from a common starting mean."),
 dict(q="A student says that artificial selection proves that a breeder can produce any trait a species does not already have. How should this be corrected?",
   choices=[
     "A breeder can only select among the variation present, so a trait with no basis in the population cannot be selected for",
     "The student is correct, since selection creates whatever variation the breeder chooses",
     "A breeder can produce any trait, but only in wild populations rather than bred ones",
     "A breeder can produce any trait, provided enough generations pass",
     "Artificial selection does not affect variation at all, so no trait can be produced"], ans=0,
   why="EK 7.3.A.1 has humans affect variation in other species, and EK 7.2.A.1 makes phenotypic variation what selection acts on. Choosing parents sorts what exists; EK 6.7.B.1 makes mutation the random source of anything new, and a breeder does not direct it."),
 dict(q="Which statement about a breeding programme is a description of a trend, in the sense suggested skill 4.B intends?",
   choices=[
     "The mean value of the trait increased at every generation that was recorded",
     "The mean value of the trait increased because the breeder chose the largest parents",
     "The mean value of the trait should be increased further in future generations",
     "The mean value of the trait would increase in any species treated this way",
     "The mean value of the trait is the most important measure of the programme"], ans=0,
   why="Skill 4.B's second part is describing trends and patterns in the data, which is a report of the direction the recorded numbers take. Naming a cause, recommending an action, generalizing to other species and judging importance are each something other than describing what the data show."),
 dict(q="Which account of artificial selection is consistent with everything the framework states about it?",
   choices=[
     "A population already varies; humans allow only some individuals to breed; over generations the variation in the species is affected in the direction the humans chose",
     "A population is uniform; humans create the variation they want by choosing parents; the new variation is then inherited",
     "Humans change the environment; the environment then changes the individuals during their lifetimes; those changes are inherited",
     "Humans change the genetic code of the species; the species then reads its genes differently",
     "Humans select individuals; the selected individuals acquire the desired trait; the trait is then passed on"], ans=0,
   why="EK 7.3.A.1 states that through artificial selection humans affect variation in other species, and EK 7.2.A.1 makes phenotypic variation what any selection acts on. Each rejected account has selection create variation, has acquired changes inherited, or alters the genetic code, which EK 6.4.A.3.iv makes shared across nearly all organisms."),
]
