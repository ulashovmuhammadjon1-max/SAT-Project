# AP HUMAN GEOGRAPHY 2.6 Malthusian Theory -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding IMP-2; learning
# objective IMP-2.B, "Explain theories of population growth and decline."
#
# Essential knowledge for this topic -- one statement, and note what it asks for:
#   IMP-2.B.3  Malthusian theory AND ITS CRITIQUES are used to analyze
#              population change and its consequences.
#
# The CED puts the critiques inside the required content, so a module that
# taught only the theory would be teaching half the topic. Roughly half the
# items below are on the argument and half on what is wrong with it, which is
# the balance the sentence asks for.
#
# THE ARGUMENT, as the course states it and as every key here is traced to.
# The CED names the theory without describing it, so these are the descriptions
# the module holds itself to:
#   -- Population, unchecked, grows GEOMETRICALLY: it multiplies, doubling in a
#      fixed interval (1, 2, 4, 8, 16 ...).
#   -- The means of subsistence grows ARITHMETICALLY: it adds a roughly constant
#      increment each interval (1, 2, 3, 4, 5 ...).
#   -- Therefore population must eventually outrun food, and be brought back by
#      checks.
#   -- POSITIVE checks raise the death rate: famine, disease, war.
#   -- PREVENTIVE checks lower the birth rate: delayed marriage, moral restraint.
#   The distinction between the two kinds of check is what items 5, 6, 12 and 21
#   turn on, and students reliably read "positive" as "good".
#
# THE CRITIQUES, which the CED requires:
#   -- Boserup: causation runs the other way. Population pressure INDUCES
#      agricultural intensification and innovation, so more people can mean more
#      food per hectare rather than less.
#   -- The empirical record: food output has outrun population for two centuries.
#      Mechanization, fertilizer, irrigation and the Green Revolution's
#      high-yielding varieties raised output faster than Malthus allowed for.
#   -- Fertility falls with development, so the geometric premise fails: birth
#      rates decline as incomes, education and urbanization rise, which Malthus
#      did not anticipate.
#   -- Famine is usually a failure of DISTRIBUTION, entitlement and politics
#      rather than of aggregate supply -- people starve in countries with food
#      in them.
#   -- Neo-Malthusians accept the critiques on food and restate the argument for
#      resources generally: water, soil, fisheries, atmosphere. Item 17 covers
#      this, and it is a restatement rather than a refutation.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_6.py. FIVE choices (A-E).
TOPIC = ("2.6", "Malthusian Theory", 2)

