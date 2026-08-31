# AP HUMAN GEOGRAPHY 6.5 The Internal Structure of Cities -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding PSO-6, "The presence
# and growth of cities vary across geographical locations because of physical
# geography and resources." Learning objective PSO-6.D, "Explain the internal
# structure of cities using various models and theories." Suggested skill 1.E,
# explain the strengths, weaknesses, and limitations of different geographic
# models and theories in a specified context.
#
# Essential knowledge -- ONE statement, and it is a list of six:
#   PSO-6.D.1  Models and theories that are useful for explaining internal
#              structures of cities include the Burgess concentric-zone model,
#              the Hoyt sector model, the Harris and Ullman multiple-nuclei
#              model, the galactic city model, bid-rent theory, and urban models
#              drawn from Latin America, Southeast Asia, and Africa.
#
# THE SUGGESTED SKILL IS THE TOPIC. Skill 1.E asks for the STRENGTHS, WEAKNESSES
# AND LIMITATIONS of models in a specified context, and the CED lists six
# because no one of them accounts for every city. So this module spends as much
# effort on what each model misses as on what each one says: items 18, 19, 20,
# 24 and 29 are limitation items, and item 16 asks directly why a list of six
# was necessary.
#
# THE SHAPE EACH MODEL CLAIMS, which is what every application item turns on:
#   concentric zone   RINGS around a single centre, each ring a different land
#                     use, the city growing outward from the middle
#   sector            WEDGES running outward from the centre, each following a
#                     transport corridor, so a high-rent district extends as a
#                     strip rather than as a ring
#   multiple nuclei   SEVERAL separate centres, each with its own specialization,
#                     with incompatible uses repelling one another
#   galactic city     a weakened centre surrounded by edge cities strung along a
#                     ring road, held together by the car
#   bid-rent          not a shape at all but the MECHANISM -- land value falls
#                     with distance from the centre, which is why any of the
#                     shapes above sorts uses by what each can pay
# Items 2 to 11 walk them, and items 22 and 23 are the two discriminations
# students actually get wrong: rings against wedges, and wedges against nuclei.
#
# THE THREE REGIONAL MODELS ARE ON THE LIST FOR A REASON, and item 13 keys on
# the sharpest instance of it. In the Latin American model the wealthiest housing
# runs outward along a spine from the centre and the poorest settlement is at the
# PERIPHERY, which is the reverse of the income gradient the Burgess and Hoyt
# models were drawn from. A student who has learned only the first three models
# will read a real income map backwards. The Southeast Asian model is organized
# on a former colonial PORT zone rather than a single central business district,
# and the African model characteristically shows more than one central business
# district -- a colonial one, a traditional one and an open-air market zone.
#
# WHAT THIS MODULE WILL NOT DO: assert that a named real city fits a named model.
# Every application item describes a pattern and asks which model it matches, so
# the key rests on the described pattern rather than on a contestable claim about
# a real place. NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# SYNONYM CARE. `geo_check` treats {"concentric zone model", "burgess model"},
# {"sector model", "hoyt model"} and {"multiple nuclei model", "harris and
# ullman model", "harris-ullman model"} as three constructs. Each item therefore
# names a given model in exactly ONE way; offering two names for one model in a
# single choice list would make the item unanswerable.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.5", "The Internal Structure of Cities", 6)

