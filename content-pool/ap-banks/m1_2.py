# MACRO 1.2 Opportunity Cost and the Production Possibilities Curve — 50 questions
#
# Table verified: PPC (increasing opportunity cost), Ridge Country, all resources used.
#   Combination : Wheat (tons) : Steel (tons)
#     A :  0 : 100
#     B : 10 :  95
#     C : 20 :  85
#     D : 30 :  70
#     E : 40 :  50
#   Opportunity cost of wheat, moving down the table (steel given up / wheat gained):
#     A->B: (100-95)/(10-0)  =  5/10 = 0.5 steel per ton of wheat
#     B->C: (95-85)/(20-10)  = 10/10 = 1.0 steel per ton of wheat
#     C->D: (85-70)/(30-20)  = 15/10 = 1.5 steel per ton of wheat
#     D->E: (70-50)/(40-30)  = 20/10 = 2.0 steel per ton of wheat
#   Rising cost per unit => increasing opportunity cost => bowed outward (concave) curve.
#   Total cost of moving A to E: 100 - 50 = 50 steel for 40 wheat = 1.25 steel per wheat on average.
#   Opportunity cost of steel, moving up the table (wheat given up / steel gained):
#     E->D: 10 wheat / 20 steel = 0.5 wheat per ton of steel
#     D->C: 10 wheat / 15 steel = 0.667 wheat per ton of steel
#     C->B: 10 wheat / 10 steel = 1.0 wheat per ton of steel
#     B->A: 10 wheat /  5 steel = 2.0 wheat per ton of steel
#   Inside-the-curve check: (20 wheat, 70 steel) lies inside, since C on the curve
#   allows 85 steel with 20 wheat; 70 < 85, so resources are idle or misallocated.
#   Outside check: (30 wheat, 90 steel) is unattainable, since D allows only 70 steel at 30 wheat.
#
# Table verified: LINEAR PPC (constant opportunity cost), Flat Country.
#   Combination : Bread (loaves) : Butter (tubs)
#     A :  0 : 80
#     B : 10 : 60
#     C : 20 : 40
#     D : 30 : 20
#     E : 40 :  0
#   Every 10 loaves costs exactly 20 tubs, so the cost is 2 tubs per loaf at every point,
#   and 0.5 loaves per tub in the other direction. Constant cost => straight-line PPC.

TOPIC = ("1.2", "Opportunity Cost and the Production Possibilities Curve", 1)

PPC = dict(
    headers=["Combination", "Wheat (tons)", "Steel (tons)"],
    rows=[["A", "0", "100"], ["B", "10", "95"], ["C", "20", "85"],
          ["D", "30", "70"], ["E", "40", "50"]],
)

LINPPC = dict(
    headers=["Combination", "Bread (loaves)", "Butter (tubs)"],
    rows=[["A", "0", "80"], ["B", "10", "60"], ["C", "20", "40"],
          ["D", "30", "20"], ["E", "40", "0"]],
)

