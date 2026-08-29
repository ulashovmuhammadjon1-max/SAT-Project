# MACRO 1.5 Supply — 50 questions
#
# Table verified: supply schedule for wheat (a single market, per month).
#   Price ($ per bushel) : Quantity supplied (bushels)
#     2 : 100
#     4 : 200
#     6 : 300
#     8 : 400
#    10 : 500
#   Every $2 rise in price raises quantity supplied by exactly 100 bushels, so the schedule
#   is linear and upward sloping, consistent with the law of supply.
#   Slope check: (10 - 2) / (500 - 100) = 8 / 400 = 0.02 dollars per bushel, so the inverse
#   supply curve is P = 0.02Q. Check at Q = 300: 0.02 x 300 = 6, which matches the table.
#   At P = 0 the quantity supplied is 0, so this supply curve passes through the origin.
#
# Table verified: an increase in supply of 120 bushels at every price (a rightward shift),
#   caused for example by a better harvesting technology. New quantity supplied = old + 120:
#     2 : 220, 4 : 320, 6 : 420, 8 : 520, 10 : 620.
#   At the unchanged price of $6 the quantity supplied rises from 300 to 420 bushels, which
#   is a shift of the curve and not a movement along it.

TOPIC = ("1.5", "Supply", 1)

SUP = dict(
    headers=["Price ($ per bushel)", "Quantity supplied (bushels per month)"],
    rows=[["2", "100"], ["4", "200"], ["6", "300"], ["8", "400"], ["10", "500"]],
)

SUP2 = dict(
    headers=["Price ($ per bushel)", "Original quantity supplied", "New quantity supplied"],
    rows=[["2", "100", "220"], ["4", "200", "320"], ["6", "300", "420"],
          ["8", "400", "520"], ["10", "500", "620"]],
)

