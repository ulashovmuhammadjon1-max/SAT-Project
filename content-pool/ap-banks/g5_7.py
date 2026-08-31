# AP HUMAN GEOGRAPHY 5.7 Spatial Organization of Agriculture -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding PSO-5, "Availability
# of resources and cultural practices influence agricultural practices and
# land-use patterns." Learning objective PSO-5.C, "Explain how economic forces
# influence agricultural practices."
#
# Essential knowledge -- the three statements assigned to this topic:
#   PSO-5.C.3  Large-scale commercial agricultural operations are replacing
#              small family farms.
#   PSO-5.C.4  Complex commodity chains link production and consumption of
#              agricultural products.
#   PSO-5.C.5  Technology has increased economies of scale in the agricultural
#              sector and the carrying capacity of the land.
#
# THE THREE STATEMENTS ARE ONE ARGUMENT, and reading them separately is how the
# topic is missed:
#
#   PSO-5.C.5  technology raises economies of scale
#        |      (a bigger operation now costs less per tonne than a small one)
#        v
#   PSO-5.C.3  so large operations replace small family farms
#        |      (not because families farm badly, but because unit cost decides
#        |       who survives a price they cannot set)
#        v
#   PSO-5.C.4  and what results is a long chain between the field and the plate
#
# Items 3, 15, 18 and 30 run that argument; items 4 and 5 supply the two terms
# PSO-5.C.5 names without defining.
#
# THE TWO TERMS THE CED USES AND DOES NOT DEFINE:
#   economies of scale   the fall in cost PER UNIT as output rises, because
#                        large fixed costs -- machinery, storage, a buyer
#                        relationship, compliance -- are spread over more tonnes
#   carrying capacity    the population an area can support given the technology
#                        in use; raising yields raises it, which is why the
#                        figure is not a property of the land alone
# Item 5 keys on the second half of that carrying-capacity definition, because a
# student who treats it as a fixed natural constant will misread both this topic
# and Malthus in Unit 2 (item 22).
#
# A COMMODITY CHAIN, since PSO-5.C.4 names it without listing its links: inputs,
# production, processing, transport, wholesaling, retailing, consumption. The
# geographic content is that these steps happen in DIFFERENT PLACES, often on
# different continents, so the distance between the person who grows food and the
# person who eats it is the thing the term measures. Items 6, 7, 12, 13 and 27
# are built on that, and item 8 on where in the chain the money stays.
#
# WHAT THE CED DOES NOT SAY, and no item here asserts: that small family farms
# have disappeared, that consolidation proceeds at the same rate in every sector,
# or that technology can raise carrying capacity without limit. Items 16, 19 and
# 21 key against each of those overstatements in turn.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.7", "Spatial Organization of Agriculture", 5)

