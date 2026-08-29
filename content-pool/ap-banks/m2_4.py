# MACRO 2.4 Price Indices and Inflation — 50 questions
# Table verified (BASKET). Fixed market basket, base year = Year 1.
#   Item      Qty   P(Yr1)  P(Yr2)  P(Yr3)
#   Bread      10    $2.00   $2.50   $3.00
#   Milk        5    $3.00   $3.00   $4.00
#   Gasoline   20    $2.00   $3.00   $3.25
#
#   Cost of basket, Year 1 = 10(2.00) + 5(3.00) + 20(2.00)
#                          = 20 + 15 + 40 = $75
#   Cost of basket, Year 2 = 10(2.50) + 5(3.00) + 20(3.00)
#                          = 25 + 15 + 60 = $100
#   Cost of basket, Year 3 = 10(3.00) + 5(4.00) + 20(3.25)
#                          = 30 + 20 + 65 = $115
#
#   CPI(year) = 100 * cost of basket in that year / cost of basket in base year
#   CPI(Yr1) = 100 * 75/75  = 100.00
#   CPI(Yr2) = 100 * 100/75 = 133.33
#   CPI(Yr3) = 100 * 115/75 = 153.33
#
#   Inflation Yr1 -> Yr2 = (133.33 - 100)/100     = 0.3333 = 33.3%
#   Inflation Yr2 -> Yr3 = (153.33 - 133.33)/133.33 = 20/133.33 = 0.15 = 15.0%
#     (check directly: 115/100 - 1 = 0.15, same base cancels)
#   Inflation Yr1 -> Yr3 = 115/75 - 1 = 0.5333 = 53.3%
#
#   Gasoline's own price rise Yr1 -> Yr2 = 3.00/2.00 - 1 = 50%
#   Gasoline weight in the base-year basket = 40/75 = 53.3%
TOPIC = ("2.4", "Price Indices and Inflation", 2)

BASKET = dict(headers=["Item", "Quantity in basket", "Year 1 price", "Year 2 price", "Year 3 price"],
              rows=[["Bread", "10", "$2.00", "$2.50", "$3.00"],
                    ["Milk", "5", "$3.00", "$3.00", "$4.00"],
                    ["Gasoline", "20", "$2.00", "$3.00", "$3.25"]])

