# 6.1 Socially Efficient and Inefficient Market Outcomes — 50 questions
# Table verified: competitive market, equilibrium P = $6, Q = 40.
#   At Q = 40, marginal benefit = marginal cost = $6.
#   At Q = 30, MB = $8 and MC = $5, so the 31st through 40th units are worth making.
#   At Q = 50, MB = $4 and MC = $7, so those units cost more than they are worth.
TOPIC = ("6.1", "Socially Efficient and Inefficient Market Outcomes", 6)
EFF = dict(headers=["Quantity", "Marginal benefit", "Marginal cost"],
           rows=[["30", "$8", "$5"], ["40", "$6", "$6"], ["50", "$4", "$7"]])
QUESTIONS = [
 dict(q="Consumer surplus is", choices=[
   "the total amount consumers pay",
   "the difference between what consumers are willing to pay and what they actually pay",
   "the area under the supply curve",
   "the firm's profit",
   "total revenue minus total cost"], ans=1,
   why="It is the area below the demand curve and above the price."),
 dict(q="Producer surplus is", choices=[
   "total revenue",
   "the difference between the price a producer receives and the minimum it would accept",
   "accounting profit",
   "the area under the demand curve",
   "total fixed cost"], ans=1,
   why="It is the area above the supply curve and below the price."),
 dict(q="Total surplus is", choices=[
   "consumer surplus minus producer surplus",
   "consumer surplus plus producer surplus",
   "total revenue",
   "the deadweight loss",
   "the government's tax revenue"], ans=1,
   why="It measures the total gains from trade in the market."),
 dict(q="A market outcome is allocatively efficient when", choices=[
   "producer surplus is maximized",
   "the marginal benefit of the last unit equals its marginal cost",
   "consumer surplus is maximized",
   "price equals average total cost",
   "output is as large as possible"], ans=1,
   why="At that quantity no further mutually beneficial trade is available."),
 dict(q="In a competitive market free of externalities, the equilibrium quantity", choices=[
   "is always too small",
   "maximizes total surplus",
   "is always too large",
   "creates deadweight loss",
   "sets price below marginal cost"], ans=1,
   why="Supply reflects marginal cost and demand reflects marginal benefit, so equilibrium equates them."),
 dict(q="Using the table, the socially efficient quantity is", table=EFF, choices=[
   "30", "40", "50", "any of them", "none of them"], ans=1,
   why="At 40 units marginal benefit equals marginal cost at $6."),
 dict(q="Using the table, at a quantity of 30 society should", table=EFF, choices=[
   "produce less",
   "produce more, since the marginal benefit of $8 exceeds the marginal cost of $5",
   "produce nothing",
   "leave output unchanged",
   "raise the price"], ans=1,
   why="Each further unit is worth more than it costs."),
 dict(q="Using the table, at a quantity of 50 society should", table=EFF, choices=[
   "produce more",
   "produce less, since the marginal cost of $7 exceeds the marginal benefit of $4",
   "leave output unchanged",
   "produce nothing",
   "lower the price"], ans=1,
   why="Those units cost more resources than the value they create."),
 dict(q="Using the table, producing at 50 rather than 40 units generates", table=EFF, choices=[
   "extra total surplus",
   "a deadweight loss, because resources are used on units worth less than they cost",
   "no change in surplus",
   "higher consumer surplus only",
   "allocative efficiency"], ans=1,
   why="Overproduction destroys surplus just as underproduction forgoes it."),
 dict(q="Using the table, the marginal benefit curve is another name for the", table=EFF, choices=[
   "supply curve", "demand curve", "marginal cost curve", "total revenue curve", "average cost curve"], ans=1,
   why="Demand shows what buyers are willing to pay, which is the marginal benefit."),
 dict(q="The demand curve in a market without externalities represents", choices=[
   "marginal cost", "marginal benefit to society", "total surplus", "producer surplus", "average revenue only"], ans=1,
   why="Willingness to pay measures the value of the unit to the buyer."),
 dict(q="The supply curve in a market without externalities represents", choices=[
   "marginal benefit", "marginal cost to society", "consumer surplus", "total revenue", "average benefit"], ans=1,
   why="The minimum acceptable price reflects the cost of producing the unit."),
 dict(q="Deadweight loss is", choices=[
   "the profit lost by firms",
   "the reduction in total surplus caused by producing a quantity other than the efficient one",
   "the tax revenue collected",
   "consumer surplus alone",
   "the total cost of production"], ans=1,
   why="It measures value that neither buyers, sellers, nor the government receives."),
 dict(q="A price ceiling set below the equilibrium price causes", choices=[
   "a surplus", "a shortage and a deadweight loss", "no change", "higher output", "efficiency"], ans=1,
   why="Quantity demanded exceeds quantity supplied and some valuable trades do not occur."),
 dict(q="A price floor set above the equilibrium price causes", choices=[
   "a shortage", "a surplus and a deadweight loss", "no change", "efficiency", "lower prices"], ans=1,
   why="Quantity supplied exceeds quantity demanded and output falls below the efficient level."),
 dict(q="A binding price ceiling reduces total surplus because", choices=[
   "producers earn more",
   "quantity traded falls below the efficient level, so some valuable trades are lost",
   "consumers pay more",
   "output rises above the efficient level",
   "the government collects revenue"], ans=1,
   why="The reduced quantity is where the loss comes from."),
 dict(q="A market has demand P = 20 - Q and supply P = Q. Total surplus at the competitive equilibrium is", choices=[
   "$50", "$100", "$150", "$200", "$400"], ans=1,
   why="Equilibrium is Q = 10 at P = 10, giving consumer surplus of 50 and producer surplus of 50."),
 dict(q="In that market, if output is held at 6 units instead of the efficient 10, the deadweight loss is", choices=[
   "$8", "$16", "$32", "$40", "$64"], ans=1,
   why="Marginal benefit is 14 and marginal cost is 6 at Q = 6, so the lost surplus is half of 4 times 8."),
 dict(q="A per-unit tax on a good causes the quantity traded to", choices=[
   "rise above the efficient level",
   "fall below the efficient level, creating a deadweight loss",
   "stay the same",
   "become zero",
   "be unaffected"], ans=1,
   why="The tax drives a wedge between the price buyers pay and sellers receive."),
 dict(q="The deadweight loss of a tax comes from", choices=[
   "the revenue collected by the government",
   "the trades that no longer happen because of the tax wedge",
   "the price buyers pay",
   "the producer surplus transferred",
   "the price sellers receive"], ans=1,
   why="Tax revenue is a transfer; the lost trades are the real loss."),
 dict(q="A tax's deadweight loss is larger when supply and demand are", choices=[
   "inelastic", "elastic", "perfectly inelastic", "vertical", "unit elastic"], ans=1,
   why="Elastic responses mean a larger fall in the quantity traded."),
 dict(q="A tax on a good with perfectly inelastic demand generates", choices=[
   "a very large deadweight loss",
   "no deadweight loss, because the quantity traded does not change",
   "no tax revenue",
   "a surplus",
   "a shortage"], ans=1,
   why="Deadweight loss comes from changed behavior, and none occurs here."),
 dict(q="Total surplus is maximized at the competitive quantity because at any smaller quantity", choices=[
   "producers capture too much of the surplus",
   "there remain units buyers value more than they cost to produce",
   "marginal cost exceeds marginal benefit",
   "consumer surplus is zero",
   "the price is above the demand curve"], ans=1,
   why="Every unmade unit whose marginal benefit exceeds its marginal cost is surplus left on the table."),
 dict(q="On the demand curve P = 20 - Q, consumer surplus when the price falls from $12 to $8 rises by", choices=[
   "$4", "$16", "$32", "$40", "$72"], ans=3,
   why="Surplus goes from 32 at a quantity of 8 to 72 at a quantity of 12."),
 dict(q="A trade between a buyer and a seller creates surplus whenever", choices=[
   "the buyer's willingness to pay exceeds the seller's willingness to accept",
   "the price is set by the government",
   "the seller's cost exceeds the buyer's valuation",
   "both parties pay the same amount",
   "the good is scarce"], ans=0,
   why="The gap between what the unit is worth to the buyer and what it costs the seller is the surplus the trade creates."),
 dict(q="An efficient market outcome is one in which it is impossible to", choices=[
   "raise one person's surplus without lowering another's",
   "produce any output at all",
   "achieve equality of income",
   "earn accounting profit",
   "lower the price"], ans=0,
   why="With every mutually beneficial trade already made, further gains can only come at someone else's expense."),
 dict(q="A per-unit subsidy on a good causes quantity traded to", choices=[
   "fall below the efficient level",
   "rise above the efficient level, creating a deadweight loss",
   "stay at the efficient level",
   "become zero",
   "be unaffected"], ans=1,
   why="Units worth less than they cost get produced."),
 dict(q="A subsidy in a market with no externalities is inefficient because", choices=[
   "it costs the government money only",
   "it encourages production of units whose marginal cost exceeds their marginal benefit",
   "it lowers prices",
   "it raises producer surplus",
   "it raises consumer surplus"], ans=1,
   why="The efficient quantity is where MB = MC, and the subsidy pushes past it."),
 dict(q="A quota that restricts the quantity sold below the equilibrium level causes", choices=[
   "a surplus of the good",
   "a deadweight loss from the trades that no longer occur",
   "an increase in total surplus",
   "efficiency",
   "lower prices"], ans=1,
   why="Restricting quantity below the efficient level forgoes valuable trades."),
 dict(q="Market failure occurs when", choices=[
   "firms earn no profit",
   "a market left to itself does not allocate resources efficiently",
   "prices are too high",
   "a firm goes bankrupt",
   "the government intervenes"], ans=1,
   why="Failure here means an inefficient outcome, not a business failing."),
 dict(q="Which of the following is a source of market failure?", choices=[
   "many buyers and sellers",
   "externalities, public goods, market power, and imperfect information",
   "free entry",
   "perfect competition",
   "perfect information"], ans=1,
   why="These are the standard cases where the market outcome is not efficient."),
 dict(q="In a competitive market at equilibrium, the deadweight loss is", choices=[
   "positive", "zero", "negative", "equal to total surplus", "equal to consumer surplus"], ans=1,
   why="Every valuable trade takes place, so nothing is lost."),
 dict(q="If a market produces less than the efficient quantity, the deadweight loss represents", choices=[
   "resources wasted on unwanted units",
   "the value of trades that would have benefited both buyer and seller but did not occur",
   "the government's revenue",
   "producer profit",
   "consumer spending"], ans=1,
   why="Underproduction forgoes gains from trade."),
 dict(q="A market at a quantity of 100 has marginal benefit $12 and marginal cost $9. Society should", choices=[
   "produce less", "produce more", "leave output unchanged", "shut the market", "raise the price"], ans=1,
   why="Additional units are worth more than they cost."),
 dict(q="A market at a quantity of 200 has marginal benefit $5 and marginal cost $11. Society should", choices=[
   "produce more", "produce less", "leave output unchanged", "subsidize production", "raise output"], ans=1,
   why="Those units cost more than the value they create."),
 dict(q="A market where marginal benefit equals marginal cost at the current quantity is", choices=[
   "producing too much", "allocatively efficient", "producing too little", "in deadweight loss", "a monopoly"], ans=1,
   why="That equality is the definition of allocative efficiency."),
 dict(q="Consumer surplus in a market with equilibrium price $10, a demand curve intercept of $30, and a quantity of 40 is", choices=[
   "$200", "$400", "$800", "$1,200", "$40"], ans=1,
   why="The triangle is ½ × 40 × ($30 − $10) = $400."),
 dict(q="Producer surplus in a market with equilibrium price $10, a supply curve intercept of $2, and a quantity of 40 is", choices=[
   "$80", "$160", "$320", "$400", "$40"], ans=1,
   why="½ × 40 × ($10 − $2) = $160."),
 dict(q="Using those figures, total surplus is", choices=[
   "$160", "$400", "$560", "$640", "$240"], ans=2,
   why="$400 of consumer surplus plus $160 of producer surplus."),
 dict(q="A monopoly creates a deadweight loss because it", choices=[
   "earns profit",
   "restricts output to a level where price exceeds marginal cost",
   "produces too much",
   "sets price equal to marginal cost",
   "has high costs"], ans=1,
   why="The units between the monopoly output and the efficient output are worth making but are not made."),
 dict(q="An efficient allocation of resources requires that goods be produced", choices=[
   "in the largest possible quantity",
   "at the lowest possible cost and in the quantities consumers value most",
   "by the fewest firms",
   "by the government",
   "at zero price"], ans=1,
   why="Productive and allocative efficiency together."),
 dict(q="Productive efficiency means", choices=[
   "producing the right mix of goods",
   "producing any given output at the lowest possible cost",
   "maximizing consumer surplus",
   "setting price equal to marginal cost",
   "eliminating profit"], ans=1,
   why="It concerns cost, while allocative efficiency concerns what to produce."),
 dict(q="Equity and efficiency are different concepts because efficiency concerns", choices=[
   "how fairly the surplus is divided",
   "the size of the total surplus, not how it is distributed",
   "government revenue",
   "producer profit only",
   "consumer spending only"], ans=1,
   why="An efficient outcome can be highly unequal."),
 dict(q="A policy that raises total surplus but makes some people worse off is", choices=[
   "necessarily a bad policy",
   "efficient, though it raises a separate question about equity",
   "inefficient",
   "impossible",
   "always adopted"], ans=1,
   why="Efficiency and fairness are evaluated separately."),
 dict(q="A tax whose revenue exceeds its deadweight loss is", choices=[
   "impossible",
   "still distortionary, but the revenue is a transfer rather than a loss",
   "efficient by definition",
   "equivalent to a subsidy",
   "a price ceiling"], ans=1,
   why="Only the forgone trades are a genuine loss of surplus."),
 dict(q="In a competitive market, the invisible hand result says that self-interested behavior", choices=[
   "always harms society",
   "can lead to an efficient allocation of resources when there are no market failures",
   "requires government direction",
   "eliminates all surplus",
   "guarantees fairness"], ans=1,
   why="The efficiency conclusion depends on the absence of externalities and market power."),
 dict(q="Which of the following would move a competitive market away from allocative efficiency?", choices=[
   "free entry",
   "the introduction of a binding price ceiling",
   "perfect information",
   "many small firms",
   "an identical product"], ans=1,
   why="A binding ceiling reduces the quantity traded below the efficient level."),
 dict(q="A market in which the quantity traded is below the efficient level has", choices=[
   "maximum total surplus",
   "a deadweight loss equal to the forgone gains from the untraded units",
   "no consumer surplus",
   "no producer surplus",
   "excess supply"], ans=1,
   why="The lost surplus is the triangle between the two curves over the missing units."),
 dict(q="The efficient quantity in a market is found where the", choices=[
   "supply curve intersects the vertical axis",
   "demand curve intersects the supply curve, absent externalities",
   "demand curve intersects the horizontal axis",
   "average cost is minimized",
   "profit is maximized"], ans=1,
   why="That intersection is where marginal benefit equals marginal cost."),
 dict(q="If a market's marginal benefit exceeds its marginal cost at the current quantity, total surplus can be increased by", choices=[
   "reducing output", "increasing output", "taxing the good", "imposing a quota", "leaving output unchanged"], ans=1,
   why="Each added unit creates more value than it consumes in resources."),
]
