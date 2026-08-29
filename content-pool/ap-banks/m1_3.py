# MACRO 1.3 Comparative Advantage and Gains from Trade — 50 questions
#
# TABLE 1 (OUTPUT method) verified. Output per day from one identical bundle of resources:
#   Country : Cloth (bolts) : Wine (barrels)
#   Alpha   : 60 : 30
#   Beta    : 40 : 40
#
#   Absolute advantage: Alpha in cloth (60 > 40); Beta in wine (40 > 30).
#
#   Opportunity cost, OUTPUT method  ->  divide the OTHER good's output by the good's own output
#   ("other over own"):
#     Alpha, 1 bolt of cloth  = 30 wine / 60 cloth = 0.5 barrels of wine
#     Alpha, 1 barrel of wine = 60 cloth / 30 wine = 2 bolts of cloth
#     Beta,  1 bolt of cloth  = 40 wine / 40 cloth = 1 barrel of wine
#     Beta,  1 barrel of wine = 40 cloth / 40 wine = 1 bolt of cloth
#
#   Comparative advantage: Alpha in cloth (0.5 < 1 barrel); Beta in wine (1 < 2 bolts).
#   So Alpha specializes in cloth, Beta in wine.
#
#   Mutually beneficial terms of trade:
#     price of 1 bolt of cloth must lie strictly between 0.5 and 1 barrel of wine;
#     price of 1 barrel of wine must lie strictly between 1 and 2 bolts of cloth.
#     Example: 0.75 barrels per bolt (equivalently 4 bolts for 3 barrels) benefits both.
#
#   Joint-output check: without trade, if each splits resources evenly it gets half of each
#   maximum: Alpha 30 cloth + 15 wine, Beta 20 cloth + 20 wine  => total 50 cloth, 35 wine.
#   With full specialization: Alpha 60 cloth, Beta 40 wine => total 60 cloth, 40 wine.
#   Specialization gains 10 cloth and 5 wine, so trade can leave both better off.
#
# TABLE 2 (INPUT method) verified. Hours of labor needed to produce ONE unit:
#   Country : Rice (hours per ton) : Tea (hours per ton)
#   Xanda   :  4 :  2
#   Yorra   : 10 :  4
#
#   Absolute advantage: Xanda in BOTH goods (fewer hours for each). Xanda still gains from trade.
#
#   Opportunity cost, INPUT method  ->  divide the good's OWN input by the OTHER good's input
#   ("own over other"), the reverse of the output method:
#     Xanda, 1 ton of rice =  4 / 2 = 2.0 tons of tea
#     Xanda, 1 ton of tea  =  2 / 4 = 0.5 tons of rice
#     Yorra, 1 ton of rice = 10 / 4 = 2.5 tons of tea
#     Yorra, 1 ton of tea  =  4 / 10 = 0.4 tons of rice
#
#   Comparative advantage: Xanda in rice (2.0 < 2.5 tons of tea);
#                          Yorra in tea  (0.4 < 0.5 tons of rice).
#   Terms of trade for 1 ton of rice must lie strictly between 2 and 2.5 tons of tea.

TOPIC = ("1.3", "Comparative Advantage and Gains from Trade", 1)

OUT = dict(
    headers=["Country", "Cloth (bolts per day)", "Wine (barrels per day)"],
    rows=[["Alpha", "60", "30"], ["Beta", "40", "40"]],
)

INP = dict(
    headers=["Country", "Hours per ton of rice", "Hours per ton of tea"],
    rows=[["Xanda", "4", "2"], ["Yorra", "10", "4"]],
)

