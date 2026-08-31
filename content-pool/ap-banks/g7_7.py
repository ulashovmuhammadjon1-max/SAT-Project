# AP HUMAN GEOGRAPHY 7.7 Changes as a Result of the World Economy -- 30 questions
# CED Course Framework V.1, Unit 7. Enduring understanding PSO-7, "Economic and
# social development happen at different times and rates in different places."
# Learning objective PSO-7.A, "Explain causes and geographic consequences of
# recent economic changes such as the increase in international trade,
# deindustrialization, and growing interdependence in the world economy."
# Suggested skill 4.F, "Explain possible limitations of visual sources provided."
#
# Essential knowledge -- THREE statements. The CED splits learning objective
# PSO-7.A across two topics: 7.6 carries PSO-7.A.1 to PSO-7.A.4 and 7.7 carries
# PSO-7.A.5 to PSO-7.A.7. This module keeps strictly to the last three, and
# g7_6.py keeps strictly to the first four, so the two do not overlap:
#   PSO-7.A.5  Outsourcing and economic restructuring have led to a decline in
#              jobs in core regions and an increase in jobs in newly
#              industrialized countries.
#   PSO-7.A.6  In countries outside the core, the growth of industry has
#              resulted in the creation of new manufacturing zones -- including
#              special economic zones, free-trade zones, and export-processing
#              zones -- and the emergence of an international division of labor
#              in which developing countries have lower-paying jobs.
#   PSO-7.A.7  The contemporary economic landscape has been transformed by
#              post-Fordist methods of production, multiplier effects, economies
#              of scale, agglomeration, just-in-time delivery, the emergence of
#              service sectors, high technology industries, and growth poles.
#
# PSO-7.A.7 IS A LIST OF EIGHT THINGS AND THE CED DEFINES NONE OF THEM. Neither
# does it define the three zone types in PSO-7.A.6, nor outsourcing, nor
# economic restructuring. The module supplies the discipline's standard sense
# for each and says so here, the same way g7_2 did for least cost theory and
# g7_5 for Rostow's stages. Each such item's `why` is worded as an explanation
# of a term the CED names, never as a quotation of a sentence it does not carry:
#   outsourcing              contracting work out to another firm, frequently in
#                            another country, rather than doing it in-house
#   economic restructuring   a shift in which sectors an economy's employment
#                            and output sit in, not merely a fall in one of them
#   special economic zone    a designated area inside a country where the rules
#                            on trade, tax and investment differ from those
#                            applying elsewhere in the same country
#   free-trade zone          an area where goods may be landed, held, handled and
#                            re-exported without the customs charges that apply
#                            to goods entering the country proper
#   export-processing zone   a zone whose concessions are conditional on the
#                            output being exported rather than sold at home
#   post-Fordist production  flexible, smaller-batch production able to change
#                            what it makes, against the long standardized runs
#                            of Fordist mass production
#   multiplier effect        the additional employment and income that follow
#                            from an initial job or investment, through the
#                            suppliers it buys from and the wages it pays out
#   agglomeration            the clustering of related firms in one place for the
#                            advantages the cluster itself confers
#   just-in-time delivery    components arriving as they are needed rather than
#                            being held in stock
#   growth pole              a concentration of activity that draws further
#                            activity toward it, so growth spreads outward from it
#
# THE WORD AGGLOMERATION MEANS SOMETHING ELSE IN UNIT 6. g6_2 uses "urban
# agglomeration" for a continuous built-up area and its population. PSO-7.A.7's
# agglomeration is the clustering of RELATED FIRMS, which is a different concept
# wearing the same word. Item 17 states the industrial sense in full and never
# uses the phrase "urban agglomeration", so nothing here can be read against the
# unit 6 definition.
#
# ECONOMIES OF SCALE IS ALREADY DEFINED IN THIS BANK. g5_7 q10 asks "What are
# economies of scale?" outright, under EK PSO-5.C.5, and carries five further
# items on the mechanism. Writing a second definition item here would be the
# tenth cross-topic duplicate of the kind COMP_GOV_DEDUPE.md records. Item 20
# therefore asks what economies of scale do to the MAP of production -- fewer
# and larger plants each serving a wider area -- which is the geographic
# consequence PSO-7.A.7 is listing them for, and which g5_7 does not ask.
#
# SUGGESTED SKILL 4.F IS ABOUT VISUAL SOURCES, and this bank can carry a table
# and nothing else, so items 25 and 26 ask what a photograph CANNOT show rather
# than presenting one. That is the honest form of the skill here: a wage, a
# contract and a position in a chain are not photographable, and a picture of a
# closed plant records an absence without recording what replaced it.
#
# NO REAL COUNTRY, REGION OR FIRM IS NAMED ANYWHERE IN THIS MODULE. The three
# data items carry hypothetical records attached to an unnamed core region, an
# unnamed newly industrialized country and an unnamed plant.
#
# SYNONYM CARE. `geo_check` treats {"special economic zone", "sez"} as one
# construct, so every choice names it in exactly one way, using the CED's words.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("7.7", "Changes as a Result of the World Economy", 7)