QUESTIONS = [
 dict(q="Inflation is best defined as", choices=[
   "an increase in the price of one important good",
   "a sustained increase in the general level of prices in an economy",
   "an increase in the money supply",
   "an increase in nominal GDP",
   "a fall in the value of exports"], ans=1,
   why="Inflation refers to the overall price level, not to any single price."),
 dict(q="The consumer price index measures", choices=[
   "the cost of all goods produced in an economy",
   "the cost of a fixed market basket of goods and services typically purchased by households",
   "the average wage of workers",
   "the total spending of the government",
   "the value of exports relative to imports"], ans=1,
   why="The CPI prices a fixed basket meant to represent typical household purchases."),
 dict(q="The formula for a price index in a given year is", choices=[
   "100 × (cost of the basket in the base year ÷ cost of the basket in the given year)",
   "100 × (cost of the basket in the given year ÷ cost of the basket in the base year)",
   "cost of the basket in the given year − cost in the base year",
   "100 × (nominal GDP ÷ population)",
   "100 × (real GDP ÷ nominal GDP)"], ans=1,
   why="The index expresses the current cost of the basket as a percentage of its base-year cost."),
 dict(q="The value of the CPI in the base year is always", choices=[
   "0", "1", "50", "100", "equal to the inflation rate"], ans=3,
   why="Dividing the base-year cost of the basket by itself and multiplying by 100 gives 100."),
 dict(q="The inflation rate between two years is calculated as", choices=[
   "the difference in the two index values",
   "100 × (index in the later year − index in the earlier year) ÷ index in the earlier year",
   "the later index divided by 100",
   "the later index minus 100",
   "the average of the two index values"], ans=1,
   why="Inflation is the percentage change in the index, so the earlier year's index is the denominator."),
 dict(q="Using the market basket below, the cost of the basket in Year 1 is", table=BASKET, choices=[
   "$65", "$70", "$75", "$85", "$100"], ans=2,
   why="10($2.00) + 5($3.00) + 20($2.00) = 20 + 15 + 40 = $75."),
 dict(q="Using the same basket, the cost of the basket in Year 2 is", table=BASKET, choices=[
   "$75", "$90", "$100", "$110", "$115"], ans=2,
   why="10($2.50) + 5($3.00) + 20($3.00) = 25 + 15 + 60 = $100."),
 dict(q="Using the same basket, the cost of the basket in Year 3 is", table=BASKET, choices=[
   "$100", "$105", "$110", "$115", "$130"], ans=3,
   why="10($3.00) + 5($4.00) + 20($3.25) = 30 + 20 + 65 = $115."),
 dict(q="Using the same basket with Year 1 as the base year, the CPI in Year 2 is closest to", table=BASKET, choices=[
   "75.0", "100.0", "125.0", "133.3", "153.3"], ans=3,
   why="100 × $100/$75 = 133.3."),
 dict(q="Using the same basket with Year 1 as the base year, the CPI in Year 3 is closest to", table=BASKET, choices=[
   "115.0", "133.3", "143.8", "153.3", "165.0"], ans=3,
   why="100 × $115/$75 = 153.3."),
 dict(q="Using the same basket with Year 1 as the base year, the inflation rate from Year 1 to Year 2 is closest to", table=BASKET, choices=[
   "15.0%", "25.0%", "33.3%", "40.0%", "53.3%"], ans=2,
   why="The index rises from 100 to 133.3, a 33.3% increase."),
 dict(q="Using the same basket, the inflation rate from Year 2 to Year 3 is", table=BASKET, choices=[
   "13.0%", "15.0%", "20.0%", "23.3%", "33.3%"], ans=1,
   why="($115 − $100)/$100 = 0.15, so the price level rose 15%."),
 dict(q="Using the same basket, the inflation rate from Year 1 to Year 3 is closest to", table=BASKET, choices=[
   "15.0%", "33.3%", "48.3%", "53.3%", "153.3%"], ans=3,
   why="$115/$75 − 1 = 0.533, and note that this is not 33.3% + 15% because the increases compound."),
 dict(q="Using the same basket, the price of gasoline rose between Year 1 and Year 2 by", table=BASKET, choices=[
   "15%", "25%", "33%", "50%", "100%"], ans=3,
   why="$3.00/$2.00 − 1 = 0.50."),
 dict(q="Using the same basket, gasoline's weight in the Year 1 basket is closest to", table=BASKET, choices=[
   "20%", "27%", "40%", "53%", "67%"], ans=3,
   why="Gasoline accounts for $40 of the $75 base-year basket."),
 dict(q="Using the same basket, milk's contribution to the change in the basket's cost from Year 2 to Year 3 is", table=BASKET, choices=[
   "$0", "$5", "$10", "$15", "$20"], ans=1,
   why="Milk rose from $3.00 to $4.00 on 5 units, adding $5 to the basket."),
 dict(q="The quantities in the CPI basket are held fixed between rebasing so that", choices=[
   "consumers cannot substitute",
   "changes in the index reflect changes in prices rather than changes in what people buy",
   "the index always rises",
   "the base year cost is minimized",
   "real GDP can be computed"], ans=1,
   why="Holding quantities constant isolates the price effect, which is exactly what a price index is meant to measure."),
 dict(q="Substitution bias in the CPI arises because", choices=[
   "the index includes too many goods",
   "consumers shift toward relatively cheaper goods, but the fixed basket keeps the old quantities",
   "prices are collected too often",
   "the base year changes each year",
   "imports are excluded"], ans=1,
   why="The fixed basket assumes people keep buying the same amounts, so it overstates the rise in the true cost of living."),
 dict(q="Substitution bias causes the CPI to", choices=[
   "understate inflation", "overstate inflation", "measure inflation exactly", "be negative", "equal the GDP deflator"], ans=1,
   why="Consumers escape part of the price increase by substituting, and the fixed basket does not capture that escape."),
 dict(q="New-product bias in the CPI arises because", choices=[
   "new goods raise prices",
   "new goods enter the basket only with a lag, so the benefit of greater variety is missed",
   "old goods are dropped too quickly",
   "the base year is arbitrary",
   "quality is measured too accurately"], ans=1,
   why="Goods are added to the basket only when the basket is revised, so early price declines on new products are missed."),
 dict(q="Quality change bias arises because", choices=[
   "product quality never changes",
   "part of a price increase may reflect a genuinely better product rather than pure inflation",
   "quality is always falling",
   "quality is included twice",
   "the basket is too large"], ans=1,
   why="If a car costs 5% more but is safer and more fuel-efficient, treating the whole increase as inflation overstates it."),
 dict(q="Taken together, substitution bias, new-product bias, and quality bias imply that the CPI tends to", choices=[
   "understate the true rise in the cost of living",
   "overstate the true rise in the cost of living",
   "measure it without error",
   "understate the price level in the base year",
   "equal the GDP deflator exactly"], ans=1,
   why="All three biases push the measured index above the true increase in the cost of maintaining a given standard of living."),
 dict(q="The GDP deflator is calculated as", choices=[
   "100 × (real GDP ÷ nominal GDP)",
   "100 × (nominal GDP ÷ real GDP)",
   "nominal GDP − real GDP",
   "100 × (nominal GDP ÷ population)",
   "the CPI divided by 100"], ans=1,
   why="The deflator compares output valued at current prices with the same output valued at base-year prices."),
 dict(q="A key difference between the CPI and the GDP deflator is that the GDP deflator", choices=[
   "uses a fixed basket of consumer goods",
   "covers all goods and services produced domestically, with weights that change as the composition of output changes",
   "includes imported consumer goods",
   "is published only once a decade",
   "is always larger than the CPI"], ans=1,
   why="The deflator's basket is current output, so its weights update automatically."),
 dict(q="An increase in the price of imported consumer electronics would", choices=[
   "raise the GDP deflator but not the CPI",
   "raise the CPI but have little direct effect on the GDP deflator",
   "raise both by the same amount",
   "lower both",
   "have no effect on either"], ans=1,
   why="Imports are bought by households and so appear in the CPI, but they are not domestic production and so are outside the deflator."),
 dict(q="An increase in the price of industrial machinery produced and sold domestically to firms would", choices=[
   "raise the CPI but not the GDP deflator",
   "raise the GDP deflator but have little direct effect on the CPI",
   "raise both equally",
   "lower the deflator",
   "affect neither index"], ans=1,
   why="Capital goods are part of domestic output but are not in the consumer basket."),
 dict(q="Because the GDP deflator's weights update with current output, it does not suffer from", choices=[
   "any measurement problems at all",
   "substitution bias in the way the fixed-basket CPI does",
   "the need for a base year",
   "the effect of price changes",
   "revisions"], ans=1,
   why="Current-period weights automatically reflect the shift toward relatively cheaper goods."),
 dict(q="The producer price index measures", choices=[
   "prices paid by households",
   "prices received by domestic producers for their output",
   "wages paid to workers",
   "the cost of imported goods only",
   "the price of financial assets"], ans=1,
   why="The PPI tracks prices at the producer level, and it often moves ahead of the CPI."),
 dict(q="If the CPI rises from 200 to 210 over a year, the inflation rate is", choices=[
   "1.0%", "4.8%", "5.0%", "10.0%", "21.0%"], ans=2,
   why="(210 − 200)/200 = 0.05."),
 dict(q="If the CPI rises from 125 to 130, the inflation rate is", choices=[
   "3.8%", "4.0%", "5.0%", "5.5%", "6.5%"], ans=1,
   why="(130 − 125)/125 = 0.04."),
 dict(q="If the CPI falls from 150 to 147, the economy has experienced", choices=[
   "inflation of 2%", "deflation of 2%", "disinflation of 2%", "hyperinflation", "no change in prices"], ans=1,
   why="A falling price level is deflation, and (147 − 150)/150 = −0.02."),
 dict(q="Disinflation refers to", choices=[
   "a falling price level",
   "a positive but declining rate of inflation",
   "a rising rate of inflation",
   "an unchanged price level",
   "inflation above 50% per month"], ans=1,
   why="Prices are still rising under disinflation, just more slowly than before."),
 dict(q="Hyperinflation is usually defined as", choices=[
   "inflation above 3% per year",
   "an extremely rapid and accelerating rise in prices, often above 50% per month",
   "any inflation above the central bank's target",
   "deflation followed by inflation",
   "an increase in the price of one good"], ans=1,
   why="Hyperinflation is an order of magnitude beyond ordinary inflation and is nearly always driven by rapid money creation."),
 dict(q="If a basket cost $400 in the base year and $460 this year, the price index this year is", choices=[
   "60", "86.9", "100", "115", "146"], ans=3,
   why="100 × 460/400 = 115."),
 dict(q="If the price index is 125 and the base year index is 100, a good that cost $80 in the base year would cost approximately", choices=[
   "$64", "$80", "$95", "$100", "$105"], ans=3,
   why="$80 × 125/100 = $100 if the good's price tracked the general price level."),
 dict(q="Converting a nominal wage in year t into base-year dollars requires", choices=[
   "multiplying by the price index in year t",
   "dividing the nominal wage by the price index in year t and multiplying by 100",
   "subtracting the inflation rate",
   "dividing by the inflation rate",
   "adding the base-year index"], ans=1,
   why="Deflating by the index expresses the wage in constant purchasing power."),
 dict(q="A worker earned $30,000 when the CPI was 120 and earns $36,000 now that the CPI is 150. The worker's real wage has", choices=[
   "risen by 20%", "fallen slightly", "risen by 25%", "stayed exactly constant", "fallen by 20%"], ans=1,
   why="Nominal pay rose 20% while prices rose 25%, so real pay of $25,000 in base-year terms fell to $24,000."),
 dict(q="A cost-of-living adjustment clause in a wage contract is designed to", choices=[
   "raise real wages every year",
   "protect the real value of wages by raising nominal wages with the price index",
   "reduce nominal wages during inflation",
   "index taxes to income",
   "eliminate structural unemployment"], ans=1,
   why="COLAs keep purchasing power roughly constant when prices rise."),
 dict(q="Core inflation excludes", choices=[
   "housing and medical care",
   "food and energy prices, which are volatile",
   "all services",
   "imported goods",
   "durable goods"], ans=1,
   why="Stripping out the most volatile components gives a clearer view of the underlying trend."),
 dict(q="The CPI is used for all of the following EXCEPT", choices=[
   "indexing Social Security benefits",
   "measuring the volume of a country's physical output",
   "adjusting wages under COLA clauses",
   "converting nominal values into real values",
   "measuring changes in the cost of living"], ans=1,
   why="Output volume is measured by real GDP, not by a price index."),
 dict(q="If nominal GDP is $22 trillion and real GDP is $20 trillion, the GDP deflator equals", choices=[
   "90.9", "100", "102", "110", "120"], ans=3,
   why="100 × 22/20 = 110."),
 dict(q="If the GDP deflator is 125 and nominal GDP is $15 trillion, real GDP equals", choices=[
   "$1.875 trillion", "$11.0 trillion", "$12.0 trillion", "$15.0 trillion", "$18.75 trillion"], ans=2,
   why="Real GDP = 15 × 100/125 = $12 trillion."),
 dict(q="Which statement about the CPI and the GDP deflator is correct?", choices=[
   "they always give identical inflation rates",
   "they usually move together but can diverge, particularly when import prices change sharply",
   "the CPI includes capital goods",
   "the deflator uses a fixed basket",
   "the deflator excludes services"], ans=1,
   why="Different coverage and different weighting make the two measures similar in trend but not identical."),
 dict(q="A country rebases its CPI so that a more recent year equals 100. This will", choices=[
   "change all the measured inflation rates between past years",
   "rescale the index values without changing the percentage changes between years",
   "eliminate substitution bias",
   "make past inflation appear negative",
   "make the index unusable"], ans=1,
   why="Rebasing multiplies every index value by a constant, and percentage changes are unaffected by that scaling."),
 dict(q="Suppose gasoline prices double while all other prices are unchanged and gasoline is 5% of the basket. The CPI rises by approximately", choices=[
   "0.5%", "5%", "10%", "50%", "100%"], ans=1,
   why="A 100% rise on a 5% weight adds about 5 percentage points to the index."),
 dict(q="Which of the following would be recorded as inflation by the CPI even though households are not necessarily worse off?", choices=[
   "a rise in the price of an unchanged good",
   "a rise in the price of a laptop that accompanies a large improvement in its speed and battery life",
   "a general rise in all prices",
   "a rise in rents with no change in housing quality",
   "a rise in the price of milk"], ans=1,
   why="Without a full quality adjustment, part of the price increase that buys a better product is counted as pure inflation."),
 dict(q="Between Year 1 and Year 2 in the basket above, which good contributed the largest dollar increase to the cost of the basket?", table=BASKET, choices=[
   "bread, adding $5",
   "milk, adding $5",
   "gasoline, adding $20",
   "milk, adding $15",
   "bread, adding $25"], ans=2,
   why="Gasoline rose $1.00 on 20 units, adding $20 of the basket's $25 increase, while bread added $5 and milk added nothing."),
 dict(q="If the base year for the basket above were changed to Year 2, the index value for Year 1 would be", table=BASKET, choices=[
   "65.2", "75.0", "100.0", "115.0", "133.3"], ans=1,
   why="100 × $75/$100 = 75.0, since Year 1's basket cost three-quarters of Year 2's."),
 dict(q="A student computes inflation from Year 1 to Year 3 in the basket above as 33.3% + 15% = 48.3%. The error is that", choices=[
   "the two rates should be multiplied by 100",
   "percentage changes compound rather than add, so the correct figure is (1.333)(1.15) − 1 = 53.3%",
   "Year 2 should be excluded",
   "the base year is wrong",
   "the quantities changed between years"], ans=1,
   why="Applying a 15% rise on top of an already 33.3% higher level gives 53.3%, not 48.3%."),
 dict(q="The most important reason economists distinguish a change in one relative price from a change in the price level is that", choices=[
   "relative price changes are always larger",
   "a rise in one price signals a change in that market, while a rise in the price level affects the purchasing power of money generally",
   "relative prices are never measured",
   "the CPI ignores relative prices",
   "the price level never changes"], ans=1,
   why="Relative prices allocate resources between markets; the price level is a monetary phenomenon affecting all prices at once."),
]
