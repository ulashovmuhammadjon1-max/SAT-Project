# 4.2 Monopoly — 50 questions
# Table verified: linear demand P = 10 - Q
#   Q=1 P=9 TR=9   MR=9
#   Q=2 P=8 TR=16  MR=7
#   Q=3 P=7 TR=21  MR=5
#   Q=4 P=6 TR=24  MR=3
#   Q=5 P=5 TR=25  MR=1
#   With constant MC = $3, MR = MC at Q = 4, where P = $6.
TOPIC = ("4.2", "Monopoly", 4)
MON = dict(headers=["Quantity", "Price"],
           rows=[["1", "$9"], ["2", "$8"], ["3", "$7"], ["4", "$6"], ["5", "$5"]])
QUESTIONS = [
 dict(q="A monopoly is a market in which", choices=[
   "a few firms sell similar products",
   "a single firm sells a product with no close substitutes and entry is blocked",
   "many firms sell differentiated products",
   "many firms sell identical products",
   "there is a single buyer"], ans=1,
   why="One seller, no close substitute, and barriers to entry define monopoly."),
 dict(q="A monopolist's demand curve is", choices=[
   "horizontal at the market price",
   "the market demand curve, which slopes downward",
   "vertical",
   "perfectly elastic",
   "upward sloping"], ans=1,
   why="Being the only seller, the firm faces the entire market demand."),
 dict(q="For a monopolist, marginal revenue is", choices=[
   "equal to price", "less than price at every positive quantity", "greater than price",
   "constant and equal to marginal cost", "always negative"], ans=1,
   why="To sell one more unit the monopolist must lower the price on all units."),
 dict(q="A monopolist maximizes profit by producing where", choices=[
   "price equals marginal cost",
   "marginal revenue equals marginal cost",
   "price equals average total cost",
   "total revenue is at its maximum",
   "average total cost is minimized"], ans=1,
   why="MR = MC is the general profit-maximizing rule."),
 dict(q="After finding its profit-maximizing quantity, a monopolist sets its price by", choices=[
   "reading the price off its marginal revenue curve at that quantity",
   "reading the price off the demand curve at that quantity",
   "setting price equal to marginal cost",
   "setting price equal to average total cost",
   "charging whatever it wishes, without limit"], ans=1,
   why="Demand shows the highest price at which that quantity will actually sell."),
 dict(q="Using the table, what is total revenue at a quantity of 3?", table=MON, choices=[
   "$7", "$15", "$21", "$24", "$30"], ans=2,
   why="TR = 7 × 3 = $21."),
 dict(q="Using the table, what is marginal revenue for the third unit?", table=MON, choices=[
   "$3", "$5", "$7", "$16", "$21"], ans=1,
   why="TR rises from $16 to $21, so MR = $5."),
 dict(q="Using the table, what is marginal revenue for the fourth unit?", table=MON, choices=[
   "$1", "$3", "$5", "$6", "$24"], ans=1,
   why="TR rises from $21 to $24, so MR = $3."),
 dict(q="Using the table, if marginal cost is constant at $3, the profit-maximizing quantity is", table=MON, choices=[
   "1", "2", "3", "4", "5"], ans=3,
   why="MR equals the $3 marginal cost at the fourth unit."),
 dict(q="Using the table, if marginal cost is constant at $3, the price the monopolist charges is", table=MON, choices=[
   "$3", "$5", "$6", "$7", "$8"], ans=2,
   why="At the profit-maximizing quantity of 4, demand shows a price of $6."),
 dict(q="Using the table, marginal revenue is smaller than price at every quantity because", table=MON, choices=[
   "the monopolist has high costs",
   "selling another unit requires cutting the price on all units sold",
   "the demand curve is horizontal",
   "marginal cost is rising",
   "total revenue is falling"], ans=1,
   why="The revenue gained on the extra unit is offset by the revenue lost on the earlier ones."),
 dict(q="Using the table, at what quantity is total revenue largest?", table=MON, choices=[
   "1", "2", "3", "4", "5"], ans=4,
   why="TR is 9, 16, 21, 24, 25, so it peaks at 5 units."),
 dict(q="Using the table, a monopolist would not choose the quantity that maximizes total revenue because", table=MON, choices=[
   "revenue does not matter",
   "the extra units cost something to produce, and profit, not revenue, is the objective",
   "marginal revenue is negative there",
   "price would be too high",
   "demand is elastic there"], ans=1,
   why="Beyond MR = MC each unit adds more cost than revenue."),
 dict(q="A monopolist's marginal revenue curve, for a linear demand curve, is", choices=[
   "the same as the demand curve",
   "twice as steep as the demand curve and lies below it",
   "horizontal",
   "upward sloping",
   "always positive"], ans=1,
   why="For P = a − bQ, MR = a − 2bQ."),
 dict(q="A monopolist earning positive economic profit can maintain it in the long run because", choices=[
   "its costs fall over time",
   "barriers to entry prevent competitors from entering",
   "it produces where P = MC",
   "consumers cannot switch",
   "marginal revenue equals price"], ans=1,
   why="Nothing erodes the profit if no one can enter."),
 dict(q="A monopolist's economic profit is", choices=[
   "always positive",
   "positive only if price exceeds average total cost at the profit-maximizing quantity",
   "always zero in the long run",
   "always negative",
   "equal to total revenue"], ans=1,
   why="Market power does not guarantee that demand is strong enough to cover costs."),
 dict(q="A monopolist produces 500 units, charges $18, and has an average total cost of $12. Its profit is", choices=[
   "$6", "$500", "$3,000", "$6,000", "$9,000"], ans=2,
   why="(18 − 12) × 500 = $3,000."),
 dict(q="A monopolist produces 200 units, charges $25, and has an average total cost of $30. It is", choices=[
   "earning $1,000", "losing $1,000", "breaking even", "earning $5,000", "losing $5"], ans=1,
   why="(25 − 30) × 200 = −$1,000."),
 dict(q="A monopolist that incurs a loss in the short run should shut down if price is below", choices=[
   "average total cost", "average variable cost", "marginal cost", "marginal revenue", "average fixed cost"], ans=1,
   why="The shutdown rule is the same as for any firm."),
 dict(q="Compared with a perfectly competitive industry with the same costs, a monopoly produces", choices=[
   "more output at a lower price",
   "less output at a higher price",
   "the same output at a higher price",
   "more output at a higher price",
   "the same output at the same price"], ans=1,
   why="Setting MR = MC with MR below price restricts output."),
 dict(q="Deadweight loss under monopoly arises because", choices=[
   "the monopolist earns profit",
   "units for which buyers' willingness to pay exceeds marginal cost are not produced",
   "average total cost is minimized",
   "the monopolist has high fixed costs",
   "consumers pay nothing"], ans=1,
   why="The lost mutually beneficial trades are the efficiency cost."),
 dict(q="Monopoly is allocatively inefficient because at the monopolist's output", choices=[
   "price equals marginal cost",
   "price exceeds marginal cost",
   "price is below marginal cost",
   "average cost is minimized",
   "marginal revenue equals price"], ans=1,
   why="The last unit is worth more to buyers than it costs to make."),
 dict(q="Compared with perfect competition, monopoly typically transfers surplus", choices=[
   "from producers to consumers",
   "from consumers to the producer",
   "from the government to consumers",
   "equally in both directions",
   "not at all"], ans=1,
   why="A higher price converts part of consumer surplus into monopoly profit."),
 dict(q="A monopolist will always operate on the portion of its demand curve where demand is", choices=[
   "inelastic", "elastic", "unit elastic", "perfectly inelastic", "perfectly elastic"], ans=1,
   why="Where demand is inelastic MR is negative, so cutting output would raise revenue and cut cost."),
 dict(q="If a monopolist's marginal revenue is negative, total revenue is", choices=[
   "rising", "falling", "at its maximum", "zero", "equal to profit"], ans=1,
   why="Negative MR means an extra unit reduces revenue."),
 dict(q="A monopolist has no supply curve because", choices=[
   "it produces nothing",
   "it chooses a price-quantity pair from the demand curve rather than responding to a given price",
   "its marginal cost is zero",
   "it always sells at average cost",
   "it faces no demand"], ans=1,
   why="A supply curve maps a given price to a quantity, which is a price taker's problem."),
 dict(q="A natural monopoly arises when", choices=[
   "the firm sells a natural resource",
   "economies of scale continue over the whole relevant range of demand",
   "the government nationalizes the firm",
   "many firms have identical costs",
   "marginal cost rises steeply"], ans=1,
   why="Falling average cost throughout means one firm serves the market most cheaply."),
 dict(q="A monopolist currently sells 40 units at $30. To sell the 41st unit it must drop the price to $29.50 on every unit. Marginal revenue for that unit is", choices=[
   "$29.50", "$9.50", "$20.00", "$30.00", "-$0.50"], ans=1,
   why="It gains $29.50 on the new unit but loses $0.50 on each of the 40 already sold, so 29.50 - 20 = $9.50."),
 dict(q="A monopolist's demand is P = 80 - 2Q with constant marginal cost of $8. Its profit-maximizing quantity is", choices=[
   "9", "18", "20", "36", "40"], ans=1,
   why="MR = 80 - 4Q; setting that equal to 8 gives Q = 18."),
 dict(q="For the monopolist facing P = 80 - 2Q with marginal cost $8, the price charged is", choices=[
   "$8", "$18", "$36", "$44", "$80"], ans=3,
   why="Demand at Q = 18 gives P = 80 - 2(18) = $44."),
 dict(q="A monopolist's profit-maximizing output compared with the allocatively efficient output is", choices=[
   "larger", "smaller", "the same", "zero", "unrelated"], ans=1,
   why="Efficiency requires P = MC, which lies to the right of MR = MC."),
 dict(q="Which of the following is a source of monopoly power?", choices=[
   "many close substitutes",
   "exclusive ownership of a key input",
   "free entry",
   "identical products sold by many firms",
   "perfect information"], ans=1,
   why="Rivals cannot produce without the input."),
 dict(q="A patent creates a temporary monopoly in order to", choices=[
   "raise government revenue",
   "give inventors an incentive to bear the cost of innovation",
   "lower consumer prices immediately",
   "eliminate deadweight loss",
   "guarantee zero profit"], ans=1,
   why="The prospect of monopoly profit is what funds the research."),
 dict(q="When a monopolist's patent expires, we expect", choices=[
   "price to rise and output to fall",
   "entry, lower prices, and greater output",
   "no change",
   "the firm to earn more profit",
   "demand to become perfectly inelastic"], ans=1,
   why="Barriers falling away allows competition."),
 dict(q="A monopolist facing a per-unit tax on output will", choices=[
   "keep output unchanged",
   "reduce output and raise price, since marginal cost has shifted up",
   "increase output",
   "lower its price",
   "exit immediately"], ans=1,
   why="The tax adds to the cost of each unit produced."),
 dict(q="A monopolist facing a lump-sum tax will", choices=[
   "reduce output",
   "keep its price and output unchanged while earning less profit",
   "raise its price",
   "increase output",
   "always shut down"], ans=1,
   why="A fixed payment does not enter marginal cost."),
 dict(q="A monopolist with constant marginal cost of $10 faces demand P = 50 − Q. Marginal revenue is", choices=[
   "50 − Q", "50 − 2Q", "25 − Q", "10 − Q", "50 + 2Q"], ans=1,
   why="For a linear demand P = a − bQ, MR = a − 2bQ."),
 dict(q="For the monopolist in the previous question, the profit-maximizing quantity is", choices=[
   "10", "20", "25", "40", "50"], ans=1,
   why="Setting 50 − 2Q = 10 gives Q = 20."),
 dict(q="For that same monopolist, the price charged is", choices=[
   "$10", "$20", "$30", "$40", "$50"], ans=2,
   why="P = 50 − 20 = $30."),
 dict(q="A monopolist with constant marginal cost of $4 faces demand P = 20 − 2Q. Its profit-maximizing quantity is", choices=[
   "2", "4", "8", "10", "16"], ans=1,
   why="MR = 20 − 4Q; setting it equal to 4 gives Q = 4."),
 dict(q="For that monopolist, the price charged is", choices=[
   "$4", "$8", "$12", "$16", "$20"], ans=2,
   why="P = 20 − 2(4) = $12."),
 dict(q="A monopolist that could sell the same quantity at a higher price would", choices=[
   "already be doing so, since it maximizes profit",
   "need to lower its costs first",
   "be violating the law",
   "have to exit",
   "face a horizontal demand curve"], ans=0,
   why="The price it charges is already the most the market will bear at that quantity."),
 dict(q="The claim that a monopolist can charge any price it likes is wrong because", choices=[
   "the government sets all prices",
   "the quantity buyers will purchase falls as the price rises",
   "its marginal cost is fixed",
   "marginal revenue equals price",
   "it has no fixed costs"], ans=1,
   why="The demand curve constrains the firm even though it is the only seller."),
 dict(q="Compared with a competitive firm, a monopolist in long-run equilibrium produces at an output where average total cost is", choices=[
   "always at its minimum",
   "generally not at its minimum",
   "always zero",
   "equal to marginal revenue",
   "equal to price"], ans=1,
   why="Nothing forces a protected monopolist to the productively efficient scale."),
 dict(q="Antitrust policy addresses monopoly power mainly by", choices=[
   "subsidizing monopolists",
   "preventing or breaking up anticompetitive market structures and conduct",
   "setting all prices in the economy",
   "guaranteeing profits",
   "raising barriers to entry"], ans=1,
   why="The aim is to restore competition where it can work."),
 dict(q="Consumer surplus under monopoly compared with perfect competition is", choices=[
   "larger", "smaller", "the same", "zero", "negative"], ans=1,
   why="A higher price and smaller quantity shrink the area under demand above price."),
 dict(q="Total surplus under monopoly compared with perfect competition is", choices=[
   "larger", "smaller by the amount of the deadweight loss", "the same", "zero", "always negative"], ans=1,
   why="The transfer to the producer is not a loss, but the unproduced units are."),
 dict(q="A monopolist that has driven its price to the point where demand is unit elastic has", choices=[
   "maximized profit",
   "maximized total revenue, which is generally not the profit-maximizing point",
   "minimized average cost",
   "achieved allocative efficiency",
   "eliminated deadweight loss"], ans=1,
   why="Profit maximization requires accounting for cost, not just revenue."),
 dict(q="Which condition would turn a monopoly into a competitive market over time?", choices=[
   "a stronger patent",
   "the removal of legal barriers to entry",
   "acquisition of a rival",
   "increased brand loyalty",
   "exclusive control of an input"], ans=1,
   why="Free entry is precisely what monopoly lacks."),
 dict(q="A monopolist choosing output where MR = MC and finding P > ATC will", choices=[
   "exit the industry",
   "earn a positive economic profit that can persist in the long run",
   "shut down in the short run",
   "produce the efficient quantity",
   "earn zero economic profit"], ans=1,
   why="Barriers to entry protect the profit indefinitely."),
]
