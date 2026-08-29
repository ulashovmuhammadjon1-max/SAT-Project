# 4.3 Price Discrimination — 50 questions
TOPIC = ("4.3", "Price Discrimination", 4)
PD = dict(headers=["Buyer", "Willingness to pay"],
          rows=[["1", "$10"], ["2", "$8"], ["3", "$6"], ["4", "$4"]])
QUESTIONS = [
 dict(q="Price discrimination is the practice of", choices=[
   "charging every customer the same price",
   "charging different buyers different prices for the same good for reasons not based on cost differences",
   "selling below marginal cost",
   "refusing to serve some customers",
   "setting price equal to average cost"], ans=1,
   why="The differing prices reflect differing willingness to pay, not differing costs."),
 dict(q="Which of the following is NOT required for a firm to price discriminate?", choices=[
   "some market power",
   "the ability to identify buyers with different willingness to pay",
   "the ability to prevent resale between buyers",
   "a perfectly elastic demand curve",
   "the ability to charge different prices"], ans=3,
   why="A price taker facing perfectly elastic demand cannot charge different prices at all."),
 dict(q="A firm that cannot prevent resale will find price discrimination fails because", choices=[
   "buyers charged the low price will resell to those charged the high price",
   "its marginal cost will rise",
   "demand becomes inelastic",
   "the government forbids it",
   "consumers stop buying entirely"], ans=0,
   why="Arbitrage collapses the two prices into one."),
 dict(q="Perfect, or first-degree, price discrimination means the firm", choices=[
   "charges everyone the same price",
   "charges each buyer exactly his or her maximum willingness to pay",
   "charges two prices only",
   "sells at marginal cost to everyone",
   "charges the lowest price to everyone"], ans=1,
   why="Every unit is sold for the most that particular buyer would pay."),
 dict(q="Under perfect price discrimination, consumer surplus is", choices=[
   "maximized", "zero, because every buyer pays exactly what the good is worth to them",
   "unchanged from single pricing", "negative", "equal to producer surplus"], ans=1,
   why="The whole surplus is captured by the seller."),
 dict(q="Under perfect price discrimination, the deadweight loss of monopoly is", choices=[
   "doubled", "eliminated, because the firm produces up to the point where price equals marginal cost",
   "unchanged", "converted into consumer surplus", "made larger"], ans=1,
   why="With no need to cut the price on earlier units, MR equals price, so output reaches the efficient level."),
 dict(q="Under perfect price discrimination, the firm's marginal revenue curve is", choices=[
   "below its demand curve", "identical to its demand curve", "horizontal", "upward sloping", "negative"], ans=1,
   why="Each extra unit sells at its own price without lowering the price of earlier units."),
 dict(q="Perfect price discrimination is allocatively efficient but is often criticized because", choices=[
   "it produces too little output",
   "all of the gains from trade go to the seller rather than being shared with buyers",
   "price is below marginal cost",
   "the firm earns no profit",
   "output exceeds the efficient level"], ans=1,
   why="Efficiency and distribution are separate questions."),
 dict(q="Using the table, a single-price seller with a marginal cost of $6 charging $8 would sell to", table=PD, choices=[
   "buyer 1 only", "buyers 1 and 2", "buyers 1, 2, and 3", "all four buyers", "no one"], ans=1,
   why="Only buyers willing to pay at least $8 will purchase."),
 dict(q="Using the table, a single-price seller charging $8 earns revenue of", table=PD, choices=[
   "$8", "$16", "$18", "$24", "$28"], ans=1,
   why="Two buyers pay $8 each."),
 dict(q="Using the table, a perfectly price-discriminating seller with a marginal cost of $6 would sell to", table=PD, choices=[
   "buyer 1 only", "buyers 1 and 2", "buyers 1, 2, and 3", "all four buyers", "no one"], ans=2,
   why="It serves everyone whose willingness to pay is at least the $6 marginal cost."),
 dict(q="Using the table, a perfectly price-discriminating seller charging each buyer his maximum earns revenue from buyers 1-3 of", table=PD, choices=[
   "$18", "$24", "$28", "$10", "$16"], ans=1,
   why="10 + 8 + 6 = $24."),
 dict(q="Using the table, the consumer surplus of buyer 1 when a single price of $8 is charged is", table=PD, choices=[
   "$0", "$2", "$8", "$10", "$18"], ans=1,
   why="Willing to pay $10 but paying $8 leaves a $2 surplus."),
 dict(q="Using the table, buyer 1's consumer surplus under perfect price discrimination is", table=PD, choices=[
   "$10", "$2", "$0", "$8", "$6"], ans=2,
   why="Paying exactly the maximum willingness to pay leaves no surplus."),
 dict(q="Second-degree price discrimination charges different prices based on", choices=[
   "each individual buyer's identity",
   "the quantity purchased, as with bulk discounts",
   "the buyer's age only",
   "the seller's costs",
   "the time of year only"], ans=1,
   why="Buyers self-select into a pricing tier by how much they buy."),
 dict(q="A supermarket offering a lower unit price on a large package than on a small one is practising", choices=[
   "first-degree price discrimination", "second-degree price discrimination", "third-degree price discrimination",
   "predatory pricing", "average-cost pricing"], ans=1,
   why="The price varies with quantity purchased and buyers sort themselves."),
 dict(q="Third-degree price discrimination charges different prices to", choices=[
   "each individual buyer",
   "identifiable groups of buyers with different demand elasticities",
   "buyers of different quantities only",
   "everyone equally",
   "buyers in the same group"], ans=1,
   why="Groups such as students or seniors are charged different prices."),
 dict(q="A cinema charging students less than other adults is practising", choices=[
   "first-degree price discrimination", "second-degree price discrimination", "third-degree price discrimination",
   "cost-based pricing", "marginal-cost pricing"], ans=2,
   why="It is a group-based price difference not explained by cost."),
 dict(q="Under third-degree price discrimination, the group with the more elastic demand is charged", choices=[
   "a higher price", "a lower price", "the same price", "nothing", "marginal cost exactly"], ans=1,
   why="More price-sensitive buyers must be offered a lower price to be served."),
 dict(q="Under third-degree price discrimination, the group with the more inelastic demand is charged", choices=[
   "a lower price", "a higher price", "the same price", "nothing", "below marginal cost"], ans=1,
   why="Less price-sensitive buyers will pay more without dropping out."),
 dict(q="Airlines charging more for tickets booked at the last minute is price discrimination because", choices=[
   "the flight costs more to operate",
   "late bookers, often business travellers, have less elastic demand",
   "the seats are physically different",
   "fuel prices rise near departure",
   "the airline has no market power"], ans=1,
   why="The price difference tracks willingness to pay, not cost."),
 dict(q="Which of the following is NOT price discrimination?", choices=[
   "senior discounts at a museum",
   "charging more to ship a package a longer distance",
   "student discounts on software",
   "cheaper matinee film tickets",
   "lower prices for bulk purchases"], ans=1,
   why="A longer distance genuinely costs more, so the price difference is cost-based."),
 dict(q="A firm practising price discrimination will earn", choices=[
   "less profit than a single-price firm",
   "more profit than the same firm charging a single price",
   "the same profit",
   "zero profit",
   "negative profit"], ans=1,
   why="It can always replicate the single price and do better by tailoring."),
 dict(q="Price discrimination generally causes total output to", choices=[
   "fall below the single-price level",
   "rise above the single-price level, since buyers with lower willingness to pay can be served",
   "stay the same",
   "fall to zero",
   "exceed the efficient level"], ans=1,
   why="Low-value buyers can be served without cutting the price to everyone."),
 dict(q="Coupons work as a price-discrimination device because", choices=[
   "they are free to print",
   "buyers willing to spend time clipping them tend to be the more price-sensitive ones",
   "they raise the shelf price",
   "they lower marginal cost",
   "everyone uses them equally"], ans=1,
   why="The effort involved sorts buyers by their price sensitivity."),
 dict(q="For price discrimination to raise profit, the seller must", choices=[
   "have no market power",
   "face buyers with different willingness to pay",
   "sell an identical product to identical buyers",
   "have constant returns to scale",
   "charge below marginal cost"], ans=1,
   why="With identical buyers there is nothing to exploit."),
 dict(q="A monopolist selling in two separate markets will allocate output so that", choices=[
   "prices are equal in both markets",
   "marginal revenue is equal across both markets and equal to marginal cost",
   "quantities are equal in both markets",
   "total revenue is equal in both markets",
   "elasticities are equal"], ans=1,
   why="Otherwise it could shift a unit to the market where it earns more."),
 dict(q="A monopolist sells in Market A with inelastic demand and Market B with elastic demand. It will charge", choices=[
   "a higher price in Market B", "a higher price in Market A", "the same price in both", "nothing in Market A", "below cost in Market A"], ans=1,
   why="The less elastic market bears the higher price."),
 dict(q="Peak-load pricing, such as higher electricity rates during peak hours, is", choices=[
   "always pure price discrimination",
   "partly cost-based, since serving peak demand genuinely costs more",
   "illegal everywhere",
   "unrelated to demand",
   "a form of first-degree discrimination"], ans=1,
   why="A price difference that tracks a real cost difference is not discrimination."),
 dict(q="Under perfect price discrimination, producer surplus equals", choices=[
   "zero", "the entire area between the demand curve and the marginal cost curve", "half of total surplus",
   "consumer surplus", "the deadweight loss"], ans=1,
   why="The seller captures every gain from trade."),
 dict(q="The quantity produced under perfect price discrimination equals the quantity that would be produced under", choices=[
   "single-price monopoly", "perfect competition", "monopolistic competition", "a cartel", "no production at all"], ans=1,
   why="Both produce where price equals marginal cost."),
 dict(q="Compared with single-price monopoly, perfect price discrimination results in", choices=[
   "less output and more deadweight loss",
   "more output and no deadweight loss",
   "the same output",
   "less profit for the firm",
   "more consumer surplus"], ans=1,
   why="Efficient output is reached, but the surplus all goes to the seller."),
 dict(q="A firm that offers a discount to customers who present a student card is trying to", choices=[
   "raise its costs",
   "separate buyers into groups with different price sensitivities",
   "eliminate its market power",
   "achieve productive efficiency",
   "sell below marginal cost"], ans=1,
   why="The card is an observable signal of a more elastic demand."),
 dict(q="Which of the following makes price discrimination harder to sustain?", choices=[
   "non-transferable services such as haircuts",
   "an active resale market for the product",
   "personalized subscriptions",
   "identity verification at purchase",
   "geographically separated markets"], ans=1,
   why="Resale lets buyers arbitrage away the price difference."),
 dict(q="Services are often easier to price discriminate than physical goods because", choices=[
   "services cost nothing to provide",
   "services are consumed by the buyer and generally cannot be resold",
   "services have no demand curve",
   "governments regulate goods more heavily",
   "services have constant marginal cost"], ans=1,
   why="Non-transferability blocks arbitrage."),
 dict(q="A drug company charging much less for a medicine in a low-income country is practising", choices=[
   "first-degree price discrimination",
   "third-degree price discrimination across geographic markets",
   "second-degree price discrimination",
   "cost-based pricing",
   "predatory pricing"], ans=1,
   why="Separate national markets with different demand elasticities are charged different prices."),
 dict(q="Price discrimination requires that markets be separated so that", choices=[
   "costs differ across markets",
   "buyers in the low-price market cannot resell to the high-price market",
   "demand is identical in each",
   "the firm has no market power",
   "output is identical in each"], ans=1,
   why="Separation is what makes different prices sustainable."),
 dict(q="Total surplus under perfect price discrimination compared with perfect competition is", choices=[
   "smaller", "the same, but distributed entirely to the producer", "larger", "zero", "negative"], ans=1,
   why="Both reach the efficient quantity; only the division differs."),
 dict(q="A single-price monopolist earns $4,000 profit. If it could perfectly price discriminate with the same costs, its profit would be", choices=[
   "less than $4,000", "at least $4,000 and generally more", "exactly $4,000", "zero", "impossible to determine"], ans=1,
   why="Discrimination is an added option, never a constraint."),
 dict(q="Which of the following best explains why a monopolist would ever sell some units at a low price?", choices=[
   "to reduce its profit",
   "to capture sales from buyers who would not pay the high price, without lowering the price to everyone",
   "because marginal cost is negative",
   "to satisfy a legal requirement",
   "to achieve productive efficiency"], ans=1,
   why="That is the whole logic of discriminating."),
 dict(q="An early-bird discount at a restaurant is most likely", choices=[
   "a cost-based price difference",
   "third-degree price discrimination separating time-flexible from time-inflexible diners",
   "first-degree price discrimination",
   "predatory pricing",
   "marginal-cost pricing"], ans=1,
   why="Diners who can shift their schedule tend to be more price-sensitive."),
 dict(q="If a firm with market power charges a single price, some potential buyers go unserved because", choices=[
   "the firm cannot produce more",
   "their willingness to pay is below the single price but above marginal cost",
   "they do not want the product",
   "marginal revenue is zero",
   "the government forbids the sale"], ans=1,
   why="Those unserved but valuable trades are the deadweight loss."),
 dict(q="Compared with charging a single price, price discrimination changes consumer surplus by", choices=[
   "increasing it", "reducing it, since the firm captures more of the gains from trade", "leaving it unchanged", "making it negative", "doubling it"], ans=1,
   why="Buyers pay closer to their maximum willingness to pay."),
 dict(q="A firm offering a two-part tariff, such as a membership fee plus a per-unit price, is using", choices=[
   "a form of price discrimination that captures consumer surplus through the fixed fee",
   "marginal-cost pricing only",
   "perfect competition pricing",
   "a cost-based pricing scheme",
   "predatory pricing"], ans=0,
   why="The fee extracts surplus while the per-unit price governs the quantity."),
 dict(q="Which of the following is a necessary condition for price discrimination?", choices=[
   "perfectly elastic demand",
   "the firm must be a price setter rather than a price taker",
   "constant marginal cost",
   "zero fixed costs",
   "identical buyers"], ans=1,
   why="A price taker cannot deviate from the market price at all."),
 dict(q="Price discrimination is generally more profitable when the difference in willingness to pay across buyers is", choices=[
   "small", "large", "zero", "negative", "irrelevant"], ans=1,
   why="A wider spread means more surplus available to capture."),
 dict(q="Which of the following is most likely to be able to price discriminate?", choices=[
   "a wheat farmer",
   "a university setting tuition net of individualized financial aid",
   "a corner shop selling branded soft drinks at list price",
   "a competitive fishing boat",
   "a firm facing horizontal demand"], ans=1,
   why="Aid packages set an individualized price based on ability to pay."),
 dict(q="Under third-degree price discrimination with two markets, the firm sets output in each market where", choices=[
   "price equals average cost",
   "that market's marginal revenue equals the firm's marginal cost",
   "prices are equalized",
   "total revenue is maximized",
   "elasticity equals one"], ans=1,
   why="Each market gets units up to the point where the last one just pays for itself."),
 dict(q="A firm that begins price discriminating will typically serve", choices=[
   "fewer customers than before", "more customers than before", "exactly the same customers",
   "only its highest-paying customer", "no customers"], ans=1,
   why="Lower-value buyers can now be served at prices they will accept."),
 dict(q="The reason perfect price discrimination is rare in practice is that", choices=[
   "it is always illegal",
   "a firm rarely knows each buyer's exact willingness to pay and rarely can stop resale entirely",
   "it lowers profit",
   "it requires perfect competition",
   "it produces too little output"], ans=1,
   why="The informational and arbitrage requirements are severe."),
]
