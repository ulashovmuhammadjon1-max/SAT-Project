# AP HUMAN GEOGRAPHY 6.10 Challenges of Urban Changes -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding SPS-6, "Urban areas
# face unique economic, political, cultural, and environmental challenges."
# Learning objective SPS-6.A, "Explain causes and effects of geographic change
# within urban areas." Suggested skill 4.E.
#
# Essential knowledge -- five statements, the largest set in the unit:
#   SPS-6.A.1  As urban populations move within a city, economic and social
#              challenges result, including: issues related to housing and
#              housing discrimination such as redlining, blockbusting, and
#              affordability; access to services; rising crime; environmental
#              injustice; and the growth of disamenity zones or zones of
#              abandonment.
#   SPS-6.A.2  Squatter settlements and conflicts over land tenure within large
#              cities have increased.
#   SPS-6.A.3  Responses to economic and social challenges in urban areas can
#              include inclusionary zoning and local food movements.
#   SPS-6.A.4  Urban renewal and gentrification have both positive and negative
#              consequences.
#   SPS-6.A.5  Functional and geographic fragmentation of governments -- the way
#              government agencies and institutions are dispersed between state,
#              county, city, and neighborhood levels -- presents challenges in
#              addressing urban issues.
#
# THE FIVE STATEMENTS FORM A SEQUENCE, and item 30 keys on it: challenges arise
# (A.1), one particular challenge has grown (A.2), responses exist (A.3), the
# two biggest responses cut both ways (A.4), and the machinery for responding is
# itself divided (A.5). A student who learns them as five unrelated lists misses
# that the last one is the reason the third is so hard.
#
# HOW THE TWO NAMED DISCRIMINATION PRACTICES ARE HANDLED. The CED names redlining
# and blockbusting, so this module defines both -- items 3 and 4 -- because a
# student cannot recognize a practice they cannot describe. The definitions state
# the MECHANISM and nothing else: no real place is named, no claim is made about
# where or when either occurred or whether either continues, and no party is
# named as having done it. What makes each of them a housing challenge is
# structural and can be stated without any of that.
#
# SPS-6.A.4 IS EXPLICITLY TWO-SIDED, exactly like IMP-6.D.1 in Topic 6.8: urban
# renewal and gentrification have BOTH positive AND negative consequences. Items
# 14, 15, 16 and 17 hold both halves, and item 17's distractors are the two
# one-sided readings. Neither a key celebrating gentrification nor one condemning
# it would be reporting this statement.
#
# WHAT THE CED DEFINES AND WHAT IT DOES NOT. It names the terms and defines only
# one of them -- fragmentation, which it glosses inside SPS-6.A.5. The working
# definitions used here for the rest: affordability is housing cost measured
# against income rather than in absolute terms (item 5, item 27); environmental
# injustice is the uneven exposure of some communities to environmental hazards
# (item 7); a disamenity zone is an area outside the reach of ordinary services
# and sometimes outside effective public control, and a zone of abandonment is
# one whose property has been given up on (item 8); inclusionary zoning requires
# or induces a share of new housing to be affordable (item 11); land tenure is
# the recognized right to occupy land, which is why disputes over it are the
# characteristic conflict of a squatter settlement (item 10).
#
# SYNONYM CARE. `geo_check` treats {"squatter settlement", "informal
# settlement"} as one construct, so no choice list offers both names.
#
# NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.10", "Challenges of Urban Changes", 6)

