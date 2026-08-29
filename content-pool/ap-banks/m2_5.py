# MACRO 2.5 Costs of Inflation — 50 questions
# Arithmetic verified (no data table needed for this topic; all figures worked here):
#   Fisher equation, approximation: real rate = nominal rate - inflation rate
#     nominal 8%, inflation 3%  -> real = 5%
#     nominal 6%, inflation 9%  -> real = -3%  (lender loses purchasing power)
#     nominal 5%, expected inflation 2% -> expected real = 3%; if actual
#       inflation turns out to be 6%, realized real rate = 5 - 6 = -1%
#   Loan example: $1,000 borrowed at 5% nominal, repay $1,050 in one year.
#     If inflation is 5%, $1,050 next year buys what $1,000 buys today,
#     so the realized real return to the lender is 0%.
#     If inflation is 10%, $1,050 / 1.10 = $954.55 in today's dollars: the
#       lender is repaid less real value than was lent, a real loss of ~4.5%.
#   Fixed pension of $2,000 a month with 4% annual inflation: after one year
#     its purchasing power is 2,000 / 1.04 = $1,923.08, a loss of $76.92.
#   Nominal wage rising 3% with inflation of 5%: real wage change
#     = 1.03/1.05 - 1 = -1.9% (approximation: 3 - 5 = -2%)
TOPIC = ("2.5", "Costs of Inflation", 2)

