# AP HUMAN GEOGRAPHY 5.12 Women in Agriculture -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding IMP-5, "Agricultural
# production and consumption patterns vary in different locations, presenting
# different environmental, social, economic, and cultural opportunities and
# challenges." Learning objective IMP-5.C, "Explain geographic variations in
# female roles in food production and consumption." Suggested skill 3.D, compare
# patterns and trends in maps and in quantitative and geospatial data.
#
# Essential knowledge -- ONE statement:
#   IMP-5.C.1  The role of females in food production, distribution, and
#              consumption varies in many places depending on the type of
#              production involved.
#
# THE STATEMENT'S SUBJECT IS VARIATION, and that decides how every item here is
# keyed. The CED does not say what women's role in agriculture IS; it says the
# role VARIES, and that it varies with the TYPE OF PRODUCTION. So:
#
#   - No key in this module asserts a universal role for women in agriculture.
#     An item keyed "women do X in farming" would contradict the one sentence
#     the topic rests on. Items 1, 2 and 23 key against exactly that, and item 2
#     offers the universal claim as its distractor.
#   - Where a key describes a role, it is tied to a STATED type of production --
#     a subsistence system, a mechanized commercial one, an export horticulture
#     operation -- because that is the variable the CED names.
#   - NO REAL COUNTRY OR REGION IS NAMED. Gendered divisions of agricultural
#     labour differ within countries as much as between them, they change, and
#     the CED names none. The three data items use lettered regions.
#
# THE STATEMENT NAMES THREE DOMAINS and they are easy to collapse into one:
# PRODUCTION (growing and tending), DISTRIBUTION (moving, trading, selling) and
# CONSUMPTION (preparing and allocating food within a household). Item 3 keys on
# all three, and items 10 and 11 exist so that distribution and consumption are
# not left as an afterthought to production.
#
# THE MECHANISM MOST WORTH TEACHING, and the one items 7, 8, 9 and 27 rest on:
# where women hold land less securely and obtain credit, inputs and advice less
# readily, the constraint is on ACCESS TO RESOURCES rather than on skill or
# effort. That is a claim about institutions, it is measurable, and it is what
# makes the topic answerable with data rather than with assertion -- which is
# also why the CED's suggested skill for this topic is data analysis.
#
# THE MEASUREMENT PROBLEM IS PART OF THE TOPIC. Work that is unpaid, seasonal,
# and carried out on a household's own holding is systematically under-recorded
# by labour statistics, so a figure for women's participation in agriculture can
# understate it badly. Items 12, 18 and 29 key on that, and item 29 states it as
# a limitation of the very kind of table items 26 to 28 use.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.12", "Women in Agriculture", 5)

