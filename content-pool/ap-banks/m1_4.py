# MACRO 1.4 Demand — 50 questions
#
# Table verified: demand schedule for coffee (a single market, per week).
#   Price ($ per pound) : Quantity demanded (pounds)
#     2 : 500
#     4 : 400
#     6 : 300
#     8 : 200
#    10 : 100
#   Every $2 rise in price lowers quantity demanded by exactly 100 pounds, so the schedule
#   is linear and downward sloping, consistent with the law of demand.
#   Slope check: (10 - 2) / (100 - 500) = 8 / -400 = -0.02 dollars per pound, so the inverse
#   demand curve is P = 12 - 0.02Q. Check at Q = 300: 12 - 6 = 6, which matches the table.
#   Choke price (Q = 0): P = 12. Maximum quantity (P = 0): Q = 600.
#
# Table verified: a 150-pound increase in quantity demanded at every price (an increase in
#   demand, that is, a rightward
#   shift). New quantity demanded = old + 150 at each price:
#     2 : 650, 4 : 550, 6 : 450, 8 : 350, 10 : 250.
#   Note that at the unchanged price of $6 the quantity demanded rises from 300 to 450,
#   which is a shift, not a movement along the original curve.

TOPIC = ("1.4", "Demand", 1)

DEM = dict(
    headers=["Price ($ per pound)", "Quantity demanded (pounds per week)"],
    rows=[["2", "500"], ["4", "400"], ["6", "300"], ["8", "200"], ["10", "100"]],
)

DEM2 = dict(
    headers=["Price ($ per pound)", "Original quantity demanded", "New quantity demanded"],
    rows=[["2", "500", "650"], ["4", "400", "550"], ["6", "300", "450"],
          ["8", "200", "350"], ["10", "100", "250"]],
)

