# 1.4 Comparative Advantage and Trade — 50 questions
# All numeric answers verified by hand:
#   Alpha 40W/20C, Beta 30W/10C -> OC wheat: A 1/2C, B 1/3C; OC cloth: A 2W, B 3W
#   Japan steel1200/coal300, Canada steel1000/coal500 -> OC steel: J 1/4, C 1/2; OC coal: J 4, C 2
#   US car3h/truck6h, Brazil car2h/truck2h -> OC car: US 1/2T, Br 1T; OC truck: US 2C, Br 1C
#   Maya 8 cakes/4 pies, Leo 6/6 -> OC cake: M 1/2P, L 1P; OC pie: M 2C, L 1C
OUT1 = dict(headers=["", "Wheat (tons)", "Cloth (bolts)"], rows=[["Alpha", "40", "20"], ["Beta", "30", "10"]])
OUT2 = dict(headers=["", "Steel (tons)", "Coal (tons)"], rows=[["Japan", "1200", "300"], ["Canada", "1000", "500"]])
INP1 = dict(headers=["Hours to produce one unit", "Car", "Truck"], rows=[["United States", "3", "6"], ["Brazil", "2", "2"]])
OUT3 = dict(headers=["Per day", "Cakes", "Pies"], rows=[["Maya", "8", "4"], ["Leo", "6", "6"]])

