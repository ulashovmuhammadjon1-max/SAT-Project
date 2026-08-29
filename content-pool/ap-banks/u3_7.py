# 3.7 Perfect Competition — 50 questions
# Table verified: market price $9 (price taker), so TR = 9Q and MR = 9 at every Q.
#   Q=0 TC=10 ; Q=1 TC=17 ; Q=2 TC=22 ; Q=3 TC=29 ; Q=4 TC=38 ; Q=5 TC=50
#   MC:        7          5          7          9          12
#   Profit: -10, -8, -4, -2, -2, -5  -> maximum at Q=3 or Q=4 (both -2);
#   MR = MC exactly at Q=4, which is the rule's answer.
TOPIC = ("3.7", "Perfect Competition", 3)
PC = dict(headers=["Quantity", "Total cost"],
          rows=[["0", "$10"], ["1", "$17"], ["2", "$22"],
                ["3", "$29"], ["4", "$38"], ["5", "$50"]])
QUESTIONS = [
 dict(q="Which of the following is a characteristic of perfect competition?", choices=[
   "a single seller",
   "many buyers and sellers, each too small to affect the market price",
   "substantial barriers to entry",
   "highly differentiated products",
   "extensive advertising by each firm"], ans=1,
   why="Large numbers on both sides are what make every participant a price taker."),
 dict(q="In perfect competition, the product sold by different firms is", choices=[
   "highly differentiated", "standardized and identical across firms", "protected by patents",
   "sold only under brand names", "unavailable elsewhere"], ans=1,
   why="Homogeneity means buyers have no reason to prefer one seller."),
 dict(q="A price taker is a firm that", choices=[
   "sets the market price",
   "must accept the market price as given",
   "faces a downward-sloping demand curve",
   "can raise price without losing customers",
   "controls industry output"], ans=1,
   why="Its output is too small a share of the market to move price."),
 dict(q="The demand curve facing an individual perfectly competitive firm is", choices=[
   "downward sloping and identical to market demand",
   "horizontal and perfectly elastic at the market price",
   "vertical",
   "upward sloping",
   "unit elastic at every price"], ans=1,
   why="The firm can sell any quantity at the market price and none above it."),
 dict(q="The market demand curve in a perfectly competitive industry is", choices=[
   "horizontal", "downward sloping", "vertical", "perfectly elastic", "upward sloping"], ans=1,
   why="Buyers in aggregate purchase more only at lower prices, even though each firm faces a flat curve."),
 dict(q="For a perfectly competitive firm, price equals", choices=[
   "average total cost always",
   "marginal revenue and average revenue",
   "marginal cost always",
   "average variable cost",
   "total revenue"], ans=1,
   why="Selling every unit at the same price makes both average and marginal revenue equal to price."),
 dict(q="Average revenue is calculated as", choices=[
   "total revenue divided by quantity", "the change in total revenue", "price times quantity",
   "total cost divided by quantity", "profit per unit"], ans=0,
   why="AR = TR/Q, which for any firm equals price."),
 dict(q="Using the table, if the market price is $9, total revenue at 3 units is", table=PC, choices=[
   "$9", "$18", "$27", "$29", "$36"], ans=2,
   why="TR = 9 × 3 = $27."),
 dict(q="Using the table, the marginal cost of the second unit is", table=PC, choices=[
   "$5", "$7", "$9", "$11", "$22"], ans=0,
   why="Total cost rises from $17 to $22."),
 dict(q="Using the table, the marginal cost of the fourth unit is", table=PC, choices=[
   "$7", "$9", "$12", "$29", "$38"], ans=1,
   why="Total cost rises from $29 to $38."),
 dict(q="Using the table, the firm's total fixed cost is", table=PC, choices=[
   "$0", "$10", "$17", "$22", "$50"], ans=1,
   why="Total cost at zero output is the fixed cost."),
 dict(q="Using the table with a price of $9, applying the MR = MC rule gives an output of", table=PC, choices=[
   "1", "2", "3", "4", "5"], ans=3,
   why="Marginal cost first equals the $9 price at the fourth unit."),
 dict(q="Using the table with a price of $9, the firm's profit at 4 units is", table=PC, choices=[
   "$36", "$2", "−$2", "−$10", "$38"], ans=2,
   why="TR = 36, TC = 38, so the firm loses $2."),
 dict(q="Using the table with a price of $9, the firm should operate rather than shut down because", table=PC, choices=[
   "it earns a positive profit",
   "a $2 loss is smaller than the $10 fixed cost it would bear if it shut down",
   "marginal cost is falling",
   "average total cost is minimized",
   "total revenue exceeds total cost"], ans=1,
   why="Operating covers all variable cost plus $8 of the fixed cost."),
 dict(q="Using the table, the firm's total variable cost at 3 units is", table=PC, choices=[
   "$10", "$19", "$29", "$39", "$9"], ans=1,
   why="VC = TC − FC = 29 − 10 = $19."),
 dict(q="A perfectly competitive firm's total revenue curve is", choices=[
   "a straight line through the origin with slope equal to price",
   "a curve that rises then falls",
   "horizontal",
   "vertical",
   "downward sloping"], ans=0,
   why="Each unit adds exactly the market price to revenue."),
 dict(q="In perfect competition, individual firms do not advertise their own brand because", choices=[
   "advertising is illegal",
   "the products are identical, so a firm can already sell all it wants at the market price",
   "consumers cannot read",
   "profits are always negative",
   "the government sets prices"], ans=1,
   why="There is nothing to differentiate and no unmet demand at the market price."),
 dict(q="Perfect competition requires that buyers and sellers have", choices=[
   "no information about prices",
   "full information about prices and product quality",
   "long-term exclusive contracts",
   "government licenses",
   "brand loyalty"], ans=1,
   why="Perfect information keeps a single price prevailing throughout the market."),
 dict(q="Which real-world market most closely approximates perfect competition?", choices=[
   "commercial aircraft manufacturing",
   "wheat farming",
   "smartphone operating systems",
   "municipal water supply",
   "automobile production"], ans=1,
   why="Many small producers sell a standardized commodity at a price none of them controls."),
 dict(q="If the market price in a competitive industry rises, an individual firm's demand curve", choices=[
   "becomes downward sloping",
   "shifts upward, remaining horizontal",
   "shifts downward",
   "becomes steeper",
   "is unaffected"], ans=1,
   why="The firm still takes the price as given, but that price is now higher."),
 dict(q="A perfectly competitive firm that raises its price above the market price will sell", choices=[
   "the same quantity", "essentially nothing", "more than before", "half as much", "all of the market's output"], ans=1,
   why="Buyers switch to identical output from other sellers."),
 dict(q="The market supply curve in a competitive industry is found by", choices=[
   "adding firms' marginal cost curves vertically",
   "summing the quantities each firm supplies at each price horizontally",
   "using the largest firm's supply curve",
   "averaging firms' average total costs",
   "adding demand curves"], ans=1,
   why="Market supply is the horizontal sum of individual supply curves."),
 dict(q="In perfect competition, the market price is determined by", choices=[
   "each individual firm",
   "the interaction of market supply and market demand",
   "the government",
   "the largest firm's costs",
   "buyers alone"], ans=1,
   why="No single participant sets price; the market does."),
 dict(q="A competitive firm earning positive economic profit in the short run is producing where", choices=[
   "price is below average total cost",
   "price exceeds average total cost",
   "price equals average variable cost",
   "marginal cost exceeds price",
   "output is zero"], ans=1,
   why="Profit per unit is price minus ATC."),
 dict(q="A competitive firm's short-run supply curve is the portion of its marginal cost curve", choices=[
   "below minimum average variable cost",
   "at and above minimum average variable cost",
   "below minimum average total cost",
   "that is downward sloping",
   "that lies above average total cost only"], ans=1,
   why="Below minimum AVC the firm supplies nothing."),
 dict(q="In perfect competition, a firm has no market power, meaning it", choices=[
   "produces nothing",
   "cannot influence the price at which it sells",
   "cannot choose its output",
   "must sell at a loss",
   "faces no competition"], ans=1,
   why="Market power is the ability to set price above marginal cost."),
 dict(q="In long-run equilibrium in perfect competition, price equals", choices=[
   "marginal cost and minimum average total cost",
   "average variable cost only",
   "marginal revenue but not marginal cost",
   "average fixed cost",
   "the highest cost firm's ATC"], ans=0,
   why="Profit maximization gives P = MC and free entry gives P = min ATC."),
 dict(q="Perfect competition achieves allocative efficiency because", choices=[
   "firms earn maximum profit",
   "price equals marginal cost at the equilibrium quantity",
   "average total cost is at a minimum",
   "there are many firms",
   "advertising is absent"], ans=1,
   why="The value buyers place on the last unit equals the resource cost of producing it."),
 dict(q="Perfect competition achieves productive efficiency in the long run because", choices=[
   "price exceeds marginal cost",
   "each firm produces at the minimum of its average total cost curve",
   "profit is maximized",
   "output is unlimited",
   "fixed costs are zero"], ans=1,
   why="Entry drives price down to the lowest attainable average cost."),
 dict(q="Consumer surplus in a competitive market is", choices=[
   "the amount buyers pay",
   "the difference between what buyers are willing to pay and what they actually pay",
   "total revenue",
   "the firm's profit",
   "the area under the supply curve"], ans=1,
   why="It is the area below demand and above price."),
 dict(q="Producer surplus in a competitive market is", choices=[
   "total revenue",
   "the difference between the price received and the marginal cost of producing each unit",
   "accounting profit",
   "the area under the demand curve",
   "total fixed cost"], ans=1,
   why="It is the area above supply and below price."),
 dict(q="At the competitive equilibrium, total surplus is", choices=[
   "zero", "maximized", "minimized", "equal to producer surplus alone", "negative"], ans=1,
   why="Any other quantity leaves mutually beneficial trades unmade or forces value-destroying ones."),
 dict(q="Deadweight loss in a competitive market occurs when output is", choices=[
   "at the equilibrium quantity",
   "above or below the quantity where price equals marginal cost",
   "always zero",
   "at minimum average total cost",
   "maximized"], ans=1,
   why="Away from P = MC, some units worth more than they cost go unproduced, or vice versa."),
 dict(q="A competitive firm produces 500 units at a price of $6 with an average total cost of $4. Its profit is", choices=[
   "$2", "$500", "$1,000", "$2,000", "$3,000"], ans=2,
   why="(6 − 4) × 500 = $1,000."),
 dict(q="A competitive firm produces 250 units at a price of $7 with an average total cost of $8. It is", choices=[
   "earning $250", "losing $250", "breaking even", "earning $1,750", "losing $1"], ans=1,
   why="(7 − 8) × 250 = −$250."),
 dict(q="A competitive firm produces where MC = $15 and price is $15, with ATC = $12. Its per-unit profit is", choices=[
   "$0", "$3", "$12", "$15", "$27"], ans=1,
   why="Per-unit profit is P − ATC = 15 − 12 = $3."),
 dict(q="An increase in market demand in a competitive industry causes the individual firm, in the short run, to", choices=[
   "reduce output", "increase output and possibly earn economic profit", "shut down", "exit", "lower its price"], ans=1,
   why="A higher price meets MC at a larger quantity."),
 dict(q="A decrease in market demand in a competitive industry causes the individual firm, in the short run, to", choices=[
   "increase output", "reduce output and possibly incur a loss", "raise its price", "earn more profit", "expand its plant"], ans=1,
   why="A lower price meets MC at a smaller quantity."),
 dict(q="A perfectly competitive firm's marginal revenue curve is", choices=[
   "downward sloping",
   "horizontal and identical to its demand curve",
   "upward sloping",
   "below its average revenue curve",
   "vertical"], ans=1,
   why="Every unit sells at the same market price, so MR = AR = P."),
 dict(q="Which of the following would make a market less like perfect competition?", choices=[
   "an increase in the number of sellers",
   "the emergence of strong brand loyalty for one firm's product",
   "better information for buyers",
   "removal of licensing requirements",
   "standardization of the product"], ans=1,
   why="Brand loyalty gives a firm some ability to raise price without losing all buyers."),
 dict(q="In perfect competition, an individual firm's output decision has", choices=[
   "a large effect on market price",
   "essentially no effect on market price",
   "a direct effect on market demand",
   "no effect on its own profit",
   "no relation to marginal cost"], ans=1,
   why="Its share of total output is negligible."),
 dict(q="Which of the following is true of a competitive firm in long-run equilibrium?", choices=[
   "P > MC", "P = MC = minimum ATC", "P < ATC", "MR > MC", "P = AVC"], ans=1,
   why="All three coincide when entry has eliminated economic profit."),
 dict(q="Free entry and exit in perfect competition ensures that in the long run", choices=[
   "economic profit is positive",
   "economic profit tends toward zero",
   "accounting profit is zero",
   "firms leave the market entirely",
   "prices rise steadily"], ans=1,
   why="Entry erodes profits and exit erases losses."),
 dict(q="A competitive market's equilibrium price is $14 and a firm's minimum ATC is $14. This firm is", choices=[
   "earning positive economic profit",
   "earning normal profit and has no incentive to enter or leave",
   "losing money",
   "about to shut down",
   "producing below minimum AVC"], ans=1,
   why="Zero economic profit is exactly the long-run equilibrium condition."),
 dict(q="Compared with a monopoly serving the same demand and cost conditions, a perfectly competitive industry generally produces", choices=[
   "less output at a higher price",
   "more output at a lower price",
   "the same output at the same price",
   "less output at a lower price",
   "no output"], ans=1,
   why="Price equals marginal cost in competition rather than exceeding it."),
 dict(q="A perfectly competitive firm's decision about how much to produce depends on", choices=[
   "the price it chooses to set",
   "its marginal cost relative to the given market price",
   "the market demand curve's slope",
   "advertising expenditures",
   "the number of buyers it can attract"], ans=1,
   why="With price given, only cost varies with output."),
 dict(q="If the market price equals a competitive firm's minimum average variable cost, the firm's loss equals", choices=[
   "zero", "its total fixed cost", "its total variable cost", "its total cost", "its marginal cost"], ans=1,
   why="Revenue exactly covers variable cost, leaving fixed cost uncovered."),
 dict(q="An industry has 500 identical firms, each producing 200 units. Market output is", choices=[
   "700", "2.5", "100,000", "500", "200"], ans=2,
   why="500 × 200 = 100,000 units."),
 dict(q="If market demand at a price of $6 is 90,000 units and each competitive firm produces 300 units at that price, the number of firms is", choices=[
   "300", "600", "3,000", "90,000", "1,500"], ans=0,
   why="90,000 ÷ 300 = 300 firms."),
 dict(q="Which statement about a perfectly competitive firm is correct?", choices=[
   "It maximizes profit by maximizing total revenue.",
   "It maximizes profit by producing where the market price equals its marginal cost.",
   "It sets price above marginal cost.",
   "It always earns positive economic profit.",
   "It faces a downward-sloping demand curve."], ans=1,
   why="P = MR for a price taker, so MR = MC becomes P = MC."),
]
