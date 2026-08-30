# AP HUMAN GEOGRAPHY 2.10 Causes of Migration -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding IMP-2; learning
# objective IMP-2.C, "Explain how different causal factors encourage migration."
#
# Essential knowledge, in full -- two statements, and the second is a closed
# list that the whole module is built on:
#   IMP-2.C.1  Migration is commonly divided into push factors and pull factors.
#   IMP-2.C.2  Push/pull factors and intervening opportunities/obstacles can be
#              cultural, demographic, economic, environmental, or political.
#
# IMP-2.C.2 does two things at once and both are examinable. It introduces
# INTERVENING OPPORTUNITIES and INTERVENING OBSTACLES as a second axis alongside
# push and pull, and it supplies FIVE categories -- cultural, demographic,
# economic, environmental, political -- that apply to all four of those terms.
# A question in this topic therefore has two independent answers available for
# any migration: which of the four roles a factor plays, and which of the five
# categories it belongs to. Items 12, 16, 21 and 28 ask for both at once,
# because that is how the real exam asks it.
#
# The four roles, as this module uses them:
#   push factor            a condition AT THE ORIGIN driving people away
#   pull factor            a condition AT THE DESTINATION drawing people in
#   intervening obstacle   something BETWEEN origin and destination that
#                          hinders or prevents the move -- a mountain range, an
#                          ocean, a closed border, a visa regime, the cost of
#                          the journey
#   intervening opportunity  something BETWEEN them that causes a migrant to
#                          stop short of the intended destination, most often a
#                          job or a community found on the way
#
# The distinction students most reliably lose, and the reason items 8, 14, 20
# and 27 exist: an obstacle STOPS or slows a migrant; an opportunity DIVERTS
# one. Both sit between origin and destination and neither is a push or a pull.
#
# One further discipline the module observes. Push and pull are usually two
# descriptions of the same difference -- no work at home and work elsewhere --
# so an item asking which one is at work must supply enough detail to decide
# where the condition is located. Items 3, 5 and 24 are written that way on
# purpose.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_10.py. FIVE choices (A-E).
TOPIC = ("2.10", "Causes of Migration", 2)