QUESTIONS = [
 dict(q="According to the framework, what produces the economic and social challenges this topic describes?", choices=[
   "The movement of urban populations within a city",
   "The movement of populations between countries",
   "The physical expansion of a country's territory",
   "Changes in a country's climate",
   "The construction of new cities on empty land"], ans=0,
   why="EK SPS-6.A.1 begins by saying that AS URBAN POPULATIONS MOVE WITHIN A CITY, economic and social challenges result. The subject is redistribution inside an urban area rather than movement into or between countries."),

 dict(q="Which set of challenges does the framework name as resulting from movement within a city?", choices=[
   "Housing and housing discrimination, affordability, access to services, rising crime, environmental injustice, and the growth of disamenity zones or zones of abandonment",
   "Suburbanization, sprawl, and decentralization",
   "Mixed land use, walkability, and smart growth",
   "Site, situation, and cycles of development",
   "Rank-size distributions, primacy, and gravity"], ans=0,
   why="EK SPS-6.A.1 names exactly this set. Suburbanization and sprawl are processes in EK PSO-6.A.4, the design initiatives belong to EK IMP-6.C.1, and the size principles to EK PSO-6.C.1, so each rejected option comes from a different statement."),

 dict(q="What is redlining?", choices=[
   "The practice of refusing or restricting mortgage lending and insurance in areas marked out as high risk, so that whole neighbourhoods are cut off from credit",
   "The practice of drawing new municipal boundaries around a city",
   "The marking of streets to be widened for traffic",
   "The zoning of land for industrial rather than residential use",
   "The demolition of housing to make way for a road"], ans=0,
   why="EK SPS-6.A.1 names redlining among the housing discrimination issues that result as urban populations move within a city. The mechanism is that the judgement is applied to an AREA rather than to an applicant, so every household in the area is affected by where it lives."),

 dict(q="What is blockbusting?", choices=[
   "Persuading owners to sell quickly and cheaply by suggesting that their neighbourhood's composition is about to change, then reselling the properties at much higher prices",
   "Demolishing an entire block of housing at once",
   "Building an unusually large block of flats in a low-rise district",
   "Combining several small plots into one large development site",
   "Closing a street to through traffic"], ans=0,
   why="EK SPS-6.A.1 names blockbusting among the housing discrimination issues. The practice works by manufacturing the expectation of a fall in value, since the fear of the fall is what produces the cheap sale it is used to obtain."),

 dict(q="What does housing AFFORDABILITY measure?", choices=[
   "Housing cost measured against household income, so a cheap dwelling can still be unaffordable to a low-income household",
   "The absolute price of a dwelling, regardless of who is buying it",
   "The physical quality of a dwelling's construction",
   "The distance from a dwelling to the city centre",
   "The number of dwellings built in a city each year"], ans=0,
   why="EK SPS-6.A.1 names affordability among the housing issues resulting as urban populations move within a city. Affordability is a ratio rather than a price, which is why the least expensive districts of a city can be the least affordable ones."),

 dict(q="What does the framework's challenge of ACCESS TO SERVICES refer to?", choices=[
   "Whether residents of a district can actually reach schools, health care, shops and transport, which depends on where those are and how they are reached",
   "Whether a city provides any services at all",
   "The total number of services in a city",
   "The cost of running a city's services",
   "The architectural quality of service buildings"], ans=0,
   why="EK SPS-6.A.1 names access to services among the challenges resulting as urban populations move within a city. Access is a relationship between a household and a facility, so a city can be well provided overall and still contain districts that reach nothing."),

 dict(q="The framework lists rising crime among the challenges that result as urban populations move within a city. What is the geographic content of that item?", choices=[
   "Crime is distributed unevenly within a city and concentrates where investment, services and stable occupancy have withdrawn, so it is part of the same pattern as the other challenges listed",
   "Crime is spread evenly across every district of a city",
   "Crime is a national rather than an urban phenomenon",
   "Crime rates are identical in every city in the world",
   "Crime has no relationship to any other feature of a district"], ans=0,
   why="EK SPS-6.A.1 lists rising crime alongside housing issues, access to services and the growth of zones of abandonment, all as consequences of movement within a city. What makes it a geographic item rather than a criminological one is that it appears in the same districts as the rest of the list and for the same underlying reason."),

 dict(q="What is environmental injustice in an urban context?", choices=[
   "The uneven exposure of some communities to environmental hazards such as pollution, waste facilities and contaminated land",
   "The equal distribution of parks across a city",
   "The legal protection of endangered species within a city",
   "The requirement that new buildings meet energy standards",
   "The tendency of cities to be warmer than surrounding countryside"], ans=0,
   why="EK SPS-6.A.1 names environmental injustice among the challenges resulting as urban populations move within a city. What makes it a justice question rather than merely an environmental one is that the burden and the benefit fall on different communities."),

 dict(q="What are disamenity zones and zones of abandonment?", choices=[
   "Areas outside the reach of ordinary services, sometimes beyond effective public control, and areas whose property has been given up on and left",
   "Districts reserved for parks and open space",
   "The most expensive residential districts of a city",
   "Zones set aside for future development",
   "Areas where new building is temporarily prohibited"], ans=0,
   why="EK SPS-6.A.1 names the growth of disamenity zones or zones of abandonment among the challenges resulting as urban populations move within a city. Both are what remains where investment, services and residents have withdrawn, which is why the statement pairs them."),

 dict(q="What does the framework say about squatter settlements and land tenure conflicts?", choices=[
   "Both have increased within large cities",
   "Both have disappeared from large cities",
   "Squatter settlements have increased while tenure conflicts have ended",
   "Neither occurs within large cities",
   "Both are confined to rural areas"], ans=0,
   why="EK SPS-6.A.2 states that squatter settlements and conflicts over land tenure within large cities have increased. The statement pairs them because the second follows from the first: settlement without recognized rights is what a tenure conflict is a conflict about."),

 dict(q="Why is LAND TENURE the characteristic point of conflict in a squatter settlement?", choices=[
   "Residents occupy land without a recognized legal right to it, so their homes, their investment in them and their access to services all rest on an unsettled claim",
   "Because the land is physically unsuitable for building",
   "Because residents refuse to pay for services",
   "Because such settlements have no residents",
   "Because tenure conflicts concern only agricultural land"], ans=0,
   why="EK SPS-6.A.2 names squatter settlements AND conflicts over land tenure together, which identifies what the conflict is about. Without a recognized right, a household cannot safely improve its dwelling and a utility has no straightforward basis on which to connect it."),

 dict(q="What is inclusionary zoning?", choices=[
   "A requirement or inducement that a share of the dwellings in a new development be affordable to lower-income households",
   "A rule excluding certain kinds of household from a district",
   "The separation of residential from industrial land uses",
   "A restriction on the height of new buildings",
   "A requirement that all new housing be built at high density"], ans=0,
   why="EK SPS-6.A.3 names inclusionary zoning among the responses to economic and social challenges in urban areas. It works by attaching a condition to permission to build, which places affordable dwellings inside new development rather than in a separate district."),

 dict(q="Why does the framework list local food movements among RESPONSES to urban challenges?", choices=[
   "They address access to fresh food in districts that lack it, which is one form of the access-to-services challenge the framework names",
   "They reduce the price of all housing in a city",
   "They resolve conflicts over land tenure",
   "They eliminate environmental injustice entirely",
   "They are the only response the framework recognizes"], ans=0,
   why="EK SPS-6.A.3 names local food movements alongside inclusionary zoning as responses, and EK SPS-6.A.1 names access to services among the challenges. Food deserts are the specific access problem such movements address, which is why a food response belongs on a list about urban challenges."),

 dict(q="What does the framework's word CAN in 'responses can include inclusionary zoning and local food movements' indicate?", choices=[
   "That these are examples of possible responses rather than a complete or guaranteed list",
   "That these responses are required of every city",
   "That no other response has ever been attempted",
   "That these responses always succeed",
   "That responses are impossible in urban areas"], ans=0,
   why="EK SPS-6.A.3 says responses CAN INCLUDE inclusionary zoning and local food movements, which is illustrative rather than exhaustive. The hedge also stops short of claiming that either response resolves the challenge it addresses."),

 dict(q="What does the framework say about urban renewal and gentrification?", choices=[
   "Both have positive and negative consequences",
   "Both have only positive consequences",
   "Both have only negative consequences",
   "Urban renewal has positive consequences and gentrification only negative ones",
   "Neither has any measurable consequence"], ans=0,
   why="EK SPS-6.A.4 states that urban renewal and gentrification have BOTH positive and negative consequences. The framework declines to settle the question, so a module keyed either way would be reporting something other than the statement."),

 dict(q="Which are POSITIVE consequences that can follow from urban renewal or gentrification?", choices=[
   "Buildings repaired, vacant land brought back into use, services returning, and a district's tax base recovering",
   "Long-standing residents priced out of the district",
   "The loss of businesses that served the previous population",
   "The dispersal of an established community",
   "A rise in rents beyond what existing residents can pay"], ans=0,
   why="EK SPS-6.A.4 says urban renewal and gentrification have both positive and negative consequences, and these are the positive side. Investment returning to a district that had lost it repairs the physical stock and restores services, which is a real gain to whoever remains to enjoy it."),

 dict(q="Which are NEGATIVE consequences that can follow from urban renewal or gentrification?", choices=[
   "Rents and prices rising beyond what existing residents can pay, so an established community is dispersed and the businesses serving it close",
   "Vacant buildings being repaired and reoccupied",
   "Services returning to a district that had lost them",
   "A district's tax base recovering",
   "Derelict land being brought back into use"], ans=0,
   why="EK SPS-6.A.4 says urban renewal and gentrification have both positive and negative consequences, and these are the negative side. The same rise in value that funds the repairs is what prices out the households who lived through the decline."),

 dict(q="A student writes that gentrification is simply good for a neighbourhood. What does the framework require?", choices=[
   "That both the positive and the negative consequences be stated, since the framework asserts both",
   "That only the positive consequences be considered",
   "That only the negative consequences be considered",
   "That the question be left entirely unanswered",
   "That gentrification be shown never to occur"], ans=0,
   why="EK SPS-6.A.4 says urban renewal and gentrification have BOTH positive and negative consequences. The two lists are connected rather than independent, since the rising value that pays for the improvement is the same rise that displaces people."),

 dict(q="What does the framework mean by FUNCTIONAL AND GEOGRAPHIC FRAGMENTATION of governments?", choices=[
   "Government agencies and institutions are dispersed between state, county, city and neighbourhood levels, so responsibility for an urban issue is divided among many bodies",
   "A city government has collapsed entirely",
   "A city has been divided into two separate countries",
   "A national government has moved its capital",
   "A city has abolished all of its neighbourhood institutions"], ans=0,
   why="EK SPS-6.A.5 supplies this definition in its own words, glossing the term as the dispersal of agencies and institutions between state, county, city and neighborhood levels. It is one of the few terms the CED defines rather than merely naming."),

 dict(q="Why does fragmentation of government make urban problems harder to address?", choices=[
   "A problem whose geography crosses many jurisdictions can be solved only by bodies that must each agree, and none of them is accountable for the whole of it",
   "Because more governments always means more money",
   "Because fragmented governments are legally forbidden to cooperate",
   "Because urban problems affect only one district at a time",
   "Because fragmentation eliminates all local government"], ans=0,
   why="EK SPS-6.A.5 says fragmentation of governments presents challenges in addressing urban issues. Housing markets, watersheds, air sheds and labour markets are metropolitan while authority is divided, so the unit that has the problem and the unit that can act on it are different units."),

 dict(q="Why is the fragmentation described in the framework called FUNCTIONAL as well as geographic?", choices=[
   "Responsibility is divided by subject as well as by territory, so transport, water, housing and schooling can each sit with a different body over the same ground",
   "Because it functions only in some cities",
   "Because it concerns the functions of buildings rather than of governments",
   "Because it applies only to transport",
   "Because the two words mean the same thing"], ans=0,
   why="EK SPS-6.A.5 names functional AND geographic fragmentation. Two authorities can cover the same territory and still be unable to act together, because each holds a different subject, which is a second axis of division on top of the boundary one."),

 dict(q="How does the challenge of affordability connect to the process of gentrification?", choices=[
   "Rising prices in an improving district are simultaneously the measure of its improvement and the reason existing residents can no longer afford to stay",
   "The two are unrelated processes",
   "Gentrification lowers prices and so improves affordability",
   "Affordability concerns only newly built housing",
   "Gentrification affects only commercial property"], ans=0,
   why="EK SPS-6.A.1 names affordability among the challenges and EK SPS-6.A.4 says gentrification has both positive and negative consequences. Price is the single variable through which the positive and the negative consequences are transmitted, which is what makes them inseparable."),

 dict(q="Why does the growth of a zone of abandonment tend to reinforce itself?", choices=[
   "Departures reduce the demand and revenue that support services and maintenance, which gives those remaining further reason to leave",
   "Because abandoned property is quickly reoccupied",
   "Because services expand into districts that are losing population",
   "Because property values rise as buildings are vacated",
   "Because abandonment is reversed automatically after a fixed period"], ans=0,
   why="EK SPS-6.A.1 names the GROWTH of disamenity zones or zones of abandonment among the challenges resulting as urban populations move within a city. The word growth points at a process rather than a state, and a self-reinforcing withdrawal is what that process consists of."),

 dict(q="At which scales must the challenges in this topic be examined?", choices=[
   "The district, where a challenge is experienced, and the metropolitan area, whose divided governments and shared housing market produce it",
   "Only the metropolitan scale, since cities are metropolitan",
   "Only the district scale, since challenges are local",
   "The global scale only, since urbanization is worldwide",
   "No scale, since these are social rather than spatial questions"], ans=0,
   why="EK SPS-6.A.1 locates the challenges in movement WITHIN a city and EK SPS-6.A.5 locates the difficulty of responding in governments divided across a metropolitan area. A district-only account misses the cause and a metropolitan-only account misses who bears it."),

 dict(q="Which pairing of a description with the framework's term for it is CORRECT?", choices=[
   "Refusing mortgage lending across a whole marked-out neighbourhood, matched to redlining",
   "Refusing mortgage lending across a whole marked-out neighbourhood, matched to blockbusting",
   "Persuading owners to sell cheaply by predicting a change in the neighbourhood, matched to inclusionary zoning",
   "Requiring a share of new dwellings to be affordable, matched to environmental injustice",
   "Uneven exposure of some communities to pollution, matched to land tenure conflict"], ans=0,
   why="EK SPS-6.A.1, EK SPS-6.A.2 and EK SPS-6.A.3 name these terms for distinct things. Only one pairing here matches a description to the term the framework uses for it, and each of the others attaches a description to a different named concept."),

 dict(q="Lending outcomes by district in one city are recorded below. Using the accompanying record, which conclusion is best supported?",
   table=dict(headers=["District", "Risk grade assigned to the district", "Mortgage applications", "Applications refused (%)", "Median dwelling value change over 40 years (%)"],
     rows=[["District 1", "A", "4,800", "4", "310"],
           ["District 2", "B", "3,900", "11", "218"],
           ["District 3", "C", "3,100", "29", "64"],
           ["District 4", "D", "2,700", "62", "9"]]),
   choices=[
   "Refusal rates rise from 4 to 62 percent as the assigned grade falls, and value growth falls from 310 to 9 percent, so the districts denied credit are the districts whose values did not rise",
   "Refusal rates and value growth rise together",
   "The district with the highest refusal rate had the greatest value growth",
   "Refusal rates are identical across the four districts",
   "The record shows nothing about the relationship between credit and value"], ans=0,
   why="Refusal rates rise at every step from 4 to 62 percent as the grade falls, while forty-year value growth falls at every step from 310 to 9 percent. EK SPS-6.A.1 names redlining among the housing discrimination issues, and a judgement applied to an area rather than to an applicant produces exactly this pattern of withheld credit and withheld value."),

 dict(q="Rents and incomes in four districts are recorded below. Using the accompanying figures, which district faces the greatest affordability problem?",
   table=dict(headers=["District", "Median household income", "Median monthly rent"],
     rows=[["District 1", "68,000", "1,300"],
           ["District 2", "42,000", "1,150"],
           ["District 3", "27,000", "980"],
           ["District 4", "19,000", "870"]]),
   choices=[
   "District 4, where rent takes about 55 percent of median income even though its rent is the lowest of the four",
   "District 1, because it has the highest rent",
   "District 2, because it is closest to the middle",
   "District 3, because its rent is close to a thousand",
   "All four equally, since each district has rents and incomes"], ans=0,
   why="Annual rent as a share of median income works out at about 23, 33, 44 and 55 percent across the four districts, so the burden rises as rents fall. EK SPS-6.A.1 names affordability among the housing challenges, and affordability is a ratio, which is why the cheapest district is the least affordable one here."),

 dict(q="Four metropolitan areas are compared below. Using the accompanying record, which conclusion is supported?",
   table=dict(headers=["Metropolitan area", "Separate general-purpose local governments", "Separate transit operators", "Years to complete a cross-boundary transit project"],
     rows=[["Metro W", "3", "1", "6"],
           ["Metro X", "27", "4", "11"],
           ["Metro Y", "88", "9", "19"],
           ["Metro Z", "140", "14", "26"]]),
   choices=[
   "Both measures of fragmentation rise together and the time taken rises with them, from 6 years where there are 3 governments to 26 where there are 140",
   "Time taken falls as the number of governments rises",
   "The most fragmented metropolitan area completed its project fastest",
   "The number of transit operators is unrelated to the number of governments",
   "No relationship can be read, since the four areas differ in size"], ans=0,
   why="Governments rise from 3 to 140, transit operators from 1 to 14 and completion time from 6 to 26 years, all at every step. EK SPS-6.A.5 says functional and geographic fragmentation of governments presents challenges in addressing urban issues, and a project crossing more boundaries needs more agreements before it can begin."),

 dict(q="What limitation should be stated when using completion times to demonstrate the effect of fragmented government?", choices=[
   "More fragmented metropolitan areas are usually larger and more complex as well, so size and fragmentation are difficult to separate in such a comparison",
   "Completion times cannot be recorded for infrastructure projects",
   "Counts of governments and years can never appear in one record",
   "A pattern across four cases establishes its own cause",
   "The framework forbids comparing metropolitan areas"], ans=0,
   why="EK SPS-6.A.5 says fragmentation PRESENTS CHALLENGES in addressing urban issues, which is a claim about difficulty rather than a measured effect size. Number of jurisdictions and metropolitan scale rise together, so a record showing both cannot attribute the delay to one of them alone."),

 dict(q="A summary must connect this topic's five statements rather than list them. Which summary does that?", choices=[
   "Movement within cities produces housing, service, environmental and abandonment challenges; informal settlement and tenure disputes have grown; responses exist; the two largest responses cut both ways; and divided government makes any response harder to deliver",
   "Movement within cities produces challenges to which no response has ever been attempted",
   "Urban renewal and gentrification resolve every challenge the framework names",
   "Fragmented government is the only urban challenge the framework identifies",
   "The five statements describe unrelated phenomena with no connection between them"], ans=0,
   why="EK SPS-6.A.1 supplies the challenges, EK SPS-6.A.2 the growth of one of them, EK SPS-6.A.3 the responses, EK SPS-6.A.4 their two-sidedness and EK SPS-6.A.5 the difficulty of delivering them. The last statement is the reason the third is hard, which is the connection a list of five would miss."),
]
