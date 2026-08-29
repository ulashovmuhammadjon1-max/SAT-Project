# MACRO 1.6 Market Equilibrium, Disequilibrium, and Changes in Equilibrium — 50 questions
#
# Table verified: market for apples (thousands of bushels per month).
#   Price ($) : Quantity demanded : Quantity supplied : Qd - Qs
#      1 :  900 :  200 :  +700  -> shortage of 700
#      2 :  750 :  400 :  +350  -> shortage of 350
#      3 :  600 :  600 :     0  -> EQUILIBRIUM
#      4 :  450 :  800 :  -350  -> surplus of 350
#      5 :  300 : 1000 :  -700  -> surplus of 700
#   Demand is linear: each $1 rise lowers Qd by 150 (900, 750, 600, 450, 300).
#   Supply is linear: each $1 rise raises Qs by 200 (200, 400, 600, 800, 1000).
#   Qd = Qs requires 1050 - 150P = 200P, so 1050 = 350P and P = 3; then Q = 200 x 3 = 600
#   and Qd = 1050 - 450 = 600. The two agree, so equilibrium is P = $3, Q = 600.
#   Check of one disequilibrium row: at P = 4, Qs - Qd = 800 - 450 = 350, a surplus of 350.
#
# The four single-shift results, each derived by sliding along the unchanged curve:
#   demand increases, supply unchanged  ->  P up,   Q up
#   demand decreases, supply unchanged  ->  P down, Q down
#   supply increases, demand unchanged  ->  P down, Q up
#   supply decreases, demand unchanged  ->  P up,   Q down
#
# The four double-shift results. In each case one variable is determined and the other
# depends on which shift is larger, so it is indeterminate:
#   demand up,   supply up    ->  Q rises,  P indeterminate
#   demand down, supply down  ->  Q falls,  P indeterminate
#   demand up,   supply down  ->  P rises,  Q indeterminate
#   demand down, supply up    ->  P falls,  Q indeterminate
#   The rule: when the two curves shift in the SAME direction, quantity is determined and
#   price is not; when they shift in OPPOSITE directions, price is determined and quantity
#   is not.

TOPIC = ("1.6", "Market Equilibrium, Disequilibrium, and Changes in Equilibrium", 1)

MKT = dict(
    headers=["Price ($ per bushel)", "Quantity demanded (thousands)", "Quantity supplied (thousands)"],
    rows=[["1", "900", "200"], ["2", "750", "400"], ["3", "600", "600"],
          ["4", "450", "800"], ["5", "300", "1000"]],
)