QUESTIONS = [
 dict(q="The law of supply states that, other things equal,", choices=[
   "as the price of a good rises, the quantity supplied of that good rises",
   "as the price of a good rises, supply rises",
   "as costs rise, supply rises",
   "as the price of a good rises, the quantity supplied falls",
   "price and quantity supplied are unrelated"], ans=0,
   why="Higher prices make production more profitable, so producers offer more units for sale."),
 dict(q="Supply refers to", choices=[
   "the quantity a firm actually sells",
   "the entire relationship between price and the quantity producers are willing and able to sell",
   "the amount of a good in existence",
   "the amount consumers wish to buy",
   "the equilibrium quantity"], ans=1,
   why="Supply is a whole schedule, while quantity supplied is one point on it."),
 dict(q="The supply curve slopes upward mainly because", choices=[
   "consumers buy less at higher prices",
   "a higher price makes it worthwhile to bear the higher marginal cost of producing extra units",
   "firms enjoy raising prices",
   "governments require it",
   "resources are unlimited"], ans=1,
   why="Producing more units usually costs more per unit, so only a higher price justifies expanding output."),
 dict(q="A change in the price of a good itself causes", choices=[
   "a shift of the supply curve",
   "a movement along the supply curve, that is, a change in quantity supplied",
   "a change in supply",
   "a shift of the demand curve only",
   "no change of any kind"], ans=1,
   why="The good's own price is on the axis, so a change in it moves you along the supply curve."),
 dict(q="An increase in supply is represented by", choices=[
   "a movement up along the supply curve",
   "a rightward shift of the supply curve",
   "a leftward shift of the supply curve",
   "a movement down along the supply curve",
   "a vertical supply curve"], ans=1,
   why="At every price producers now offer more, which places the whole curve farther right."),
 dict(q="A decrease in supply means that at every price producers", choices=[
   "offer more for sale",
   "offer less for sale",
   "charge a higher price",
   "produce the same amount",
   "demand more inputs"], ans=1,
   why="A leftward shift lowers the quantity supplied at each price."),
 dict(q="An increase in the price of an input used to produce a good will", choices=[
   "increase supply",
   "decrease supply, shifting the curve left",
   "cause a movement along the supply curve",
   "increase demand",
   "leave supply unchanged"], ans=1,
   why="Higher production costs make each unit less profitable, so less is offered at every price."),
 dict(q="A fall in the wage rate paid by a firm will, in the market for its product,", choices=[
   "shift the supply curve left",
   "shift the supply curve right",
   "cause a movement up along the supply curve",
   "shift the demand curve right",
   "have no effect on supply"], ans=1,
   why="Lower input costs raise profitability at every price, so more is supplied."),
 dict(q="An improvement in production technology will", choices=[
   "shift the supply curve left",
   "shift the supply curve right, since more can be produced from the same inputs",
   "cause a movement along the supply curve",
   "shift the demand curve left",
   "raise the cost per unit"], ans=1,
   why="Better technology lowers unit cost, which raises the quantity offered at every price."),
 dict(q="An increase in the number of firms selling in a market will", choices=[
   "decrease market supply",
   "increase market supply",
   "cause a movement along the market supply curve",
   "decrease market demand",
   "leave market supply unchanged"], ans=1,
   why="Market supply is the sum of individual supplies, so more sellers means more offered at every price."),
 dict(q="If producers expect the price of their product to be much higher next month, current supply will most likely", choices=[
   "increase",
   "decrease, as producers hold back inventory to sell later",
   "stay exactly the same",
   "become perfectly elastic",
   "shift the demand curve"], ans=1,
   why="Withholding output for a better future price reduces what is offered today."),
 dict(q="A per-unit tax imposed on producers of a good will", choices=[
   "shift the supply curve right",
   "shift the supply curve left, since the tax adds to the cost of each unit",
   "cause a movement along the supply curve",
   "shift the demand curve left",
   "have no effect on supply"], ans=1,
   why="A tax raises the effective cost of production, so less is supplied at every price."),
 dict(q="A government subsidy paid to producers per unit of output will", choices=[
   "shift the supply curve left",
   "shift the supply curve right, since it lowers the net cost of each unit",
   "cause a movement down the supply curve",
   "shift the demand curve right",
   "leave supply unchanged"], ans=1,
   why="A subsidy is the mirror image of a tax and increases supply."),
 dict(q="Using the supply schedule, the quantity supplied when the price is $8 per bushel is", table=SUP, choices=[
   "100 bushels", "200 bushels", "300 bushels", "400 bushels", "500 bushels"], ans=3,
   why="Reading straight across from a price of $8 gives 400 bushels."),
 dict(q="Using the supply schedule, a fall in price from $10 to $4 changes quantity supplied by", table=SUP, choices=[
   "a fall of 100 bushels", "a fall of 200 bushels", "a fall of 300 bushels", "a rise of 300 bushels", "no change"], ans=2,
   why="Quantity supplied falls from 500 to 200 bushels, a decrease of 300."),
 dict(q="Using the supply schedule, each $2 increase in price raises quantity supplied by", table=SUP, choices=[
   "50 bushels", "100 bushels", "200 bushels", "300 bushels", "400 bushels"], ans=1,
   why="The schedule rises by exactly 100 bushels for each $2 step, so the relationship is linear."),
 dict(q="Using the supply schedule, the change from a price of $4 to a price of $6 is best described as", table=SUP, choices=[
   "an increase in supply",
   "an increase in quantity supplied caused by the higher price",
   "a decrease in supply",
   "a decrease in quantity supplied",
   "a shift of the supply curve"], ans=1,
   why="Only the good's own price changed, so this is a movement up along the same curve."),
 dict(q="In the wheat table comparing the original and new quantities offered at each price, the change shown is", table=SUP2, choices=[
   "an increase in quantity supplied",
   "an increase in supply, since quantity supplied is 120 bushels higher at every price",
   "a decrease in supply",
   "a movement along the supply curve",
   "a change in demand"], ans=1,
   why="A change at every price, with price itself unchanged, is a shift of the whole curve."),
 dict(q="Using the two-column comparison, at the unchanged price of $6 the quantity supplied rises from", table=SUP2, choices=[
   "100 to 220 bushels", "200 to 320 bushels", "300 to 420 bushels", "400 to 520 bushels", "500 to 620 bushels"], ans=2,
   why="Reading the $6 row gives 300 originally and 420 after the shift."),
 dict(q="What could have caused the wheat producers to offer 120 more bushels at every price?", table=SUP2, choices=[
   "a rise in the price of wheat",
   "a new harvesting technology that lowers cost per bushel",
   "a drought that destroys part of the crop",
   "a per-unit tax on wheat producers",
   "a decrease in the number of wheat farms"], ans=1,
   why="Only a fall in unit cost or an increase in sellers would raise the quantity supplied at every price."),
 dict(q="Which of the following causes a movement along the supply curve rather than a shift?", choices=[
   "a change in input prices",
   "a change in the market price of the good",
   "a change in technology",
   "a change in the number of sellers",
   "a change in producer expectations"], ans=1,
   why="Only the good's own price moves you along the curve; every other determinant shifts it."),
 dict(q="Which of the following is NOT a supply shifter?", choices=[
   "input prices",
   "the price of the good itself",
   "technology",
   "the number of sellers",
   "producer expectations"], ans=1,
   why="The good's own price is measured on the axis, so it produces a movement along the curve."),
 dict(q="A severe drought in a wheat-growing region will", choices=[
   "shift the supply curve for wheat right",
   "shift the supply curve for wheat left",
   "cause a movement down the supply curve",
   "shift the demand curve for wheat right",
   "leave the wheat market unchanged"], ans=1,
   why="Destroyed crops reduce what can be offered at every price."),
 dict(q="Market supply is obtained by", choices=[
   "adding individual supply curves vertically",
   "adding the quantities supplied by all sellers at each price",
   "averaging the prices firms charge",
   "multiplying price by quantity",
   "subtracting demand from supply"], ans=1,
   why="Market supply is the horizontal sum of individual quantities at each price."),
 dict(q="If a firm produces both wheat and barley on the same land, a rise in the price of barley will", choices=[
   "increase the supply of wheat",
   "decrease the supply of wheat, as land is switched to the more profitable crop",
   "cause a movement along the wheat supply curve",
   "increase the demand for wheat",
   "have no effect on the wheat market"], ans=1,
   why="Goods that compete for the same resources are substitutes in production, so a better price for one draws resources from the other."),
 dict(q="Beef and leather are produced together from the same animal. A rise in the price of beef will most likely", choices=[
   "decrease the supply of leather",
   "increase the supply of leather",
   "cause a movement down the leather supply curve",
   "decrease the demand for leather",
   "leave the leather market unchanged"], ans=1,
   why="They are complements in production, so producing more beef automatically yields more leather."),
 dict(q="A supply curve drawn steeply implies that", choices=[
   "quantity supplied responds a great deal to a price change",
   "quantity supplied responds relatively little to a price change",
   "supply has shifted",
   "costs are zero",
   "demand is fixed"], ans=1,
   why="A steep curve means a large price change produces only a small change in quantity supplied."),
 dict(q="A perfectly inelastic supply curve is", choices=[
   "horizontal",
   "vertical, because the quantity supplied is fixed regardless of price",
   "downward sloping",
   "upward sloping at a 45 degree angle",
   "impossible to draw"], ans=1,
   why="A fixed quantity, such as seats in a stadium tonight, does not respond to price at all."),
 dict(q="Which of the following would shift the supply curve for automobiles to the right?", choices=[
   "an increase in steel prices",
   "a robotics advance that lowers assembly costs",
   "a new tax on automobile manufacturers",
   "a decrease in the number of automobile plants",
   "an increase in the price of automobiles"], ans=1,
   why="Lower unit cost raises the quantity offered at every price."),
 dict(q="Which of the following would shift the supply curve for automobiles to the left?", choices=[
   "a fall in steel prices",
   "a sharp increase in autoworker wages",
   "a new production technology",
   "a producer subsidy",
   "an increase in consumer income"], ans=1,
   why="Higher input costs reduce the quantity offered at every price."),
 dict(q="A report that higher wheat prices have led farmers to plant more wheat describes", choices=[
   "an increase in supply",
   "an increase in quantity supplied",
   "a decrease in supply",
   "a decrease in demand",
   "a shift of the supply curve"], ans=1,
   why="The cause was the good's own price, so it is a movement along the supply curve."),
 dict(q="A report that a new fertilizer allows farmers to grow more wheat on the same land at every price describes", choices=[
   "an increase in quantity supplied",
   "an increase in supply",
   "a decrease in supply",
   "a movement along the supply curve",
   "an increase in demand"], ans=1,
   why="A technology change affecting output at every price is a shift of the curve."),
 dict(q="An increase in supply with demand unchanged will, in a competitive market,", choices=[
   "raise both price and quantity",
   "lower the equilibrium price and raise the equilibrium quantity",
   "raise price and lower quantity",
   "lower both price and quantity",
   "leave the market unchanged"], ans=1,
   why="A rightward supply shift slides down the demand curve to a lower price and larger quantity."),
 dict(q="A decrease in supply with demand unchanged will", choices=[
   "lower both price and quantity",
   "raise the equilibrium price and lower the equilibrium quantity",
   "raise both price and quantity",
   "lower price and raise quantity",
   "leave the market unchanged"], ans=1,
   why="A leftward supply shift moves up the demand curve to a higher price and smaller quantity."),
 dict(q="The main difference between a change in supply and a change in quantity supplied is that", choices=[
   "a change in supply is caused by the good's own price",
   "a change in supply shifts the whole curve, while a change in quantity supplied is a movement along it caused by the good's own price",
   "the two terms mean the same thing",
   "a change in quantity supplied shifts the curve",
   "neither involves price"], ans=1,
   why="The distinction turns entirely on whether the good's own price or another determinant changed."),
 dict(q="A firm's supply decision is based on comparing", choices=[
   "total revenue with total assets",
   "the price it receives with the marginal cost of producing another unit",
   "its price with its competitors' advertising",
   "consumer income with the good's price",
   "average revenue with fixed cost only"], ans=1,
   why="Producing another unit is worthwhile when the price at least covers the extra cost."),
 dict(q="A regulation that requires costly new emissions equipment on factories will", choices=[
   "increase supply in the affected industry",
   "decrease supply in the affected industry",
   "increase demand for the industry's product",
   "cause a movement along the supply curve",
   "have no effect on production costs"], ans=1,
   why="A regulation that raises unit cost reduces the quantity offered at every price."),
 dict(q="A fall in the price of oil, an input for plastics manufacturers, will in the plastics market", choices=[
   "shift supply left and raise price",
   "shift supply right and lower price",
   "shift demand right",
   "cause a movement up the supply curve",
   "leave the market unchanged"], ans=1,
   why="Cheaper inputs raise supply, and a rightward supply shift lowers the equilibrium price."),
 dict(q="If both an increase in wages and an improvement in technology occur in the same industry, the net effect on supply is", choices=[
   "certainly an increase",
   "indeterminate, since the two changes push supply in opposite directions",
   "certainly a decrease",
   "a movement along the supply curve",
   "zero by definition"], ans=1,
   why="Higher wages shift supply left and better technology shifts it right, so the net direction depends on their relative sizes."),
 dict(q="In the short run, a firm can most easily expand output by", choices=[
   "building a new factory",
   "using its existing plant more intensively, for example with overtime hours",
   "changing its industry",
   "reducing its capital stock",
   "waiting for new firms to enter"], ans=1,
   why="Some inputs are fixed in the short run, so extra output comes from varying the flexible ones."),
 dict(q="Supply tends to be more elastic in the long run than in the short run because", choices=[
   "consumers become more sensitive to price",
   "firms have time to adjust plant size and new firms can enter the market",
   "input prices never change",
   "demand becomes vertical",
   "governments intervene"], ans=1,
   why="Given time, every input becomes variable, so quantity supplied can respond more fully to price."),
 dict(q="An unexpected freeze destroys half of a country's orange crop. In the market for oranges this is", choices=[
   "a decrease in quantity supplied",
   "a decrease in supply",
   "an increase in supply",
   "an increase in demand",
   "a movement along the supply curve"], ans=1,
   why="Fewer oranges are available at every price, so the whole curve shifts left."),
 dict(q="Which statement about the relationship between cost and supply is correct?", choices=[
   "Lower production costs shift supply left",
   "Lower production costs shift supply right",
   "Costs have no effect on supply",
   "Costs shift the demand curve",
   "Higher costs cause a movement down the supply curve"], ans=1,
   why="Falling unit costs make production profitable at lower prices, expanding supply."),
 dict(q="If a firm's supply curve is upward sloping, then at a price of $10 the firm supplies more than at a price of $6 because", choices=[
   "consumers demand more",
   "the higher price covers the higher marginal cost of the additional units",
   "the firm's fixed costs fall",
   "technology improves at higher prices",
   "input prices fall automatically"], ans=1,
   why="The extra units are worth producing only once the price covers what they cost to make."),
 dict(q="Which of the following pairs of events would both increase the supply of coffee?", choices=[
   "a rise in the wages of coffee pickers and a new tax on growers",
   "an improved drying technology and an increase in the number of coffee farms",
   "a drought and a producer subsidy",
   "a rise in the price of coffee and an increase in demand",
   "a decrease in the number of sellers and higher input prices"], ans=1,
   why="Both a cost-reducing technology and additional sellers raise the quantity offered at every price."),
 dict(q="A producer subsidy of $1 per unit will shift the supply curve", choices=[
   "left by $1 measured vertically",
   "right, and vertically downward by $1 at every quantity",
   "right, and vertically upward by $1",
   "not at all",
   "into a vertical line"], ans=1,
   why="The subsidy lowers the price a producer needs to receive for each unit by exactly $1."),
 dict(q="A per-unit excise tax of $2 collected from sellers shifts the supply curve", choices=[
   "right by $2 measured vertically",
   "left, and vertically upward by $2 at every quantity",
   "left, and vertically downward by $2",
   "not at all",
   "into a horizontal line"], ans=1,
   why="Sellers now require $2 more per unit to offer the same quantity."),
 dict(q="Which of the following would cause the supply curve for solar panels to shift right and the demand curve to remain unchanged?", choices=[
   "a rise in household income",
   "a fall in the price of the silicon used to make panels",
   "a government rebate paid to panel buyers",
   "an increase in electricity prices",
   "a change in consumer tastes toward solar power"], ans=1,
   why="A cheaper input affects sellers' costs only, leaving the demand side untouched."),
 dict(q="If producers of a good expect its price to fall sharply next year, current supply will most likely", choices=[
   "decrease",
   "increase, as producers sell now rather than later",
   "stay the same",
   "become perfectly inelastic",
   "shift the demand curve left"], ans=1,
   why="Expecting a worse price later gives producers a reason to bring output to market today."),
 dict(q="An economy-wide fall in energy prices affects most industries by", choices=[
   "shifting supply curves left and raising prices",
   "shifting supply curves right and putting downward pressure on prices",
   "shifting demand curves left",
   "causing movements along supply curves only",
   "leaving costs unchanged"], ans=1,
   why="Energy is an input almost everywhere, so cheaper energy lowers unit costs across the economy."),
]
