# MACRO 6.5 Changes in the Foreign Exchange Market and Net Exports — 50 questions
# The full chain, each direction verified link by link:
#   Depreciation of the domestic currency
#     -> foreign-currency price of exports falls, so exports rise
#     -> domestic-currency price of imports rises, so imports fall
#     -> net exports (X - M) rise
#     -> aggregate demand shifts right
#     -> in the short run real GDP rises, the price level rises, unemployment falls.
#   Appreciation reverses every link: exports fall, imports rise, net exports fall,
#     AD shifts left, real GDP and the price level fall, unemployment rises.
#   Offsetting case: deficit-financed government spending raises AD directly but
#     raises the real interest rate, appreciates the currency, and lowers net
#     exports, so the net rightward shift of AD is smaller than the direct effect.
#   Numeric check: exports 260, imports 300 => net exports -40. If depreciation
#     raises exports to 300 and cuts imports to 280, net exports = +20, a change
#     of +60. With a spending multiplier of 4 that is a 240 increase in AD.
TOPIC = ("6.5", "Changes in the Foreign Exchange Market and Net Exports", 6)

QUESTIONS = [
 dict(q="A depreciation of the domestic currency causes exports to", choices=[
   "fall, because they cost more abroad",
   "rise, because they cost less in foreign currency",
   "stay the same",
   "fall, because imports get cheaper",
   "rise, but only if tariffs fall too"], ans=1,
   why="Foreign buyers need less of their own currency to buy each unit of the country's goods."),
 dict(q="A depreciation of the domestic currency causes imports to", choices=[
   "rise, because they get cheaper",
   "fall, because they cost more in domestic currency",
   "stay the same",
   "rise, because exports rise",
   "fall, because the price level falls"], ans=1,
   why="It takes more domestic currency to buy the foreign currency needed to pay for imports."),
 dict(q="A depreciation of the domestic currency causes net exports to", choices=[
   "fall", "rise", "stay unchanged", "become zero", "rise only under a fixed exchange rate"], ans=1,
   why="Exports rise and imports fall, so exports minus imports increases."),
 dict(q="An appreciation of the domestic currency causes net exports to", choices=[
   "rise", "fall", "stay unchanged", "become exactly zero", "fall only in the long run"], ans=1,
   why="A stronger currency makes exports dearer abroad and imports cheaper at home."),
 dict(q="An increase in net exports shifts the aggregate demand curve", choices=[
   "left", "right", "not at all", "vertically only", "down along itself"], ans=1,
   why="Net exports is a component of aggregate demand."),
 dict(q="A currency depreciation therefore shifts aggregate demand", choices=[
   "left, lowering real GDP",
   "right, raising real GDP and the price level in the short run",
   "not at all",
   "right, lowering the price level",
   "left, raising the price level"], ans=1,
   why="Higher net exports add to aggregate demand, raising output and prices in the short run."),
 dict(q="A currency appreciation shifts aggregate demand", choices=[
   "right, raising output",
   "left, lowering real GDP and the price level in the short run",
   "not at all",
   "left, raising the price level",
   "right, lowering unemployment"], ans=1,
   why="Lower net exports subtract from aggregate demand."),
 dict(q="Following a depreciation, short-run unemployment in the domestic economy will most likely", choices=[
   "rise", "fall", "stay the same", "rise then stay high", "be unaffected by net exports"], ans=1,
   why="Higher aggregate demand raises output and employment in the short run."),
 dict(q="Following an appreciation, short-run unemployment in the domestic economy will most likely", choices=[
   "fall", "rise", "stay the same", "fall then rise back", "be unaffected"], ans=1,
   why="Lower net exports reduce aggregate demand and output, so employment falls."),
 dict(q="A country's exports are 260 billion and its imports are 300 billion. Net exports are", choices=[
   "-560 billion", "-40 billion", "0", "+40 billion", "+560 billion"], ans=1,
   why="260 minus 300 equals -40 billion."),
 dict(q="After a depreciation, that same country's exports rise to 300 billion and imports fall to 280 billion. Net exports are now", choices=[
   "-40 billion", "-20 billion", "0", "+20 billion", "+580 billion"], ans=3,
   why="300 minus 280 equals +20 billion."),
 dict(q="In that example, the change in net exports caused by the depreciation is", choices=[
   "+20 billion", "+40 billion", "+50 billion", "+60 billion", "+580 billion"], ans=3,
   why="Net exports moved from -40 to +20, a change of 60 billion."),
 dict(q="If the spending multiplier is 4 and net exports rise by 60 billion, the resulting change in aggregate demand is", choices=[
   "15 billion", "60 billion", "120 billion", "180 billion", "240 billion"], ans=4,
   why="60 times a multiplier of 4 equals 240 billion."),
 dict(q="Which sequence correctly describes the effect of an appreciation of the dollar?", choices=[
   "dollar up, exports up, net exports up, aggregate demand right",
   "dollar up, exports down and imports up, net exports down, aggregate demand left",
   "dollar up, imports down, net exports up, real GDP up",
   "dollar up, price level up, real GDP up",
   "dollar up, net exports unchanged, real GDP unchanged"], ans=1,
   why="A stronger dollar hurts exports, helps imports, and lowers net exports and aggregate demand."),
 dict(q="Expansionary monetary policy raises real GDP through two channels. The net export channel works because lower interest rates", choices=[
   "appreciate the currency and raise exports",
   "depreciate the currency, which raises net exports",
   "raise the price level directly",
   "reduce imports through tariffs",
   "raise foreign incomes"], ans=1,
   why="Capital flows out, the currency weakens, and a weaker currency raises net exports."),
 dict(q="Contractionary monetary policy reduces real GDP partly because higher interest rates", choices=[
   "depreciate the currency and reduce exports",
   "appreciate the currency, which reduces net exports",
   "reduce the price of imports and raise net exports",
   "raise foreign demand for exports",
   "increase government spending"], ans=1,
   why="Capital flows in, the currency strengthens, and a stronger currency lowers net exports."),
 dict(q="Deficit-financed government spending raises aggregate demand directly, but the effect is partly offset because", choices=[
   "the currency depreciates and net exports fall",
   "higher interest rates appreciate the currency, so net exports fall",
   "the money supply falls automatically",
   "taxes rise by the same amount",
   "imports become more expensive"], ans=1,
   why="Net export crowding out subtracts from the direct fiscal stimulus."),
 dict(q="The net rightward shift of aggregate demand from deficit-financed fiscal expansion in an open economy is", choices=[
   "larger than in a closed economy",
   "smaller than in a closed economy",
   "exactly the same as in a closed economy",
   "always zero",
   "always negative"], ans=1,
   why="Part of the stimulus leaks abroad as net exports fall with the stronger currency."),
 dict(q="Contractionary fiscal policy in an open economy is partly offset because lower interest rates", choices=[
   "appreciate the currency and lower net exports",
   "depreciate the currency, which raises net exports and partly cushions the contraction",
   "raise the price level",
   "raise government spending automatically",
   "reduce exports"], ans=1,
   why="The exchange rate channel works against the domestic contraction."),
 dict(q="A recession in a country's major trading partners will most likely cause the country's", choices=[
   "exports and net exports to rise",
   "exports to fall, net exports to fall, and aggregate demand to shift left",
   "imports to fall enough to raise net exports",
   "currency to appreciate strongly",
   "real GDP to rise"], ans=1,
   why="Weaker foreign income means fewer of the country's exports are bought."),
 dict(q="A boom among a country's trading partners will most likely cause the country's aggregate demand to", choices=[
   "shift left as exports fall",
   "shift right as exports and net exports rise",
   "stay put",
   "shift left as its currency appreciates",
   "become vertical"], ans=1,
   why="Richer foreign buyers purchase more of the country's exports."),
 dict(q="An increase in domestic income, holding foreign income constant, will cause net exports to", choices=[
   "rise, because exports rise",
   "fall, because imports rise",
   "stay unchanged",
   "become zero",
   "rise, because the currency appreciates"], ans=1,
   why="Higher domestic income raises spending on imports while exports depend on foreign income."),
 dict(q="A country's currency depreciates and its short-run aggregate supply is unchanged. In the short run the domestic price level will", choices=[
   "fall", "rise", "stay constant", "fall then rise to the original level", "be unaffected by net exports"], ans=1,
   why="A rightward shift of aggregate demand along an upward-sloping short-run aggregate supply curve raises prices."),
 dict(q="A currency depreciation contributes to inflation through two routes: higher aggregate demand and", choices=[
   "lower wages",
   "a higher domestic price of imported goods and inputs",
   "a lower price of exports at home",
   "a smaller money supply",
   "a decrease in government spending"], ans=1,
   why="Imported goods and imported inputs cost more in domestic currency, which is a cost-push effect."),
 dict(q="If a country imports most of its oil, a sharp depreciation of its currency will most likely shift its short-run aggregate supply curve", choices=[
   "right, lowering prices",
   "left, because imported input costs rise",
   "not at all",
   "right, because net exports rise",
   "left, lowering the price level"], ans=1,
   why="Dearer imported inputs raise production costs across the economy."),
 dict(q="An appreciation of the domestic currency helps domestic consumers most directly by", choices=[
   "raising the price of exports",
   "lowering the domestic price of imported goods",
   "raising domestic wages",
   "raising net exports",
   "lowering the interest rate"], ans=1,
   why="A stronger currency buys more foreign goods per unit."),
 dict(q="An appreciation of the domestic currency hurts which group most directly?", choices=[
   "domestic consumers of imports",
   "domestic exporters and firms competing with imports",
   "foreign consumers of the country's goods",
   "domestic tourists traveling abroad",
   "domestic firms buying foreign inputs"], ans=1,
   why="Exporters see foreign-currency prices rise and import-competing firms face cheaper foreign rivals."),
 dict(q="Which of the following would raise a country's net exports?", choices=[
   "an appreciation of its currency",
   "a depreciation of its currency",
   "a rise in domestic incomes",
   "a recession abroad",
   "a rise in domestic interest rates"], ans=1,
   why="Depreciation makes exports cheaper abroad and imports dearer at home."),
 dict(q="Which of the following would lower a country's net exports?", choices=[
   "a depreciation of its currency",
   "a recession among its trading partners",
   "a boom abroad",
   "a fall in domestic incomes",
   "a fall in domestic interest rates"], ans=1,
   why="Lower foreign incomes reduce purchases of the country's exports."),
 dict(q="A country experiencing a recessionary gap would benefit most from", choices=[
   "an appreciation of its currency",
   "a depreciation of its currency, which raises net exports and aggregate demand",
   "higher domestic interest rates",
   "a recession abroad",
   "a rise in the domestic price of exports"], ans=1,
   why="More net exports shift aggregate demand toward full employment output."),
 dict(q="A country with an inflationary gap could reduce inflationary pressure through", choices=[
   "a depreciation of its currency",
   "an appreciation of its currency, which lowers net exports and aggregate demand",
   "a boom in trading partners' economies",
   "an increase in export subsidies",
   "a cut in domestic interest rates"], ans=1,
   why="A stronger currency pulls aggregate demand back and also lowers import prices."),
 dict(q="The Federal Reserve raises interest rates to fight inflation. The net export channel", choices=[
   "works against the policy, because net exports rise",
   "reinforces the policy, because the dollar appreciates and net exports fall",
   "has no bearing on the policy",
   "reverses the policy entirely",
   "operates only under a fixed exchange rate"], ans=1,
   why="Both the investment and net export channels push aggregate demand in the same, contractionary direction."),
 dict(q="Congress passes a large deficit-financed infrastructure program. The exchange rate channel", choices=[
   "reinforces the program's effect on output",
   "works against it, because a stronger currency reduces net exports",
   "has no effect on output",
   "makes the multiplier larger",
   "lowers the real interest rate"], ans=1,
   why="Higher interest rates appreciate the currency and crowd out net exports."),
 dict(q="A country's currency depreciates 20 percent but its net exports barely move in the first few months. The most likely explanation is that", choices=[
   "exchange rates do not affect trade",
   "trade contracts and buying habits take time to adjust, so quantities respond with a lag",
   "the currency actually appreciated",
   "the country has no trading partners",
   "the price level fell by 20 percent at the same time"], ans=1,
   why="Trade volumes are slow to adjust, so the quantity response to a price change takes time."),
 dict(q="If a depreciation raises the domestic-currency cost of imports before import quantities fall, the trade balance in the very short run may", choices=[
   "improve immediately by a large amount",
   "worsen before it improves",
   "stay exactly the same forever",
   "become permanently negative",
   "have no relation to the exchange rate"], ans=1,
   why="The price effect hits first and the quantity effect arrives with a lag."),
 dict(q="A currency depreciation raises real GDP in the short run. In the long run, if the economy returns to full employment, the main lasting effect is on", choices=[
   "real output, which stays permanently higher",
   "the price level, which is permanently higher",
   "the unemployment rate, which stays permanently lower",
   "the natural rate of unemployment",
   "nothing at all"], ans=1,
   why="Aggregate demand increases raise output only temporarily; the long-run effect is on prices."),
 dict(q="Which of the following pairs of effects follows from a domestic currency appreciation?", choices=[
   "exports up and imports down",
   "exports down and imports up",
   "exports up and imports up",
   "exports down and imports down",
   "no change in either"], ans=1,
   why="A stronger currency makes domestic goods dearer abroad and foreign goods cheaper at home."),
 dict(q="A U.S. steel producer competing against imported steel benefits most from", choices=[
   "a stronger dollar",
   "a weaker dollar, which raises the dollar price of imported steel",
   "lower foreign incomes",
   "higher U.S. interest rates",
   "a fall in U.S. exports"], ans=1,
   why="Depreciation makes the imported competitor more expensive in dollars."),
 dict(q="An increase in foreign demand for a country's exports affects the country twice: aggregate demand shifts right and", choices=[
   "the currency depreciates, adding further to net exports",
   "the currency appreciates, which partly offsets the rise in net exports",
   "the currency is unaffected",
   "the price level falls",
   "the interest rate falls"], ans=1,
   why="Foreign buyers must buy the currency, which strengthens it and partly reverses the export gain."),
 dict(q="If a country's currency depreciates and, at the same time, its trading partners enter a recession, the effect on its net exports is", choices=[
   "certainly positive",
   "indeterminate, because the two forces push in opposite directions",
   "certainly negative",
   "certainly zero",
   "positive only if its interest rate rises"], ans=1,
   why="Depreciation raises net exports while a foreign recession lowers them."),
 dict(q="If a country's currency appreciates while foreign incomes boom, the effect on its exports is", choices=[
   "certainly a decrease",
   "indeterminate, since the appreciation lowers exports and the foreign boom raises them",
   "certainly an increase",
   "zero by definition",
   "an increase only if domestic income falls"], ans=1,
   why="The two forces work against each other, so the net effect depends on their sizes."),
 dict(q="Net exports enter aggregate demand as", choices=[
   "exports plus imports",
   "exports minus imports",
   "imports minus exports",
   "exports divided by imports",
   "government spending plus exports"], ans=1,
   why="Imports are subtracted because they are spending on foreign, not domestic, output."),
 dict(q="A rise in a country's imports with exports unchanged will, other things equal, shift aggregate demand", choices=[
   "right, since more goods are available",
   "left, because net exports fall",
   "not at all",
   "right, because the currency depreciates",
   "vertically"], ans=1,
   why="Spending directed at foreign output reduces demand for domestic output."),
 dict(q="Which statement about the exchange rate and real GDP is correct?", choices=[
   "a stronger currency raises real GDP in the short run",
   "a weaker currency raises real GDP in the short run by raising net exports",
   "the exchange rate has no effect on real GDP",
   "a weaker currency lowers real GDP because imports cost more",
   "only fiscal policy can change real GDP"], ans=1,
   why="Depreciation raises net exports, a component of aggregate demand."),
 dict(q="A central bank deliberately weakens its currency to boost exports. A likely cost of this policy is", choices=[
   "a fall in domestic employment",
   "higher inflation, both from stronger aggregate demand and from dearer imports",
   "a permanent decrease in the price level",
   "a fall in net exports",
   "an immediate appreciation"], ans=1,
   why="Depreciation adds demand-pull and cost-push pressure at the same time."),
 dict(q="Which chain correctly links contractionary monetary policy to net exports?", choices=[
   "money supply down, interest rate down, currency down, net exports up",
   "money supply down, interest rate up, currency up, net exports down",
   "money supply down, interest rate up, currency down, net exports up",
   "money supply down, price level up, currency up, net exports up",
   "money supply down, interest rate up, currency up, net exports up"], ans=1,
   why="Tighter money raises the interest rate, strengthens the currency, and reduces net exports."),
 dict(q="Two countries have equal inflation, but one lets its currency depreciate steadily. That country will most likely experience", choices=[
   "a steadily worsening trade balance",
   "an improving trade balance and stronger export industries",
   "no change in trade at all",
   "a permanently lower price level",
   "a decrease in aggregate demand"], ans=1,
   why="Steady depreciation makes its goods progressively cheaper relative to its partner's."),
 dict(q="Suppose a large capital inflow appreciates a country's currency. The effect on its current account is", choices=[
   "a move toward surplus as net exports rise",
   "a move toward deficit as net exports fall",
   "no change",
   "an immediate balance of zero",
   "a rise in exports and a fall in imports"], ans=1,
   why="The financial account surplus is mirrored by a weaker current account through the stronger currency."),
 dict(q="Which is the most complete statement of the effect of a depreciation on the domestic economy in the short run?", choices=[
   "net exports rise only",
   "net exports rise, aggregate demand shifts right, real GDP and the price level rise, and unemployment falls",
   "the price level falls and output rises",
   "output falls and unemployment rises",
   "nothing changes because prices adjust instantly"], ans=1,
   why="Every link in the chain runs in that direction in the short run."),
 dict(q="A student argues that a stronger currency is always good for a country's economy. The best correction is that a stronger currency", choices=[
   "is always harmful and never helps anyone",
   "lowers import prices for consumers but reduces net exports and hurts exporters",
   "has no effect on trade at all",
   "always raises net exports",
   "always causes inflation"], ans=1,
   why="Appreciation has real winners and real losers rather than a single unambiguous effect."),
]
