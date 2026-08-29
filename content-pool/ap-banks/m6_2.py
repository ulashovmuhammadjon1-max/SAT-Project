# MACRO 6.2 Exchange Rates — 50 questions
# Every conversion verified in both directions:
#   $1.25 per euro  <-> 1/1.25 = 0.80 euros per dollar.
#   $1.50 per euro  <-> 1/1.50 = 0.6667 euros per dollar.
#   $1.60 per pound <-> 1/1.60 = 0.625 pounds per dollar.
#   100 yen per dollar <-> 1/100 = $0.010 per yen.
#   125 yen per dollar <-> 1/125 = $0.008 per yen.
#   20 pesos per dollar <-> $0.05 per peso; 25 pesos per dollar <-> $0.04 per peso.
#   1.25 Canadian dollars per U.S. dollar <-> US$0.80 per Canadian dollar.
#   A EUR 40,000 car: at $1.25/EUR costs $50,000; at $1.50/EUR costs $60,000.
#   A $30,000 car: at $1.25/EUR costs EUR 24,000; at $1.50/EUR costs EUR 20,000.
#   Percent change from $1.25/EUR to $1.50/EUR = 0.25/1.25 = +20% (dollar price of
#     the euro rises 20%, so the euro appreciates 20% against the dollar).
#   In the other direction 0.80 -> 0.6667 euros per dollar = -16.67%.
#   Cross rate: if $1.50 = 1 pound and $1.20 = 1 euro, then 1 pound = 1.50/1.20
#     = 1.25 euros.
#   A EUR 200 hotel bill at $1.10/EUR = $220; at $1.05/EUR = $210.
TOPIC = ("6.2", "Exchange Rates", 6)

