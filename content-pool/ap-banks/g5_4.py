# AP HUMAN GEOGRAPHY 5.4 The Second Agricultural Revolution -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding SPS-5, "Agriculture
# has changed over time because of cultural diffusion and advances in
# technology." Learning objective SPS-5.C, "Explain the advances and impacts of
# the second agricultural revolution."
#
# Essential knowledge -- ONE statement, and it is a causal chain:
#   SPS-5.C.1  New technology and increased food production in the second
#              agricultural revolution led to better diets, longer life
#              expectancies, and more people available for work in factories.
#
# READ THE SENTENCE AS A CHAIN, because that is how it is built:
#
#   new technology  ->  more food produced  ->  better diets
#                                           ->  longer life expectancies
#                                           ->  more people available for
#                                               factory work
#
# The three consequences are not a list of unrelated results. Better diets are
# WHY life expectancy rose, and rising output per farm worker is WHY people
# became available to work somewhere other than a farm. Items 5, 11, 15, 21 and
# 29 are built on the links rather than on the endpoints, which is what the
# learning objective's word "impacts" asks for.
#
# THE DIRECTION OF THE LAST LINK is the one students reverse. The CED says
# increased food production LED TO more people being AVAILABLE for factory work.
# It does not say factories drew people off the land, and it does not say
# farming collapsed. Output per farm worker rose, so fewer workers were needed to
# feed the same population and the surplus could do something else. Items 11, 15
# and 19 key against the reversed reading, and item 19 states explicitly what the
# sentence does NOT claim.
#
# WHAT THE CED DOES NOT NAME: any specific technology, any date, any country.
# The technologies used here are the standard ones for this revolution -- the
# seed drill, four-course rotation replacing bare fallow, selective breeding of
# livestock, consolidation of scattered strips into compact enclosed farms, and
# the mechanical reaper and thresher. Each item keys on the MECHANISM by which
# the device raises output, never on a date, an inventor or a place, because the
# mechanism is what the CED's "new technology and increased food production"
# actually asserts and the rest would be content the framework does not carry.
#
# THE NEIGHBOURING TOPICS this is most often confused with, and how each item
# separates them: the FIRST agricultural revolution is domestication, which is
# Topic 5.3's SPS-5.A.1 (item 16); the GREEN REVOLUTION is Topic 5.5's SPS-5.D.1,
# a twentieth-century package of high-yield seeds, chemicals and mechanized
# farming in the developing world (item 17). Both are on the list of things a
# student must be able to tell apart from this one.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.4", "The Second Agricultural Revolution", 5)

