# AP HUMAN GEOGRAPHY 1.5 Human-Environmental Interaction -- 30 questions
# (TOPIC below carries the CED's own en-dash spelling of the title.)
# CED Course Framework V.1, Unit 1. Enduring understanding PSO-1; learning
# objective PSO-1.B, "Explain how major geographic concepts illustrate spatial
# relationships."
#
# Essential knowledge, in full -- the topic has exactly two statements:
#   PSO-1.B.1  Concepts of nature and society include sustainability, natural
#              resources, and land use.
#   PSO-1.B.2  Theories regarding the interaction of the natural environment
#              with human societies have evolved from environmental determinism
#              to possibilism.
#
# PSO-1.B.2 is the load-bearing sentence and it says something precise: the
# theories EVOLVED FROM determinism TO possibilism. That direction is the
# examinable content. Determinism holds that the physical environment causes
# and limits cultural outcomes; possibilism holds that the environment sets a
# range of possibilities within which culture chooses. The module therefore
# tests the pair by application -- given an argument, which theory is it? -- and
# by consequence, since environmental determinism was used historically to
# justify claims about the superiority of peoples in particular climates, and
# that is why it was abandoned rather than merely refined.
#
# PSO-1.B.1 supplies three named concepts and no definitions, so items about
# renewable and nonrenewable resources, sustainable yield, and land-use
# categories are keyed to what the terms pick out rather than to a framework
# sentence. Those items cite no EK, deliberately.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_5.py. FIVE choices (A-E).
TOPIC = ("1.5", "Human–Environmental Interaction", 1)

