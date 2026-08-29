# 2.5 Other Elasticities (income and cross-price) — 50 questions
TOPIC = ("2.5", "Other Elasticities", 2)
QUESTIONS = [
 dict(q="Income elasticity of demand measures", choices=[
   "how quantity demanded responds to a change in consumer income",
   "how quantity demanded responds to the good's own price",
   "how supply responds to income",
   "how price responds to quantity",
   "the share of income spent on a good"], ans=0,
   why="YED is the responsiveness of demand to income changes."),
 dict(q="The formula for income elasticity of demand is", choices=[
   "% change in income ÷ % change in quantity demanded",
   "% change in quantity demanded ÷ % change in income",
   "quantity demanded ÷ income",
   "income ÷ price",
   "% change in quantity demanded ÷ % change in price"], ans=1,
   why="YED = %ΔQd / %ΔIncome."),
 dict(q="A positive income elasticity of demand indicates the good is", choices=[
   "inferior", "normal", "a substitute", "a complement", "a public good"], ans=1,
   why="Demand rising with income defines a normal good."),
 dict(q="A negative income elasticity of demand indicates the good is", choices=[
   "normal", "inferior", "a complement", "a luxury", "perfectly elastic"], ans=1,
   why="Demand falling as income rises defines an inferior good."),
 dict(q="A normal good with income elasticity GREATER than 1 is classified as", choices=[
   "a necessity", "a luxury (income elastic)", "an inferior good", "a complement", "a Giffen good"], ans=1,
   why="YED > 1 means demand grows faster than income — a luxury."),
 dict(q="A normal good with income elasticity between 0 and 1 is classified as", choices=[
   "a luxury", "a necessity (income inelastic)", "an inferior good", "a substitute", "a public good"], ans=1,
   why="0 < YED < 1 means demand grows more slowly than income — a necessity."),
 dict(q="If income rises 10% and quantity demanded of a good rises 25%, income elasticity equals", choices=[
   "0.4", "1.5", "2.5", "10", "25"], ans=2,
   why="25% / 10% = 2.5, an income-elastic luxury good."),
 dict(q="If income rises 20% and quantity demanded rises 4%, the good is", choices=[
   "inferior, YED = −0.2",
   "a necessity, YED = 0.2",
   "a luxury, YED = 5",
   "unit elastic",
   "a complement"], ans=1,
   why="4% / 20% = 0.2, positive but below 1 — a normal necessity."),
 dict(q="If income rises 15% and quantity demanded FALLS 3%, income elasticity equals", choices=[
   "0.2", "−0.2", "5", "−5", "3"], ans=1,
   why="−3% / 15% = −0.2 — an inferior good."),
 dict(q="Which good most likely has a negative income elasticity?", choices=[
   "Luxury cars",
   "International vacations",
   "Generic instant noodles",
   "Fine dining",
   "Designer clothing"], ans=2,
   why="Cheap staples are bought less as income rises — inferior goods."),
 dict(q="Which good most likely has an income elasticity greater than 1?", choices=[
   "Salt",
   "Bus travel",
   "Luxury yachts",
   "Basic bread",
   "Used clothing"], ans=2,
   why="Luxuries have demand that grows faster than income."),
 dict(q="Cross-price elasticity of demand measures", choices=[
   "how quantity demanded of one good responds to a change in the price of another good",
   "how a good's own price affects its quantity demanded",
   "how income affects demand",
   "how supply responds to price",
   "the elasticity of the market as a whole"], ans=0,
   why="XED captures the demand relationship between two goods."),
 dict(q="The formula for cross-price elasticity of demand is", choices=[
   "% change in quantity demanded of good A ÷ % change in price of good B",
   "% change in price of A ÷ % change in quantity of B",
   "price of A ÷ price of B",
   "% change in quantity of A ÷ % change in income",
   "quantity of A × price of B"], ans=0,
   why="XED = %ΔQd of A / %ΔP of B."),
 dict(q="A POSITIVE cross-price elasticity indicates the two goods are", choices=[
   "complements", "substitutes", "inferior goods", "unrelated", "public goods"], ans=1,
   why="A price rise in B raising demand for A means buyers substitute."),
 dict(q="A NEGATIVE cross-price elasticity indicates the two goods are", choices=[
   "substitutes", "complements", "normal goods", "luxuries", "unrelated"], ans=1,
   why="A price rise in B lowering demand for A means they are consumed together."),
 dict(q="A cross-price elasticity of approximately ZERO indicates the goods are", choices=[
   "perfect substitutes", "perfect complements", "unrelated", "both inferior", "both luxuries"], ans=2,
   why="No demand response means the goods are independent."),
 dict(q="The price of tea rises 10% and quantity demanded of coffee rises 6%. The cross-price elasticity is", choices=[
   "−0.6", "0.6", "1.67", "−1.67", "6"], ans=1,
   why="6% / 10% = +0.6 — substitutes."),
 dict(q="The price of printers rises 20% and quantity demanded of ink cartridges falls 10%. The cross-price elasticity is", choices=[
   "+0.5", "−0.5", "+2", "−2", "10"], ans=1,
   why="−10% / 20% = −0.5 — complements."),
 dict(q="The larger the ABSOLUTE value of cross-price elasticity, the", choices=[
   "weaker the relationship between the two goods",
   "stronger the substitute or complement relationship",
   "more inferior the good",
   "more inelastic own-price demand is",
   "lower the income elasticity"], ans=1,
   why="Bigger magnitude means a stronger relationship in either direction."),
 dict(q="Two goods with a cross-price elasticity of +3.5 are", choices=[
   "weak complements", "strong complements", "close substitutes", "unrelated", "inferior goods"], ans=2,
   why="A large positive value indicates goods that substitute closely."),
 dict(q="During a recession, firms selling luxury goods typically see demand fall sharply because those goods have", choices=[
   "negative income elasticity",
   "high positive income elasticity",
   "zero income elasticity",
   "negative cross-price elasticity",
   "inelastic own-price demand"], ans=1,
   why="High YED means demand swings more than income does."),
 dict(q="A discount grocery chain often performs relatively well during recessions because its products tend to be", choices=[
   "luxuries", "inferior goods with negative income elasticity", "complements", "perfectly elastic", "public goods"], ans=1,
   why="Falling income raises demand for inferior goods."),
 dict(q="Knowing that two products have a strongly positive cross-price elasticity is useful to a firm because it identifies", choices=[
   "its close competitors",
   "its complementary products",
   "its fixed costs",
   "its income elasticity",
   "consumer surplus"], ans=0,
   why="Strong substitutes are competitors whose prices affect your sales."),
 dict(q="If a firm learns its product has a strongly negative cross-price elasticity with another product, it should recognize that", choices=[
   "the other product is a competitor",
   "the products are complements, so a fall in the other's price helps its own sales",
   "the products are unrelated",
   "its own good is inferior",
   "demand is perfectly inelastic"], ans=1,
   why="Complements sell together, so a cheaper partner good boosts demand."),
 dict(q="Income elasticity of demand for a good equals 0. This means demand is", choices=[
   "highly responsive to income",
   "completely unresponsive to income changes",
   "negative",
   "elastic with respect to price",
   "a luxury"], ans=1,
   why="YED = 0 means income changes do not affect quantity demanded."),
 dict(table=dict(headers=["Good", "Income elasticity"],
   rows=[["A", "2.4"], ["B", "0.3"], ["C", "−0.8"]]),
   q="Using the table, which good is an inferior good?", choices=[
   "Good A", "Good B", "Good C", "All three", "None"], ans=2,
   why="Only Good C has a negative income elasticity."),
 dict(table=dict(headers=["Good", "Income elasticity"],
   rows=[["A", "2.4"], ["B", "0.3"], ["C", "−0.8"]]),
   q="Using the same table, which good is a normal necessity?", choices=[
   "Good A, since 2.4 exceeds 1",
   "Good B, since 0.3 is between 0 and 1",
   "Good C, since −0.8 is negative",
   "Both A and C",
   "None of them"], ans=1,
   why="Necessities have income elasticity between 0 and 1."),
 dict(table=dict(headers=["Good", "Income elasticity"],
   rows=[["A", "2.4"], ["B", "0.3"], ["C", "−0.8"]]),
   q="Using the same table, which good's demand would fall the most in a recession?", choices=[
   "Good A, the income-elastic luxury",
   "Good B, the necessity",
   "Good C, the inferior good",
   "All would fall equally",
   "None would change"], ans=0,
   why="The highest positive YED means demand swings most with income."),
 dict(q="Cross-price elasticity between butter and margarine is likely to be", choices=[
   "large and negative", "large and positive", "exactly zero", "undefined", "always 1"], ans=1,
   why="They are close substitutes, so XED is strongly positive."),
 dict(q="Cross-price elasticity between cars and gasoline is likely to be", choices=[
   "positive", "negative", "zero", "infinite", "exactly 1"], ans=1,
   why="They are complements consumed together, giving a negative XED."),
 dict(q="Cross-price elasticity between textbooks and bananas is likely to be", choices=[
   "strongly positive", "strongly negative", "close to zero", "infinite", "exactly −1"], ans=2,
   why="Unrelated goods have essentially no cross-price response."),
 dict(q="If income rises by 5% and demand for public bus rides falls by 2%, bus rides are", choices=[
   "a luxury", "a necessity", "an inferior good", "a complement to income", "unrelated to income"], ans=2,
   why="Negative income elasticity (−0.4) makes bus rides inferior here."),
 dict(q="An engineering firm predicting future demand for its luxury product should pay closest attention to forecasts of", choices=[
   "input costs only",
   "aggregate consumer income growth",
   "the number of competitors only",
   "government spending only",
   "its own fixed costs"], ans=1,
   why="High-YED goods track income closely, so income forecasts matter most."),
 dict(q="Which statement about elasticity types is correct?", choices=[
   "PED and YED are always the same value",
   "PED uses own price, YED uses income, and XED uses another good's price",
   "All three use the good's own price",
   "XED cannot be negative",
   "YED cannot be negative"], ans=1,
   why="Each elasticity divides quantity response by a different driver."),
 dict(q="If demand for a good rises 8% when income rises 8%, the good is", choices=[
   "inferior",
   "unit income elastic — a borderline case between necessity and luxury",
   "a strong luxury",
   "unrelated to income",
   "a complement"], ans=1,
   why="YED = 1 exactly is the boundary between necessity and luxury."),
 dict(q="A firm considering entering the market for a good with income elasticity of 3.0 should recognize the market will be", choices=[
   "stable regardless of the economy",
   "highly sensitive to the business cycle",
   "unaffected by recessions",
   "inferior",
   "perfectly inelastic"], ans=1,
   why="Very high YED means booms and busts swing demand hard."),
 dict(q="Cross-price elasticity is useful in antitrust analysis because it helps determine", choices=[
   "production costs",
   "whether two firms' products actually compete in the same market",
   "consumer income",
   "the tax rate",
   "fixed costs"], ans=1,
   why="High positive XED shows products are substitutes competing directly."),
 dict(q="The price of Good X rises from $10 to $12 and quantity demanded of Good Y rises from 100 to 110. The cross-price elasticity (using initial values) is", choices=[
   "0.2", "0.5", "2.0", "−0.5", "10"], ans=1,
   why="Y rises 10%, X's price rises 20%; 10/20 = +0.5 — substitutes."),
 dict(q="Based on that result (+0.5), Goods X and Y are", choices=[
   "complements", "substitutes", "unrelated", "both inferior", "both luxuries"], ans=1,
   why="A positive cross-price elasticity means substitutes."),
 dict(q="Which of the following goods would you expect to have the LOWEST income elasticity of demand?", choices=[
   "Private jets", "Table salt", "Luxury watches", "Overseas travel", "Sports cars"], ans=1,
   why="Consumption of a cheap staple barely changes as income grows."),
 dict(q="A good with income elasticity of −1.5 experiences a 4% fall in income. Quantity demanded will", choices=[
   "fall 6%", "rise 6%", "fall 1.5%", "rise 1.5%", "not change"], ans=1,
   why="−1.5 × −4% = +6% — the inferior good's demand rises as income falls."),
 dict(q="Why do governments care about income elasticity when forecasting tax revenue?", choices=[
   "It determines the tax rate",
   "It predicts how consumption of taxed goods will change as incomes grow or shrink",
   "It eliminates deadweight loss",
   "It sets the price level",
   "It measures supply"], ans=1,
   why="Income-elastic tax bases swing with the business cycle."),
 dict(q="A restaurant finds that when a nearby competitor lowers prices 10%, its own sales fall 15%. The cross-price elasticity is", choices=[
   "+1.5, indicating close substitutes",
   "−1.5, indicating complements",
   "+0.67",
   "−0.67",
   "zero"], ans=0,
   why="−15% quantity over −10% price = +1.5, a positive value indicating substitutes."),
 dict(q="Which pairing of elasticity value and interpretation is CORRECT?", choices=[
   "YED = −0.5: luxury good",
   "XED = −2.0: complements",
   "XED = +2.0: complements",
   "YED = +2.0: inferior good",
   "XED = 0: perfect substitutes"], ans=1,
   why="Negative cross-price elasticity always means complements."),
 dict(q="During a strong economic expansion, which good's sales would you expect to grow FASTEST?", choices=[
   "A good with YED = −1.0",
   "A good with YED = 0.1",
   "A good with YED = 0.9",
   "A good with YED = 2.8",
   "A good with YED = 0"], ans=3,
   why="The highest positive income elasticity grows fastest with income."),
 dict(q="Estimating both income and cross-price elasticities helps a firm", choices=[
   "set its fixed costs",
   "anticipate how economic conditions and rivals' prices will affect demand",
   "eliminate competition",
   "raise its own-price elasticity",
   "compute total cost"], ans=1,
   why="They map how outside forces move the firm's demand curve."),
 dict(q="Public transportation ridership rising during recessions is evidence that public transit is", choices=[
   "a luxury good", "an inferior good", "a complement to income", "perfectly elastic", "unrelated to income"], ans=1,
   why="Rising demand when income falls is the definition of an inferior good."),
 dict(q="Which elasticity would a firm use to decide whether a price cut by a rival threatens its sales?", choices=[
   "Price elasticity of supply",
   "Income elasticity of demand",
   "Cross-price elasticity of demand",
   "Own-price elasticity of supply",
   "Elasticity of substitution in production"], ans=2,
   why="Cross-price elasticity measures a rival's price effect on your demand."),
 dict(q="A good can be BOTH normal and income inelastic. This means", choices=[
   "demand falls when income rises",
   "demand rises with income, but by a smaller percentage than income rises",
   "demand rises faster than income",
   "income has no effect",
   "the good is inferior"], ans=1,
   why="0 < YED < 1: positive but less than proportional — a necessity."),
 dict(q="If two goods have a cross-price elasticity of −0.05, the best conclusion is that they are", choices=[
   "very strong complements",
   "very weak complements, close to unrelated",
   "strong substitutes",
   "identical products",
   "both inferior goods"], ans=1,
   why="The sign says complements, but the tiny magnitude means a very weak link."),
]
assert len(QUESTIONS) == 50, len(QUESTIONS)
