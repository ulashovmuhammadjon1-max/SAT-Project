# AP U.S. HISTORY 1.2 Native American Societies Before European Contact
# (title copied from US_HISTORY_topics.json)
# Unit 1, Period 1: 1491 to 1607. Suggested skill 1.A, identify a historical concept,
# development, or process. Reasoning process printed for this topic: Comparison.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 1 Learning Objective B
#       Explain how and why various native populations in the period before European
#       contact interacted with the natural environment in North America.
#
#   KC-1.1       As native populations migrated and settled across the vast expanse of
#                North America over time, they developed distinct and increasingly
#                complex societies by adapting to and transforming their diverse
#                environments.
#   KC-1.1.I     Different native societies adapted to and transformed their
#                environments through innovations in agriculture, resource use, and
#                social structure.
#   KC-1.1.I.A   The spread of maize cultivation from present-day Mexico northward into
#                the present-day American Southwest and beyond supported economic
#                development, settlement, advanced irrigation, and social
#                diversification among societies.
#   KC-1.1.I.B   Societies responded to the aridity of the Great Basin and the
#                grasslands of the western Great Plains by developing largely mobile
#                lifestyles.
#   KC-1.1.I.C   In the Northeast, the Mississippi River Valley, and along the Atlantic
#                seaboard, some societies developed mixed agricultural and
#                hunter-gatherer economies that favored the development of permanent
#                villages.
#   KC-1.1.I.D   Societies in the Northwest and present-day California supported
#                themselves by hunting and gathering, and in some areas developed
#                settled communities supported by the vast resources of the ocean.
#
#   THEMATIC FOCUS printed on this topic page, Geography and the Environment GEO:
#       Geographic and environmental factors, including competition over and debates
#       about natural resources, shape the development of America and foster regional
#       diversity. The development of America impacts the environment and reshapes
#       geography, which leads to debates about environmental and geographic issues.
#
#   Reasoning Process 1, Comparison, 1.i: Describe similarities and/or differences
#   between different historical developments or processes.
#
# WHAT IS NOT KEYED. The framework's four sub-points are the whole of the Required
# Course Content for this topic, and they name FOUR AREAS and FOUR WAYS OF LIFE and
# nothing else. No key here names a people, a date, a crop other than the maize the
# framework itself names, or a European. The CED's optional-sources list mentions
# Hohokam, Apache, Lenape, Chinook and others; the CED says in as many words that none
# of the exam questions requires students to have studied those specific sources, so
# nothing here rests on them.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1491 to 1607", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("1.2", "Native American Societies Before European Contact", 1)

_T_REGIONS = dict(
    headers=["Area of North America (illustrative)",
             "Environmental condition described",
             "Way of life described"],
    rows=[["Area W", "Arid basin and open grassland",
           "Largely mobile, moving with the seasons"],
          ["Area X", "River valley with fertile floodplain",
           "Permanent villages, farming with hunting and fishing"],
          ["Area Y", "Dry uplands watered by canals dug for the purpose",
           "Permanent towns supported by maize"],
          ["Area Z", "Ocean coast rich in fish and sea mammals",
           "Settled communities that do not farm"]])

_T_SITES = dict(
    headers=["Site (illustrative)",
             "Months of the year the site was occupied",
             "Permanent dwellings recorded at the site"],
    rows=[["Site 1", "12", "40"],
          ["Site 2", "4", "0"],
          ["Site 3", "12", "25"],
          ["Site 4", "3", "0"]])