QUESTIONS = [
 dict(q="A nineteenth-century writer argued that peoples of temperate climates were industrious and inventive while peoples of tropical climates were indolent, and that this followed directly from the climate itself. This argument is an example of",
   choices=[
     "Environmental determinism, since the physical environment is treated as the cause of cultural outcomes",
     "Possibilism, since the writer describes a range of outcomes",
     "Sustainability, since the writer is discussing long-term conditions",
     "Land use, since climates shape agriculture",
     "A natural resource argument, since climate is a resource"],
   ans=0,
   why="EK PSO-1.B.2 names environmental determinism as the earlier of the two theories, and its signature is exactly this move: physical conditions are made to explain human character and achievement. That the conclusions ranked peoples by climate is why the theory was discarded."),

 dict(q="A geographer studying the Netherlands notes that much of the country lies below sea level, that this constrains what can be built and farmed, and that Dutch society responded by developing dikes, pumps, and polders. Which theory does this account illustrate?",
   choices=[
     "Possibilism, since the environment sets limits within which a society chooses its response",
     "Environmental determinism, since sea level determined Dutch history",
     "Environmental determinism, since the Dutch had no alternative",
     "Neither theory, since engineering is not a geographic subject",
     "Sustainability, since dikes must be maintained"],
   ans=0,
   why="EK PSO-1.B.2 describes the shift from determinism to possibilism, and the possibilist reading is that physical conditions bound the menu without picking the dish. The account credits a social choice among available responses, which is what determinism denies."),

 dict(q="Which statement best expresses why environmental determinism was abandoned by geographers?",
   choices=[
     "It could not account for very different societies developing in similar environments, and its conclusions were used to rank peoples",
     "It was too difficult to test with the data available at the time",
     "It applied only to agricultural societies",
     "It was replaced because possibilism is easier to teach",
     "It was correct but became unfashionable"],
   ans=0,
   why="The theory fails empirically because similar climates host radically different cultures, economies and technologies, so the environment cannot be doing the causal work claimed. It also failed morally, since its explanations became justifications for hierarchy among peoples."),

 dict(q="A planner argues that a mountain valley's steep slopes and short growing season make large-scale grain farming impractical, but that the same conditions support dairying, forestry, and tourism, and that the community will choose among them. This reasoning is",
   choices=[
     "Possibilist, because the environment narrows the options while the society selects among them",
     "Determinist, because the slopes decide the outcome",
     "Determinist, because the growing season is fixed",
     "Outside both theories, because economics rather than environment is involved",
     "Possibilist, because the environment imposes no constraints at all"],
   ans=0,
   why="Possibilism is not the claim that the environment is irrelevant; it is the claim that it constrains rather than determines. Naming several viable land uses and leaving the choice to the community is precisely that structure."),

 dict(q="Which of the following is a nonrenewable natural resource?",
   choices=[
     "Crude oil, which forms over geological time and is consumed far faster than it is replaced",
     "Timber, which regrows on a decadal cycle if replanted",
     "Solar radiation, which arrives continuously",
     "Wind, which is generated by atmospheric circulation",
     "Fish stocks, which reproduce annually"],
   ans=0,
   why="PSO-1.B.1 names natural resources as a concept without defining the categories, and the operative distinction is the rate of replacement relative to the rate of use. A stock formed over millions of years is nonrenewable on any human timescale."),

 dict(q="A fishery's stock regenerates at about 20,000 tonnes a year. Catches have run at 34,000 tonnes a year for a decade and the stock has fallen steadily. The most accurate description is that",
   choices=[
     "The fishery is being harvested beyond its sustainable yield, so a renewable resource is being depleted",
     "The fishery is nonrenewable, since the stock is falling",
     "The fishery is sustainable, since fish reproduce every year",
     "The catch is irrelevant, since fish stocks are determined by ocean conditions alone",
     "The fishery will recover automatically if catches continue"],
   ans=0,
   why="Renewability is a property of the resource and sustainability is a property of the use made of it, so a renewable stock can be destroyed by a harvest that outruns its regeneration. Twenty thousand tonnes replaced against thirty-four thousand removed is a deficit every year."),

 dict(q="Which definition of sustainability best matches the way the concept is used in this course?",
   choices=[
     "Using resources in ways that meet present needs without compromising the ability of future generations to meet theirs",
     "Leaving the environment entirely untouched by human activity",
     "Maximizing economic output from a resource in the shortest possible time",
     "Replacing every renewable resource with a nonrenewable one",
     "Confining all human activity to urban areas"],
   ans=0,
   why="PSO-1.B.1 lists sustainability among the concepts of nature and society. The standard formulation is intergenerational: use is sustainable if it can continue without foreclosing the options of the people who come after, which is neither preservation nor maximization."),

 dict(q="A satellite land-cover classification for a district reports categories such as cropland, pasture, forest, wetland, and built-up area. The classification is a record of",
   choices=[
     "Land use, one of the concepts of nature and society named in the framework",
     "Sustainability, since land cover changes over time",
     "Environmental determinism, since the land determines the categories",
     "Natural resources only, since none of these categories involves people",
     "Possibilism, since several categories are possible"],
   ans=0,
   why="EK PSO-1.B.1 names land use alongside sustainability and natural resources. A classification of how each parcel of the surface is occupied and worked is exactly what the term denotes, and several of the listed categories exist only because of human activity."),

 dict(q="Two neighboring countries share the same climate, terrain, and mineral endowment, yet one has a heavily industrial economy and the other an agricultural one. This comparison is most damaging to which claim?",
   choices=[
     "That the physical environment determines a society's economic development",
     "That natural resources can be classified as renewable or nonrenewable",
     "That land use can be mapped from imagery",
     "That resource use can be unsustainable",
     "That environments set limits on what is possible"],
   ans=0,
   why="A controlled comparison in which the environment is held constant and the outcomes differ is precisely the evidence determinism cannot absorb. It leaves the possibilist claim untouched, since limits are compatible with different choices being made inside them."),

 dict(q="An aquifer is recharged by rainfall at 40 million cubic metres a year. A city withdraws 65 million. What is the geographic consequence over time?",
   choices=[
     "The water table falls year after year, and wells, land subsidence, and saltwater intrusion become progressively worse",
     "Nothing changes, because groundwater is a renewable resource",
     "The recharge rate rises to match the withdrawal",
     "The aquifer becomes a nonrenewable resource",
     "The city's withdrawals become sustainable once the water table stabilizes"],
   ans=0,
   why="A withdrawal exceeding recharge is a stock being drawn down, and the physical consequences follow from the falling water table rather than from the label on the resource. Recharge is set by rainfall and geology and does not respond to demand."),

 dict(q="Which of these is the clearest example of a society changing its land use in response to an environmental constraint without that constraint dictating the outcome?",
   choices=[
     "Terracing steep hillsides to grow rice where flat fields are impossible",
     "Abandoning a region entirely because rainfall declined",
     "Building on a floodplain and being flooded",
     "Mining a mineral deposit until it is exhausted",
     "Measuring the slope of a hillside with a survey instrument"],
   ans=0,
   why="Terracing is the possibilist case in its clearest form: the slope forecloses flat-field cultivation and the society answers with an engineered alternative rather than either abandoning the site or being defeated by it."),

 dict(q="A government subsidizes irrigation so heavily that farmers in a semi-arid region grow a water-intensive crop, drawing the regional river below the level needed to reach its delta. Which concepts are most directly at stake?",
   choices=[
     "Land use and sustainability, since a policy changed what the land is used for and the use exceeds what the water supply can support",
     "Environmental determinism, since the climate produced the outcome",
     "Only natural resources, since water is the resource involved",
     "Neither sustainability nor land use, since the change was caused by policy rather than by nature",
     "Possibilism only, since farmers had a choice of crops"],
   ans=0,
   why="EK PSO-1.B.1 names both land use and sustainability, and the case joins them: the cropping pattern is a land-use decision and its water demand exceeds the river's capacity to supply it indefinitely. That a policy caused it does not remove it from the framework's concepts."),

 dict(q="Which of the following would a possibilist regard as the correct way to state the influence of a harsh Arctic climate on human settlement?",
   choices=[
     "The climate makes some ways of living costly or impossible, and the societies there developed particular technologies and social arrangements in response",
     "The climate made the development of complex societies impossible",
     "The climate had no influence on how people there live",
     "The climate determined the languages spoken there",
     "The climate guarantees that resource extraction will be the only economic activity"],
   ans=0,
   why="Possibilism keeps the environmental constraint and denies the environmental cause, so the correct statement names what is foreclosed and credits the society with the response. The absolute-impossibility and no-influence statements are the two errors the theory sits between."),

 dict(q="Copper is mined, used, discarded, and in part recovered from scrap. Which statement about its status as a resource is most accurate?",
   choices=[
     "It is nonrenewable in the ground but partly recoverable through recycling, which extends the usable stock without replacing the ore",
     "It is renewable, because it can be recycled indefinitely with no losses",
     "It is renewable, because new deposits form each year",
     "Recycling has no effect on the demand for newly mined ore",
     "It is neither renewable nor nonrenewable, since metals are elements"],
   ans=0,
   why="The ore body does not regenerate on a human timescale, so extraction is drawdown, while recycling returns metal already extracted to use and reduces how fast the remaining ore must be mined. Neither collection nor reprocessing is perfectly efficient, so the stock is extended rather than made renewable."),

 dict(q="A textbook claims that river valleys 'gave rise to' the earliest civilizations. A geographer objects that many river valleys never hosted such societies. The objection is best understood as",
   choices=[
     "A challenge to a deterministic explanation, since the same environmental condition did not produce the same outcome",
     "A challenge to possibilism, since it shows that the environment matters",
     "A defense of environmental determinism at a different scale",
     "An argument about land use rather than about theory",
     "An argument that river valleys are not natural resources"],
   ans=0,
   why="If a condition is offered as the cause of an outcome, cases with the condition and without the outcome are decisive counterexamples. That is the standard form of the empirical case against determinism and the reason possibilism replaced it."),

 dict(q="Which pair correctly matches a resource with the reason it is classified as renewable or nonrenewable?",
   choices=[
     "Groundwater in a deep fossil aquifer is nonrenewable because its recharge is negligible on a human timescale",
     "Coal is renewable because new seams are discovered regularly",
     "Old-growth forest is renewable because trees can be planted",
     "Sunlight is nonrenewable because it is not available at night",
     "Soil is renewable because it can be moved from one field to another"],
   ans=0,
   why="The classification turns on whether the stock is replaced as fast as it is used. A fossil aquifer that receives almost no recharge is drawn down like an ore body, whereas discovery, replanting of a different forest, the day-night cycle and relocation change none of the relevant rates."),

 dict(q="A city converts 300 hectares of market gardens on its edge into low-density housing. Which is the most complete geographic description of what has happened?",
   choices=[
     "A change in land use that removes food-producing land from the urban fringe and commits the site to a use that is costly to reverse",
     "A change in the climate of the urban fringe",
     "An increase in the region's stock of natural resources",
     "An application of environmental determinism to city planning",
     "A demonstration that suburban land use is sustainable"],
   ans=0,
   why="EK PSO-1.B.1 names land use, and conversion is the change of one category into another. Housing is among the least reversible conversions, since the buildings, services and property boundaries all outlast any decision to change course."),

 dict(q="Which of the following best illustrates a sustainability trade-off rather than an unambiguous gain?",
   choices=[
     "A wind farm reduces fossil fuel burning but occupies grazing land and requires mined materials for its turbines",
     "A city plants trees along its streets",
     "A factory installs equipment that lowers its water use with no other change",
     "A household replaces its lightbulbs with more efficient ones",
     "A country maps its remaining forests"],
   ans=0,
   why="A trade-off requires a cost to be incurred somewhere as the benefit is obtained, and the wind farm's benefit in emissions is bought with land and with extraction elsewhere. The other options improve one thing without a stated cost, which is why they are not trade-offs."),

 dict(q="A researcher writes that 'the monsoon shapes but does not dictate the agricultural calendar of the region.' This sentence is",
   choices=[
     "A possibilist formulation, because it grants environmental influence while reserving the decision to the society",
     "A determinist formulation, because it says the monsoon shapes agriculture",
     "A statement about natural resources rather than about theory",
     "Incompatible with both theories",
     "A claim that the monsoon is irrelevant to agriculture"],
   ans=0,
   why="The sentence is built to separate the two verbs: shaping is constraint and dictating is causation, and possibilism accepts the first while rejecting the second. That is exactly the distinction PSO-1.B.2's shift is about."),

 dict(q="Which question would a geographer studying human-environmental interaction be LEAST likely to treat as answerable by the environment alone?",
   choices=[
     "Why one country with abundant oil is wealthy and another with equal reserves is not",
     "Where the treeline lies on a mountain range",
     "How much rain the windward slope receives",
     "Which crops can survive a 90-day growing season",
     "Where a river's floodplain lies"],
   ans=0,
   why="Four of these are physical facts with physical answers, whereas the distribution of wealth from an identical endowment depends on institutions, ownership and history. Treating the last as environmentally caused is the determinist error the course asks students to identify."),

 dict(q="A coastal community bans construction within 100 metres of the shoreline after repeated storm damage. In the framework's vocabulary, this decision is best described as",
   choices=[
     "A land-use rule adopted to make settlement of the coast more sustainable in the face of an environmental hazard",
     "An application of environmental determinism, since the storms decided the policy",
     "A conversion of a nonrenewable resource into a renewable one",
     "A rejection of possibilism, since the community accepted a limit",
     "A change with no geographic consequences, since it only prevents new building"],
   ans=0,
   why="EK PSO-1.B.1 names land use and sustainability, and a setback rule is a land-use instrument aimed at making occupation of a hazardous zone endurable over time. Choosing a rule in response to a hazard is a possibilist response rather than a rejection of possibilism."),

 dict(q="Which of the following is the strongest reason that 'natural resource' is a social category as well as a physical one?",
   choices=[
     "A substance becomes a resource only when a society has a use and a technology for it, which is why uranium was not a resource before the twentieth century",
     "Resources are owned by governments",
     "Resources are located using maps",
     "Resources are always found in remote places",
     "Resources are counted by national statistical offices"],
   ans=0,
   why="What is in the ground does not change when a use for it is discovered; what changes is whether it counts as a resource at all. That dependence on technology and demand is what makes the category social as well as physical."),

 dict(q="An argument that a country's national character was forged by its mountains, and that its people are therefore naturally independent, should be identified as",
   choices=[
     "Environmental determinism, and treated with the suspicion the course attaches to that theory",
     "Possibilism, since mountains offer several possibilities",
     "A sustainability argument about mountain environments",
     "A land-use claim about upland agriculture",
     "A neutral description with no theoretical content"],
   ans=0,
   why="Attributing a collective personality to a landform is the determinist move in its most recognizable form, and EK PSO-1.B.2's account of the shift away from it is the reason the course expects it to be named rather than accepted."),

 dict(q="Two land uses compete for the same peri-urban parcel: an intensive vegetable farm and a warehouse. Which consideration is most clearly a sustainability consideration rather than simply an economic one?",
   choices=[
     "Whether paving the parcel permanently removes soil that took centuries to form and increases downstream flooding",
     "Which use pays the higher rent per hectare",
     "Which use employs more people in the first year",
     "Which use is closer to the motorway junction",
     "Which use the current owner prefers"],
   ans=0,
   why="A sustainability question asks what the decision forecloses for the future, and soil formation on a centuries-long timescale plus altered runoff are effects that outlast the tenancy. Rent, first-year jobs, access and owner preference are all present-period accounting."),

 dict(q="A student writes that possibilism means 'the environment does not matter because technology can overcome anything.' The best correction is that",
   choices=[
     "Possibilism holds that the environment sets real limits and that societies choose among the options remaining inside them",
     "Possibilism holds that the environment determines outcomes in the long run",
     "Possibilism applies only to industrialized societies",
     "The student is right, since possibilism replaced determinism entirely",
     "Possibilism is a theory about land use rather than about environment and society"],
   ans=0,
   why="EK PSO-1.B.2 presents possibilism as the successor theory, not as a denial of environmental influence. Collapsing it into technological optimism removes the constraint that the theory is built around and makes it unfalsifiable."),

 dict(q="A country's energy sources are recorded below. Using the table, what share of its electricity comes from sources that are renewable?",
   table=dict(
     headers=["Source", "Share of electricity (%)"],
     rows=[
       ["Coal", "38"],
       ["Natural gas", "22"],
       ["Hydroelectric", "19"],
       ["Wind", "12"],
       ["Solar", "9"]]),
   choices=[
     "40 percent, from hydroelectric, wind, and solar together",
     "60 percent, from coal and natural gas together",
     "19 percent, from hydroelectric alone",
     "21 percent, from wind and solar together",
     "100 percent, since electricity itself is renewable"],
   ans=0,
   why="Hydroelectric, wind and solar draw on flows replenished continuously and together account for 19 plus 12 plus 9. Coal and gas are stocks formed over geological time, so the two groups partition the table into 40 and 60 percent."),

 dict(q="Four fisheries are managed by quota. Using the table, which fishery is being harvested unsustainably by the widest margin?",
   table=dict(
     headers=["Fishery", "Annual regeneration (tonnes)", "Annual catch (tonnes)"],
     rows=[
       ["Fishery A", "50,000", "46,000"],
       ["Fishery B", "18,000", "27,000"],
       ["Fishery C", "80,000", "92,000"],
       ["Fishery D", "9,000", "9,000"]]),
   choices=[
     "Fishery B, whose catch exceeds regeneration by half again as much as the stock can replace",
     "Fishery C, whose catch exceeds regeneration by the largest number of tonnes",
     "Fishery A, whose catch is the second largest in the table",
     "Fishery D, whose catch exactly equals its regeneration",
     "None of them, because every fishery has a quota"],
   ans=0,
   why="Overharvest measured as a share of what the stock can replace gives minus 8 percent, plus 50 percent, plus 15 percent and zero, so the largest tonnage excess and the largest proportional excess belong to different fisheries. A small stock is destroyed by a smaller absolute overshoot."),

 dict(q="A district's land is classified as shown. Using the table, how much of the district is in uses that generate food, and what has happened to that share since 1990?",
   table=dict(
     headers=["Land use", "1990 (hectares)", "2020 (hectares)"],
     rows=[
       ["Cropland", "24,000", "18,000"],
       ["Pasture", "12,000", "10,000"],
       ["Forest", "9,000", "8,000"],
       ["Built-up", "5,000", "14,000"]]),
   choices=[
     "28,000 hectares in 2020, down from 36,000 in 1990, while built-up land nearly tripled",
     "28,000 hectares in 2020, unchanged since 1990",
     "18,000 hectares in 2020, since only cropland produces food",
     "36,000 hectares in 2020, since the district's total area is unchanged",
     "42,000 hectares in 2020, since forest also produces food"],
   ans=0,
   why="Cropland plus pasture is 36,000 hectares in 1990 and 28,000 in 2020, a loss of 8,000, while built-up land rises from 5,000 to 14,000. The district's total is constant at 50,000, so the built-up gain comes almost entirely out of food-producing land."),

 dict(q="Groundwater accounts for four basins are shown. Using the table, which basin can sustain its current withdrawal indefinitely?",
   table=dict(
     headers=["Basin", "Annual recharge (million m3)", "Annual withdrawal (million m3)"],
     rows=[
       ["Basin 1", "120", "140"],
       ["Basin 2", "60", "58"],
       ["Basin 3", "200", "260"],
       ["Basin 4", "45", "70"]]),
   choices=[
     "Basin 2, the only basin whose withdrawal is below its recharge",
     "Basin 3, because it has the largest annual recharge in the table",
     "Basin 1, because its annual deficit is the smallest in absolute terms",
     "Basin 4, because it has the smallest recharge and so the least to replace",
     "All four, because groundwater is a renewable resource everywhere"],
   ans=0,
   why="Only one basin withdraws less than it receives, and that comparison is the whole test of whether a stock is being drawn down. The largest recharge, the smallest deficit and the smallest recharge all belong to basins that are in deficit nonetheless."),

 dict(q="Four countries with similar tropical climates report the figures below. Using the table, which conclusion is best supported?",
   table=dict(
     headers=["Country", "Mean annual rainfall (mm)", "GDP per capita (US$)", "Share of workforce in agriculture (%)"],
     rows=[
       ["Country W", "1,800", "1,200", "62"],
       ["Country X", "1,750", "14,600", "9"],
       ["Country Y", "1,900", "3,400", "38"],
       ["Country Z", "1,820", "22,100", "4"]]),
   choices=[
     "Rainfall is nearly identical across the four while income differs by a factor of more than eighteen, which is evidence against environmental determinism",
     "Higher rainfall produces higher income, since the wettest country is the richest",
     "Rainfall determines the share of the workforce in agriculture",
     "The table supports environmental determinism, since all four countries are tropical",
     "No conclusion is possible, because climate cannot be compared across countries"],
   ans=0,
   why="Rainfall spans 1,750 to 1,900 millimetres, a range of under 9 percent, while income runs from 1,200 to 22,100 dollars, a range of more than eighteenfold. A near-constant environmental variable cannot explain an outcome that varies that widely, and the wettest country is not the richest."),
]
