# AP HUMAN GEOGRAPHY 6.11 Challenges of Urban Sustainability -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding SPS-6, "Urban areas
# face unique economic, political, cultural, and environmental challenges."
# Learning objective SPS-6.B, "Describe the effectiveness of different attempts
# to address urban sustainability challenges."
#
# Essential knowledge -- two statements, one of challenges and one of responses:
#   SPS-6.B.1  Challenges to urban sustainability include suburban sprawl,
#              sanitation, climate change, air and water quality, the large
#              ecological footprint of cities, and energy use.
#   SPS-6.B.2  Responses to urban sustainability challenges can include regional
#              planning efforts, remediation and redevelopment of brownfields,
#              establishment of urban growth boundaries, and farmland protection
#              policies.
#
# THE LEARNING OBJECTIVE'S WORD IS EFFECTIVENESS, and that is what separates this
# topic from a pair of vocabulary lists. SPS-6.B asks students to DESCRIBE THE
# EFFECTIVENESS of different attempts, so items 14 to 18 and 22 to 24 evaluate
# each response rather than merely naming it -- what it actually achieves, what
# it costs, what it moves elsewhere, and what would have to be measured to know.
# Item 18 asks for that directly.
#
# EVERY RESPONSE ON SPS-6.B.2'S LIST HAS A COST OR A DISPLACEMENT, and saying so
# is not scepticism -- it is what "describe the effectiveness" requires:
#   regional planning        acts at the scale the problems have, and needs the
#                            agreement of the divided governments of EK SPS-6.A.5
#   brownfield redevelopment builds on land already served, and costs more per
#                            hectare because contaminated ground must be cleaned
#   urban growth boundary    stops outward expansion, and restricts the supply of
#                            developable land, which EK IMP-6.D.1 records as
#                            raising housing costs
#   farmland protection      keeps land in production, and can push growth past
#                            the protected land rather than preventing it
# Items 15, 16, 17 and 22 key on these, each stating the achievement and the cost
# together.
#
# THE ECOLOGICAL FOOTPRINT is the item most often misread and items 8, 20 and 28
# handle it. A city's footprint is the land and water area required to supply
# what it consumes and absorb what it emits, so it is many times the city's own
# area and lies mostly outside it. That is the sense in which the footprint is
# "large". It does NOT follow that cities are inefficient: per PERSON, dense urban
# living is generally lighter than dispersed living on every measure in item 26's
# table. Item 20 keys on that distinction, because a student who reads SPS-6.B.1's
# "large ecological footprint of cities" as "cities are the problem" has drawn a
# per-city conclusion from what is really a per-person question.
#
# A BROWNFIELD, since the CED names one without defining it: land previously
# built on, often industrially, whose reuse requires contamination to be dealt
# with first. Remediation is the cleaning; redevelopment is what follows.
#
# NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.11", "Challenges of Urban Sustainability", 6)