QUESTIONS = [
 dict(q="How is migration 'commonly divided' in the framework's own words?",
   choices=[
     "Into push factors and pull factors",
     "Into voluntary and forced movement",
     "Into internal and international movement",
     "Into permanent and temporary movement",
     "Into rural and urban movement"],
   ans=0,
   why="EK IMP-2.C.1 states that migration is commonly divided into push factors and pull factors. The other four distinctions are real and appear elsewhere in this unit, but none of them is the division this statement names."),

 dict(q="Which list gives the five categories the framework assigns to push, pull, and intervening factors?",
   choices=[
     "Cultural, demographic, economic, environmental, and political",
     "Cultural, economic, historical, political, and religious",
     "Economic, environmental, linguistic, political, and social",
     "Demographic, economic, environmental, physical, and technological",
     "Cultural, economic, environmental, political, and urban"],
   ans=0,
   why="EK IMP-2.C.2 prints exactly this list of five and applies it to push and pull factors and to intervening opportunities and obstacles alike. Every distractor swaps in a plausible category the statement does not contain."),

 dict(q="A family leaves a district where the harvest has failed for three consecutive years. In their decision, the failed harvests are",
   choices=[
     "An environmental push factor, since the condition is at the origin and concerns the physical environment",
     "An environmental pull factor, since it draws them elsewhere",
     "An intervening obstacle, since it stands in their way",
     "An economic pull factor, since they seek income",
     "A political push factor, since agriculture is regulated"],
   ans=0,
   why="EK IMP-2.C.1's push factors are conditions at the origin, and EK IMP-2.C.2 supplies environmental as one of the five categories. Repeated crop failure is a physical condition of the place being left, which fixes both the role and the category."),

 dict(q="A city advertises well-paid work in its construction industry, and workers arrive from several regions. The advertised work is",
   choices=[
     "An economic pull factor, since it is a condition at the destination that attracts migrants",
     "An economic push factor, since it concerns wages",
     "An intervening opportunity, since the workers pass other cities",
     "A demographic pull factor, since it changes population",
     "A cultural pull factor, since construction is an occupation"],
   ans=0,
   why="EK IMP-2.C.1 distinguishes push from pull by where the condition sits, and this one sits at the destination. EK IMP-2.C.2's economic category covers work and wages, which makes the classification complete on both axes."),

 dict(q="What distinguishes a push factor from a pull factor?",
   choices=[
     "A push factor is a condition at the place of origin; a pull factor is a condition at the destination",
     "A push factor is economic and a pull factor is cultural",
     "A push factor applies to forced migration and a pull factor to voluntary migration",
     "A push factor is temporary and a pull factor is permanent",
     "A push factor affects individuals and a pull factor affects whole societies"],
   ans=0,
   why="EK IMP-2.C.1's division is spatial: the two terms name where a condition is located relative to the migrant's move. EK IMP-2.C.2 then applies all five categories to both, so neither term is tied to a particular kind of cause."),

 dict(q="A mountain range that migrants must cross, a sea they must pay to be carried over, and a border requiring a visa they cannot obtain are all examples of",
   choices=[
     "Intervening obstacles, since each lies between origin and destination and hinders the move",
     "Push factors, since each makes leaving harder",
     "Pull factors, since each lies near the destination",
     "Intervening opportunities, since each offers a chance to stop",
     "Demographic factors, since each affects population movement"],
   ans=0,
   why="EK IMP-2.C.2 names intervening obstacles as a category alongside push and pull. What unites the three examples is position -- between the two ends of the move -- and effect, which is to hinder rather than to attract or repel."),

 dict(q="A worker sets out for a distant capital but finds steady employment in a market town two days along the route and settles there. The market town's job is",
   choices=[
     "An intervening opportunity, since it lay between origin and intended destination and ended the journey early",
     "An intervening obstacle, since it stopped the migration",
     "A pull factor of the capital",
     "A push factor of the origin",
     "A demographic factor, since it changed a population"],
   ans=0,
   why="EK IMP-2.C.2 names intervening opportunities as a distinct role, and the diagnostic is diversion rather than obstruction. The job did not prevent the move; it satisfied the reason for it before the intended destination was reached."),

 dict(q="Which statement correctly distinguishes an intervening obstacle from an intervening opportunity?",
   choices=[
     "An obstacle hinders or prevents the move; an opportunity diverts the migrant to a nearer destination",
     "An obstacle is physical and an opportunity is economic",
     "An obstacle occurs at the origin and an opportunity at the destination",
     "An obstacle affects forced migrants and an opportunity affects voluntary ones",
     "The two terms mean the same thing"],
   ans=0,
   why="Both lie between origin and destination, so position cannot separate them and the difference has to be in effect. EK IMP-2.C.2 lists them as a pair precisely because they are the two ways the space between two places can alter a migration."),

 dict(q="A government revokes the citizenship of an ethnic minority, and members of that group leave the country. The revocation is",
   choices=[
     "A political push factor, since a state action at the origin drives people out",
     "A cultural pull factor, since the group shares an identity",
     "An intervening obstacle, since citizenship is required to travel",
     "A demographic push factor, since it reduces the population",
     "An economic push factor, since citizenship affects employment"],
   ans=0,
   why="EK IMP-2.C.2's political category covers the acts of states, and EK IMP-2.C.1's push factors are conditions at the origin. That the consequence includes economic and demographic effects does not change what kind of factor the revocation itself is."),

 dict(q="Young adults leave a rural district because almost everyone their own age has already gone and there is no one left to marry or work alongside. This is best classified as",
   choices=[
     "A demographic push factor, since the composition of the origin's population is itself the reason for leaving",
     "An economic push factor, since employment is involved",
     "A cultural pull factor, since marriage is a cultural practice",
     "An intervening opportunity, since other districts are nearer",
     "A political push factor, since districts are governed"],
   ans=0,
   why="EK IMP-2.C.2 lists demographic among the five categories, and this is what that category is for: the number and age composition of the people already there. Prior migration has thinned the cohort itself, which is a demographic condition rather than an economic one."),

 dict(q="A country's language and religion are shared by a large established community in a particular foreign city, and migrants from that country choose it over closer alternatives. The community is",
   choices=[
     "A cultural pull factor, since shared language and religion at the destination attract migrants",
     "A cultural push factor, since it concerns the migrants' own culture",
     "An intervening obstacle, since it lies between other destinations",
     "A demographic pull factor, since the community is a population",
     "An economic pull factor, since migrants seek work"],
   ans=0,
   why="EK IMP-2.C.2's cultural category and EK IMP-2.C.1's pull role combine here: the condition is at the destination and it concerns language, religion and belonging. Choosing a further city over a nearer one is what shows the cultural factor outweighing distance."),

 dict(q="Rising sea level makes a low-lying island's fields too saline to farm and its wells brackish, and households move to the mainland. Classify the cause by role and by category.",
   choices=[
     "An environmental push factor",
     "An environmental pull factor",
     "An economic intervening obstacle",
     "A political push factor",
     "A demographic pull factor"],
   ans=0,
   why="The condition is at the origin, which makes it a push under EK IMP-2.C.1, and it is a physical change in the environment, which places it in EK IMP-2.C.2's environmental category. Both axes have to be answered, and this option is the only one correct on each."),

 dict(q="Why do geographers say that push and pull factors usually operate together rather than singly?",
   choices=[
     "A migrant compares conditions at two places, so a decision to move requires both something to leave and somewhere better to go",
     "Push factors always cause pull factors",
     "Only push factors actually cause migration",
     "Only pull factors actually cause migration",
     "The two terms describe unrelated processes"],
   ans=0,
   why="EK IMP-2.C.1 divides the factors into two halves of a single comparison, and a comparison needs both terms. Unemployment at home is a reason to leave only if work exists somewhere reachable, which is why lists of causes rarely name just one side."),

 dict(q="A migrant intending to reach a distant country is stopped by the cost of the journey and remains in a nearby city instead. Which two roles are involved?",
   choices=[
     "An intervening obstacle, the cost, and an intervening opportunity, the nearby city where the migrant settles",
     "Two intervening obstacles",
     "Two pull factors",
     "A push factor and a pull factor only",
     "Neither an obstacle nor an opportunity"],
   ans=0,
   why="EK IMP-2.C.2 names both terms, and the case contains one of each: the cost hinders the intended move and the nearer city absorbs the migrant instead. Separating them matters because they act on the same journey in opposite ways."),

 dict(q="Which is the strongest reason a single condition can be a push factor for one household and not for another in the same village?",
   choices=[
     "Households differ in resources, obligations, and alternatives, so the same condition weighs differently in each decision",
     "Push factors apply only to individuals, never to households",
     "Conditions are measured differently for different households",
     "Only economic conditions can be push factors",
     "A condition is a push factor for everyone or for no one"],
   ans=0,
   why="EK IMP-2.C.1's factors enter a decision rather than determine one, so the same drought or wage level is weighed against different assets, ties and options. That is why migration from a village is selective rather than total."),

 dict(q="A war destroys housing and infrastructure and families flee across a border. Which classification is most complete?",
   choices=[
     "A political push factor with environmental and economic consequences, since the war is a state and armed-group action at the origin",
     "An environmental push factor, since buildings were destroyed",
     "An economic pull factor of the receiving country",
     "An intervening obstacle, since the border was crossed",
     "A demographic push factor, since population fell"],
   ans=0,
   why="EK IMP-2.C.2's five categories classify the FACTOR rather than its consequences, and the factor here is organized violence, which is political. Naming the consequences separately is what makes the classification complete rather than confused."),

 dict(q="A country introduces a work-visa quota that admits only a fraction of applicants. For those refused, the quota is",
   choices=[
     "A political intervening obstacle, since a state rule stands between them and the destination",
     "A political pull factor, since visas are desirable",
     "An economic push factor, since work is involved",
     "An intervening opportunity, since some applicants are admitted",
     "A cultural obstacle, since applicants come from another country"],
   ans=0,
   why="EK IMP-2.C.2 applies the five categories to intervening obstacles as well as to push and pull factors. A quota is a rule made by a state that sits between the migrant and the destination, which fixes both the role and the category."),

 dict(q="Which of these is best described as a demographic PULL factor?",
   choices=[
     "A destination with a shortage of workers in the ages the migrants belong to, so arrivals are readily absorbed",
     "A destination offering higher wages than the origin does",
     "A destination in which the migrants' own language is widely spoken",
     "An origin in which the harvest has failed three years running",
     "A border crossing that requires a visa the migrant cannot obtain"],
   ans=0,
   why="EK IMP-2.C.2's demographic category concerns the composition of a population rather than its wages or its culture. A gap in a destination's own age structure is a demographic condition at the destination, which makes it demographic and a pull at once."),

 dict(q="Which pairing of a factor with its correct role is INCORRECT?",
   choices=[
     "Political persecution in the country a migrant is leaving, classified as a pull factor",
     "A desert crossing on the route, classified as an intervening obstacle",
     "Higher wages in the destination city, classified as a pull factor",
     "Drought in the home district, classified as a push factor",
     "A job found halfway along the route, classified as an intervening opportunity"],
   ans=0,
   why="EK IMP-2.C.1 fixes push and pull by location, and persecution in the country being left is at the origin, which makes it a push factor. The other four pairings each place the condition correctly relative to the move."),

 dict(q="A geographer argues that improved roads and cheap bus services have increased migration from a rural region. In the framework's terms, what has changed?",
   choices=[
     "An intervening obstacle has weakened, so moves that were previously too costly or slow now happen",
     "A push factor at the origin has strengthened",
     "A pull factor at the destination has strengthened",
     "An intervening opportunity has appeared",
     "The five categories no longer apply"],
   ans=0,
   why="EK IMP-2.C.2 makes obstacles a factor in their own right, and distance, cost and time are among the commonest of them. Nothing at either end of the move has changed here; what changed is what lies between them."),

 dict(q="Migrants from one country settle overwhelmingly in a single neighbourhood of a destination city, near earlier arrivals from the same region. Which classification best fits the earlier arrivals?",
   choices=[
     "A cultural pull factor, since an existing community supplies language, contacts, housing, and work information",
     "A demographic push factor of the origin",
     "An intervening obstacle for later migrants",
     "An environmental pull factor of the neighbourhood",
     "A political pull factor of the destination state"],
   ans=0,
   why="EK IMP-2.C.2's cultural category covers shared language, kinship and community, and the condition sits at the destination, which makes it a pull. An established community lowers the real cost of arriving, which is why later migrants concentrate where earlier ones did."),

 dict(q="Which of the following is an ENVIRONMENTAL pull factor rather than an environmental push factor?",
   choices=[
     "A warm, dry climate that attracts retirees to a particular region",
     "A drought that empties a farming district",
     "A flood that destroys a village",
     "Soil exhaustion that ends cultivation",
     "A hurricane that destroys coastal housing"],
   ans=0,
   why="EK IMP-2.C.1 fixes the role by where the condition is, and only one option describes a physical condition at a place people are moving TO. The other four are physical conditions at places people are moving FROM, which makes them pushes."),

 dict(q="Why does the framework apply the same five categories to push factors, pull factors, obstacles, and opportunities?",
   choices=[
     "Because the cause of a migration and the thing standing in its way can each be cultural, demographic, economic, environmental, or political",
     "Because all four terms mean the same thing",
     "Because only economic factors matter in practice",
     "Because the categories apply only to push factors and the CED lists them once for brevity",
     "Because obstacles are always physical and the list is therefore redundant"],
   ans=0,
   why="EK IMP-2.C.2 explicitly attaches the five categories to push and pull factors AND to intervening opportunities and obstacles. Treating obstacles as always physical is the misreading the statement forecloses, since a visa regime and a war zone are political obstacles."),

 dict(q="A student writes that 'poverty causes migration.' Why is this an incomplete account in the framework's terms?",
   choices=[
     "It names a condition at the origin without saying what is available elsewhere or what lies between, and the poorest people often cannot afford to move at all",
     "Poverty is not a real cause of migration",
     "Poverty is a pull factor rather than a push factor",
     "Poverty is an intervening obstacle rather than a push factor",
     "The statement is complete as written"],
   ans=0,
   why="EK IMP-2.C.1 divides causes into two halves and EK IMP-2.C.2 adds what lies between, so a one-term account leaves out both. It also runs into the cost of the journey, which is an intervening obstacle that rises in importance exactly as income falls."),

 dict(q="A regional government offers relocation grants, housing, and guaranteed school places to families willing to move to a depopulating district. These measures are",
   choices=[
     "Deliberately created pull factors, chiefly economic, aimed at reversing an existing flow",
     "Push factors of the depopulating district",
     "Intervening obstacles for families already there",
     "Demographic push factors, since population has fallen",
     "Cultural pull factors, since the district has traditions"],
   ans=0,
   why="EK IMP-2.C.1's pull factors are conditions at the destination, and a grant, a house and a school place are exactly that for the district being moved to. EK IMP-2.C.2's economic category covers the money and the housing, which is what the package mostly consists of."),

 dict(q="Survey responses on reasons for leaving are shown for one region. Using the table, which category of push factor dominates, and by how much?",
   table=dict(
     headers=["Main reason given for leaving", "Respondents"],
     rows=[
       ["No work available locally", "1,840"],
       ["Repeated crop failure and water shortage", "760"],
       ["Fear of violence or persecution", "410"],
       ["To join family already elsewhere", "620"],
       ["No one of my own age left in the village", "370"]]),
   choices=[
     "Economic reasons, given by 1,840 of 4,000 respondents, more than twice the next largest category",
     "Environmental reasons, given by 760 of 4,000 respondents",
     "Political reasons, given by 410 of 4,000 respondents",
     "Cultural reasons, given by 620 of 4,000 respondents",
     "Demographic reasons, given by 370 of 4,000 respondents"],
   ans=0,
   why="The five reasons map one to one onto the framework's five categories, and 1,840 of the 4,000 responses fall in the economic one against 760 for the next largest. That the economic share exceeds twice the runner-up is what the question asks to be checked."),

 dict(q="Migrants leaving one origin were asked where they intended to go and where they actually settled. Using the table, what does the comparison show?",
   table=dict(
     headers=["Destination", "Distance from origin (km)", "Intended to settle there", "Actually settled there"],
     rows=[
       ["Market town", "60", "300", "1,900"],
       ["Provincial city", "240", "1,700", "1,600"],
       ["National capital", "900", "3,000", "1,500"]]),
   choices=[
     "Settlement shifted sharply toward the nearest destination, which is the pattern intervening opportunities produce",
     "Settlement matched intentions exactly at every destination",
     "Settlement shifted toward the most distant destination",
     "Intentions and outcomes differed only for the provincial city",
     "The table shows an intervening obstacle rather than an opportunity"],
   ans=0,
   why="The nearest destination gains 1,600 settlers over intentions while the most distant loses 1,500, and the middle one barely moves. Migrants stopping short of an intended destination at a nearer place is the definition of an intervening opportunity."),

 dict(q="Wage levels at an origin and three possible destinations are shown along with the cost of reaching each. Using the table, which destination offers the largest net gain in the first year?",
   table=dict(
     headers=["Place", "Annual wage (US$)", "One-off cost of moving there (US$)"],
     rows=[
       ["Origin", "1,200", "0"],
       ["Destination 1", "3,000", "400"],
       ["Destination 2", "5,200", "3,000"],
       ["Destination 3", "4,000", "900"]]),
   choices=[
     "Destination 3, with a first-year net gain of 1,900 dollars",
     "Destination 2, with the highest wage in the table",
     "Destination 1, with the lowest cost of moving",
     "Destination 2, with a first-year net gain of 4,000 dollars",
     "All three are equal once the cost of moving is subtracted"],
   ans=0,
   why="Subtracting the origin wage and then the moving cost gives net gains of 1,400, 1,000 and 1,900 dollars, so the highest-wage destination is not the best first-year outcome. The cost of the journey is an intervening obstacle and it changes the ranking."),

 dict(q="Applications and admissions under a destination country's visa categories are shown. Using the table, which category functions as the strongest intervening obstacle?",
   table=dict(
     headers=["Visa category", "Applications", "Admissions"],
     rows=[
       ["Skilled worker", "40,000", "22,000"],
       ["Seasonal agricultural", "18,000", "16,200"],
       ["Family reunification", "25,000", "12,500"],
       ["Humanitarian protection", "20,000", "2,400"]]),
   choices=[
     "Humanitarian protection, which admits 12 percent of applicants",
     "Skilled worker, which refuses the largest number of applicants",
     "Family reunification, which admits half of applicants",
     "Seasonal agricultural, which receives the fewest applications",
     "All four are equal obstacles, since each refuses some applicants"],
   ans=0,
   why="Admission rates are 55, 90, 50 and 12 percent, so the category refusing the largest NUMBER of applicants is not the one hardest to pass. An obstacle is measured by the chance it blocks a given migrant, which is a rate rather than a count."),

 dict(q="Net migration and two possible causes are shown for four districts. Using the table, which district's outflow is least well explained by wages alone?",
   table=dict(
     headers=["District", "Average wage relative to national (%)", "Years since last major flood", "Net migration rate (per 1,000)"],
     rows=[
       ["District A", "72", "11", "-14"],
       ["District B", "68", "9", "-16"],
       ["District C", "94", "1", "-21"],
       ["District D", "88", "14", "-4"]]),
   choices=[
     "District C, whose wages are near the national average yet whose outflow is the largest, and which flooded last year",
     "District A, whose wages are the lowest in the table",
     "District B, whose outflow is the second largest",
     "District D, whose outflow is the smallest",
     "None of them, since wages explain all four outflows"],
   ans=0,
   why="Wages of 72, 68, 94 and 88 percent line up with outflows of 14, 16, 4 and 21 per 1,000 for three districts but not the fourth, which has near-average wages and the largest outflow. Its flood the previous year points to an environmental push factor the wage column cannot capture."),
]
