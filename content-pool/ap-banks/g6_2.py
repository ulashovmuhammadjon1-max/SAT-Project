# AP HUMAN GEOGRAPHY 6.2 Cities Across the World -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding PSO-6, "The presence
# and growth of cities vary across geographical locations because of physical
# geography and resources." Learning objective PSO-6.A, "Explain the processes
# that initiate and drive urbanization and suburbanization."
#
# Essential knowledge -- the two statements assigned to this topic:
#   PSO-6.A.3  Megacities and metacities are distinct spatial outcomes of
#              urbanization increasingly located in countries of the periphery
#              and semiperiphery.
#   PSO-6.A.4  Processes of suburbanization, sprawl, and decentralization have
#              created new land-use forms -- including edge cities, exurbs, and
#              boomburbs -- and new challenges.
#
# THE TWO STATEMENTS LOOK AT OPPOSITE ENDS OF THE SAME PROCESS. PSO-6.A.3 is
# about urbanization producing enormous single agglomerations, and about WHERE
# those are increasingly found. PSO-6.A.4 is about urban population and activity
# spreading outward and about the settlement forms that spreading has invented.
# One statement concerns concentration and the other dispersal, and item 24 keys
# on the fact that both are happening at once.
#
# THE THRESHOLDS, since the CED names the two terms without defining either. The
# conventional figures used throughout are the standard ones for this course:
#   megacity   an urban agglomeration of at least 10 million people
#   metacity   an urban agglomeration of at least 20 million
# Item 2 and item 3 state them as conventional thresholds rather than as legal
# definitions, because they are conventions and no authority fixes them. Item 23
# tests the reasoning rather than the number: what makes a city cross a threshold
# is growth in the agglomeration, not a change in its administrative boundary.
#
# "INCREASINGLY LOCATED IN COUNTRIES OF THE PERIPHERY AND SEMIPERIPHERY" is the
# CED's own wording and it is a claim about a TREND, not about a fixed fact.
# Items 1, 6 and 25 key on the mechanism behind the trend -- population growth
# and rural-to-urban migration are fastest where the urban share was lowest, so
# the largest additions to city populations occur there. NO REAL CITY IS NAMED
# ANYWHERE IN THIS MODULE, including in the data items, because which
# agglomerations are largest changes and a ranking true when written can be false
# when read.
#
# THE FIVE FORMS IN PSO-6.A.4 and the definitions this module uses, none of
# which the CED supplies:
#   suburbanization  growth of residential settlement at a city's edge
#   sprawl           low-density, discontinuous, car-dependent outward expansion
#   decentralization the movement of people AND jobs, retail and services away
#                    from the central city
#   edge city        a concentration of offices, retail and entertainment outside
#                    the traditional downtown, characteristically at a major
#                    highway junction
#   exurb            prosperous low-density settlement beyond the continuous
#                    suburbs, still tied to the metropolitan area by commuting
#   boomburb         a rapidly grown suburban municipality of substantial size
#                    that is not its metropolitan area's largest city
# Items 8 to 15 walk them, and items 14 and 15 are the two distinctions students
# actually confuse: edge city against exurb, and boomburb against ordinary
# suburb.
#
# SYNONYM CARE. `geo_check` treats {"world system theory", "world-systems
# theory", "core-periphery model"} as one construct, so no choice list names that
# framework in two ways.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.2", "Cities Across the World", 6)