TOPIC = ("1.4", "Comparative Advantage and Trade", 1)
QUESTIONS = [
 dict(q="Absolute advantage is the ability to", choices=[
   "produce a good at the lowest opportunity cost",
   "produce more of a good with the same resources (or the same amount with fewer resources) than another producer",
   "sell a good at the highest price",
   "consume more than another country",
   "export every good a country makes"], ans=1,
   why="Absolute advantage is producing more with the same resources (or the same with fewer)."),
 dict(q="Comparative advantage is the ability to", choices=[
   "produce more of every good than a rival",
   "produce a good at a lower opportunity cost than another producer",
   "employ more workers than a rival",
   "use the most advanced technology",
   "produce without any opportunity cost"], ans=1,
   why="Comparative advantage means lower opportunity cost, not greater output."),
 dict(q="The terms of trade are defined as", choices=[
   "the tariffs two countries charge each other",
   "the rate at which one good is exchanged for another",
   "the transportation cost of trade",
   "the currency exchange rate",
   "the legal documents governing a trade agreement"], ans=1,
   why="Terms of trade are the exchange rate between the goods themselves."),
 dict(q="According to the principle of comparative advantage, countries gain from trade when each specializes in the good it", choices=[
   "can produce in the largest quantity",
   "produces at the lowest opportunity cost",
   "has produced the longest",
   "consumes the most",
   "can produce with the most labor"], ans=1,
   why="Specialization should follow the lower opportunity cost."),
 dict(q="A country can have an absolute advantage in a good without a comparative advantage in it because", choices=[
   "absolute advantage is about opportunity costs",
   "producing more of a good may still come at a higher opportunity cost",
   "comparative advantage requires better technology",
   "absolute advantage requires trade",
   "the two terms mean the same thing"], ans=1,
   why="Bigger output can still mean a larger sacrifice of the other good."),
 dict(q="Countries generally export goods in which they have", choices=[
   "an absolute disadvantage",
   "a comparative advantage",
   "the highest production costs",
   "no domestic demand",
   "government monopolies"], ans=1,
   why="Export the comparative-advantage good; import the other."),
 dict(q="It is impossible for one country to have a comparative advantage in BOTH goods of a two-good model because", choices=[
   "no country is that productive",
   "opportunity costs are reciprocals — a lower cost in one good implies a higher cost in the other",
   "trade agreements forbid it",
   "absolute advantage prevents it",
   "resources are identical across countries"], ans=1,
   why="If your OC of X is lower, your OC of Y (its reciprocal) must be higher."),
 dict(q="In OUTPUT problems, the per-unit opportunity cost of a good is calculated as", choices=[
   "gain divided by give up",
   "the amount of the other good given up divided by the amount of this good gained",
   "price divided by quantity",
   "hours divided by output",
   "output divided by hours"], ans=1,
   why="Output problems: OC = (other output given up) / (output gained) — 'Output Other Over.'"),
 dict(q="In INPUT problems (resources needed per unit), the opportunity cost of a good is calculated using", choices=[
   "output other over",
   "the good's own input divided by the other good's input",
   "give up divided by gain with outputs",
   "price times quantity",
   "total hours worked"], ans=1,
   why="Input problems: OC of a good = its input requirement over the other good's — 'Input Other Under' (IOU)."),
 dict(table=OUT1, q="Using all resources, Alpha and Beta can produce the amounts shown. Which country has an absolute advantage, and in what?", choices=[
   "Alpha in wheat only",
   "Beta in cloth only",
   "Alpha in both goods",
   "Beta in both goods",
   "Neither country in either good"], ans=2,
   why="Alpha out-produces Beta in wheat (40>30) and cloth (20>10)."),
 dict(table=OUT1, q="In the table, Alpha's opportunity cost of producing one ton of wheat is", choices=[
   "2 bolts of cloth", "1/2 bolt of cloth", "1/3 bolt of cloth", "3 bolts of cloth", "20 bolts of cloth"], ans=1,
   why="20 cloth forgone / 40 wheat = 1/2 bolt per ton of wheat."),
 dict(table=OUT1, q="In the table, Beta's opportunity cost of producing one bolt of cloth is", choices=[
   "1/3 ton of wheat", "1/2 ton of wheat", "2 tons of wheat", "3 tons of wheat", "10 tons of wheat"], ans=3,
   why="30 wheat forgone / 10 cloth = 3 tons per bolt."),
 dict(table=OUT1, q="Based on the table, which country has the comparative advantage in wheat?", choices=[
   "Alpha, because its wheat opportunity cost is 1/2 bolt versus Beta's 1/3 bolt",
   "Beta, because its wheat opportunity cost of 1/3 bolt is lower than Alpha's 1/2 bolt",
   "Alpha, because it produces more wheat",
   "Beta, because it produces less cloth",
   "Neither country"], ans=1,
   why="Beta gives up only 1/3 bolt per ton of wheat, less than Alpha's 1/2."),
 dict(table=OUT1, q="If Alpha and Beta specialize according to comparative advantage and trade, which terms of trade for cloth would benefit BOTH countries?", choices=[
   "1 bolt of cloth for 1.5 tons of wheat",
   "1 bolt of cloth for 2.5 tons of wheat",
   "1 bolt of cloth for 4 tons of wheat",
   "1 bolt of cloth for 1 ton of wheat",
   "1 bolt of cloth for 5 tons of wheat"], ans=1,
   why="Mutually beneficial terms lie between the OCs: 2 and 3 wheat per bolt; 2.5 qualifies."),
 dict(table=OUT2, q="One worker per day can produce the amounts shown. Japan's opportunity cost of one ton of steel is", choices=[
   "4 tons of coal", "1/2 ton of coal", "1/4 ton of coal", "2 tons of coal", "300 tons of coal"], ans=2,
   why="300 coal / 1200 steel = 1/4 ton of coal per ton of steel."),
 dict(table=OUT2, q="Based on the table, which country should export coal, and why?", choices=[
   "Japan, because it has an absolute advantage in steel",
   "Canada, because its opportunity cost of coal (2 steel) is lower than Japan's (4 steel)",
   "Japan, because its coal output is smaller",
   "Canada, because it produces more steel",
   "Neither — coal cannot be traded profitably"], ans=1,
   why="Canada sacrifices 2 steel per coal versus Japan's 4 — Canada has the CA in coal."),
 dict(table=OUT2, q="Which terms of trade for 1 ton of coal would be acceptable to BOTH Japan and Canada?", choices=[
   "1 ton of steel", "1.5 tons of steel", "3 tons of steel", "5 tons of steel", "6 tons of steel"], ans=2,
   why="Terms must fall between the coal OCs of 2 and 4 steel; 3 does."),
 dict(table=INP1, q="The table shows hours needed to make one unit. Which country has the absolute advantage in each good?", choices=[
   "The U.S. in both",
   "Brazil in both, since it needs fewer hours for each good",
   "The U.S. in cars, Brazil in trucks",
   "Brazil in cars, the U.S. in trucks",
   "Neither country in either good"], ans=1,
   why="Brazil uses fewer hours per car (2<3) and per truck (2<6)."),
 dict(table=INP1, q="Using the table, the U.S. opportunity cost of producing one car is", choices=[
   "2 trucks", "1 truck", "1/2 truck", "3 trucks", "6 trucks"], ans=2,
   why="Input rule: 3 hours per car / 6 hours per truck = 1/2 truck per car."),
 dict(table=INP1, q="Based on opportunity costs from the table, trade between the two countries should involve", choices=[
   "the U.S. exporting cars and importing trucks from Brazil",
   "the U.S. exporting trucks and importing cars",
   "Brazil exporting both goods",
   "the U.S. exporting both goods",
   "no trade, since Brazil has an absolute advantage in both"], ans=0,
   why="U.S. CA in cars (1/2 truck < 1 truck); Brazil CA in trucks (1 car < 2 cars)."),
 dict(table=INP1, q="Which terms of trade for one truck would benefit both the U.S. and Brazil?", choices=[
   "1/2 car", "3/4 car", "1.5 cars", "2.5 cars", "3 cars"], ans=2,
   why="Truck OCs are 1 car (Brazil) and 2 cars (U.S.); 1.5 lies between."),
 dict(table=OUT3, q="Maya and Leo can each produce the daily amounts shown. Who has the comparative advantage in pies?", choices=[
   "Maya, because she bakes more cakes",
   "Leo, because his opportunity cost of a pie (1 cake) is lower than Maya's (2 cakes)",
   "Maya, because her opportunity cost of a pie is lower",
   "Leo, because he has an absolute advantage in everything",
   "Neither person"], ans=1,
   why="Pie OC: Maya 8/4 = 2 cakes; Leo 6/6 = 1 cake — Leo's is lower."),
 dict(table=OUT3, q="If Maya and Leo specialize according to comparative advantage, Maya should", choices=[
   "produce only pies",
   "produce only cakes",
   "produce both goods equally",
   "produce nothing and only trade",
   "match whatever Leo produces"], ans=1,
   why="Maya's cake OC (1/2 pie) beats Leo's (1 pie), so she specializes in cakes."),
 dict(table=OUT3, q="Which exchange rate for one pie would make BOTH Maya and Leo better off?", choices=[
   "1/2 cake per pie", "3/4 cake per pie", "1.5 cakes per pie", "2.5 cakes per pie", "3 cakes per pie"], ans=2,
   why="Between the pie OCs of 1 cake (Leo) and 2 cakes (Maya): 1.5 works."),
 dict(q="Island X can produce 10 fish or 5 coconuts per day; Island Y can produce 20 fish or 10 coconuts. Which statement is correct?", choices=[
   "Y has a comparative advantage in both goods",
   "X has a comparative advantage in fish",
   "Their opportunity costs are identical, so there are no gains from specialization",
   "X should export coconuts and import fish",
   "Y should import both goods"], ans=2,
   why="Both face 1 fish = 1/2 coconut; equal OCs mean no basis for mutually beneficial trade."),
 dict(q="If two producers can each make one unit of a good using the same amount of resources, then with respect to that good", choices=[
   "each has a comparative advantage",
   "neither has an absolute advantage",
   "both should specialize in it",
   "trade in it is impossible",
   "one must have an absolute advantage"], ans=1,
   why="Equal productivity means neither out-produces the other — no absolute advantage."),
 dict(q="Specialization according to comparative advantage, followed by trade, allows total world output to", choices=[
   "stay the same but be shared differently",
   "increase, because goods are produced at the lowest opportunity cost",
   "decrease as countries stop producing some goods",
   "increase only for the country with absolute advantage",
   "become irrelevant to consumption"], ans=1,
   why="Producing where OC is lowest raises combined output — the gains from trade."),
 dict(q="Mutually beneficial terms of trade must lie", choices=[
   "above both countries' opportunity costs",
   "below both countries' opportunity costs",
   "between the two countries' opportunity costs for the traded good",
   "exactly at one country's opportunity cost",
   "at whatever the larger country dictates"], ans=2,
   why="Only rates between the two OCs leave both sides better off than self-production."),
 dict(q="If the terms of trade exactly equal a country's own opportunity cost of the good, that country", choices=[
   "gains enormously from trading",
   "gains nothing compared with producing the good itself",
   "must stop producing entirely",
   "will import both goods",
   "loses from trading"], ans=1,
   why="Trading at your own OC replicates what you could do alone — zero gain."),
 dict(q="Trade allows a country's CONSUMPTION possibilities to", choices=[
   "shrink to match production",
   "exceed its own production possibilities",
   "equal its production possibilities exactly",
   "become independent of world prices",
   "depend only on its absolute advantage"], ans=1,
   why="With trade, a country can consume combinations beyond its own PPC."),
 dict(q="Gains from trade are the", choices=[
   "tariff revenues collected by governments",
   "economic benefits from specialization by comparative advantage and mutually beneficial exchange",
   "profits earned only by exporters",
   "losses avoided by refusing to trade",
   "subsidies paid to import-competing firms"], ans=1,
   why="Gains from trade come from specialization plus mutually beneficial exchange."),
 dict(q="Anna needs 2 hours to bake a loaf of bread and 4 hours to make a wheel of cheese. Ben needs 3 hours for either one. Who has the comparative advantage in cheese?", choices=[
   "Anna, whose cheese costs 2 loaves of bread",
   "Ben, whose cheese costs only 1 loaf of bread",
   "Anna, because she is faster at bread",
   "Ben, because he is slower at everything",
   "Neither person"], ans=1,
   why="Cheese OC: Anna 4/2 = 2 loaves; Ben 3/3 = 1 loaf — Ben's is lower."),
 dict(q="In the previous scenario (Anna: 2h bread, 4h cheese; Ben: 3h each), absolute advantage belongs to", choices=[
   "Anna in both goods",
   "Ben in both goods",
   "Anna in bread and Ben in cheese",
   "Ben in bread and Anna in cheese",
   "neither person in either good"], ans=2,
   why="Fewer hours wins: Anna's bread (2<3); Ben's cheese (3<4)."),
 dict(q="The mnemonic 'Output Other Over' reminds students that in output problems the opportunity cost of a good equals", choices=[
   "the other good's output divided by this good's output",
   "this good's output divided by the other's",
   "total output over total input",
   "output multiplied by input",
   "the price ratio of the goods"], ans=0,
   why="OC = other good's forgone output over this good's output."),
 dict(q="The mnemonic 'Input Other Under' (IOU) reminds students that in input problems the opportunity cost of a good equals", choices=[
   "the other good's input requirement divided by this good's",
   "this good's input requirement divided by the other good's",
   "inputs multiplied together",
   "the reciprocal of output",
   "hours minus output"], ans=1,
   why="With inputs, OC of a good = its own input over the other good's input."),
 dict(q="Which of the following is TRUE when a small country trades with a large, highly productive country?", choices=[
   "Only the large country can gain",
   "Only the small country can gain",
   "Both can gain if they trade at terms between their opportunity costs",
   "Neither gains unless productivity is equal",
   "The small country must run a trade deficit"], ans=2,
   why="Gains depend on differing OCs, not size; suitable terms benefit both."),
 dict(q="A country with a comparative advantage in wheat may still have", choices=[
   "the lowest opportunity cost in every good",
   "an absolute disadvantage in wheat",
   "no opportunity costs at all",
   "no reason to trade",
   "a comparative advantage in all other goods too"], ans=1,
   why="Comparative advantage can coexist with lower absolute productivity."),
 dict(q="Specialization means a producer", choices=[
   "makes a wide variety of goods",
   "concentrates production on the good(s) in which it has a comparative advantage",
   "produces only for domestic consumption",
   "refuses to trade",
   "matches competitors' product lines"], ans=1,
   why="Specialization concentrates effort where opportunity cost is lowest."),
 dict(q="Most economists agree that free trade based on comparative advantage", choices=[
   "reduces total world output",
   "raises overall economic welfare",
   "benefits only rich countries",
   "eliminates all domestic industries",
   "is identical to self-sufficiency"], ans=1,
   why="Trade by comparative advantage raises efficiency, output, and consumption."),
 dict(q="Producer A's opportunity cost of one chair is 3 tables; Producer B's is 2 tables. Trade at 4 tables per chair would", choices=[
   "benefit both producers",
   "benefit neither the chair buyer nor be acceptable to the table producer",
   "be rejected by whoever buys chairs, since self-production costs less than 4 tables",
   "be the only mutually beneficial rate",
   "benefit only B"], ans=2,
   why="At 4 tables, buying a chair costs more than either producer's own OC (3 or 2)."),
 dict(q="For the same producers (A: 1 chair = 3 tables; B: 1 chair = 2 tables), which trade ratio benefits both?", choices=[
   "1 chair for 1 table",
   "1 chair for 1.5 tables",
   "1 chair for 2.5 tables",
   "1 chair for 3.5 tables",
   "1 chair for 4 tables"], ans=2,
   why="Mutually beneficial terms lie between 2 and 3 tables per chair."),
 dict(q="In a two-good model, if Country Z's opportunity cost of good X is 5 units of good Y, then Z's opportunity cost of one unit of good Y is", choices=[
   "5 units of X", "1 unit of X", "1/5 unit of X", "10 units of X", "impossible to determine"], ans=2,
   why="Opportunity costs are reciprocals: 1 Y costs 1/5 X."),
 dict(q="When two individuals both benefit from an exchange, each obtaining a good at less than their own opportunity cost of making it, economists call this", choices=[
   "exploitation",
   "mutually beneficial trade",
   "absolute advantage",
   "protectionism",
   "autarky"], ans=1,
   why="Both parties gaining relative to self-production is mutually beneficial trade."),
 dict(q="AP exam problems describing 'how much can be produced with a set amount of resources' are", choices=[
   "input problems", "output problems", "terms-of-trade problems", "growth problems", "utility problems"], ans=1,
   why="Given resources, quantities produced = an output problem."),
 dict(q="AP exam problems describing 'how many hours are needed to produce one unit' are", choices=[
   "output problems", "input problems", "PPC problems", "elasticity problems", "cost-curve problems"], ans=1,
   why="Resource requirements per unit = an input problem."),
 dict(q="If two countries have identical opportunity costs for all goods, then", choices=[
   "trade will still raise total output",
   "specialization cannot increase combined output",
   "one country must subsidize the other",
   "both should specialize in the same good",
   "absolute advantage determines trade"], ans=1,
   why="Gains from trade require differing OCs; identical costs leave nothing to gain."),
 dict(q="A nation shifting all its resources into its comparative-advantage good and importing the other good expects to", choices=[
   "consume less of both goods",
   "consume more than it could in self-sufficiency",
   "eliminate its trading partner's gains",
   "abolish opportunity cost",
   "shrink its consumption possibilities"], ans=1,
   why="Specialize-and-trade expands what the country can consume."),
 dict(q="Which statement about the relationship between absolute and comparative advantage is correct?", choices=[
   "They always belong to the same country",
   "A country with absolute advantage in both goods still has comparative advantage in only one",
   "Comparative advantage requires absolute advantage",
   "Absolute advantage determines the direction of trade",
   "Neither concept involves opportunity cost"], ans=1,
   why="Even an all-around more productive country has a lower relative cost in just one good."),
 dict(q="Country M can make 60 phones or 20 drones. Its opportunity cost of one drone is", choices=[
   "1/3 phone", "3 phones", "20 phones", "60 phones", "2 phones"], ans=1,
   why="60 phones / 20 drones = 3 phones per drone."),
 dict(q="Country M (OC: 1 drone = 3 phones) trades with Country N, whose opportunity cost of a drone is 5 phones. Which country exports drones, and at which terms could both gain?", choices=[
   "N exports drones at 6 phones per drone",
   "M exports drones at 4 phones per drone",
   "M exports drones at 2 phones per drone",
   "N exports drones at 4 phones per drone",
   "Neither country trades drones"], ans=1,
   why="M's drone OC (3) is lower, so M exports; 4 lies between 3 and 5, benefiting both."),
]
assert len(QUESTIONS) == 50, len(QUESTIONS)