QUESTIONS = [
 dict(q="Market equilibrium occurs at the price and quantity where", choices=[
   "quantity demanded exceeds quantity supplied",
   "quantity demanded equals quantity supplied",
   "quantity supplied exceeds quantity demanded",
   "the government sets the price",
   "producers earn the highest possible profit"], ans=1,
   why="At equilibrium there is no shortage and no surplus, so there is no pressure on price to change."),
 dict(q="The equilibrium price is often called the market-clearing price because at that price", choices=[
   "every producer earns a profit",
   "everyone willing to buy at that price finds a seller and everyone willing to sell finds a buyer",
   "the government approves it",
   "the price cannot change again",
   "quantity demanded is at its maximum"], ans=1,
   why="Nothing is left over and nobody willing to trade at that price is turned away."),
 dict(q="Using the market table, the equilibrium price and quantity are", table=MKT, choices=[
   "$1 and 900 thousand bushels",
   "$2 and 750 thousand bushels",
   "$3 and 600 thousand bushels",
   "$4 and 800 thousand bushels",
   "$5 and 1,000 thousand bushels"], ans=2,
   why="At $3 quantity demanded and quantity supplied are both 600 thousand bushels."),
 dict(q="Using the market table, at a price of $2 the market experiences a", table=MKT, choices=[
   "surplus of 350 thousand bushels",
   "shortage of 350 thousand bushels",
   "shortage of 750 thousand bushels",
   "surplus of 400 thousand bushels",
   "market-clearing outcome"], ans=1,
   why="Quantity demanded of 750 exceeds quantity supplied of 400, leaving 350 thousand bushels unfilled."),
 dict(q="Using the market table, at a price of $5 the market experiences a", table=MKT, choices=[
   "shortage of 700 thousand bushels",
   "surplus of 700 thousand bushels",
   "surplus of 300 thousand bushels",
   "shortage of 300 thousand bushels",
   "market-clearing outcome"], ans=1,
   why="Quantity supplied of 1,000 exceeds quantity demanded of 300, leaving 700 thousand bushels unsold."),
 dict(q="Using the market table, at a price of $1 the size of the shortage is", table=MKT, choices=[
   "200 thousand bushels", "350 thousand bushels", "600 thousand bushels", "700 thousand bushels", "900 thousand bushels"], ans=3,
   why="Quantity demanded of 900 minus quantity supplied of 200 leaves a shortage of 700 thousand."),
 dict(q="Using the market table, at a price of $4 the size of the surplus is", table=MKT, choices=[
   "150 thousand bushels", "350 thousand bushels", "450 thousand bushels", "700 thousand bushels", "800 thousand bushels"], ans=1,
   why="Quantity supplied of 800 minus quantity demanded of 450 leaves 350 thousand bushels unsold."),
 dict(q="A shortage occurs when the price is", choices=[
   "above the equilibrium price",
   "below the equilibrium price",
   "at the equilibrium price",
   "zero",
   "set by producers"], ans=1,
   why="A low price encourages buying and discourages producing, so quantity demanded exceeds quantity supplied."),
 dict(q="A surplus occurs when the price is", choices=[
   "below the equilibrium price",
   "above the equilibrium price",
   "at the equilibrium price",
   "negative",
   "set by consumers"], ans=1,
   why="A high price encourages production and discourages buying, so goods go unsold."),
 dict(q="When a shortage exists in a competitive market, the price tends to", choices=[
   "fall until the surplus disappears",
   "rise, which reduces quantity demanded and raises quantity supplied until the shortage is eliminated",
   "stay the same",
   "rise permanently without limit",
   "be set by the government"], ans=1,
   why="Frustrated buyers bid the price up, and both sides of the market respond until the gap closes."),
 dict(q="When a surplus exists in a competitive market, the price tends to", choices=[
   "rise until the shortage disappears",
   "fall, which raises quantity demanded and lowers quantity supplied until the surplus is eliminated",
   "stay the same",
   "fall to zero",
   "be fixed by sellers"], ans=1,
   why="Sellers with unsold inventory cut prices, and both sides adjust until the market clears."),
 dict(q="Using the market table, if the current price is $4, market forces will push the price", table=MKT, choices=[
   "up toward $5",
   "down toward $3, where the surplus disappears",
   "up toward $3",
   "to zero",
   "nowhere, since $4 is equilibrium"], ans=1,
   why="A surplus of 350 thousand bushels pushes sellers to cut price until quantity demanded and supplied meet at $3."),
 dict(q="Using the market table, if the current price is $1, market forces will push the price", table=MKT, choices=[
   "down toward zero",
   "up toward $3, where the shortage disappears",
   "down toward $2",
   "up toward $5",
   "nowhere, since $1 is equilibrium"], ans=1,
   why="A shortage of 700 thousand bushels leads buyers to bid the price up until the market clears at $3."),
 dict(q="An increase in demand with supply unchanged causes", choices=[
   "price to rise and quantity to fall",
   "price to rise and quantity to rise",
   "price to fall and quantity to rise",
   "price to fall and quantity to fall",
   "no change in price or quantity"], ans=1,
   why="A rightward demand shift creates a shortage at the old price, and the market clears at a higher price and larger quantity."),
 dict(q="A decrease in demand with supply unchanged causes", choices=[
   "price to rise and quantity to rise",
   "price to fall and quantity to fall",
   "price to fall and quantity to rise",
   "price to rise and quantity to fall",
   "no change in either variable"], ans=1,
   why="A leftward demand shift creates a surplus at the old price, and the market clears lower on the supply curve."),
 dict(q="An increase in supply with demand unchanged causes", choices=[
   "price to rise and quantity to rise",
   "price to fall and quantity to rise",
   "price to fall and quantity to fall",
   "price to rise and quantity to fall",
   "no change in either variable"], ans=1,
   why="A rightward supply shift creates a surplus at the old price, and the market clears further down the demand curve."),
 dict(q="A decrease in supply with demand unchanged causes", choices=[
   "price to fall and quantity to fall",
   "price to rise and quantity to fall",
   "price to rise and quantity to rise",
   "price to fall and quantity to rise",
   "no change in either variable"], ans=1,
   why="A leftward supply shift creates a shortage at the old price, and the market clears higher up the demand curve."),
 dict(q="If both demand and supply increase, the equilibrium quantity", choices=[
   "falls",
   "rises, while the change in price is indeterminate",
   "is indeterminate, while price rises",
   "is unchanged",
   "rises, and price certainly rises as well"], ans=1,
   why="Both shifts push quantity up, but they push price in opposite directions, so price depends on the relative sizes."),
 dict(q="If both demand and supply decrease, the equilibrium quantity", choices=[
   "rises",
   "falls, while the change in price is indeterminate",
   "is indeterminate, while price falls",
   "is unchanged",
   "falls, and price certainly falls as well"], ans=1,
   why="Both shifts pull quantity down, while one pushes price up and the other pulls it down."),
 dict(q="If demand increases and supply decreases, the equilibrium price", choices=[
   "falls",
   "rises, while the change in quantity is indeterminate",
   "is indeterminate, while quantity rises",
   "is unchanged",
   "rises, and quantity certainly rises as well"], ans=1,
   why="Both shifts push price up, but one raises quantity and the other lowers it."),
 dict(q="If demand decreases and supply increases, the equilibrium price", choices=[
   "rises",
   "falls, while the change in quantity is indeterminate",
   "is indeterminate, while quantity falls",
   "is unchanged",
   "falls, and quantity certainly falls as well"], ans=1,
   why="Both shifts push price down, but one lowers quantity and the other raises it."),
 dict(q="The general rule for double shifts is that", choices=[
   "both price and quantity are always indeterminate",
   "when the curves shift in the same direction quantity is determined and price is not, and when they shift in opposite directions price is determined and quantity is not",
   "price is always determined and quantity never is",
   "quantity is always determined and price never is",
   "double shifts cancel out completely"], ans=1,
   why="The variable both shifts push the same way is determined, and the other depends on the relative sizes of the shifts."),
 dict(q="Demand increases by a large amount while supply increases by a small amount. The equilibrium price will", choices=[
   "fall", "rise", "be unchanged", "be indeterminate even with this information", "fall to zero"], ans=1,
   why="Knowing the demand shift is larger resolves the ambiguity, and the larger demand increase dominates."),
 dict(q="Demand increases by a small amount while supply increases by a large amount. The equilibrium price will", choices=[
   "rise", "fall", "be unchanged", "remain indeterminate", "double"], ans=1,
   why="The larger supply increase dominates, pushing price down even though demand rose."),
 dict(q="Demand and supply both increase by exactly the same amount at every price. The equilibrium price will", choices=[
   "rise", "fall", "be unchanged, while quantity rises", "be unchanged, while quantity falls", "become zero"], ans=2,
   why="Equal and opposite pressures on price cancel, but both shifts raise the quantity traded."),
 dict(q="A hurricane destroys much of the orange crop while a health report simultaneously increases consumer interest in orange juice. In the orange market,", choices=[
   "price falls and quantity rises",
   "price rises while the change in quantity is indeterminate",
   "quantity rises while price is indeterminate",
   "both price and quantity fall",
   "nothing changes"], ans=1,
   why="Supply falls and demand rises, so both push price up while pulling quantity in opposite directions."),
 dict(q="New drilling technology raises oil output at the same time that a global recession reduces demand for oil. The equilibrium price of oil will", choices=[
   "rise",
   "fall, while the change in quantity is indeterminate",
   "be unchanged",
   "fall, and quantity will certainly rise",
   "rise, and quantity will certainly fall"], ans=1,
   why="Supply increases and demand decreases, so both push price down while pulling quantity in opposite directions."),
 dict(q="A rise in household income and a fall in the cost of producing smartphones occur together. The equilibrium quantity of smartphones will", choices=[
   "fall",
   "rise, while the change in price is indeterminate",
   "be unchanged",
   "rise, and price will certainly rise",
   "rise, and price will certainly fall"], ans=1,
   why="Demand and supply both increase, which raises quantity for certain but leaves price ambiguous."),
 dict(q="A market is initially in equilibrium. If the price is then fixed by law below equilibrium, the result is", choices=[
   "a persistent surplus",
   "a persistent shortage",
   "a return to equilibrium",
   "a higher equilibrium quantity",
   "no effect on the market"], ans=1,
   why="A binding price ceiling keeps price below the clearing level, so quantity demanded stays above quantity supplied."),
 dict(q="A market is initially in equilibrium. If the price is then fixed by law above equilibrium, the result is", choices=[
   "a persistent shortage",
   "a persistent surplus",
   "a return to equilibrium",
   "a lower equilibrium price",
   "no effect on the market"], ans=1,
   why="A binding price floor keeps price above the clearing level, so quantity supplied stays above quantity demanded."),
 dict(q="Using the market table, suppose demand rises so that quantity demanded is 200 thousand bushels higher at every price. The new equilibrium price will be", table=MKT, choices=[
   "below $3", "exactly $3", "above $3", "zero", "impossible to determine"], ans=2,
   why="At the old price of $3 quantity demanded would be 800 against 600 supplied, a shortage that pushes price up."),
 dict(q="Using the market table, suppose supply rises so that quantity supplied is 200 thousand bushels higher at every price. The new equilibrium price will be", table=MKT, choices=[
   "above $3", "exactly $3", "below $3", "above $5", "impossible to determine"], ans=2,
   why="At the old price of $3 quantity supplied would be 800 against 600 demanded, a surplus that pushes price down."),
 dict(q="Disequilibrium in a market means that", choices=[
   "the price has been set by the government",
   "quantity demanded and quantity supplied are not equal at the current price",
   "the market has no supply curve",
   "profits are zero",
   "consumers are irrational"], ans=1,
   why="Any price other than the market-clearing price leaves a shortage or a surplus."),
 dict(q="The quantity actually traded when a shortage exists equals", choices=[
   "quantity demanded",
   "quantity supplied, since buyers cannot purchase goods that were never produced",
   "the average of the two",
   "zero",
   "the equilibrium quantity"], ans=1,
   why="Trade is limited by the short side of the market, which in a shortage is the sellers."),
 dict(q="The quantity actually traded when a surplus exists equals", choices=[
   "quantity supplied",
   "quantity demanded, since sellers cannot force buyers to purchase",
   "the average of the two",
   "the equilibrium quantity",
   "zero"], ans=1,
   why="Trade is again limited by the short side, which in a surplus is the buyers."),
 dict(q="A rise in the price of a substitute good, with everything else unchanged, will in this market", choices=[
   "lower the equilibrium price and quantity",
   "raise the equilibrium price and quantity",
   "raise price and lower quantity",
   "lower price and raise quantity",
   "leave equilibrium unchanged"], ans=1,
   why="A costlier substitute increases demand, and a rightward demand shift raises both price and quantity."),
 dict(q="A rise in the price of a key input, with everything else unchanged, will", choices=[
   "lower the equilibrium price and raise quantity",
   "raise the equilibrium price and lower quantity",
   "raise both price and quantity",
   "lower both price and quantity",
   "leave equilibrium unchanged"], ans=1,
   why="Higher costs decrease supply, and a leftward supply shift raises price and reduces quantity."),
 dict(q="Which pair of changes would definitely raise the equilibrium quantity in a market?", choices=[
   "an increase in demand and a decrease in supply",
   "an increase in demand and an increase in supply",
   "a decrease in demand and a decrease in supply",
   "a decrease in demand and an increase in supply",
   "a decrease in demand alone and an increase in input prices"], ans=1,
   why="Two shifts that both push quantity the same way settle the direction of quantity."),
 dict(q="Which pair of changes would definitely lower the equilibrium price in a market?", choices=[
   "an increase in demand and a decrease in supply",
   "a decrease in demand and an increase in supply",
   "an increase in demand and an increase in supply",
   "a decrease in demand and a decrease in supply",
   "an increase in the number of buyers alone"], ans=1,
   why="Weaker demand and stronger supply both press on price from the same side."),
 dict(q="A market in which the price is currently above equilibrium will adjust as", choices=[
   "buyers bid the price up",
   "sellers accumulate unsold inventory and cut prices",
   "the government imposes a ceiling",
   "supply shifts left automatically",
   "demand shifts right automatically"], ans=1,
   why="The unsold surplus is the pressure that drives price back to the clearing level."),
 dict(q="An observed increase in both the price and the quantity of a good traded is most consistent with", choices=[
   "an increase in supply",
   "an increase in demand",
   "a decrease in demand",
   "a decrease in supply",
   "no change in either curve"], ans=1,
   why="Only a rightward demand shift moves the market up along an unchanged supply curve."),
 dict(q="An observed decrease in price together with an increase in quantity traded is most consistent with", choices=[
   "an increase in demand",
   "an increase in supply",
   "a decrease in supply",
   "a decrease in demand",
   "a binding price floor"], ans=1,
   why="Only a rightward supply shift moves the market down along an unchanged demand curve."),
 dict(q="An observed increase in price together with a decrease in quantity traded is most consistent with", choices=[
   "an increase in supply",
   "a decrease in supply",
   "an increase in demand",
   "a decrease in demand",
   "both curves shifting right"], ans=1,
   why="A leftward supply shift moves the market up along an unchanged demand curve."),
 dict(q="An observed decrease in both price and quantity traded is most consistent with", choices=[
   "a decrease in supply",
   "a decrease in demand",
   "an increase in supply",
   "an increase in demand",
   "a binding price ceiling"], ans=1,
   why="A leftward demand shift moves the market down along an unchanged supply curve."),
 dict(q="Suppose the price of a good rises but the quantity traded does not change measurably. The most likely explanation is that", choices=[
   "supply increased",
   "demand increased while supply decreased by an offsetting amount",
   "demand decreased",
   "the market is not in equilibrium",
   "the good has no substitutes"], ans=1,
   why="Opposite shifts both push price up while their effects on quantity cancel."),
 dict(q="In a competitive market, the equilibrium price is determined by", choices=[
   "sellers alone",
   "the interaction of demand and supply",
   "buyers alone",
   "the government",
   "the cost of production alone"], ans=1,
   why="Neither side sets the price by itself; the clearing price comes from both schedules together."),
 dict(q="If a market is in equilibrium and neither curve shifts, the price will", choices=[
   "rise gradually",
   "remain at the equilibrium level",
   "fall gradually",
   "oscillate",
   "become indeterminate"], ans=1,
   why="With no shortage or surplus there is no force acting on price."),
 dict(q="A binding price ceiling in a market with a shortage will, over time, tend to produce", choices=[
   "a surplus of the good",
   "queues, rationing, or black markets, since price cannot allocate the good",
   "a rightward shift of supply",
   "an immediate return to equilibrium",
   "a fall in quantity demanded to zero"], ans=1,
   why="When price is prevented from rising, some other mechanism must ration the limited quantity supplied."),
 dict(q="Which of the following changes would leave the equilibrium price unchanged but raise the equilibrium quantity?", choices=[
   "an increase in demand only",
   "equal increases in both demand and supply",
   "an increase in supply only",
   "a decrease in demand only",
   "equal decreases in demand and supply"], ans=1,
   why="Offsetting price pressures cancel while both shifts push quantity up."),
 dict(q="Consumers' incomes rise and, at the same time, a new tax is imposed on the producers of a normal good. The equilibrium price will", choices=[
   "fall",
   "rise, while the change in quantity cannot be determined without knowing the sizes of the shifts",
   "be unchanged",
   "rise, and quantity will certainly rise",
   "fall, and quantity will certainly fall"], ans=1,
   why="Demand shifts right and supply shifts left, so price rises for certain while quantity is pulled both ways."),
]
