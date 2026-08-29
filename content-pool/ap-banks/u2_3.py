# 2.3 Price Elasticity of Demand — 50 questions
# Math verified: total-revenue test, midpoint formula, %chg ratios.
TOPIC = ("2.3", "Price Elasticity of Demand", 2)
QUESTIONS = [
 dict(q="Price elasticity of demand measures", choices=[
   "how much quantity demanded responds to a change in the good's price",
   "how much price responds to a change in quantity",
   "the slope of the supply curve",
   "total revenue at each price",
   "how income affects demand"], ans=0,
   why="PED is the responsiveness of quantity demanded to a price change."),
 dict(q="The formula for price elasticity of demand is", choices=[
   "% change in price ÷ % change in quantity demanded",
   "% change in quantity demanded ÷ % change in price",
   "change in quantity ÷ change in price",
   "price × quantity",
   "total revenue ÷ quantity"], ans=1,
   why="PED = %ΔQd / %ΔP."),
 dict(q="Demand is described as ELASTIC when the absolute value of PED is", choices=[
   "less than 1", "equal to 0", "greater than 1", "equal to 1", "negative"], ans=2,
   why="|PED| > 1 means quantity responds proportionally more than price."),
 dict(q="Demand is described as INELASTIC when the absolute value of PED is", choices=[
   "greater than 1", "less than 1", "equal to 1", "infinite", "always negative"], ans=1,
   why="|PED| < 1 means quantity responds proportionally less than price."),
 dict(q="Demand is UNIT ELASTIC when the absolute value of PED is", choices=[
   "0", "1", "greater than 1", "less than 1", "infinite"], ans=1,
   why="|PED| = 1 means quantity and price change by the same percentage."),
 dict(q="Price elasticity of demand is normally negative because", choices=[
   "consumers are irrational",
   "price and quantity demanded move in opposite directions",
   "income always falls",
   "supply slopes upward",
   "elasticity is measured in dollars"], ans=1,
   why="The law of demand gives the ratio a negative sign; we usually take absolute value."),
 dict(q="If the price of a good rises 10% and quantity demanded falls 20%, PED equals", choices=[
   "0.5", "1.0", "2.0", "10", "20"], ans=2,
   why="|−20% / 10%| = 2, elastic demand."),
 dict(q="If the price of a good rises 20% and quantity demanded falls 5%, demand is", choices=[
   "elastic, PED = 4",
   "inelastic, PED = 0.25",
   "unit elastic, PED = 1",
   "perfectly elastic",
   "perfectly inelastic"], ans=1,
   why="|−5% / 20%| = 0.25, which is less than 1 — inelastic."),
 dict(q="Perfectly inelastic demand is represented by a demand curve that is", choices=[
   "horizontal", "vertical", "downward sloping at 45 degrees", "upward sloping", "U-shaped"], ans=1,
   why="A vertical curve means quantity demanded does not change at all with price."),
 dict(q="Perfectly elastic demand is represented by a demand curve that is", choices=[
   "vertical", "horizontal", "steeply sloped", "upward sloping", "backward bending"], ans=1,
   why="A horizontal curve means any price increase drops quantity demanded to zero."),
 dict(q="Which of the following goods is most likely to have INELASTIC demand?", choices=[
   "A particular brand of soda",
   "Insulin for a diabetic patient",
   "Restaurant meals",
   "Foreign vacations",
   "Designer handbags"], ans=1,
   why="A necessity with no substitutes has highly inelastic demand."),
 dict(q="Which of the following goods is most likely to have ELASTIC demand?", choices=[
   "Salt",
   "Electricity",
   "One specific brand of bottled water among many",
   "Life-saving medication",
   "Tap water"], ans=2,
   why="Many close substitutes make demand for one brand highly elastic."),
 dict(q="The single most important determinant of price elasticity of demand is", choices=[
   "the number and closeness of available substitutes",
   "the price of the good",
   "the firm's profit margin",
   "the good's production cost",
   "the number of firms"], ans=0,
   why="More and closer substitutes make it easier to switch away, raising elasticity."),
 dict(q="Demand for a good tends to be MORE elastic when", choices=[
   "the good is a necessity",
   "the good takes up a large share of the consumer's budget",
   "the time period considered is very short",
   "there are no substitutes",
   "the good is habit-forming"], ans=1,
   why="Big-budget items get shopped around more, raising elasticity."),
 dict(q="Demand tends to become MORE elastic as the time period considered", choices=[
   "gets shorter, because consumers react instantly",
   "gets longer, because consumers have more time to find substitutes",
   "is irrelevant to elasticity",
   "approaches zero",
   "is fixed by contract"], ans=1,
   why="Given time, buyers find alternatives and adjust habits."),
 dict(q="Demand for a broadly defined category such as 'food' is generally", choices=[
   "more elastic than demand for a single brand of cereal",
   "less elastic than demand for a single brand of cereal",
   "perfectly elastic",
   "identical to that for a single brand",
   "always unit elastic"], ans=1,
   why="Broad necessities have few substitutes; individual brands have many."),
 dict(q="If demand is ELASTIC and a firm RAISES its price, total revenue will", choices=[
   "rise", "fall", "stay the same", "become zero", "always double"], ans=1,
   why="With elastic demand, quantity falls proportionally more than price rises."),
 dict(q="If demand is INELASTIC and a firm RAISES its price, total revenue will", choices=[
   "fall", "rise", "stay the same", "become zero", "be indeterminate"], ans=1,
   why="Quantity falls proportionally less than the price rises, so revenue increases."),
 dict(q="If demand is INELASTIC and a firm LOWERS its price, total revenue will", choices=[
   "rise", "fall", "stay the same", "double", "be unaffected"], ans=1,
   why="Quantity rises proportionally less than price falls, so revenue drops."),
 dict(q="If demand is UNIT ELASTIC, a change in price will cause total revenue to", choices=[
   "rise", "fall", "remain unchanged", "become negative", "become zero"], ans=2,
   why="Price and quantity changes offset exactly, holding revenue constant."),
 dict(q="A concert promoter raises ticket prices by 15% and finds total revenue increases. This implies demand for the tickets is", choices=[
   "elastic", "inelastic", "unit elastic", "perfectly elastic", "impossible to determine"], ans=1,
   why="Revenue rising with price is the signature of inelastic demand."),
 dict(q="A store cuts prices by 20% and total revenue rises. Demand for its product is", choices=[
   "inelastic", "elastic", "unit elastic", "perfectly inelastic", "zero"], ans=1,
   why="Revenue rising when price falls indicates elastic demand."),
 dict(q="The midpoint (arc) formula for elasticity is used because it", choices=[
   "is easier to memorize",
   "gives the same elasticity whether price rises or falls between two points",
   "always yields a value greater than 1",
   "ignores quantity changes",
   "converts elasticity to dollars"], ans=1,
   why="Using averages as the base makes the result direction-independent."),
 dict(q="Using the midpoint formula, price falls from $10 to $8 and quantity rises from 40 to 60. The percentage change in quantity is", choices=[
   "50%", "40%", "33%", "25%", "20%"], ans=1,
   why="ΔQ/average Q = 20/50 = 40%."),
 dict(q="Continuing that example (P: $10→$8, Q: 40→60), the percentage change in price using the midpoint formula is", choices=[
   "−20%", "−22.2%", "−25%", "−18%", "−10%"], ans=1,
   why="ΔP/average P = −2/9 ≈ −22.2%."),
 dict(q="Using those midpoint results (40% quantity change, 22.2% price change), the price elasticity of demand is approximately", choices=[
   "0.55", "1.0", "1.8", "2.5", "4.0"], ans=2,
   why="40 / 22.2 ≈ 1.8, so demand is elastic over that range."),
 dict(q="Along a straight-line downward-sloping demand curve, elasticity", choices=[
   "is constant everywhere",
   "is greater at higher prices and smaller at lower prices",
   "is greater at lower prices",
   "is always equal to 1",
   "equals the slope"], ans=1,
   why="On a linear demand curve the upper portion is elastic, the lower inelastic."),
 dict(q="At the midpoint of a straight-line demand curve, demand is", choices=[
   "perfectly elastic", "elastic", "unit elastic", "inelastic", "perfectly inelastic"], ans=2,
   why="The midpoint of a linear demand curve is exactly unit elastic."),
 dict(q="Total revenue is maximized at the point on a linear demand curve where demand is", choices=[
   "perfectly elastic", "elastic", "unit elastic", "inelastic", "perfectly inelastic"], ans=2,
   why="Revenue peaks where PED = 1, since further price change reduces revenue either way."),
 dict(q="Elasticity and slope are not the same thing because elasticity", choices=[
   "uses percentage changes, so it does not depend on the units of measurement",
   "is always constant along a curve",
   "measures only price",
   "is measured in dollars per unit",
   "ignores quantity"], ans=0,
   why="Percentages make elasticity unit-free, unlike slope."),
 dict(q="A government wanting to raise the most tax revenue from a per-unit tax should tax goods whose demand is", choices=[
   "highly elastic", "inelastic", "perfectly elastic", "unit elastic", "unknown"], ans=1,
   why="Inelastic demand means quantity barely falls, so the tax base holds up."),
 dict(q="A government wanting to REDUCE consumption of a good most effectively with a tax should target a good whose demand is", choices=[
   "inelastic", "elastic", "perfectly inelastic", "unit elastic", "vertical"], ans=1,
   why="Elastic demand means buyers cut back sharply when price rises."),
 dict(q="When demand is more inelastic than supply, the burden of a per-unit tax falls", choices=[
   "entirely on producers",
   "mostly on consumers",
   "equally on both",
   "entirely on the government",
   "on neither party"], ans=1,
   why="The less elastic side of the market bears more of the tax."),
 dict(q="Which of the following would make demand for gasoline more elastic over time?", choices=[
   "Cars becoming less fuel efficient",
   "Growth of public transit and electric vehicle options",
   "Fewer commuting alternatives",
   "Gasoline becoming a smaller share of budgets",
   "Higher incomes"], ans=1,
   why="More substitutes for driving on gasoline raises elasticity."),
 dict(table=dict(headers=["Price", "Quantity demanded", "Total revenue"],
   rows=[["$10", "10", "$100"], ["$8", "20", "$160"], ["$6", "30", "$180"], ["$4", "40", "$160"], ["$2", "50", "$100"]]),
   q="Using the table, demand is elastic over which price range?", choices=[
   "From $6 to $4, since revenue falls as price falls",
   "From $10 to $8, since revenue rises as price falls",
   "From $4 to $2, since revenue rises",
   "Nowhere on this schedule",
   "Everywhere on this schedule"], ans=1,
   why="Revenue rising when price falls ($100 → $160) signals elastic demand."),
 dict(table=dict(headers=["Price", "Quantity demanded", "Total revenue"],
   rows=[["$10", "10", "$100"], ["$8", "20", "$160"], ["$6", "30", "$180"], ["$4", "40", "$160"], ["$2", "50", "$100"]]),
   q="Using the same table, total revenue is maximized at a price of", choices=[
   "$10", "$8", "$6", "$4", "$2"], ans=2,
   why="Revenue peaks at $180 when price is $6 — the unit-elastic region."),
 dict(table=dict(headers=["Price", "Quantity demanded", "Total revenue"],
   rows=[["$10", "10", "$100"], ["$8", "20", "$160"], ["$6", "30", "$180"], ["$4", "40", "$160"], ["$2", "50", "$100"]]),
   q="Using the same table, demand is INELASTIC over which range?", choices=[
   "From $10 to $8", "From $8 to $6", "From $4 to $2, since revenue falls as price falls", "Nowhere", "Only at $10"], ans=2,
   why="Revenue falling as price falls ($160 → $100) means demand is inelastic there."),
 dict(q="A firm currently operating in the inelastic portion of its demand curve can increase total revenue by", choices=[
   "lowering price", "raising price", "leaving price unchanged", "increasing output", "advertising only"], ans=1,
   why="In the inelastic range, a price increase raises revenue."),
 dict(q="A perfectly competitive firm faces a demand curve that is", choices=[
   "perfectly inelastic",
   "perfectly elastic at the market price",
   "unit elastic",
   "downward sloping and steep",
   "upward sloping"], ans=1,
   why="A price taker can sell any quantity at the market price but nothing above it."),
 dict(q="If PED for a good equals 0.4, a 10% price increase will change quantity demanded by", choices=[
   "−4%", "−10%", "−40%", "+4%", "+40%"], ans=0,
   why="%ΔQ = PED × %ΔP = 0.4 × 10% = 4% decrease."),
 dict(q="If PED for a good equals 3, a 5% price decrease will change quantity demanded by", choices=[
   "+1.7%", "+5%", "+15%", "−15%", "−5%"], ans=2,
   why="3 × 5% = 15% increase in quantity demanded."),
 dict(q="Goods that are habit-forming or addictive typically have demand that is", choices=[
   "highly elastic", "relatively inelastic", "perfectly elastic", "unit elastic", "upward sloping"], ans=1,
   why="Habit reduces buyers' willingness to substitute away when prices rise."),
 dict(q="Which pair of characteristics would produce the MOST elastic demand?", choices=[
   "A necessity with no substitutes, purchased immediately",
   "A luxury with many substitutes, considered over a long time period",
   "A tiny share of the budget with no alternatives",
   "An addictive good in the short run",
   "A good bought under contract"], ans=1,
   why="Luxury status, substitutes, and time all raise elasticity."),
 dict(q="An elasticity of demand equal to zero means", choices=[
   "consumers buy nothing at any price",
   "quantity demanded does not change at all when price changes",
   "revenue is always zero",
   "the good is free",
   "the demand curve is horizontal"], ans=1,
   why="PED = 0 is perfectly inelastic — a vertical demand curve."),
 dict(q="Airlines charge business travelers more than leisure travelers largely because business travel demand is", choices=[
   "more elastic", "less elastic", "perfectly elastic", "unit elastic", "zero"], ans=1,
   why="Business travelers must fly on set dates, so they are less price-sensitive."),
 dict(q="Which statement about elasticity and total revenue is TRUE?", choices=[
   "Price and revenue always move together",
   "In the elastic range, price and total revenue move in opposite directions",
   "In the inelastic range, price and total revenue move in opposite directions",
   "Revenue is unrelated to elasticity",
   "Revenue is maximized where demand is perfectly elastic"], ans=1,
   why="Elastic: raise price, revenue falls; lower price, revenue rises."),
 dict(q="A 1% fall in price causes a 1% rise in quantity demanded. Total revenue will", choices=[
   "rise noticeably", "fall noticeably", "remain approximately unchanged", "double", "fall to zero"], ans=2,
   why="Unit elasticity leaves total revenue essentially unchanged."),
 dict(q="Which of the following would most likely make demand for a specific restaurant MORE elastic?", choices=[
   "It is the only restaurant in an isolated town",
   "Several similar restaurants open next door",
   "Its customers are extremely loyal",
   "It serves a necessity",
   "Its prices fall below cost"], ans=1,
   why="New close substitutes make buyers far more responsive to its prices."),
 dict(q="Luxury goods generally have more elastic demand than necessities because", choices=[
   "they cost more to produce",
   "consumers can postpone or forgo luxury purchases when prices rise",
   "they are taxed more heavily",
   "they have fewer substitutes",
   "their supply is fixed"], ans=1,
   why="Luxuries are optional, so buyers respond sharply to price."),
 dict(q="If a 5% increase in price leaves quantity demanded completely unchanged, PED equals", choices=[
   "0, perfectly inelastic", "1, unit elastic", "5, elastic", "infinity, perfectly elastic", "0.5, inelastic"], ans=0,
   why="No quantity response at all means PED = 0."),
]
assert len(QUESTIONS) == 50, len(QUESTIONS)
