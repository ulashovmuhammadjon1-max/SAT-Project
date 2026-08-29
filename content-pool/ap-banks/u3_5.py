# 3.5 Profit Maximization — 50 questions
# Table verified: P = $12 (price taker), so MR = 12 at every Q.
#   Q=1 MC=6  Q=2 MC=8  Q=3 MC=10  Q=4 MC=12  Q=5 MC=16
#   Profit-maximizing output is 4, where MR = MC = 12.
TOPIC = ("3.5", "Profit Maximization", 3)
MRMC = dict(headers=["Quantity", "Marginal cost"],
            rows=[["1", "$6"], ["2", "$8"], ["3", "$10"], ["4", "$12"], ["5", "$16"]])
QUESTIONS = [
 dict(q="A firm maximizes profit by producing the quantity at which", choices=[
   "total revenue is at its maximum",
   "marginal revenue equals marginal cost",
   "average total cost is at its minimum",
   "price equals average total cost",
   "marginal cost is at its minimum"], ans=1,
   why="The MR = MC rule identifies the last unit worth producing."),
 dict(q="Marginal revenue is", choices=[
   "total revenue divided by quantity",
   "the change in total revenue from selling one more unit",
   "price times quantity",
   "the change in total cost",
   "profit per unit"], ans=1,
   why="MR = ΔTR/ΔQ."),
 dict(q="If marginal revenue exceeds marginal cost, the firm should", choices=[
   "reduce output", "increase output", "shut down", "leave output unchanged", "raise its price"], ans=1,
   why="The next unit adds more to revenue than to cost, so it adds to profit."),
 dict(q="If marginal cost exceeds marginal revenue, the firm should", choices=[
   "increase output", "reduce output", "shut down immediately", "raise fixed cost", "leave output unchanged"], ans=1,
   why="The last unit costs more than it brings in, so cutting it raises profit."),
 dict(q="For a perfectly competitive firm, marginal revenue equals", choices=[
   "average total cost", "the market price", "average variable cost", "zero", "total revenue"], ans=1,
   why="A price taker sells every additional unit at the going market price."),
 dict(q="A perfectly competitive firm's demand curve is", choices=[
   "downward sloping",
   "horizontal at the market price",
   "vertical",
   "upward sloping",
   "the same as the market demand curve"], ans=1,
   why="The firm is too small to affect price, so it faces a perfectly elastic demand curve."),
 dict(q="For a perfectly competitive firm, the profit-maximizing rule can be written as", choices=[
   "P = ATC", "P = MC", "P = AVC", "MR = ATC", "MC = AFC"], ans=1,
   why="Since P = MR for a price taker, MR = MC becomes P = MC."),
 dict(q="Using the table, if the market price is $12, the profit-maximizing output is", table=MRMC, choices=[
   "1", "2", "3", "4", "5"], ans=3,
   why="MR is $12 at every quantity, and MC reaches $12 at the fourth unit."),
 dict(q="Using the table with a price of $12, the firm should not produce the fifth unit because", table=MRMC, choices=[
   "its marginal cost of $16 exceeds the $12 it would add to revenue",
   "its marginal cost is below price",
   "average total cost is falling",
   "fixed cost would rise",
   "marginal revenue would fall"], ans=0,
   why="A unit costing $16 that sells for $12 reduces profit by $4."),
 dict(q="Using the table with a price of $12, producing only 2 units would be a mistake because", table=MRMC, choices=[
   "the third and fourth units each add more to revenue than to cost",
   "marginal cost is too high at 2 units",
   "the firm would earn no revenue",
   "average cost would be minimized",
   "marginal revenue would exceed price"], ans=0,
   why="At Q = 3 and Q = 4, MC of $10 and $12 is at or below the $12 price."),
 dict(q="Using the table, if the market price fell to $8, the profit-maximizing output would be", table=MRMC, choices=[
   "1", "2", "3", "4", "0"], ans=1,
   why="MC reaches $8 at the second unit; the third costs $10, more than the price."),
 dict(q="Using the table, if the market price rose to $16, the profit-maximizing output would be", table=MRMC, choices=[
   "2", "3", "4", "5", "6"], ans=3,
   why="MC reaches $16 at the fifth unit."),
 dict(q="Using the table, the firm's marginal cost schedule above minimum AVC is also its", table=MRMC, choices=[
   "demand curve", "short-run supply curve", "average cost curve", "total revenue curve", "marginal revenue curve"], ans=1,
   why="A price taker's output response to price is traced by its marginal cost curve."),
 dict(q="Producing where MR = MC maximizes profit rather than revenue because", choices=[
   "revenue is irrelevant",
   "profit is revenue minus cost, and the rule stops production exactly where an added unit stops adding to that difference",
   "marginal cost is always zero",
   "total revenue is always maximized at the same point",
   "average cost is minimized there"], ans=1,
   why="Maximizing revenue ignores what the extra units cost."),
 dict(q="A firm that produces where average total cost is minimized rather than where MR = MC will", choices=[
   "always earn higher profit",
   "generally earn less than the maximum profit",
   "earn zero revenue",
   "shut down",
   "produce the same quantity"], ans=1,
   why="Lowest average cost is not the same target as the largest gap between revenue and cost."),
 dict(q="In the short run, a firm should shut down if price is", choices=[
   "below average total cost",
   "below minimum average variable cost",
   "below marginal cost",
   "above average fixed cost",
   "equal to marginal revenue"], ans=1,
   why="If revenue cannot even cover variable cost, producing loses more than the fixed cost alone."),
 dict(q="A firm that shuts down in the short run incurs a loss equal to", choices=[
   "zero", "its total fixed cost", "its total variable cost", "its total cost", "its marginal cost"], ans=1,
   why="Fixed costs are owed whether or not the firm produces."),
 dict(q="If price is above minimum AVC but below minimum ATC, in the short run the firm should", choices=[
   "shut down",
   "keep producing, since it covers all variable cost and part of fixed cost",
   "exit the industry immediately",
   "raise its price",
   "produce where P = AVC"], ans=1,
   why="Operating loses less than shutting down when revenue exceeds variable cost."),
 dict(q="The shutdown point occurs at the", choices=[
   "minimum of average total cost",
   "minimum of average variable cost",
   "minimum of marginal cost",
   "maximum of average fixed cost",
   "point where price equals average fixed cost"], ans=1,
   why="Below minimum AVC, no output level covers variable cost."),
 dict(q="The break-even point for a competitive firm occurs where price equals", choices=[
   "minimum average variable cost",
   "minimum average total cost",
   "marginal cost at any output",
   "average fixed cost",
   "zero"], ans=1,
   why="At minimum ATC the firm earns exactly zero economic profit."),
 dict(q="A perfectly competitive firm's short-run supply curve is its", choices=[
   "average total cost curve",
   "marginal cost curve above minimum average variable cost",
   "average variable cost curve",
   "demand curve",
   "marginal revenue curve"], ans=1,
   why="For each price, the firm supplies where P = MC, as long as it is worth operating."),
 dict(q="A firm faces a price of $20. At its profit-maximizing output of 50 units, ATC is $16. Its profit is", choices=[
   "$4", "$200", "$800", "$1,000", "$180"], ans=2,
   why="(20 − 16) × 50 = $800."),
 dict(q="A firm faces a price of $9. At its profit-maximizing output of 120 units, ATC is $11. Its loss is", choices=[
   "$2", "$120", "$240", "$1,080", "$1,320"], ans=2,
   why="(9 − 11) × 120 = −$240."),
 dict(q="A competitive firm sells at $30 and produces 200 units where ATC is $30. Its economic profit is", choices=[
   "$6,000", "zero", "$200", "$30", "cannot be determined"], ans=1,
   why="Price equals average total cost, so profit is zero."),
 dict(q="At the profit-maximizing output, a firm's profit per unit is measured by the vertical distance between", choices=[
   "price and marginal cost",
   "price and average total cost",
   "price and average variable cost",
   "marginal revenue and marginal cost",
   "ATC and AVC"], ans=1,
   why="Per-unit profit is what the unit sells for minus what it costs on average."),
 dict(q="Total profit on a graph is shown as the area of a rectangle whose height is", choices=[
   "price minus average total cost and whose width is the quantity produced",
   "marginal cost and whose width is price",
   "average variable cost and whose width is fixed cost",
   "price and whose width is marginal revenue",
   "average fixed cost and whose width is output"], ans=0,
   why="Per-unit profit times quantity equals total profit."),
 dict(q="A firm should produce where MR = MC on the portion of the MC curve that is", choices=[
   "downward sloping", "upward sloping", "horizontal", "vertical", "below AFC"], ans=1,
   why="Where MC is falling, MR = MC identifies a profit minimum rather than a maximum."),
 dict(q="If MR = MC at two output levels, the profit-maximizing one is", choices=[
   "the smaller output, where MC is falling",
   "the larger output, where MC is rising",
   "either one, since profit is the same",
   "neither one",
   "the one with lower fixed cost"], ans=1,
   why="Profit increases between the two points, so the larger output is the maximum."),
 dict(q="A perfectly competitive firm cannot raise its price above the market price because", choices=[
   "the government forbids it",
   "buyers would purchase the identical product from other sellers instead",
   "its marginal cost would rise",
   "it would violate the MR = MC rule",
   "fixed costs would increase"], ans=1,
   why="With a homogeneous product and many sellers, demand for one firm's output at a higher price is zero."),
 dict(q="A perfectly competitive firm has no reason to lower its price below the market price because", choices=[
   "it can already sell as much as it wants at the market price",
   "marginal cost would fall",
   "the government sets a floor",
   "demand is inelastic",
   "average total cost would rise"], ans=0,
   why="Facing a horizontal demand curve, cutting price only reduces revenue per unit."),
 dict(q="Total revenue for a perfectly competitive firm rises", choices=[
   "at a decreasing rate as output rises",
   "at a constant rate equal to the market price",
   "then falls",
   "only if price rises",
   "at an increasing rate"], ans=1,
   why="Each unit adds exactly the market price to revenue, so TR is a straight line."),
 dict(q="If a competitive firm's total revenue is $4,000 at 200 units, the market price is", choices=[
   "$2", "$20", "$200", "$4,000", "cannot be determined"], ans=1,
   why="P = TR/Q = 4,000/200 = $20."),
 dict(q="At the profit-maximizing output, marginal cost is $14 and the market price is $14. The firm's economic profit", choices=[
   "must be zero",
   "could be positive, negative, or zero depending on average total cost",
   "must be positive",
   "must be negative",
   "equals $14 per unit"], ans=1,
   why="P = MC fixes the quantity; profit depends on how ATC compares with price."),
 dict(q="A firm operating at a loss in the short run should continue producing as long as total revenue exceeds", choices=[
   "total cost", "total variable cost", "total fixed cost", "marginal cost", "average total cost"], ans=1,
   why="Any revenue above variable cost reduces the loss below the fixed cost the firm would bear if shut."),
 dict(q="A firm has total revenue of $9,000, total variable cost of $7,000, and total fixed cost of $4,000. In the short run it should", choices=[
   "shut down, losing $4,000",
   "keep operating, since it loses $2,000 rather than $4,000",
   "keep operating and earn a profit of $2,000",
   "exit the industry today",
   "raise its price"], ans=1,
   why="Operating covers all variable cost plus $2,000 of the fixed cost."),
 dict(q="A firm has total revenue of $5,000, total variable cost of $6,500, and total fixed cost of $3,000. In the short run it should", choices=[
   "keep operating, losing $4,500",
   "shut down, losing only the $3,000 fixed cost",
   "keep operating and earn a profit",
   "expand output",
   "raise its fixed cost"], ans=1,
   why="Revenue does not cover variable cost, so producing adds $1,500 to the loss."),
 dict(q="An increase in a firm's fixed cost will change its profit-maximizing output by", choices=[
   "raising it", "lowering it", "leaving it unchanged in the short run", "reducing it to zero", "doubling it"], ans=2,
   why="Fixed cost does not enter marginal cost, so the MR = MC quantity is unaffected."),
 dict(q="An increase in a firm's variable cost per unit will", choices=[
   "leave the profit-maximizing output unchanged",
   "shift marginal cost upward and reduce the profit-maximizing output at a given price",
   "raise the profit-maximizing output",
   "affect only fixed cost",
   "raise marginal revenue"], ans=1,
   why="Higher MC intersects the unchanged MR at a smaller quantity."),
 dict(q="A per-unit tax on output will", choices=[
   "shift marginal cost up and reduce the firm's output",
   "shift only average fixed cost",
   "leave marginal cost unchanged",
   "raise the firm's profit",
   "increase output"], ans=0,
   why="A tax paid on each unit adds to the cost of producing that unit."),
 dict(q="A lump-sum tax on a firm will", choices=[
   "reduce output in the short run",
   "reduce profit but leave the profit-maximizing output unchanged in the short run",
   "raise marginal cost",
   "raise output",
   "have no effect on profit"], ans=1,
   why="A fixed payment does not change the cost of an additional unit."),
 dict(q="A competitive firm produces where P = MC. If price rises, the firm's output will", choices=[
   "fall", "rise", "stay the same", "fall to zero", "become undefined"], ans=1,
   why="A higher price meets the upward-sloping MC curve at a larger quantity."),
 dict(q="A competitive firm's profit-maximizing output when price is below minimum AVC is", choices=[
   "where P = MC", "zero", "at minimum ATC", "where P = ATC", "unlimited"], ans=1,
   why="Shutting down is the loss-minimizing choice, so the firm supplies nothing."),
 dict(q="The MR = MC rule applies to", choices=[
   "perfectly competitive firms only",
   "all profit-maximizing firms in every market structure",
   "monopolies only",
   "firms with no fixed costs",
   "firms in the long run only"], ans=1,
   why="What differs across market structures is the shape of MR, not the rule."),
 dict(q="For a firm facing a downward-sloping demand curve, marginal revenue is", choices=[
   "equal to price", "less than price", "greater than price", "constant at zero", "equal to marginal cost always"], ans=1,
   why="Selling an extra unit requires lowering the price on all units, so MR falls below P."),
 dict(q="A firm producing 30 units earns a profit of $150. At 31 units it earns $158. This suggests that at 30 units", choices=[
   "MC exceeded MR", "MR exceeded MC", "MR equaled MC", "the firm should shut down", "profit was maximized"], ans=1,
   why="Profit rose by $8, so the 31st unit added more revenue than cost."),
 dict(q="A firm producing 40 units earns a profit of $300. At 41 units it earns $295. The firm should", choices=[
   "produce 41 units", "produce 40 units", "produce 45 units", "shut down", "raise price"], ans=1,
   why="The 41st unit reduced profit, so output should stop at 40."),
 dict(q="If a competitive firm's price equals minimum average variable cost, the firm is", choices=[
   "earning zero economic profit",
   "indifferent between producing and shutting down, since either way it loses its fixed cost",
   "earning positive profit",
   "at the break-even point",
   "producing where P = ATC"], ans=1,
   why="Revenue covers variable cost exactly, so the loss equals fixed cost in both cases."),
 dict(q="At its profit-maximizing output a competitive firm has P = $18, ATC = $22, and AVC = $16. It should", choices=[
   "shut down immediately",
   "continue producing in the short run, since price exceeds average variable cost",
   "raise price to $22",
   "exit today",
   "expand output substantially"], ans=1,
   why="Price above AVC means operating covers variable cost and part of fixed cost."),
 dict(q="At its profit-maximizing output a competitive firm has P = $10, ATC = $15, and AVC = $12. It should", choices=[
   "continue producing",
   "shut down in the short run",
   "expand output",
   "raise price to $15",
   "be indifferent"], ans=1,
   why="Price below AVC means every unit produced deepens the loss."),
 dict(q="The main reason a firm does not simply maximize total revenue is that", choices=[
   "revenue is impossible to measure",
   "producing extra units to raise revenue can add more to cost than to revenue",
   "revenue is always zero",
   "marginal cost is constant",
   "price is fixed by law"], ans=1,
   why="Profit is the objective, and beyond MR = MC the extra units are loss-making."),
]