QUESTIONS = [
 dict(q="A production possibilities curve shows", choices=[
   "the prices at which two goods trade",
   "the maximum combinations of two goods an economy can produce with its current resources and technology",
   "the quantity of a good consumers wish to buy",
   "the distribution of income across households",
   "the rate at which an economy grows each year"], ans=1,
   why="The curve is a boundary of what is producible, not a statement about prices or demand."),
 dict(q="A point located on the production possibilities curve represents", choices=[
   "an unattainable combination",
   "a combination that is both attainable and productively efficient",
   "a combination with unemployed resources",
   "the socially preferred combination",
   "a combination that requires trade to reach"], ans=1,
   why="On the curve every resource is being used, so more of one good requires less of the other."),
 dict(q="A point inside the production possibilities curve indicates that", choices=[
   "the economy is producing more than its capacity",
   "some resources are unemployed or used inefficiently",
   "technology has improved",
   "the economy must trade to survive",
   "opportunity cost is zero for every good"], ans=1,
   why="Interior points waste capacity, so more of both goods could be produced at once."),
 dict(q="A point outside the production possibilities curve is", choices=[
   "efficient",
   "unattainable with current resources and technology",
   "inefficient",
   "the equilibrium point",
   "attainable only if unemployment rises"], ans=1,
   why="The curve is the frontier of what the economy can currently produce."),
 dict(q="Moving from one point on a production possibilities curve to another point on the same curve requires", choices=[
   "no sacrifice at all",
   "giving up some of one good to gain more of the other",
   "an increase in the labor force",
   "an improvement in technology",
   "a fall in the price level"], ans=1,
   why="On the frontier all resources are already employed, so a gain in one good is paid for by the other."),
 dict(q="A production possibilities curve that is bowed outward from the origin reflects", choices=[
   "constant opportunity cost",
   "increasing opportunity cost as more of a good is produced",
   "decreasing opportunity cost",
   "zero opportunity cost",
   "unemployment of resources"], ans=1,
   why="The curve steepens because each additional unit costs more of the other good."),
 dict(q="Increasing opportunity cost along a production possibilities curve arises mainly because", choices=[
   "money loses value over time",
   "resources are not equally well suited to producing both goods",
   "consumers change their preferences",
   "the government intervenes in markets",
   "population grows"], ans=1,
   why="As output expands, resources poorly suited to that good must be pulled in, raising cost per unit."),
 dict(q="A straight-line production possibilities curve implies that", choices=[
   "resources are perfectly adaptable between the two goods, so opportunity cost is constant",
   "opportunity cost rises as output rises",
   "opportunity cost falls as output rises",
   "the economy is inefficient",
   "no trade-off exists"], ans=0,
   why="A constant slope means each extra unit always costs the same amount of the other good."),
 dict(q="The slope of a production possibilities curve at any point measures", choices=[
   "the price ratio of the two goods",
   "the opportunity cost of one more unit of the good on the horizontal axis",
   "the level of unemployment",
   "the growth rate of output",
   "consumer satisfaction"], ans=1,
   why="The slope is the amount of the vertical-axis good sacrificed per unit gained horizontally."),
 dict(q="Using the table, the opportunity cost of moving from combination A to combination B is", table=PPC, choices=[
   "5 tons of steel", "10 tons of steel", "15 tons of steel", "20 tons of steel", "95 tons of steel"], ans=0,
   why="Steel falls from 100 to 95 while wheat rises by 10, so 5 tons of steel are given up."),
 dict(q="Using the table, the opportunity cost per ton of wheat when moving from combination D to combination E is", table=PPC, choices=[
   "0.5 tons of steel", "1.0 tons of steel", "1.5 tons of steel", "2.0 tons of steel", "20 tons of steel"], ans=3,
   why="Steel falls from 70 to 50, a loss of 20 tons, for 10 additional tons of wheat, so 2 tons of steel each."),
 dict(q="Using the table, the opportunity cost per ton of wheat when moving from combination B to combination C is", table=PPC, choices=[
   "0.5 tons of steel", "1.0 tons of steel", "1.5 tons of steel", "2.0 tons of steel", "10 tons of steel"], ans=1,
   why="Ten tons of steel are given up for ten additional tons of wheat, a cost of one for one."),
 dict(q="The table shows that this economy faces", table=PPC, choices=[
   "constant opportunity cost",
   "increasing opportunity cost, since each additional 10 tons of wheat costs more steel than the last",
   "decreasing opportunity cost",
   "zero opportunity cost",
   "no trade-off between the goods"], ans=1,
   why="The steel sacrificed per 10 tons of wheat rises from 5 to 10 to 15 to 20."),
 dict(q="Based on the table, a combination of 20 tons of wheat and 70 tons of steel would be", table=PPC, choices=[
   "efficient and on the curve",
   "attainable but inefficient, since 85 tons of steel are possible with 20 tons of wheat",
   "unattainable",
   "possible only after economic growth",
   "the same as combination D"], ans=1,
   why="Combination C shows 85 tons of steel at 20 tons of wheat, so producing only 70 wastes capacity."),
 dict(q="Based on the table, a combination of 30 tons of wheat and 90 tons of steel is", table=PPC, choices=[
   "efficient",
   "unattainable without growth in resources or technology",
   "inefficient",
   "identical to combination C",
   "attainable if unemployment falls"], ans=1,
   why="At 30 tons of wheat the maximum steel output is 70 tons, so 90 lies beyond the frontier."),
 dict(q="Using the table, the opportunity cost of moving from combination E to combination D, per ton of steel gained, is", table=PPC, choices=[
   "0.5 tons of wheat", "1 ton of wheat", "1.5 tons of wheat", "2 tons of wheat", "10 tons of wheat"], ans=0,
   why="Ten tons of wheat are given up to gain 20 tons of steel, which is half a ton of wheat per ton of steel."),
 dict(q="Using the table, the average opportunity cost per ton of wheat of moving all the way from combination A to combination E is", table=PPC, choices=[
   "0.5 tons of steel", "1.25 tons of steel", "2 tons of steel", "40 tons of steel", "50 tons of steel"], ans=1,
   why="Fifty tons of steel are sacrificed for forty tons of wheat, and 50 divided by 40 is 1.25."),
 dict(q="Using the linear table, the opportunity cost of one loaf of bread is", table=LINPPC, choices=[
   "0.5 tubs of butter", "1 tub of butter", "2 tubs of butter", "10 tubs of butter", "20 tubs of butter"], ans=2,
   why="Every 10 loaves costs 20 tubs, so each loaf costs 2 tubs, and the cost never changes."),
 dict(q="Using the linear table, the opportunity cost of one tub of butter is", table=LINPPC, choices=[
   "0.5 loaves of bread", "1 loaf of bread", "2 loaves of bread", "20 loaves of bread", "40 loaves of bread"], ans=0,
   why="Twenty tubs cost 10 loaves, so one tub costs half a loaf."),
 dict(q="The linear table describes a production possibilities curve that is", table=LINPPC, choices=[
   "bowed outward",
   "a straight line, because opportunity cost is constant at every combination",
   "bowed inward",
   "vertical",
   "upward sloping"], ans=1,
   why="Each 10 loaves always costs exactly 20 tubs, so the slope never changes."),
 dict(q="An improvement in technology that raises output of both goods will", choices=[
   "move the economy along its existing curve",
   "shift the entire production possibilities curve outward",
   "shift the curve inward",
   "leave the curve unchanged",
   "make the curve vertical"], ans=1,
   why="Growth in productive capacity moves the whole frontier outward."),
 dict(q="A technological advance that raises productivity only in the wheat industry will", choices=[
   "shift the entire curve outward evenly",
   "rotate the curve outward along the wheat axis while the maximum steel output stays the same",
   "shift the curve inward",
   "leave the curve unchanged",
   "cause a movement along the curve"], ans=1,
   why="Only the intercept for the improved good moves, so the frontier pivots rather than shifting evenly."),
 dict(q="A severe earthquake that destroys much of a country's capital stock will", choices=[
   "shift the production possibilities curve outward",
   "shift the production possibilities curve inward",
   "cause a movement along the curve",
   "leave the curve unchanged",
   "eliminate opportunity cost"], ans=1,
   why="Fewer resources means every combination the economy can reach shrinks."),
 dict(q="An increase in the size of the labor force through immigration is most likely to", choices=[
   "shift the production possibilities curve outward",
   "shift the curve inward",
   "cause a movement from one point on the curve to another",
   "make the curve a straight line",
   "have no effect on productive capacity"], ans=0,
   why="More labor raises the maximum output of both goods."),
 dict(q="An economy operating at a point inside its production possibilities curve can increase production of both goods by", choices=[
   "giving up some of one good",
   "putting its idle resources back to work",
   "acquiring new technology only",
   "reducing its population",
   "raising the price level"], ans=1,
   why="Interior points leave slack, so unemployment can fall without any sacrifice."),
 dict(q="A rise in the unemployment rate during a recession is best represented on the production possibilities curve as", choices=[
   "an outward shift of the curve",
   "a movement from a point on the curve to a point inside it",
   "a movement along the curve",
   "an inward shift of the curve",
   "a movement to a point outside the curve"], ans=1,
   why="Capacity is unchanged; the economy simply stops using all of it."),
 dict(q="Which of the following would NOT shift a country's production possibilities curve outward?", choices=[
   "an increase in the capital stock",
   "a decision to produce more consumer goods and fewer capital goods this year",
   "an improvement in worker education",
   "the discovery of a new mineral deposit",
   "a new production technology"], ans=1,
   why="Choosing a different point on the same frontier is a movement along it, not a change in capacity."),
 dict(q="An economy that devotes a larger share of current output to capital goods rather than consumer goods can expect", choices=[
   "a smaller outward shift of its future curve",
   "a larger outward shift of its future production possibilities curve, at the cost of less consumption now",
   "no change in its future curve",
   "an inward shift of its future curve",
   "the elimination of opportunity cost"], ans=1,
   why="Capital goods add to future productive capacity, and the sacrifice is present consumption."),
 dict(q="Productive efficiency is achieved when an economy", choices=[
   "produces the combination consumers most prefer",
   "produces on its production possibilities curve, so no more of one good can be made without less of another",
   "produces inside its curve",
   "eliminates opportunity cost",
   "produces equal amounts of both goods"], ans=1,
   why="Productive efficiency is about being on the frontier, not about which point on it is chosen."),
 dict(q="Allocative efficiency refers to producing", choices=[
   "the maximum possible total output",
   "the particular combination of goods on the curve that society most values",
   "equal quantities of every good",
   "inside the curve to keep reserves",
   "only capital goods"], ans=1,
   why="Many points are productively efficient, but only one matches society's preferences."),
 dict(q="Which of the following statements about a bowed-outward production possibilities curve is correct?", choices=[
   "Opportunity cost is the same at every point",
   "The opportunity cost of a good rises as more of it is produced",
   "Opportunity cost falls as more of a good is produced",
   "Every point on the curve is inefficient",
   "The curve implies unemployment"], ans=1,
   why="The bowed shape is exactly the graphical statement of increasing opportunity cost."),
 dict(q="If a country can produce a maximum of 500 cars or a maximum of 1,000 computers with constant opportunity cost, the opportunity cost of one car is", choices=[
   "0.5 computers", "1 computer", "2 computers", "500 computers", "1,000 computers"], ans=2,
   why="Giving up all 1,000 computers buys 500 cars, so each car costs 2 computers."),
 dict(q="In the same country, whose constant-cost frontier runs between 500 cars and 1,000 computers, the opportunity cost of one computer is", choices=[
   "0.5 cars", "1 car", "2 cars", "500 cars", "1,000 cars"], ans=0,
   why="One thousand computers cost 500 cars, so each computer costs half a car."),
 dict(q="A country's straight-line curve has intercepts of 500 cars and 1,000 computers. A combination of 300 cars and 400 computers is", choices=[
   "on the curve, since 300 cars costs 600 computers and 1,000 minus 600 leaves exactly 400",
   "inside the curve",
   "outside the curve",
   "impossible to classify without prices",
   "attainable only after economic growth"], ans=0,
   why="Each car costs 2 computers, so 300 cars uses up 600 computers and leaves exactly the 400 produced."),
 dict(q="Economic growth is best represented on a production possibilities diagram by", choices=[
   "a movement along the curve",
   "an outward shift of the curve",
   "a movement to a point inside the curve",
   "a steepening of the curve only",
   "no change at all"], ans=1,
   why="Growth means the whole set of attainable combinations expands."),
 dict(q="The production possibilities curve for guns and butter is drawn assuming", choices=[
   "resources and technology are fixed and all resources are used efficiently",
   "prices are fixed",
   "the government sets output",
   "trade with other countries occurs",
   "unemployment is high"], ans=0,
   why="Fixed resources and technology are what make the frontier a fixed boundary."),
 dict(q="If a country's production possibilities curve shifts outward but the country continues to produce at a point inside the new curve, then", choices=[
   "productive capacity fell",
   "capacity rose but some resources remain unemployed",
   "the country is allocatively efficient",
   "opportunity cost is zero",
   "the curve must be a straight line"], ans=1,
   why="An outward shift raises what is possible, but an interior point still means idle resources."),
 dict(q="The law of increasing costs states that as production of a good expands", choices=[
   "its money price must fall",
   "the amount of the other good sacrificed per additional unit rises",
   "total output falls",
   "opportunity cost stays constant",
   "unemployment must rise"], ans=1,
   why="Less suitable resources are drawn in as output expands, raising cost per unit."),
 dict(q="Suppose an economy can produce 40 tons of wheat and 50 tons of steel, or 30 tons of wheat and 70 tons of steel. The opportunity cost of moving to the higher-wheat combination is", choices=[
   "10 tons of wheat", "20 tons of steel", "30 tons of steel", "50 tons of steel", "zero"], ans=1,
   why="Gaining 10 tons of wheat means steel falls from 70 to 50, a sacrifice of 20 tons."),
 dict(q="Which of the following is measured on the axes of a standard production possibilities curve?", choices=[
   "price and quantity",
   "the quantities of two different goods",
   "income and consumption",
   "cost and revenue",
   "output and the price level"], ans=1,
   why="Both axes are quantities of goods, which is why the slope is an opportunity cost rather than a price."),
 dict(q="A country discovers that a large share of its workers lack the skills used in the steel industry but are well suited to farming. This helps explain why its curve", choices=[
   "is a straight line",
   "is bowed outward, since resources are not equally productive in both uses",
   "is bowed inward",
   "shifts inward each year",
   "has a positive slope"], ans=1,
   why="Unequal resource suitability is precisely the source of increasing opportunity cost."),
 dict(q="If both goods on a production possibilities diagram are consumer goods and the economy moves along the curve toward more of one good, then", choices=[
   "future capacity necessarily rises",
   "the economy trades one form of present consumption for another with no gain in future capacity",
   "the curve shifts outward",
   "unemployment must rise",
   "opportunity cost is zero"], ans=1,
   why="Shifting between two consumer goods changes the mix of present consumption, not the capital stock."),
 dict(q="A war that destroys factories and a rise in unemployment during a recession differ on a production possibilities diagram in that", choices=[
   "both shift the curve inward",
   "the war shifts the curve inward while the recession moves the economy to a point inside an unchanged curve",
   "both are movements along the curve",
   "the recession shifts the curve inward while the war does not",
   "neither has any effect"], ans=1,
   why="Destroyed capital reduces capacity, but idle workers only leave existing capacity unused."),
 dict(q="Which combination of statements about a point on the production possibilities curve is correct?", choices=[
   "It is attainable and resources are idle",
   "It is attainable and no more of one good can be produced without producing less of the other",
   "It is unattainable and efficient",
   "It is attainable only after growth",
   "It is inefficient but attainable"], ans=1,
   why="Being on the frontier means attainable and fully efficient at the same time."),
 dict(q="Suppose the opportunity cost of the first 10 units of a good is 5 units of another good, the second 10 units costs 5, and the third 10 units also costs 5. The curve is", choices=[
   "bowed outward", "a straight line", "bowed inward", "vertical", "horizontal"], ans=1,
   why="A constant sacrifice per batch is a constant slope, which is a straight line."),
 dict(q="Opportunity cost on a production possibilities curve is measured in units of", choices=[
   "dollars",
   "the other good forgone",
   "hours of labor",
   "the price level",
   "percentage points of unemployment"], ans=1,
   why="The cost of a good on the frontier is the quantity of the other good given up for it."),
 dict(q="An economy is producing at a point on its production possibilities curve. Government orders firms to produce more of both goods. The most likely result is that", choices=[
   "output of both goods rises",
   "the order cannot be fulfilled without more resources or better technology",
   "the curve shifts outward automatically",
   "opportunity cost falls to zero",
   "unemployment rises"], ans=1,
   why="A point on the frontier already uses every resource, so more of both is not available."),
 dict(q="A country whose curve is bowed outward decides to produce only wheat and no steel. At that extreme point, the opportunity cost of the last ton of wheat is", choices=[
   "zero",
   "at its highest, because the resources least suited to wheat are being used for wheat",
   "at its lowest",
   "equal to the cost of the first ton",
   "impossible to determine"], ans=1,
   why="The curve is steepest at the extreme, so the final units cost the most steel."),
 dict(q="A more educated workforce and a larger stock of machinery both affect the production possibilities curve by", choices=[
   "moving the economy along the curve",
   "shifting the curve outward, since each raises the economy's productive capacity",
   "shifting the curve inward",
   "flattening the curve without shifting it",
   "leaving capacity unchanged"], ans=1,
   why="Human capital and physical capital are both productive resources, so more of either expands the frontier."),
 dict(q="Which of the following best explains why a production possibilities curve slopes downward?", choices=[
   "Prices fall as output rises",
   "With resources fully employed, producing more of one good requires producing less of the other",
   "Consumers prefer variety",
   "Technology improves over time",
   "Unemployment rises with output"], ans=1,
   why="Scarcity plus full employment forces a trade-off, and that trade-off is the negative slope."),
]