QUESTIONS = [

 dict(q="Unit 1's Learning Objective B asks students to explain how and why various "
        "native populations, in the period before European contact, did what?",
      choices=[
        "Interacted with the natural environment in North America",
        "Interacted with European traders along the Atlantic seaboard",
        "Migrated southward from the Great Plains into present-day Mexico",
        "Adopted a single shared system of government across the continent",
        "Recorded their own histories in written documents"],
      ans=0,
      why="Unit 1 Learning Objective B reads 'Explain how and why various native "
          "populations in the period before European contact interacted with the natural "
          "environment in North America.' Contact with Europeans is placed after this "
          "period by the objective's own wording, and neither a continental government "
          "nor written record-keeping appears anywhere in KC-1.1.I."),

 dict(q="KC-1.1.I.A describes the spread of maize cultivation. In which direction, and "
        "between which areas, does the framework say it spread?",
      choices=[
        "Northward from present-day Mexico into the present-day American Southwest and "
        "beyond",
        "Southward from the present-day American Southwest into present-day Mexico",
        "Eastward from present-day California into the Great Basin",
        "Westward from the Atlantic seaboard into the Mississippi River Valley",
        "Northward from the Caribbean islands into the Southeast"],
      ans=0,
      why="KC-1.1.I.A states that the spread of maize cultivation ran from present-day "
          "Mexico northward into the present-day American Southwest and beyond. The "
          "reversal keeps the two places and exchanges them, which is the likeliest way "
          "to misremember the sentence; the other routes name areas the sentence does "
          "not connect at all."),

 dict(q="According to KC-1.1.I.A, the spread of maize cultivation supported four things "
        "among societies. Which set names all four?",
      choices=[
        "Economic development, settlement, advanced irrigation, and social "
        "diversification",
        "Economic development, settlement, written record-keeping, and warfare",
        "Settlement, advanced irrigation, monarchy, and long-distance seafaring",
        "Economic development, social diversification, metalworking, and horse breeding",
        "Advanced irrigation, settlement, and a common language across societies"],
      ans=0,
      why="KC-1.1.I.A names economic development, settlement, advanced irrigation, and "
          "social diversification as what the spread of maize cultivation supported. "
          "Record-keeping, warfare, monarchy, seafaring, metalworking, horse breeding and "
          "a shared language are not in that sentence."),

 dict(q="What does KC-1.1.I.B say societies developed, and in response to what?",
      choices=[
        "Largely mobile lifestyles, in response to the aridity of the Great Basin and the "
        "grasslands of the western Great Plains",
        "Permanent towns, in response to the aridity of the Great Basin and the grasslands "
        "of the western Great Plains",
        "Largely mobile lifestyles, in response to the ocean resources of the Northwest "
        "coast",
        "Mixed agricultural and hunter-gatherer economies, in response to the Mississippi "
        "River Valley",
        "Irrigated fields, in response to the woodlands of the Northeast"],
      ans=0,
      why="KC-1.1.I.B states that societies responded to the aridity of the Great Basin "
          "and the grasslands of the western Great Plains by developing largely mobile "
          "lifestyles. Two of the alternatives keep half the sentence and replace the "
          "other half, which is why the response and the environment have to be read "
          "together; the mixed economies belong to KC-1.1.I.C."),

 dict(q="KC-1.1.I.C names three areas in which some societies developed mixed "
        "agricultural and hunter-gatherer economies. Which set names all three?",
      choices=[
        "The Northeast, the Mississippi River Valley, and the Atlantic seaboard",
        "The Northeast, the Great Basin, and the Atlantic seaboard",
        "The Mississippi River Valley, the western Great Plains, and present-day "
        "California",
        "The Northwest, the Atlantic seaboard, and the American Southwest",
        "The Great Basin, the western Great Plains, and the Northwest"],
      ans=0,
      why="KC-1.1.I.C names the Northeast, the Mississippi River Valley, and the Atlantic "
          "seaboard. The Great Basin and the western Great Plains belong to KC-1.1.I.B, "
          "the Northwest and present-day California to KC-1.1.I.D, and the American "
          "Southwest to KC-1.1.I.A, so each rejected set imports an area from a different "
          "sub-point."),

 dict(q="KC-1.1.I.C says a particular kind of economy favored a particular kind of "
        "settlement. Which pairing does the framework state?",
      choices=[
        "Mixed agricultural and hunter-gatherer economies favored the development of "
        "permanent villages",
        "Mixed agricultural and hunter-gatherer economies favored the development of "
        "largely mobile lifestyles",
        "Economies resting wholly on hunting favored the development of permanent "
        "villages",
        "Irrigated maize agriculture favored the development of seasonal camps",
        "Trade with distant societies favored the development of permanent villages"],
      ans=0,
      why="KC-1.1.I.C states that some societies developed mixed agricultural and "
          "hunter-gatherer economies that favored the development of permanent villages. "
          "Mobile lifestyles are KC-1.1.I.B's outcome and belong to different areas, "
          "irrigated maize is KC-1.1.I.A's, and the framework nowhere makes trade the "
          "cause of settlement in these areas."),

 dict(q="KC-1.1.I.D describes societies in the Northwest and present-day California. How "
        "does the framework say they supported themselves?",
      choices=[
        "By hunting and gathering, with settled communities in some areas supported by the "
        "vast resources of the ocean",
        "By irrigated maize agriculture, with permanent towns supported by the vast "
        "resources of the ocean",
        "By hunting and gathering, with no settled communities anywhere in those areas",
        "By mixed agricultural and hunter-gatherer economies that favored permanent "
        "villages",
        "By largely mobile lifestyles adopted in response to aridity"],
      ans=0,
      why="KC-1.1.I.D states that societies in the Northwest and present-day California "
          "supported themselves by hunting and gathering, and in some areas developed "
          "settled communities supported by the vast resources of the ocean. The sentence "
          "holds hunting and gathering together with settlement, so an option denying "
          "either half misstates it; the mixed economies are KC-1.1.I.C's and the mobile "
          "lifestyles KC-1.1.I.B's."),

 dict(q="Which pairing of an area with the way of life KC-1.1.I describes there is the "
        "one the framework actually states?",
      choices=[
        "The Great Basin with largely mobile lifestyles, and the Northwest with settled "
        "communities drawing on ocean resources",
        "The Great Basin with settled communities drawing on ocean resources, and the "
        "Northwest with largely mobile lifestyles",
        "The Mississippi River Valley with largely mobile lifestyles, and the western "
        "Great Plains with permanent villages",
        "The American Southwest with hunting and gathering, and present-day California "
        "with irrigated maize",
        "The Atlantic seaboard with irrigated maize, and the Great Basin with permanent "
        "villages"],
      ans=0,
      why="KC-1.1.I.B places largely mobile lifestyles in the Great Basin and the western "
          "Great Plains, and KC-1.1.I.D places settled communities supported by the ocean "
          "in the Northwest and present-day California. Exchanging the two areas keeps "
          "both ways of life and still misreports the framework, which is why the pairing "
          "has to be read as a whole; the remaining options move permanent villages, "
          "maize and hunting to areas KC-1.1.I.A and KC-1.1.I.C assign elsewhere."),

 dict(q="The framework writes that societies in those two dry areas developed LARGELY "
        "mobile lifestyles. What does that qualifier do to the claim?",
      choices=[
        "It describes the general pattern without asserting that no society in those areas "
        "ever stayed in one place",
        "It asserts that every society in those areas moved constantly and never settled",
        "It restricts the claim to societies that also cultivated maize",
        "It makes the mobility a response to ocean resources rather than to aridity",
        "It places those societies outside the period this unit covers"],
      ans=0,
      why="KC-1.1.I.B's word 'largely' states a predominant pattern rather than a rule "
          "without exceptions, so the sentence supports the general claim and stops short "
          "of the absolute one. The same sentence gives aridity and grassland as the "
          "conditions responded to, not ocean resources, and KC-1.1 places these "
          "developments in the long period before the contact of KC-1.2."),

 dict(q="A hypothetical excavation report, its author unnamed, describes a dry upland "
        "settlement with canals carrying water to fields of maize and houses built to "
        "stand for generations. Which statement of KC-1.1.I does it most directly "
        "illustrate?",
      choices=[
        "KC-1.1.I.A, on maize cultivation supporting settlement and advanced irrigation",
        "KC-1.1.I.B, on largely mobile lifestyles developed in response to aridity",
        "KC-1.1.I.C, on mixed economies favoring the development of permanent villages",
        "KC-1.1.I.D, on hunting and gathering supported by the resources of the ocean",
        "KC-1.1, on native populations migrating across North America over time"],
      ans=0,
      why="KC-1.1.I.A names settlement and advanced irrigation among the things the "
          "spread of maize cultivation supported, and the described site combines exactly "
          "those two with the crop itself. The land is dry, but the response described is "
          "irrigation rather than the mobility of KC-1.1.I.B; no ocean and no mixed "
          "hunting economy appears, and KC-1.1 describes migration rather than a "
          "particular site."),

 dict(q="Suppose an illustrative notebook, its author unnamed, records a group in an arid "
        "basin that moved several times a year, carrying its shelters and following game "
        "across open grassland. Which framework statement does it illustrate?",
      choices=[
        "KC-1.1.I.B, on societies responding to aridity and grassland with largely mobile "
        "lifestyles",
        "KC-1.1.I.A, on the spread of maize cultivation supporting advanced irrigation",
        "KC-1.1.I.C, on mixed economies favoring the development of permanent villages",
        "KC-1.1.I.D, on settled communities supported by the vast resources of the ocean",
        "KC-1.1, on societies becoming increasingly complex over time"],
      ans=0,
      why="KC-1.1.I.B is the sentence that joins aridity and grassland to largely mobile "
          "lifestyles, and the described group has both the environment and the response. "
          "Nothing in the description involves maize, irrigation, permanent villages or "
          "the ocean, so KC-1.1.I.A, KC-1.1.I.C and KC-1.1.I.D do not fit, and KC-1.1 "
          "makes a claim about long-run complexity rather than about one group's "
          "movements."),

 dict(q="A hypothetical field notebook, its author unnamed, describes a village beside a "
        "river whose people planted crops in cleared ground and also hunted deer and "
        "netted fish through the year. Which statement of KC-1.1.I does it illustrate?",
      choices=[
        "KC-1.1.I.C, on mixed agricultural and hunter-gatherer economies favoring "
        "permanent villages",
        "KC-1.1.I.A, on maize cultivation supporting advanced irrigation in dry uplands",
        "KC-1.1.I.B, on largely mobile lifestyles developed in response to aridity",
        "KC-1.1.I.D, on communities supported by the vast resources of the ocean",
        "KC-1.1.I, on innovations in agriculture, resource use, and social structure alone"],
      ans=0,
      why="KC-1.1.I.C describes economies that mix agriculture with hunting and "
          "gathering and says such economies favored the development of permanent "
          "villages, which is precisely the combination described. The site is a river "
          "valley rather than dry upland or ocean coast, and the people stay rather than "
          "move, so KC-1.1.I.A, KC-1.1.I.B and KC-1.1.I.D do not apply; KC-1.1.I is the "
          "general statement under which all four sit."),

 dict(q="An illustrative museum label, its author unnamed, describes a coastal people "
        "living in large plank houses through the year and drawing their food from salmon "
        "runs and sea mammals rather than from planted fields. Which framework statement "
        "does it illustrate?",
      choices=[
        "KC-1.1.I.D, on hunting and gathering with settled communities supported by the "
        "vast resources of the ocean",
        "KC-1.1.I.C, on mixed agricultural and hunter-gatherer economies in river valleys",
        "KC-1.1.I.B, on largely mobile lifestyles developed in response to aridity",
        "KC-1.1.I.A, on the spread of maize cultivation and advanced irrigation",
        "KC-1.1, on native populations migrating and settling over time"],
      ans=0,
      why="KC-1.1.I.D is the only sub-point that puts settled communities and the absence "
          "of farming together, and it names the vast resources of the ocean as what "
          "supported them. Because there are no planted fields, KC-1.1.I.C's mixed "
          "economy and KC-1.1.I.A's maize both fail, and the people described do not move, "
          "which rules out KC-1.1.I.B."),

 dict(q="Using the table of illustrative areas, which conclusion does the record support?",
      table=_T_REGIONS,
      choices=[
        "Each area's recorded way of life differs, and each differs alongside a different "
        "environmental condition",
        "Every area is recorded as growing maize",
        "Only one area is recorded with a settled or permanent way of life",
        "The mobile way of life is recorded alongside the ocean coast",
        "The same way of life is recorded in every area"],
      ans=0,
      why="Read from the table alone: four areas carry four different environmental "
          "conditions and four different ways of life, and the two vary together. That "
          "covariation is what KC-1.1.I asserts when it says different native societies "
          "adapted to and transformed their environments. Maize appears in one row rather "
          "than four, three rows record settled or permanent life, and the mobile row is "
          "the arid basin rather than the ocean coast."),

 dict(q="Using the same table of illustrative areas, which claim goes BEYOND what the "
        "record can support?",
      table=_T_REGIONS,
      choices=[
        "That the peoples of these areas traded with one another",
        "That the recorded environmental conditions differ from area to area",
        "That three of the four areas are recorded with a settled or permanent way of life",
        "That one recorded way of life rests on maize",
        "That one recorded way of life is largely mobile"],
      ans=0,
      why="The table records an environmental condition and a way of life for each area "
          "and nothing about relations between areas, so exchange between them is the one "
          "claim of the five it cannot reach. The other four are read straight off the "
          "rows. KC-1.1.I concerns innovations in agriculture, resource use and social "
          "structure, none of which is a claim about trade between regions."),

 dict(q="The thematic focus printed on this topic page is Geography and the Environment. "
        "What does it state about geographic and environmental factors?",
      choices=[
        "That they shape the development of America and foster regional diversity",
        "That they are shaped by the development of America but do not shape it in turn",
        "That they begin to matter only after European contact",
        "That they produce uniformity across regions rather than diversity",
        "That they concern natural resources but have no bearing on settlement"],
      ans=0,
      why="The thematic focus states that geographic and environmental factors, including "
          "competition over and debates about natural resources, shape the development of "
          "America and foster regional diversity, and that the development of America in "
          "turn impacts the environment. Unit 1 Learning Objective B asks for exactly that "
          "two-way relationship in the period before European contact, and KC-1.1.I.A ties "
          "settlement to an environmental change."),

 dict(q="KC-1.1 says native societies developed by adapting to AND TRANSFORMING their "
        "diverse environments. Which of KC-1.1.I's four statements most clearly describes "
        "a society transforming an environment rather than only fitting into it?",
      choices=[
        "The advanced irrigation that followed the spread of maize cultivation",
        "The largely mobile lifestyles adopted in the Great Basin",
        "The hunting and gathering practised in the Northwest",
        "The vast resources of the ocean drawn on by coastal communities",
        "The grasslands of the western Great Plains"],
      ans=0,
      why="KC-1.1.I.A names advanced irrigation among the things the spread of maize "
          "cultivation supported, and digging channels to water dry ground alters the "
          "environment rather than accommodating it, which is the 'transforming' half of "
          "KC-1.1. Mobility in KC-1.1.I.B and hunting and gathering in KC-1.1.I.D are "
          "responses to conditions, and the ocean resources and the grasslands are the "
          "conditions themselves."),

 dict(q="Why does KC-1.1.I.A's list include social diversification alongside economic "
        "development and settlement?",
      choices=[
        "Because the framework treats an agricultural change as having social consequences "
        "as well as economic and settlement ones",
        "Because the framework treats maize cultivation as a purely economic development",
        "Because social differences existed only where maize was not cultivated",
        "Because the framework ranks social diversification above the other consequences",
        "Because maize cultivation is described as leaving societies otherwise unchanged"],
      ans=0,
      why="KC-1.1.I.A places social diversification in the same list as economic "
          "development, settlement and advanced irrigation, so the framework has one "
          "agricultural change producing consequences of several kinds at once. The "
          "sentence gives no ranking among the four, makes no claim about societies "
          "without maize, and its own list is what rules out calling the change purely "
          "economic; KC-1.1.I likewise names social structure alongside agriculture."),

 dict(q="The suggested skill printed on this topic page is 1.A. How does the framework "
        "state that skill?",
      choices=[
        "Identify a historical concept, development, or process",
        "Explain a historical concept, development, or process",
        "Identify and describe a historical context for a specific historical development "
        "or process",
        "Identify patterns among or connections between historical developments and "
        "processes",
        "Identify the evidence used in a source to support an argument"],
      ans=0,
      why="Skill 1.A as printed on this topic page reads 'Identify a historical concept, "
          "development, or process', and it is the skill Unit 1 Learning Objective B asks "
          "students to apply to the four ways of life KC-1.1.I describes. The other four "
          "are skills 1.B, 4.A, 5.A and 3.B, each printed on other topic pages of this "
          "course."),

 dict(q="A hypothetical revision guide states that KC-1.1.I ranks native societies from "
        "least to most developed according to whether they farmed. Why does the framework "
        "not support that?",
      choices=[
        "KC-1.1.I presents four ways of adapting to different environments and ranks none "
        "of them",
        "KC-1.1.I states that all native societies cultivated maize",
        "KC-1.1.I says nothing about agriculture at all",
        "KC-1.1.I applies only to the period after European contact",
        "KC-1.1.I describes a single way of life shared across North America"],
      ans=0,
      why="KC-1.1.I says different native societies adapted to and transformed their "
          "environments through innovations in agriculture, resource use, and social "
          "structure, and its four sub-points set those ways of life beside one another "
          "without ordering them. Agriculture is named in KC-1.1.I.A and KC-1.1.I.C but "
          "not everywhere, Learning Objective B places the topic before European contact, "
          "and KC-1.1 calls the societies distinct rather than uniform."),

 dict(q="KC-1.1.I.B describes largely mobile societies and KC-1.1.I.D describes settled "
        "communities that did not farm. What does holding both statements together "
        "establish?",
      choices=[
        "That the framework does not make settled life depend on agriculture, since one "
        "settled way of life rests on hunting and gathering",
        "That the framework treats agriculture as the only possible basis for settled life",
        "That mobility and settlement are described by the framework as the same thing",
        "That the Great Basin and the Northwest are described as environmentally alike",
        "That settled communities are described only where maize was cultivated"],
      ans=0,
      why="KC-1.1.I.D has societies supporting themselves by hunting and gathering and "
          "nonetheless developing settled communities where ocean resources were vast, "
          "while KC-1.1.I.B has mobility follow from aridity and grassland. Together they "
          "make the resources of a place, not the presence of farming, what the framework "
          "connects to staying put, and they describe two environments the framework "
          "contrasts rather than equates."),

 dict(q="What does the phrase AND BEYOND allow, where the framework traces maize "
        "cultivation into the present-day American Southwest?",
      choices=[
        "That the framework does not fix the northern limit of the spread at the Southwest",
        "That the spread reversed direction once it reached the Southwest",
        "That maize cultivation is described as confined to the Southwest",
        "That the framework dates the spread precisely",
        "That the framework denies any spread outside present-day Mexico"],
      ans=0,
      why="KC-1.1.I.A writes that the spread ran from present-day Mexico northward into "
          "the present-day American Southwest 'and beyond', which leaves the far end of "
          "the movement open rather than stopping it at a boundary. A confinement to the "
          "Southwest or a denial of any spread contradicts the sentence outright, it "
          "states a direction rather than a reversal, and it gives no dates at all."),

 dict(q="What does the qualifier SOME rule out, where the framework says some societies "
        "in three named areas developed mixed agricultural and hunter-gatherer economies?",
      choices=[
        "A claim that every society in the Northeast, the Mississippi River Valley and "
        "along the Atlantic seaboard had that economy",
        "A claim that any society in those areas had a mixed economy of that kind",
        "A claim that permanent villages developed in those areas",
        "A claim that hunting and gathering were practised in those areas",
        "A claim that agriculture was practised in those areas"],
      ans=0,
      why="KC-1.1.I.C's word 'some' makes the mixed economy a pattern found among "
          "societies of those areas rather than a description of all of them, so a "
          "universal claim is the one the sentence blocks. The remaining four are things "
          "the same sentence asserts: it names the mixed economy, the hunting and "
          "gathering and the agriculture within it, and the permanent villages such "
          "economies favored."),

 dict(q="Which reading matches KC-1.1.I.D's statement that settled communities developed "
        "IN SOME AREAS of the Northwest and present-day California?",
      choices=[
        "Settlement is described as occurring in part of that region rather than "
        "throughout it",
        "Settlement is described as occurring everywhere in that region",
        "Settlement is described as absent from the whole of that region",
        "Settlement in that region is attributed to maize cultivation",
        "Settlement in that region is attributed to the aridity of the Great Basin"],
      ans=0,
      why="KC-1.1.I.D says societies there supported themselves by hunting and gathering "
          "and 'in some areas' developed settled communities, which places settlement in "
          "part of the region without either extending it to all of it or denying it. The "
          "same sentence attributes those communities to the vast resources of the ocean, "
          "not to maize, which belongs to KC-1.1.I.A, nor to aridity, which belongs to "
          "KC-1.1.I.B."),

 dict(q="Using the table of illustrative sites, what pattern do the entries record?",
      table=_T_SITES,
      choices=[
        "The two sites occupied for the whole year are the two at which permanent "
        "dwellings are recorded",
        "Permanent dwellings are recorded at every site",
        "The site occupied for the fewest months records the most permanent dwellings",
        "Every site was occupied for the whole year",
        "The same number of permanent dwellings is recorded at every site"],
      ans=0,
      why="Read from the table alone: two sites are occupied for twelve months and those "
          "same two carry the only permanent dwellings, while the two occupied for three "
          "and four months carry none. That is the link between staying and building that "
          "KC-1.1.I.C makes when it says mixed economies favored the development of "
          "permanent villages, and KC-1.1.I.B's mobile lifestyles are the other side of "
          "it. Two sites record no dwellings at all, the shortest-occupied site records "
          "none, and the counts differ."),

 dict(q="What do all four statements of KC-1.1.I have in common, as the framework writes "
        "them?",
      choices=[
        "Each links a way of life to the environment of the area in which it developed",
        "Each describes a society that cultivated maize",
        "Each describes a society that moved with the seasons",
        "Each describes contact between native societies and European traders",
        "Each describes one way of life shared across the whole of North America"],
      ans=0,
      why="KC-1.1.I.A ties settlement and irrigation to maize country, KC-1.1.I.B ties "
          "mobility to aridity and grassland, KC-1.1.I.C ties permanent villages to "
          "river valleys and the seaboard, and KC-1.1.I.D ties settled coastal "
          "communities to ocean resources, which is the pattern KC-1.1.I states in "
          "general and Unit 1 Learning Objective B asks students to explain. Maize and "
          "seasonal movement each appear in some sub-points only, and Europeans in none "
          "of them."),

 dict(q="An illustrative textbook caption, its author unnamed, states that the societies "
        "of the Northwest supported themselves chiefly by cultivating maize. Which "
        "framework sentence contradicts it?",
      choices=[
        "KC-1.1.I.D, which says those societies supported themselves by hunting and "
        "gathering",
        "KC-1.1.I.A, which traces maize cultivation northward from present-day Mexico",
        "KC-1.1.I.B, which describes largely mobile lifestyles in the Great Basin",
        "KC-1.1.I.C, which describes mixed economies in the Northeast",
        "KC-1.1, which describes native populations migrating and settling over time"],
      ans=0,
      why="KC-1.1.I.D states that societies in the Northwest and present-day California "
          "supported themselves by hunting and gathering, which is the direct denial of a "
          "maize-based livelihood there. KC-1.1.I.A concerns a different direction of "
          "spread and a different region, KC-1.1.I.B and KC-1.1.I.C concern other areas "
          "again, and KC-1.1 makes no claim about which crop was grown where."),

 dict(q="KC-1.1.I.A and KC-1.1.I.C both describe settlement. What distinguishes the basis "
        "the framework gives for each?",
      choices=[
        "KC-1.1.I.A ties settlement to maize cultivation and advanced irrigation, while "
        "KC-1.1.I.C ties permanent villages to economies mixing agriculture with hunting "
        "and gathering",
        "KC-1.1.I.A ties settlement to economies mixing agriculture with hunting and "
        "gathering, while KC-1.1.I.C ties permanent villages to maize cultivation and "
        "advanced irrigation",
        "Both tie settlement to the vast resources of the ocean",
        "Both tie settlement to the aridity of the Great Basin",
        "Neither of the two statements mentions settlement at all"],
      ans=0,
      why="KC-1.1.I.A names settlement and advanced irrigation among what the spread of "
          "maize cultivation supported, while KC-1.1.I.C says mixed agricultural and "
          "hunter-gatherer economies favored the development of permanent villages. "
          "Exchanging the two bases keeps every phrase and still misreports both "
          "sentences, which is why each has to be read with its own code; ocean resources "
          "belong to KC-1.1.I.D and aridity to KC-1.1.I.B."),

 dict(q="The reasoning process printed for this topic in the unit outline is Comparison. "
        "Which task does the framework's description of that process include?",
      choices=[
        "Describing similarities and/or differences between different historical "
        "developments or processes",
        "Describing causes and/or effects of a specific historical development or process",
        "Describing patterns of continuity and/or change over time",
        "Making a historically defensible claim",
        "Identifying a source's point of view, purpose, historical situation, or audience"],
      ans=0,
      why="The framework's Reasoning Process 1, Comparison, opens with describing "
          "similarities and differences between different historical developments or "
          "processes, and that is what Unit 1 Learning Objective B invites when it sets "
          "four regional ways of life beside one another in KC-1.1.I. Causes and effects "
          "belong to Causation, patterns over time to Continuity and Change, and the "
          "remaining two are historical thinking skills rather than reasoning processes."),

 dict(q="Which single sentence collects what the framework says about all four areas "
        "without adding to it?",
      choices=[
        "Different native societies adapted to and transformed their environments through "
        "innovations in agriculture, resource use, and social structure, and those "
        "innovations took a different form in each area the framework names",
        "Native societies across North America shared one way of life resting on maize "
        "cultivation",
        "Native societies were shaped by their environments but altered nothing about them",
        "Native societies developed permanent settlement only where they cultivated crops",
        "Native societies moved constantly wherever the land was dry or wooded"],
      ans=0,
      why="The first is KC-1.1.I in the framework's own words with the observation that "
          "its four sub-points describe four different forms, and it adds nothing else. "
          "KC-1.1 calls the societies distinct rather than uniform, KC-1.1.I.A's advanced "
          "irrigation is an alteration of the environment, KC-1.1.I.D has settled "
          "communities without farming, and KC-1.1.I.C has permanent villages in wooded "
          "river country."),
]