QUESTIONS = [
 dict(q="What does the framework assert about the role of females in food production, distribution and consumption?", choices=[
   "That it varies in many places depending on the type of production involved",
   "That it is the same in every place and every farming system",
   "That females take no part in food production anywhere",
   "That it depends only on the climate of the region",
   "That it has never changed in any society"], ans=0,
   why="EK IMP-5.C.1 states that the role of females in food production, distribution and consumption varies in many places depending on the type of production involved. Variation is the claim itself, and the variable the statement names is the type of production."),

 dict(q="A student writes that women's role in agriculture is essentially the same everywhere. What is the objection from the framework?", choices=[
   "The framework's single statement on this topic is that the role varies, and that it varies with the type of production",
   "The framework agrees that the role is the same everywhere",
   "The framework says women have no role in agriculture",
   "The framework says the role varies only with climate",
   "The framework makes no claim about women in agriculture"], ans=0,
   why="EK IMP-5.C.1 is a statement about variation, so a claim of uniformity contradicts the only sentence the topic contains. Learning objective IMP-5.C reinforces this by asking for GEOGRAPHIC VARIATIONS in female roles rather than for a description of one role."),

 dict(q="Which three domains does the framework's statement cover?", choices=[
   "Food production, food distribution, and food consumption",
   "Food production, land ownership, and inheritance law",
   "Food consumption, education, and migration",
   "Food production, food distribution, and climate change",
   "Land tenure, credit, and mechanization"], ans=0,
   why="EK IMP-5.C.1 names food production, distribution and consumption in that order. Land tenure and credit are mechanisms that help explain the variation rather than domains the statement itself names, which is why they belong in the reasoning rather than in the list."),

 dict(q="In a household producing mainly for its own consumption, what pattern of work does the framework's variable of production type lead a geographer to expect?", choices=[
   "Women commonly carry a large share of field labour together with processing, water and fuel collection, and preparing what is eaten",
   "Women take no part in growing or preparing food",
   "All work is performed by hired labour",
   "The division of tasks is identical to that of a mechanized commercial farm",
   "Production, distribution and consumption are handled by separate specialists"], ans=0,
   why="EK IMP-5.C.1 says the role varies with the type of production involved, and a subsistence household is the type in which production, processing and consumption occur in the same place. Where the household is the productive unit, the same people carry out tasks a commercial system would separate."),

 dict(q="In a large mechanized commercial operation, how does the pattern of work typically differ from a subsistence household?", choices=[
   "Tasks are specialized and waged, and the recorded operator and machinery roles are more often held by men, while women's paid work concentrates in tasks such as sorting, packing and horticulture",
   "The division of work is identical to a subsistence household's",
   "No work of any kind is performed by women",
   "Every task is performed by the household that owns the land",
   "Production and consumption occur in the same household"], ans=0,
   why="EK IMP-5.C.1 makes the type of production the variable that the role depends on. Mechanization and waged employment separate tasks that a household performs together, and where the tasks separate the pattern of who does which one changes with them."),

 dict(q="Why can the introduction of machinery change the gendered division of agricultural labour?", choices=[
   "Machinery replaces some tasks and creates others, and who has access to training, credit and the machine itself decides who does the new work",
   "Machinery can be operated only by men for physical reasons",
   "Machinery eliminates all agricultural labour",
   "Machinery has no effect on who performs which task",
   "Machinery is distributed equally to everyone in a district"], ans=0,
   why="EK IMP-5.C.1 says the role varies depending on the type of production involved, and mechanization changes that type. The reallocation runs through access to the equipment and the training rather than through the task itself, which is why the outcome differs from place to place."),

 dict(q="Why does insecure land tenure limit what a woman farming a plot can achieve?", choices=[
   "Without secure rights she cannot safely invest in improvements she may not keep, and she often cannot use the land as security for a loan",
   "Insecure tenure changes the fertility of the soil",
   "Insecure tenure prevents any crop from being planted",
   "Insecure tenure affects only very large holdings",
   "Insecure tenure has no economic consequences"], ans=0,
   why="EK IMP-5.C.1 places female roles in food production under an enduring understanding about opportunities and challenges varying by location. Tenure is an institution rather than a fact about a person, and it determines both the incentive to improve land and the ability to borrow against it."),

 dict(q="A study finds that plots farmed by women in one district yield less than plots farmed by men in the same district and the same soils. What is the most defensible explanation?", choices=[
   "Differences in access to inputs, credit, advice and secure land rather than any difference in skill or effort",
   "A difference in farming ability between the two groups",
   "A difference in the soils, which the study has already ruled out",
   "A difference in climate between adjacent plots",
   "No explanation is possible from geographic reasoning"], ans=0,
   why="EK IMP-5.C.1 makes the role a matter of the production system a person is working within. Holding soil and district constant leaves the institutional differences -- who can buy fertilizer, who can obtain a loan, who is visited by an extension officer -- as the available explanation."),

 dict(q="How does unequal access to extension services and agricultural advice affect production?", choices=[
   "Farmers who are not reached by advice adopt improved varieties and methods more slowly, so the gap in output reflects the gap in information",
   "Advice has no measurable effect on what farmers produce",
   "Advice affects only farmers who own machinery",
   "Extension services reach every farmer equally in all districts",
   "Advice affects consumption but never production"], ans=0,
   why="EK IMP-5.C.1 says the role of females in food production varies with the type of production involved, and information is one of the inputs a production system distributes. Where advice is delivered to a recorded landholder, whoever is not the recorded landholder receives it late or not at all."),

 dict(q="The framework names DISTRIBUTION as one of the three domains. What kind of role does that refer to?", choices=[
   "Moving, trading and selling food -- in many places market trading of produce is substantially carried out by women",
   "Deciding national agricultural policy",
   "Ploughing and planting fields",
   "Preparing meals within a household",
   "Deciding which crops a country will import"], ans=0,
   why="EK IMP-5.C.1 names food distribution alongside production and consumption. Distribution covers the stages between the field and the household, and the CED's inclusion of it is a reminder that a role can be central in one domain and marginal in another."),

 dict(q="The framework names CONSUMPTION as one of the three domains. What kind of role does that refer to?", choices=[
   "Preparing food and deciding how it is allocated within a household, which shapes who in the household is well fed",
   "Deciding a country's food imports",
   "Harvesting a crop from a field",
   "Setting the price of food in a market",
   "Transporting produce to a market town"], ans=0,
   why="EK IMP-5.C.1 names consumption as the third domain in which female roles vary. Allocation within a household is where a national food supply finally becomes an individual's diet, which is why the domain belongs in a geography of food rather than only in a study of production."),

 dict(q="Why do labour statistics often understate women's participation in agriculture?", choices=[
   "Work that is unpaid, seasonal and performed on the household's own holding is frequently not recorded as employment at all",
   "Because women deliberately conceal their work from enumerators",
   "Because agricultural work cannot be counted by any method",
   "Because statistics count only work performed outside a household's own land, and no such work exists",
   "Because women's agricultural work is always recorded twice"], ans=0,
   why="EK IMP-5.C.1 concerns roles in production, distribution and consumption, and much of that work falls outside the categories a labour survey is built around. A measurement rule that counts paid employment will miss unpaid work on one's own holding however substantial it is."),

 dict(q="In some farming systems a distinction is drawn between crops grown to sell and crops grown to eat. Why does that distinction matter for this topic?", choices=[
   "Where the two are separated, control of the cash from the sold crop and responsibility for the food crop can fall to different members of the household",
   "Because crops grown to eat cannot be sold at any price",
   "Because cash crops require no labour",
   "Because food crops are always grown on better soil",
   "Because the distinction has no bearing on who does what"], ans=0,
   why="EK IMP-5.C.1 says the role varies depending on the type of production involved, and a system separating a cash crop from a food crop is one such type. Responsibility for feeding the household and control of the household's money can then rest with different people, which is a variation in role of exactly the kind the statement describes."),

 dict(q="Why does time spent collecting water and fuel bear on a household's agricultural output?", choices=[
   "Those hours are unavailable for cultivation, processing or paid work, so the burden is a constraint on production as well as on the person carrying it",
   "Water and fuel collection increases the time available for farming",
   "Water and fuel collection is agricultural production in itself",
   "The time involved is too small to have any effect",
   "It affects consumption but has no production consequence"], ans=0,
   why="EK IMP-5.C.1 covers roles in production and consumption together, and a day has a fixed number of hours. Where the same person is responsible for provisioning tasks and for field work, an increase in one is a reduction in the other."),

 dict(q="When men from a rural district migrate to cities for work in large numbers, what typically happens to women's agricultural role there?", choices=[
   "It expands, since women take on tasks and decisions previously carried out by the absent household members, often without a matching change in land rights or access to credit",
   "It disappears, since farming ceases when men leave",
   "It is unchanged in every respect",
   "It becomes purely a consumption role",
   "It transfers automatically to hired labour"], ans=0,
   why="EK IMP-5.C.1 says the role varies with the type of production involved, and a labour-exporting district is a distinct type. The additional responsibility usually arrives before any change in the institutions that record who holds the land."),

 dict(q="At which two scales must the framework's claim about variation be examined?", choices=[
   "Within a household, where tasks are divided between its members, and between regions, where whole systems of production differ",
   "Only at the global scale, since food is traded internationally",
   "Only at the household scale, since food is prepared in households",
   "At no scale, since gendered roles are not spatial",
   "Only at the national scale, since governments collect the statistics"], ans=0,
   why="EK IMP-5.C.1 says the role varies in many PLACES depending on the TYPE OF PRODUCTION, which puts variation at both scales at once. A national average conceals the household division of labour, and a single household cannot show the regional differences the statement asserts."),

 dict(q="Why is data analysis the framework's suggested skill for this topic?", choices=[
   "The claim is about variation, and variation can only be demonstrated by comparing measurements across places rather than by describing one case",
   "Because agricultural data are always complete and accurate",
   "Because the topic has no qualitative dimension of any kind",
   "Because data analysis is the suggested skill for every topic in the course",
   "Because the framework forbids the use of interviews or narratives"], ans=0,
   why="EK IMP-5.C.1 asserts that the role varies in many places, which is a comparative claim. One place, however carefully described, cannot establish variation, and the CED's suggested skill for this topic is comparing patterns and trends in quantitative and geospatial data."),

 dict(q="Which single indicator would best support a claim about women's role in agricultural PRODUCTION in a region?", choices=[
   "The share of agricultural work performed by women, measured in a way that captures unpaid work on a household's own holding",
   "The number of women living in rural areas",
   "The share of the region's food that is imported",
   "The average size of an agricultural holding",
   "The number of agricultural machines in the region"], ans=0,
   why="EK IMP-5.C.1 concerns roles in production, so the indicator has to measure work rather than residence or assets. The qualification matters because a measure restricted to paid employment omits most of the work the statement is about."),

 dict(q="How does the framework's claim in this topic connect to the treatment of women and economic development later in the course?", choices=[
   "Both treat women's economic roles as changing with the system they work within rather than as fixed, so a change in production or in development alters the role",
   "The two topics make contradictory claims",
   "The later topic concerns only urban employment and has no connection",
   "Both assert that women's roles are constant across all societies",
   "There is no connection, since one topic concerns agriculture"], ans=0,
   why="EK IMP-5.C.1 makes the role depend on the type of production, and EK SPS-7.D.1 states that the roles of women change as countries develop economically. Both statements locate the explanation in the surrounding system rather than in any fixed characteristic."),

 dict(q="A large export horticulture operation employs mainly women in its packing and grading houses. What does this illustrate about the framework's claim?", choices=[
   "That a change in the type of production creates a new pattern of paid work, which is a variation in role rather than an absence of one",
   "That women do not work in agriculture in that region",
   "That the operation must be a subsistence system",
   "That packing is not part of the food system",
   "That the framework's claim does not apply to export crops"], ans=0,
   why="EK IMP-5.C.1 says the role varies depending on the type of production involved, and an export horticulture operation is a type with its own labour requirements. Recorded waged employment in packing is a different role from unrecorded field labour on a household holding, not a smaller one."),

 dict(q="What is meant by describing a household member as time-poor, and why does it matter here?", choices=[
   "The person's hours are fully committed across productive and household tasks, so any new opportunity can be taken only by giving something else up",
   "The person has no work to do at any time of year",
   "The person is paid too little for the hours worked",
   "The person works only during the harvest season",
   "The term has no application to agricultural households"], ans=0,
   why="EK IMP-5.C.1 covers roles across production, distribution and consumption, which for one person can add up to a full day before any new activity begins. A programme offering training or a new crop reaches a time-poor household as a cost as well as an opportunity."),

 dict(q="Why does the framework's phrase 'varies in many places' resist a single generalization about women in agriculture?", choices=[
   "Because the systems of production differ, and the role follows the system rather than being carried unchanged from place to place",
   "Because no data on the subject exist anywhere",
   "Because the framework considers the subject unimportant",
   "Because women's roles change too quickly to be described",
   "Because every place has exactly the same system of production"], ans=0,
   why="EK IMP-5.C.1 attaches the variation explicitly to the type of production involved. That is a causal claim as well as a descriptive one: it says where to look for the explanation of a difference, which is in the production system rather than in the people."),

 dict(q="Which policy change would most directly address the constraint the reasoning in this topic identifies?", choices=[
   "Recording women as landholders in their own right, so that tenure, credit and extension services follow the record",
   "Increasing the total area of farmland in the region",
   "Raising the price of the region's main export crop",
   "Building a food-processing plant in the nearest city",
   "Introducing a new variety of the region's main crop"], ans=0,
   why="EK IMP-5.C.1 places female roles in production under an enduring understanding about varying opportunities and challenges. Where tenure records determine who can borrow and who is advised, changing the record changes access to every resource attached to it, which the other options leave untouched."),

 dict(q="Why is the share of agricultural work a person performs a different question from the control that person has over what the work produces?", choices=[
   "Work is a matter of hours in a field while control is a matter of who owns the land, sells the crop and keeps the money, and a production system can separate the two completely",
   "They are two ways of describing the same thing",
   "Control always follows automatically from the share of work performed",
   "Neither can be measured in an agricultural household",
   "Control matters only in subsistence systems and work only in commercial ones"], ans=0,
   why="EK IMP-5.C.1 spans production, distribution and consumption, which is exactly the span across which work and control can come apart. A person may perform most of the labour on a plot recorded in someone else's name and sold by someone else, so a single figure for participation answers only the first of the two questions."),

 dict(q="Which pairing of a situation with the framework's domain it belongs to is CORRECT?", choices=[
   "Selling produce at a weekly market town, matched to distribution",
   "Weeding and harvesting a household's plot, matched to consumption",
   "Deciding how a household's food is shared out, matched to production",
   "Carrying grain to a mill for grinding, matched to production",
   "Preparing the household's evening meal, matched to distribution"], ans=0,
   why="EK IMP-5.C.1 names production, distribution and consumption as three distinct domains. Only one pairing here matches an activity to the domain it belongs to; each of the others moves an activity into one of the statement's other two categories."),

 dict(q="Women's participation in agriculture in four regions is recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Region", "Women as a share of the agricultural labour force (%)", "Women as a share of recorded holding operators (%)"],
     rows=[["Region 1", "24", "9"],
           ["Region 2", "43", "14"],
           ["Region 3", "51", "12"],
           ["Region 4", "62", "11"]]),
   choices=[
   "In every region the share of the labour force is far above the share of recorded operators, and the gap is widest where women's labour share is highest",
   "The two shares are approximately equal in every region",
   "The share of recorded operators exceeds the labour share in every region",
   "Women's labour share falls as the share of recorded operators rises",
   "No pattern can be read, since the regions are not named"], ans=0,
   why="Labour shares run from 24 to 62 percent while recorded operator shares stay between 9 and 14, so the gap widens from 15 points to 51 as the labour share rises. EK IMP-5.C.1 makes the role depend on the type of production, and a large gap between who works the land and who is recorded as operating it is a difference in institutions rather than in effort."),

 dict(q="Landholding and credit in four countries are recorded below. Using the accompanying figures, what relationship do they show?",
   table=dict(headers=["Country", "Women as a share of agricultural landholders (%)", "Share of agricultural credit going to women (%)"],
     rows=[["Country A", "5", "4"],
           ["Country B", "13", "10"],
           ["Country C", "20", "17"],
           ["Country D", "8", "7"]]),
   choices=[
   "The credit share tracks the landholding share closely and sits slightly below it in every country, which is consistent with land being used as security for borrowing",
   "The credit share exceeds the landholding share in every country",
   "The two shares are unrelated across the four countries",
   "The country with the fewest women landholders receives the most credit",
   "Credit shares are identical in all four countries"], ans=0,
   why="Ranking the countries by landholding share gives 5, 8, 13 and 20 percent and ranking them by credit share gives 4, 7, 10 and 17 in the same order, with credit slightly below landholding in every case. EK IMP-5.C.1 makes the role depend on the production system, and a lender requiring security ties one institution directly to the other."),

 dict(q="Daily time use by adults in one farming district is recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Activity", "Hours per day, men", "Hours per day, women"],
     rows=[["Field and paid work", "5.2", "3.9"],
           ["Food processing, water and fuel collection", "1.1", "4.6"]]),
   choices=[
   "Women record 8.5 hours across the two categories against 6.3 for men, and their extra 3.5 hours of processing and collection more than offsets their 1.3 fewer hours of field and paid work",
   "Men record more total hours than women across the two categories",
   "Women record no hours of field or paid work",
   "The two groups record identical totals",
   "Men record more hours of processing and collection than women"], ans=0,
   why="Adding the two rows gives 6.3 hours for men and 8.5 for women, and the 3.5-hour difference in processing and collection is larger than the 1.3-hour difference in field and paid work. EK IMP-5.C.1 covers roles across production and consumption together, which is why a record confined to field work alone would reverse the comparison."),

 dict(q="What limitation should be stated when using a labour-force participation figure to describe women's role in agriculture?", choices=[
   "The figure may exclude unpaid work on a household's own holding, so it can understate the role it is meant to measure",
   "Labour-force figures are always exactly accurate",
   "Percentages cannot be compared between regions at all",
   "A participation figure settles the question of who controls the land",
   "The framework forbids the use of labour statistics in this topic"], ans=0,
   why="EK IMP-5.C.1 concerns roles across production, distribution and consumption, much of which is unpaid and performed on a household's own land. A measure built around paid employment omits that work by construction, which is a defect of the instrument rather than of the people it counts."),

 dict(q="Which sentence states this topic's essential knowledge without adding to it or subtracting from it?", choices=[
   "The role of women in producing, distributing and consuming food differs from place to place, and what it depends on is the type of production involved",
   "Women perform most agricultural labour in every part of the world",
   "Women perform no agricultural labour in any part of the world",
   "Women's role in agriculture depends only on the climate of the region",
   "Women's role in agriculture has been identical throughout history"], ans=0,
   why="EK IMP-5.C.1 asserts variation and names the type of production as what the variation depends on. Both universal claims contradict the statement, and the climate version replaces the CED's own variable with one it does not name."),
]
