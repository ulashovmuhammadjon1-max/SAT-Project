# 3.6 Firms' Entry and Exit Decisions in the Long Run — 50 questions
# Scenario table verified (P vs cost curves at the firm's chosen output):
#   Firm A: P=20 ATC=16 AVC=11 -> profit, entry follows
#   Firm B: P=14 ATC=14 AVC=9  -> zero economic profit, long-run equilibrium
#   Firm C: P=12 ATC=17 AVC=10 -> loss but operates in short run, exit in long run
#   Firm D: P=8  ATC=15 AVC=11 -> shut down now, exit in long run
TOPIC = ("3.6", "Firms' Entry and Exit Decisions in the Long Run", 3)
ENTRY = dict(headers=["Firm", "Price", "ATC", "AVC"],
             rows=[["A", "$20", "$16", "$11"], ["B", "$14", "$14", "$9"],
                   ["C", "$12", "$17", "$10"], ["D", "$8", "$15", "$11"]])
QUESTIONS = [
 dict(q="In the long run, firms enter a perfectly competitive industry when existing firms earn", choices=[
   "zero economic profit", "positive economic profit", "negative economic profit",
   "zero accounting profit", "normal profit"], ans=1,
   why="Returns above the normal level attract new resources into the industry."),
 dict(q="In the long run, firms exit a perfectly competitive industry when existing firms earn", choices=[
   "positive economic profit", "negative economic profit", "zero economic profit",
   "normal profit", "positive accounting profit"], ans=1,
   why="If resources earn less here than elsewhere, they leave."),
 dict(q="Entry of new firms into a competitive industry shifts the market supply curve", choices=[
   "leftward, raising price", "rightward, lowering price", "not at all",
   "rightward, raising price", "leftward, lowering price"], ans=1,
   why="More sellers means more output offered at every price, driving price down."),
 dict(q="Exit of firms from a competitive industry shifts the market supply curve", choices=[
   "rightward, lowering price", "leftward, raising price", "not at all",
   "leftward, lowering price", "rightward, raising price"], ans=1,
   why="Fewer sellers reduces supply and pushes price up."),
 dict(q="Entry continues until", choices=[
   "price falls to the minimum of average variable cost",
   "economic profit is driven to zero",
   "all firms exit",
   "price equals marginal cost only",
   "accounting profit is zero"], ans=1,
   why="The incentive to enter disappears exactly when economic profit reaches zero."),
 dict(q="In long-run competitive equilibrium, price equals", choices=[
   "minimum average variable cost",
   "marginal cost and the minimum of average total cost simultaneously",
   "average fixed cost",
   "marginal revenue only",
   "the maximum of average total cost"], ans=1,
   why="P = MC comes from profit maximization and P = min ATC from free entry and exit."),
 dict(q="Using the table, Firm A is earning", table=ENTRY, choices=[
   "an economic loss", "a positive economic profit", "zero economic profit",
   "normal profit only", "revenue below variable cost"], ans=1,
   why="Price of $20 exceeds ATC of $16."),
 dict(q="Using the table, we would expect the industry containing Firm A to see", table=ENTRY, choices=[
   "firms exit", "new firms enter", "no change", "the price rise further", "all firms shut down"], ans=1,
   why="Positive economic profit attracts entry."),
 dict(q="Using the table, Firm B is", table=ENTRY, choices=[
   "earning a positive economic profit",
   "in long-run equilibrium, earning zero economic profit",
   "suffering a loss",
   "about to shut down",
   "earning zero accounting profit"], ans=1,
   why="Price equals ATC, so economic profit is zero."),
 dict(q="Using the table, Firm C should in the short run", table=ENTRY, choices=[
   "shut down, since price is below average total cost",
   "keep operating, since price of $12 exceeds average variable cost of $10",
   "expand output substantially",
   "raise its price to $17",
   "exit immediately"], ans=1,
   why="Price above AVC means operating loses less than the fixed cost alone."),
 dict(q="Using the table, in the long run Firm C will", table=ENTRY, choices=[
   "continue operating indefinitely at a loss",
   "exit the industry unless price rises",
   "earn positive economic profit",
   "become a monopoly",
   "have zero fixed costs"], ans=1,
   why="Long-run losses cannot be sustained when every cost is avoidable."),
 dict(q="Using the table, Firm D should in the short run", table=ENTRY, choices=[
   "keep producing",
   "shut down, since the $8 price is below its $11 average variable cost",
   "expand output",
   "exactly break even",
   "earn normal profit"], ans=1,
   why="Below AVC, each unit produced adds to the loss."),
 dict(q="Using the table, which firm is in long-run equilibrium?", table=ENTRY, choices=[
   "A", "B", "C", "D", "none of them"], ans=1,
   why="Only Firm B has price equal to average total cost."),
 dict(q="Using the table, which firm's industry would see supply shift rightward over time?", table=ENTRY, choices=[
   "A, because profits attract entry", "B", "C", "D", "none"], ans=0,
   why="Entry into a profitable industry expands market supply."),
 dict(q="As firms enter a competitive industry, an individual existing firm's demand curve", choices=[
   "shifts upward",
   "shifts downward as the market price falls",
   "becomes downward sloping",
   "becomes vertical",
   "is unaffected"], ans=1,
   why="The firm's horizontal demand curve sits at the market price, which entry lowers."),
 dict(q="As firms exit a competitive industry, the remaining firms' economic profit", choices=[
   "falls further", "rises toward zero as price increases", "stays negative forever",
   "becomes permanently positive", "is unaffected"], ans=1,
   why="Reduced supply raises price, shrinking each surviving firm's loss."),
 dict(q="The long-run adjustment process in a competitive market ends when", choices=[
   "only one firm remains",
   "there is no incentive for any firm to enter or leave",
   "price equals average variable cost",
   "all firms shut down",
   "marginal cost is zero"], ans=1,
   why="Equilibrium is defined by the absence of an incentive to change."),
 dict(q="A key condition that makes long-run zero economic profit possible in perfect competition is", choices=[
   "government price controls",
   "free entry into and exit from the industry",
   "product differentiation",
   "barriers to entry",
   "a single large seller"], ans=1,
   why="Without free entry and exit, profits or losses could persist."),
 dict(q="In long-run competitive equilibrium, each firm produces at", choices=[
   "an output above minimum ATC",
   "the minimum point of its average total cost curve",
   "the minimum of average variable cost",
   "an output where MC exceeds price",
   "zero output"], ans=1,
   why="Price is competed down to minimum ATC, and P = MC there."),
 dict(q="Productive efficiency in long-run competitive equilibrium means the firm", choices=[
   "produces the socially optimal quantity",
   "produces at the lowest possible average total cost",
   "earns maximum profit",
   "sets price above marginal cost",
   "minimizes fixed cost"], ans=1,
   why="Productive efficiency is producing at minimum ATC."),
 dict(q="Allocative efficiency in long-run competitive equilibrium means", choices=[
   "average total cost is minimized",
   "price equals marginal cost, so the value of the last unit to buyers equals its cost",
   "economic profit is positive",
   "output is as large as possible",
   "no firms exit"], ans=1,
   why="P = MC aligns the marginal benefit of the last unit with its marginal cost."),
 dict(q="A constant-cost industry has a long-run supply curve that is", choices=[
   "upward sloping", "horizontal", "downward sloping", "vertical", "U-shaped"], ans=1,
   why="If input prices do not change as the industry expands, output grows at an unchanged price."),
 dict(q="An increasing-cost industry has a long-run supply curve that is", choices=[
   "horizontal", "upward sloping", "downward sloping", "vertical", "backward bending"], ans=1,
   why="Expansion bids up input prices, so a higher price is needed to sustain more output."),
 dict(q="A decreasing-cost industry has a long-run supply curve that is", choices=[
   "upward sloping", "downward sloping", "horizontal", "vertical", "identical to marginal cost"], ans=1,
   why="Expansion lowers input costs, so more output can be supplied at a lower price."),
 dict(q="A permanent increase in demand in a constant-cost competitive industry will, in the long run, lead to", choices=[
   "a permanently higher price",
   "a larger industry output at the original price",
   "a permanently lower price",
   "fewer firms",
   "positive economic profit forever"], ans=1,
   why="Entry restores the original price while expanding total output."),
 dict(q="A permanent decrease in demand in a competitive industry will, in the long run, lead to", choices=[
   "more firms in the industry",
   "exit until the surviving firms again earn zero economic profit",
   "permanently negative economic profit",
   "a higher long-run price than before in a constant-cost industry",
   "no change in the number of firms"], ans=1,
   why="Losses drive exit until price recovers to minimum ATC."),
 dict(q="In the short run following an increase in demand, a competitive firm will", choices=[
   "earn zero economic profit",
   "earn positive economic profit as price rises above ATC",
   "shut down",
   "exit",
   "face a downward-sloping demand curve"], ans=1,
   why="Before entry occurs, the higher price exceeds average total cost."),
 dict(q="The number of firms in a competitive industry in the long run is determined by", choices=[
   "government licensing",
   "the level of demand relative to the output each firm produces at minimum ATC",
   "the size of fixed costs alone",
   "the marginal revenue curve",
   "the shutdown price"], ans=1,
   why="Market quantity at the long-run price divided by each firm's efficient scale gives the number of firms."),
 dict(q="A competitive industry's long-run price in a constant-cost industry is set by", choices=[
   "market demand alone",
   "the minimum of the typical firm's long-run average total cost",
   "the maximum of average variable cost",
   "the largest firm's marginal cost",
   "the government"], ans=1,
   why="Entry and exit force price to that minimum."),
 dict(q="If the long-run price in a competitive industry is $25 and a firm's minimum LRATC is $30, that firm will", choices=[
   "earn positive economic profit",
   "exit the industry",
   "expand",
   "break even",
   "become the market leader"], ans=1,
   why="It cannot cover its costs at the prevailing price."),
 dict(q="A firm with lower costs than its competitors in a competitive industry may", choices=[
   "never earn economic profit",
   "earn positive economic profit even in long-run equilibrium",
   "be forced to exit",
   "set a higher price",
   "face a downward-sloping demand curve"], ans=1,
   why="Entry drives price to the typical firm's minimum ATC, which is above a low-cost firm's."),
 dict(q="Exit differs from shutting down in that exit", choices=[
   "is a short-run decision",
   "is a long-run decision in which the firm leaves the industry and sheds all of its costs",
   "still leaves the firm paying variable costs",
   "requires the firm to keep producing",
   "raises fixed cost"], ans=1,
   why="Shutting down halts production while fixed costs continue; exit ends them."),
 dict(q="A firm shuts down but does not exit when", choices=[
   "it expects the low price to be permanent",
   "the price is temporarily below AVC but expected to recover",
   "it has no fixed costs",
   "it earns economic profit",
   "price exceeds ATC"], ans=1,
   why="Keeping the plant preserves the option to resume when conditions improve."),
 dict(q="Which of the following is a barrier that would prevent long-run zero economic profit?", choices=[
   "many small sellers",
   "a government-granted exclusive license to produce",
   "identical products",
   "perfect information",
   "free exit"], ans=1,
   why="A legal barrier blocks the entry that would compete profits away."),
 dict(q="A competitive market with positive economic profits and no entry barriers will see profits", choices=[
   "persist indefinitely", "eroded by entry over time", "grow", "become sunk costs", "become fixed costs"], ans=1,
   why="Entry increases supply, lowering price and profit."),
 dict(q="In long-run equilibrium a competitive firm's marginal cost equals", choices=[
   "average variable cost only",
   "price and minimum average total cost",
   "average fixed cost",
   "zero",
   "total revenue"], ans=1,
   why="At the minimum of ATC the MC curve passes through, and price sits there too."),
 dict(q="If a competitive industry's firms are earning economic losses, in the long run the market price will", choices=[
   "fall further", "rise as firms exit and supply decreases", "stay the same", "fall to zero", "be set by the government"], ans=1,
   why="Exit shifts supply left, raising price."),
 dict(q="The speed of long-run adjustment in a competitive industry depends mainly on", choices=[
   "the elasticity of demand only",
   "how quickly firms can build or dismantle plants and enter or leave",
   "the level of fixed cost",
   "the number of consumers",
   "the tax rate"], ans=1,
   why="Adjustment is limited by how fast capacity can change."),
 dict(q="Which of the following signals that resources should move into an industry?", choices=[
   "economic losses", "positive economic profits", "zero economic profit", "high fixed costs", "declining demand"], ans=1,
   why="Profits above normal indicate the resources are more valuable here than elsewhere."),
 dict(q="Which of the following signals that resources should move out of an industry?", choices=[
   "positive economic profits", "sustained economic losses", "normal profit", "rising demand", "falling input prices"], ans=1,
   why="Losses mean the resources would be worth more in another use."),
 dict(q="In a constant-cost industry, an increase in demand causes the long-run number of firms to", choices=[
   "fall", "rise", "stay the same", "fall to one", "become zero"], ans=1,
   why="Total output expands at the same per-firm efficient scale, so more firms operate."),
 dict(q="A firm's decision to exit in the long run is based on comparing price with", choices=[
   "average variable cost", "long-run average total cost", "average fixed cost", "marginal revenue only", "total fixed cost"], ans=1,
   why="In the long run every cost is avoidable, so LRATC is the relevant benchmark."),
 dict(q="A firm's decision to shut down in the short run is based on comparing price with", choices=[
   "average total cost", "average variable cost", "average fixed cost", "long-run average cost", "total cost"], ans=1,
   why="Only variable costs can be avoided by halting production."),
 dict(q="An industry in long-run equilibrium experiences a permanent fall in input prices. In the new long-run equilibrium", choices=[
   "price is higher and firms earn profit",
   "price is lower, matching the new lower minimum average total cost",
   "price is unchanged",
   "all firms exit",
   "economic profit is permanently positive"], ans=1,
   why="Entry competes the temporary profits away at the new, lower cost level."),
 dict(q="If a competitive firm earns zero economic profit in the long run, its owners are", choices=[
   "earning nothing and should leave",
   "earning exactly what they could earn in their next-best alternative",
   "losing money",
   "earning above-normal returns",
   "paying no implicit costs"], ans=1,
   why="Zero economic profit is normal profit, the opportunity-cost break-even."),
 dict(q="A subsidy paid per unit to every firm in a competitive industry will, in the long run", choices=[
   "leave price unchanged",
   "attract entry and push price down until economic profit returns to zero",
   "permanently raise economic profit",
   "cause exit",
   "raise the market price"], ans=1,
   why="Free entry dissipates any advantage shared by all firms."),
 dict(q="Which of the following best explains why a competitive firm cannot earn long-run economic profit?", choices=[
   "It faces a downward-sloping demand curve.",
   "Nothing prevents other firms from copying it and entering the market.",
   "Its marginal cost is always zero.",
   "The government caps its price.",
   "It has no fixed costs."], ans=1,
   why="Free entry is the mechanism that erases the profit."),
 dict(q="A competitive industry currently has 100 firms and price above minimum ATC. Over time we expect the number of firms to", choices=[
   "fall below 100", "rise above 100", "stay at exactly 100", "fall to zero", "be unaffected by profit"], ans=1,
   why="Positive economic profit invites entry."),
 dict(q="A competitive industry currently has 80 firms and price below minimum ATC but above minimum AVC. Over time we expect", choices=[
   "immediate shutdown of all firms",
   "gradual exit until price rises to minimum ATC",
   "entry of new firms",
   "price to fall further permanently",
   "no change"], ans=1,
   why="Firms operate through the short run but leave as their capital wears out."),
 dict(q="Long-run equilibrium in perfect competition is efficient because", choices=[
   "firms earn maximum profit",
   "output is produced at the lowest possible average cost and sold at a price equal to marginal cost",
   "price exceeds marginal cost",
   "there are few firms",
   "fixed costs are zero"], ans=1,
   why="Both productive and allocative efficiency hold simultaneously."),
]