QUESTIONS = [
 dict(q="Which three impacts does the framework attribute to the second agricultural revolution?", choices=[
   "Better diets, longer life expectancies, and more people available for work in factories",
   "High-yield seeds, increased chemical use, and mechanized farming",
   "Domestication of plants, domestication of animals, and the founding of villages",
   "Suburbanization, deindustrialization, and outsourcing",
   "Better diets, higher birth rates, and a return of workers to the land"], ans=0,
   why="EK SPS-5.C.1 names exactly these three impacts. High-yield seeds, chemicals and mechanization are the Green Revolution's characteristics in EK SPS-5.D.1, and domestication belongs to EK SPS-5.A.1, so both of those describe different revolutions."),

 dict(q="According to the framework, what produced the impacts of the second agricultural revolution?", choices=[
   "New technology and increased food production",
   "A fall in the number of people needing to be fed",
   "The abandonment of farming across whole regions",
   "The domestication of new species of plants and animals",
   "The introduction of high-yield seed varieties in the developing world"], ans=0,
   why="EK SPS-5.C.1 identifies new technology and increased food production as the cause of the three impacts it names. The causal order in the sentence runs from technology through output to the social consequences, and it never runs the other way."),

 dict(q="A seed drill places seed at an even depth in rows instead of scattering it by hand. Why does that raise output?", choices=[
   "Far less seed is wasted and a much larger share of it germinates, so more of each field becomes crop",
   "Because the drill adds nutrients to the soil directly",
   "Because rows of crops need no water",
   "Because the drill allows two harvests where there had been none",
   "Because scattered seed cannot germinate at all"], ans=0,
   why="EK SPS-5.C.1 attributes the revolution's impacts to new technology and increased food production, and this device raises output by improving the ratio of plants established to seed sown. The gain is in efficiency of a scarce input rather than in the fertility of the ground."),

 dict(q="Replacing bare fallow with a rotation that includes a nitrogen-fixing crop and a fodder crop raises output. What is the mechanism?", choices=[
   "Land that was formerly left idle now grows a crop, and the rotation restores fertility rather than waiting for it",
   "The rotation eliminates the need for any labour on the farm",
   "The rotation makes the soil permanently immune to erosion",
   "The rotation reduces the total area of the farm that is planted",
   "The rotation works only on land that has never been farmed"], ans=0,
   why="EK SPS-5.C.1 attributes increased food production to new technology, and a rotation is a technology in the sense of a method. Under bare fallow a share of every farm produced nothing each year, so a rotation that keeps that share in production is a direct addition to output."),

 dict(q="How did rising output per farm worker make more people available for work in factories?", choices=[
   "Fewer workers were needed to feed the same population, so labour was released rather than pulled away",
   "Farms deliberately dismissed workers to help factories",
   "Food production fell, forcing people to seek other work",
   "Factories were built on farmland, displacing the workers who lived there",
   "Governments required a fixed share of workers to leave agriculture"], ans=0,
   why="EK SPS-5.C.1 says increased food production led to more people being AVAILABLE for work in factories, which is a statement about a surplus rather than about recruitment. If a smaller share of the workforce can feed everyone, the remainder is free to do something else."),

 dict(q="How does better nutrition lengthen life expectancy?", choices=[
   "A better-fed population, and particularly better-fed infants and children, resists infectious disease better and dies of it less often",
   "Better nutrition eliminates infectious disease entirely",
   "Better nutrition raises the maximum age a human being can reach",
   "Better nutrition works only for adults over sixty",
   "Better nutrition has no effect on mortality"], ans=0,
   why="EK SPS-5.C.1 lists better diets and longer life expectancies in that order, which reflects the mechanism running between them. Nutrition changes how likely an infection is to kill rather than whether it occurs, and the largest effect falls on the youngest, who are the most vulnerable."),

 dict(q="Selective breeding of livestock for size, milk yield or growth rate contributed to the second agricultural revolution. Why does this count as new technology?", choices=[
   "Systematic breeding is a method for raising output from the same land and feed, which is what a technology does",
   "Because breeding requires machinery",
   "Because it introduced species that had never been domesticated",
   "Because it replaced crop farming entirely",
   "Because it was the only change of the period"], ans=0,
   why="EK SPS-5.C.1 attributes the revolution's impacts to new technology and increased food production, and a technology is any means of getting more from given inputs. An animal bred to put more of its feed into meat or milk raises output without the farm acquiring another hectare."),

 dict(q="Consolidating a household's scattered strips into one compact enclosed farm raised output. Why?", choices=[
   "A single block can be worked, drained, fenced and improved as a unit, and the time formerly spent moving between strips becomes working time",
   "Because scattered strips cannot be planted at all",
   "Because consolidation increases the total area of farmland in a district",
   "Because consolidation guarantees higher rainfall",
   "Because a compact farm needs no labour"], ans=0,
   why="EK SPS-5.C.1 attributes increased food production to new technology, and reorganizing how land is held is one of the changes of this period. Improvements such as drainage and selective breeding are practicable on a block one household controls and impracticable across strips shared with neighbours."),

 dict(q="A mechanical reaper allows a given crop to be cut by a fraction of the workers a scythe would need. Which of the framework's impacts does this most directly serve?", choices=[
   "More people available for work in factories, since the harvest no longer requires the same labour force",
   "Better diets, since machinery improves the nutritional content of grain",
   "Longer life expectancies, since machinery is safer than hand tools",
   "None of the three, since machinery affects only cost",
   "A return of factory workers to agriculture"], ans=0,
   why="EK SPS-5.C.1 names more people available for work in factories among the impacts, and labour-saving machinery is the most direct route to it. The crop is the same; what has changed is how many hands are needed to gather it."),

 dict(q="Why is a rise in food production a precondition for a large industrial workforce?", choices=[
   "Industrial workers do not grow their own food, so they can exist in large numbers only where farms produce a surplus and it can reach them",
   "Because factories require the same skills as farming",
   "Because industrial work produces food directly",
   "Because industrial workers eat less than farm workers",
   "Because factories cannot be built on former farmland"], ans=0,
   why="EK SPS-5.C.1 links increased food production to more people being available for work in factories. A city is a concentration of people who buy their food rather than growing it, which is possible only when a surplus exists and there is a way to move it."),

 dict(q="Which comparison correctly states what changed about farm labour in the second agricultural revolution?", choices=[
   "Output per farm worker rose, so total agricultural output could rise while the number of farm workers fell",
   "Output per farm worker fell, so more workers were needed on the land",
   "Output and the number of workers both fell together",
   "Output per hectare fell while output per worker rose",
   "Nothing changed about farm labour, only about diets"], ans=0,
   why="EK SPS-5.C.1 pairs increased food production with more people available for factory work, and both can be true at once only if each remaining worker produces more. Rising output alongside a shrinking agricultural workforce is the signature of the whole period."),

 dict(q="A geographer says the second agricultural revolution was a precondition of the Industrial Revolution rather than a consequence of it. What is the strongest support in the framework's own wording?", choices=[
   "The framework says increased food production LED TO more people being available for work in factories, which places the food first",
   "The framework says factories produced the new farming technology",
   "The framework does not mention factories at all",
   "The framework says the two revolutions were unrelated",
   "The framework says life expectancy fell during industrialization"], ans=0,
   why="EK SPS-5.C.1's verb points in one direction: food production led to availability for factory work. The sentence would have to be written the other way round to support the reverse claim, and it is not."),

 dict(q="In the demographic transition model, which stage does the framework's claim about longer life expectancies correspond to?", choices=[
   "The stage in which death rates fall sharply while birth rates remain high, producing rapid population growth",
   "The stage in which both birth and death rates are high and population is stable",
   "The stage in which birth rates fall below death rates and population declines",
   "The stage in which birth and death rates are both low and population is stable",
   "No stage, since the model does not concern mortality"], ans=0,
   why="EK SPS-5.C.1 names longer life expectancies among the impacts, and a rise in life expectancy is a fall in mortality. A falling death rate against a birth rate that has not yet responded is precisely the second stage of the demographic transition model."),

 dict(q="Why did the second agricultural revolution contribute to urbanization?", choices=[
   "It released labour from the land at the same time as it made feeding a large non-farming population possible",
   "It made farming illegal in rural areas",
   "It moved factories into the countryside",
   "It reduced the total food supply, forcing people into cities to buy food",
   "It had no connection to where people lived"], ans=0,
   why="EK SPS-5.C.1 names more people available for work in factories among the impacts, and factories were built where labour, capital and transport met. The same change supplies both halves of a city: the people who can leave the land and the food that will feed them once they have."),

 dict(q="What does the framework's phrase 'more people AVAILABLE for work in factories' assert, and what does it not?", choices=[
   "It asserts that labour was freed from agriculture; it does not assert that agricultural output fell or that farms were abandoned",
   "It asserts that farming collapsed and workers had no alternative",
   "It asserts that governments assigned workers to factories",
   "It asserts that factory work was better paid than farm work",
   "It asserts that every farm worker moved to a city"], ans=0,
   why="EK SPS-5.C.1 pairs INCREASED food production with the availability of workers, so the two claims are made together. A reading in which farming failed contradicts the first half of the same sentence."),

 dict(q="How does the second agricultural revolution differ from the first?", choices=[
   "The first was the domestication of plants and animals; the second raised the output of species already domesticated",
   "The first used machinery and the second did not",
   "The two are different names for the same set of changes",
   "The first occurred in the developing world and the second in hearths",
   "The first raised yields and the second introduced new species"], ans=0,
   why="EK SPS-5.A.1 locates the domestication of plants and animals in early hearths, while EK SPS-5.C.1 describes new technology raising food production. Bringing a species under cultivation and getting more from a species already cultivated are different achievements separated by thousands of years."),

 dict(q="How does the second agricultural revolution differ from the Green Revolution?", choices=[
   "The Green Revolution is a later package of high-yield seeds, chemicals and mechanization applied in the developing world, rather than the earlier changes described here",
   "They are two names for the same events",
   "The Green Revolution concerned only livestock breeding",
   "The Green Revolution reduced food production",
   "The Green Revolution preceded the domestication of plants"], ans=0,
   why="EK SPS-5.D.1 characterizes the Green Revolution by high-yield seeds, increased chemical use and mechanized farming in the developing world, while EK SPS-5.C.1 describes the second agricultural revolution's technology and its social impacts. They are separate topics with separate essential knowledge statements."),

 dict(q="Why is a rise in average life expectancy usually driven more by infant and child survival than by old people living longer?", choices=[
   "An average is pulled up sharply when deaths that used to occur in the first years of life stop occurring",
   "Because old people are not counted in life expectancy",
   "Because life expectancy measures only the age of the oldest person",
   "Because infants have always survived at high rates",
   "Because life expectancy is unrelated to mortality at any age"], ans=0,
   why="EK SPS-5.C.1 names longer life expectancies as an impact, and the measure is an average of ages at death across a whole population. A death at one year removes far more years from that average than a death at seventy, which is why improvements in infant survival dominate the figure."),

 dict(q="Improvements in canals, roads and later railways accompanied the second agricultural revolution. How do they belong to the framework's account?", choices=[
   "A surplus feeds a distant city only if it can be moved there, so transport turns higher production into a larger food supply where the workers are",
   "Transport reduces the amount of food produced",
   "Transport is unrelated to agriculture in any period",
   "Transport replaced the need for higher yields",
   "Transport prevented food from reaching cities"], ans=0,
   why="EK SPS-5.C.1 connects increased food production to more people being available for work in factories, and that connection runs through a market. Grain that cannot reach the city does not feed the city, so movement is part of the same causal chain rather than a separate story."),

 dict(q="At which scales does the framework's claim about better diets operate?", choices=[
   "A national or regional rise in food supply appears at the household scale as more and more varied food on the table",
   "Only at the global scale, since food is traded internationally",
   "Only at the household scale, since diets are personal",
   "At no scale, since diet is not a geographic concept",
   "Only at the scale of an individual farm"], ans=0,
   why="EK SPS-5.C.1 names better diets among the impacts of increased food production, and production is measured for regions while diets are eaten by households. Reading one process at two scales is what turns an aggregate statistic into a statement about people's lives."),

 dict(q="A region adopts new farming methods but its food supply per person does not rise, because population grows as fast as output. What does this show about the framework's chain?", choices=[
   "Increased total production improves diets only if it outpaces the number of people it must feed",
   "That new technology never raises production",
   "That the framework's claim has been disproved for all cases",
   "That diets improve regardless of population",
   "That population growth always precedes technological change"], ans=0,
   why="EK SPS-5.C.1 links increased food production to better diets, and what a person eats depends on output divided by population. The chain is stated as a historical outcome rather than as a law, so a case in which growth absorbs the gain is a limit on the claim and not a refutation of it."),

 dict(q="Which piece of evidence would best support the claim that a region underwent the changes the framework describes?", choices=[
   "Grain output per hectare and per farm worker both rising while the share of the workforce in agriculture fell",
   "The total population of the region falling",
   "The number of farms in the region staying exactly the same",
   "The area of farmland in the region doubling",
   "A record of which crops were first domesticated there"], ans=0,
   why="EK SPS-5.C.1 pairs increased food production with more people available for factory work. Rising yields per hectare and per worker alongside a falling agricultural share of employment is exactly that pairing, whereas expanding the farmed area would raise output without showing a change in technique."),

 dict(q="Why does the framework treat better diets and longer life expectancies as connected rather than as two independent results?", choices=[
   "Better nutrition is the mechanism by which mortality fell, so the second follows from the first",
   "They are unrelated and the framework lists them only for convenience",
   "Longer life expectancy causes better diets rather than the reverse",
   "Both were caused by factory work rather than by food",
   "Neither has anything to do with food production"], ans=0,
   why="EK SPS-5.C.1 lists the two consecutively as impacts of increased food production, and the order reflects the causal path. A better-fed population survives infection more often, which is what a rising life expectancy records."),

 dict(q="A student writes that the second agricultural revolution 'made farming unimportant'. What is the strongest objection?", choices=[
   "Agriculture became more productive, not less important -- a smaller share of workers was feeding a larger population than ever before",
   "Farming did become unimportant, so the student is correct",
   "The revolution reduced total food production",
   "The revolution had no effect on the number of farm workers",
   "Agriculture employed a larger share of the workforce afterwards"], ans=0,
   why="EK SPS-5.C.1 attributes INCREASED food production to the period, so output rose rather than fell. A falling share of employment in a sector is a measure of that sector's productivity, not of its irrelevance."),

 dict(q="Which of the following would NOT be evidence of the second agricultural revolution in a region's landscape?", choices=[
   "Terraced hillsides built centuries earlier for hand cultivation",
   "Hedged and fenced compact farms replacing open strip fields",
   "New drainage ditches on formerly waterlogged ground",
   "Barns and yards built for stall-fed improved livestock",
   "Straightened field boundaries suited to horse-drawn machinery"], ans=0,
   why="EK SPS-5.C.1 attributes the period's impacts to new technology raising food production, and four of these are physical traces of exactly that. Terraces built long before for hand cultivation record an older adaptation to slope and say nothing about the changes this statement describes."),

 dict(q="Grain yields in one region are recorded below. Using the accompanying figures, by what proportion did the yield rise?",
   table=dict(headers=["Period", "Grain yield (tonnes per hectare)", "Area under grain (hectares)"],
     rows=[["Before the new methods", "0.9", "400,000"],
           ["After the new methods", "2.1", "400,000"]]),
   choices=[
   "It rose by about 133 percent, and since the area is unchanged the gain came from the land already in use",
   "It rose by about 43 percent",
   "It rose by 120 percent because the area also expanded",
   "It fell, since more land is now needed",
   "No conclusion is possible without knowing the population"], ans=0,
   why="The yield rises from 0.9 to 2.1 tonnes per hectare, an increase of 1.2 on a base of 0.9, which is about 133 percent. The area under grain is identical in both rows, so the additional output came from higher yields rather than from bringing new land into cultivation."),

 dict(q="Agricultural employment in one region is recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Period", "Farm workers per 1,000 hectares", "Share of the workforce in agriculture (%)", "Total grain output (thousand tonnes)"],
     rows=[["Earlier", "620", "61", "360"],
           ["Later", "210", "24", "840"]]),
   choices=[
   "Output more than doubled while the agricultural share of the workforce fell from 61 to 24 percent, so each remaining farm worker produced far more",
   "Output fell as workers left agriculture",
   "Both output and the agricultural share of the workforce rose",
   "The agricultural share of the workforce rose while output stayed level",
   "No change in productivity can be inferred, since only three figures are given"], ans=0,
   why="Output rises from 360 to 840 thousand tonnes while farm workers per 1,000 hectares fall from 620 to 210 and the agricultural share of employment falls from 61 to 24 percent. EK SPS-5.C.1 pairs increased food production with more people available for factory work, and both halves of that pairing appear in the record at once."),

 dict(q="Food supply and mortality in one region are recorded below. Using the accompanying figures, what does the record support?",
   table=dict(headers=["Period", "Food energy available per person per day (kilocalories)", "Life expectancy at birth (years)", "Deaths before age five per 1,000 births"],
     rows=[["Earlier", "1,950", "36", "310"],
           ["Later", "2,650", "48", "140"]]),
   choices=[
   "Available food energy rose by 700 kilocalories a day, deaths before age five fell by more than half, and life expectancy rose by 12 years",
   "Life expectancy fell as food supply rose",
   "Deaths before age five rose while life expectancy rose",
   "Food energy per person fell across the period",
   "Life expectancy rose by 36 years"], ans=0,
   why="Food energy rises from 1,950 to 2,650 kilocalories, deaths before five fall from 310 to 140 per thousand, which is more than a halving, and life expectancy rises from 36 to 48 years. EK SPS-5.C.1 names better diets and longer life expectancies among the impacts, and the child mortality column shows where the gain in the average came from."),

 dict(q="Why is it more accurate to describe this topic's essential knowledge as a chain than as a list of three separate results?", choices=[
   "Better diets are the reason life expectancy rose, and higher output per farm worker is the reason labour became available, so the three results are linked to each other and not only to the cause",
   "Because the framework numbers the three results in order of importance",
   "Because only one of the three results actually occurred",
   "Because the three results occurred in three different regions",
   "Because the framework says the results are unrelated"], ans=0,
   why="EK SPS-5.C.1 puts new technology and increased food production at the head of a sentence whose three consequences depend on one another as well as on it. Nutrition is the mechanism behind mortality, and productivity per worker is the mechanism behind released labour."),

 dict(q="A textbook must state in one sentence what this topic's essential knowledge establishes. Which sentence stays inside what the framework claims?", choices=[
   "New technology raised food production, which improved diets, lengthened life expectancy, and freed labour for factory work",
   "Factory work drew people off the land, which forced farms to adopt new technology",
   "New technology reduced food production but improved diets",
   "The second agricultural revolution introduced high-yield seeds to the developing world",
   "The second agricultural revolution was the domestication of plants and animals"], ans=0,
   why="EK SPS-5.C.1 states exactly this chain, running from technology through production to three social consequences. The reversed version contradicts the sentence's direction, and the last two describe the Green Revolution of EK SPS-5.D.1 and the hearths of EK SPS-5.A.1 respectively."),
]
