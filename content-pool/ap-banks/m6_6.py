# MACRO 6.6 Real Interest Rates and International Capital Flows — 50 questions
# Arithmetic verified line by line:
#   LF table (loanable funds, billions):
#     real rate 3%: quantity demanded 900, quantity supplied 700 -> shortage 200.
#     real rate 4%: quantity demanded 800, quantity supplied 800 -> equilibrium.
#     real rate 5%: quantity demanded 700, quantity supplied 900 -> surplus 200.
#   Fisher: real rate = nominal rate - inflation rate.
#     nominal 7% with inflation 3% -> real 4%.
#     nominal 5% with inflation 6% -> real -1%.
#     nominal 9% with inflation 2% -> real 7%.
#     To get a real return of 4% with expected inflation of 5%, the nominal rate
#     must be 9%.
#   Comparison: Country A real rate 5%, Country B real rate 2%. Financial capital
#     flows from B to A; A's currency appreciates and B's depreciates.
#   Chain: budget deficit up -> demand for loanable funds up -> real rate up ->
#     domestic investment falls (crowding out) and foreign financial capital flows
#     in -> currency appreciates -> net exports fall.
TOPIC = ("6.6", "Real Interest Rates and International Capital Flows", 6)

LF = dict(headers=["Real interest rate", "Quantity of loanable funds demanded (billions)",
                   "Quantity of loanable funds supplied (billions)"],
          rows=[["3%", "900", "700"],
                ["4%", "800", "800"],
                ["5%", "700", "900"]])

