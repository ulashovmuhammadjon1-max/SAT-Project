# MACRO 5.4 Government Deficits and the National Debt — 50 questions
# Every number worked out:
#   BUDGET table: revenue and outlays in billions.
#     Yr1: rev 900, out 950 -> deficit 50.  Yr2: rev 1,000, out 1,120 -> deficit 120.
#     Yr3: rev 1,150, out 1,100 -> surplus 50. Yr4: rev 1,200, out 1,280 -> deficit 80.
#     Sum of Yr1-Yr4 balances: -50 - 120 + 50 - 80 = -200, so debt rises by 200 over
#     the four years. Starting debt 1,000 -> ending debt 1,200.
#     Debt at end of Yr1 = 1,050; Yr2 = 1,170; Yr3 = 1,120; Yr4 = 1,200.
#   Debt-to-GDP: debt 1,200 with GDP 4,000 -> 30%. Debt 1,500 with GDP 5,000 -> 30%,
#     so a larger debt can be a smaller ratio only if GDP grows faster; here they tie.
#   Debt 4,000 and GDP 8,000 -> 50%. If debt grows 2% to 4,080 while GDP grows 5% to
#     8,400, the ratio falls to 4,080/8,400 = 48.6%, below 50%.
#   Deficit 300 with GDP 6,000 -> deficit is 5% of GDP.
TOPIC = ("5.4", "Government Deficits and the National Debt", 5)
BUDGET = dict(
    headers=["Year", "Tax revenue ($b)", "Government outlays ($b)"],
    rows=[["1", "900", "950"], ["2", "1,000", "1,120"], ["3", "1,150", "1,100"], ["4", "1,200", "1,280"]],
)
QUESTIONS = [
 dict(q="A government budget deficit occurs when", choices=[
   "tax revenue exceeds government outlays in a year",
   "government outlays exceed tax revenue in a year",
   "the national debt falls",
   "the government owes money to foreigners",
   "the money supply grows"], ans=1,
   why="A deficit is the annual shortfall of revenue against spending."),
 dict(q="The national debt is best described as", choices=[
   "the amount by which spending exceeded revenue last year",
   "the accumulated total of past deficits less past surpluses",
   "the annual interest payment on borrowing",
   "the government's tax revenue",
   "the trade deficit"], ans=1,
   why="The debt is the stock built up by the flow of yearly deficits and surpluses."),
 dict(q="The key distinction between the deficit and the debt is that", choices=[
   "they are the same thing measured in different units",
   "the deficit is a flow measured over a period while the debt is a stock measured at a point in time",
   "the debt is measured yearly and the deficit is cumulative",
   "the deficit includes interest and the debt does not",
   "only the debt can be negative"], ans=1,
   why="A flow accumulates into a stock, the way annual saving accumulates into wealth."),
 dict(q="Which of the following is analogous to the relationship between the deficit and the debt?", choices=[
   "the relationship between price and quantity",
   "the relationship between the water flowing into a bathtub each minute and the water standing in the tub",
   "the relationship between exports and imports",
   "the relationship between the money supply and velocity",
   "the relationship between wages and employment"], ans=1,
   why="The inflow per period is the flow; the accumulated level is the stock."),
 dict(q="If a government runs a budget surplus, the national debt will", choices=[
   "rise", "fall", "stay the same", "double", "become negative automatically"], ans=1,
   why="A surplus lets the government retire some outstanding debt."),
 dict(q="A country can run a smaller deficit this year than last year and still see its national debt", choices=[
   "fall", "rise", "stay constant necessarily", "disappear", "become negative"], ans=1,
   why="Any deficit at all adds to the debt; only a surplus reduces it."),
 dict(q="Refer to the table. The budget balance in Year 2 is", table=BUDGET, choices=[
   "a surplus of $50 billion", "a deficit of $50 billion", "a deficit of $80 billion",
   "a deficit of $120 billion", "a surplus of $120 billion"], ans=3,
   why="Outlays of $1,120 billion less revenue of $1,000 billion is a $120 billion deficit."),
 dict(q="Refer to the table. Which year shows a budget surplus?", table=BUDGET, choices=[
   "Year 1", "Year 2", "Year 3", "Year 4", "none of the years"], ans=2,
   why="In Year 3 revenue of $1,150 billion exceeds outlays of $1,100 billion."),
 dict(q="Refer to the table. Over the four years combined, the government's debt changes by", table=BUDGET, choices=[
   "an increase of $50 billion", "an increase of $120 billion", "an increase of $200 billion",
   "a decrease of $200 billion", "no change"], ans=2,
   why="Summing the balances gives -50 - 120 + 50 - 80 = -$200 billion, so the debt rises by $200 billion."),
 dict(q="Refer to the table. If the debt at the start of Year 1 was $1,000 billion, the debt at the end of Year 4 is", table=BUDGET, choices=[
   "$800 billion", "$1,000 billion", "$1,120 billion", "$1,200 billion", "$1,400 billion"], ans=3,
   why="The $200 billion of cumulative deficits adds to the opening $1,000 billion."),
 dict(q="Refer to the table. The debt outstanding at the end of Year 3, starting from $1,000 billion, is", table=BUDGET, choices=[
   "$1,050 billion", "$1,120 billion", "$1,170 billion", "$1,200 billion", "$1,220 billion"], ans=1,
   why="1,000 + 50 + 120 - 50 = $1,120 billion."),
 dict(q="If the national debt is $1,200 billion and nominal GDP is $4,000 billion, the debt-to-GDP ratio is", choices=[
   "12%", "24%", "30%", "33%", "48%"], ans=2,
   why="1,200/4,000 = 0.30, or 30%."),
 dict(q="If a country's deficit is $300 billion and its nominal GDP is $6,000 billion, the deficit as a share of GDP is", choices=[
   "0.5%", "2%", "3%", "5%", "20%"], ans=3,
   why="300/6,000 = 5%."),
 dict(q="Economists usually focus on the debt-to-GDP ratio rather than the dollar level of the debt because", choices=[
   "the dollar level is impossible to measure",
   "the ratio compares the debt with the economy's capacity to service it",
   "GDP is fixed",
   "the ratio is always constant",
   "only foreigners care about the ratio"], ans=1,
   why="A larger economy can carry a larger debt, so the burden depends on the size of the tax base."),
 dict(q="A country's debt grows 2 percent while its nominal GDP grows 5 percent. The debt-to-GDP ratio will", choices=[
   "rise", "fall", "stay the same", "double", "become negative"], ans=1,
   why="When the denominator grows faster than the numerator, the ratio declines."),
 dict(q="A country's debt-to-GDP ratio will rise when", choices=[
   "the debt grows more slowly than nominal GDP",
   "the debt grows faster than nominal GDP",
   "the budget is balanced and GDP grows",
   "the government runs a surplus and GDP grows",
   "inflation raises nominal GDP faster than borrowing"], ans=1,
   why="The ratio follows the relative growth rates of its numerator and denominator."),
 dict(q="A country with a balanced budget and positive nominal GDP growth will see its debt-to-GDP ratio", choices=[
   "rise", "fall", "stay exactly the same", "become negative", "double"], ans=1,
   why="The debt is unchanged while GDP grows, so the ratio shrinks."),
 dict(q="A cyclical deficit is one that arises because", choices=[
   "the government has permanently high spending programs",
   "a recession reduces tax revenues and raises transfer payments",
   "the central bank raised interest rates",
   "the debt is held by foreigners",
   "tax rates were cut permanently"], ans=1,
   why="Automatic stabilizers widen the deficit when output is below potential."),
 dict(q="A structural deficit is the deficit that would exist", choices=[
   "only during a recession",
   "even if the economy were producing at potential output",
   "only when the debt is zero",
   "only if interest rates were zero",
   "only in wartime"], ans=1,
   why="It reflects the government's tax and spending policies rather than the state of the business cycle."),
 dict(q="During a recession, the budget deficit tends to", choices=[
   "shrink automatically",
   "widen automatically as revenues fall and transfers rise",
   "become a surplus",
   "stay exactly constant",
   "be eliminated by law"], ans=1,
   why="Automatic stabilizers move the budget toward deficit when incomes fall."),
 dict(q="An expansion tends to", choices=[
   "widen the deficit",
   "narrow the deficit as tax revenues rise and transfer payments fall",
   "leave the budget unchanged",
   "raise the structural deficit",
   "raise the debt-to-GDP ratio"], ans=1,
   why="Rising incomes raise tax collections and reduce spending on benefits."),
 dict(q="Government debt held by the public consists of", choices=[
   "debt owed by households to banks",
   "government securities held by individuals, firms, foreign investors, and central banks outside the government",
   "the government's holdings of private assets",
   "unpaid taxes",
   "corporate bonds"], ans=1,
   why="It is the part of the debt actually sold into financial markets."),
 dict(q="Intragovernmental debt refers to", choices=[
   "debt owed to foreign governments",
   "debt one part of the government owes to another, such as bonds held by a social insurance trust fund",
   "debt owed by state governments to households",
   "debt held by commercial banks",
   "debt that has been repaid"], ans=1,
   why="It is an internal accounting claim rather than borrowing from the public."),
 dict(q="When the national debt is held largely by domestic residents, the burden of repayment is", choices=[
   "entirely a transfer of resources to foreigners",
   "largely a transfer from taxpayers to domestic bondholders rather than a loss of national income",
   "zero in all senses",
   "borne only by future foreigners",
   "impossible to describe"], ans=1,
   why="Payments stay inside the country, though the redistribution and the tax distortions are real costs."),
 dict(q="When a large share of the national debt is held by foreign investors,", choices=[
   "interest payments stay within the domestic economy",
   "interest payments represent a flow of income out of the country",
   "the debt has no cost",
   "the debt is automatically forgiven",
   "the debt-to-GDP ratio must fall"], ans=1,
   why="Servicing foreign-held debt sends real purchasing power abroad."),
 dict(q="A commonly cited cost of a large and rising national debt is that", choices=[
   "it reduces the money supply",
   "growing interest payments crowd out other government spending or require higher taxes",
   "it eliminates the trade deficit",
   "it lowers the price level",
   "it always causes deflation"], ans=1,
   why="Debt service is a claim on the budget before any program can be funded."),
 dict(q="A frequently cited argument that the burden of the debt is passed to future generations is that", choices=[
   "future generations must repay foreign creditors and may face higher taxes and a smaller capital stock",
   "money loses value automatically",
   "the debt must be repaid within one year",
   "past generations pay no taxes",
   "interest rates are always zero"], ans=0,
   why="Deficit finance can reduce investment today, leaving future workers with less capital and a larger tax bill."),
 dict(q="A counterargument to the claim that debt always burdens future generations is that", choices=[
   "the debt is never repaid",
   "borrowing that finances productive public investment can raise future output enough to more than cover the cost",
   "interest payments are illegal",
   "future generations do not pay taxes",
   "the debt is always held abroad"], ans=1,
   why="What matters is whether the borrowed funds are spent on something that raises future capacity."),
 dict(q="A government that borrows to build roads, bridges, and schools differs from one that borrows to fund current transfers in that", choices=[
   "only the first raises the debt",
   "the first adds to the capital stock, which may raise future output and the tax base",
   "the second is always cheaper",
   "only the second raises interest rates",
   "there is no economic difference"], ans=1,
   why="Public investment creates an asset alongside the liability."),
 dict(q="Persistent large deficits are most likely to raise", choices=[
   "the money supply automatically",
   "the real interest rate, as the government competes with private borrowers for funds",
   "the natural rate of unemployment",
   "velocity",
   "the price level in the short run only"], ans=1,
   why="Additional government demand for loanable funds bids the real interest rate up."),
 dict(q="A default on government debt would most likely", choices=[
   "lower interest rates on future government borrowing",
   "raise the risk premium and thus the interest rate the government must pay in the future",
   "eliminate the debt with no consequences",
   "raise the country's credit rating",
   "reduce the trade deficit"], ans=1,
   why="Lenders demand compensation for the risk that they will not be repaid."),
 dict(q="A government that borrows in its own currency and controls its central bank", choices=[
   "cannot ever run a deficit",
   "can always meet nominal obligations by creating money, but at the cost of inflation",
   "must default whenever debt is high",
   "faces no economic constraints at all",
   "has zero interest payments"], ans=1,
   why="Monetizing debt avoids nominal default but transfers the cost to money holders through inflation."),
 dict(q="A balanced budget amendment requiring the budget to balance every year would", choices=[
   "strengthen automatic stabilizers",
   "force spending cuts or tax increases during recessions, making downturns worse",
   "eliminate the business cycle",
   "raise potential output",
   "have no effect on the economy"], ans=1,
   why="It would require contractionary policy exactly when the economy is weakest."),
 dict(q="Interest payments on the national debt appear in the government budget as", choices=[
   "revenue",
   "an outlay that must be paid regardless of current program choices",
   "a transfer from foreigners",
   "an investment",
   "a reduction in the debt"], ans=1,
   why="Debt service is mandatory spending that competes with everything else."),
 dict(q="If nominal interest rates rise sharply, a highly indebted government will face", choices=[
   "lower debt service costs",
   "higher debt service costs as maturing debt is refinanced at higher rates",
   "an automatic surplus",
   "a lower debt-to-GDP ratio",
   "no budget change"], ans=1,
   why="Rolling over existing debt at higher rates raises interest outlays."),
 dict(q="Unexpected inflation affects the real value of outstanding government debt by", choices=[
   "raising it",
   "reducing it, since the debt is repaid in dollars of lower purchasing power",
   "leaving it unchanged",
   "converting it into equity",
   "eliminating interest payments"], ans=1,
   why="Government is a large nominal debtor, so surprise inflation shrinks the real burden."),
 dict(q="Which of the following would reduce the deficit without changing tax rates or program design?", choices=[
   "a recession",
   "an economic expansion that raises incomes and tax collections",
   "an increase in transfer payments",
   "a rise in interest rates",
   "an increase in defense spending"], ans=1,
   why="Cyclical improvement raises revenue and reduces benefit spending automatically."),
 dict(q="A country whose debt-to-GDP ratio is 50 percent has debt of $4,000 billion. Its nominal GDP is", choices=[
   "$2,000 billion", "$4,000 billion", "$6,000 billion", "$8,000 billion", "$10,000 billion"], ans=3,
   why="If 4,000 is half of GDP, GDP is $8,000 billion."),
 dict(q="Two countries have equal dollar debts, but one has twice the GDP of the other. Compared with the smaller economy, the larger economy's debt is", choices=[
   "a larger burden relative to its capacity to repay",
   "a smaller burden relative to its capacity to repay",
   "identical in burden",
   "impossible to compare",
   "necessarily unsustainable"], ans=1,
   why="The same debt against a bigger tax base is a smaller debt-to-GDP ratio."),
 dict(q="Government borrowing is financed by", choices=[
   "printing currency only",
   "selling government bonds to households, firms, and foreign investors",
   "raising the reserve requirement",
   "taxing bondholders",
   "reducing the money multiplier"], ans=1,
   why="Deficits are covered by issuing debt securities in financial markets."),
 dict(q="The primary deficit differs from the total deficit in that the primary deficit", choices=[
   "includes only interest payments",
   "excludes interest payments on existing debt",
   "includes only defense spending",
   "measures the debt rather than the deficit",
   "is always larger"], ans=1,
   why="It isolates the budget balance attributable to current programs and taxes."),
 dict(q="A country running a primary surplus but a total deficit is one where", choices=[
   "programs cost more than revenue",
   "revenue exceeds program spending but not once interest on the debt is added",
   "the debt is falling",
   "interest payments are zero",
   "revenue is zero"], ans=1,
   why="Interest costs alone are turning a program surplus into an overall deficit."),
 dict(q="Which of the following is a stock rather than a flow?", choices=[
   "this year's budget deficit",
   "the national debt outstanding at the end of the year",
   "annual tax revenue",
   "annual government spending",
   "quarterly interest payments"], ans=1,
   why="A stock is measured at a moment; the other items are measured over a period."),
 dict(q="Which of the following is a flow rather than a stock?", choices=[
   "the national debt",
   "the annual budget deficit",
   "the capital stock",
   "household wealth",
   "the money supply"], ans=1,
   why="The deficit is measured per unit of time."),
 dict(q="If a government runs deficits every year for a decade, the national debt at the end of the decade must be", choices=[
   "lower than at the start",
   "higher than at the start",
   "unchanged",
   "zero",
   "equal to the last year's deficit"], ans=1,
   why="Each year's deficit adds to the accumulated stock."),
 dict(q="During a severe recession, most economists would argue that a larger deficit is", choices=[
   "always harmful and should be avoided",
   "acceptable, because the alternative of cutting spending or raising taxes would deepen the downturn",
   "irrelevant to output",
   "certain to cause hyperinflation",
   "the same as a surplus"], ans=1,
   why="Deficit finance supports aggregate demand when private spending is weak."),
 dict(q="Debt monetization occurs when", choices=[
   "the government repays debt with tax revenue",
   "the central bank buys government bonds, effectively financing the deficit with new money",
   "foreigners buy government bonds",
   "the government issues equity",
   "the debt is forgiven"], ans=1,
   why="Central bank purchases replace bond finance with money creation."),
 dict(q="Sustained debt monetization is dangerous mainly because it", choices=[
   "lowers the price level",
   "leads to rapid money growth and inflation",
   "raises real output permanently",
   "reduces the deficit",
   "raises the real interest rate permanently"], ans=1,
   why="Financing spending with new money is the classic route to high inflation."),
 dict(q="A country's debt is considered sustainable when", choices=[
   "the dollar level of debt never rises",
   "the debt-to-GDP ratio is stable or falling over time",
   "there is no interest payment",
   "all debt is held abroad",
   "the budget is balanced every single year"], ans=1,
   why="Sustainability is about the ratio's trajectory, not the raw level."),
 dict(q="If the interest rate on government debt is below the growth rate of nominal GDP, a country running a small primary deficit may still see its debt-to-GDP ratio", choices=[
   "rise without limit",
   "stabilize or fall, because GDP grows faster than the debt compounds",
   "become negative",
   "double each year",
   "be unaffected by growth"], ans=1,
   why="Growth in the denominator can outpace the compounding of the numerator."),
]