QUESTIONS = [
 dict(q="Menu costs of inflation refer to", choices=[
   "the higher price of restaurant meals",
   "the real resources firms use to change and communicate their posted prices",
   "the cost of holding cash",
   "the loss suffered by lenders",
   "taxes on nominal capital gains"], ans=1,
   why="Reprinting catalogs, relabeling shelves, and updating systems are real costs of frequent price changes."),
 dict(q="Shoe-leather costs of inflation refer to", choices=[
   "the wear and tear on manufactured goods",
   "the time and effort spent economizing on cash holdings, such as making more frequent trips to the bank",
   "the cost of changing posted prices",
   "the cost of writing contracts",
   "the loss to borrowers"], ans=1,
   why="Inflation makes holding money costly, so people spend real resources minimizing their cash balances."),
 dict(q="Shoe-leather costs arise fundamentally because inflation acts like", choices=[
   "a subsidy on saving",
   "a tax on holding money, since currency loses purchasing power over time",
   "a tariff on imports",
   "a tax on labor income",
   "a reduction in the nominal interest rate"], ans=1,
   why="Cash pays no interest, so its real value erodes at the inflation rate."),
 dict(q="The unit-of-account problem created by inflation refers to", choices=[
   "the difficulty of counting currency",
   "the way changing prices make money a less reliable yardstick for comparing values and planning over time",
   "the cost of printing money",
   "a shortage of coins",
   "errors in the CPI"], ans=1,
   why="When the measuring stick itself changes length, accounting figures and long-run plans become harder to interpret."),
 dict(q="Because tax brackets and depreciation allowances are often stated in nominal terms, inflation can", choices=[
   "reduce real tax burdens",
   "raise real tax burdens by pushing taxpayers into higher brackets and taxing purely nominal gains",
   "have no effect on taxes",
   "eliminate the income tax",
   "reduce nominal revenue"], ans=1,
   why="This is bracket creep, and it means inflation raises real taxes without any legislated change."),
 dict(q="Unanticipated inflation redistributes purchasing power from", choices=[
   "borrowers to lenders",
   "lenders to borrowers",
   "workers to firms only",
   "the government to households",
   "importers to exporters"], ans=1,
   why="Loans are repaid in dollars worth less than expected, which benefits the debtor at the creditor's expense."),
 dict(q="A person who borrowed at a fixed nominal interest rate benefits from unexpectedly high inflation because", choices=[
   "the nominal amount owed falls",
   "the real value of the fixed nominal payments is lower than either party expected",
   "the interest rate is adjusted downward",
   "the loan is forgiven",
   "the lender must lend more"], ans=1,
   why="The debt is fixed in dollars, and those dollars are worth less than anticipated."),
 dict(q="Who is most harmed by unexpectedly high inflation?", choices=[
   "a homeowner with a 30-year fixed-rate mortgage",
   "a bank holding long-term fixed-rate loans",
   "a worker whose wage is indexed to the CPI",
   "the federal government as a net debtor",
   "a firm with large fixed-rate debts"], ans=1,
   why="The bank receives a stream of fixed nominal payments whose real value has been eroded."),
 dict(q="A retiree living on a fixed nominal pension is harmed by inflation because", choices=[
   "the nominal pension falls",
   "the same nominal payment buys fewer goods each year",
   "pensions are taxed at a higher rate",
   "the retiree must work more",
   "nominal interest rates fall"], ans=1,
   why="Nothing about the payment changes, but its purchasing power shrinks."),
 dict(q="A pension of $2,000 a month is not indexed, and inflation is 4% over the year. In terms of the prior year's purchasing power, the payment is now worth about", choices=[
   "$1,846", "$1,923", "$2,000", "$2,080", "$2,400"], ans=1,
   why="$2,000 ÷ 1.04 = $1,923, a loss of about $77 of purchasing power a month."),
 dict(q="The Fisher equation states, approximately, that", choices=[
   "the real interest rate equals the nominal rate plus inflation",
   "the nominal interest rate equals the real interest rate plus the expected inflation rate",
   "inflation equals the money supply growth rate",
   "the real rate always equals zero",
   "nominal GDP equals real GDP times inflation"], ans=1,
   why="Lenders add expected inflation to the real return they require."),
 dict(q="If the nominal interest rate is 8% and inflation is 3%, the real interest rate is approximately", choices=[
   "3%", "5%", "8%", "11%", "24%"], ans=1,
   why="Real ≈ nominal − inflation = 8 − 3 = 5%."),
 dict(q="If the nominal interest rate is 6% and inflation turns out to be 9%, the realized real interest rate is approximately", choices=[
   "-15%", "-3%", "3%", "6%", "15%"], ans=1,
   why="6 − 9 = −3%, so the lender's purchasing power actually fell."),
 dict(q="A lender charges 5% expecting 2% inflation, but inflation turns out to be 6%. The lender's realized real return is approximately", choices=[
   "-1%", "3%", "5%", "6%", "11%"], ans=0,
   why="The realized real rate is 5 − 6 = −1%, three percentage points below the 3% expected."),
 dict(q="If inflation is fully and correctly anticipated by everyone, then", choices=[
   "there are no costs of inflation whatsoever",
   "the redistribution between borrowers and lenders is largely avoided because nominal interest rates adjust, though menu and shoe-leather costs remain",
   "borrowers always gain",
   "lenders always gain",
   "the real interest rate must be zero"], ans=1,
   why="Anticipation removes the surprise redistribution but not the resource costs of operating with changing prices."),
 dict(q="The main reason unanticipated inflation is considered more costly than anticipated inflation is that", choices=[
   "it is always larger",
   "it arbitrarily redistributes wealth between parties to nominal contracts who could not adjust in advance",
   "menu costs are higher",
   "it always causes unemployment",
   "it cannot be measured"], ans=1,
   why="Contracts written on the wrong forecast transfer real wealth in a way no one intended."),
 dict(q="Inflation uncertainty tends to reduce long-term lending because", choices=[
   "borrowers cannot repay",
   "lenders face greater risk that the real return will be far from what they expected",
   "nominal rates cannot change",
   "the government forbids it",
   "inflation lowers the demand for loans"], ans=1,
   why="Greater variance in the real return makes long-horizon nominal contracts unattractive."),
 dict(q="A worker whose nominal wage rises 3% during a year in which inflation is 5% experiences", choices=[
   "a real wage increase of 8%",
   "a real wage decrease of about 2%",
   "a real wage increase of 2%",
   "no change in the real wage",
   "a real wage decrease of 5%"], ans=1,
   why="Real wage growth is approximately nominal growth minus inflation, 3 − 5 = −2%."),
 dict(q="A worker whose nominal wage rises 6% during a year in which inflation is 2% experiences a real wage change of approximately", choices=[
   "-4%", "0%", "+3%", "+4%", "+8%"], ans=3,
   why="6 − 2 = +4%."),
 dict(q="Wage contracts negotiated before an unexpected surge in inflation tend to", choices=[
   "raise real wages",
   "lower real wages, transferring purchasing power from workers to employers",
   "leave real wages unchanged",
   "raise nominal wages automatically",
   "eliminate unemployment"], ans=1,
   why="A fixed nominal wage buys less when prices rise faster than expected."),
 dict(q="Indexing a contract to the CPI is intended to", choices=[
   "raise real payments over time",
   "hold the real value of the payments roughly constant regardless of inflation",
   "reduce the nominal payment",
   "eliminate menu costs",
   "guarantee a positive nominal interest rate"], ans=1,
   why="Indexation adjusts nominal amounts so purchasing power is preserved."),
 dict(q="Which asset holder is most protected against unanticipated inflation?", choices=[
   "the holder of cash under a mattress",
   "the holder of an inflation-indexed government bond",
   "the holder of a long-term fixed-rate corporate bond",
   "the holder of a fixed-rate savings account",
   "a lender under a fixed nominal mortgage"], ans=1,
   why="An indexed bond's principal and coupon rise with the price level."),
 dict(q="Deflation is", choices=[
   "a slowing of the rate of inflation",
   "a sustained fall in the general price level",
   "a fall in the price of one good",
   "an increase in the real interest rate only",
   "an increase in unemployment"], ans=1,
   why="Deflation means the price level itself is declining, so the inflation rate is negative."),
 dict(q="Deflation harms borrowers because", choices=[
   "nominal debts fall in value",
   "the real value of their fixed nominal debts rises as prices fall",
   "interest rates rise automatically",
   "lenders demand early repayment",
   "wages rise faster than prices"], ans=1,
   why="Falling prices make each dollar of debt harder to earn, which is the opposite of the borrower's gain under inflation."),
 dict(q="A serious danger of deflation is that consumers may", choices=[
   "spend more immediately",
   "postpone purchases in expectation of lower prices, further reducing aggregate demand",
   "borrow more heavily",
   "demand higher nominal wages",
   "hold less cash"], ans=1,
   why="Anticipated price declines reward waiting, which can deepen a downturn."),
 dict(q="During deflation, holding cash offers", choices=[
   "a negative real return",
   "a positive real return, since each dollar buys more over time",
   "no real return",
   "a return equal to the nominal interest rate",
   "the same return as during inflation"], ans=1,
   why="A stable nominal balance gains purchasing power when prices fall."),
 dict(q="With a nominal interest rate near zero and deflation of 2%, the real interest rate is approximately", choices=[
   "-2%", "0%", "+2%", "+4%", "+6%"], ans=2,
   why="Real ≈ 0 − (−2) = +2%, which is why deflation makes borrowing expensive even when nominal rates cannot fall further."),
 dict(q="Because nominal interest rates cannot fall far below zero, deflation makes monetary policy", choices=[
   "more effective",
   "less effective, because the central bank cannot push the real interest rate low enough",
   "unnecessary",
   "automatically expansionary",
   "identical to fiscal policy"], ans=1,
   why="The zero lower bound on nominal rates puts a floor under the real rate when inflation is negative."),
 dict(q="Which of the following is a real resource cost rather than a redistribution?", choices=[
   "a borrower gaining at a lender's expense",
   "the labor and materials used to reprint price lists",
   "a retiree's pension losing purchasing power",
   "a bank earning a lower real return",
   "a worker's real wage falling"], ans=1,
   why="Menu costs consume resources that could have produced something else; the others move purchasing power between people."),
 dict(q="During hyperinflation, money increasingly fails to serve as", choices=[
   "a medium of exchange only",
   "a store of value and a unit of account, so barter and foreign currency take over",
   "legal tender",
   "a means of paying taxes",
   "a factor of production"], ans=1,
   why="When prices double weekly, no one wants to hold the currency and no one can price with it."),
 dict(q="The efficiency loss from very high inflation is greatest because", choices=[
   "menu costs alone are enormous",
   "relative price signals become hard to read, so resources are misallocated across markets",
   "the CPI cannot be computed",
   "unemployment must rise",
   "exports become impossible"], ans=1,
   why="Prices coordinate production, and rapidly changing money prices obscure what is genuinely becoming scarce."),
 dict(q="A firm that must reprice its entire product line every week during high inflation is bearing", choices=[
   "shoe-leather costs", "menu costs", "an inflation tax on cash only", "a redistribution loss", "a nominal capital gains tax"], ans=1,
   why="The resources spent changing posted prices are the definition of menu costs."),
 dict(q="A household making daily trips to the bank because holding cash is costly during high inflation is bearing", choices=[
   "menu costs", "shoe-leather costs", "a unit-of-account problem", "a tax bracket effect", "a real wage loss"], ans=1,
   why="Time and effort spent economizing on money balances are shoe-leather costs."),
 dict(q="Nominal capital gains taxation during inflation means an investor may", choices=[
   "pay less tax than the real gain warrants",
   "owe tax on a gain that is entirely inflation and represents no increase in purchasing power",
   "owe no tax at all",
   "receive a refund automatically",
   "be indexed automatically"], ans=1,
   why="Taxing an unindexed nominal gain taxes the erosion of the currency itself."),
 dict(q="Which group tends to gain from unanticipated inflation?", choices=[
   "creditors holding fixed-rate loans",
   "debtors with fixed-rate obligations, including a heavily indebted government",
   "people on fixed nominal incomes",
   "holders of currency",
   "workers with long-term fixed nominal wage contracts"], ans=1,
   why="Fixed nominal obligations are repaid in cheaper dollars."),
 dict(q="A government that finances spending by printing money is said to collect", choices=[
   "a payroll tax",
   "an inflation tax, since the resulting inflation erodes the value of the money the public holds",
   "a tariff",
   "a capital gains tax",
   "a property tax"], ans=1,
   why="The public's purchasing power is transferred to the issuer without any legislated levy."),
 dict(q="Which statement about moderate, stable, anticipated inflation is most accurate?", choices=[
   "it imposes no costs at all",
   "its costs are real but modest, mainly menu and shoe-leather costs and tax distortions",
   "it is more damaging than hyperinflation",
   "it always causes unemployment",
   "it eliminates all redistribution"], ans=1,
   why="Predictability removes most of the redistribution, leaving smaller resource and tax costs."),
 dict(q="Most central banks target a small positive inflation rate rather than zero partly because", choices=[
   "inflation is always beneficial",
   "a small buffer keeps the economy away from deflation and allows real wages to adjust downward without nominal wage cuts",
   "zero inflation is impossible to measure",
   "it maximizes the inflation tax",
   "it eliminates menu costs"], ans=1,
   why="Nominal wages are sticky downward, and a positive target also guards against the greater dangers of deflation."),
 dict(q="A borrower and a lender agree on a 7% nominal rate expecting 4% inflation. Inflation turns out to be 1%. The result is that", choices=[
   "the borrower gains",
   "the lender gains, receiving a realized real return of about 6% instead of 3%",
   "neither party is affected",
   "the loan is void",
   "the real rate is 8%"], ans=1,
   why="Lower-than-expected inflation makes the fixed repayment worth more than either party planned."),
 dict(q="Consider a $1,000 one-year loan at a 5% nominal rate. If inflation over the year is 5%, the lender's realized real return is", choices=[
   "-5%", "0%", "5%", "10%", "105%"], ans=1,
   why="The $1,050 repaid buys exactly what $1,000 bought at the start of the year."),
 dict(q="Consider the same $1,000 loan at 5% when inflation turns out to be 10%. In beginning-of-year dollars, the lender receives about", choices=[
   "$909", "$955", "$1,000", "$1,050", "$1,155"], ans=1,
   why="$1,050 ÷ 1.10 = $954.55, so the lender is repaid less real value than was lent."),
 dict(q="Inflation is sometimes described as a cruel tax because it", choices=[
   "is legislated by Congress",
   "falls hardest on those holding cash and on those with fixed nominal incomes, groups that are often less able to protect themselves",
   "applies only to the wealthy",
   "is refunded each year",
   "reduces the money supply"], ans=1,
   why="Those without indexed incomes or inflation-protected assets bear the largest share."),
 dict(q="Which of the following is NOT a cost of inflation?", choices=[
   "menu costs",
   "an increase in real output that occurs simply because prices are rising",
   "shoe-leather costs",
   "arbitrary redistribution between debtors and creditors",
   "distortions in an unindexed tax system"], ans=1,
   why="A higher price level does not by itself create real output, which is precisely why economists study inflation's costs rather than its benefits."),
 dict(q="Two economies both average 4% inflation, but one's inflation is highly variable. The economy with variable inflation will most likely experience", choices=[
   "identical costs",
   "larger costs, because uncertainty makes nominal contracting riskier and misallocates resources",
   "smaller costs",
   "no menu costs",
   "a lower natural rate of unemployment"], ans=1,
   why="Variability, not just the average level, is what makes forecasting and contracting difficult."),
 dict(q="If a labor contract contains a full COLA clause and inflation exceeds expectations, the redistribution from worker to employer is", choices=[
   "larger than without the clause",
   "largely eliminated, because nominal wages rise with the price level",
   "unchanged",
   "reversed entirely in favor of the employer",
   "converted into a menu cost"], ans=1,
   why="Indexation is precisely the device that protects real wages from an inflation surprise."),
 dict(q="Suppose all wages, contracts, taxes, and interest rates were perfectly indexed to the price level. Remaining costs of inflation would be limited mainly to", choices=[
   "redistribution between debtors and creditors",
   "menu costs, shoe-leather costs, and confusion in comparing values over time",
   "unemployment",
   "falling real GDP",
   "a rising natural rate"], ans=1,
   why="Perfect indexation removes redistribution but not the resource costs of continually changing prices."),
 dict(q="Which best explains why holding currency is costly during inflation while holding an interest-bearing account may not be?", choices=[
   "currency is not legal tender",
   "currency pays no nominal interest, so its real return is the negative of the inflation rate, while a deposit's nominal interest can offset rising prices",
   "deposits are indexed by law",
   "currency is taxed",
   "banks do not lend during inflation"], ans=1,
   why="The cost of holding money is the interest forgone, and inflation raises nominal rates."),
 dict(q="An economy experiences 2% deflation while nominal wages are rigid. The most likely consequence is", choices=[
   "a fall in real wages and a rise in employment",
   "a rise in real wages and, with it, a rise in unemployment",
   "no effect on the labor market",
   "an immediate rise in aggregate demand",
   "a rise in the price level"], ans=1,
   why="If nominal wages will not fall, falling prices push real labor costs up and firms hire fewer workers."),
 dict(q="A student claims that inflation makes everyone poorer because prices rise. The most important correction is that", choices=[
   "prices never rise for everyone",
   "in aggregate, higher prices are also higher incomes for sellers, so inflation's harm lies in redistribution and resource costs rather than in a fall in total real income",
   "inflation always raises real GDP",
   "the CPI is unreliable",
   "wages always rise faster than prices"], ans=1,
   why="Every price is someone's cost and someone else's revenue, so the aggregate effect is not a straightforward loss of real income."),
 dict(q="Ranking the costs of inflation, most economists would agree that the largest costs arise when inflation is", choices=[
   "low, stable, and fully anticipated",
   "high, variable, and unanticipated",
   "exactly equal to zero",
   "slightly negative",
   "equal to the nominal interest rate"], ans=1,
   why="Unpredictability drives both the redistribution and the misallocation of resources."),
]