QUESTIONS = [
 dict(q="What does the framework say is happening to small family farms?", choices=[
   "They are being replaced by large-scale commercial agricultural operations",
   "They are replacing large-scale commercial operations",
   "They are growing in number and in average size",
   "They are unchanged in number and in share of output",
   "They are being converted into subsistence holdings"], ans=0,
   why="EK PSO-5.C.3 states that large-scale commercial agricultural operations are replacing small family farms. The direction is one-way in the framework's wording, and the mechanism is the economies of scale named in EK PSO-5.C.5."),

 dict(q="What does the framework say complex commodity chains do?", choices=[
   "They link the production and the consumption of agricultural products",
   "They prevent agricultural products from reaching consumers",
   "They replace the need for farms",
   "They apply only to manufactured goods and not to food",
   "They shorten the distance between grower and eater"], ans=0,
   why="EK PSO-5.C.4 states that complex commodity chains link production and consumption of agricultural products. The word 'complex' is the point: the link runs through many steps in many places rather than directly from a field to a table."),

 dict(q="Why do large-scale commercial operations tend to displace small family farms rather than simply coexisting with them?", choices=[
   "Larger operations produce at a lower cost per tonne, and a farm that cannot set the price it receives must survive on its costs",
   "Small farms are legally prohibited in most countries",
   "Small farms produce lower yields per hectare in every case",
   "Consumers refuse to buy from small farms",
   "Large operations use less land in total"], ans=0,
   why="EK PSO-5.C.5 names increased economies of scale and EK PSO-5.C.3 names the replacement that follows. A commodity producer takes the market price rather than setting it, so the operation with the lower unit cost keeps a margin at a price that leaves the other with none."),

 dict(q="What are economies of scale?", choices=[
   "The fall in cost per unit of output as the scale of production rises, because large fixed costs are spread over more units",
   "The rise in total cost as output rises",
   "The total area of land a farm occupies",
   "The number of different crops a farm grows",
   "The distance between a farm and its market"], ans=0,
   why="EK PSO-5.C.5 says technology has increased economies of scale in the agricultural sector. The measure is cost per unit rather than total cost, which is why a larger operation can spend far more in total and still produce more cheaply per tonne."),

 dict(q="What does the framework mean by saying technology has increased the carrying capacity of the land?", choices=[
   "The number of people a given area can support depends on the technology in use, so better technology raises the figure without the land changing",
   "The physical area of farmland has increased",
   "The land has become permanently more fertile without human action",
   "Carrying capacity is a fixed natural constant that technology cannot affect",
   "Fewer people can now be supported by the same land"], ans=0,
   why="EK PSO-5.C.5 pairs economies of scale with carrying capacity as two things technology has raised. Treating carrying capacity as a property of the land alone is the error the statement rules out, since the same hectare supports very different numbers under different methods."),

 dict(q="What is a commodity chain?", choices=[
   "The sequence of linked steps -- inputs, production, processing, transport, wholesaling, retailing -- that carries a product from field to consumer",
   "A group of farms owned by one family",
   "A chain of shops selling only local produce",
   "The physical fencing that divides a large farm",
   "The rotation of crops on one holding across several years"], ans=0,
   why="EK PSO-5.C.4 says complex commodity chains link production and consumption of agricultural products. What makes the concept geographic is that the steps happen in different places, so the chain is a description of distance as much as of process."),

 dict(q="A chocolate bar's cocoa is grown in one country, fermented and dried near the farm, shipped to a second country for processing, manufactured into bars in a third, and sold in a fourth. Which framework statement does this illustrate?", choices=[
   "That complex commodity chains link the production and consumption of agricultural products",
   "That large-scale operations are replacing small family farms",
   "That technology has raised the carrying capacity of the land",
   "That agricultural production regions are defined by climate",
   "That rural settlement patterns are clustered, dispersed, or linear"], ans=0,
   why="EK PSO-5.C.4 names complex commodity chains as the link between production and consumption. Four countries and five stages between the tree and the shopper is precisely the complexity the word 'complex' is carrying."),

 dict(q="In a long agricultural commodity chain, where does the largest share of the final retail price usually remain?", choices=[
   "In the later stages -- processing, distribution and retailing -- rather than with the farmer who grew the crop",
   "With the farmer, who does the most physical work",
   "Distributed exactly equally among all the stages",
   "With the consumer, who pays the price",
   "With the supplier of seed, who begins the chain"], ans=0,
   why="EK PSO-5.C.4 describes a complex chain linking production and consumption, and each link takes a margin. The growing stage typically has many competing suppliers of an interchangeable raw product, while the later stages are fewer and hold the brand, so bargaining power and value sit downstream."),

 dict(q="A single firm owns the seed supply, the farms, the processing plant and the distribution network for one product. What is this arrangement called, and why is it adopted?", choices=[
   "Vertical integration, adopted so that one firm controls quality, timing and cost across every stage instead of bargaining at each one",
   "Horizontal diffusion, adopted to spread a crop between regions",
   "Subsistence production, adopted to feed the firm's employees",
   "Shifting cultivation, adopted to rest the land",
   "Long lot survey, adopted to divide the firm's land"], ans=0,
   why="EK PSO-5.C.4 describes complex commodity chains linking production and consumption, and integration is one response to that complexity. Owning consecutive links removes the negotiation between them, which is worth most where timing is tight and quality must be guaranteed."),

 dict(q="A farming district's holdings consolidate from four hundred family farms into thirty large operations over three decades. What is the most likely consequence for the district's settlement?", choices=[
   "Fewer households live in the district, so schools, shops and services lose the population that supported them",
   "The district's population rises sharply",
   "The district's farmland is abandoned entirely",
   "The district's output falls in proportion to the number of farms lost",
   "Nothing changes, since the same land is still farmed"], ans=0,
   why="EK PSO-5.C.3 states that large-scale commercial operations are replacing small family farms, and each farm that disappears was also a household. Rural services depend on the number of people rather than on the hectares, so consolidation empties a district even when the land stays in production."),

 dict(q="A grower signs an agreement to plant a specified variety on a specified schedule for a single processor, who supplies the seed and buys the entire crop at an agreed price. What does this arrangement illustrate?", choices=[
   "A commodity chain in which the grower's decisions are set by the next link rather than by the grower",
   "A subsistence system in which output is consumed by the household",
   "A shifting cultivation cycle",
   "A rejection of commercial agriculture",
   "A settlement pattern rather than an economic relationship"], ans=0,
   why="EK PSO-5.C.4 describes complex commodity chains linking production and consumption of agricultural products. When a downstream firm supplies the inputs and buys the whole output, what to plant and when to harvest are decided at that link, so the chain reaches back into the field."),

 dict(q="What is the most important geographic consequence of a long commodity chain for the person eating the food?", choices=[
   "The food may be produced thousands of kilometres away under conditions the consumer cannot see or verify",
   "The food must be produced within the consumer's own district",
   "The food cannot be transported at all",
   "The consumer necessarily knows the farmer personally",
   "The chain has no consequences for consumers"], ans=0,
   why="EK PSO-5.C.4 says complex commodity chains link production and consumption, and the link is what separates as well as connects. Every additional stage puts distance and another firm between the field and the shelf, so what is visible at the point of sale is a package rather than a place."),

 dict(q="Why does a long commodity chain make it harder to trace the source of a contaminated food product?", choices=[
   "Ingredients from many producers are combined at processing stages, so a single package may contain output from hundreds of farms",
   "Because records are never kept at any stage",
   "Because food does not travel between countries",
   "Because contamination can occur only at the farm",
   "Because a long chain has fewer stages than a short one"], ans=0,
   why="EK PSO-5.C.4 names the chains as complex, and blending is one form that complexity takes. Once a processing stage pools output from many suppliers, the finished product no longer corresponds to any one field, which is what makes tracing back through it difficult."),

 dict(q="How can a country's total agricultural output rise while its number of farms falls sharply?", choices=[
   "The remaining farms are larger and more productive, so output per farm rises faster than the number of farms falls",
   "Output cannot rise while the number of farms falls",
   "The farmed area must have doubled",
   "Imports must be counted as domestic output",
   "The output figures must be inaccurate"], ans=0,
   why="EK PSO-5.C.3 describes large operations replacing small family farms and EK PSO-5.C.5 attributes rising economies of scale and carrying capacity to technology. Fewer, larger, higher-yielding units is exactly the combination that produces more from the same ground."),

 dict(q="What does the framework's claim about technology and carrying capacity imply about the limits of a region's population?", choices=[
   "The limit moves as technology changes, so it must be stated together with the methods in use rather than as a fixed number",
   "The limit is fixed permanently by the region's soil and climate",
   "The limit has been abolished and no longer exists",
   "The limit falls whenever technology improves",
   "The limit depends only on the region's total area"], ans=0,
   why="EK PSO-5.C.5 says technology has increased the carrying capacity of the land, which makes the figure a function of method as well as of place. A limit that moves is still a limit, so this is not a claim that population can grow without constraint."),

 dict(q="A student says technology can raise carrying capacity without limit. What does the framework support, and what does it not?", choices=[
   "It supports the claim that technology has raised carrying capacity; it says nothing about that process continuing indefinitely",
   "It supports the claim that carrying capacity can rise without limit",
   "It denies that technology has raised carrying capacity at all",
   "It states that carrying capacity has fallen",
   "It states an exact upper limit for every region"], ans=0,
   why="EK PSO-5.C.5 makes a claim about what HAS happened rather than about what must continue. Reading a past increase as an unlimited future one goes beyond the sentence, which is exactly the move the environmental costs in EK IMP-5.A.1 make questionable."),

 dict(q="At which three scales must the framework's account of agricultural organization be read to see the whole of it?", choices=[
   "The individual farm that consolidates or disappears, the district whose settlement thins, and the global chain along which the product travels",
   "The global scale only, since food is traded internationally",
   "The farm scale only, since farming happens on farms",
   "The national scale only, since governments regulate agriculture",
   "No scale, since economic organization is not spatial"], ans=0,
   why="EK PSO-5.C.3 describes a change in the units of production, EK PSO-5.C.4 a chain that crosses continents, and EK PSO-5.C.5 the technology behind both. The three statements sit at different scales, which is why an account confined to one of them misses most of the topic."),

 dict(q="Why does expensive machinery in particular drive economies of scale in agriculture?", choices=[
   "A machine costs nearly the same whether it works a hundred hectares or a thousand, so its cost per hectare falls as the area worked rises",
   "Machinery costs rise in exact proportion to the area worked",
   "Machinery cannot be used on holdings above a certain size",
   "Machinery raises the cost per tonne of everything it touches",
   "Machinery is supplied free to large operations"], ans=0,
   why="EK PSO-5.C.5 attributes increased economies of scale to technology, and a fixed cost is the mechanism. The purchase price is incurred once, so the arithmetic of spreading it favours whoever has the most hectares to spread it over."),

 dict(q="Why does consolidation proceed further in some agricultural sectors than in others?", choices=[
   "Where the product is uniform, storable and machine-harvested the advantages of scale are largest, while delicate or specialty products keep a place for smaller producers",
   "Because governments choose which sectors may consolidate",
   "Because consolidation happens at exactly the same rate everywhere",
   "Because only livestock operations can be large",
   "Because small producers always outcompete large ones in every sector"], ans=0,
   why="EK PSO-5.C.3 says large operations are replacing small family farms and EK PSO-5.C.5 gives economies of scale as the reason. Where the scale advantage is small -- hand-picked fruit, a product sold on its particular character -- the pressure the statement describes is correspondingly weaker."),

 dict(q="Which strategy would best allow a small farm to survive alongside large-scale operations, on the framework's own logic?", choices=[
   "Competing on something other than cost per tonne, such as a product or a relationship the large operation cannot reproduce",
   "Producing the same commodity at a still lower price than the large operation",
   "Expanding to match the largest operation's area immediately",
   "Withdrawing from all markets and producing only for the household",
   "Waiting for the large operation to close"], ans=0,
   why="EK PSO-5.C.5 attributes the pressure to economies of scale, which is an advantage in cost per unit of an identical product. A small producer cannot win that comparison and can avoid making it, which is why survival runs through differentiation rather than through price."),

 dict(q="How does the framework's claim about carrying capacity bear on Malthus's argument?", choices=[
   "Malthus treated food supply as growing slowly against population, while this statement records technology raising the number a given area can support",
   "The two claims are identical",
   "The framework confirms that carrying capacity cannot be changed",
   "Malthus argued that technology raises carrying capacity without limit",
   "Neither claim concerns population or food"], ans=0,
   why="EK PSO-5.C.5 says technology has increased the carrying capacity of the land, which is the historical answer to the mechanism Malthus proposed. It does not settle the argument, since a capacity that has risen is not thereby shown to be able to rise forever."),

 dict(q="What is agribusiness?", choices=[
   "The whole commercial system around farming -- inputs, finance, processing, distribution and retail -- of which the farm itself is one part",
   "Any farm owned by a single family",
   "The practice of growing food only for the household",
   "A government department that regulates farming",
   "The physical land area occupied by a farm"], ans=0,
   why="EK PSO-5.C.4 describes complex commodity chains linking production and consumption, and the term names the system those chains constitute. Reading agriculture as the farm alone leaves out most of the value and most of the decisions."),

 dict(q="A handful of firms supply most of a country's seed and buy most of its grain, while there are tens of thousands of farms. What follows for the farms?", choices=[
   "They face concentrated buyers and sellers on both sides while competing with one another, so they have little bargaining power over price",
   "They can dictate the price of both their inputs and their output",
   "They are unaffected, since the number of firms does not matter",
   "They will consolidate into a single farm",
   "They benefit because concentration always lowers input prices"], ans=0,
   why="EK PSO-5.C.4 names complex commodity chains linking production and consumption, and bargaining power depends on how many actors occupy each link. Many identical sellers facing few buyers is the structural position that leaves the growing stage with the thinnest margin."),

 dict(q="In a commodity chain in which a processor sets the price and the grower supplies to contract, who bears most of the risk of a bad harvest?", choices=[
   "The grower, whose costs were incurred before the harvest and whose income depends on delivering it",
   "The retailer, who has the most customers",
   "The consumer, who pays the final price",
   "The risk is shared exactly equally along the chain",
   "Nobody, since a bad harvest has no financial consequences"], ans=0,
   why="EK PSO-5.C.4 describes complex commodity chains linking production and consumption. Downstream links can substitute another supplier or another region, while the grower has one crop in one field, which is why weather risk stops where substitution stops."),

 dict(q="Which of these would be the strongest evidence that the process described in EK PSO-5.C.3 is occurring in a country?", choices=[
   "A falling number of farms alongside a rising average farm size, with total farmland roughly unchanged",
   "A rising number of farms alongside a rising average farm size",
   "A rising population in rural districts",
   "An increase in the number of crops grown per farm",
   "A fall in total agricultural output"], ans=0,
   why="EK PSO-5.C.3 states that large-scale operations are replacing small family farms, which is a claim about the same land being held in fewer and larger units. Fewer farms with a stable total area is exactly that, whereas a rising farm count would contradict it."),

 dict(q="A country's farm structure over seventy years is recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Year", "Farms (thousands)", "Average farm size (hectares)", "Total farmland (million hectares)"],
     rows=[["1950", "5,400", "86", "464"],
           ["1980", "2,400", "175", "420"],
           ["2010", "2,200", "180", "396"],
           ["2020", "2,000", "200", "400"]]),
   choices=[
   "The number of farms fell by about 63 percent while average size rose from 86 to 200 hectares and total farmland changed by less than 15 percent",
   "Both the number of farms and the average farm size fell",
   "Total farmland more than doubled, which explains the larger farms",
   "The number of farms rose while average size fell",
   "Average farm size was unchanged across the period"], ans=0,
   why="Farms fall from 5,400 to 2,000 thousand, a decline of about 63 percent, while average size rises from 86 to 200 hectares and total farmland moves only from 464 to 400 million hectares. EK PSO-5.C.3 describes large operations replacing small family farms, and the near-constant total area shows the same ground held in fewer and bigger units."),

 dict(q="The share of a retail food price captured at each stage of one commodity chain is recorded below. Using the accompanying figures, which stage retains the least?",
   table=dict(headers=["Stage", "Share of the final retail price (%)"],
     rows=[["Farm production", "8"],
           ["Processing", "22"],
           ["Transport", "9"],
           ["Wholesaling", "12"],
           ["Retailing", "49"]]),
   choices=[
   "Farm production, which retains 8 percent while retailing retains 49 percent",
   "Retailing, which retains the smallest share",
   "Processing, which retains 22 percent",
   "Transport, which is the shortest stage",
   "All stages retain equal shares"], ans=0,
   why="The five shares sum to 100 and the smallest of them, 8 percent, belongs to the stage that grows the crop, while the largest, 49 percent, belongs to the stage that sells it. EK PSO-5.C.4 describes complex chains linking production and consumption, and each additional link is a place where part of the price stops."),

 dict(q="Production cost by operation size is recorded below. Using the accompanying figures, what do the numbers demonstrate?",
   table=dict(headers=["Operation size (hectares)", "Cost per tonne produced (currency units)"],
     rows=[["20", "265"],
           ["100", "190"],
           ["500", "148"],
           ["2,000", "131"]]),
   choices=[
   "Economies of scale, since cost per tonne falls from 265 to 131 as size rises, though each further increase in size saves less than the one before",
   "Diseconomies of scale, since larger operations cost more per tonne",
   "That cost per tonne is unrelated to operation size",
   "That the largest operation has the highest cost per tonne",
   "That cost per tonne falls by the same amount at every step"], ans=0,
   why="Cost per tonne falls at every step from 265 to 190 to 148 to 131, but the successive savings are 75, 42 and 17, so the advantage of further size is shrinking. EK PSO-5.C.5 says technology has increased economies of scale, and a falling unit cost with diminishing gains is what such an advantage looks like in figures."),

 dict(q="What limitation should be stated when using a table of unit costs by farm size to explain why small farms disappear?", choices=[
   "The record shows a cost disadvantage but not whether it is decisive, since access to credit, land prices and succession also determine which farms continue",
   "Cost per tonne cannot be measured on farms of different sizes",
   "A record showing a pattern always establishes its cause",
   "Currency units cannot be compared across farm sizes",
   "The framework forbids the use of cost data in this topic"], ans=0,
   why="EK PSO-5.C.3 states that large operations are replacing small family farms and EK PSO-5.C.5 supplies economies of scale as a mechanism, but neither says it is the only one. A unit-cost gradient makes the mechanism plausible without ruling out the others that operate alongside it."),

 dict(q="Which sentence connects this topic's three essential knowledge statements into the argument they actually make?", choices=[
   "Technology raised economies of scale, which let large operations displace small family farms, and the food they produce now reaches consumers through long chains of intermediaries",
   "Small family farms are displacing large commercial operations, shortening commodity chains",
   "Technology has lowered the carrying capacity of the land, forcing farms to consolidate",
   "Commodity chains have become simpler as farms have grown larger",
   "The three statements describe unrelated processes with no connection between them"], ans=0,
   why="EK PSO-5.C.5 supplies the technological cause, EK PSO-5.C.3 the change in the units of production, and EK PSO-5.C.4 the chain that links those units to consumers. Each rejected version reverses one of the three directions the statements set."),
]
