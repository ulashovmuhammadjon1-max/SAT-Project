# AP HUMAN GEOGRAPHY 2.5 The Demographic Transition Model -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding IMP-2; learning
# objective IMP-2.B, "Explain theories of population growth and decline."
#
# Essential knowledge for THIS topic (IMP-2.B.3, Malthus, belongs to 2.6):
#   IMP-2.B.1  The demographic transition model can be used to explain
#              population change over time.
#   IMP-2.B.2  The epidemiological transition explains causes of changing
#              death rates.
#
# Both statements name a model and neither describes it, so every key here rests
# on the model as the course teaches it. Those descriptions are set out in full
# below, because a key that cannot be traced to a stated description is exactly
# what this bank is not allowed to ship.
#
# DEMOGRAPHIC TRANSITION MODEL -- what happens to the two rates:
#   Stage 1  high birth rate, high and fluctuating death rate; little or no
#            natural increase. No country's national population is at this stage
#            today.
#   Stage 2  death rate FALLS sharply while the birth rate stays high --
#            sanitation, clean water, food supply, basic medicine. Natural
#            increase reaches its maximum here. Pyramid: very wide base.
#   Stage 3  birth rate now falls, death rate already low; growth continues but
#            decelerates. Urbanization, female education and employment, and the
#            rising cost of raising a child are the usual drivers.
#   Stage 4  both rates low; natural increase near zero. Population near stable.
#   Stage 5  birth rate below death rate; natural increase NEGATIVE and the
#            population ages and declines without migration. Treated in this
#            course as an extension of the model rather than part of its
#            original four stages, and the items below say so.
#
# The single most important structural fact, and the one items 2, 6, 12, 19 and
# 26 turn on: the death rate falls FIRST and the birth rate falls LATER, and the
# gap between the two curves is population growth. Stage 2 is not a stage of
# high fertility -- fertility is high in stage 1 too -- it is the stage in which
# mortality has already fallen and fertility has not yet.
#
# EPIDEMIOLOGICAL TRANSITION -- what people die OF, which is a different
# question from how many die:
#   Stage 1  pestilence and famine: infectious and parasitic disease, famine
#   Stage 2  receding pandemics: sanitation, nutrition and public health cut
#            infectious mortality sharply
#   Stage 3  degenerative and human-created disease: heart disease, cancer and
#            other chronic conditions become the leading causes
#   Stage 4  delayed degenerative disease: medicine postpones the same chronic
#            deaths to later ages, so life expectancy rises further
#   Stage 5  a proposed stage of re-emerging infectious disease -- antibiotic
#            resistance, evolution of pathogens, and rapid global travel
#
# The model's limitations are examinable too, and items 15, 20 and 25 carry
# them: the model was built from the European experience, it says nothing about
# migration, and its stages are descriptive rather than a schedule any country
# must follow.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_5.py. FIVE choices (A-E).
TOPIC = ("2.5", "The Demographic Transition Model", 2)

