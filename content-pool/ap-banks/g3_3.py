# AP HUMAN GEOGRAPHY 3.3 Cultural Patterns -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding PSO-3; learning
# objective PSO-3.D, "Explain patterns and landscapes of language, religion,
# ethnicity, and gender."
#
# Essential knowledge, in full -- two statements:
#   PSO-3.D.1  Regional patterns of language, religion, and ethnicity contribute
#              to a sense of place, enhance placemaking, and shape the global
#              cultural landscape.
#   PSO-3.D.2  Language, ethnicity, and religion are factors in creating
#              centripetal and centrifugal forces.
#
# The same three cultural variables appear in both statements doing two
# different jobs, and keeping the jobs apart is what this module is for:
#
#   PSO-3.D.1 is about MEANING. Regional patterns of language, religion and
#   ethnicity give a place its character, are used deliberately to make places,
#   and together compose the global cultural landscape. Items 1-8, 11, 15, 18,
#   22 and 26 are keyed to it.
#
#   PSO-3.D.2 is about COHESION. The same three variables can bind a state
#   together or pull it apart. Items 9, 10, 12-14, 16, 17, 19-21, 23-25 and
#   27-30 are keyed to it.
#
# The two terms PSO-3.D.2 names are not defined by the CED, so the definitions
# every key here rests on are:
#   centripetal force  anything that draws a population together and strengthens
#                      its attachment to the state or community -- a shared
#                      language, a common faith, a unifying institution
#   centrifugal force  anything that pulls a population apart and weakens that
#                      attachment -- linguistic division, sectarian conflict,
#                      an ethnic minority denied standing
# The critical point, and the reason items 10, 16, 21 and 28 exist: the SAME
# variable can act in either direction, and which direction depends on how it is
# distributed and how the state treats it. A single national language is
# centripetal where everyone already speaks it and centrifugal where it is
# imposed on speakers of another.
#
# SENSE OF PLACE and PLACEMAKING, also undefined by the CED and used here as:
#   sense of place  the character and meaning a place holds for those who know it
#   placemaking     the deliberate shaping of a place's character, by residents
#                   or by institutions, so that it means something particular
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_3.py. FIVE choices (A-E).
TOPIC = ("3.3", "Cultural Patterns", 3)