QUESTIONS = [
 dict(q="A country has an absolute advantage in producing a good when it can", choices=[
   "produce the good at a lower opportunity cost than another country",
   "produce more of the good than another country using the same quantity of resources",
   "sell the good at a higher price",
   "produce every good more cheaply in money terms",
   "export the good without a tariff"], ans=1,
   why="Absolute advantage compares physical productivity, not opportunity cost."),
 dict(q="A country has a comparative advantage in producing a good when it can", choices=[
   "produce more of the good than any other country",
   "produce the good at a lower opportunity cost than another country",
   "produce the good using the fewest workers",
   "produce every good more efficiently",
   "produce the good without any imported inputs"], ans=1,
   why="Comparative advantage is about what must be given up, which is why it drives specialization."),
 dict(q="The gains from trade arise fundamentally from differences between countries in", choices=[
   "population size",
   "opportunity costs",
   "money prices",
   "tariff rates",
   "exchange rates"], ans=1,
   why="If two countries had identical opportunity costs there would be no basis for mutually beneficial trade."),
 dict(q="A country that has an absolute advantage in producing both goods", choices=[
   "should produce both goods itself and not trade",
   "can still gain from trade by specializing where its comparative advantage lies",
   "has a comparative advantage in both goods",
   "will always lose from trade",
   "cannot have a comparative advantage in anything"], ans=1,
   why="Comparative advantage cannot be held in both goods, so specialization still pays."),
 dict(q="It is impossible for one country to have a comparative advantage in both of two goods because", choices=[
   "resources are unlimited",
   "if its opportunity cost of one good is lower, its opportunity cost of the other must be higher",
   "trade is always balanced",
   "absolute advantage prevents it",
   "prices adjust to prevent it"], ans=1,
   why="The two opportunity costs are reciprocals, so being low in one forces being high in the other."),
 dict(q="Using the output table, which country has an absolute advantage in cloth?", table=OUT, choices=[
   "Alpha, because it produces 60 bolts to Beta's 40",
   "Beta, because it produces more wine",
   "Neither country",
   "Both countries equally",
   "It cannot be determined from output data"], ans=0,
   why="Absolute advantage in cloth goes to whichever country produces more cloth from the same resources."),
 dict(q="Using the output table, which country has an absolute advantage in wine?", table=OUT, choices=[
   "Alpha",
   "Beta, because it produces 40 barrels to Alpha's 30",
   "Neither",
   "Both equally",
   "Alpha, because it produces more cloth"], ans=1,
   why="Beta gets more barrels from the same resources, so it is absolutely more productive in wine."),
 dict(q="Using the output table, Alpha's opportunity cost of producing one bolt of cloth is", table=OUT, choices=[
   "0.5 barrels of wine", "1 barrel of wine", "2 barrels of wine", "30 barrels of wine", "60 barrels of wine"], ans=0,
   why="With the output method you divide the other good by the good itself: 30 wine over 60 cloth is 0.5."),
 dict(q="Using the output table, Alpha's opportunity cost of producing one barrel of wine is", table=OUT, choices=[
   "0.5 bolts of cloth", "1 bolt of cloth", "2 bolts of cloth", "30 bolts of cloth", "60 bolts of cloth"], ans=2,
   why="Sixty bolts divided by 30 barrels is 2 bolts sacrificed per barrel, the reciprocal of 0.5."),
 dict(q="Using the output table, Beta's opportunity cost of producing one bolt of cloth is", table=OUT, choices=[
   "0.25 barrels of wine", "0.5 barrels of wine", "1 barrel of wine", "2 barrels of wine", "40 barrels of wine"], ans=2,
   why="Beta produces 40 of each from the same resources, so one bolt costs exactly one barrel."),
 dict(q="Using the output table, which country has the comparative advantage in cloth?", table=OUT, choices=[
   "Alpha, whose cost of a bolt is 0.5 barrels against Beta's 1 barrel",
   "Beta, whose cost of a bolt is lower",
   "Neither, since the costs are equal",
   "Both, since each is more productive in something",
   "It depends on the terms of trade"], ans=0,
   why="Alpha gives up less wine per bolt, so it is the low-cost cloth producer."),
 dict(q="Using the output table, which country has the comparative advantage in wine?", table=OUT, choices=[
   "Alpha, at 2 bolts per barrel",
   "Beta, at 1 bolt per barrel against Alpha's 2 bolts",
   "Neither",
   "Both",
   "Alpha, because it has fewer barrels"], ans=1,
   why="Beta sacrifices only one bolt per barrel while Alpha sacrifices two."),
 dict(q="Using the output table, if the two countries specialize according to comparative advantage, then", table=OUT, choices=[
   "Alpha produces wine and Beta produces cloth",
   "Alpha produces cloth and Beta produces wine",
   "both produce cloth",
   "both produce wine",
   "neither specializes"], ans=1,
   why="Each country concentrates on the good it can produce at the lower opportunity cost."),
 dict(q="Using the output table, a mutually beneficial price for one bolt of cloth would be", table=OUT, choices=[
   "0.25 barrels of wine", "0.4 barrels of wine", "0.75 barrels of wine", "1.5 barrels of wine", "2 barrels of wine"], ans=2,
   why="The price must lie between Alpha's cost of 0.5 barrels and Beta's cost of 1 barrel, and 0.75 does."),
 dict(q="Using the output table, a mutually beneficial price for one barrel of wine would be", table=OUT, choices=[
   "0.5 bolts of cloth", "0.75 bolts of cloth", "1.5 bolts of cloth", "2.5 bolts of cloth", "3 bolts of cloth"], ans=2,
   why="The wine price must lie between Beta's cost of 1 bolt and Alpha's cost of 2 bolts."),
 dict(q="Using the output table, which proposed trade would Alpha refuse?", table=OUT, choices=[
   "trading 1 bolt of cloth for 0.9 barrels of wine",
   "trading 1 bolt of cloth for 0.4 barrels of wine",
   "trading 1 bolt of cloth for 0.6 barrels of wine",
   "trading 1 bolt of cloth for 0.75 barrels of wine",
   "trading 1 bolt of cloth for 0.8 barrels of wine"], ans=1,
   why="Alpha can turn a bolt into 0.5 barrels at home, so anything below 0.5 is worse than not trading."),
 dict(q="Using the output table, which proposed trade would Beta refuse?", table=OUT, choices=[
   "trading 1 barrel of wine for 1.2 bolts of cloth",
   "trading 1 barrel of wine for 0.8 bolts of cloth",
   "trading 1 barrel of wine for 1.5 bolts of cloth",
   "trading 1 barrel of wine for 1.8 bolts of cloth",
   "trading 1 barrel of wine for 1.1 bolts of cloth"], ans=1,
   why="Beta can convert a barrel into one bolt itself, so receiving less than one bolt makes it worse off."),
 dict(q="Using the output table, if each country splits its resources evenly between the two goods, total output is 50 bolts and 35 barrels. Under full specialization, total output is", table=OUT, choices=[
   "50 bolts and 35 barrels",
   "60 bolts and 40 barrels",
   "40 bolts and 30 barrels",
   "100 bolts and 70 barrels",
   "60 bolts and 30 barrels"], ans=1,
   why="Alpha making only cloth yields 60 bolts and Beta making only wine yields 40 barrels."),
 dict(q="Using the output table, the increase in combined output made possible by specialization is", table=OUT, choices=[
   "10 bolts of cloth and 5 barrels of wine",
   "5 bolts of cloth and 10 barrels of wine",
   "20 bolts of cloth and 10 barrels of wine",
   "no gain at all",
   "60 bolts of cloth and 40 barrels of wine"], ans=0,
   why="Output rises from 50 bolts and 35 barrels to 60 bolts and 40 barrels."),
 dict(q="Using the input table, which country has an absolute advantage in producing rice?", table=INP, choices=[
   "Xanda, because it needs only 4 hours per ton rather than 10",
   "Yorra, because it needs more hours",
   "Neither, since hours are not output",
   "Both equally",
   "It cannot be determined from input data"], ans=0,
   why="With input data, fewer hours per unit means greater productivity, so the lower number wins."),
 dict(q="Using the input table, which country has an absolute advantage in producing tea?", table=INP, choices=[
   "Yorra, at 4 hours per ton",
   "Xanda, at 2 hours per ton against Yorra's 4",
   "Neither",
   "Both equally",
   "Xanda, because it grows more rice"], ans=1,
   why="Xanda needs half as many hours per ton of tea, so it is absolutely more productive."),
 dict(q="Using the input table, Xanda's opportunity cost of one ton of rice is", table=INP, choices=[
   "0.4 tons of tea", "0.5 tons of tea", "2 tons of tea", "2.5 tons of tea", "4 tons of tea"], ans=2,
   why="With input data you divide the good's own hours by the other good's hours: 4 over 2 equals 2."),
 dict(q="Using the input table, Xanda's opportunity cost of one ton of tea is", table=INP, choices=[
   "0.4 tons of rice", "0.5 tons of rice", "2 tons of rice", "2.5 tons of rice", "4 tons of rice"], ans=1,
   why="Two hours for tea divided by four hours for rice gives half a ton of rice given up."),
 dict(q="Using the input table, Yorra's opportunity cost of one ton of rice is", table=INP, choices=[
   "0.4 tons of tea", "0.5 tons of tea", "2 tons of tea", "2.5 tons of tea", "10 tons of tea"], ans=3,
   why="Ten hours for rice divided by four hours for tea gives 2.5 tons of tea sacrificed."),
 dict(q="Using the input table, Yorra's opportunity cost of one ton of tea is", table=INP, choices=[
   "0.4 tons of rice", "0.5 tons of rice", "1 ton of rice", "2.5 tons of rice", "4 tons of rice"], ans=0,
   why="Four hours for tea divided by ten hours for rice gives 0.4 tons of rice given up."),
 dict(q="Using the input table, which country has the comparative advantage in rice?", table=INP, choices=[
   "Xanda, at 2 tons of tea per ton of rice against Yorra's 2.5",
   "Yorra, at 2.5 tons of tea per ton of rice",
   "Neither, since Xanda is better at both",
   "Both, since costs are equal",
   "Yorra, because it is less productive overall"], ans=0,
   why="Xanda gives up less tea per ton of rice, so rice is where it should specialize."),
 dict(q="Using the input table, which country has the comparative advantage in tea?", table=INP, choices=[
   "Xanda, since it needs fewer hours per ton of tea",
   "Yorra, since it gives up only 0.4 tons of rice per ton of tea against Xanda's 0.5",
   "Neither",
   "Both",
   "Xanda, since it is absolutely more productive"], ans=1,
   why="Absolute productivity is irrelevant here; Yorra sacrifices less rice per ton of tea."),
 dict(q="Using the input table, a mutually beneficial rate for one ton of rice would be", table=INP, choices=[
   "1.5 tons of tea", "1.9 tons of tea", "2.2 tons of tea", "2.6 tons of tea", "3 tons of tea"], ans=2,
   why="The rate must lie between Xanda's cost of 2 tons and Yorra's cost of 2.5 tons of tea."),
 dict(q="A common student error with the input method is to", choices=[
   "divide the good's own input requirement by the other good's input requirement",
   "use the output rule of dividing the other good by the good itself, which reverses the correct ratio",
   "compare hours across countries",
   "compute absolute advantage first",
   "check the terms of trade"], ans=1,
   why="Output data uses other-over-own while input data uses own-over-other, and swapping them inverts every cost."),
 dict(q="When a table reports units of output per worker, the opportunity cost of one unit of a good is found by dividing", choices=[
   "that good's output by the other good's output",
   "the other good's output by that good's output",
   "hours by units",
   "units by hours",
   "output by the number of workers"], ans=1,
   why="With outputs the rule is other over own, which converts one good's units into the other's."),
 dict(q="When a table reports hours of labor required per unit, the opportunity cost of one unit of a good is found by dividing", choices=[
   "that good's hours by the other good's hours",
   "the other good's hours by that good's hours",
   "hours by output",
   "output by hours",
   "total hours by the number of goods"], ans=0,
   why="With inputs the rule is own over other, the reverse of the output rule."),
 dict(q="Terms of trade that lie outside the range set by the two countries' opportunity costs will", choices=[
   "benefit both countries",
   "leave at least one country worse off than producing the good itself",
   "always benefit the smaller country",
   "be enforced by tariffs",
   "raise total world output"], ans=1,
   why="A country will not accept a price worse than its own cost of making the good at home."),
 dict(q="Specialization according to comparative advantage raises total world output because", choices=[
   "each country produces everything it consumes",
   "each good is produced by the country that gives up the least to make it",
   "absolute advantage is eliminated",
   "prices fall in every market",
   "resources become unlimited"], ans=1,
   why="Assigning production to the lowest-cost producer wastes the least of the other good."),
 dict(q="If two countries have identical opportunity costs for both goods, then", choices=[
   "both gain enormously from trade",
   "there is no comparative advantage and no basis for mutually beneficial specialization",
   "the larger country gains",
   "trade doubles output",
   "absolute advantage determines trade"], ans=1,
   why="Gains come from differences in opportunity cost, and here there are none."),
 dict(q="On a two-good production possibilities diagram for a single country, comparative advantage corresponds to", choices=[
   "the intercepts of the curve",
   "the slope of the curve, which is the opportunity cost",
   "the area under the curve",
   "the position of the curve relative to the origin",
   "the level of unemployment"], ans=1,
   why="The slope measures what must be given up, so the flatter-slope country is the low-cost producer."),
 dict(q="A country with a small population and few resources", choices=[
   "cannot gain from trade",
   "can still have a comparative advantage and gain from trade",
   "must have an absolute advantage to trade",
   "always has a comparative advantage in every good",
   "should produce all goods itself"], ans=1,
   why="Comparative advantage depends on relative costs, not on the scale of the economy."),
 dict(q="Country M can produce 100 shirts or 200 hats with its resources; Country N can produce 80 shirts or 240 hats. The opportunity cost of one shirt in Country M is", choices=[
   "0.5 hats", "1 hat", "2 hats", "3 hats", "100 hats"], ans=2,
   why="Two hundred hats divided by 100 shirts gives 2 hats given up per shirt."),
 dict(q="Country M can produce 100 shirts or 200 hats; Country N can produce 80 shirts or 240 hats. The opportunity cost of one shirt in Country N is", choices=[
   "0.5 hats", "1 hat", "2 hats", "3 hats", "240 hats"], ans=3,
   why="Two hundred forty hats divided by 80 shirts gives 3 hats given up per shirt."),
 dict(q="With M able to make 100 shirts or 200 hats and N able to make 80 shirts or 240 hats, comparative advantage lies with", choices=[
   "M in shirts and N in hats",
   "M in hats and N in shirts",
   "M in both goods",
   "N in both goods",
   "neither country in either good"], ans=0,
   why="M gives up 2 hats per shirt against N's 3, while N gives up one third of a shirt per hat against M's one half."),
 dict(q="Given M's cost of 2 hats per shirt and N's cost of 3 hats per shirt, a mutually acceptable price for one shirt is", choices=[
   "1 hat", "1.5 hats", "2.5 hats", "3.5 hats", "4 hats"], ans=2,
   why="The shirt price must fall between M's cost of 2 hats and N's cost of 3 hats."),
 dict(q="Trade based on comparative advantage allows a country to consume", choices=[
   "only combinations on its own production possibilities curve",
   "combinations beyond its own production possibilities curve",
   "less than it produces",
   "only the good it specializes in",
   "the same bundle as before trade"], ans=1,
   why="Trading at a price better than the domestic cost lets consumption exceed domestic production possibilities."),
 dict(q="The consumption possibilities curve of a country that trades at favorable terms lies", choices=[
   "inside its production possibilities curve",
   "outside its production possibilities curve",
   "exactly on its production possibilities curve",
   "below the horizontal axis",
   "at a single point"], ans=1,
   why="Trade converts the specialized good into the other good more cheaply than home production can."),
 dict(q="Which of the following is the strongest argument against the claim that a country should never import a good it can make itself?", choices=[
   "imports are always cheaper in money terms",
   "resources used to make that good could produce more value in the industry where the country's opportunity cost is lowest",
   "domestic firms dislike competition",
   "tariffs raise revenue",
   "trade balances must be equal"], ans=1,
   why="The relevant cost is what the resources could otherwise produce, not whether production is technically possible."),
 dict(q="If the world price of a good equals a country's own domestic opportunity cost of producing it, that country", choices=[
   "gains a great deal from trading that good",
   "gains nothing from trading that good, since trade and home production cost the same",
   "loses from trade",
   "should specialize completely in it",
   "should stop producing it"], ans=1,
   why="At the boundary of the trading range, trade neither improves nor worsens the country's position."),
 dict(q="Two neighbors, one a faster carpenter and a faster cook than the other, should still divide the work because", choices=[
   "absolute advantage requires it",
   "each has a lower opportunity cost in one task, so specializing raises total output of both",
   "fairness demands it",
   "one of them must be worse at both",
   "trade is always equal"], ans=1,
   why="The comparative advantage argument applies to individuals exactly as it does to countries."),
 dict(q="A country that specializes completely according to comparative advantage will", choices=[
   "produce a bundle it also consumes",
   "produce more of its specialty than it consumes and trade the surplus for the other good",
   "consume only its specialty",
   "produce inside its production possibilities curve",
   "have zero opportunity cost"], ans=1,
   why="The whole point of specializing is exchanging the surplus for goods it no longer produces."),
 dict(q="An improvement in technology that doubles a country's output of both goods equally will", choices=[
   "reverse its comparative advantage",
   "leave its comparative advantage unchanged, since relative opportunity costs are the same",
   "eliminate comparative advantage",
   "give it comparative advantage in both goods",
   "make trade impossible"], ans=1,
   why="Comparative advantage depends on the ratio of the two outputs, which doubling leaves untouched."),
 dict(q="An improvement in technology that raises a country's output of only one good may", choices=[
   "never change comparative advantage",
   "change which good the country has a comparative advantage in, since the ratio of outputs changes",
   "eliminate absolute advantage",
   "raise opportunity cost in both goods",
   "have no effect on production"], ans=1,
   why="A lopsided productivity gain alters relative costs and can flip the pattern of specialization."),
 dict(q="The main reason a country might resist specializing fully in a single good is that", choices=[
   "comparative advantage is a myth",
   "concentrating in one industry exposes the economy to risks such as price swings and loss of self-sufficiency",
   "trade lowers world output",
   "opportunity cost falls to zero",
   "absolute advantage forbids it"], ans=1,
   why="The gains from specialization are real, but so is the risk of depending on one industry or trading partner."),
 dict(q="Which statement about absolute and comparative advantage is correct?", choices=[
   "A country with an absolute advantage in a good necessarily has a comparative advantage in it",
   "A country can have an absolute advantage in a good without having a comparative advantage in it",
   "Comparative advantage requires absolute advantage",
   "Absolute advantage determines the pattern of trade",
   "The two concepts always coincide"], ans=1,
   why="Being more productive in a good says nothing about what that production costs in terms of the other good."),
]