QUESTIONS = [
 dict(q="What does the framework say outsourcing and economic restructuring have led to?", choices=[
   "A decline in jobs in core regions and an increase in jobs in newly industrialized countries",
   "A decline in jobs everywhere in the world at the same time",
   "An increase in jobs in core regions and a decline elsewhere",
   "No change in the distribution of jobs between regions",
   "An equal number of jobs in every region of the world"], ans=0,
   why="EK PSO-7.A.5 states that outsourcing and economic restructuring have led to a decline in jobs in core regions and an increase in jobs in newly industrialized countries. Two directions are asserted in one sentence, and reporting either alone turns a redistribution into a disappearance or a windfall."),

 dict(q="What is outsourcing?", choices=[
   "Contracting work out to another firm, frequently in another country, rather than carrying it out within the company itself",
   "Selling a finished product abroad rather than at home",
   "Buying raw materials from a foreign supplier",
   "Moving a company's headquarters to a different city",
   "Employing more workers at an existing plant"], ans=0,
   why="EK PSO-7.A.5 names outsourcing as one of the two processes behind the shift it describes, and the CED does not define it. What moves is the performance of the work rather than the ownership of the product, which is why the practice can shift employment across a border without moving a single sale."),

 dict(q="What does economic restructuring mean, beyond a simple loss of jobs?", choices=[
   "A shift in which sectors an economy's employment and output sit in, so employment can rise overall while manufacturing falls",
   "A fall in the total number of jobs in every sector at once",
   "A change in the ownership of a country's largest companies",
   "A change in the currency a country uses",
   "A change in the physical layout of a factory floor"], ans=0,
   why="EK PSO-7.A.5 names economic restructuring alongside outsourcing, and EK SPS-7.B.1 says the different economic sectors are characterized by distinct development patterns. Restructuring is a change in the composition of employment, which is why a region can lose manufacturing jobs and still add jobs in total."),

 dict(q="Why does one process show as a loss of jobs in one part of the world and a gain in another?", choices=[
   "The work itself is relocated rather than abolished, so the same task appears as a subtraction where it was done and an addition where it is now done",
   "Because the two changes have entirely separate causes that happen to coincide",
   "Because the number of jobs in the world is fixed by international agreement",
   "Because workers physically migrate with the jobs they held",
   "Because job counts in different regions are measured in different units"], ans=0,
   why="EK PSO-7.A.5 puts the decline in core regions and the increase in newly industrialized countries in a single sentence with a single cause. A relocated task is subtracted at one end of the move and added at the other, which is what makes the two halves one phenomenon rather than two."),

 dict(q="What does the framework mean by a newly industrialized country?", choices=[
   "A country whose manufacturing employment and output have grown rapidly and recently, so it now holds work that was previously done in core regions",
   "A country that has never had any manufacturing industry",
   "A country whose industry is the oldest in the world",
   "A country that has recently stopped manufacturing altogether",
   "A country whose economy consists only of services"], ans=0,
   why="EK PSO-7.A.5 says jobs have increased in newly industrialized countries, and EK PSO-7.A.6 says the growth of industry outside the core has created new manufacturing zones there. The category is defined by recent and rapid growth of industry rather than by any absolute level of output."),

 dict(q="A firm closes an assembly plant in a core region and contracts the same assembly work to an independent supplier abroad. Which framework claim does this most directly illustrate?", choices=[
   "That outsourcing and economic restructuring have produced a decline in jobs in core regions and an increase in newly industrialized countries",
   "That neoliberal policies created new organizations that foster greater globalization",
   "That complementarity and comparative advantage establish the basis for trade",
   "That sustainable development policies address natural-resource depletion",
   "That government initiatives at all scales may affect economic development"], ans=0,
   why="EK PSO-7.A.5 names outsourcing specifically, and contracting work to an independent supplier abroad is what the word describes. The rejected claims are real statements of this unit, and each concerns a different process, which is what makes matching a case to the right statement a genuine test."),

 dict(q="What does the framework say the growth of industry has created in countries outside the core?", choices=[
   "New manufacturing zones and an international division of labor",
   "A single world factory serving every market",
   "The disappearance of all agricultural employment",
   "Identical wage levels in every country",
   "The end of trade between countries outside the core"], ans=0,
   why="EK PSO-7.A.6 states that in countries outside the core the growth of industry has resulted in the creation of new manufacturing zones and the emergence of an international division of labor. Both a place and an arrangement are asserted, and the arrangement is the more consequential of the two."),

 dict(q="Which three kinds of manufacturing zone does the framework name?", choices=[
   "Special economic zones, free-trade zones, and export-processing zones",
   "Greenbelts, enterprise districts, and industrial parks",
   "Core zones, semiperipheral zones, and peripheral zones",
   "Primary zones, secondary zones, and tertiary zones",
   "Growth poles, agglomerations, and multiplier zones"], ans=0,
   why="EK PSO-7.A.6 names exactly these three as the new manufacturing zones created by the growth of industry outside the core. The rejected sets mix terms from other statements of this unit and from urban planning, none of which the statement lists here."),

 dict(q="What is a special economic zone?", choices=[
   "A designated area inside a country where the rules on trade, tax and investment differ from those applying in the rest of that country",
   "An area from which all industry is excluded by law",
   "A region that has been granted independence from its state",
   "An international body that regulates trade among its members",
   "A zone in which only agricultural production is permitted"], ans=0,
   why="EK PSO-7.A.6 names it among the new manufacturing zones and the CED does not define it. The defining feature is that the rules change at a boundary drawn inside one country, which is what makes such a zone a geographic object rather than a policy applying everywhere."),

 dict(q="What is a free-trade zone?", choices=[
   "An area where goods may be landed, held, handled and sent onward without the customs charges applied to goods entering the country proper",
   "An agreement between two countries to remove tariffs on each other's goods",
   "A country that levies no taxes of any kind",
   "A port that is open to ships of every nation",
   "An area in which no goods may be manufactured"], ans=0,
   why="EK PSO-7.A.6 names free-trade zones among the manufacturing zones created outside the core, and the CED does not define them. The concession is territorial and attaches to goods that pass through rather than enter, which is what distinguishes such a zone from a free trade agreement between states."),

 dict(q="What distinguishes an export-processing zone from the other manufacturing zones the framework names?", choices=[
   "Its concessions are conditional on the output being sent abroad rather than sold in the domestic market",
   "It is the only zone in which any manufacturing is allowed",
   "It applies to a whole country rather than to an area within one",
   "It offers no advantage to firms that locate inside it",
   "It permits only the import of finished goods"], ans=0,
   why="EK PSO-7.A.6 names export-processing zones alongside the other two, and the CED does not define them. The condition attached to the concession is what the name records, and it is why such a zone can raise a country's exports without changing what is available to its own buyers."),

 dict(q="What is the international division of labor, and what does the framework say about the jobs developing countries hold within it?", choices=[
   "Different stages of producing one good are carried out in different countries, and the framework says developing countries have the lower-paying jobs",
   "Every country produces every good for itself, and wages are equal everywhere",
   "Countries take turns producing goods, and wages rotate with them",
   "One country produces all goods, and the others produce none",
   "Stages of production are divided among regions of a single country"], ans=0,
   why="EK PSO-7.A.6 names the emergence of an international division of labor IN WHICH DEVELOPING COUNTRIES HAVE LOWER-PAYING JOBS. The arrangement and the wage claim sit in one clause, so an account that describes the division without the pay difference has dropped what the framework actually asserts about it."),

 dict(q="Why do the manufacturing zones the framework names concentrate production so sharply in particular places?", choices=[
   "The concessions apply only inside a drawn boundary, so a firm gains them by locating there and loses them by locating anywhere else in the same country",
   "Because the land inside such zones is physically more suitable for factories",
   "Because firms are legally forbidden to manufacture outside them",
   "Because workers are only permitted to live inside such zones",
   "Because transport is impossible outside such zones"], ans=0,
   why="EK PSO-7.A.6 says the growth of industry outside the core has created new manufacturing zones, and a zone is defined by its boundary. A rule that changes at a line makes location itself valuable, which is why such a policy produces a cluster rather than a general increase spread across the country."),

 dict(q="Which set does the framework name as having transformed the contemporary economic landscape?", choices=[
   "Post-Fordist methods of production, multiplier effects, economies of scale, agglomeration, just-in-time delivery, the emergence of service sectors, high technology industries, and growth poles",
   "Complementarity, comparative advantage, neoliberal policies, and tariffs",
   "Rostow's stages, dependency theory, commodity dependence, and the world economy",
   "Ecotourism, sustainable development policies, and the Sustainable Development Goals",
   "Primary, secondary, tertiary, quaternary, and quinary employment"], ans=0,
   why="EK PSO-7.A.7 names exactly these eight as what has transformed the contemporary economic landscape. Each rejected list is a real statement of this unit, drawn from the topics on trade, on theories of development, on sustainability and on economic sectors respectively."),

 dict(q="What distinguishes post-Fordist methods of production from the Fordist mass production they followed?", choices=[
   "Production is flexible and works in smaller batches that can be changed, rather than committing a plant to long standardized runs of one item",
   "Production is carried out entirely by hand rather than by machine",
   "Production takes place only in core regions rather than anywhere else",
   "Production is organized so that each plant makes every part of a product",
   "Production stops entirely between orders"], ans=0,
   why="EK PSO-7.A.7 names post-Fordist methods of production first among the eight things transforming the economic landscape, and the CED does not define them. Flexibility is the defining property, and it is what allows a firm to distribute stages of one product across several places instead of concentrating a long run in one."),

 dict(q="What is a multiplier effect?", choices=[
   "The further employment and income that follow from an initial job or investment, through the suppliers it buys from and the wages its workers spend",
   "The rate at which a factory's output grows from one year to the next",
   "The number of products a single machine can make in an hour",
   "The proportion of a firm's revenue that is paid in tax",
   "The increase in a product's price as it passes through each stage of a supply chain"], ans=0,
   why="EK PSO-7.A.7 names multiplier effects among the eight, and the CED does not define them. The effect works through two channels -- purchases from suppliers and wages spent locally -- which is why the employment associated with a plant is always larger than the plant's own payroll."),

 dict(q="What does agglomeration mean in the framework's list of what transformed the economic landscape?", choices=[
   "The clustering of related firms in one place for the advantages the cluster itself confers, such as shared suppliers, a common pool of skilled labour and the rapid movement of ideas between them",
   "The merging of two companies into a single company",
   "The accumulation of unsold goods in a warehouse",
   "The combining of several products into a single package for sale",
   "The gathering of a firm's shareholders to vote on its direction"], ans=0,
   why="EK PSO-7.A.7 names agglomeration among the eight, and EK SPS-7.B.2 names the factors influencing where manufacturing locates. The advantage is external to any one firm and belongs to the cluster, which is why the process is self-reinforcing: each arrival makes the place more attractive to the next."),

 dict(q="What is just-in-time delivery?", choices=[
   "Components arrive as they are needed for production rather than being held in stock against future need",
   "Finished goods are delivered to customers on a guaranteed date",
   "Workers are hired only for the hours in which they are needed",
   "Factories operate continuously through the night as well as the day",
   "Orders are placed only after a product has already been sold"], ans=0,
   why="EK PSO-7.A.7 names just-in-time delivery among the eight, and the CED does not define it. The practice replaces a stock of components with a flow of them, which removes the cost of holding inventory and puts the reliability of transport in its place."),

 dict(q="What is a growth pole?", choices=[
   "A concentration of activity that draws further activity toward it, so growth spreads outward from that point rather than appearing evenly",
   "The point in a country with the largest population",
   "The northernmost industrial region of a country",
   "A government target for the rate of national economic growth",
   "The moment at which an economy grows fastest"], ans=0,
   why="EK PSO-7.A.7 names growth poles among the eight and the CED does not define them. The concept is spatial: growth is treated as something that begins somewhere and propagates, which is why a state that wants development in a lagging region may try to establish one there."),

 dict(q="What do economies of scale do to the MAP of production?", choices=[
   "They favour fewer and larger plants, each serving a wider area, so production concentrates in fewer places and travels further to reach its market",
   "They favour many small plants, each serving the area immediately around it",
   "They have no effect on where production is located",
   "They require every plant to be the same size as every other",
   "They prevent goods from being transported between regions"], ans=0,
   why="EK PSO-7.A.7 names economies of scale among the things that transformed the contemporary economic landscape, which is a claim about the landscape rather than about accounting. If unit cost falls as a plant gets larger, the cheapest arrangement concentrates output and accepts a longer haul to the customer."),

 dict(q="What does just-in-time delivery require of the geography around a plant?", choices=[
   "Suppliers close enough and transport reliable enough that a delay of hours cannot stop the line, since there is no stock of components to fall back on",
   "Suppliers as far away as possible, so that deliveries are spread out",
   "A warehouse large enough to hold several months of components",
   "That every component be made inside the plant itself",
   "That the plant be located away from any transport route"], ans=0,
   why="EK PSO-7.A.7 names just-in-time delivery among the eight things transforming the economic landscape, and its spatial consequence is the reason it belongs on that list. Removing the stock removes the cushion, so the plant's tolerance for a transport failure falls to nearly nothing and proximity becomes worth paying for."),

 dict(q="Why does the closure of one large plant cost a region more jobs than the plant itself employed?", choices=[
   "The plant's purchases supported employment at its suppliers and its wages supported employment in local services, and both fall away when it closes",
   "Because the regional job count is measured incorrectly after a closure",
   "Because other employers are legally required to close at the same time",
   "Because workers who lose a job are counted twice in the statistics",
   "Because the region's population is fixed and cannot change"], ans=0,
   why="EK PSO-7.A.7 names multiplier effects among the eight things that transformed the economic landscape, and a multiplier runs in both directions. The two channels that add employment when a plant opens are the same two that subtract it when the plant closes."),

 dict(q="What does the framework's mention of the emergence of service sectors and high technology industries record about the contemporary economic landscape?", choices=[
   "That the work which grew as manufacturing employment fell was of a different kind, so the landscape was transformed rather than simply emptied",
   "That manufacturing has ceased to exist anywhere in the world",
   "That services and high technology industries employ nobody",
   "That every worker who left manufacturing entered a high technology industry",
   "That services and high technology industries are found only outside the core"], ans=0,
   why="EK PSO-7.A.7 names the emergence of service sectors and high technology industries among the eight, and EK PSO-7.A.5 records the decline of jobs in core regions. Read together they describe a change of composition, which is exactly the economic restructuring the earlier statement names."),

 dict(q="How do post-Fordist methods of production support the international division of labor the framework describes?", choices=[
   "Flexible production in smaller batches allows the stages of one product to be separated and placed wherever each stage is cheapest, instead of holding them together in one long run",
   "Flexible production requires every stage to be carried out in one building",
   "Flexible production removes the need for any transport between stages",
   "Flexible production makes wage differences between countries irrelevant",
   "Flexible production applies only to agricultural goods"], ans=0,
   why="EK PSO-7.A.7 names post-Fordist methods of production and EK PSO-7.A.6 names the emergence of an international division of labor. A production method that can be broken into changeable segments is what makes the geographic separation of those segments practical, so the two statements describe one change from two sides."),

 dict(q="A geographer has only a photograph of a large modern factory inside a manufacturing zone. What limitation should be stated in using it as evidence about the international division of labor?", choices=[
   "A single view records the building and the equipment, and not the wages paid, the terms of employment, or where this stage sits in a chain running through other countries",
   "A photograph cannot show what a building looks like",
   "A photograph is unusable because factories all look alike",
   "A photograph proves that wages inside are high",
   "A photograph settles the question of who owns the plant"], ans=0,
   why="Suggested skill 4.F for this topic asks students to explain possible limitations of visual sources provided. EK PSO-7.A.6 makes a claim about pay and about position in a division of labour, and neither of those is a visible property of a building, so the source cannot reach the claim."),

 dict(q="A set of photographs of closed and derelict plants is offered as evidence that a core region has deindustrialized. What limitation should be stated?", choices=[
   "Images of what has closed record an absence and not what replaced it, so they can support the decline in manufacturing without showing the restructuring that accompanied it",
   "Photographs of buildings cannot be dated at all",
   "Photographs cannot show that a building is derelict",
   "The images prove that total employment in the region has fallen",
   "Visual sources may never be used as evidence about a region"], ans=0,
   why="Suggested skill 4.F asks for the possible limitations of visual sources, and EK PSO-7.A.5 names outsourcing AND economic restructuring together. A photographic record is selected from what is visible, and the offices and service employment that grew are neither ruined nor photogenic, so the set can be accurate and still one-sided."),

 dict(q="Employment in two places is set out in the hypothetical record below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Place", "Manufacturing jobs at the start (thousands)", "Manufacturing jobs at the end (thousands)", "Service jobs at the start (thousands)", "Service jobs at the end (thousands)"],
     rows=[["An unnamed core region", "820", "540", "1,900", "2,480"],
           ["An unnamed newly industrialized country", "310", "760", "640", "910"]]),
   choices=[
   "Manufacturing employment fell by 280 thousand in the core region and rose by 450 thousand in the newly industrialized country, while service employment rose in both, so the core region's total employment grew even as its manufacturing shrank",
   "Manufacturing employment fell in the core region and in the newly industrialized country alike",
   "The core region lost employment in total, because its manufacturing jobs fell",
   "Service employment fell in the core region as its manufacturing employment did",
   "The newly industrialized country gained exactly as many manufacturing jobs as the core region lost"], ans=0,
   why="Recomputed from the record: manufacturing falls from 820 to 540 thousand in one place and rises from 310 to 760 thousand in the other, while services rise in both, so the core region's total moves from 2,720 to 3,020 thousand. EK PSO-7.A.5 names a decline in core regions and an increase in newly industrialized countries, and EK PSO-7.A.7 names the emergence of service sectors, which is why the total can rise while manufacturing falls."),

 dict(q="The stages of producing one good are set out in the hypothetical table below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Stage of production", "Where the stage is carried out", "Share of the product's final price captured at this stage (%)", "Average hourly pay at this stage (currency units)"],
     rows=[["Design and engineering", "A core region", "31", "46"],
           ["Component manufacture", "A semiperipheral country", "22", "11"],
           ["Final assembly", "A newly industrialized country", "9", "4"],
           ["Marketing and retail", "A core region", "38", "28"]]),
   choices=[
   "The two stages carried out in the core capture 69 percent of the final price between them, while final assembly captures 9 percent and pays the lowest hourly wage in the chain",
   "Final assembly captures the largest share of the product's final price",
   "The stage paying the highest hourly wage captures the smallest share of the final price",
   "Each of the four stages captures about a quarter of the final price",
   "The stages carried out outside the core capture more of the final price than those inside it"], ans=0,
   why="Recomputed from the record: the four shares add to 100, the two core stages hold 31 and 38 of them, and final assembly holds the smallest share at the lowest hourly pay. EK PSO-7.A.6 names an international division of labor IN WHICH DEVELOPING COUNTRIES HAVE LOWER-PAYING JOBS, and a chain whose value and whose pay are concentrated at the same end is what that clause describes."),

 dict(q="A plant closure and its effects are recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Measure", "Value"],
     rows=[["Jobs directly employed at the plant", "1,200"],
           ["Jobs at suppliers serving the plant", "900"],
           ["Jobs in local services supported by the wages of the first two groups", "1,500"],
           ["Jobs in the region before the plant closed", "48,000"],
           ["Jobs in the region two years after it closed", "44,100"]]),
   choices=[
   "The plant's 1,200 direct jobs stand behind 3,600 in total once suppliers and local services are counted, and the region records 3,900 fewer jobs two years later, which is a multiplier effect running in reverse",
   "The closure cost the region exactly the 1,200 jobs the plant itself held",
   "Jobs at suppliers outnumber the jobs in local services that the wages supported",
   "The region held more jobs two years after the closure than before it",
   "The effect reaches the plant's suppliers but not the local services around it"], ans=0,
   why="Recomputed from the record: 1,200 direct jobs, 900 at suppliers and 1,500 in local services total 3,600, and the region's employment falls from 48,000 to 44,100, a loss of 3,900. EK PSO-7.A.7 names multiplier effects among the things that transformed the contemporary economic landscape, and the same two channels that add employment subtract it when the plant goes."),

 dict(q="A student must state what this topic's three essential knowledge statements establish together. Which account is accurate?", choices=[
   "Outsourcing and restructuring moved jobs from core regions to newly industrialized countries, industry outside the core created new manufacturing zones and an international division of labor in which developing countries hold the lower-paying jobs, and eight named processes transformed the economic landscape as a whole",
   "Jobs disappeared from the world economy and were not created anywhere else",
   "Industry outside the core created manufacturing zones in which wages are equal to those in the core",
   "The contemporary economic landscape was transformed by a single process acting alone",
   "Manufacturing employment rose in core regions while falling in newly industrialized countries"], ans=0,
   why="EK PSO-7.A.5 supplies the two directions of the job shift, EK PSO-7.A.6 the zones and the division of labour with its wage clause, and EK PSO-7.A.7 the eight processes. Each rejected summary either turns a redistribution into a disappearance, drops the clause about lower-paying jobs, reduces a list of eight to one, or reverses the direction of the shift."),
]