QUESTIONS = [
 dict(q="Which three cultural variables does the framework name as producing regional patterns that shape the global cultural landscape?",
   choices=[
     "Language, religion, and ethnicity",
     "Language, technology, and climate",
     "Religion, economy, and government",
     "Ethnicity, migration, and urbanization",
     "Language, agriculture, and architecture"],
   ans=0,
   why="EK PSO-3.D.1 names exactly these three and EK PSO-3.D.2 names the same three again in a different role. Their reappearance is deliberate: the variables that give a region its character are the ones that can also unite or divide a state."),

 dict(q="A district is known for the language heard in its streets, the festivals it keeps, and the food sold in its markets, and residents describe it as unmistakably itself. This is best described as",
   choices=[
     "A sense of place produced by regional patterns of language, religion, and ethnicity",
     "A centrifugal force acting on the district",
     "A physical feature of the district",
     "An absence of cultural pattern",
     "A political boundary"],
   ans=0,
   why="EK PSO-3.D.1 states that regional patterns of language, religion and ethnicity contribute to a sense of place. What residents are describing is the character those patterns give a district, which is exactly the effect the statement names."),

 dict(q="A neighbourhood association installs bilingual street signage, commissions murals of the community's history, and reopens a disused hall for its festivals. This activity is best described as",
   choices=[
     "Placemaking, the deliberate shaping of a place's character so that it expresses a particular community",
     "A centrifugal force weakening the neighbourhood",
     "Sequent occupance",
     "An ethnocentric attitude",
     "A physical modification of the landscape only"],
   ans=0,
   why="EK PSO-3.D.1 says regional patterns of language, religion and ethnicity ENHANCE PLACEMAKING. Signage, murals and a reopened hall are all deliberate acts intended to make the district legible as belonging to a particular community."),

 dict(q="How does the framework connect regional cultural patterns to the GLOBAL cultural landscape?",
   choices=[
     "Regional patterns of language, religion, and ethnicity together compose the world's cultural landscape rather than being local exceptions to it",
     "Only global patterns matter, and regional ones are irrelevant",
     "Regional patterns exist only where there is no global culture",
     "The global cultural landscape is uniform",
     "Regional patterns have no relationship to the global scale"],
   ans=0,
   why="EK PSO-3.D.1 says these regional patterns SHAPE the global cultural landscape, which is a statement about scale. The world's cultural map is the assembly of its regional ones rather than a separate thing sitting above them."),

 dict(q="Which of the following would contribute most directly to a region's distinctive sense of place, in the framework's terms?",
   choices=[
     "A language spoken there and almost nowhere else, together with religious observances kept there and a shared ethnic history",
     "The region's mean July temperature",
     "The region's distance from the national capital",
     "The number of people living in the region",
     "The region's total area in square kilometres"],
   ans=0,
   why="EK PSO-3.D.1 names language, religion and ethnicity as the sources of a sense of place. Temperature, distance, population and area describe a region without giving it a character anyone could recognize as belonging to a particular people."),

 dict(q="A city government funds a heritage trail, a museum, and an annual festival built around one community's history. In the framework's terms this is",
   choices=[
     "Institutional placemaking, since a public body is deliberately shaping what the place is understood to mean",
     "A centrifugal force by definition",
     "An example of sequent occupance",
     "A physical feature of the city",
     "Evidence that the city has no cultural pattern"],
   ans=0,
   why="EK PSO-3.D.1 says cultural patterns enhance placemaking without limiting who does the making. A municipality choosing which history to mark and fund is shaping meaning as deliberately as residents do, and with more resources."),

 dict(q="Two regions of one country have distinct languages, distinct religious traditions, and long separate histories. According to the framework, what does this produce?",
   choices=[
     "Strong regional senses of place, and cultural variables capable of acting as centrifugal forces on the state",
     "A single uniform national culture",
     "No effect on the state, since culture and politics are separate",
     "An absence of any sense of place in either region",
     "A guaranteed division of the country"],
   ans=0,
   why="EK PSO-3.D.1 makes these patterns sources of a sense of place and EK PSO-3.D.2 makes the same variables factors in centrifugal forces. Naming a capacity rather than an outcome is what makes the answer defensible: division is possible, not guaranteed."),

 dict(q="Which is the strongest reason toponyms are useful evidence about regional cultural patterns?",
   choices=[
     "Place names record the language of whoever named a place and often survive long after that group has gone",
     "Place names are chosen by governments and therefore reflect official policy only",
     "Place names change every generation",
     "Place names carry no linguistic information",
     "Place names are the only cultural evidence available"],
   ans=0,
   why="EK PSO-3.D.1 makes regional patterns of language part of what shapes a cultural landscape, and a place name is language fixed to a location. Their durability is what makes them evidence, since a name can outlast the population that coined it."),

 dict(q="Centripetal and centrifugal forces, as the framework applies them to culture, refer to",
   choices=[
     "Factors that draw a population together and factors that pull it apart",
     "Physical forces acting on the Earth's surface",
     "The movement of people toward and away from cities",
     "The growth and decline of a population",
     "The spread and disappearance of a language"],
   ans=0,
   why="EK PSO-3.D.2 names language, ethnicity and religion as factors in creating centripetal and centrifugal forces, and the CED does not define the pair. The definitions used throughout are cohesion and division: what binds a population to a state or community, and what loosens that bond."),

 dict(q="A country adopts a single official language spoken as a first language by 92 percent of its people. What is the most likely effect?",
   choices=[
     "A centripetal effect, since the policy formalizes something almost everyone already shares",
     "A centrifugal effect, since language policy always divides",
     "No effect, since language is not a political variable",
     "A centrifugal effect, since the remaining 8 percent are numerous",
     "A centripetal effect only if the country is small"],
   ans=0,
   why="EK PSO-3.D.2 makes language a factor in both kinds of force, and which one it produces depends on distribution. Formalizing a language that nearly the whole population already uses adds a symbol of unity without imposing a cost on many people."),

 dict(q="A country adopts a single official language spoken as a first language by 46 percent of its people, in a state where the other 54 percent speak four other languages. What is the most likely effect?",
   choices=[
     "A centrifugal effect, since a majority is required to conduct public life in a language that is not its own",
     "A centripetal effect, since a single language is always unifying",
     "No effect, since official languages are symbolic",
     "A centripetal effect, since 46 percent is the largest group",
     "An effect that cannot be predicted from the figures"],
   ans=0,
   why="EK PSO-3.D.2 makes language a factor in both directions, and the same policy that unified in the previous case divides here because the distribution is different. Being required to use another group's language in court, school and administration is a standing grievance rather than a symbol of unity."),

 dict(q="What is the most important lesson from comparing those two language policies?",
   choices=[
     "The same cultural variable can act as a centripetal or a centrifugal force depending on how it is distributed and how the state handles it",
     "Language policy always unifies a country",
     "Language policy always divides a country",
     "Language is not a factor in either kind of force",
     "Only religion can produce centrifugal forces"],
   ans=0,
   why="EK PSO-3.D.2 names the three variables as factors in BOTH kinds of force, which is the point of listing them once for the pair rather than twice. Distribution and policy decide the direction; the variable itself decides nothing."),

 dict(q="A shared religion observed by almost the whole population, with a common calendar of holidays and a widely respected institution, most likely acts as",
   choices=[
     "A centripetal force, since it gives the population a common identity and shared institutions",
     "A centrifugal force, since religion always divides",
     "Neither, since religion is a private matter",
     "A centrifugal force, since institutions compete with the state",
     "A physical feature of the landscape"],
   ans=0,
   why="EK PSO-3.D.2 names religion among the factors in centripetal and centrifugal forces. A faith held in common supplies shared symbols, a shared calendar and institutions reaching every settlement, which is cohesion in its most tangible form."),

 dict(q="A state in which two religious communities of similar size contest control of public institutions is most likely experiencing",
   choices=[
     "A centrifugal force, since the division runs through the institutions the state depends on",
     "A centripetal force, since both communities are engaged in national life",
     "No cultural force at all",
     "A centripetal force, since the communities are of similar size",
     "A sense of place produced by religion"],
   ans=0,
   why="EK PSO-3.D.2 names religion as a factor in centrifugal as well as centripetal forces. Two communities of comparable size competing for the same institutions makes every institutional decision a contest between them, which is what pulls a state apart."),

 dict(q="Which of the following best illustrates a regional pattern of ETHNICITY shaping a cultural landscape?",
   choices=[
     "A belt of settlements founded by one group, where the surnames, church denominations, and building styles still differ from those on either side",
     "A belt of settlements at the same elevation",
     "A belt of settlements with similar populations",
     "A belt of settlements the same distance from a river",
     "A belt of settlements built in the same decade"],
   ans=0,
   why="EK PSO-3.D.1 names ethnicity among the regional patterns that shape a cultural landscape. A shared founding population leaves traces in names, worship and building that persist as a visible band across the map."),

 dict(q="A national government recognizes a minority language for education and official business in the region where it is spoken. What is the most likely effect on cohesion?",
   choices=[
     "A centripetal effect, since recognition removes a grievance and gives the minority a stake in the state",
     "A centrifugal effect, since recognition encourages separatism in every case",
     "No effect, since language policy is symbolic",
     "A centrifugal effect, since two languages cannot coexist",
     "An effect on the physical landscape only"],
   ans=0,
   why="EK PSO-3.D.2 makes language a factor in both directions, and accommodation moves it toward the centripetal one by converting an exclusion into a form of belonging. Asserting the opposite as an invariable rule is what makes the separatism option wrong rather than merely pessimistic."),

 dict(q="Why does the framework list the same three variables in both of its statements for this topic?",
   choices=[
     "Because language, religion, and ethnicity both give regions their character and determine whether a state coheres, and those are two different consequences of one distribution",
     "Because the two statements say the same thing twice",
     "Because only these three variables exist in cultural geography",
     "Because the statements were written by different authors",
     "Because the second statement corrects the first"],
   ans=0,
   why="EK PSO-3.D.1 assigns the three variables a role in meaning and EK PSO-3.D.2 assigns them a role in cohesion. One map of who speaks, worships and identifies how produces both a landscape of distinctive places and a politics of unity or division."),

 dict(q="A geographer says a region 'has a strong sense of place'. What would be the best evidence for that claim?",
   choices=[
     "Residents and outsiders alike can describe what is distinctive about the region, and its language, observances, and landscape support the description",
     "The region has a large population",
     "The region has clearly surveyed boundaries",
     "The region is administratively separate",
     "The region has a high average income"],
   ans=0,
   why="EK PSO-3.D.1 makes sense of place a product of regional patterns of language, religion and ethnicity. Evidence therefore has to be about recognizable character rather than about size, administration or wealth, none of which produces distinctiveness."),

 dict(q="Which pairing correctly matches a cultural situation to the force it most likely produces?",
   choices=[
     "A shared national language taught in every school, matched to a centripetal force",
     "A shared national language taught in every school, matched to a centrifugal force",
     "A single religion observed by almost everyone, matched to a centrifugal force",
     "An ethnic minority with full political representation, matched to a centrifugal force",
     "A common founding history taught in every school, matched to a centrifugal force"],
   ans=0,
   why="EK PSO-3.D.2 makes language a factor in both kinds of force, and a language everyone learns and shares supplies a medium for national life. The other four pairings attach a unifying condition to the dividing force, which reverses the relationship."),

 dict(q="A state suppresses a minority's language in schools and public life. What effect on cohesion should be expected, and why?",
   choices=[
     "A centrifugal effect, since suppression turns a cultural difference into a grievance and a basis for organizing against the state",
     "A centripetal effect, since fewer languages mean more unity",
     "No effect, since schooling is a local matter",
     "A centripetal effect, since the minority will assimilate quickly",
     "An effect on sense of place but not on cohesion"],
   ans=0,
   why="EK PSO-3.D.2 names language as a factor in centrifugal forces, and suppression is the case in which it most reliably becomes one. A difference that could have been unremarkable is made into an identity worth defending, which is the opposite of what suppression intends."),

 dict(q="A city district is systematically renamed, its shopfront signage regulated to one language, and its festivals discouraged. Which two framework concepts are involved?",
   choices=[
     "Placemaking used to erase one community's sense of place, and a cultural variable acting as a centrifugal force",
     "Sequent occupance and carrying capacity",
     "Distance decay and time-space compression",
     "Physiological density and arithmetic density",
     "Neither concept, since signage rules are administrative"],
   ans=0,
   why="EK PSO-3.D.1 covers placemaking and sense of place and EK PSO-3.D.2 covers the resulting force on cohesion. Placemaking is not intrinsically benign: the same tools that build a community's character can be turned to removing it."),

 dict(q="Which observation would most support the claim that language, religion, and ethnicity are analytically separate variables rather than one thing?",
   choices=[
     "Two groups sharing a language but not a religion, and two sharing a religion but not a language, within the same country",
     "A group that shares all three with its neighbours",
     "A group that shares none of the three with its neighbours",
     "A country with only one language",
     "A country with only one religion"],
   ans=0,
   why="EK PSO-3.D.1 and EK PSO-3.D.2 both list the three separately, and separateness is demonstrated by cross-cutting cases. Where the three lines fall in different places, no one of them can be standing in for the others."),

 dict(q="A country's minority group is concentrated in one border region, shares a language with the state across that border, and has little representation in the national government. Which combination of framework factors is at work?",
   choices=[
     "Language and ethnicity acting as centrifugal forces, sharpened by the group's concentration and its exclusion from national institutions",
     "Religion acting as a centripetal force",
     "Language acting as a centripetal force",
     "No framework factor, since the situation is political rather than cultural",
     "Ethnicity acting as a centripetal force"],
   ans=0,
   why="EK PSO-3.D.2 names language and ethnicity among the factors in centrifugal forces, and this case adds the two conditions that intensify them: territorial concentration, which makes separation thinkable, and exclusion, which removes the reason not to seek it."),

 dict(q="Which of the following is the best example of a cultural variable acting as a CENTRIPETAL force in a diverse country?",
   choices=[
     "A widely used second language that lets speakers of many first languages conduct national business together",
     "A first language spoken by only one region",
     "A religion practised by a small minority",
     "An ethnic identity claimed by one province",
     "A dialect confined to a single valley"],
   ans=0,
   why="EK PSO-3.D.2 makes language a factor in centripetal forces, and a shared second language unifies without displacing anyone's first. The other options each name something confined to a part of the population, which cannot bind the whole."),

 dict(q="A geographer warns against predicting a country's stability from its cultural diversity alone. What is the strongest justification?",
   choices=[
     "Whether diversity acts centripetally or centrifugally depends on how institutions accommodate it, so the same diversity is compatible with unity or with division",
     "Cultural diversity has no political consequences",
     "Diverse countries are always unstable",
     "Diverse countries are always stable",
     "Cultural diversity cannot be measured"],
   ans=0,
   why="EK PSO-3.D.2 makes the three variables FACTORS in both kinds of force rather than causes of either. Counting languages predicts nothing on its own, because the same count is consistent with recognition and with suppression."),

 dict(q="Survey responses about what makes a region distinctive are shown. Using the table, which factor contributes most to the region's sense of place?",
   table=dict(
     headers=["Named as making the region distinctive", "Residents (%)", "Visitors (%)"],
     rows=[
       ["The regional language", "81", "74"],
       ["Religious observances and festivals", "58", "66"],
       ["Shared ethnic history", "47", "23"],
       ["Landscape and scenery", "39", "61"],
       ["Local economy", "12", "9"]]),
   choices=[
     "The regional language, named by 81 percent of residents and 74 percent of visitors, the only factor above 70 percent for both groups",
     "Landscape and scenery, since visitors name it far more often than residents do",
     "Shared ethnic history, since it shows the largest gap between the two groups",
     "Religious observances, since visitors name them more than residents do",
     "The local economy, since both groups name it least"],
   ans=0,
   why="Only one factor exceeds 70 percent in both columns, and the two columns are shares of two different groups rather than parts of one whole, so they do not sum to 100. EK PSO-3.D.1 names language, religion and ethnicity as the sources of a sense of place, and language leads both groups here."),

 dict(q="Language use is shown for two countries. Using the table, which country's language situation is more likely to generate centrifugal forces if one language is made the sole official one?",
   table=dict(
     headers=["Country", "Largest first language (%)", "Second largest (%)", "Third largest (%)", "All others (%)"],
     rows=[
       ["Country A", "93", "4", "2", "1"],
       ["Country B", "41", "29", "19", "11"]]),
   choices=[
     "Country B, where the largest language is spoken by only 41 percent and three other languages exceed 10 percent",
     "Country A, where one language dominates",
     "Country B, because it has fewer languages",
     "Country A, because 7 percent speak something else",
     "Neither, since official language policy has no effect"],
   ans=0,
   why="Both rows sum to 100, and one country's largest language covers 93 percent while the other's covers 41 with three further languages above 10. EK PSO-3.D.2 makes language a factor in both directions, and imposing a minority language on a majority is the case that divides."),

 dict(q="Religious composition is shown for three states. Using the table, which state's religious pattern is least likely to act as a centripetal force?",
   table=dict(
     headers=["State", "Largest tradition (%)", "Second tradition (%)", "Other or none (%)"],
     rows=[
       ["State 1", "88", "7", "5"],
       ["State 2", "49", "46", "5"],
       ["State 3", "71", "18", "11"]]),
   choices=[
     "State 2, where two traditions of nearly equal size divide the population almost in half",
     "State 1, where one tradition holds 88 percent",
     "State 3, where one tradition holds 71 percent",
     "State 1, because it has the smallest second tradition",
     "All three equally, since each has more than one tradition"],
   ans=0,
   why="Every row sums to 100, and one state pairs 49 percent with 46 percent while the others have a dominant tradition of 88 and 71 percent. EK PSO-3.D.2 names religion among the factors in centrifugal forces, and near-parity is the distribution that makes every institutional question a contest."),

 dict(q="Language recognition and separatist support are shown for four minority regions. Using the table, what relationship do the data suggest?",
   table=dict(
     headers=["Region", "Minority language recognized in schools and courts", "Support for separation (%)"],
     rows=[
       ["Region W", "Yes", "9"],
       ["Region X", "No", "44"],
       ["Region Y", "Yes", "13"],
       ["Region Z", "No", "38"]]),
   choices=[
     "Regions where the language is recognized average 11 percent support against 41 percent where it is not, which fits accommodation acting centripetally",
     "Recognition is associated with higher separatist support",
     "Recognition has no association with separatist support in these data",
     "All four regions show similar levels of support",
     "The data show that recognition causes separatism"],
   ans=0,
   why="The two recognized regions average 11 percent and the two unrecognized average 41, a gap of 30 points with no overlap between the groups. EK PSO-3.D.2 makes language a factor in both directions, and four regions cannot establish causation, which is why the key says the data fit the reading rather than prove it."),

 dict(q="Placemaking investment and a measure of residents' attachment are shown for four districts. Using the table, which district shows the strongest relationship between the two?",
   table=dict(
     headers=["District", "Placemaking projects completed", "Residents describing the district as distinctive (%)"],
     rows=[
       ["District 1", "0", "22"],
       ["District 2", "3", "41"],
       ["District 3", "7", "63"],
       ["District 4", "12", "78"]]),
   choices=[
     "Attachment rises at every step as projects increase, from 22 percent with none to 78 percent with twelve",
     "Attachment falls as projects increase",
     "Attachment is unrelated to the number of projects",
     "The district with no projects has the highest attachment",
     "Only the district with the most projects shows any attachment"],
   ans=0,
   why="Projects run 0, 3, 7 and 12 while the attachment figures run 22, 41, 63 and 78 percent, rising at every step with no reversal. EK PSO-3.D.1 says cultural patterns enhance placemaking, and four districts show an association rather than establishing that the projects caused it."),
]
