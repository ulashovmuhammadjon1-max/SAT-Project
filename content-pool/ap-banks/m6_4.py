# MACRO 6.4 Policy and Economic Conditions in the Foreign Exchange Market — 50 questions
# The chains used throughout, each checked link by link:
#   Expansionary monetary policy: MS up -> nominal and real interest rate down ->
#     financial capital flows out (demand for domestic currency falls, supply of
#     domestic currency rises) -> currency depreciates -> net exports rise.
#   Contractionary monetary policy: MS down -> interest rate up -> capital flows
#     in -> currency appreciates -> net exports fall.
#   Expansionary fiscal policy financed by borrowing: government borrowing raises
#     the demand for loanable funds -> real interest rate up -> capital inflow ->
#     currency appreciates -> net exports fall, which partly offsets the direct
#     increase in aggregate demand (net export crowding out).
#   Contractionary fiscal policy: borrowing falls -> real interest rate down ->
#     capital outflow -> currency depreciates -> net exports rise, partly
#     offsetting the contraction.
TOPIC = ("6.4", "Policy and Economic Conditions in the Foreign Exchange Market", 6)

QUESTIONS = [
 dict(q="Expansionary monetary policy in the United States lowers U.S. interest rates. In the foreign exchange market this will", choices=[
   "increase demand for dollars and appreciate the dollar",
   "reduce demand for dollars and depreciate the dollar",
   "leave the dollar's value unchanged",
   "raise the dollar's value and reduce net exports",
   "reduce the supply of dollars"], ans=1,
   why="Lower U.S. returns make dollar assets less attractive, so foreigners demand fewer dollars."),
 dict(q="Contractionary monetary policy in the United States raises U.S. interest rates, which will cause the dollar to", choices=[
   "depreciate and net exports to rise",
   "appreciate and net exports to fall",
   "depreciate and net exports to fall",
   "appreciate and net exports to rise",
   "be unaffected"], ans=1,
   why="Higher returns attract foreign financial capital, and a stronger dollar makes U.S. goods dearer abroad."),
 dict(q="The Federal Reserve buys government bonds on the open market. The likely effect on the dollar is", choices=[
   "appreciation, because bond prices rise",
   "depreciation, because the interest rate falls and financial capital leaves",
   "no change, because open market operations are domestic",
   "appreciation, because the money supply falls",
   "depreciation, because U.S. exports fall"], ans=1,
   why="An open market purchase is expansionary, lowering the interest rate and weakening the dollar."),
 dict(q="The Federal Reserve sells government bonds on the open market. In the foreign exchange market this will", choices=[
   "increase the supply of dollars and depreciate the dollar",
   "increase the demand for dollars and appreciate the dollar",
   "decrease the demand for dollars and depreciate the dollar",
   "have no effect on the exchange rate",
   "raise net exports"], ans=1,
   why="Selling bonds drains reserves and raises the interest rate, attracting foreign financial capital."),
 dict(q="An increase in the U.S. money supply affects net exports through which chain?", choices=[
   "money supply up, interest rate up, dollar up, net exports down",
   "money supply up, interest rate down, dollar down, net exports up",
   "money supply up, interest rate down, dollar up, net exports up",
   "money supply up, price level down, dollar down, net exports down",
   "money supply up, interest rate down, dollar down, net exports down"], ans=1,
   why="A lower interest rate weakens the currency, and a weaker currency raises net exports."),
 dict(q="Expansionary monetary policy raises aggregate demand through", choices=[
   "only the investment channel",
   "both higher domestic investment and higher net exports from a weaker currency",
   "only higher net exports",
   "higher taxes",
   "a stronger currency"], ans=1,
   why="Lower interest rates raise interest-sensitive spending and, through depreciation, net exports as well."),
 dict(q="A government finances a large increase in spending by borrowing. The effect on the real interest rate and the currency is", choices=[
   "the real interest rate falls and the currency depreciates",
   "the real interest rate rises and the currency appreciates",
   "the real interest rate rises and the currency depreciates",
   "the real interest rate falls and the currency appreciates",
   "neither changes"], ans=1,
   why="Government borrowing raises demand for loanable funds and the higher rate attracts foreign financial capital."),
 dict(q="The appreciation caused by deficit-financed government spending will", choices=[
   "reinforce the increase in aggregate demand",
   "partly offset the increase in aggregate demand by reducing net exports",
   "have no effect on aggregate demand",
   "eliminate the budget deficit",
   "reduce the domestic price level to its original value"], ans=1,
   why="A stronger currency lowers net exports, which is net export crowding out."),
 dict(q="Net export crowding out refers to the fact that expansionary fiscal policy", choices=[
   "reduces government spending automatically",
   "raises interest rates, attracts capital inflows, appreciates the currency, and reduces net exports",
   "lowers interest rates and increases exports",
   "always increases the trade surplus",
   "makes monetary policy ineffective"], ans=1,
   why="The exchange rate channel drains part of the stimulus away through the trade balance."),
 dict(q="Contractionary fiscal policy, such as a cut in government spending financed by less borrowing, will most likely", choices=[
   "raise the real interest rate and appreciate the currency",
   "lower the real interest rate, depreciate the currency, and raise net exports",
   "lower the real interest rate and reduce net exports",
   "raise the real interest rate and raise net exports",
   "leave interest rates and the exchange rate unchanged"], ans=1,
   why="Less government borrowing lowers the real rate, capital leaves, and the weaker currency lifts net exports."),
 dict(q="An increase in a country's budget deficit will most likely move its current account", choices=[
   "toward surplus",
   "toward deficit, as the currency appreciates and net exports fall",
   "to exactly zero",
   "toward surplus, as interest rates fall",
   "in a direction unrelated to the exchange rate"], ans=1,
   why="The twin-deficit chain runs through higher interest rates and a stronger currency."),
 dict(q="Which policy combination would most strongly appreciate a country's currency?", choices=[
   "expansionary monetary policy and expansionary fiscal policy",
   "contractionary monetary policy and expansionary deficit-financed fiscal policy",
   "expansionary monetary policy and contractionary fiscal policy",
   "contractionary monetary policy and contractionary fiscal policy",
   "no policy change at all"], ans=1,
   why="Both raise the real interest rate, which draws in foreign financial capital."),
 dict(q="Which policy combination would most strongly depreciate a country's currency?", choices=[
   "contractionary monetary policy and contractionary fiscal policy",
   "expansionary monetary policy and contractionary fiscal policy",
   "contractionary monetary policy and expansionary fiscal policy",
   "expansionary monetary policy and expansionary fiscal policy",
   "a rise in the required reserve ratio"], ans=1,
   why="Both push the real interest rate down, sending financial capital abroad."),
 dict(q="A central bank that wants to weaken its currency through direct intervention would", choices=[
   "buy its own currency with foreign reserves",
   "sell its own currency and buy foreign currency assets",
   "raise the discount rate",
   "sell government bonds domestically",
   "raise reserve requirements"], ans=1,
   why="Selling its own currency increases the currency's supply on the market."),
 dict(q="A central bank that wants to strengthen its currency through direct intervention would", choices=[
   "sell its own currency for foreign currency",
   "use foreign exchange reserves to buy its own currency",
   "lower the policy interest rate",
   "buy government bonds on the open market",
   "increase the money supply"], ans=1,
   why="Buying its own currency raises demand for it in the foreign exchange market."),
 dict(q="A country with a fixed exchange rate that faces persistent downward market pressure on its currency will", choices=[
   "accumulate foreign reserves indefinitely",
   "lose foreign reserves as it buys its own currency to defend the peg",
   "automatically move to a floating rate",
   "see its currency appreciate",
   "experience no reserve change"], ans=1,
   why="Defending an overvalued peg requires spending reserves buying the currency."),
 dict(q="Under a fixed exchange rate regime, a central bank's ability to pursue an independent monetary policy is", choices=[
   "unaffected",
   "limited, because interest rates must be set to keep the exchange rate at its peg",
   "expanded, because it controls the exchange rate",
   "irrelevant, because fiscal policy alone matters",
   "guaranteed by the size of its reserves"], ans=1,
   why="Defending a peg ties monetary policy to the exchange rate rather than domestic goals."),
 dict(q="Under a floating exchange rate regime, a balance of payments imbalance tends to be corrected by", choices=[
   "changes in official reserves",
   "movements in the exchange rate itself",
   "government-imposed quotas",
   "changes in the required reserve ratio",
   "an international agreement"], ans=1,
   why="A floating rate adjusts until the currency market clears."),
 dict(q="A country that pegs its currency below its market value in order to boost exports will over time", choices=[
   "run out of foreign reserves",
   "accumulate large foreign exchange reserves",
   "see its exports fall",
   "have to appreciate immediately",
   "eliminate its trade surplus"], ans=1,
   why="Selling its own currency to hold the undervalued peg means buying foreign assets."),
 dict(q="Which is the strongest argument for a fixed exchange rate?", choices=[
   "it lets monetary policy target domestic unemployment freely",
   "it reduces exchange rate uncertainty for traders and investors",
   "it guarantees a trade surplus",
   "it eliminates the need for foreign reserves",
   "it makes fiscal policy more powerful at home"], ans=1,
   why="Predictable rates lower the risk in international trade and investment contracts."),
 dict(q="Which is the strongest argument for a floating exchange rate?", choices=[
   "it removes all exchange rate risk",
   "it lets monetary policy respond to domestic conditions rather than defend a peg",
   "it guarantees balanced trade every year",
   "it eliminates inflation",
   "it prevents speculation entirely"], ans=1,
   why="A floating rate frees the central bank to target output and inflation at home."),
 dict(q="A recession abroad in a country's major trading partners will, for the home country,", choices=[
   "raise demand for the home currency and appreciate it",
   "reduce demand for the home currency and depreciate it, as exports fall",
   "raise net exports",
   "leave the exchange rate unchanged",
   "raise the home interest rate"], ans=1,
   why="Foreign buyers with lower incomes purchase fewer of the home country's exports and so need less of its currency."),
 dict(q="A domestic economic boom that raises incomes at home will most likely", choices=[
   "appreciate the domestic currency as imports fall",
   "depreciate the domestic currency as imports and the supply of domestic currency rise",
   "leave the currency unchanged",
   "increase net exports",
   "reduce the demand for foreign currency"], ans=1,
   why="Higher domestic income raises import demand, and paying for imports supplies domestic currency."),
 dict(q="A rise in a country's expected inflation rate relative to its trading partners will most likely cause its currency to", choices=[
   "appreciate", "depreciate", "hold its value exactly", "be revalued upward", "become fixed"], ans=1,
   why="Expected loss of purchasing power reduces demand for the currency and increases its supply."),
 dict(q="A country succeeds in reducing its inflation rate well below its trading partners'. Its currency will most likely", choices=[
   "depreciate", "appreciate", "be unaffected", "have to be devalued", "leave the foreign exchange market"], ans=1,
   why="Lower inflation preserves the currency's purchasing power relative to others."),
 dict(q="Political instability in a country typically causes its currency to", choices=[
   "appreciate as investors seek higher risk",
   "depreciate as financial capital flees to safer countries",
   "hold steady",
   "be revalued by the central bank",
   "rise in real but not nominal terms"], ans=1,
   why="Capital flight means investors sell the currency to move funds elsewhere."),
 dict(q="A country's currency is described as a 'safe haven.' During a global crisis its value will most likely", choices=[
   "fall sharply", "rise as investors move funds into its assets", "stay exactly constant", "be devalued", "become worthless"], ans=1,
   why="Crisis-driven demand for its assets raises demand for the currency."),
 dict(q="If a central bank raises the discount rate and increases reserve requirements at the same time, the domestic currency will most likely", choices=[
   "depreciate", "appreciate", "be unaffected", "become fixed", "fall in real terms only"], ans=1,
   why="Both actions are contractionary, raising interest rates and attracting foreign financial capital."),
 dict(q="Expansionary monetary policy at home while a trading partner leaves policy unchanged will cause the home currency to depreciate and the home country's real GDP to", choices=[
   "fall", "rise, helped by both investment and net exports", "stay the same", "rise only if taxes are cut", "fall in the short run and rise in the long run"], ans=1,
   why="Lower rates raise interest-sensitive spending, and the weaker currency adds net exports."),
 dict(q="If two countries pursue identical expansionary monetary policies at the same time, the bilateral exchange rate between them will most likely", choices=[
   "move sharply in favor of the first country",
   "change little, because both interest rates fall together",
   "be fixed automatically",
   "move sharply in favor of the second country",
   "become undefined"], ans=1,
   why="Exchange rates respond to interest rate differentials, and here the differential barely changes."),
 dict(q="Sterilized intervention means a central bank", choices=[
   "intervenes in the foreign exchange market and offsets the effect on the domestic money supply with an open market operation",
   "never intervenes",
   "abandons its peg",
   "intervenes only in the bond market",
   "raises tariffs instead of intervening"], ans=0,
   why="Sterilization neutralizes the domestic monetary consequences of the currency operation."),
 dict(q="A central bank buys foreign currency with newly created domestic currency and does not sterilize. The domestic money supply will", choices=[
   "fall", "rise", "stay the same", "become fixed", "fall then rise by the same amount"], ans=1,
   why="Creating domestic currency to buy foreign assets injects money into the domestic economy."),
 dict(q="Suppose a country raises its real interest rate to defend a currency peg while it is in a recession. The likely domestic cost is", choices=[
   "higher inflation",
   "deeper recession, because higher rates reduce investment and consumption",
   "a larger money supply",
   "a weaker currency",
   "an immediate trade deficit"], ans=1,
   why="Defending the peg forces contractionary policy exactly when expansion is needed."),
 dict(q="A rise in foreign demand for a country's government bonds will cause the country's currency to appreciate and its net exports to", choices=[
   "rise", "fall", "stay the same", "become zero", "rise then fall by the same amount"], ans=1,
   why="A stronger currency makes exports dearer abroad and imports cheaper at home."),
 dict(q="If the U.S. Federal Reserve raises interest rates while the European Central Bank cuts rates, the dollar will", choices=[
   "depreciate against the euro",
   "appreciate against the euro",
   "not change against the euro",
   "be devalued",
   "appreciate only if U.S. inflation also rises"], ans=1,
   why="The interest rate differential moves in the dollar's favor, drawing financial capital into dollar assets."),
 dict(q="A country imposes capital controls that make it hard for foreigners to buy its financial assets. The immediate effect on its currency is", choices=[
   "appreciation from reduced supply",
   "depreciation from reduced foreign demand for the currency",
   "no effect",
   "an automatic devaluation",
   "a rise in the real interest rate abroad"], ans=1,
   why="Blocking asset purchases removes a source of demand for the currency."),
 dict(q="Which of the following would tend to cause a currency to appreciate?", choices=[
   "a fall in domestic real interest rates",
   "a rise in foreign demand for domestic exports",
   "a rise in domestic inflation",
   "an increase in domestic incomes",
   "political turmoil at home"], ans=1,
   why="Foreign buyers must acquire the currency to pay for the exports."),
 dict(q="Which of the following would tend to cause a currency to depreciate?", choices=[
   "a rise in domestic real interest rates",
   "expansionary monetary policy at home",
   "a fall in domestic inflation",
   "an increase in foreign demand for domestic bonds",
   "an increase in the country's exports"], ans=1,
   why="Expansionary money policy lowers the domestic interest rate and sends financial capital abroad."),
 dict(q="A country running an expansionary fiscal policy and a contractionary monetary policy at once should expect", choices=[
   "a sharply weaker currency",
   "a sharply stronger currency and a fall in net exports",
   "no exchange rate movement",
   "a rise in net exports",
   "an immediate current account surplus"], ans=1,
   why="Both policies raise the real interest rate, which appreciates the currency and hurts net exports."),
 dict(q="In an open economy, monetary policy is generally more powerful than in a closed economy because", choices=[
   "the interest rate effect on investment disappears",
   "the exchange rate channel adds to the effect on aggregate demand in the same direction",
   "the money multiplier is larger",
   "fiscal policy has no effect",
   "prices are fully flexible"], ans=1,
   why="Depreciation raises net exports at the same time lower rates raise investment."),
 dict(q="In an open economy, deficit-financed fiscal policy is generally less powerful than in a closed economy because", choices=[
   "the government spending multiplier is zero",
   "some of the stimulus leaks away as a stronger currency reduces net exports",
   "taxes automatically rise to offset it",
   "the money supply must fall",
   "interest rates cannot change"], ans=1,
   why="Net export crowding out subtracts from the direct increase in aggregate demand."),
 dict(q="A country's central bank sells large amounts of foreign reserves to defend its currency. If the intervention is not sterilized, the domestic money supply will", choices=[
   "rise, raising inflation",
   "fall, raising domestic interest rates",
   "remain unchanged",
   "double",
   "fall only if the peg is abandoned"], ans=1,
   why="Buying its own currency with reserves removes domestic money from circulation."),
 dict(q="If markets expect a pegged currency to be devalued soon, speculators will", choices=[
   "buy the currency heavily, defending the peg",
   "sell the currency heavily, draining the central bank's reserves faster",
   "ignore the expectation",
   "buy the country's exports",
   "lend to the central bank at low rates"], ans=1,
   why="Expected devaluation gives speculators a reason to unload the currency, which accelerates the crisis."),
 dict(q="A country announces a credible plan to reduce its budget deficit sharply. The likely short-run effect on its currency is", choices=[
   "appreciation as interest rates rise",
   "depreciation as the real interest rate falls and financial capital leaves",
   "no change",
   "immediate devaluation",
   "a rise in net exports with no exchange rate change"], ans=1,
   why="Less government borrowing lowers the real interest rate and reduces the capital inflow."),
 dict(q="Expansionary monetary policy causes a depreciation. The effect on the domestic price level is", choices=[
   "downward pressure, because import prices fall",
   "upward pressure, because both aggregate demand and import prices rise",
   "no effect",
   "downward pressure, because net exports fall",
   "upward pressure only if the currency is fixed"], ans=1,
   why="A weaker currency raises the domestic price of imports on top of the demand-side effect."),
 dict(q="A central bank targeting a stable exchange rate under a peg while its trading partner raises interest rates must", choices=[
   "cut its own interest rate",
   "raise its own interest rate to keep capital from leaving",
   "do nothing at all",
   "abandon the peg immediately",
   "impose export subsidies"], ans=1,
   why="Matching the partner's rate keeps the interest differential and the capital flow stable."),
 dict(q="Which statement about central bank intervention is most accurate?", choices=[
   "it can move an exchange rate permanently regardless of market forces",
   "it can influence an exchange rate, but its power is limited by the size of the reserves it can spend",
   "it always requires an act of the legislature",
   "it has no effect on the money supply under any circumstances",
   "it is only possible under a floating regime"], ans=1,
   why="A central bank can only buy its own currency while it still has foreign reserves to spend."),
 dict(q="A managed float is an arrangement in which", choices=[
   "the exchange rate is rigidly fixed by law",
   "the rate is mostly market determined but the central bank intervenes at times to smooth movements",
   "the rate is set by an international treaty each year",
   "capital flows are banned",
   "the currency is tied to gold"], ans=1,
   why="Managed floating combines market determination with occasional official intervention."),
 dict(q="A country experiencing both a recession and a currency it wants to keep strong faces a policy conflict because", choices=[
   "expansionary policy raises the interest rate",
   "the expansionary policy needed for output lowers interest rates and weakens the currency",
   "contractionary policy raises output",
   "exchange rates do not respond to interest rates",
   "fiscal policy cannot affect output"], ans=1,
   why="The two goals require the interest rate to move in opposite directions."),
 dict(q="If a country's real interest rate is unchanged but its trading partners all cut their real rates, that country's currency will", choices=[
   "depreciate", "appreciate", "hold exactly steady", "be devalued", "become fixed"], ans=1,
   why="What matters is the differential, and it has moved in the country's favor."),
]
