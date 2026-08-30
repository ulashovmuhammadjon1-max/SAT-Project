# AP HUMAN GEOGRAPHY 1.6 Scales of Analysis -- 30 questions
# CED Course Framework V.1, Unit 1. Enduring understanding PSO-1; two learning
# objectives, which is unusual for a Unit 1 topic and is why the module is built
# in two halves.
#
# Essential knowledge, in full:
#   PSO-1.C.1  Scales of analysis include global, regional, national, and local.
#   PSO-1.D.1  Patterns and processes at different scales reveal variations in,
#              and different interpretations of, data.
#
# PSO-1.C is definitional -- name the four scales -- and items 1-9 and 14 are
# keyed to that list. PSO-1.D is the sentence the exam actually leans on, and it
# says something strong: the SAME data seen at different scales support
# DIFFERENT interpretations. Items 10-13, 15-25 and every table item are keyed
# to that, which is why so much of this module is comparative rather than
# definitional.
#
# One distinction the module insists on because students reliably collapse it:
# SCALE OF ANALYSIS is the size of the unit the data are aggregated to and
# reasoned about (county, province, country, world region); CARTOGRAPHIC SCALE
# is the ratio between map distance and ground distance. They are independent,
# and a large-scale map can display a global-scale analysis. Items 5 and 22
# test exactly that confusion.
#
# The second thing PSO-1.D.1 licenses is the ecological fallacy in both
# directions: what is true of an aggregate need not be true of its members, and
# what is true of members need not survive aggregation. Items 11, 16, 19, 28 and
# 29 turn on it.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_6.py. FIVE choices (A-E).
TOPIC = ("1.6", "Scales of Analysis", 1)

