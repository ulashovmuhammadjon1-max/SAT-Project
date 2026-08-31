# AP COMPARATIVE GOVERNMENT AND POLITICS 5.8 Causes and Effects of Demographic
# Change
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding LEG-4 (demographic changes have political causes and
# consequences, and they can present challenges to a government's legitimacy);
# learning objective LEG-4.A. Suggested skill 3.E, Data Analysis (explain possible
# limitations of the data provided).
#
# Essential knowledge relied on:
#   LEG-4.A.1  GROWING POPULATIONS, CHANGING LAND USE AND VALUES, and ECONOMIC
#              OPPORTUNITIES motivate INTERNAL AND EXTERNAL POPULATION MOVEMENTS
#              (including RURAL TO URBAN SHIFTS and CHANGING NET MIGRATION RATES),
#              and the corresponding demographic changes POSE SIGNIFICANT CHALLENGES
#              TO GOVERNMENTAL RESOURCES
#   LEG-4.A.2  GOVERNMENT POLICIES AND EMPLOYMENT OPPORTUNITIES can DRAW WORKERS TO
#              DIFFERENT GEOGRAPHIC REGIONS or INFLUENCE POSITIVE OR NEGATIVE
#              MIGRATION RATES, often DEEPENING PREEXISTING CLASS AND REGIONAL
#              DIFFERENCES and TAXING GOVERNMENT RESOURCES:
#     .a CHINA's shift from agriculture to industry, SPECIAL ECONOMIC ZONES, the
#        ENCOURAGEMENT OF FOREIGN DIRECT INVESTMENT and FEWER GOVERNMENT RESTRICTIONS
#        have led to migration RURAL TO URBAN and WEST TO EAST (INTERIOR TO COAST),
#        creating a growing population whose RISING INCOMES ALLOW THEM TO PURSUE WORK
#        AND EDUCATIONAL OPPORTUNITIES ABROAD
#     .b HIGHLY SKILLED OR WELL-EDUCATED INDIVIDUALS HAVE LEFT home countries SUCH AS
#        IRAN AND NIGERIA TO ESCAPE GOVERNMENT POLICIES OR PRACTICES PERCEIVED AS
#        LIMITING, CORRUPT, OR REPRESSIVE
#     .c the NORTH AMERICAN FREE TRADE AGREEMENT and other economic liberalization
#        policies (SUCH AS REMOVING AGRICULTURAL SUBSIDIES), MAQUILADORA ZONES and
#        FOREIGN DIRECT INVESTMENT PATTERNS prompted migration RURAL TO URBAN and
#        SOUTHERN TO NORTHERN MEXICO, and contributed to GREATER ECONOMIC DEVELOPMENT
#        IN THE NORTH THAN IN THE SOUTH
#     .d a POSITIVE NET MIGRATION of immigrants into countries LIKE THE UNITED KINGDOM
#        has RESULTED IN SOCIAL AND POLITICAL TENSIONS
#   LEG-4.A.3  shifting migration patterns have consequences including .a INCREASED
#              CRIME STEMMING FROM HIGHER POPULATION DENSITY, .b the CONCENTRATION OF
#              HIGHLY SKILLED INDIVIDUALS IN CERTAIN AREAS AND THEIR ABSENCE IN
#              OTHERS, .c INCREASED USE OF EXISTING INFRASTRUCTURE AND HOUSING AND
#              DEMANDS FOR NEW AND EXPANDED INFRASTRUCTURE AND HOUSING, .d the GROWTH
#              OF NEW POLITICAL PARTIES THAT STAND AGAINST IMMIGRATION AND
#              SUPRANATIONAL ORGANIZATIONS THAT CHALLENGE THE GOVERNMENT'S LEGITIMACY
#   LEG-4.A.4  the political leadership of the UNITED KINGDOM faces increasing
#              constituent demands to REDUCE THE RISING COSTS OF HEALTH CARE,
#              exacerbated by an AGING POPULATION and a DECLINING WORKING-AGE
#              POPULATION faced with INCREASED TAX BURDENS to fund the UNIVERSAL
#              HEALTH CARE SYSTEM
#   LEG-4.A.5  states respond to demographic pressures with policies ENCOURAGING OR
#              DISCOURAGING THE BIRTH OF CHILDREN or actions PROMOTING OR DISCOURAGING
#              DISCRIMINATION AGAINST RELIGIOUS MINORITIES
#
# THE SUGGESTED SKILL FOR THIS TOPIC IS THE LIMITATIONS OF DATA, and that shapes
# the tables. Two of the nine data items ask what the table CANNOT establish rather
# than what it shows: a population table records how many people are in a place and
# not why, so it cannot separate migration from births and deaths (item 23), and a
# table of departures records that people left and not what they were escaping, so
# it cannot on its own establish EK LEG-4.A.2.b's stated motive (item 26). Those
# two items are the reason this module exists in the shape it does; a bank that
# only ever asks what a table shows never teaches the skill the CED names here.
#
# WHAT IS DELIBERATELY NOT ASSERTED: no migration figure, population count, health
# expenditure or election result of any real country. Every table is HYPOTHETICAL,
# labelled so, and attached to unnamed regions or occupational groups. The
# country-specific claims made are exactly the framework's own -- China's internal
# directions of movement, the departure of skilled people from Iran and Nigeria,
# Mexico's north-south development gap, positive net migration into the United
# Kingdom, and the United Kingdom's health care pressures -- all of them structural
# rather than numerical.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.8", "Causes and Effects of Demographic Change", 5)

_T_MIGR = dict(
    headers=["Region (hypothetical)", "Population at the start of the decade (thousands)",
             "Population at the end of the decade (thousands)"],
    rows=[["Coastal region", "8400", "12900"],
          ["Interior region", "11200", "9600"],
          ["Capital district", "3100", "4300"]])

_T_SKILLS = dict(
    headers=["Occupational group (hypothetical)", "People leaving the country in a year",
             "People entering the country in a year"],
    rows=[["Physicians", "1400", "260"],
          ["Engineers", "2100", "540"],
          ["Manual workers", "3200", "3900"]])

_T_HEALTH = dict(
    headers=["Year (hypothetical)", "People aged 65 and over (percent of the population)",
             "Working-age people for each person aged 65 and over",
             "Health spending per person (index)"],
    rows=[["Year 1", "14", "4.6", "100"],
          ["Year 2", "18", "3.5", "128"],
          ["Year 3", "23", "2.7", "161"]])

QUESTIONS = [
 dict(q="What does the framework identify as motivating internal and external population movements?",
   choices=[
     "growing populations, changing land use and values, and economic opportunities",
     "the decisions of supranational organizations",
     "changes in the boundaries between states",
     "the conditions attached to foreign loans",
     "the number of political parties contesting elections"], ans=0,
   why="EK LEG-4.A.1 states that growing populations, changing land use and values, and economic opportunities motivate internal and external population movements."),
 dict(q="What does the framework say the demographic changes accompanying those movements pose?",
   choices=[
     "significant challenges to governmental resources",
     "a threat to a country's international recognition",
     "an obstacle to holding elections at all",
     "a requirement to join a supranational organization",
     "no difficulty, since population is not a policy matter"], ans=0,
   why="EK LEG-4.A.1 states that the corresponding demographic changes pose significant challenges to governmental resources, which is why the topic sits under an enduring understanding about legitimacy."),
 dict(q="What does the framework say government policies and employment opportunities often deepen when they draw workers to different regions?",
   choices=[
     "preexisting class and regional differences",
     "the independence of the judiciary",
     "the number of chambers in the legislature",
     "a country's tariff schedule",
     "the powers of supranational organizations"], ans=0,
   why="EK LEG-4.A.2 states that government policies and employment opportunities can draw workers to different geographic regions or influence migration rates, often deepening preexisting class and regional differences and taxing government resources."),
 dict(q="Which directions of internal migration does the framework associate with China's economic changes?",
   choices=[
     "rural to urban, and west to east from the interior to the coast",
     "urban to rural, and east to west from the coast to the interior",
     "southern to northern regions only",
     "coastal regions to neighboring countries",
     "no internal migration at all"], ans=0,
   why="EK LEG-4.A.2.a states that China's shift from agriculture to industry, its special economic zones, its encouragement of foreign direct investment and its reduction of restrictions have led to migration from rural to urban areas and west to east, from the interior to the coast."),
 dict(q="What does the framework say the rising incomes of that growing population allow?",
   choices=[
     "the pursuit of work and educational opportunities abroad",
     "the purchase of agricultural land in the interior",
     "the founding of new political parties",
     "the acquisition of foreign citizenship by right",
     "an exemption from internal migration controls"], ans=0,
   why="EK LEG-4.A.2.a states that the growing population created by that movement has rising incomes that allow them to pursue work and educational opportunities abroad, which turns an internal movement into an external one."),
 dict(q="Which people does the framework say have left countries such as Iran and Nigeria, and why?",
   choices=[
     "highly skilled or well-educated individuals, to escape government policies or practices perceived as limiting, corrupt, or repressive",
     "agricultural laborers, to take seasonal work in neighboring states",
     "retired people, to obtain cheaper health care",
     "government officials, to avoid taxation",
     "students, under agreements with supranational organizations"], ans=0,
   why="EK LEG-4.A.2.b states that highly skilled or well-educated individuals have left home countries such as Iran and Nigeria to escape government policies or practices that are perceived as limiting, corrupt, or repressive."),
 dict(q="Which causes does the framework name for the migration it records within Mexico?",
   choices=[
     "the North American Free Trade Agreement and other liberalization policies such as removing agricultural subsidies, maquiladora zones, and foreign direct investment patterns",
     "the creation of special economic zones along a coast",
     "the departure of highly skilled individuals escaping repression",
     "a positive net migration of immigrants from abroad",
     "the imposition of austerity measures after a budget deficit"], ans=0,
   why="EK LEG-4.A.2.c names the North American Free Trade Agreement and other economic liberalization policies such as removing agricultural subsidies, maquiladora zones, and foreign direct investment patterns as what prompted migration from rural to urban areas and from southern to northern Mexico."),
 dict(q="What regional result does the framework attribute to those changes in Mexico?",
   choices=[
     "greater economic development in the north than in the south",
     "greater economic development in the south than in the north",
     "an equalization of development between the regions",
     "the depopulation of every urban area",
     "the closure of the country to foreign direct investment"], ans=0,
   why="EK LEG-4.A.2.c states that those changes contributed to greater economic development in the north than in the south, as well as other regional disparities."),
 dict(q="What does the framework say a positive net migration of immigrants into countries like the United Kingdom has resulted in?",
   choices=[
     "social and political tensions",
     "the abolition of the universal health care system",
     "a fall in the population of urban areas",
     "the withdrawal of foreign direct investment",
     "an equalization of regional development"], ans=0,
   why="EK LEG-4.A.2.d states that a positive net migration of immigrants into countries like the United Kingdom has resulted in social and political tensions."),
 dict(q="Which set of consequences does the framework attribute to shifting migration patterns?",
   choices=[
     "increased crime stemming from higher population density, the concentration of highly skilled individuals in some areas and their absence in others, heavier use of and demand for infrastructure and housing, and the growth of new parties standing against immigration and supranational organizations",
     "the redrawing of international boundaries and the loss of recognition",
     "the abolition of political parties and the suspension of elections",
     "the transfer of health policy to an international lender",
     "a reduction in the powers of regional governments"], ans=0,
   why="EK LEG-4.A.3 lists those four consequences of shifting migration patterns, and the fourth of them is stated as challenging the government's legitimacy."),
 dict(q="How does the framework describe the effect of migration on where highly skilled people are found?",
   choices=[
     "they become concentrated in certain areas and absent from others",
     "they are distributed evenly across every region",
     "they are confined to the region where they were trained",
     "they are unaffected by migration patterns",
     "they replace manual workers in every sector"], ans=0,
   why="EK LEG-4.A.3.b names the concentration of highly skilled individuals in certain areas and their absence in other areas as one of the consequences of shifting migration patterns."),
 dict(q="What kind of political organization does the framework say grows out of shifting migration patterns?",
   choices=[
     "new political parties that stand against immigration and supranational organizations and that challenge the government's legitimacy",
     "state-sanctioned peak associations representing economic sectors",
     "international financial organizations attaching conditions to loans",
     "supranational organizations with sovereign powers over member states",
     "interest groups organized around a single policy issue"], ans=0,
   why="EK LEG-4.A.3.d names the growth of new political parties that stand against immigration and supranational organizations that challenge the government's legitimacy, which is why demographic change belongs under an enduring understanding about legitimacy."),
 dict(q="Which combination does the framework say is behind the health care pressure on the political leadership of the United Kingdom?",
   choices=[
     "an aging population and a declining working-age population facing increased tax burdens to fund the universal health care system",
     "a falling number of people aged 65 and over and a growing working-age population",
     "the withdrawal of health care from public provision",
     "the transfer of health policy to a supranational organization",
     "a decline in the cost of providing health care"], ans=0,
   why="EK LEG-4.A.4 states that the political leadership of the United Kingdom faces increasing constituent demands to reduce the rising costs of health care, exacerbated by an aging population and a declining working-age population faced with increased tax burdens to fund the universal health care system."),
 dict(q="Which kinds of policy does the framework name as state responses to demographic pressures?",
   choices=[
     "policies encouraging or discouraging the birth of children, and actions promoting or discouraging discrimination against religious minorities",
     "policies raising or lowering tariffs and subsidies",
     "policies creating or abolishing political parties",
     "policies joining or leaving international financial organizations",
     "policies extending or shortening the terms of legislators"], ans=0,
   why="EK LEG-4.A.5 states that states respond to demographic pressures with different actions or policies that influence citizen behavior, including policies encouraging or discouraging the birth of children or actions promoting or discouraging discrimination against religious minorities."),
 dict(q="Which comparison of the framework's Chinese and Iranian examples is accurate?",
   choices=[
     "One describes movement within a country driven by where the work is, while the other describes people leaving a country to escape how it is governed",
     "Both describe people leaving a country to escape how it is governed",
     "Both describe movement within a country driven by employment",
     "One describes immigration into a country and the other emigration from it",
     "Neither country's population movements are described by the framework"], ans=0,
   why="EK LEG-4.A.2.a attributes movement from rural to urban areas and interior to coast in China to economic changes, while EK LEG-4.A.2.b attributes the departure of highly skilled individuals from countries such as Iran to policies or practices perceived as limiting, corrupt, or repressive."),
 dict(q="Which comparison of the framework's Chinese and Mexican examples is accurate?",
   choices=[
     "Both record rural to urban movement alongside a movement toward one part of the country, driven in each case by where liberalization drew investment and work",
     "Both record movement away from the areas receiving foreign investment",
     "Neither records rural to urban movement",
     "One records movement toward the interior and the other toward the south",
     "Both record a positive net migration of immigrants from abroad"], ans=0,
   why="EK LEG-4.A.2.a records rural to urban and west to east movement in China following special economic zones and foreign direct investment, and EK LEG-4.A.2.c records rural to urban and southern to northern movement in Mexico following liberalization policies, maquiladora zones and foreign direct investment patterns."),
 dict(q="A country finds that a large share of its trained doctors and engineers now work abroad and that the regions they left have few replacements. Which framework claims does this most directly illustrate?",
   choices=[
     "the departure of highly skilled individuals, together with their concentration in certain areas and absence in others",
     "increased crime stemming from higher population density",
     "the growth of new parties standing against immigration",
     "policies encouraging or discouraging the birth of children",
     "a positive net migration of immigrants into the country"], ans=0,
   why="EK LEG-4.A.2.b records highly skilled or well-educated individuals leaving their home countries, and EK LEG-4.A.3.b names the resulting concentration of such individuals in certain areas and their absence in others."),
 dict(q="After a decade of rising immigration, a new party wins seats on a platform opposing immigration and the country's membership of a regional body, arguing the government has lost the right to govern. Which framework claim does this illustrate?",
   choices=[
     "the growth of new political parties that stand against immigration and supranational organizations and challenge the government's legitimacy",
     "the concentration of highly skilled individuals in certain areas",
     "increased use of existing infrastructure and housing",
     "policies discouraging discrimination against religious minorities",
     "the departure of well-educated individuals escaping repression"], ans=0,
   why="EK LEG-4.A.3.d names the growth of new political parties that stand against immigration and supranational organizations that challenge the government's legitimacy, and the scenario contains all three elements of that statement."),
 dict(q="A city's transport system and housing stock are strained by new arrivals, and residents press for both to be expanded. Which framework claim does this illustrate?",
   choices=[
     "increased use of existing infrastructure and housing and demands for new and expanded infrastructure and housing",
     "increased crime stemming from higher population density",
     "the absence of highly skilled individuals from certain areas",
     "the growth of parties standing against supranational organizations",
     "actions promoting or discouraging discrimination against religious minorities"], ans=0,
   why="EK LEG-4.A.3.c names increased use of existing infrastructure and housing and demands for new and expanded infrastructure and housing among the consequences of shifting migration patterns."),
 dict(q="Which finding would most strongly support a claim that demographic change is straining a government's resources in the way the framework describes?",
   choices=[
     "The population of one region grew by a third in a decade while the budgets for its schools, clinics and transport were unchanged and waiting lists lengthened",
     "The population of every region remained stable and public services were unchanged",
     "The government raised tariffs on imported manufactured goods",
     "The government privatized several state-owned companies",
     "The country's international boundaries were formally recognized"], ans=0,
   why="EK LEG-4.A.1 states that demographic changes pose significant challenges to governmental resources and EK LEG-4.A.2 that such movements tax government resources, so the supporting finding has to pair a population change with a strain on provision."),
 dict(q="The table reports hypothetical populations for three regions of one country. Which region gained the most people over the decade?",
   table=_T_MIGR,
   choices=[
     "the coastal region, which gained 4500 thousand",
     "the capital district, which gained 1200 thousand",
     "the interior region, which gained 1600 thousand",
     "none of them, since every region lost population",
     "all three equally"], ans=0,
   why="EK LEG-4.A.2.a records migration from the interior toward the coast, so the comparison is the kind the framework describes, and subtracting each region's earlier figure from its later one shows which gained most."),
 dict(q="According to the same table of regions, the net change in the three regions' combined population is",
   table=_T_MIGR,
   choices=[
     "an increase of 4100 thousand",
     "an increase of 5700 thousand",
     "an increase of 4500 thousand",
     "an increase of 2900 thousand",
     "an increase of 1200 thousand"], ans=0,
   why="Adding the three regions' changes, including the one that is negative, gives the net change. The alternatives come from adding only the gains, from taking the largest single gain, from netting only the two extreme regions, and from taking the smallest gain."),
 dict(q="A student uses the same table to argue that migration into the coastal region caused its growth. What is the strongest objection to that use of the data?",
   table=_T_MIGR,
   choices=[
     "The table records how many people were in each region, not why the numbers changed, so it cannot separate migration from births and deaths",
     "The table covers only three regions, so no conclusion about any of them is possible",
     "The table gives populations in thousands, which is too coarse to support any conclusion",
     "The table has no column showing tariffs, so economic causes cannot be considered",
     "There is no objection, since a population increase can only come from migration"], ans=0,
   why="EK LEG-4.A.1 names growing populations as one motivation for movement and also as a demographic change in its own right, so a population total reflects natural change as well as migration, and the table records neither cause."),
 dict(q="The table reports hypothetical annual movements of three occupational groups. Which group shows the largest net loss?",
   table=_T_SKILLS,
   choices=[
     "engineers, with a net loss of 1560",
     "physicians, with a net loss of 1140",
     "manual workers, with a net loss of 700",
     "engineers, with a net loss of 2100",
     "physicians, with a net loss of 3200"], ans=0,
   why="EK LEG-4.A.2.b records highly skilled or well-educated individuals leaving their home countries, and subtracting each group's arrivals from its departures gives the net figure for each."),
 dict(q="According to the same table of occupational groups, the total number of people leaving the country in a year is",
   table=_T_SKILLS,
   choices=[
     "6700",
     "4700",
     "5300",
     "3500",
     "11400"], ans=0,
   why="Adding the departure column across the three groups gives the total. The alternatives are the other column's total, the total with the smallest group omitted, the two smallest groups added, and the two columns added together."),
 dict(q="A student uses the same table to conclude that skilled workers are leaving to escape government practices they regard as repressive. What is the strongest objection?",
   table=_T_SKILLS,
   choices=[
     "The table records how many people moved in each direction but nothing about their reasons, so it cannot establish any motive",
     "The table covers only three occupational groups, so no conclusion about any of them is possible",
     "The table reports a single year, so the numbers must be wrong",
     "The table gives no information about tariffs, so economic explanations are ruled out",
     "There is no objection, since departures can only be explained by repression"], ans=0,
   why="EK LEG-4.A.2.b attributes the departure of highly skilled individuals to policies or practices perceived as limiting, corrupt, or repressive, but that is a claim about motive, and a table of arrivals and departures records movement rather than reasons."),
 dict(q="The table follows one hypothetical country over three years. Which conclusion does it support?",
   table=_T_HEALTH,
   choices=[
     "The share of people aged 65 and over rose, the number of working-age people supporting each of them fell, and health spending per person rose",
     "The share of people aged 65 and over fell while health spending per person rose",
     "The number of working-age people supporting each older person rose across the period",
     "Health spending per person was unchanged across the period",
     "All three columns moved in the same direction"], ans=0,
   why="EK LEG-4.A.4 attributes rising health care costs to an aging population and a declining working-age population, and the table's three columns move exactly as that statement describes."),
 dict(q="According to the same table of three years, the rise in the share of people aged 65 and over is",
   table=_T_HEALTH,
   choices=[
     "9 percentage points",
     "5 percentage points",
     "4 percentage points",
     "23 percentage points",
     "61 percentage points"], ans=0,
   why="Subtracting the first year's share from the third year's gives the rise. The alternatives are the rises between the other pairs of years, the final share read as a rise, and the change in the spending index read as though it were a share."),
 dict(q="Using the same table of three years, the rise in health spending per person is",
   table=_T_HEALTH,
   choices=[
     "61 points",
     "33 points",
     "28 points",
     "100 points",
     "9 points"], ans=0,
   why="Subtracting the first year's index from the third year's gives the rise. The alternatives are the rises between the other pairs of years, the index's own starting value read as a rise, and the change in the age column read as though it belonged to this one."),
 dict(q="Taking EK LEG-4.A as a whole, which summary is most accurate?",
   choices=[
     "Population moves because of growth, changing land use and values, and where the work is; government policy shapes those flows and often widens class and regional gaps; the consequences run from crowded infrastructure and uneven distribution of skills to new parties that challenge a government's legitimacy; and states answer with policies reaching into birth rates and the treatment of minorities",
     "Population movement is driven entirely by government policy and has no economic causes",
     "Demographic change affects public services but has no political consequences",
     "Only immigration between countries has political effects; internal movement does not",
     "Governments have no policy responses available to demographic pressure"], ans=0,
   why="EK LEG-4.A.1 supplies the motivations and the strain on governmental resources, EK LEG-4.A.2 the role of policy and the deepening of class and regional differences, EK LEG-4.A.3 the four consequences including the challenge to legitimacy, and EK LEG-4.A.5 the range of state responses."),
]