QUESTIONS = [
 dict(q="Which set of models does the framework name as useful for explaining the internal structure of cities?", choices=[
   "The Burgess concentric-zone model, the Hoyt sector model, the Harris and Ullman multiple-nuclei model, the galactic city model, bid-rent theory, and models drawn from Latin America, Southeast Asia and Africa",
   "The rank-size rule, the primate city, gravity, and central place theory",
   "Site, situation, suburbanization, and sprawl",
   "The demographic transition model and the epidemiological transition model",
   "Von Thunen's model, Weber's least cost theory, and Rostow's stages"], ans=0,
   why="EK PSO-6.D.1 names exactly this set. The four principles in the second option belong to EK PSO-6.C.1 and explain relationships BETWEEN cities, whereas these models explain the arrangement of land uses WITHIN one."),

 dict(q="What arrangement of land uses does the concentric zone model describe?", choices=[
   "A series of rings around a single central business district, each ring given over to a different land use",
   "Wedges running outward from the centre along transport routes",
   "Several separate specialized centres with no single dominant core",
   "A weakened centre surrounded by edge cities along a ring road",
   "A strip of high-status housing running from the centre to the periphery"], ans=0,
   why="EK PSO-6.D.1 names the Burgess concentric-zone model among the models explaining internal city structure. Its distinctive claim is that use varies with distance from one centre and not with direction, which is what produces rings rather than wedges."),

 dict(q="What does the concentric zone model place immediately around the central business district?", choices=[
   "A zone of transition, mixing industry with deteriorating and subdivided housing",
   "The city's most expensive residential district",
   "Open farmland",
   "A ring road lined with edge cities",
   "The city's principal park system"], ans=0,
   why="EK PSO-6.D.1 names the Burgess concentric-zone model among the models useful for explaining internal city structure. The zone next to the centre is under constant pressure from the expanding business district, so long-term investment there is discouraged and the housing deteriorates."),

 dict(q="What assumption about urban growth does the concentric zone model rest on?", choices=[
   "That a city grows outward from one centre, with each ring pushing into the one beyond it",
   "That a city grows inward from its edges",
   "That a city grows only along its transport corridors",
   "That a city has several equally important centres from the beginning",
   "That a city's land uses never change position"], ans=0,
   why="EK PSO-6.D.1 names the Burgess concentric-zone model, and its rings are the record of a process rather than a static plan. Growth radiating from a single core is what makes concentric bands the expected outcome, and it is also the assumption that fails wherever a city has more than one core."),

 dict(q="What arrangement of land uses does the sector model describe?", choices=[
   "Wedges extending outward from the centre, so a given land use forms a strip from the core to the edge",
   "Rings at equal distances from the centre",
   "A grid of identical square districts",
   "Several unrelated centres scattered across the metropolitan area",
   "A single central district with no surrounding development"], ans=0,
   why="EK PSO-6.D.1 names the Hoyt sector model among the models explaining internal city structure. Its distinctive claim is that land use varies with DIRECTION from the centre as well as with distance, which turns each band into a wedge."),

 dict(q="Why does the sector model expect land uses to follow transport corridors outward?", choices=[
   "A corridor makes the land along it accessible, so a use established near the centre expands outward along the route that serves it",
   "Because corridors are the only land on which building is permitted",
   "Because transport routes always run in circles around a city",
   "Because corridors have the cheapest land in a city",
   "Because land uses avoid transport routes"], ans=0,
   why="EK PSO-6.D.1 names the Hoyt sector model among the models useful for explaining internal city structure. Accessibility is what makes a site usable for a given purpose, so an activity extends along the direction in which its accessibility persists rather than in every direction equally."),

 dict(q="What is the central claim of the multiple nuclei model?", choices=[
   "A city develops around several separate specialized centres rather than around one dominant core",
   "A city's land uses form rings around a single centre",
   "A city's land uses form wedges along transport routes",
   "A city's land value falls smoothly with distance from the centre",
   "A city has no identifiable land-use pattern at all"], ans=0,
   why="EK PSO-6.D.1 names the Harris and Ullman multiple-nuclei model among the models explaining internal city structure. Its departure from the earlier two is that it abandons the single centre those both assume."),

 dict(q="Why does the multiple nuclei model expect certain land uses to locate away from one another?", choices=[
   "Some activities are incompatible -- heavy industry and high-status housing repel each other -- while others benefit from clustering together",
   "Because a city's government assigns each use a district",
   "Because all land uses require identical sites",
   "Because activities are distributed at random",
   "Because every use must be equally far from the centre"], ans=0,
   why="EK PSO-6.D.1 names the Harris and Ullman multiple-nuclei model among the models useful for explaining internal city structure. Attraction between like uses and repulsion between unlike ones is the mechanism that produces several specialized nodes instead of one general centre."),

 dict(q="What does the galactic city model describe?", choices=[
   "A metropolitan area in which edge cities strung along a ring road have taken functions from a weakened traditional centre",
   "A city that grows in rings from a single core",
   "A city whose land uses form wedges along rail lines",
   "A pre-industrial city with a walled centre",
   "A city with no suburbs of any kind"], ans=0,
   why="EK PSO-6.D.1 names the galactic city model among the models explaining internal city structure. It is the model built for a metropolitan area whose employment and retail have decentralized, which the three earlier models were not designed to describe."),

 dict(q="Which technology is the galactic city model built around?", choices=[
   "The automobile and the high-capacity road network, which allow movement between outlying nodes without passing through the centre",
   "The electric streetcar",
   "The passenger railway terminating at a central station",
   "The pedestrian street",
   "The canal network"], ans=0,
   why="EK PSO-6.D.1 names the galactic city model among the models useful for explaining internal city structure. Earlier transport technologies converged on a single terminus, which reinforced a single centre, while a road network permits travel from any outlying point to any other."),

 dict(q="What does bid-rent theory contribute to explaining a city's internal structure?", choices=[
   "It supplies the mechanism -- land nearer the centre is more expensive, so only uses earning enough per unit of land can occupy it",
   "It describes a shape made of rings",
   "It describes a shape made of wedges",
   "It describes several separate nuclei",
   "It states that all urban land has the same value"], ans=0,
   why="EK PSO-6.D.1 lists bid-rent theory alongside the shape models rather than as one of them. It is not a picture of a city but the reason a picture arises: competing uses bid for central land and the one earning most per square metre wins it."),

 dict(q="What is distinctive about the arrangement of high-status housing in the Latin American city model?", choices=[
   "It runs outward from the centre as a spine along a major boulevard rather than forming an outer ring",
   "It occupies the outermost ring of the metropolitan area",
   "It is scattered randomly across the city",
   "It is confined entirely to the central business district",
   "It forms a complete ring immediately outside the centre"], ans=0,
   why="EK PSO-6.D.1 names urban models drawn from Latin America among the models explaining internal city structure. The elite spine is the feature that most sharply distinguishes that model from the concentric and sector models drawn from other regions."),

 dict(q="How does the income gradient in the Latin American city model differ from that in the concentric zone model?", choices=[
   "The poorest settlement is at the periphery and wealth is nearer the centre, which is the reverse of the pattern the earlier model describes",
   "The two gradients are identical",
   "There is no income gradient in either model",
   "The wealthiest housing is at the periphery in both models",
   "Income falls with distance from the centre in the concentric zone model"], ans=0,
   why="EK PSO-6.D.1 names urban models drawn from Latin America alongside the Burgess concentric-zone model, and the two disagree about direction. A student who has learned only the earlier model reads such a city's income map backwards, which is exactly why the CED lists regional models."),

 dict(q="What is organizationally distinctive about the Southeast Asian city model?", choices=[
   "It is focused on a former colonial port zone rather than on a single central business district",
   "It has no commercial activity of any kind",
   "It consists entirely of concentric rings",
   "It is organized around a ring road and edge cities",
   "It contains only one land use throughout"], ans=0,
   why="EK PSO-6.D.1 names urban models drawn from Southeast Asia among the models explaining internal city structure. Organizing on a port rather than on a downtown is a consequence of how such cities grew, and it is why a model assuming one central business district fits them poorly."),

 dict(q="What is characteristically distinctive about the African city model?", choices=[
   "It shows more than one central business district -- typically a colonial one, a traditional one and an open-air market zone",
   "It shows no commercial districts at all",
   "It is arranged in perfect concentric rings around one core",
   "It has a single central business district and nothing else",
   "It is organized entirely around a ring road"], ans=0,
   why="EK PSO-6.D.1 names urban models drawn from Africa among the models useful for explaining internal city structure. Several commercial cores of different origins coexisting in one city is a structure the single-centre models have no way to represent."),

 dict(q="Why does the framework list six models rather than one?", choices=[
   "Cities differ in when and how they grew, so a model built from one region and era does not describe cities that grew differently elsewhere",
   "Because geographers cannot agree on which single model is correct",
   "Because each model applies to a different size of city",
   "Because the framework requires exactly six models for every topic",
   "Because the models are all identical in content"], ans=0,
   why="EK PSO-6.D.1 gives a list and calls its members models USEFUL FOR EXPLAINING internal city structure, and the suggested skill for this topic is explaining strengths, weaknesses and limitations in a specified context. A model is a compressed account of the process that built a particular kind of city."),

 dict(q="A metropolitan area has a modest downtown, four office and retail concentrations spaced around an orbital motorway, and most commuting occurring between the outer nodes. Which model fits best?", choices=[
   "The galactic city model, since the centre has been weakened and outlying nodes on a ring road carry the activity",
   "The concentric zone model, since the area has a downtown",
   "The sector model, since the motorway is a transport route",
   "The Latin American city model, since there is a spine",
   "The Southeast Asian city model, since there are several nodes"], ans=0,
   why="EK PSO-6.D.1 names the galactic city model among the models explaining internal city structure, and each element of the stem is one of its features. A ring road with commuting between outer nodes is precisely the pattern the earlier single-centre models cannot represent."),

 dict(q="What is the most important limitation shared by all the models in the framework's list?", choices=[
   "Each is a simplification built from particular cities at a particular time, so no city matches any of them exactly",
   "None of them makes any prediction that could be checked",
   "They apply only to cities with more than a million residents",
   "They describe relationships between cities rather than within them",
   "They have no limitations, which is why the framework lists them"], ans=0,
   why="EK PSO-6.D.1 calls them models USEFUL FOR EXPLAINING internal city structure, and the suggested skill for this topic is explaining their strengths, weaknesses and limitations. Simplification is what makes a model usable and it is also the source of every mismatch."),

 dict(q="Why do the earliest models of internal city structure fit contemporary metropolitan areas less well than they once did?", choices=[
   "They were drawn from cities organized around a single centre reached by rail and on foot, and widespread car ownership decentralized both employment and retail",
   "Because cities have stopped growing entirely",
   "Because contemporary cities have no land-use pattern",
   "Because the models were never intended to describe real cities",
   "Because contemporary cities are smaller than the cities the models described"], ans=0,
   why="EK PSO-6.D.1 lists the galactic city model alongside the older three, which is the CED itself acknowledging that the earlier ones needed supplementing. A model encodes the transport technology of its period, so a change in that technology is what dates it."),

 dict(q="A geographer argues that two of the framework's models can describe one city at the same time. What is the strongest support?", choices=[
   "The models emphasize different features -- distance bands, directional wedges and separate nuclei -- and a real city can display more than one of them at once",
   "The models are identical, so any city fits all of them",
   "Only one model can ever apply to a city",
   "Models cannot be applied to real cities at all",
   "A city can be described only by the model of its own region"], ans=0,
   why="EK PSO-6.D.1 lists six models as useful for explaining internal structures, without assigning one to each city. Each isolates a different regularity, so a city may show rings of building age, a wedge of high-status housing and a set of specialized outlying nodes simultaneously."),

 dict(q="At which scale do the framework's models of internal city structure operate?", choices=[
   "The metropolitan scale, since each describes the arrangement of districts within a single urban area",
   "The global scale, since they compare countries",
   "The scale of a single building",
   "The national scale, since they rank a country's cities",
   "No scale, since the models are purely theoretical"], ans=0,
   why="EK PSO-6.D.1 describes these as models explaining INTERNAL structures of cities, so their subject is one urban area's districts. Ranking a country's cities is what EK PSO-6.C.1's principles do, and confusing the two lists is the commonest error across this unit."),

 dict(q="One city's manufacturing forms a complete band at a fixed distance from the centre; another's forms a strip running from the centre to the edge along a rail line. Which models do the two patterns illustrate?", choices=[
   "The first illustrates the concentric zone model and the second the sector model",
   "The first illustrates the sector model and the second the concentric zone model",
   "Both illustrate the multiple nuclei model",
   "Both illustrate the galactic city model",
   "Neither can be described by any of the framework's models"], ans=0,
   why="EK PSO-6.D.1 names both models, and the shapes distinguish them completely. A band at a constant distance varies with distance alone, while a strip along one route varies with direction, which is the difference between a ring and a wedge."),

 dict(q="What distinguishes a city described by the sector model from one described by the multiple nuclei model?", choices=[
   "The sector model keeps a single dominant centre from which wedges radiate, while the multiple nuclei model has several centres and no dominant one",
   "The sector model has several centres and the multiple nuclei model has one",
   "The two models describe the same arrangement under different names",
   "The sector model applies only to small cities",
   "The multiple nuclei model arranges land uses in rings"], ans=0,
   why="EK PSO-6.D.1 names both among the models explaining internal city structure. Wedges must radiate from something, so the sector model retains the single core it inherited, while the multiple nuclei model's whole innovation is to give that up."),

 dict(q="Why should a model developed from cities in one world region be applied cautiously elsewhere?", choices=[
   "The pattern a model encodes reflects the history, transport technology and land market of the cities it was built from, and those differ between regions",
   "Because models are valid only in the country where they were written",
   "Because all cities are in fact identical",
   "Because models cannot be tested against real cities",
   "Because the framework forbids comparing cities across regions"], ans=0,
   why="EK PSO-6.D.1 lists models drawn from Latin America, Southeast Asia and Africa alongside the older ones, which is the CED making this point in its own structure. A colonial port, a market zone and a peripheral squatter settlement are features the earlier models had no reason to include."),

 dict(q="Which pairing of a described pattern with the model it illustrates is CORRECT?", choices=[
   "Elite housing running outward from the centre along one boulevard, with unserviced settlement at the metropolitan edge, matched to the Latin American city model",
   "Rings of land use around one centre, matched to the multiple nuclei model",
   "Several specialized centres with no dominant core, matched to the concentric zone model",
   "Wedges of land use along transport corridors, matched to the galactic city model",
   "A ring road lined with edge cities, matched to the sector model"], ans=0,
   why="EK PSO-6.D.1 names six models with distinct shapes and features. Only one pairing here matches a described pattern to the model whose account it satisfies; each of the others attaches a description to a model that claims a different shape."),

 dict(q="Land values by distance from one city's centre are recorded below. Using the accompanying figures, what do they demonstrate?",
   table=dict(headers=["Distance from the centre (kilometres)", "Land value (currency units per square metre)"],
     rows=[["0", "4,800"],
           ["2", "1,150"],
           ["5", "420"],
           ["10", "160"],
           ["20", "45"]]),
   choices=[
   "Bid-rent theory, since value falls steeply from 4,800 at the centre to 45 twenty kilometres out, most sharply over the first two kilometres",
   "The multiple nuclei model, since values differ across the city",
   "The galactic city model, since the outermost value is lowest",
   "That land value is unrelated to distance from the centre",
   "That land value rises with distance from the centre"], ans=0,
   why="Value falls at every step and the fall is steepest at the start, dropping by 3,650 currency units over the first two kilometres and by 115 over the last ten. EK PSO-6.D.1 names bid-rent theory among the models useful for explaining internal city structure, and a steep distance-decay in land value is the mechanism it describes."),

 dict(q="Median household income by distance from the centre in two cities is recorded below. Using the accompanying figures, what does the comparison show?",
   table=dict(headers=["Distance from the centre (kilometres)", "City A median income (thousands)", "City B median income (thousands)"],
     rows=[["1", "22", "68"],
           ["5", "34", "44"],
           ["10", "58", "26"],
           ["20", "71", "11"]]),
   choices=[
   "Income rises outward in City A from 22 to 71 and falls outward in City B from 68 to 11, so the two cities have opposite income gradients",
   "Income rises outward in both cities",
   "Income falls outward in both cities",
   "Income is unrelated to distance in either city",
   "The two cities have identical income gradients"], ans=0,
   why="City A's income rises at every step from 22 to 71 while City B's falls at every step from 68 to 11, so the two gradients run in opposite directions. EK PSO-6.D.1 lists urban models drawn from Latin America alongside the concentric-zone model, and this reversal is why a single model cannot serve both cities."),

 dict(q="Employment by centre in one metropolitan area is recorded below. Using the accompanying figures, which model does the distribution best support?",
   table=dict(headers=["Employment centre", "Jobs"],
     rows=[["Traditional downtown", "118,000"],
           ["Outlying centre 1", "96,000"],
           ["Outlying centre 2", "74,000"],
           ["Outlying centre 3", "61,000"],
           ["All other locations", "210,000"]]),
   choices=[
   "The galactic city model, since the downtown holds only about 21 percent of the area's 559,000 jobs and three outlying centres are of comparable size",
   "The concentric zone model, since the downtown holds the most jobs of any single centre",
   "The sector model, since the centres could lie along corridors",
   "That the metropolitan area has only one employment centre",
   "That employment is evenly distributed across the metropolitan area"], ans=0,
   why="The five entries total 559,000 jobs and the downtown's 118,000 is about 21 percent of them, while three outlying centres between them hold 231,000. EK PSO-6.D.1 names the galactic city model among the models explaining internal city structure, and a downtown that is merely the largest of several comparable nodes is what it describes."),

 dict(q="What limitation should be stated when using an income-by-distance table to decide which model a city fits?", choices=[
   "A single line outward from the centre cannot show whether the pattern is a ring or a wedge, since a ring and a wedge look the same along one radius",
   "Median incomes cannot be measured by distance from a centre",
   "Distances and incomes can never appear in one record",
   "One gradient is sufficient to identify any model with certainty",
   "The framework forbids the use of income data in urban geography"], ans=0,
   why="EK PSO-6.D.1 names both the concentric-zone model and the sector model, and they differ in whether land use varies with direction as well as with distance. A single radius holds direction constant, so it cannot distinguish the two, which is precisely what the sector model was proposed to correct."),

 dict(q="A revision guide must say what this topic's essential knowledge establishes. Which statement is accurate?", choices=[
   "Several models each capture part of how land uses are arranged within a city, they encode the era and region they were drawn from, and bid-rent theory supplies the mechanism behind the patterns they describe",
   "One model correctly describes the internal structure of every city",
   "The models describe relationships between cities rather than within them",
   "The models have been superseded and no longer explain anything",
   "Bid-rent theory describes a shape made of rings"], ans=0,
   why="EK PSO-6.D.1 lists six models and theories as useful for explaining internal structures of cities, and the suggested skill is explaining their strengths, weaknesses and limitations in context. Bid-rent theory is listed alongside the shape models because it explains why land uses sort themselves at all."),
]