QUESTIONS = [
 dict(q="What does the demographic transition model describe?",
   choices=[
     "The changing relationship between a population's birth and death rates over time, and the growth or decline that results",
     "The movement of people between countries over time",
     "The distribution of population across a country's regions",
     "The relationship between population size and food supply",
     "The share of a population living in cities over time"],
   ans=0,
   why="EK IMP-2.B.1 states that the demographic transition model can be used to explain population change over time, and the model does that by tracking two rates against each other. Migration, distribution, food supply and urbanization are the subjects of other models in this course."),

 dict(q="In which stage of the demographic transition is a population's rate of natural increase at its highest?",
   choices=[
     "Stage 2, because the death rate has fallen sharply while the birth rate is still high",
     "Stage 1, because the birth rate is at its highest",
     "Stage 3, because the birth rate is falling",
     "Stage 4, because both rates are low and stable",
     "Stage 5, because the population is aging"],
   ans=0,
   why="Natural increase is the gap between the two rates, not the level of either one. Both rates are high in the first stage so the gap is small; the gap opens widest when mortality has already fallen and fertility has not yet begun to."),

 dict(q="A country has a high birth rate and a death rate that swings sharply with harvests and epidemics, so its population barely grows over a century. Which stage does this describe?",
   choices=[
     "Stage 1, in which high fertility is offset by high and unstable mortality",
     "Stage 2, in which mortality has begun to fall",
     "Stage 3, in which fertility is falling",
     "Stage 4, in which both rates are low",
     "Stage 5, in which the population is declining"],
   ans=0,
   why="The signature of the first stage is not merely a high birth rate but a death rate that is both high and volatile, so growth in good years is cancelled in bad ones. That instability is what the later stages remove."),

 dict(q="Which set of changes best explains the fall in death rates that moves a country into the second stage?",
   choices=[
     "Clean water, sanitation, improved nutrition, and basic public health measures such as vaccination",
     "A sudden fall in the number of children families choose to have",
     "The construction of universities and the expansion of higher education",
     "A rise in the average age at which people marry",
     "The introduction of pension systems for the elderly"],
   ans=0,
   why="The mortality decline that opens the second stage is driven by the causes of death that are cheapest to prevent, which are infectious and diarrhoeal disease and undernutrition. The other options all act on fertility or on the old, and neither is what moves the death rate first."),

 dict(q="A country's birth rate has begun falling while its death rate has been low for decades, and its population is still growing but more slowly each year. Which stage is it in?",
   choices=[
     "Stage 3, in which fertility falls and growth decelerates",
     "Stage 2, in which mortality falls and growth accelerates",
     "Stage 4, in which growth has stopped",
     "Stage 5, in which the population declines",
     "Stage 1, in which growth is negligible"],
   ans=0,
   why="The third stage is defined by the second of the two declines: the death rate has already fallen and the birth rate is now following it down. The gap between the curves is narrowing, which is deceleration rather than either maximum growth or stability."),

 dict(q="Which pair of factors most commonly drives the FERTILITY decline that defines the third stage?",
   choices=[
     "Urbanization together with expanded education and employment for women",
     "Improved sanitation together with vaccination",
     "Rising immigration together with falling emigration",
     "A larger land area together with lower population density",
     "Improved harvests together with better food storage"],
   ans=0,
   why="Sanitation and vaccination lower mortality, which is the previous stage's mechanism. The fertility decline is driven by changes in what a child costs and what alternatives adults have, and city living and women's schooling and paid work are the standard pair."),

 dict(q="A country has low and nearly equal birth and death rates and a population that has been almost unchanged for twenty years. Which stage best fits?",
   choices=[
     "Stage 4, in which both rates are low and natural increase is close to zero",
     "Stage 5, in which the population declines",
     "Stage 3, in which growth is decelerating",
     "Stage 2, in which growth is fastest",
     "Stage 1, in which both rates are high"],
   ans=0,
   why="A near-zero natural increase can arise from two high rates or two low ones, and the low pair is the fourth stage. The stem specifies that both rates are low, which rules out the first stage even though its natural increase is also close to zero."),

 dict(q="What distinguishes the stage sometimes added as Stage 5 from Stage 4?",
   choices=[
     "The birth rate falls below the death rate, so natural increase becomes negative and the population declines without migration",
     "The death rate rises above the level of Stage 1",
     "The birth rate rises sharply",
     "Migration replaces natural increase as the only source of change",
     "Both rates return to the high levels of Stage 1"],
   ans=0,
   why="The extension of the model to a fifth stage records the case in which fertility falls not just to replacement but below it, so deaths outnumber births in a population that is also aging. The death rate rises only because the population is old, not because conditions have worsened."),

 dict(q="A country's population pyramid has a very wide base and narrows sharply upward. Which stage of the demographic transition does this most likely indicate?",
   choices=[
     "Stage 2, in which high fertility and recently reduced mortality produce very large young cohorts",
     "Stage 4, in which cohorts are of similar size",
     "Stage 5, in which the base is the narrowest part",
     "Stage 3, in which the base has begun to narrow",
     "Stage 1, in which the pyramid is a narrow triangle at every level"],
   ans=0,
   why="A wide base means many births, and each cohort being sharply smaller than the one below it means those births are recent and growing in number. That combination belongs to the stage in which mortality has already fallen and fertility has not."),

 dict(q="The epidemiological transition, as the framework uses it, explains",
   choices=[
     "How the leading causes of death change as a society develops, and why the death rate changes with them",
     "How birth rates fall as incomes rise",
     "How populations move between countries",
     "How population density affects disease",
     "How food supply limits population growth"],
   ans=0,
   why="EK IMP-2.B.2 states that the epidemiological transition explains causes of changing death rates. It is a companion to the demographic model, answering what people die of rather than how many of them die."),

 dict(q="In the first stage of the epidemiological transition, the leading causes of death are",
   choices=[
     "Infectious and parasitic diseases together with famine",
     "Heart disease and cancer",
     "Injuries sustained in industrial workplaces",
     "Conditions of old age postponed by modern medicine",
     "Newly resistant strains of bacteria"],
   ans=0,
   why="EK IMP-2.B.2 makes the epidemiological transition an account of changing causes of death, and its opening stage is the one commonly called pestilence and famine. Chronic disease dominates only where enough people survive to old age to die of it."),

 dict(q="A country's leading causes of death shift from diarrhoeal disease and pneumonia to heart disease and cancer over forty years. What has happened?",
   choices=[
     "It has moved through the epidemiological transition as infectious mortality receded and more people survived to the ages when chronic disease kills",
     "Its people have become less healthy overall",
     "Its death rate must have risen",
     "It has returned to the first stage of the transition",
     "Its birth rate must have risen at the same time"],
   ans=0,
   why="EK IMP-2.B.2's transition is about composition rather than level: removing the causes that kill the young leaves the causes that kill the old as the largest share. Life expectancy rises even though the leading causes now sound more serious."),

 dict(q="Antibiotic-resistant infections, rapidly spreading new pathogens, and diseases carried by international air travel are cited as evidence for",
   choices=[
     "A possible further stage of the epidemiological transition in which infectious disease re-emerges",
     "A return of the demographic transition to its first stage",
     "The end of the demographic transition",
     "The claim that death rates cannot change",
     "The failure of the demographic transition model to describe fertility"],
   ans=0,
   why="The proposed extension of EK IMP-2.B.2's transition covers exactly these mechanisms: pathogens evolving faster than treatments, and connectivity moving them faster than containment. It is a proposed stage rather than an established one, which is why the option is phrased as a possibility."),

 dict(q="Why does the demographic transition model predict a large surge in population even in countries where fertility eventually falls?",
   choices=[
     "Mortality falls before fertility does, so for a generation or more many more people are born than die",
     "Fertility rises during the transition before it falls",
     "Mortality rises during the transition",
     "The model predicts no surge in population at any stage",
     "Migration into the country accelerates during the transition"],
   ans=0,
   why="The whole shape of the model comes from the two declines being separated in time, since the interventions that cut deaths are cheaper and faster acting than the social changes that cut births. The population added during that lag does not disappear when fertility finally falls."),

 dict(q="Which is a legitimate criticism of the demographic transition model?",
   choices=[
     "It was generalized from the European experience and does not account for migration, so it describes some countries' paths poorly",
     "It cannot be applied to any country outside Europe under any circumstances",
     "It has been shown to be wrong about the direction in which death rates move",
     "It claims that birth rates never fall",
     "It makes no reference to death rates at all"],
   ans=0,
   why="EK IMP-2.B.1 says the model can be USED to explain population change, which is a claim about usefulness rather than about universal law. Its two best-documented limits are its origin in one region's history and its silence on migration, which for many countries is the largest component of change."),

 dict(q="Two countries are both in the third stage, but one is moving through it in twenty-five years and the other took ninety. What does this show about the model?",
   choices=[
     "The model describes a sequence of changes, not a fixed timetable, so the pace varies with the conditions of each country",
     "One of the two countries has been misclassified",
     "The model applies only to countries that transition slowly",
     "The stages must always take the same number of years",
     "The model cannot describe more than one country at a time"],
   ans=0,
   why="EK IMP-2.B.1 offers the model as an explanatory tool rather than a schedule. Countries transitioning later can import medicine and contraception that took the earlier ones a century to develop, so the same sequence runs at very different speeds."),

 dict(q="A country in the fourth stage has a stable total population but an increasingly old age structure. What accounts for this?",
   choices=[
     "Low fertility sustained for decades means each new cohort is no larger than the last, while low mortality keeps earlier cohorts alive into old age",
     "The country must be receiving elderly migrants",
     "Its death rate must be rising sharply",
     "Its birth rate must be rising",
     "Aging is unrelated to the demographic transition"],
   ans=0,
   why="A stable total conceals a changing shape: with births flat and survival high, the population accumulates in the older cohorts each year. Aging is therefore a consequence of the transition rather than a separate process."),

 dict(q="Which statement correctly relates the demographic and epidemiological transitions?",
   choices=[
     "The epidemiological transition explains WHY the death rate falls in the demographic model by describing which causes of death recede",
     "The two models describe the same variable using different words",
     "The epidemiological transition explains changes in fertility",
     "The demographic transition explains causes of death and the epidemiological transition explains birth rates",
     "The two models contradict each other"],
   ans=0,
   why="EK IMP-2.B.1 makes the demographic model an account of population change and EK IMP-2.B.2 makes the epidemiological transition an account of causes of changing death rates. One supplies the mechanism behind the other's mortality curve."),

 dict(q="A student says that Stage 2 countries have high birth rates and Stage 1 countries do not. What is the error?",
   choices=[
     "Birth rates are high in both stages; what changes between them is the death rate",
     "Birth rates are low in both stages",
     "Death rates are identical in both stages",
     "Stage 1 has the higher birth rate of the two",
     "There is no error in the statement"],
   ans=0,
   why="The first two stages share a high birth rate, and the transition between them is entirely a mortality event. Treating the second stage as the high-fertility stage misses that fertility has not yet moved and misidentifies what causes the growth."),

 dict(q="Why does the demographic transition model, taken alone, fail to predict the population of a small country with very large immigration?",
   choices=[
     "The model tracks only births and deaths, so a change driven by migration is outside what it describes",
     "The model applies only to countries with high fertility",
     "The model treats immigration as a form of natural increase",
     "The model predicts that immigration always falls",
     "Small countries have no demographic transition"],
   ans=0,
   why="EK IMP-2.B.1 makes the model an account of population change through the two rates it plots, and migration is a third component it does not carry. Where migration dominates, the model can describe natural increase correctly and still get the total badly wrong."),

 dict(q="Which observation would best support the claim that a country has entered the stage in which chronic disease dominates mortality?",
   choices=[
     "Cardiovascular disease and cancer together account for most deaths, and life expectancy exceeds seventy years",
     "Infant mortality is the country's leading cause of death",
     "Famine deaths have been recorded in the last decade",
     "The country's birth rate is above 35 per 1,000",
     "The country's population is growing at 3 percent a year"],
   ans=0,
   why="EK IMP-2.B.2's transition is diagnosed from the composition of deaths, and chronic disease can only dominate once enough people survive to the ages at which it kills. High infant mortality, famine, high fertility and rapid growth all point to an earlier stage."),

 dict(q="A country's death rate rises slightly even though its health care continues to improve. What is the most likely explanation, in terms of the model?",
   choices=[
     "The population has aged so much that a crude death rate rises even as survival at every age improves",
     "The country has returned to the first stage",
     "Health care must in fact be deteriorating",
     "The birth rate must have risen",
     "Crude death rates cannot rise once they have fallen"],
   ans=0,
   why="A crude rate is deaths divided by the whole population, so a population weighted toward the old ages produces more deaths per thousand regardless of medical improvement. This is why late-transition countries can show a rising death rate that means the opposite of what it appears to."),

 dict(q="Which sequence correctly orders the demographic transition's effects on a country's population size?",
   choices=[
     "Near-stability, then rapid growth, then decelerating growth, then near-stability again at a much larger size",
     "Rapid growth, then decline, then stability, then rapid growth",
     "Steady growth at a constant rate throughout all stages",
     "Decline, then rapid growth, then stability at the original size",
     "No change in population size at any stage"],
   ans=0,
   why="The model's shape follows from the two rates converging, separating and converging again: the first stage has a small gap, the second a wide one, the third a narrowing one, and the fourth a small gap once more at much lower levels. The population ends far larger than it began."),

 dict(q="A public health ministry wants to know where to direct spending to lower its country's death rate fastest. Which model is designed to answer that?",
   choices=[
     "The epidemiological transition, because it identifies which causes of death dominate at a country's current stage",
     "The demographic transition model, because it plots the death rate",
     "The demographic transition model, because it plots the birth rate",
     "Neither model, since both describe the past only",
     "The epidemiological transition, because it predicts birth rates"],
   ans=0,
   why="EK IMP-2.B.2 makes the epidemiological transition an account of the CAUSES of changing death rates, which is what a spending decision needs. The demographic model plots the rate itself and is silent on what is producing it."),

 dict(q="Which is the strongest reason not to treat the demographic transition model as a prediction about any particular country?",
   choices=[
     "It is a generalization from observed histories, so a country's path depends on policies, epidemics, wars, and migration that the model does not contain",
     "It has never matched any country's experience",
     "Its stages are defined too precisely to be applied",
     "It uses rates that cannot be measured",
     "It has been formally withdrawn by demographers"],
   ans=0,
   why="EK IMP-2.B.1 offers the model as something that CAN BE USED to explain change, which is a statement about explanatory value rather than about inevitability. Its accuracy for a given country depends on whether that country's circumstances resemble the histories it was built from."),

 dict(q="Vital rates for four countries are shown. Using the table, which country is most likely in Stage 2 of the demographic transition?",
   table=dict(
     headers=["Country", "Crude birth rate (per 1,000)", "Crude death rate (per 1,000)"],
     rows=[
       ["Country A", "40", "10"],
       ["Country B", "42", "38"],
       ["Country C", "13", "9"],
       ["Country D", "9", "12"]]),
   choices=[
     "Country A, with a high birth rate and a death rate that has already fallen, giving natural increase of 3.0 percent",
     "Country B, with the highest birth rate in the table",
     "Country C, with low rates and slow growth",
     "Country D, whose deaths exceed its births",
     "Country B, because its natural increase is the highest in the table"],
   ans=0,
   why="Natural increase is 3.0, 0.4, 0.4 and minus 0.3 percent, so the country with the highest birth rate is not the fastest growing. A high birth rate paired with a death rate that has already collapsed is the defining combination of the second stage."),

 dict(q="Vital rates for one country are shown at four dates. Using the table, in which interval did the country pass from mortality decline into fertility decline?",
   table=dict(
     headers=["Year", "Crude birth rate (per 1,000)", "Crude death rate (per 1,000)"],
     rows=[
       ["1950", "45", "28"],
       ["1970", "44", "13"],
       ["1990", "31", "9"],
       ["2010", "18", "7"]]),
   choices=[
     "Between 1970 and 1990, when the birth rate fell 13 points while the death rate fell only 4",
     "Between 1950 and 1970, when the death rate fell 15 points",
     "Between 1990 and 2010, when both rates reached their lowest values",
     "The country has not yet begun its fertility decline",
     "Between 1950 and 1970, when the birth rate fell 1 point"],
   ans=0,
   why="From 1950 to 1970 the death rate falls 15 points while the birth rate falls 1, which is a mortality event; from 1970 to 1990 the birth rate falls 13 against the death rate's 4. The interval in which the larger fall switches from one rate to the other is the passage between the stages."),

 dict(q="Causes of death are shown for two countries as a share of all deaths. Using the table, which statement is best supported?",
   table=dict(
     headers=["Cause of death", "Country X (% of deaths)", "Country Y (% of deaths)"],
     rows=[
       ["Infectious and parasitic disease", "48", "6"],
       ["Cardiovascular disease", "17", "42"],
       ["Cancer", "8", "29"],
       ["Injury", "12", "9"],
       ["All other causes", "15", "14"]]),
   choices=[
     "Country X is at an earlier stage of the epidemiological transition, since infectious disease still causes 48 percent of its deaths against 6 percent in Country Y",
     "Country Y is less healthy, since 71 percent of its deaths are from cardiovascular disease and cancer",
     "Country X has the higher life expectancy, since fewer of its deaths are from chronic disease",
     "The two countries are at the same stage, since both columns sum to 100",
     "Country Y is at an earlier stage, since injury causes a smaller share of its deaths"],
   ans=0,
   why="Both columns sum to 100, so only the composition can be compared and not the number of deaths. Infectious disease causing nearly half of all deaths in one country and one death in seventeen in the other is the clearest possible marker of the earlier stage."),

 dict(q="Birth and death rates are shown for four countries. Using the table, which country best fits the stage in which population declines without migration?",
   table=dict(
     headers=["Country", "Crude birth rate (per 1,000)", "Crude death rate (per 1,000)", "Share aged 65+ (%)"],
     rows=[
       ["Country J", "8", "11", "23"],
       ["Country K", "11", "10", "17"],
       ["Country L", "26", "7", "4"],
       ["Country M", "35", "9", "3"]]),
   choices=[
     "Country J, whose births fall short of its deaths and whose population is the oldest in the table",
     "Country K, whose two rates are almost equal",
     "Country L, whose birth rate has fallen a long way from its historic level",
     "Country M, whose death rate is the second lowest",
     "None of them, since a population cannot decline"],
   ans=0,
   why="Only one country has more deaths than births, at 8 against 11 per 1,000, and it also carries the largest share over 65 at 23 percent. The pairing matters because a rising crude death rate in that country reflects an old age structure rather than worsening health."),

 dict(q="Population totals and natural increase are shown for one country over sixty years. Using the table, what does the sequence illustrate about the transition?",
   table=dict(
     headers=["Year", "Population (millions)", "Rate of natural increase (%)"],
     rows=[
       ["1960", "20", "1.0"],
       ["1980", "34", "2.6"],
       ["2000", "52", "1.7"],
       ["2020", "63", "0.6"]]),
   choices=[
     "The growth rate peaked and then fell, yet the population more than tripled, because a falling rate still applies to a much larger base",
     "The population fell once the growth rate began to fall",
     "The growth rate and the population moved in the same direction throughout",
     "The population stopped growing after 1980",
     "The figures are inconsistent, since a falling rate must reduce a population"],
   ans=0,
   why="The rate rises to 2.6 percent and then falls to 0.6 while the population goes from 20 to 63 million, so a decelerating rate still adds people. That distinction between a rate and a total is why growth continues long after the transition's peak."),
]