QUESTIONS = [
 dict(q="What does the framework say about where megacities and metacities are increasingly located?", choices=[
   "In countries of the periphery and semiperiphery",
   "In core countries almost exclusively",
   "Evenly distributed among all countries",
   "In countries with the smallest total populations",
   "In countries that are not urbanizing at all"], ans=0,
   why="EK PSO-6.A.3 states that megacities and metacities are distinct spatial outcomes of urbanization increasingly located in countries of the periphery and semiperiphery. The word 'increasingly' makes it a claim about a trend rather than about a fixed distribution."),

 dict(q="What is a megacity, by the convention this course uses?", choices=[
   "An urban agglomeration of at least about ten million people",
   "Any city that is the largest in its country",
   "Any city with more than one million people",
   "A city that contains a national capital",
   "A city whose built-up area exceeds one thousand square kilometres"], ans=0,
   why="EK PSO-6.A.3 names megacities as a distinct spatial outcome of urbanization without fixing a number, and about ten million is the conventional threshold. The measure is the agglomeration -- the continuous built-up area and its population -- rather than any administrative boundary."),

 dict(q="What is a metacity, by the convention this course uses?", choices=[
   "An urban agglomeration of at least about twenty million people, so every metacity is also a megacity",
   "A city smaller than a megacity",
   "A city with exactly ten million people",
   "A city that has stopped growing",
   "Any capital city of a peripheral country"], ans=0,
   why="EK PSO-6.A.3 names megacities and metacities together as distinct spatial outcomes of urbanization, and the metacity threshold is conventionally about twice the megacity one. The categories are nested, so the second is a subset of the first rather than a separate kind of place."),

 dict(q="Why does the framework describe megacities and metacities as DISTINCT SPATIAL OUTCOMES of urbanization?", choices=[
   "Concentrating tens of millions of people into one continuous built-up area is a different kind of result from many cities each growing modestly",
   "Because they are the only outcomes urbanization can have",
   "Because they occupy no space of their own",
   "Because they are found only in one country",
   "Because they are not products of urbanization at all"], ans=0,
   why="EK PSO-6.A.3 calls them distinct spatial outcomes of urbanization. The same national rise in urban share can be delivered by dozens of medium cities or by one enormous agglomeration, and the two produce completely different geographies."),

 dict(q="What do the terms periphery and semiperiphery refer to in the framework's statement?", choices=[
   "Positions in the world economy, describing countries whose role in global production and trade is less dominant than that of the core",
   "The outer suburbs of a large city",
   "Regions with the lowest population densities",
   "Countries with the largest land areas",
   "The rural districts immediately surrounding a metropolitan area"], ans=0,
   why="EK PSO-6.A.3 places megacities and metacities increasingly in countries of the periphery and semiperiphery, which are categories from the world-systems framework named in EK SPS-7.E.1. They classify countries by their economic position rather than by any physical characteristic."),

 dict(q="Why are the world's very largest urban agglomerations increasingly found outside the core?", choices=[
   "Population growth and rural-to-urban migration are both fastest in the regions where the urban share was lowest, so the largest additions to city populations occur there",
   "Core countries have prohibited cities from growing",
   "Peripheral countries have the largest land areas available",
   "Core-country cities have all lost their entire populations",
   "The pattern is random and has no explanation"], ans=0,
   why="EK PSO-6.A.3 says megacities and metacities are increasingly located in countries of the periphery and semiperiphery, and EK PSO-6.A.2 names population growth and migration among the influences on urbanization. Core countries urbanized earlier, so the great transfers of population from countryside to city are happening elsewhere now."),

 dict(q="What is the most important consequence of a country's urban population being concentrated in one enormous agglomeration rather than spread across many cities?", choices=[
   "Investment, services and opportunity concentrate in one place, and the pressure on that one place's housing, transport and services is correspondingly extreme",
   "The country's total urban population is smaller",
   "The country ceases to have any rural areas",
   "Urban services become easier to provide than in a dispersed system",
   "There is no consequence, since the same number of people is urban either way"], ans=0,
   why="EK PSO-6.A.3 calls megacities and metacities distinct SPATIAL outcomes, which is a claim about arrangement rather than about totals. Where the arrangement concentrates, everything that follows population concentrates with it, and so does everything that strains under it."),

 dict(q="What is suburbanization?", choices=[
   "The growth of residential settlement at the edge of a city, drawing population outward from its centre",
   "The movement of rural people into a city centre",
   "The demolition of a city's outer districts",
   "The growth of a city's tallest buildings",
   "The movement of people from one country to another"], ans=0,
   why="EK PSO-6.A.4 names suburbanization among the processes that have created new land-use forms. It is a redistribution within an urban area rather than a change in how many people are urban, which is what distinguishes it from urbanization."),

 dict(q="What is urban sprawl?", choices=[
   "Low-density, often discontinuous outward expansion that consumes a great deal of land per resident and depends on the car",
   "High-density development concentrated at a city's centre",
   "The rebuilding of an existing urban district at higher density",
   "The abandonment of a city's outer areas",
   "The construction of a city's public transport network"], ans=0,
   why="EK PSO-6.A.4 names sprawl among the processes creating new land-use forms and new challenges. The defining features are the density and the discontinuity, and the car dependence follows from them, since distances become too great to walk and densities too low to support frequent transit."),

 dict(q="What is decentralization in an urban context?", choices=[
   "The movement of jobs, retail and services away from the central city, not only of residents",
   "The transfer of political power from a national government to regions",
   "The concentration of all activity in a single downtown",
   "The reduction of a city's total population",
   "The construction of a new central business district"], ans=0,
   why="EK PSO-6.A.4 names decentralization alongside suburbanization and sprawl among the processes creating new land-use forms. Suburbanization moves residents outward; decentralization is the broader movement that takes the workplaces and the shops with them."),

 dict(q="What is an edge city?", choices=[
   "A concentration of offices, retail and entertainment outside the traditional downtown, typically grown up at a major highway junction",
   "The outermost ring of low-density housing in a metropolitan area",
   "A small town on a national border",
   "The historic centre of an old city",
   "A city built entirely by a national government as a new capital"], ans=0,
   why="EK PSO-6.A.4 names edge cities among the new land-use forms created by suburbanization, sprawl and decentralization. What makes it a form rather than a suburb is that work and commerce, not only housing, have relocated there."),

 dict(q="What is an exurb?", choices=[
   "Prosperous, low-density settlement beyond the continuous built-up suburbs, still tied to the metropolitan area by commuting",
   "A dense district at the centre of a city",
   "An industrial zone inside a city's boundary",
   "A rural district with no connection to any city",
   "A concentration of offices at a highway junction"], ans=0,
   why="EK PSO-6.A.4 names exurbs among the new land-use forms. The commuting tie is what keeps an exurb part of the metropolitan area rather than a separate rural settlement, and the low density and distance are what separate it from the suburbs."),

 dict(q="What is a boomburb?", choices=[
   "A rapidly grown suburban municipality of substantial size that is nonetheless not the largest city of its metropolitan area",
   "A city that has lost population rapidly",
   "The central business district of a metropolitan area",
   "A temporary settlement built for a single industry",
   "A district of a city redeveloped at very high density"], ans=0,
   why="EK PSO-6.A.4 names boomburbs among the new land-use forms created by suburbanization and decentralization. The category exists because such places have the population of a city and the form and history of a suburb, which no earlier term captured."),

 dict(q="What distinguishes an edge city from an exurb?", choices=[
   "An edge city is a concentration of employment and commerce, while an exurb is dispersed low-density settlement whose residents commute elsewhere",
   "An edge city is further from the centre than an exurb",
   "An exurb contains more office space than an edge city",
   "They are two names for the same land-use form",
   "An edge city is rural and an exurb is urban"], ans=0,
   why="EK PSO-6.A.4 names both among the new land-use forms, and they differ in what has moved outward. In one case it is the jobs and the shops; in the other it is only the houses, so an exurb generates commuting while an edge city receives it."),

 dict(q="What distinguishes a boomburb from an ordinary suburb?", choices=[
   "Its size -- it has grown to the population of a substantial city while remaining a suburb in form and in its position within the metropolitan area",
   "It lies outside the metropolitan area entirely",
   "It contains no housing",
   "It was founded before the central city",
   "It has a lower population than a typical suburb"], ans=0,
   why="EK PSO-6.A.4 names boomburbs among the new land-use forms created by suburbanization, sprawl and decentralization. Scale is the whole of the distinction: the form is suburban and the population is urban, which is the combination that made a new word necessary."),

 dict(q="Why is sprawl characteristically dependent on the car?", choices=[
   "Low density spreads destinations too far apart to walk between and leaves too few people per route to support frequent public transport",
   "Because cars are cheaper in low-density areas",
   "Because public transport is prohibited in suburbs",
   "Because sprawl occurs only where there are no roads",
   "Because low density makes walking distances shorter"], ans=0,
   why="EK PSO-6.A.4 names sprawl among the processes creating new land-use forms and new challenges. Transit needs riders per kilometre of route and walking needs destinations within a few hundred metres, and low density undermines both conditions at once."),

 dict(q="Which of these is one of the NEW CHALLENGES the framework attributes to suburbanization, sprawl and decentralization?", choices=[
   "The cost of extending roads, water, sewers and schools across a much larger area for the same number of people",
   "A fall in the total population of metropolitan areas",
   "The disappearance of all central business districts",
   "An end to commuting of any kind",
   "The complete conversion of suburbs back into farmland"], ans=0,
   why="EK PSO-6.A.4 says these processes have created new land-use forms AND new challenges. Infrastructure is priced by length rather than by population, so spreading the same population over more ground raises the cost of serving each household."),

 dict(q="A metropolitan area's jobs have decentralized so far that many residents of the central city now commute outward to work. What does this illustrate?", choices=[
   "That decentralization moves workplaces as well as residences, which can reverse the direction of the daily journey",
   "That the central city has been abandoned",
   "That suburbanization has stopped",
   "That the metropolitan area has ceased to grow",
   "That commuting has been eliminated"], ans=0,
   why="EK PSO-6.A.4 names decentralization among the processes creating new land-use forms. Once employment has moved outward the assumption that commuting runs inward stops holding, which is one of the practical consequences of the edge city as a form."),

 dict(q="At which scales do the framework's two statements in this topic operate?", choices=[
   "The global scale, where the largest agglomerations shift toward the periphery and semiperiphery, and the metropolitan scale, where activity spreads outward from a centre",
   "Both operate only at the global scale",
   "Both operate only at the neighbourhood scale",
   "Neither statement involves scale",
   "Both operate only at the national scale"], ans=0,
   why="EK PSO-6.A.3 makes a claim about the distribution of the largest cities among countries, which is a global comparison, while EK PSO-6.A.4 describes rearrangement within a single urban area. The two statements sit in one topic because both are outcomes of urbanization observed at different resolutions."),

 dict(q="Why do edge cities characteristically form at major highway junctions?", choices=[
   "A junction is reachable from a large surrounding population, which is the accessibility offices and retail require without the cost of a downtown site",
   "Because highways provide the water supply such centres need",
   "Because junctions are the only land available for building",
   "Because governments require offices to be built at junctions",
   "Because junctions are the quietest locations in a metropolitan area"], ans=0,
   why="EK PSO-6.A.4 names edge cities among the new land-use forms created by decentralization. Accessibility is what a central business district traditionally supplied, and in a car-based metropolitan area a motorway junction supplies a version of it at a far lower land cost."),

 dict(q="Why does the framework call edge cities, exurbs and boomburbs NEW land-use forms?", choices=[
   "They are arrangements of activity that earlier urban systems did not produce, so the existing vocabulary of city, suburb and countryside did not describe them",
   "Because they are the newest buildings in any city",
   "Because they were all created in the same year",
   "Because they replace cities entirely",
   "Because they are temporary and will disappear"], ans=0,
   why="EK PSO-6.A.4 describes these as new land-use forms created by suburbanization, sprawl and decentralization. A place with a downtown's employment and no downtown, or a suburb with a city's population, does not fit categories built for a single-centred city."),

 dict(q="Which pairing of a description with the correct form is CORRECT?", choices=[
   "A cluster of office towers and a shopping mall at a motorway interchange twenty kilometres from downtown, matched to an edge city",
   "A dense historic district at the heart of a metropolitan area, matched to an exurb",
   "Scattered large houses on one-hectare plots forty kilometres out, whose residents commute in, matched to a boomburb",
   "A suburban municipality that grew from 8,000 to 300,000 residents in thirty years, matched to an exurb",
   "A low-density residential district immediately adjoining the central city, matched to an edge city"], ans=0,
   why="EK PSO-6.A.4 names edge cities, exurbs and boomburbs as three distinct new land-use forms. Only one pairing here matches a description to the form whose definition it satisfies; each of the others attaches a description to one of the statement's other two categories."),

 dict(q="An agglomeration passes ten million residents for the first time. What has actually happened, on the framework's terms?", choices=[
   "The continuous built-up area and the population living in it have grown past the conventional threshold, which is a fact about the agglomeration rather than about any city boundary",
   "The city's administrative boundary has been redrawn",
   "The country has been reclassified as peripheral",
   "The city has become a metacity",
   "The city has stopped suburbanizing"], ans=0,
   why="EK PSO-6.A.3 names megacities as distinct spatial outcomes of urbanization, and the unit being measured is the agglomeration. A boundary change can alter a municipality's recorded population without a single additional person living in the urban area, which is why the agglomeration is the meaningful unit."),

 dict(q="How can a country be experiencing both the growth of a metacity and rapid suburbanization at the same time?", choices=[
   "The two statements describe concentration and dispersal at different scales, so an agglomeration can grow enormously while its own population spreads outward within it",
   "It cannot; the two processes are mutually exclusive",
   "Only if the country has two separate urban systems",
   "Only if the country's total population is falling",
   "Only if the government has ordered both processes"], ans=0,
   why="EK PSO-6.A.3 concerns the size of whole agglomerations while EK PSO-6.A.4 concerns how activity is arranged within an urban area. A metacity that keeps adding millions is also a metacity whose new residents are housed further and further from its centre."),

 dict(q="What is the most defensible reading of the framework's word 'increasingly' in its statement about megacities?", choices=[
   "That the share of the world's largest agglomerations found in the periphery and semiperiphery has been rising, not that none are found in the core",
   "That every megacity is in the periphery",
   "That no megacity has ever existed in a core country",
   "That megacities will soon disappear from the periphery",
   "That the distribution of megacities has never changed"], ans=0,
   why="EK PSO-6.A.3 says megacities and metacities are INCREASINGLY located in countries of the periphery and semiperiphery. A statement about a changing share is weaker than a statement about every case, and reading it as the stronger claim is what makes a student vulnerable to a single counterexample."),

 dict(q="Eight of the world's largest urban agglomerations are recorded below. Using the accompanying record, which conclusion is supported?",
   table=dict(headers=["Agglomeration", "Population (millions)", "World-economy position of its country"],
     rows=[["Agglomeration 1", "37", "Core"],
           ["Agglomeration 2", "32", "Periphery"],
           ["Agglomeration 3", "29", "Semiperiphery"],
           ["Agglomeration 4", "26", "Periphery"],
           ["Agglomeration 5", "23", "Semiperiphery"],
           ["Agglomeration 6", "22", "Periphery"],
           ["Agglomeration 7", "21", "Core"],
           ["Agglomeration 8", "20", "Semiperiphery"]]),
   choices=[
   "Six of the eight are in periphery or semiperiphery countries, and all eight exceed the twenty-million metacity threshold",
   "All eight are in core countries",
   "None of the eight reaches the twenty-million threshold",
   "The two largest are both in peripheral countries",
   "Exactly half are in core countries"], ans=0,
   why="Counting the record gives two agglomerations in core countries and six across the periphery and semiperiphery, and the smallest of the eight is twenty million. EK PSO-6.A.3 says megacities and metacities are increasingly located in countries of the periphery and semiperiphery, and the count is what such a claim looks like in a table."),

 dict(q="The population of one metropolitan area by zone is recorded below. Using the accompanying figures, what has occurred?",
   table=dict(headers=["Zone", "Population in 1970 (millions)", "Population in 2020 (millions)"],
     rows=[["Central city", "2.9", "2.6"],
           ["Inner suburbs", "1.4", "2.2"],
           ["Outer suburbs", "0.5", "2.4"],
           ["Exurban fringe", "0.1", "0.9"]]),
   choices=[
   "The metropolitan total rose from 4.9 to 8.1 million while the central city lost population, so all of the growth and more occurred beyond the centre",
   "The central city grew faster than any other zone",
   "The metropolitan area lost population overall",
   "The exurban fringe was the only zone to grow",
   "Every zone grew by the same amount"], ans=0,
   why="The four zones sum to 4.9 million in 1970 and 8.1 million in 2020, and the central city is the only zone to fall, from 2.9 to 2.6 million. EK PSO-6.A.4 names suburbanization, sprawl and decentralization as processes creating new land-use forms, and this is that redistribution recorded directly."),

 dict(q="Density and commuting in four zones of one metropolitan area are recorded below. Using the accompanying figures, which relationship is shown?",
   table=dict(headers=["Zone", "Population density (persons per square kilometre)", "Share of commuters travelling by car (%)"],
     rows=[["Central city", "9,200", "31"],
           ["Inner suburbs", "3,100", "68"],
           ["Outer suburbs", "1,050", "88"],
           ["Exurban fringe", "210", "95"]]),
   choices=[
   "Car use rises from 31 to 95 percent as density falls from 9,200 to 210 persons per square kilometre, which is the car dependence the framework attributes to sprawl",
   "Car use and density rise together across the four zones",
   "Density is highest on the exurban fringe",
   "Car use is highest in the central city",
   "No relationship can be read, since the two use different units"], ans=0,
   why="Density falls at every step from 9,200 to 210 persons per square kilometre while the car share rises at every step from 31 to 95 percent, so the two move in opposite directions throughout. EK PSO-6.A.4 names sprawl among the processes creating new land-use forms and new challenges, and car dependence is the mechanism that links the density to the challenge."),

 dict(q="What limitation should be stated when using a table of the world's largest agglomerations to test the framework's claim?", choices=[
   "A snapshot of the largest cities at one moment cannot by itself show a trend, which is what the word 'increasingly' asserts",
   "Populations of agglomerations cannot be measured at all",
   "Millions and categories can never appear in the same record",
   "A count at one date is sufficient to establish any claim about change",
   "The framework forbids the use of city population data"], ans=0,
   why="EK PSO-6.A.3 says megacities and metacities are INCREASINGLY located in countries of the periphery and semiperiphery, which is a claim about change over time. One column of populations describes a moment, and demonstrating a trend requires the same measurement at two or more dates."),

 dict(q="Which sentence captures what this topic's two essential knowledge statements assert between them?", choices=[
   "Urbanization is producing enormous agglomerations, increasingly outside the core, while within metropolitan areas people and activity are spreading outward into new forms of settlement",
   "Urbanization is producing enormous agglomerations only in core countries",
   "Metropolitan areas are contracting toward their centres everywhere",
   "Suburbanization has ended and cities are becoming denser worldwide",
   "The two statements describe the same process under two names"], ans=0,
   why="EK PSO-6.A.3 supplies the concentration and its shifting location, and EK PSO-6.A.4 supplies the outward dispersal and the forms it has created. The two point in opposite directions and both are true at once, which is why the topic contains them together."),
]