QUESTIONS = [
 dict(q="The law of demand states that, other things equal,", choices=[
   "as the price of a good rises, the quantity demanded of that good falls",
   "as the price of a good rises, demand falls",
   "as income rises, demand rises",
   "as the price of a good rises, the quantity supplied falls",
   "price and quantity demanded move in the same direction"], ans=0,
   why="The law of demand is about quantity demanded and price moving in opposite directions."),
 dict(q="Demand refers to", choices=[
   "the amount consumers actually buy at the market price",
   "the entire relationship between price and the quantity consumers are willing and able to buy",
   "the amount consumers wish they could afford",
   "the amount producers offer for sale",
   "the equilibrium quantity"], ans=1,
   why="Demand is a whole schedule or curve, while quantity demanded is a single point on it."),
 dict(q="A demand curve is drawn holding constant everything except", choices=[
   "the price of the good itself",
   "consumer income",
   "the prices of related goods",
   "consumer tastes",
   "the number of buyers"], ans=0,
   why="Only the good's own price is allowed to vary along a demand curve; everything else is fixed."),
 dict(q="A change in the price of a good causes", choices=[
   "a shift of the demand curve",
   "a movement along the demand curve, that is, a change in quantity demanded",
   "a change in demand",
   "a shift of the supply curve only",
   "no change of any kind"], ans=1,
   why="The good's own price is on the axis, so a change in it moves you along the curve rather than shifting it."),
 dict(q="A change in consumer income causes", choices=[
   "a movement along the demand curve",
   "a shift of the demand curve",
   "a change in quantity demanded only",
   "a change in the price of the good with no other effect",
   "no change in the market"], ans=1,
   why="Income is one of the factors held constant when drawing the curve, so a change in it shifts the curve."),
 dict(q="An increase in demand is represented by", choices=[
   "a movement up along the demand curve",
   "a rightward shift of the demand curve",
   "a leftward shift of the demand curve",
   "a movement down along the demand curve",
   "a steepening of the demand curve"], ans=1,
   why="At every price consumers now want more, which places the whole curve farther right."),
 dict(q="A decrease in demand means that at every price consumers", choices=[
   "wish to buy more",
   "wish to buy less",
   "pay a higher price",
   "buy the same amount",
   "supply less"], ans=1,
   why="A decrease in demand shifts the curve left, lowering the quantity demanded at each price."),
 dict(q="Which of the following would cause a movement along the demand curve for gasoline rather than a shift?", choices=[
   "a rise in the price of gasoline itself",
   "an increase in consumer incomes",
   "a fall in the price of public transportation",
   "an expectation that gasoline prices will rise next month",
   "an increase in the number of drivers"], ans=0,
   why="A change in the good's own price is always a movement along the curve."),
 dict(q="For a normal good, an increase in consumer income causes", choices=[
   "demand to increase",
   "demand to decrease",
   "quantity demanded to fall with no shift",
   "the supply curve to shift",
   "no change"], ans=0,
   why="By definition a normal good is one consumers buy more of as income rises."),
 dict(q="For an inferior good, an increase in consumer income causes", choices=[
   "demand to increase",
   "demand to decrease",
   "a movement along the demand curve",
   "the price to rise with no other effect",
   "the supply curve to shift right"], ans=1,
   why="Consumers switch away from inferior goods as they can afford better substitutes."),
 dict(q="Which of the following is most likely an inferior good?", choices=[
   "restaurant meals",
   "generic instant noodles",
   "new automobiles",
   "airline travel",
   "smartphones"], ans=1,
   why="Consumers typically buy fewer of the cheapest staples as their incomes rise."),
 dict(q="During a recession in which incomes fall, demand for inferior goods will", choices=[
   "fall", "rise", "stay the same", "become vertical", "become horizontal"], ans=1,
   why="Falling income pushes consumers toward inferior goods, shifting their demand right."),
 dict(q="Two goods are substitutes if a rise in the price of one", choices=[
   "decreases demand for the other",
   "increases demand for the other",
   "has no effect on the other",
   "decreases quantity supplied of the other",
   "increases the price of the other's inputs"], ans=1,
   why="Consumers switch toward the now relatively cheaper alternative."),
 dict(q="Two goods are complements if a rise in the price of one", choices=[
   "increases demand for the other",
   "decreases demand for the other",
   "leaves the other unaffected",
   "increases the supply of the other",
   "lowers the cost of producing the other"], ans=1,
   why="Complements are consumed together, so buying less of one means wanting less of the other."),
 dict(q="An increase in the price of tea will most likely", choices=[
   "decrease the demand for coffee",
   "increase the demand for coffee",
   "decrease the quantity of coffee supplied",
   "have no effect on the coffee market",
   "shift the supply curve for coffee left"], ans=1,
   why="Tea and coffee are substitutes, so a costlier tea sends buyers toward coffee."),
 dict(q="An increase in the price of printers will most likely", choices=[
   "increase the demand for printer ink",
   "decrease the demand for printer ink",
   "increase the supply of printer ink",
   "leave the ink market unchanged",
   "raise the price of ink inputs"], ans=1,
   why="Printers and ink are complements, so fewer printers sold means less ink wanted at every price."),
 dict(q="If consumers expect the price of a good to rise sharply next month, current demand for the good will", choices=[
   "decrease", "increase", "stay the same", "become perfectly inelastic", "shift the supply curve"], ans=1,
   why="Buying now to avoid the higher future price raises demand today."),
 dict(q="If consumers expect their incomes to fall next year, current demand for normal goods will most likely", choices=[
   "increase", "decrease", "stay the same", "shift right", "become vertical"], ans=1,
   why="Expecting to be poorer, consumers cut back and save, lowering demand today."),
 dict(q="An increase in the number of buyers in a market causes", choices=[
   "a leftward shift of the demand curve",
   "a rightward shift of the demand curve",
   "a movement along the demand curve",
   "a leftward shift of the supply curve",
   "no change in demand"], ans=1,
   why="More buyers means more of the good is wanted at every price."),
 dict(q="A successful advertising campaign that makes a good more fashionable will", choices=[
   "shift the demand curve left",
   "shift the demand curve right",
   "cause a movement down the demand curve",
   "shift the supply curve right",
   "leave demand unchanged"], ans=1,
   why="A change in tastes toward the good raises the quantity wanted at every price."),
 dict(q="The substitution effect of a fall in the price of a good is that consumers", choices=[
   "buy less of the good because they feel poorer",
   "buy more of the good because it is now cheaper relative to other goods",
   "buy less of every good",
   "supply more labor",
   "save more"], ans=1,
   why="The substitution effect concerns relative prices, independent of purchasing power."),
 dict(q="The income effect of a fall in the price of a good is that consumers", choices=[
   "buy less because the good is relatively cheaper",
   "can afford more with the same money income, and so buy more of a normal good",
   "earn a higher wage",
   "receive a government transfer",
   "face a higher price level"], ans=1,
   why="A lower price raises real purchasing power, which acts like a small increase in income."),
 dict(q="Together the income and substitution effects explain why", choices=[
   "the supply curve slopes upward",
   "the demand curve slopes downward",
   "demand curves shift",
   "prices are sticky",
   "markets clear"], ans=1,
   why="Both effects push quantity demanded up when price falls, producing the negative slope."),
 dict(q="Using the demand schedule, the quantity demanded when the price is $8 per pound is", table=DEM, choices=[
   "100 pounds", "200 pounds", "300 pounds", "400 pounds", "500 pounds"], ans=1,
   why="Reading straight across from a price of $8 gives 200 pounds."),
 dict(q="Using the demand schedule, a rise in price from $4 to $8 changes quantity demanded by", table=DEM, choices=[
   "a fall of 100 pounds", "a fall of 200 pounds", "a rise of 200 pounds", "a fall of 400 pounds", "no change"], ans=1,
   why="Quantity demanded falls from 400 to 200 pounds, a decrease of 200."),
 dict(q="Using the demand schedule, each $2 increase in price reduces quantity demanded by", table=DEM, choices=[
   "50 pounds", "100 pounds", "200 pounds", "300 pounds", "400 pounds"], ans=1,
   why="The schedule falls by exactly 100 pounds for each $2 step, so the relationship is linear."),
 dict(q="Using the demand schedule, the movement from a price of $6 to a price of $4 is best described as", table=DEM, choices=[
   "an increase in demand",
   "an increase in quantity demanded caused by the lower price",
   "a decrease in demand",
   "a decrease in quantity demanded",
   "a shift of the demand curve"], ans=1,
   why="Only the good's own price changed, so this is a movement down along the same curve."),
 dict(q="Using the two-column comparison, the change from the original to the new schedule is", table=DEM2, choices=[
   "an increase in quantity demanded",
   "an increase in demand, since quantity demanded is 150 pounds higher at every price",
   "a decrease in demand",
   "a movement along the demand curve",
   "a change in supply"], ans=1,
   why="A change at every price, with the price itself unchanged, is a shift of the whole curve."),
 dict(q="Using the two-column comparison, at the unchanged price of $6 the quantity demanded rises from", table=DEM2, choices=[
   "200 to 350 pounds", "300 to 450 pounds", "400 to 550 pounds", "500 to 650 pounds", "100 to 250 pounds"], ans=1,
   why="Reading the $6 row gives 300 originally and 450 after the shift."),
 dict(q="Which of the following could have caused the shift shown in the two-column comparison for coffee?", table=DEM2, choices=[
   "a fall in the price of coffee",
   "an increase in the price of tea, a substitute for coffee",
   "a fall in consumer income, if coffee is normal",
   "an increase in the cost of growing coffee",
   "a decrease in the number of coffee drinkers"], ans=1,
   why="A costlier substitute raises demand for coffee at every price, which is exactly the shift shown."),
 dict(q="A demand curve for a normal good shifts right when income rises. This same curve would shift left if", choices=[
   "the good's own price rose",
   "income fell",
   "the number of buyers rose",
   "tastes shifted toward the good",
   "the price of a substitute rose"], ans=1,
   why="Falling income reduces what buyers want at every price for a normal good."),
 dict(q="Which of the following is NOT a determinant that shifts the demand curve?", choices=[
   "consumer income",
   "the price of the good itself",
   "the price of related goods",
   "consumer expectations",
   "the number of buyers"], ans=1,
   why="The good's own price is measured on the axis, so changing it moves along the curve."),
 dict(q="Market demand is obtained by", choices=[
   "adding the individual demand curves vertically",
   "adding the quantities demanded by all individual consumers at each price",
   "averaging the prices consumers pay",
   "multiplying price by quantity",
   "subtracting supply from demand"], ans=1,
   why="Market demand is the horizontal sum of individual quantities at each price."),
 dict(q="If the price of beef rises and the demand for chicken increases, then beef and chicken are", choices=[
   "complements", "substitutes", "inferior goods", "unrelated goods", "normal goods only"], ans=1,
   why="A rise in one good's price raising demand for the other is the definition of substitutes."),
 dict(q="If the price of hot dogs falls and the demand for hot dog buns increases, then the two goods are", choices=[
   "substitutes", "complements", "inferior goods", "unrelated", "identical"], ans=1,
   why="A fall in one good's price raising demand for the other identifies complements."),
 dict(q="An increase in the price of a good and a simultaneous increase in consumer income for a normal good will", choices=[
   "leave quantity demanded certainly higher",
   "have opposing effects, so the change in quantity demanded is indeterminate without more information",
   "leave quantity demanded certainly lower",
   "shift the supply curve",
   "have no effect at all"], ans=1,
   why="The higher price reduces quantity demanded while the higher income shifts demand right, so the net direction is unclear."),
 dict(q="A demand curve that is drawn steeply implies that", choices=[
   "quantity demanded responds a great deal to a price change",
   "quantity demanded responds relatively little to a price change",
   "demand has shifted",
   "the good is free",
   "supply is fixed"], ans=1,
   why="A steep curve means a large price change is needed to move quantity much."),
 dict(q="Which statement correctly distinguishes a change in demand from a change in quantity demanded?", choices=[
   "A change in demand is caused by the good's own price",
   "A change in demand shifts the whole curve, while a change in quantity demanded moves along it in response to the good's own price",
   "The two terms mean exactly the same thing",
   "A change in quantity demanded shifts the curve",
   "Neither involves price"], ans=1,
   why="The distinction is entirely about whether the good's own price or some other determinant changed."),
 dict(q="A newspaper reports that higher coffee prices have reduced coffee sales. The correct economic description is", choices=[
   "demand for coffee decreased",
   "quantity of coffee demanded decreased",
   "supply of coffee decreased",
   "demand for coffee increased",
   "the coffee market is in disequilibrium"], ans=1,
   why="Since the cause was coffee's own price, it is a movement along the demand curve."),
 dict(q="A report that warmer weather has made consumers want more ice cream at every price describes", choices=[
   "an increase in quantity demanded",
   "an increase in demand",
   "a decrease in demand",
   "a movement along the demand curve",
   "an increase in supply"], ans=1,
   why="A change in tastes affecting the quantity wanted at every price is a shift."),
 dict(q="Suppose bus fares rise. In the market for cars, this is most likely to", choices=[
   "decrease demand for cars",
   "increase demand for cars, since buses are a substitute",
   "decrease the supply of cars",
   "cause a movement along the demand curve for cars",
   "leave the car market unchanged"], ans=1,
   why="A more expensive substitute drives consumers toward the alternative."),
 dict(q="A drop in the price of electricity will most likely, in the market for electric heaters,", choices=[
   "decrease demand",
   "increase demand, since electricity and heaters are complements",
   "cause a movement along the heater demand curve",
   "decrease supply",
   "have no effect"], ans=1,
   why="Cheaper electricity makes owning a heater cheaper overall, so more are wanted at every price."),
 dict(q="An increase in demand accompanied by no change in supply will, in a competitive market,", choices=[
   "lower both price and quantity",
   "raise both the equilibrium price and the equilibrium quantity",
   "raise price and lower quantity",
   "lower price and raise quantity",
   "leave price and quantity unchanged"], ans=1,
   why="A rightward demand shift moves along the upward-sloping supply curve to a higher price and quantity."),
 dict(q="A decrease in demand with supply unchanged will", choices=[
   "raise both price and quantity",
   "lower both the equilibrium price and the equilibrium quantity",
   "raise price and lower quantity",
   "lower price and raise quantity",
   "leave the market unchanged"], ans=1,
   why="A leftward demand shift slides down the supply curve to a lower price and quantity."),
 dict(q="Which of the following would shift the demand curve for new houses to the right?", choices=[
   "a rise in mortgage interest rates",
   "an increase in household income and a growing population",
   "an increase in the price of new houses",
   "an increase in the cost of lumber",
   "a fall in the number of households"], ans=1,
   why="Higher income and more buyers both raise the quantity wanted at every price."),
 dict(q="An unexpected rise in the price of a good, if consumers believe it signals further increases, may temporarily", choices=[
   "reduce demand",
   "increase demand, because the expectation of higher future prices shifts the curve right",
   "flatten the supply curve",
   "eliminate the market",
   "have no effect on expectations"], ans=1,
   why="Expectations are a separate shifter, and they can pull in the opposite direction from the price change itself."),
 dict(q="Which of these best describes a normal good?", choices=[
   "a good with a horizontal demand curve",
   "a good whose demand rises when income rises",
   "a good whose demand falls when income rises",
   "a good with no substitutes",
   "a good produced by the government"], ans=1,
   why="Normal and inferior are defined entirely by the direction of the response to income."),
 dict(q="If demand for a good increases when the price of another good increases, and also increases when income increases, the good is", choices=[
   "an inferior good and a complement",
   "a normal good and a substitute for the other good",
   "an inferior good and a substitute",
   "a normal good and a complement",
   "unrelated to income or other prices"], ans=1,
   why="Rising with income makes it normal, and rising with a rival's price makes it a substitute."),
 dict(q="At a price above the choke price where quantity demanded reaches zero,", choices=[
   "demand shifts right",
   "no consumer is willing to buy the good",
   "quantity demanded is negative",
   "supply must be zero",
   "the demand curve becomes upward sloping"], ans=1,
   why="The choke price is the price at which the demand curve reaches the vertical axis."),
 dict(q="Which of the following changes would cause both a movement along the demand curve for coffee and a shift of the demand curve for tea?", choices=[
   "an increase in the price of sugar",
   "an increase in the price of coffee",
   "an increase in the number of tea drinkers",
   "an improvement in coffee-growing technology only",
   "a change in consumer tastes for tea"], ans=1,
   why="Coffee's own price moves along coffee's curve, and because tea is a substitute it shifts tea's curve."),
]