QUESTIONS = [
 dict(q="A nominal exchange rate is", choices=[
   "the ratio of two countries' price levels",
   "the price of one nation's currency expressed in terms of another nation's currency",
   "the interest rate paid on foreign bonds",
   "the ratio of exports to imports",
   "the difference between two countries' inflation rates"], ans=1,
   why="An exchange rate is simply the price of one currency in units of another."),
 dict(q="A currency appreciates when", choices=[
   "it buys fewer units of foreign currency than before",
   "it buys more units of foreign currency than before",
   "the country's price level rises",
   "the country's exports fall",
   "the central bank prints more of it"], ans=1,
   why="Appreciation means the currency has become more valuable in terms of other currencies."),
 dict(q="A currency depreciates when", choices=[
   "its value in terms of other currencies falls",
   "its value in terms of other currencies rises",
   "domestic interest rates rise",
   "the country runs a trade surplus",
   "the country's GDP grows"], ans=0,
   why="Depreciation is a fall in the currency's foreign-exchange value."),
 dict(q="If the dollar price of a euro rises from $1.20 to $1.30, then", choices=[
   "the dollar has appreciated and the euro has depreciated",
   "the euro has appreciated and the dollar has depreciated",
   "both currencies have appreciated",
   "both currencies have depreciated",
   "neither currency's value has changed"], ans=1,
   why="It now takes more dollars to buy one euro, so the euro is stronger and the dollar weaker."),
 dict(q="If the exchange rate moves from 100 yen per dollar to 125 yen per dollar, the dollar has", choices=[
   "depreciated against the yen",
   "appreciated against the yen",
   "kept the same value",
   "become fixed",
   "been devalued by the Japanese government"], ans=1,
   why="One dollar now buys more yen, so the dollar is stronger."),
 dict(q="If the exchange rate is $1.25 per euro, the price of a dollar in euros is", choices=[
   "0.75 euros", "0.80 euros", "1.00 euro", "1.25 euros", "1.60 euros"], ans=1,
   why="Inverting 1.25 gives 1/1.25 = 0.80 euros per dollar."),
 dict(q="If the exchange rate is $1.60 per British pound, the price of a dollar in pounds is", choices=[
   "0.400 pounds", "0.500 pounds", "0.625 pounds", "0.800 pounds", "1.600 pounds"], ans=2,
   why="1/1.60 = 0.625 pounds per dollar."),
 dict(q="If 100 yen exchange for one dollar, the dollar price of one yen is", choices=[
   "$0.001", "$0.010", "$0.100", "$1.000", "$10.000"], ans=1,
   why="1/100 = $0.01 per yen."),
 dict(q="If the exchange rate is 25 Mexican pesos per U.S. dollar, one peso is worth", choices=[
   "$0.02", "$0.04", "$0.25", "$2.50", "$4.00"], ans=1,
   why="1/25 = $0.04 per peso."),
 dict(q="If one Canadian dollar buys US$0.80, then one U.S. dollar buys", choices=[
   "0.80 Canadian dollars",
   "1.00 Canadian dollar",
   "1.25 Canadian dollars",
   "1.60 Canadian dollars",
   "2.00 Canadian dollars"], ans=2,
   why="1/0.80 = 1.25 Canadian dollars per U.S. dollar."),
 dict(q="The dollar-euro rate moves from $1.25 per euro to $1.50 per euro. The euro has appreciated by", choices=[
   "10 percent", "16.7 percent", "20 percent", "25 percent", "50 percent"], ans=2,
   why="The dollar price of a euro rose by 0.25 from a base of 1.25, which is 20 percent."),
 dict(q="The rate moves from 0.80 euros per dollar to 0.6667 euros per dollar. The dollar has", choices=[
   "appreciated about 17 percent",
   "depreciated about 17 percent",
   "appreciated 20 percent",
   "depreciated 20 percent",
   "not changed in value"], ans=1,
   why="The euro price of a dollar fell from 0.80 to 0.6667, a decline of about 16.7 percent."),
 dict(q="An appreciation of the U.S. dollar makes U.S. exports", choices=[
   "cheaper for foreign buyers",
   "more expensive for foreign buyers",
   "unchanged in foreign-currency price",
   "free of tariffs",
   "more numerous"], ans=1,
   why="A stronger dollar means foreigners must give up more of their currency for each dollar-priced good."),
 dict(q="An appreciation of the U.S. dollar makes imports into the United States", choices=[
   "more expensive for Americans",
   "cheaper for Americans",
   "unchanged in dollar price",
   "impossible to purchase",
   "subject to a quota"], ans=1,
   why="Each dollar buys more foreign currency, so foreign goods cost fewer dollars."),
 dict(q="A depreciation of the U.S. dollar makes U.S. exports", choices=[
   "more expensive abroad",
   "cheaper abroad",
   "unchanged in price abroad",
   "unavailable abroad",
   "taxed more heavily"], ans=1,
   why="Foreign buyers need less of their own currency to obtain a dollar."),
 dict(q="A depreciation of the U.S. dollar makes imported goods", choices=[
   "cheaper in dollars",
   "more expensive in dollars",
   "unchanged in dollars",
   "cheaper in foreign currency terms for foreigners",
   "exempt from customs duties"], ans=1,
   why="It takes more dollars to buy the foreign currency needed to pay for imports."),
 dict(q="A German car sells for 40,000 euros. At an exchange rate of $1.25 per euro, its price in dollars is", choices=[
   "$32,000", "$40,000", "$45,000", "$50,000", "$60,000"], ans=3,
   why="40,000 times 1.25 equals 50,000 dollars."),
 dict(q="The same 40,000-euro car after the rate moves to $1.50 per euro costs an American buyer", choices=[
   "$40,000", "$50,000", "$55,000", "$60,000", "$66,000"], ans=3,
   why="40,000 times 1.50 equals 60,000 dollars."),
 dict(q="An American car sells for $30,000. At $1.25 per euro its price to a European buyer is", choices=[
   "20,000 euros", "24,000 euros", "30,000 euros", "34,500 euros", "37,500 euros"], ans=1,
   why="30,000 divided by 1.25 equals 24,000 euros."),
 dict(q="The same $30,000 car after the rate moves to $1.50 per euro costs a European buyer", choices=[
   "18,000 euros", "20,000 euros", "24,000 euros", "30,000 euros", "45,000 euros"], ans=1,
   why="30,000 divided by 1.50 equals 20,000 euros, so the weaker dollar makes U.S. goods cheaper abroad."),
 dict(q="A European hotel bill of 200 euros costs an American traveler how much when the rate is $1.10 per euro?", choices=[
   "$180", "$200", "$210", "$220", "$240"], ans=3,
   why="200 times 1.10 equals 220 dollars."),
 dict(q="If the rate then moves to $1.05 per euro, that same 200-euro bill costs", choices=[
   "$190", "$200", "$210", "$220", "$230"], ans=2,
   why="200 times 1.05 equals 210 dollars, so the stronger dollar makes European travel cheaper."),
 dict(q="If $1.50 buys one British pound and $1.20 buys one euro, then one pound is worth", choices=[
   "0.80 euros", "1.00 euro", "1.25 euros", "1.50 euros", "1.80 euros"], ans=2,
   why="Dividing 1.50 dollars per pound by 1.20 dollars per euro gives 1.25 euros per pound."),
 dict(q="A student says the dollar 'got stronger' because the number of yen per dollar fell. The correct response is that", choices=[
   "the student is right, since a smaller number means a stronger dollar",
   "the student is wrong, because fewer yen per dollar means the dollar buys less and has depreciated",
   "the student is right only if U.S. inflation is zero",
   "yen per dollar says nothing about the dollar's value",
   "the statement depends on the Japanese interest rate"], ans=1,
   why="When the rate is quoted as foreign currency per dollar, a fall in that number is a dollar depreciation."),
 dict(q="An exchange rate quoted as 'dollars per pound' rising means", choices=[
   "the dollar has appreciated",
   "the pound has appreciated",
   "both currencies have gained value",
   "the pound has been devalued",
   "the U.S. trade deficit has closed"], ans=1,
   why="More dollars are needed per pound, so the pound is worth more."),
 dict(q="An exchange rate quoted as 'pounds per dollar' rising means", choices=[
   "the pound has appreciated",
   "the dollar has appreciated",
   "the dollar has depreciated",
   "nothing about relative values",
   "the two currencies now trade one for one"], ans=1,
   why="Each dollar now buys more pounds."),
 dict(q="A real exchange rate differs from a nominal exchange rate because it", choices=[
   "is quoted only in dollars",
   "adjusts the nominal rate for differences in price levels between the two countries",
   "is set by the central bank",
   "applies only to financial assets",
   "is always equal to one"], ans=1,
   why="The real rate compares the purchasing power of the two currencies over goods."),
 dict(q="If the U.S. inflation rate is much higher than Japan's over several years, the dollar will most likely", choices=[
   "appreciate against the yen",
   "depreciate against the yen",
   "remain exactly fixed",
   "become the world reserve currency",
   "rise in both nominal and real terms"], ans=1,
   why="Faster domestic inflation erodes a currency's purchasing power relative to a low-inflation partner."),
 dict(q="Purchasing power parity suggests that in the long run exchange rates adjust so that", choices=[
   "all countries have the same interest rate",
   "a given basket of goods costs about the same amount in different countries when converted to one currency",
   "trade balances are always zero",
   "all currencies trade one for one",
   "central banks never intervene"], ans=1,
   why="Purchasing power parity ties the exchange rate to relative price levels."),
 dict(q="A hamburger costs $5 in the United States and 500 yen in Japan. The purchasing power parity exchange rate is", choices=[
   "50 yen per dollar", "100 yen per dollar", "250 yen per dollar", "500 yen per dollar", "2,500 yen per dollar"], ans=1,
   why="500 yen divided by 5 dollars equals 100 yen per dollar."),
 dict(q="If that hamburger parity rate is 100 yen per dollar but the market rate is 125 yen per dollar, then relative to parity the dollar is", choices=[
   "undervalued", "overvalued", "correctly valued", "fixed", "unquoted"], ans=1,
   why="The dollar buys more yen in the market than purchasing power parity implies."),
 dict(q="Under a floating exchange rate system, the exchange rate is determined by", choices=[
   "the central bank alone",
   "supply and demand in the foreign exchange market",
   "an international treaty",
   "the ratio of the two countries' GDPs",
   "the trade ministry of the larger country"], ans=1,
   why="Floating rates are market prices set by currency supply and demand."),
 dict(q="Under a fixed exchange rate system, a government's deliberate lowering of its currency's official value is called", choices=[
   "a depreciation", "a devaluation", "an appreciation", "a revaluation", "a float"], ans=1,
   why="A deliberate policy change to a fixed rate is a devaluation, not a market depreciation."),
 dict(q="A deliberate increase in a currency's official fixed value is called", choices=[
   "an appreciation", "a revaluation", "a devaluation", "a depreciation", "sterilization"], ans=1,
   why="Revaluation is the policy counterpart to appreciation under a fixed rate."),
 dict(q="Which of the following pairs correctly describes a single exchange rate movement?", choices=[
   "the dollar appreciates and the euro appreciates",
   "the dollar appreciates and the euro depreciates",
   "the dollar depreciates and the euro depreciates",
   "the dollar appreciates and the euro is unchanged",
   "both currencies are devalued"], ans=1,
   why="A bilateral rate change is always one currency up and the other down."),
 dict(q="U.S. exporters of machinery would most prefer", choices=[
   "a strong dollar, because their inputs get cheaper",
   "a weak dollar, because it lowers the foreign-currency price of their machinery",
   "a fixed dollar, regardless of level",
   "higher U.S. tariffs on machinery",
   "a rise in the dollar price of foreign currency to zero"], ans=1,
   why="Depreciation makes U.S. goods cheaper to foreign buyers, raising export sales."),
 dict(q="U.S. consumers of imported goods and American tourists traveling abroad would most prefer", choices=[
   "a weak dollar", "a strong dollar", "high U.S. inflation", "a devaluation of the dollar", "a fall in the dollar's value"], ans=1,
   why="A strong dollar buys more foreign currency, so foreign goods and travel cost less."),
 dict(q="A U.S. firm that imports Italian marble and sells the finished product only in the United States is helped most by", choices=[
   "a depreciation of the dollar against the euro",
   "an appreciation of the dollar against the euro",
   "higher U.S. interest rates paid to foreigners",
   "an increase in Italian inflation matched by an equal euro appreciation",
   "a U.S. tariff on marble"], ans=1,
   why="A stronger dollar lowers the dollar cost of the imported input."),
 dict(q="If the dollar appreciates by 10 percent against every currency, U.S. net exports will most likely", choices=[
   "rise", "fall", "stay the same", "become zero", "rise only if inflation falls"], ans=1,
   why="Exports become dearer abroad and imports cheaper at home, both of which shrink net exports."),
 dict(q="Which of the following is measured in units of foreign currency per dollar?", choices=[
   "$1.30 per euro", "112 yen per dollar", "$0.75 per Canadian dollar", "$1.55 per pound", "$0.055 per peso"], ans=1,
   why="Only that quote puts the dollar in the denominator."),
 dict(q="If the euro appreciates against the dollar by 25 percent from $1.20 per euro, the new rate is", choices=[
   "$0.96 per euro", "$1.32 per euro", "$1.45 per euro", "$1.50 per euro", "$1.60 per euro"], ans=3,
   why="1.20 times 1.25 equals 1.50 dollars per euro."),
 dict(q="A U.S. investor holds a bond paying a fixed amount of euros. If the dollar appreciates against the euro before the bond pays, the investor's dollar return", choices=[
   "rises", "falls", "is unchanged", "becomes negative by definition", "doubles"], ans=1,
   why="The euro payment converts into fewer dollars."),
 dict(q="A Japanese investor holds U.S. Treasury bonds. If the dollar appreciates against the yen, the investor's yen return", choices=[
   "falls", "rises", "is unchanged", "is zero", "depends only on U.S. inflation"], ans=1,
   why="Dollar interest and principal convert into more yen than before."),
 dict(q="If a country's currency is expected to depreciate sharply next month, holders of that currency today will most likely", choices=[
   "buy more of it immediately",
   "sell it now in exchange for foreign currency",
   "ignore the expectation entirely",
   "demand more domestic bonds paying that currency",
   "expect its exports to become more expensive"], ans=1,
   why="Expected depreciation makes holding the currency less attractive, so people move out of it now."),
 dict(q="Everything else equal, a rise in a country's real interest rate relative to other countries tends to cause its currency to", choices=[
   "depreciate", "appreciate", "remain fixed", "be devalued", "leave the foreign exchange market"], ans=1,
   why="Higher returns draw foreign financial capital in, raising demand for the currency."),
 dict(q="The exchange rate between two currencies is quoted as 1.30 dollars per euro. An American paying a 650-euro invoice needs", choices=[
   "$500", "$650", "$780", "$845", "$910"], ans=3,
   why="650 times 1.30 equals 845 dollars."),
 dict(q="At 0.80 euros per dollar, a European paying a $2,000 invoice needs", choices=[
   "1,250 euros", "1,600 euros", "2,000 euros", "2,500 euros", "2,800 euros"], ans=1,
   why="2,000 times 0.80 equals 1,600 euros."),
 dict(q="A U.S. exporter quotes a price of $100 per unit. If the exchange rate moves from 0.80 to 0.90 euros per dollar, the euro price of the unit moves from", choices=[
   "80 euros to 70 euros",
   "80 euros to 90 euros",
   "90 euros to 80 euros",
   "100 euros to 90 euros",
   "125 euros to 111 euros"], ans=1,
   why="100 dollars times 0.80 is 80 euros and times 0.90 is 90 euros, so the stronger dollar raises the foreign price."),
 dict(q="Which statement about a currency depreciation is FALSE?", choices=[
   "it lowers the foreign-currency price of the country's exports",
   "it raises the domestic-currency price of imports",
   "it tends to raise net exports",
   "it makes foreign travel cheaper for domestic residents",
   "it can add to domestic inflationary pressure through import prices"], ans=3,
   why="A weaker currency buys less abroad, so foreign travel becomes more expensive, not cheaper."),
 dict(q="A country's nominal exchange rate is unchanged, but its price level rises 10 percent while its trading partner's is flat. The country's real exchange rate has", choices=[
   "fallen, making its goods more competitive",
   "risen, making its goods less competitive abroad",
   "stayed the same",
   "become undefined",
   "moved only if the nominal rate also moves"], ans=1,
   why="Domestic goods are now relatively more expensive even though the nominal rate did not move."),
]