QUESTIONS = [
 dict(q="The real interest rate is best defined as", choices=[
   "the interest rate posted by banks",
   "the nominal interest rate minus the inflation rate",
   "the nominal interest rate plus the inflation rate",
   "the return on stocks",
   "the rate at which the money supply grows"], ans=1,
   why="The real rate is the nominal rate adjusted for the loss of purchasing power from inflation."),
 dict(q="If the nominal interest rate is 7 percent and inflation is 3 percent, the real interest rate is", choices=[
   "-4 percent", "3 percent", "4 percent", "7 percent", "10 percent"], ans=2,
   why="7 minus 3 equals 4 percent."),
 dict(q="If the nominal interest rate is 5 percent and inflation is 6 percent, the real interest rate is", choices=[
   "-1 percent", "0 percent", "1 percent", "5 percent", "11 percent"], ans=0,
   why="5 minus 6 equals -1 percent, so lenders lose purchasing power."),
 dict(q="If the nominal interest rate is 9 percent and inflation is 2 percent, the real interest rate is", choices=[
   "2 percent", "5 percent", "7 percent", "9 percent", "11 percent"], ans=2,
   why="9 minus 2 equals 7 percent."),
 dict(q="A lender who wants a real return of 4 percent and expects 5 percent inflation should charge a nominal rate of", choices=[
   "1 percent", "4 percent", "5 percent", "9 percent", "20 percent"], ans=3,
   why="The nominal rate must equal the desired real rate plus expected inflation."),
 dict(q="International financial capital flows respond most directly to differences across countries in", choices=[
   "nominal interest rates alone",
   "expected real interest rates, adjusted for risk",
   "unemployment rates",
   "population size",
   "the level of government spending"], ans=1,
   why="Investors care about purchasing power returns, not just the posted nominal rate."),
 dict(q="Country A has a real interest rate of 5 percent and Country B has a real interest rate of 2 percent. Financial capital will tend to flow", choices=[
   "from A to B", "from B to A", "in neither direction", "equally in both directions", "only if the currencies are pegged"], ans=1,
   why="Financial capital seeks the higher real return."),
 dict(q="In that comparison, Country A's currency will most likely", choices=[
   "depreciate", "appreciate", "hold exactly steady", "be devalued", "leave the market"], ans=1,
   why="Foreign investors must buy A's currency to purchase A's assets, which raises demand for it."),
 dict(q="In that same comparison, Country B's currency will most likely", choices=[
   "appreciate", "depreciate", "stay fixed", "be revalued upward", "be unaffected"], ans=1,
   why="B's residents supply their currency to buy A's assets, which pushes B's currency down."),
 dict(q="An inflow of foreign financial capital into a country will, in that country's loanable funds market,", choices=[
   "shift the demand for loanable funds right and raise the real rate",
   "shift the supply of loanable funds right and lower the real interest rate",
   "shift the supply of loanable funds left and raise the real rate",
   "have no effect",
   "shift both curves right equally"], ans=1,
   why="Foreign savings add to the pool of funds available to domestic borrowers."),
 dict(q="An outflow of financial capital from a country will, in its loanable funds market,", choices=[
   "increase supply and lower the real rate",
   "decrease supply and raise the real interest rate",
   "increase demand and lower the real rate",
   "decrease demand and lower the real rate",
   "leave the market unchanged"], ans=1,
   why="Funds leaving the country shrink the domestic supply of loanable funds."),
 dict(q="In an open economy's loanable funds market, the demand for loanable funds comes from", choices=[
   "households saving",
   "borrowers such as firms financing investment and governments financing deficits",
   "the central bank alone",
   "foreign exporters",
   "workers seeking employment"], ans=1,
   why="Demand for funds is demand to borrow."),
 dict(q="In an open economy's loanable funds market, the supply of loanable funds comes from", choices=[
   "firms borrowing for investment",
   "national saving plus inflows of foreign financial capital",
   "government deficits",
   "the demand for money",
   "imports of goods"], ans=1,
   why="Savers, domestic and foreign, provide the funds."),
 dict(q="Using the table, the equilibrium real interest rate is", table=LF, choices=[
   "2 percent", "3 percent", "4 percent", "5 percent", "6 percent"], ans=2,
   why="At 4 percent the quantity demanded and quantity supplied are both 800 billion."),
 dict(q="Using the table, at a real interest rate of 3 percent there is", table=LF, choices=[
   "a surplus of 200 billion in loanable funds",
   "a shortage of 200 billion in loanable funds",
   "equilibrium",
   "a shortage of 900 billion",
   "a surplus of 700 billion"], ans=1,
   why="Quantity demanded of 900 exceeds quantity supplied of 700 by 200 billion."),
 dict(q="Using the table, at a real interest rate of 5 percent the market pressure is for the real rate to", table=LF, choices=[
   "rise", "fall", "stay put", "become negative", "be set by the central bank"], ans=1,
   why="Quantity supplied of 900 exceeds quantity demanded of 700, and that surplus pushes the rate down."),
 dict(q="An increase in the government budget deficit shifts the demand for loanable funds", choices=[
   "left, lowering the real interest rate",
   "right, raising the real interest rate",
   "not at all",
   "right, lowering the real interest rate",
   "left, raising the real interest rate"], ans=1,
   why="Government borrowing adds to total demand for funds."),
 dict(q="Crowding out occurs when government borrowing raises the real interest rate and thereby reduces", choices=[
   "government spending",
   "private investment spending",
   "taxes",
   "the money supply",
   "the price level"], ans=1,
   why="The higher rate makes some private investment projects unprofitable."),
 dict(q="In an open economy, a rise in the domestic real interest rate caused by government borrowing also causes", choices=[
   "an outflow of financial capital and a weaker currency",
   "an inflow of foreign financial capital and a stronger currency",
   "no change in international capital flows",
   "an increase in net exports",
   "a fall in the exchange rate"], ans=1,
   why="Higher real returns attract foreign savers, who must buy the domestic currency."),
 dict(q="That capital inflow reduces the extent of crowding out because it", choices=[
   "lowers government spending",
   "adds to the supply of loanable funds, limiting the rise in the real interest rate",
   "raises the demand for loanable funds",
   "reduces national saving",
   "raises the price level"], ans=1,
   why="Foreign funds partly satisfy the government's borrowing, holding the rate down."),
 dict(q="Even though the capital inflow limits crowding out of investment, it creates another leakage because the stronger currency", choices=[
   "raises net exports",
   "reduces net exports",
   "raises government revenue",
   "lowers the price level permanently",
   "raises the money supply"], ans=1,
   why="Appreciation makes exports dearer abroad and imports cheaper at home."),
 dict(q="The twin deficits idea holds that a larger government budget deficit tends to be accompanied by", choices=[
   "a larger current account surplus",
   "a larger current account deficit",
   "a balanced current account",
   "a smaller financial account surplus",
   "a fall in the real interest rate"], ans=1,
   why="Higher rates, capital inflow, and a stronger currency shrink net exports."),
 dict(q="A rise in a country's private saving rate will, other things equal,", choices=[
   "raise the real interest rate and attract capital inflow",
   "lower the real interest rate and encourage capital outflow",
   "have no effect on the real rate",
   "raise the demand for loanable funds",
   "appreciate the currency"], ans=1,
   why="More saving increases the supply of loanable funds, and the lower rate sends funds abroad."),
 dict(q="A country whose real interest rate falls below world levels will most likely experience", choices=[
   "a financial account surplus and an appreciating currency",
   "a net outflow of financial capital and a depreciating currency",
   "no change in either account",
   "a rise in foreign purchases of its bonds",
   "an increase in its current account deficit"], ans=1,
   why="Investors move funds where the real return is higher, which means selling the currency."),
 dict(q="An expansionary monetary policy that lowers the real interest rate will cause net capital", choices=[
   "inflow and appreciation",
   "outflow and depreciation",
   "flows to stop entirely",
   "inflow and depreciation",
   "outflow and appreciation"], ans=1,
   why="Lower domestic returns push financial capital abroad, weakening the currency."),
 dict(q="Foreign financial capital flowing into the United States shows up in the U.S. balance of payments as", choices=[
   "a current account credit",
   "a financial account credit",
   "a financial account debit",
   "a current account debit",
   "a capital account debit"], ans=1,
   why="Foreign purchases of U.S. assets are inflows recorded as financial account credits."),
 dict(q="Aside from the real interest rate, which factor most affects where financial capital flows?", choices=[
   "the country's land area",
   "the perceived risk of the country's assets, including political and default risk",
   "the country's number of exports",
   "the age of the country's currency",
   "the size of its labor force"], ans=1,
   why="Investors compare risk-adjusted returns, not raw returns."),
 dict(q="Two countries offer the same real interest rate, but one has a much higher risk of default. Financial capital will flow toward", choices=[
   "the riskier country, because risk means reward",
   "the safer country, because the risk-adjusted return is higher there",
   "neither country",
   "both countries equally",
   "the country with the larger population"], ans=1,
   why="With equal returns, investors prefer the lower-risk destination."),
 dict(q="A country that is a net importer of financial capital must be running", choices=[
   "a current account surplus",
   "a current account deficit",
   "a balanced current account",
   "a budget surplus",
   "a trade surplus in goods"], ans=1,
   why="A financial account surplus is matched by a current account deficit."),
 dict(q="A country that is a net exporter of financial capital must be running", choices=[
   "a current account deficit",
   "a current account surplus",
   "a budget deficit",
   "a balanced budget",
   "a financial account surplus"], ans=1,
   why="Lending abroad on net corresponds to selling more to the world than it buys."),
 dict(q="Which of the following would attract foreign financial capital into a country?", choices=[
   "a fall in its real interest rate",
   "a rise in its real interest rate relative to the rest of the world",
   "an increase in its expected inflation",
   "growing political instability",
   "new restrictions on foreign ownership of its assets"], ans=1,
   why="A higher relative real return is the central draw for mobile financial capital."),
 dict(q="Which of the following would drive financial capital out of a country?", choices=[
   "a rise in its real interest rate",
   "a sharp rise in its expected inflation rate",
   "an improvement in its property rights protections",
   "a fall in its default risk",
   "an expected appreciation of its currency"], ans=1,
   why="Higher expected inflation lowers the expected real return and erodes the currency's value."),
 dict(q="Contractionary fiscal policy that shrinks the budget deficit will, in the loanable funds market,", choices=[
   "shift demand right and raise the real rate",
   "shift demand left and lower the real interest rate",
   "shift supply left and raise the real rate",
   "shift supply right and raise the real rate",
   "leave the market unchanged"], ans=1,
   why="Less government borrowing reduces total demand for loanable funds."),
 dict(q="Following that fall in the real interest rate, the country's currency will", choices=[
   "appreciate as capital flows in",
   "depreciate as financial capital flows out",
   "be unaffected",
   "be revalued",
   "appreciate as net exports fall"], ans=1,
   why="A lower relative real return sends funds abroad, increasing the supply of the currency."),
 dict(q="A country opens its financial markets to foreign investors for the first time. The most likely immediate effects are", choices=[
   "a higher real interest rate and a weaker currency",
   "a lower real interest rate and a stronger currency, as foreign funds arrive",
   "no change in interest rates",
   "a lower real interest rate and a weaker currency",
   "a higher real interest rate and a stronger currency"], ans=1,
   why="Foreign funds add to loanable funds supply while foreign buying of the currency raises its value."),
 dict(q="Higher real interest rates reduce domestic investment because", choices=[
   "firms have less cash on hand",
   "the cost of borrowing to finance capital projects rises, so fewer projects are worth doing",
   "the price level falls",
   "the money supply falls",
   "consumers save less"], ans=1,
   why="Investment demand slopes downward against the real interest rate."),
 dict(q="Why is the real, rather than the nominal, interest rate the relevant one for investment and capital flow decisions?", choices=[
   "because banks quote it",
   "because it measures the purchasing power cost of borrowing and the purchasing power return to lending",
   "because it is always higher",
   "because it never changes",
   "because it is set by the central bank"], ans=1,
   why="Decisions turn on real resources gained or given up, not on the number of currency units."),
 dict(q="If a country's expected inflation rises by 3 percentage points and its nominal interest rate also rises by 3 percentage points, its real interest rate has", choices=[
   "risen by 3 points",
   "stayed the same",
   "fallen by 3 points",
   "fallen by 6 points",
   "become negative"], ans=1,
   why="The nominal rate moved exactly with expected inflation, leaving the real rate unchanged."),
 dict(q="In the case just described, the country's international capital flows would most likely", choices=[
   "surge inward",
   "change little, since the real return is unchanged",
   "stop entirely",
   "reverse direction sharply",
   "double"], ans=1,
   why="Capital responds to real returns, and here the real return did not move."),
 dict(q="An increase in the expected profitability of domestic investment projects will shift the demand for loanable funds", choices=[
   "left, lowering the real rate and causing capital outflow",
   "right, raising the real rate and attracting capital inflow",
   "not at all",
   "right, lowering the real rate",
   "left, raising the real rate"], ans=1,
   why="Firms want to borrow more, which bids up the real interest rate and pulls in foreign funds."),
 dict(q="Which sequence correctly describes deficit-financed government spending in an open economy?", choices=[
   "deficit up, real rate down, capital outflow, currency down, net exports up",
   "deficit up, real rate up, capital inflow, currency up, net exports down",
   "deficit up, real rate up, capital outflow, currency down, net exports up",
   "deficit up, real rate down, capital inflow, currency up, net exports down",
   "deficit up, real rate unchanged, no capital movement"], ans=1,
   why="Each link follows from the higher demand for loanable funds."),
 dict(q="A large, sudden capital flight from an emerging economy will most likely cause its real interest rate to", choices=[
   "fall and its currency to appreciate",
   "rise and its currency to depreciate",
   "fall and its currency to depreciate",
   "rise and its currency to appreciate",
   "stay unchanged"], ans=1,
   why="Losing foreign funds shrinks loanable funds supply and dumps the currency on the market."),
 dict(q="If world real interest rates rise while a small open economy's domestic conditions are unchanged, that economy will experience", choices=[
   "a capital inflow and a stronger currency",
   "a capital outflow and a weaker currency",
   "no change in capital flows",
   "a fall in its own real interest rate",
   "an increase in its net exports with no exchange rate change"], ans=1,
   why="Higher returns elsewhere attract funds away from the small economy."),
 dict(q="Which of the following best explains why a country can invest more than it saves domestically?", choices=[
   "it must print money to cover the gap",
   "it can borrow the difference from abroad, running a financial account surplus",
   "it can raise taxes",
   "investment can never exceed saving",
   "its central bank sets a low interest rate"], ans=1,
   why="Foreign financial capital fills the gap between domestic investment and domestic saving."),
 dict(q="National saving in an open economy equals domestic investment", choices=[
   "always, exactly",
   "plus net capital outflow",
   "minus government spending",
   "plus the price level",
   "divided by the real interest rate"], ans=1,
   why="Saving that is not invested at home is lent abroad."),
 dict(q="A country receiving a large net inflow of foreign financial capital will find that its domestic investment", choices=[
   "exceeds its national saving, with the gap financed by foreign funds",
   "is less than its national saving",
   "equals its national saving exactly",
   "must be zero",
   "is unrelated to its saving"], ans=0,
   why="Borrowed foreign funds let the country invest more than it saves at home."),
 dict(q="A central bank raises its policy rate sharply while inflation expectations stay put. The real interest rate", choices=[
   "falls, and capital leaves the country",
   "rises, and foreign financial capital flows in",
   "stays the same",
   "becomes negative",
   "rises, and capital leaves the country"], ans=1,
   why="With expected inflation fixed, a higher nominal rate is a higher real rate, which attracts funds."),
 dict(q="Which statement about international capital mobility is most accurate?", choices=[
   "financial capital moves instantly and without any barriers everywhere",
   "greater capital mobility makes exchange rates more sensitive to interest rate differences",
   "capital mobility has no relation to exchange rates",
   "capital only moves when currencies are pegged",
   "capital flows are determined only by trade balances"], ans=1,
   why="When funds move freely, small rate gaps produce large flows and large currency movements."),
 dict(q="A government reduces its deficit at the same time that private investment demand surges. The effect on the real interest rate is", choices=[
   "certainly a decrease",
   "indeterminate, because one force lowers demand for loanable funds and the other raises it",
   "certainly an increase",
   "certainly zero",
   "an increase only if saving falls"], ans=1,
   why="The two shifts of loanable funds demand run in opposite directions."),
 dict(q="Foreign investors flee a country's bonds because they fear default, while at the same time domestic saving rises sharply. The effect on the country's real interest rate is", choices=[
   "certainly a rise",
   "indeterminate, because the capital outflow reduces loanable funds supply while higher saving increases it",
   "certainly a fall",
   "zero by definition",
   "a fall only if the currency appreciates"], ans=1,
   why="Both forces move the supply of loanable funds, but in opposite directions."),
]