QUESTIONS = [
 dict(q="What was the central claim of Malthus's argument about population and food?",
   choices=[
     "Population tends to grow by multiplication while food supply grows by addition, so population must eventually outrun subsistence",
     "Population and food supply grow at the same rate, so shortages never occur",
     "Food supply grows by multiplication while population grows by addition",
     "Population growth always causes food supply to grow faster",
     "Population size is determined by government policy rather than by food"],
   ans=0,
   why="EK IMP-2.B.3 names Malthusian theory as a theory of population change and its consequences. The engine of the argument is the mismatch between two kinds of growth, geometric against arithmetic, which guarantees a crossing however large the initial food surplus."),

 dict(q="A population growing geometrically at a doubling every 25 years starts at 1 million. A food supply growing arithmetically adds enough for 1 million people every 25 years, starting at 1 million. After 100 years, how do the two compare?",
   choices=[
     "Population is 16 million while food supports 5 million, so food per person has fallen to less than a third of its starting level",
     "Population is 5 million while food supports 16 million",
     "Both reach 5 million, so the two remain in balance",
     "Both reach 16 million, so the two remain in balance",
     "Population is 4 million and food supports 4 million"],
   ans=0,
   why="Four doublings take a million to sixteen million while four equal additions take it to five million, so the ratio moves from one to one to about 3.2 to one. That divergence after only a century is the whole force of the argument."),

 dict(q="Which of the following is a POSITIVE check in Malthus's sense?",
   choices=[
     "Famine, which raises the death rate and reduces population that way",
     "Delayed marriage, which reduces the number of children born",
     "Emigration, which moves people to another country",
     "A government subsidy for large families",
     "Improved crop yields, which raise the food supply"],
   ans=0,
   why="Malthus divided the checks by which vital rate they act on: a positive check raises mortality and a preventive check lowers fertility. The word positive marks the direction of its effect on deaths, not any judgement that the outcome is good."),

 dict(q="Which of the following is a PREVENTIVE check in Malthus's sense?",
   choices=[
     "Postponing marriage to a later age, which reduces the number of children a couple has",
     "An epidemic that raises the death rate",
     "A war that kills a large share of a population",
     "A famine following a failed harvest",
     "An earthquake that destroys a city"],
   ans=0,
   why="A preventive check operates on the birth rate before a birth occurs, and later marriage shortens the childbearing years. The other four all reduce a population by killing people, which makes them positive checks in the same scheme."),

 dict(q="A student says that positive checks are 'the good ones because they are positive.' What is the correction?",
   choices=[
     "Positive refers to acting on the death rate rather than to being desirable; famine, disease and war are the examples",
     "Positive checks are those a government chooses deliberately",
     "Positive checks raise the birth rate",
     "There is no such thing as a positive check",
     "The student is right, since preventive checks are the harmful ones"],
   ans=0,
   why="The terminology names the mechanism, not its moral character. A positive check adds to mortality and a preventive check subtracts from fertility, and Malthus considered the preventive kind the humane alternative to the positive kind."),

 dict(q="Boserup's critique of Malthus reverses which relationship?",
   choices=[
     "The direction of causation: population pressure drives agricultural innovation rather than being limited by existing food supply",
     "The relationship between birth rates and death rates",
     "The relationship between urban and rural population",
     "The relationship between migration and fertility",
     "The relationship between land area and food output"],
   ans=0,
   why="EK IMP-2.B.3 requires the critiques as well as the theory. Malthus treats food supply as an external ceiling; Boserup treats it as a variable that responds to the number of mouths, because more people both need and can supply the labour that intensification requires."),

 dict(q="Which historical development is most often cited as evidence against Malthus's prediction?",
   choices=[
     "Mechanization, fertilizer, irrigation, and high-yielding crop varieties raised food output faster than population for two centuries",
     "The world's population has stopped growing",
     "Famine has never occurred since Malthus wrote",
     "The world's arable land area has doubled since 1800",
     "Birth rates have risen steadily since 1800"],
   ans=0,
   why="EK IMP-2.B.3's critiques rest first on the empirical record: output per hectare rose in ways Malthus's arithmetic premise did not allow for. Famines have continued to occur, but not because global production failed to keep pace with global population."),

 dict(q="Which of Malthus's premises does the modern fertility decline most directly undermine?",
   choices=[
     "That population, unchecked, grows geometrically, since birth rates fall on their own as societies develop",
     "That food supply grows arithmetically",
     "That famine raises the death rate",
     "That later marriage reduces births",
     "That population and food supply can be measured"],
   ans=0,
   why="The argument needs population to keep multiplying unless something stops it, and voluntary fertility decline is a brake Malthus did not foresee. Households in urbanized, educated, low-mortality societies choose fewer children without any check being applied to them."),

 dict(q="A country produces more than enough food for everyone within its borders, yet a region of it suffers famine. Which critique of Malthus does this best illustrate?",
   choices=[
     "That famine is usually a failure of distribution, purchasing power, and politics rather than of aggregate food supply",
     "That population grows arithmetically rather than geometrically",
     "That food supply is unlimited",
     "That positive checks do not exist",
     "That famines are always caused by weather"],
   ans=0,
   why="Malthus locates famine in a shortage of total production, but a shortage inside a country with surplus is a failure of access. Whether people can obtain food depends on income, entitlements, transport and political will, none of which is a term in his model."),

 dict(q="Neo-Malthusian arguments differ from Malthus's own chiefly in that they",
   choices=[
     "Extend the limits argument beyond food to water, soil, fisheries, energy, and the atmosphere",
     "Deny that population growth has any consequences",
     "Claim that food supply grows geometrically",
     "Restrict the argument to a single country",
     "Argue that population growth is always beneficial"],
   ans=0,
   why="EK IMP-2.B.3 makes both the theory and its critiques examinable, and the neo-Malthusian position accepts that food production outran the original prediction while restating the limits argument for other resources. The structure of the claim is unchanged; only the binding constraint has moved."),

 dict(q="Which observation would best SUPPORT a Malthusian reading of a particular region?",
   choices=[
     "Cultivated area and yields have stopped rising while population continues to grow, and food imports and prices are climbing",
     "The region's population is falling",
     "The region's yields per hectare have tripled in twenty years",
     "The region exports food to its neighbors",
     "The region's birth rate has halved in a generation"],
   ans=0,
   why="A Malthusian reading requires the supply side to be stalled while the demand side keeps rising, which is exactly the combination described. Every other option shows one of the two curves moving in the direction the argument says it cannot."),

 dict(q="Malthus argued that charity for the poor could be self-defeating. Within his own framework, why?",
   choices=[
     "Because relieving subsistence pressure would allow more children to survive and be born, restoring the imbalance at a larger population",
     "Because charity reduces the food supply directly",
     "Because charity is a positive check",
     "Because charity raises the death rate",
     "Because charity has no effect on population"],
   ans=0,
   why="The internal logic makes any improvement in subsistence translate into more surviving people rather than into a lasting rise in living standards. Whether that is true is one of the critiques, but the question asks what follows inside his framework."),

 dict(q="Which pattern in world food production between 1960 and 2020 is hardest for Malthus's original argument to accommodate?",
   choices=[
     "Total food output grew faster than population, so calories available per person rose while population more than doubled",
     "Total food output grew more slowly than population",
     "Population stopped growing entirely",
     "The area of cultivated land grew faster than output",
     "The number of famines increased steadily"],
   ans=0,
   why="The argument's premise is that subsistence cannot keep pace with a multiplying population, so a period in which supply per person ROSE while population doubled contradicts it directly. That output came mostly from yield rather than from new land makes the point sharper."),

 dict(q="Which is the strongest reason the framework asks students to study Malthusian theory even though its central prediction failed?",
   choices=[
     "It frames the question of whether population growth can outrun resources, which remains the question behind debates about water, soil, and climate",
     "It is the only theory of population ever proposed",
     "Its prediction has since been confirmed",
     "It accurately describes fertility decline",
     "It correctly predicted the Green Revolution"],
   ans=0,
   why="EK IMP-2.B.3 pairs the theory with its critiques precisely because the pair is the analytical tool. The specific arithmetic was wrong, while the question of whether a growing population runs into a resource ceiling is asked again for every resource in the course."),

 dict(q="A region's farmers respond to a doubling of population by terracing hillsides, shortening fallow periods, and adopting double cropping. Whose account does this best fit?",
   choices=[
     "Boserup's, because population pressure has induced more intensive use of the same land",
     "Malthus's, because the population has outrun its food supply",
     "Malthus's, because a positive check has operated",
     "Neither, because agriculture is outside both theories",
     "Boserup's, because the population has fallen"],
   ans=0,
   why="EK IMP-2.B.3 requires the critiques, and Boserup's is that necessity drives intensification. Terracing, shorter fallows and multiple harvests each raise output per hectare at the cost of more labour, which a larger population is precisely what supplies."),

 dict(q="Which statement correctly compares Malthus and Boserup on the relationship between population and agricultural technology?",
   choices=[
     "Malthus treats technology as fixed and food as the limit; Boserup treats technology as responsive and population as the spur",
     "Both treat technology as fixed",
     "Both treat technology as responsive to population",
     "Malthus treats technology as responsive and Boserup treats it as fixed",
     "Neither theory mentions agricultural technology"],
   ans=0,
   why="The disagreement is exactly about whether the food-supply curve is exogenous. Holding it fixed produces an inevitable crossing, while letting it respond to demand for food produces intensification instead of catastrophe."),

 dict(q="A neo-Malthusian argues that a region's groundwater is being pumped faster than it recharges and that its population continues to grow. What makes this a neo-Malthusian rather than a strictly Malthusian argument?",
   choices=[
     "The binding limit named is a resource other than food, which is the extension neo-Malthusians make",
     "The argument concerns a region rather than the world",
     "The argument involves population growth",
     "The argument predicts a check on population",
     "The argument uses quantitative data"],
   ans=0,
   why="Malthus's constraint is subsistence specifically, and the later restatement moves the constraint to whichever resource is scarcest. Naming water rather than food is the whole of the difference, since the structure of the reasoning is identical."),

 dict(q="What does it mean to say that Malthus's premise about food supply was 'arithmetic'?",
   choices=[
     "That output was assumed to rise by a roughly constant amount in each period rather than by a constant proportion",
     "That output was assumed to be measurable",
     "That output was assumed to be fixed at a constant level",
     "That output was assumed to double in each period",
     "That output was assumed to fall in each period"],
   ans=0,
   why="An arithmetic series adds a fixed increment while a geometric series multiplies by a fixed factor, and the two diverge without limit however small the multiplier. That structural divergence, not any particular number, is what makes the conclusion inevitable within the model."),

 dict(q="Which of these would a Malthusian identify as a positive check operating today?",
   choices=[
     "Mortality rising in a region during a prolonged drought and crop failure",
     "A national campaign encouraging later marriage",
     "Free distribution of contraception",
     "A rise in the average age at first birth",
     "A fall in the total fertility rate"],
   ans=0,
   why="A positive check operates through deaths, and famine following crop failure is the case Malthus named first. Every other option lowers the birth rate, which places it among the preventive checks instead."),

 dict(q="Why do critics argue that Malthus underestimated the food supply curve rather than merely getting a number wrong?",
   choices=[
     "He assumed a constant increment, but yields rose proportionally with new seeds, fertilizer, and irrigation, which makes food growth geometric too",
     "He assumed food supply would fall",
     "He measured food in the wrong units",
     "He used data from only one country",
     "He assumed population would stop growing"],
   ans=0,
   why="If output also multiplies rather than adds, the two curves no longer necessarily cross, and the conclusion of the argument fails rather than being merely delayed. That is a structural error in the premise, not a mistaken estimate of a coefficient."),

 dict(q="A geographer says the Malthusian debate has 'moved from the granary to the atmosphere.' What is meant?",
   choices=[
     "The question of whether population can outrun a resource has shifted from food to environmental sinks and services",
     "Malthus wrote about the atmosphere rather than about food",
     "Food is no longer produced on land",
     "Population growth no longer has consequences",
     "The debate has been settled in Malthus's favour"],
   ans=0,
   why="EK IMP-2.B.3 keeps the theory and its critiques together as tools for analyzing consequences of population change. What survived the critiques is the form of the question, and the resources now argued about are ones no one priced in 1798."),

 dict(q="Which of the following is the best reason the world's food supply outran population growth after 1950?",
   choices=[
     "Yields per hectare rose sharply, so output grew without a proportional increase in cultivated area",
     "The area of farmland doubled",
     "The world's population growth rate rose",
     "Diets shifted toward more resource-intensive foods",
     "Famines eliminated the excess population"],
   ans=0,
   why="Most of the increase came from getting more out of each hectare rather than from ploughing new ground, which is the precise sense in which technology broke the arithmetic premise. The land area under cultivation grew comparatively little over the same period."),

 dict(q="A country's population doubles while its food output rises by 60 percent. What has happened to food per person, and how would a Malthusian read it?",
   choices=[
     "Food per person has fallen by about a fifth, which a Malthusian would read as the predicted divergence beginning",
     "Food per person has risen, since output rose",
     "Food per person is unchanged, since both rose",
     "Food per person has fallen by 60 percent",
     "Nothing can be said without knowing the country's land area"],
   ans=0,
   why="Output at 1.6 times divided by population at 2 times leaves 0.8 of the original amount per person, a fall of 20 percent. A rising total with a falling per-person figure is exactly the situation the argument is about, which is why the total alone settles nothing."),

 dict(q="Which of these is NOT a recognized critique of Malthusian theory?",
   choices=[
     "That population has never grown in any period of history",
     "That agricultural technology responds to population pressure",
     "That fertility falls as societies develop",
     "That famines usually reflect distribution rather than total supply",
     "That food output has grown faster than population for two centuries"],
   ans=0,
   why="EK IMP-2.B.3 requires the critiques, and the four genuine ones each attack a premise or a prediction. Denying that population has ever grown contradicts the evidence rather than the theory, and no critic of Malthus has argued it."),

 dict(q="A policy analyst uses Malthusian reasoning to argue for investment in a region's agriculture. What is the most defensible version of that argument?",
   choices=[
     "That where output has stalled and population is still rising, the gap has to be closed by raising output, importing food, or reducing fertility",
     "That population growth should be allowed to be checked by famine",
     "That agricultural investment is always futile",
     "That food supply cannot be increased",
     "That population growth is unrelated to food supply"],
   ans=0,
   why="Using the theory analytically means identifying the gap it describes and then acting on the terms it identifies, which is what EK IMP-2.B.3's pairing with the critiques makes possible. The fatalistic reading treats the positive check as a policy, which the critiques and ordinary decency both reject."),

 dict(q="Two series are projected over five intervals. Using the table, what does the comparison show?",
   table=dict(
     headers=["Interval", "Population (millions)", "Food supply (millions fed)"],
     rows=[
       ["0", "2", "2"],
       ["1", "4", "3"],
       ["2", "8", "4"],
       ["3", "16", "5"],
       ["4", "32", "6"]]),
   choices=[
     "The population multiplies while the food supply adds a constant amount, so by interval 4 food supports fewer than one person in five",
     "Both series grow geometrically, so the ratio between them is constant",
     "Both series grow arithmetically, so the gap between them is constant",
     "The food supply grows faster than the population after interval 2",
     "The two series remain equal throughout"],
   ans=0,
   why="The population column doubles at every step while the food column rises by exactly one each time, so at the last interval 6 million can be fed out of 32 million people. That is the geometric-against-arithmetic contrast in its bare arithmetic form."),

 dict(q="World figures are shown for two dates. Using the table, which conclusion is best supported?",
   table=dict(
     headers=["Year", "Population (billions)", "Cereal production (million tonnes)"],
     rows=[
       ["1960", "3.0", "900"],
       ["2020", "7.8", "3,000"]]),
   choices=[
     "Cereal production per person rose from 300 to about 385 kilograms, so output grew faster than population",
     "Cereal production per person fell, since population grew by more than four billion",
     "Cereal production per person was unchanged, since both figures rose",
     "Population grew faster than cereal production, since it rose by 160 percent",
     "No comparison is possible, since the units differ"],
   ans=0,
   why="Nine hundred million tonnes divided among three billion people is 300 kilograms each, while three thousand million tonnes among 7.8 billion is about 385, so the per-person figure rose by nearly a third. Population grew 2.6-fold against production's 3.3-fold."),

 dict(q="Yields and cultivated area are shown for one country. Using the table, what accounts for the rise in output?",
   table=dict(
     headers=["Year", "Cultivated area (million hectares)", "Yield (tonnes per hectare)"],
     rows=[
       ["1970", "20", "1.5"],
       ["1990", "21", "2.8"],
       ["2010", "22", "4.0"]]),
   choices=[
     "Output rose from 30 to 88 million tonnes almost entirely because yield per hectare rose, while cultivated area grew only 10 percent",
     "Output rose because the cultivated area nearly tripled",
     "Output fell, because yields cannot rise indefinitely",
     "Output rose equally from area expansion and from yield growth",
     "Output cannot be calculated from the figures given"],
   ans=0,
   why="Multiplying the two columns gives 30, 58.8 and 88 million tonnes, an increase of 193 percent, while area rose only from 20 to 22 million hectares. Yield rising from 1.5 to 4.0 tonnes is what did nearly all the work, which is the mechanism Malthus's arithmetic premise excluded."),

 dict(q="A country's national food availability and a region's famine mortality are shown. Using the table, which reading is best supported?",
   table=dict(
     headers=["Year", "National food available (kcal per person per day)", "Famine deaths in Region Q"],
     rows=[
       ["Year 1", "2,450", "0"],
       ["Year 2", "2,410", "180,000"],
       ["Year 3", "2,430", "60,000"]]),
   choices=[
     "National availability barely moved while famine deaths appeared and then fell, so the failure was in access within one region rather than in national supply",
     "National availability collapsed, which caused the famine",
     "Famine deaths rose because national availability rose",
     "The figures show that famine is impossible when availability exceeds 2,400 kilocalories",
     "The famine deaths must have been recorded in error"],
   ans=0,
   why="Availability moves within 40 kilocalories across the three years, a change of under 2 percent, while famine deaths go from zero to 180,000 and back down. A national supply that never fell materially cannot be the cause of a regional catastrophe, which is the distribution critique in data."),

 dict(q="Fertility and income are shown for four countries. Using the table, which critique of Malthus does the pattern support?",
   table=dict(
     headers=["Country", "GDP per capita (US$)", "Total fertility rate"],
     rows=[
       ["Country A", "1,100", "5.4"],
       ["Country B", "4,800", "3.1"],
       ["Country C", "16,000", "1.9"],
       ["Country D", "42,000", "1.5"]]),
   choices=[
     "That population does not grow geometrically without limit, since fertility falls steadily as incomes rise",
     "That food supply grows geometrically",
     "That famine is caused by distribution",
     "That agricultural technology responds to population pressure",
     "That positive checks do not exist"],
   ans=0,
   why="Fertility falls from 5.4 to 1.5 as income rises from 1,100 to 42,000 dollars, with no reversal anywhere in the sequence. A population that limits its own growth as it develops removes the premise that only a check can stop it."),
]