QUESTIONS = [
 dict(q="Which set of challenges to urban sustainability does the framework name?", choices=[
   "Suburban sprawl, sanitation, climate change, air and water quality, the large ecological footprint of cities, and energy use",
   "Regional planning, brownfield redevelopment, growth boundaries, and farmland protection",
   "Redlining, blockbusting, and affordability",
   "Site, situation, and cycles of development",
   "Rank-size distributions, primacy, gravity, and central place theory"], ans=0,
   why="EK SPS-6.B.1 names exactly this set of challenges. The second option is EK SPS-6.B.2's list of RESPONSES to those challenges, which is the distinction this topic's two statements draw and the one an item can most easily blur."),

 dict(q="Which set of responses to urban sustainability challenges does the framework name?", choices=[
   "Regional planning efforts, remediation and redevelopment of brownfields, establishment of urban growth boundaries, and farmland protection policies",
   "Suburban sprawl, sanitation, and energy use",
   "Inclusionary zoning and local food movements",
   "Redlining, blockbusting, and urban renewal",
   "Mixed land use, walkability, and New Urbanism"], ans=0,
   why="EK SPS-6.B.2 names exactly these four responses. Inclusionary zoning and local food movements are EK SPS-6.A.3's responses to economic and social challenges, and the design initiatives belong to EK IMP-6.C.1, so each rejected option answers a different statement."),

 dict(q="Why is suburban sprawl a challenge to urban SUSTAINABILITY specifically?", choices=[
   "It consumes land, lengthens every journey and requires more infrastructure per household, so it raises the resources each resident needs",
   "It reduces the total population of a metropolitan area",
   "It concentrates people too densely for services to reach them",
   "It has no measurable resource consequences",
   "It occurs only in cities that are shrinking"], ans=0,
   why="EK SPS-6.B.1 names suburban sprawl first among the challenges to urban sustainability. Sustainability is a question about resources per person over time, and low-density outward growth raises the land, energy and infrastructure each household requires."),

 dict(q="Why does the framework name SANITATION among the challenges to urban sustainability?", choices=[
   "Concentrating people concentrates their waste, and a city that cannot collect and treat it contaminates its own water and the environment downstream",
   "Because sanitation systems have no environmental effect",
   "Because sanitation is a rural rather than an urban problem",
   "Because sanitation concerns only the appearance of streets",
   "Because sanitation affects the economy but not the environment"], ans=0,
   why="EK SPS-6.B.1 names sanitation among the challenges to urban sustainability. Density is what makes the problem urban: the same number of people spread thinly can be served by dispersed arrangements that fail entirely once they are concentrated."),

 dict(q="In what two ways does climate change appear as an urban sustainability challenge?", choices=[
   "Cities are a large source of the emissions that drive it and are also exposed to its effects, including heat, flooding and storms",
   "Cities contribute to it but are not affected by it",
   "Cities are affected by it but contribute nothing to it",
   "Cities are unaffected by climate in any respect",
   "Climate change affects only agricultural regions"], ans=0,
   why="EK SPS-6.B.1 names climate change among the challenges to urban sustainability. Cities concentrate the energy use and the emissions and they also concentrate the people and property exposed to heat, flood and storm, so they sit on both sides of the problem."),

 dict(q="Why is urban air quality a sustainability challenge?", choices=[
   "Traffic, heating, power generation and industry are concentrated in a small area, so pollutants accumulate where the most people are breathing them",
   "Because cities have no vegetation of any kind",
   "Because air quality cannot be measured in cities",
   "Because urban air is unaffected by human activity",
   "Because air quality concerns only the countryside"], ans=0,
   why="EK SPS-6.B.1 names air and water quality among the challenges to urban sustainability. Concentration is the mechanism throughout this list: the same emissions spread over a wide area are a smaller problem than the same emissions released where millions of people live."),

 dict(q="Why is urban water quality a sustainability challenge?", choices=[
   "Runoff from sealed surfaces, waste discharges and industrial contamination all reach the same watercourses that supply the city and the places downstream",
   "Because cities do not use water",
   "Because water quality is fixed by geology and cannot change",
   "Because urban water is drawn only from rainfall",
   "Because only rural areas discharge into rivers"], ans=0,
   why="EK SPS-6.B.1 names air and water quality together among the challenges. A city collects rain from a sealed surface and returns it quickly and dirty, so both the volume and the content of what leaves are altered by the city's presence."),

 dict(q="What is a city's ecological footprint?", choices=[
   "The land and water area required to supply what its population consumes and absorb what it emits, most of which lies far outside the city itself",
   "The physical area the city's buildings cover",
   "The area of parkland within the city boundary",
   "The distance from the city centre to its edge",
   "The number of people living in the city"], ans=0,
   why="EK SPS-6.B.1 names the large ecological footprint of cities among the challenges to urban sustainability. The measure is deliberately not the built area: it is the productive area a population's consumption requires, which is why a city's footprint is many times its own extent."),

 dict(q="Why does the framework name ENERGY USE separately from climate change and air quality?", choices=[
   "Energy use is the underlying activity, while emissions and air quality are two of its consequences, so it can be addressed directly rather than only through its effects",
   "Because energy use has no relationship to emissions",
   "Because energy is used only outside cities",
   "Because the framework lists the same challenge three times",
   "Because energy use affects only the cost of living"], ans=0,
   why="EK SPS-6.B.1 lists energy use alongside climate change and air and water quality. Listing the driver as well as its consequences is what makes reduction a possible response, since a policy can act on how much energy is used rather than only on what the use produces."),

 dict(q="What do REGIONAL PLANNING EFFORTS attempt to do about urban sustainability?", choices=[
   "Coordinate decisions across a whole metropolitan area, so that land use, transport and growth are settled at the scale the problems actually occupy",
   "Replace local governments with a national authority",
   "Plan each municipality entirely independently of its neighbours",
   "Restrict planning decisions to a single neighbourhood",
   "Remove all restrictions on where development may occur"], ans=0,
   why="EK SPS-6.B.2 names regional planning efforts among the responses to urban sustainability challenges. Sprawl, air quality, watersheds and transport are all metropolitan in scale, so a response confined to one municipality is smaller than the problem it addresses."),

 dict(q="What is a brownfield, and what does remediation of one involve?", choices=[
   "Land previously built on, often industrially, whose reuse first requires contamination in the soil or groundwater to be removed or contained",
   "Undeveloped farmland at the edge of a city",
   "Parkland that has been allowed to become overgrown",
   "Land that has never been built on or farmed",
   "A district of new housing built to environmental standards"], ans=0,
   why="EK SPS-6.B.2 names remediation and redevelopment of brownfields among the responses to urban sustainability challenges. The two words describe two steps: the contamination must be dealt with before the site can carry a new use, which is the whole reason such land sits idle."),

 dict(q="What is an urban growth boundary?", choices=[
   "A line beyond which urban development is not permitted, drawn to contain a city's outward expansion",
   "The administrative border of a city",
   "The edge of the continuously built-up area at a given date",
   "A ring road marking the limit of the city centre",
   "A line dividing residential from industrial zones"], ans=0,
   why="EK SPS-6.B.2 names the establishment of urban growth boundaries among the responses to urban sustainability challenges. It is a limit on where building may occur rather than a description of where building currently is, which is what distinguishes it from a city's boundary."),

 dict(q="What do farmland protection policies aim to achieve?", choices=[
   "Keeping agricultural land in production by restricting its conversion to urban uses, since building on soil is effectively permanent",
   "Increasing the price farmers receive for their crops",
   "Converting urban land back into farmland",
   "Requiring cities to grow all of their own food",
   "Preventing any agricultural activity near cities"], ans=0,
   why="EK SPS-6.B.2 names farmland protection policies among the responses to urban sustainability challenges, and EK IMP-5.B.3 names land use lost to suburbanization among the challenges of feeding a global population. The two statements meet at the metropolitan edge, where the best farmland and the cheapest building land are the same land."),

 dict(q="How effective is an urban growth boundary at what it is meant to do, and what does it cost?", choices=[
   "It contains outward expansion directly and reliably, and by limiting the supply of developable land it puts upward pressure on housing prices inside the line",
   "It contains expansion and has no effect on any other variable",
   "It has no effect on outward expansion",
   "It lowers housing prices inside the line",
   "It affects prices but not the physical extent of the city"], ans=0,
   why="EK SPS-6.B.2 names growth boundaries among the responses and learning objective SPS-6.B asks for their EFFECTIVENESS. The instrument works on the thing it targets, and EK IMP-6.D.1 records increased housing costs among the criticisms of such initiatives, so describing its effectiveness means stating both."),

 dict(q="How effective is brownfield redevelopment, and what is its principal obstacle?", choices=[
   "It supplies building land inside the already-served area and spares farmland, but cleaning contaminated ground makes each hectare more expensive than an untouched site",
   "It is cheaper per hectare than building on open land",
   "It requires new roads and pipes to be built from scratch",
   "It consumes more farmland than greenfield development",
   "It has no effect on where a city grows"], ans=0,
   why="EK SPS-6.B.2 names remediation and redevelopment of brownfields among the responses, and learning objective SPS-6.B asks how effective such attempts are. The land is in the right place and the ground has to be paid for twice, which is why such sites remain idle without a policy to bridge the gap."),

 dict(q="What does regional planning require in order to be effective, and why is that difficult?", choices=[
   "The agreement of many separate authorities, which is hard because a metropolitan area's government is divided among state, county, city and neighbourhood levels",
   "A single national law imposing identical rules everywhere",
   "The abolition of all local government",
   "That each municipality plan without consulting others",
   "Nothing beyond a technical study of the region"], ans=0,
   why="EK SPS-6.B.2 names regional planning efforts among the responses and EK SPS-6.A.5 names functional and geographic fragmentation of governments as a challenge in addressing urban issues. The response operates at the metropolitan scale and the authority to deliver it does not."),

 dict(q="What limitation should be recognized in farmland protection policies?", choices=[
   "Protecting particular land does not remove the demand for building land, so growth can move past the protected area rather than stopping",
   "Protected farmland cannot be farmed",
   "Farmland protection increases the rate of urban expansion",
   "Farmland protection applies only to land already built on",
   "Farmland protection has no effect on where growth occurs"], ans=0,
   why="EK SPS-6.B.2 names farmland protection policies among the responses and learning objective SPS-6.B asks how effective attempts are. A restriction on one parcel redirects demand rather than extinguishing it, which is why such policies work best alongside a boundary or a regional plan rather than alone."),

 dict(q="Why does the framework's learning objective ask about EFFECTIVENESS rather than simply about what the responses are?", choices=[
   "Naming a policy says nothing about whether it works, and each response achieves some things, costs something and displaces something else",
   "Because none of the responses has any effect",
   "Because effectiveness is the same for every response",
   "Because the responses are required by law everywhere",
   "Because the framework has already established that all four succeed"], ans=0,
   why="Learning objective SPS-6.B asks students to DESCRIBE THE EFFECTIVENESS of different attempts to address urban sustainability challenges. A list of responses is the input to that question rather than an answer to it, which is what makes this topic an evaluation rather than a vocabulary exercise."),

 dict(q="A city occupies 340 square kilometres and its ecological footprint is estimated at 47,000 square kilometres. What does that comparison show?", choices=[
   "The city depends on an area more than a hundred times its own size, almost all of it beyond its boundary",
   "The city's built-up area has been measured incorrectly",
   "The city's footprint lies entirely within its boundary",
   "The city consumes nothing that is produced elsewhere",
   "The two figures measure the same thing in different units"], ans=0,
   why="EK SPS-6.B.1 names the large ecological footprint of cities among the challenges to urban sustainability. The footprint measures the productive area a population's consumption requires, and the gap between that and the city's own extent is precisely what makes a city a place that lives on other places."),

 dict(q="Does a large total ecological footprint mean that cities are an inefficient way for people to live?", choices=[
   "Not by itself, since the total is large because many people live there while the footprint PER PERSON is generally smaller in dense cities than in dispersed settlement",
   "Yes, since a large total footprint proves inefficiency",
   "Yes, because cities produce nothing themselves",
   "No, because cities have no ecological footprint at all",
   "The question cannot be investigated with any evidence"], ans=0,
   why="EK SPS-6.B.1 names the large ecological footprint OF CITIES, which is a statement about a total. Shorter journeys, shared walls and shared infrastructure make dense living lighter per person, so the per-capita and per-city readings of the same measure point in opposite directions."),

 dict(q="Which response from the framework's list most directly addresses the challenge of suburban sprawl?", choices=[
   "The establishment of an urban growth boundary, which limits where outward development may occur",
   "Sanitation improvements, which treat waste",
   "Air quality regulation, which limits emissions",
   "Energy efficiency standards, which reduce consumption",
   "None of the responses addresses sprawl"], ans=0,
   why="EK SPS-6.B.1 names suburban sprawl among the challenges and EK SPS-6.B.2 names growth boundaries among the responses. Sprawl is defined by outward extent, so the instrument that acts on outward extent is the one aimed at it."),

 dict(q="Two of the framework's responses can work against each other. Which pairing shows a real tension?", choices=[
   "A growth boundary contains sprawl but raises land prices inside, which makes the expensive remediation of brownfield sites more viable and housing less affordable at the same time",
   "Regional planning and farmland protection are mutually exclusive",
   "Brownfield redevelopment prevents any regional planning",
   "Farmland protection makes growth boundaries impossible",
   "No two of the responses interact in any way"], ans=0,
   why="Learning objective SPS-6.B asks for the effectiveness of different attempts, and effectiveness has to be judged across a package rather than one instrument at a time. A higher land price inside a boundary is simultaneously the criticism recorded in EK IMP-6.D.1 and the thing that makes a contaminated site worth cleaning."),

 dict(q="Which indicator would best test whether a city's sustainability policies are working?", choices=[
   "Resource use and emissions per resident over time, since a city can grow while each resident's demands fall",
   "The total population of the city",
   "The number of policies the city has adopted",
   "The area of the city's administrative boundary",
   "The total energy the city uses, regardless of how many people live there"], ans=0,
   why="Learning objective SPS-6.B asks students to describe the EFFECTIVENESS of attempts to address urban sustainability challenges. A total rises with population whatever the policy achieves, so a per-resident measure is what separates a policy effect from simple growth."),

 dict(q="Why is the effectiveness of an urban sustainability policy difficult to judge in its first few years?", choices=[
   "The policies act on land use and infrastructure, which change slowly, so most of the effect appears long after the policy is adopted",
   "Because such policies are never actually implemented",
   "Because their effects appear immediately and then vanish",
   "Because effectiveness cannot be measured at any point",
   "Because policies are changed every year in every city"], ans=0,
   why="EK SPS-6.B.2's responses act on where building may occur and on what is built there, and EK IMP-6.A.1 makes those decisions long-lived. A boundary changes the next fifty years of building rather than the existing stock, so an early evaluation measures mostly the period before the policy took hold."),

 dict(q="Which pairing of a challenge with the response most directly aimed at it is CORRECT?", choices=[
   "Loss of agricultural land at the metropolitan edge, matched to farmland protection policies",
   "Loss of agricultural land at the metropolitan edge, matched to brownfield remediation",
   "Contaminated former industrial land, matched to farmland protection policies",
   "Decisions taken separately by many municipalities, matched to an urban growth boundary",
   "Outward expansion onto new land, matched to regional planning alone"], ans=0,
   why="EK SPS-6.B.1 names the challenges and EK SPS-6.B.2 the responses, and each response is aimed at a particular problem. Only one pairing here matches a challenge to the instrument designed for it; each of the others attaches a challenge to a different response on the same list."),

 dict(q="Four cities are compared below. Using the accompanying figures, what relationship do the columns show?",
   table=dict(headers=["City", "Population density (persons per square kilometre)", "Ecological footprint per person (global hectares)", "Transport energy per person (gigajoules per year)"],
     rows=[["City 1", "900", "6.8", "82"],
           ["City 2", "2,600", "5.1", "47"],
           ["City 3", "6,400", "3.9", "24"],
           ["City 4", "14,000", "3.2", "11"]]),
   choices=[
   "As density rises from 900 to 14,000, footprint per person falls from 6.8 to 3.2 and transport energy per person falls from 82 to 11, so denser living is lighter per resident on both measures",
   "Footprint per person rises as density rises",
   "Transport energy per person rises as density rises",
   "The two per-person measures move in opposite directions",
   "Density is unrelated to either per-person measure"], ans=0,
   why="Density rises at every step while both per-person measures fall at every step, footprint from 6.8 to 3.2 global hectares and transport energy from 82 to 11 gigajoules. EK SPS-6.B.1 names the large ecological footprint of cities among the challenges, and this record shows why the per-city and per-person readings of that measure differ."),

 dict(q="The cost of developing one hectare on two kinds of site is recorded below. Using the accompanying figures, what does the comparison show?",
   table=dict(headers=["Cost component per hectare (millions)", "Brownfield site", "Greenfield site"],
     rows=[["Land acquisition", "1.8", "0.9"],
           ["Contamination remediation", "2.4", "0.0"],
           ["New roads, water and sewerage", "0.3", "2.1"],
           ["Farmland consumed (hectares)", "0.0", "1.0"]]),
   choices=[
   "The brownfield site costs 4.5 million against the greenfield site's 3.0 million, entirely because of remediation, while consuming no farmland and needing almost no new infrastructure",
   "The brownfield site is cheaper in total than the greenfield site",
   "The greenfield site requires more remediation than the brownfield site",
   "The two sites cost the same in total",
   "The brownfield site consumes more farmland than the greenfield site"], ans=0,
   why="Adding the three cost rows gives 4.5 million for the brownfield site and 3.0 million for the greenfield one, and the 2.4 million remediation charge is larger than the whole 1.5 million difference. EK SPS-6.B.2 names remediation and redevelopment of brownfields among the responses, and learning objective SPS-6.B asks how effective such attempts are, which means pricing them."),

 dict(q="A city's ecological footprint is broken down below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Component", "Area required (square kilometres)"],
     rows=[["The city's own built-up area", "340"],
           ["Land to produce its food", "18,900"],
           ["Land to produce its timber and fibre", "5,600"],
           ["Land and sea to absorb its carbon emissions", "22,400"]]),
   choices=[
   "The three off-site components total 46,900 square kilometres, about 138 times the city's own built-up area, and carbon absorption alone is the largest of them",
   "The city's built-up area is the largest component",
   "The components total less than the city's own area",
   "Food production is the largest component of the footprint",
   "The footprint lies entirely within the city's boundary"], ans=0,
   why="The three off-site components sum to 46,900 square kilometres against a built-up area of 340, a ratio of about 138 to 1, and the carbon component at 22,400 exceeds the food component at 18,900. EK SPS-6.B.1 names the large ecological footprint of cities among the challenges, and the ratio is what the word large refers to."),

 dict(q="What limitation should be stated when comparing per-person footprints across cities of different densities?", choices=[
   "Denser cities also tend to differ in income, climate and industrial structure, so density is not the only thing varying between them",
   "Ecological footprints cannot be estimated for any city",
   "Densities and footprints can never appear in one record",
   "A consistent pattern across four cities establishes its cause",
   "The framework forbids comparing cities on environmental measures"], ans=0,
   why="EK SPS-6.B.1 names the large ecological footprint of cities among the challenges without attributing it to a single variable. A footprint responds to what a population consumes as well as to how it is arranged, so a density gradient narrows the explanation without isolating it."),

 dict(q="A city council asks what this topic establishes about its options. Which answer states it accurately?", choices=[
   "The framework names six sustainability challenges and four responses, and asks that each response be judged on what it achieves, what it costs and what it displaces rather than on being adopted",
   "The framework names four responses and states that each of them solves its challenge completely",
   "The framework names six challenges for which no response exists",
   "The framework establishes that urban sustainability challenges cannot be measured",
   "The framework's responses address economic rather than environmental challenges"], ans=0,
   why="EK SPS-6.B.1 supplies the challenges, EK SPS-6.B.2 the responses with the hedge CAN INCLUDE, and learning objective SPS-6.B asks for their effectiveness. Adopting a policy and achieving an outcome are different things, which is exactly what the objective's verb is there to insist on."),
]