QUESTIONS = [
 dict(q="A researcher maps the share of each country's population living in cities for every country on Earth. What scale of analysis is she using?",
   choices=[
     "Global, because the units are countries but the frame of comparison is the whole world",
     "Local, because cities are the subject",
     "National, because each value describes one country",
     "Regional, because countries fall into world regions",
     "The scale cannot be identified without knowing the map's projection"],
   ans=0,
   why="EK PSO-1.C.1 names global among the four scales of analysis. The scale of analysis is set by the extent over which comparison is drawn, and a study covering every country on Earth is comparing at the global scale even though the reporting unit is a country."),

 dict(q="A study compares unemployment among the twelve provinces of one country. The scale of analysis is",
   choices=[
     "National, since the comparison is drawn across the units of a single country",
     "Global, since unemployment is a worldwide phenomenon",
     "Local, since provinces contain towns",
     "Regional, since provinces are regions in the everyday sense of the word",
     "Undefined, since unemployment is measured by sampling"],
   ans=0,
   why="EK PSO-1.C.1 lists global, regional, national and local. What fixes the scale is the extent within which variation is being examined, and here that extent is one country's own internal divisions."),

 dict(q="A geographer studies migration among the countries of Southeast Asia. This is analysis at which scale?",
   choices=[
     "Regional, because the frame is a group of neighboring countries rather than the world or one state",
     "Global, because migration crosses international borders",
     "National, because each migrant leaves one country",
     "Local, because migrants leave particular villages",
     "It is at all four scales simultaneously and cannot be classified"],
   ans=0,
   why="EK PSO-1.C.1 names regional as a scale distinct from both global and national. A study bounded by a multi-country world region is regional by construction, whatever the scale at which the individual moves happen."),

 dict(q="A city council examines which of its 40 neighborhoods lack a grocery store within a kilometer. The scale of analysis is",
   choices=[
     "Local, since the units compared are subdivisions of a single city",
     "National, since food policy is set nationally",
     "Regional, since the city sits inside a larger region",
     "Global, since food is traded worldwide",
     "Both global and local, since food systems connect the two"],
   ans=0,
   why="EK PSO-1.C.1 lists local as one of the four scales. The unit of comparison here is a neighborhood and the extent is one city, which is the finest of the four scales the framework names."),

 dict(q="A student says that a 1:5,000 street map 'must be a local-scale analysis.' What is wrong with this reasoning?",
   choices=[
     "Cartographic scale is the ratio of map distance to ground distance, while scale of analysis is the extent being reasoned about; the two are independent",
     "Nothing is wrong; a large cartographic scale always means a local analysis",
     "The reasoning fails only because 1:5,000 is a small cartographic scale",
     "Scale of analysis applies only to statistical data, never to maps",
     "Cartographic scale and scale of analysis are the same concept under two names"],
   ans=0,
   why="A single street map could be one illustration inside a study comparing a hundred cities worldwide, in which case the analysis is global while the map is large-scale. Conflating the ratio with the extent is the most common scale error in the course."),

 dict(q="Which of the following studies is conducted at the national scale of analysis?",
   choices=[
     "A comparison of literacy rates across the states of one federation",
     "A comparison of literacy rates across all countries in the world",
     "A comparison of literacy in three villages of one district",
     "A comparison of literacy across the countries of West Africa",
     "A comparison of literacy between two city blocks"],
   ans=0,
   why="EK PSO-1.C.1's national scale means the frame of the comparison is one country and its internal divisions. A worldwide comparison is global, a group of neighboring countries is regional, and villages or blocks are local."),

 dict(q="A geographer wants to know whether a country's population growth is concentrated in a few places or spread evenly. Which choice of analytical unit would most obscure the answer?",
   choices=[
     "Reporting one growth figure for the whole country",
     "Reporting growth for each of its 30 provinces",
     "Reporting growth for each of its 400 districts",
     "Reporting growth for each of its municipalities",
     "Reporting growth for each census tract"],
   ans=0,
   why="The question asked is about internal variation, and a single national figure contains no internal variation by construction. The coarser the unit, the more of the pattern is averaged away, and one unit averages away all of it."),

 dict(q="Which statement best expresses what PSO-1.D.1 means by saying that different scales reveal different interpretations of data?",
   choices=[
     "A pattern visible at one scale can disappear or reverse at another, so the scale chosen is part of the finding rather than a neutral backdrop",
     "Data are more accurate at large scales than at small ones",
     "Only the global scale gives a true picture, and finer scales are approximations",
     "Data collected at one scale cannot be analyzed at any other",
     "Interpretations differ because different researchers disagree"],
   ans=0,
   why="EK PSO-1.D.1 asserts that patterns and processes at different scales reveal variations in and different interpretations of data. The claim is about the data behaving differently under aggregation, not about accuracy or about disagreement among analysts."),

 dict(q="A world map of average national income shows a wealthy country. A map of that same country's provinces shows one very wealthy capital region and several poor provinces. What is the most defensible conclusion?",
   choices=[
     "Both maps are correct, and the finer scale reveals an internal inequality that the national average conceals",
     "The world map is wrong, since the country is not uniformly wealthy",
     "The provincial map is wrong, since the national figure is official",
     "The two maps cannot both be correct",
     "The country's wealth changed between the two maps"],
   ans=0,
   why="An average is a real summary of the values beneath it and says nothing about their spread, so a high mean is fully consistent with wide internal inequality. That the two views differ is the phenomenon PSO-1.D.1 names rather than a contradiction to resolve."),

 dict(q="A study finds that countries with more physicians per capita have longer life expectancy, and concludes that any individual who lives near more physicians will live longer. This inference is",
   choices=[
     "An ecological fallacy, since a relationship among aggregates need not hold for the individuals inside them",
     "Valid, since national data are collected from individuals",
     "Valid, since the two variables are both measured per capita",
     "Invalid only if the sample of countries is small",
     "Impossible to evaluate without knowing the countries involved"],
   ans=0,
   why="Aggregate correlations can arise from composition and from confounding variables that vary between countries rather than within them. Carrying a between-unit finding down to individuals is the classic scale error PSO-1.D.1's warning about interpretation points at."),

 dict(q="A national newspaper reports that the country's crime rate fell 8 percent last year. A local paper reports that crime in one district rose 30 percent. Assuming both figures are accurate, the best explanation is that",
   choices=[
     "A national aggregate can fall while particular places within it rise, because the aggregate is a weighted sum of many local changes",
     "One of the two figures must be wrong",
     "The district is not part of the country",
     "National statistics are always more reliable than local ones",
     "Crime cannot be measured at the district scale"],
   ans=0,
   why="An aggregate summarizes many components and moves with their weighted total, so a large rise in a small component is easily outweighed. Both statements can be true at once, which is exactly the interpretive variation across scales that the framework names."),

 dict(q="Which pair of questions is best matched to the scale each requires?",
   choices=[
     "Where in the world are birth rates highest -- global; where in this city are birth rates highest -- local",
     "Where in the world are birth rates highest -- local; where in this city are birth rates highest -- global",
     "Both questions require the national scale",
     "Both questions require the regional scale",
     "Neither question has a scale, since birth rates are counts"],
   ans=0,
   why="EK PSO-1.C.1 lists the four scales, and the correct one is the extent the question ranges over. A worldwide ranking demands global coverage while a within-city ranking demands units finer than the city itself."),

 dict(q="A climate agreement is negotiated by states, implemented through national laws, and felt in particular coastal towns. This case illustrates that",
   choices=[
     "A single process can operate at several scales at once, and analysis at only one of them will miss part of it",
     "Only the global scale matters for climate questions",
     "Only the local scale matters, since effects are felt locally",
     "The process has no scale, since it involves the atmosphere",
     "The scales are alternatives and an analyst must pick exactly one"],
   ans=0,
   why="EK PSO-1.D.1's point is that different scales reveal different aspects of the same phenomenon. A study confined to the treaty misses the flooded street and a study confined to the street misses the treaty, so the scales are complementary rather than competing."),

 dict(q="Which of these is a REGIONAL-scale analysis?",
   choices=[
     "A comparison of drought severity across the countries of the Sahel",
     "A comparison of drought severity across every country on Earth",
     "A comparison of drought severity between two farms",
     "A comparison of drought severity across the counties of one country",
     "A comparison of rainfall between two neighborhoods of one city"],
   ans=0,
   why="EK PSO-1.C.1's regional scale sits between national and global: a group of neighboring countries or a coherent portion of a continent. A worldwide comparison is global and comparisons inside one country are national or local."),

 dict(q="An election is decided by district. One candidate wins a majority of the national vote but loses the election. What does this show about scale?",
   choices=[
     "The unit at which votes are aggregated changes the outcome, so the rule of aggregation is part of the result",
     "The national vote count must have been miscounted",
     "District results are always more accurate than national totals",
     "The two figures measure different elections",
     "Aggregation never affects an outcome"],
   ans=0,
   why="Summing votes nationally and summing them district by district are two different operations on the same ballots, and they can disagree because districts have different sizes and margins. That is PSO-1.D.1's claim about interpretation made concrete."),

 dict(q="A public health analyst wants to identify neighborhoods with unusually high asthma rates in a city of 800,000. Which reporting unit is most appropriate?",
   choices=[
     "Census tracts or similar small areas, because the question asks about variation inside the city",
     "The city as a whole, because the question is about the city",
     "The country as a whole, because health policy is national",
     "The continent, because air quality is a continental issue",
     "The individual household, because asthma affects individuals"],
   ans=0,
   why="The unit has to be finer than the thing being compared or the comparison has nothing to work with, and coarser than the individual or the rates become unstable and identifying. Small areas inside the city are the level at which the question is actually asked."),

 dict(q="A geographer writes: 'At the global scale, this country is an exporter of manufactured goods; at the national scale, only two of its provinces manufacture anything.' The two statements are",
   choices=[
     "Compatible, because a national total can be produced by a small number of places within the country",
     "Contradictory, because a country cannot both manufacture and not manufacture",
     "Compatible only if the country is very small",
     "Contradictory unless the data were collected in different years",
     "Impossible to compare, because exports and production are different variables"],
   ans=0,
   why="A national figure is a sum, and a sum says nothing about how evenly its contributions are distributed among the places that made it. Concentration inside a country is invisible from outside it, which is precisely why the framework asks for analysis at more than one scale."),

 dict(q="Which is the strongest reason a study of deforestation might reach different conclusions at the national and the local scale?",
   choices=[
     "A country's forest area can be stable while old-growth forest is cleared in one region and plantations expand in another",
     "Deforestation can be measured only at the local scale",
     "National governments do not collect forest data",
     "Satellite imagery works only at the global scale",
     "Forests are natural and therefore have no scale"],
   ans=0,
   why="A national total nets gains against losses and hides both their location and their character, so a constant figure is compatible with large offsetting changes. Recognising what a net figure conceals is the interpretive point PSO-1.D.1 makes."),

 dict(q="A map shows every country shaded by its own average value, and a critic complains that the map 'makes each country look internally uniform.' This criticism is",
   choices=[
     "Correct, because a single shade per country is exactly an assertion of uniformity within it",
     "Incorrect, because averages carry information about internal spread",
     "Correct only for countries larger than a certain area",
     "Incorrect, because choropleth maps never mislead",
     "Irrelevant, because the scale of analysis is chosen by the reader"],
   ans=0,
   why="A choropleth assigns one value to the whole of each unit, so the visual claim is homogeneity even when the underlying distribution is wildly uneven. The criticism is about what the chosen unit of analysis conceals rather than about the data being wrong."),

 dict(q="A regional development agency compares its region's GDP per person with the national figure and with the average for its continent. It is deliberately using",
   choices=[
     "More than one scale of analysis, so that its own position can be read against several different frames",
     "Only the regional scale, since it is a regional agency",
     "Only the national scale, since the national figure is the benchmark",
     "Cartographic scale rather than scale of analysis",
     "No scale, since GDP per person is a ratio"],
   ans=0,
   why="Comparing one value against national and continental benchmarks is an explicit multi-scale exercise, and the region's apparent performance changes with the frame chosen. That dependence on frame is what PSO-1.D.1 asks students to notice."),

 dict(q="Which statement about the four scales named in the framework is correct?",
   choices=[
     "They are nested in extent, so a finding at one scale does not automatically hold at another",
     "They are alternative names for the same thing",
     "They apply only to physical geography",
     "The global scale is the sum of the local scales and therefore contains no new information",
     "A phenomenon can be studied at only one of them"],
   ans=0,
   why="EK PSO-1.C.1 lists global, regional, national and local as distinct scales, and EK PSO-1.D.1 states that they reveal different interpretations. Nesting is what makes the second sentence possible: aggregation is a real operation that can change what the data show."),

 dict(q="A study of one square kilometer of rainforest is published in a paper about worldwide biodiversity loss. The best description is that",
   choices=[
     "The fieldwork is local while the analytical frame is global, which is a common and legitimate combination",
     "The study is invalid because its evidence is local",
     "The study is global because rainforests are found worldwide",
     "The study is local, and any claim about the world is illegitimate",
     "The study has no scale because it examines a single site"],
   ans=0,
   why="The scale at which evidence is gathered and the scale at which a claim is made are different things, and the second has to be argued rather than assumed. Saying so precisely is what distinguishes a defensible generalization from an overreach."),

 dict(q="Two analysts study the same dataset of household incomes. One reports the national median; the other maps median income by district. What has the second analyst gained?",
   choices=[
     "Information about where incomes are high and low, which the single national figure cannot contain",
     "A more accurate estimate of the national median",
     "A larger sample of households",
     "A guarantee that district medians sum to the national median",
     "Nothing, since both use the same data"],
   ans=0,
   why="Disaggregation does not add data; it stops discarding the spatial information the data already carried. The national figure is not made more accurate by mapping, and medians do not sum, which is why the gain has to be stated as location rather than precision."),

 dict(q="Which of the following would be the best reason to analyze a phenomenon at the regional rather than the national scale?",
   choices=[
     "The process being studied crosses national borders and is shared by neighboring countries",
     "Regional data are always easier to obtain than national data",
     "Regions are smaller than countries and therefore simpler",
     "National governments cannot collect data",
     "Regional analysis produces larger numbers"],
   ans=0,
   why="The scale should match the extent of the process rather than the convenience of the data. A shared river basin, a migration system or a common drought does not stop at a border, so a national frame cuts the phenomenon in pieces."),

 dict(q="A student concludes from a global map that 'Africa has high fertility.' What is the most precise objection?",
   choices=[
     "The statement treats a continent of more than fifty countries as one unit, and fertility varies widely among and within them",
     "The statement is wrong because fertility cannot be mapped globally",
     "The statement is wrong because Africa is a region, not a scale",
     "The statement is acceptable, because global maps are always summaries",
     "The objection cannot be evaluated without the map's projection"],
   ans=0,
   why="Reading a continental block off a global map and then speaking as though the block were homogeneous is the scale error the course targets. The correction is not that the map is wrong but that the conclusion is drawn at a coarser scale than the underlying variation."),

 dict(q="A country's income figures are shown below. Using the table, which statement is best supported?",
   table=dict(
     headers=["Region", "Population (millions)", "GDP per capita (US$)"],
     rows=[
       ["Capital region", "6", "38,000"],
       ["Northern region", "10", "9,000"],
       ["Central region", "14", "7,000"],
       ["Southern region", "20", "5,000"]]),
   choices=[
     "The national figure of about $10,320 per person is above the level enjoyed in three of the four regions",
     "The national figure of about $10,320 per person is typical of the four regions listed",
     "All four regions are close to the national average",
     "The capital region's figure is close to the national figure",
     "The national figure cannot be calculated from regional data"],
   ans=0,
   why="Weighting each regional figure by its population gives a national average of $10,320, which exceeds the Northern, Central and Southern figures and falls far below the capital's. One small very rich region is enough to pull a mean above most of the population."),

 dict(q="School pass rates are shown for two regions in two years. Using the table, which statement is correct?",
   table=dict(
     headers=["Region", "2010 candidates", "2010 pass rate", "2020 candidates", "2020 pass rate"],
     rows=[
       ["Region A", "100", "60%", "20", "55%"],
       ["Region B", "20", "90%", "100", "85%"]]),
   choices=[
     "The national pass rate rose from 65 to 80 percent even though the rate fell in both regions",
     "The national pass rate fell, in line with both regions",
     "The national pass rate was unchanged at 75 percent",
     "One of the two regional rates must have been recorded incorrectly",
     "The national rate cannot be computed without knowing each candidate's score"],
   ans=0,
   why="In 2010, 60 of 100 and 18 of 20 give 78 of 120, or 65 percent; in 2020, 11 of 20 and 85 of 100 give 96 of 120, or 80 percent. The national rate rose because candidates shifted toward the higher-performing region, which is a change in composition rather than in performance."),

 dict(q="Four districts of one city report the data below. Using the table, which conclusion about the city is warranted?",
   table=dict(
     headers=["District", "Households", "Households without a car (%)"],
     rows=[
       ["District 1", "20,000", "12"],
       ["District 2", "5,000", "48"],
       ["District 3", "15,000", "20"],
       ["District 4", "10,000", "35"],]),
   choices=[
     "About 23 percent of the city's households have no car, but the district figures range from 12 to 48 percent",
     "About 29 percent of the city's households have no car, the simple average of the four districts",
     "Every district is close to the citywide figure",
     "The district with the highest share without a car contains the most such households",
     "The citywide share cannot be estimated from district data"],
   ans=0,
   why="Weighting by households gives 2,400 plus 2,400 plus 3,000 plus 3,500, which is 11,300 of 50,000, or 22.6 percent, while the unweighted mean of the four percentages is 28.75. The district with the highest rate is also the smallest, so it holds fewer carless households than District 4 does."),

 dict(q="A dataset of forest area is shown at two scales. Using the table, which statement is best supported?",
   table=dict(
     headers=["Unit", "Forest area 2000 (km2)", "Forest area 2020 (km2)"],
     rows=[
       ["Province I", "40,000", "22,000"],
       ["Province II", "15,000", "31,000"],
       ["Province III", "25,000", "27,000"],
       ["National total", "80,000", "80,000"]]),
   choices=[
     "The national total is unchanged while one province lost 18,000 square kilometers of forest",
     "No province changed, since the national total is unchanged",
     "Every province gained forest between 2000 and 2020",
     "The national total fell, in line with the largest province",
     "The provincial figures must be wrong, since they contradict the national total"],
   ans=0,
   why="The three provinces sum to 80,000 in both years, so the national row is consistent, yet one province fell by 18,000 while the other two gained 16,000 and 2,000. A net figure conceals both the size and the location of offsetting changes, which is why the finer scale is needed."),

 dict(q="Population change for one country is reported at three scales. Using the table, which interpretation is supported at every scale shown?",
   table=dict(
     headers=["Scale", "Unit", "Population change 2010-2020 (%)"],
     rows=[
       ["National", "Whole country", "+6"],
       ["Regional", "Coastal region", "+14"],
       ["Regional", "Interior region", "-3"],
       ["Local", "Capital city", "+22"],
       ["Local", "Interior mining town", "-19"]]),
   choices=[
     "Growth is real nationally but is concentrated on the coast and in the capital, while interior units are losing people",
     "Every unit in the country grew between 2010 and 2020",
     "The country as a whole lost population",
     "The interior region grew faster than the coastal region",
     "The national figure is the average of the four sub-national figures"],
   ans=0,
   why="The national row is positive while two of the four sub-national rows are negative, so growth is a net outcome rather than a universal one, and the two largest gains are coastal and metropolitan. Averaging the four sub-national percentages would give plus 3.5, which is not how a population-weighted national figure is formed."),
]
