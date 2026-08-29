# MACRO 5.3 Money Growth and Inflation — 50 questions
# Every number checked against MV = PQ:
#   M=200, V=5 -> MV=1000; Q=500 -> P = 1000/500 = 2.
#   M doubled to 400 with V=5, Q=500 -> MV=2000, P = 2000/500 = 4 (price level doubles).
#   M=1,000, V=4 -> nominal GDP = 4,000; Q=800 -> P = 4,000/800 = 5.
#   M=500, V=6, P=3 -> Q = MV/P = 3,000/3 = 1,000.
#   Nominal GDP 6,000 with M=1,500 -> V = 6,000/1,500 = 4.
#   Nominal GDP 9,000 with M=1,800 -> V = 5.
#   Growth form: %M + %V = %P + %Q.
#     %M=8, %V=0, %Q=3 -> %P = 5.
#     %M=10, %V=0, %Q=2 -> %P = 8.
#     %M=12, %V=0, %Q=3 -> %P = 9.
#     %M=6, %V=0, %Q=6 -> %P = 0.
#     %M=4, %V=2, %Q=3 -> %P = 3.
#   Fisher: nominal rate = real rate + expected inflation; 3 + 6 = 9.
TOPIC = ("5.3", "Money Growth and Inflation", 5)
MVPQ = dict(
    headers=["Year", "Money supply (M)", "Velocity (V)", "Real output (Q)"],
    rows=[["1", "200", "5", "500"], ["2", "400", "5", "500"]],
)
QUESTIONS = [
 dict(q="The equation of exchange is written as", choices=[
   "M + V = P + Q",
   "MV = PQ",
   "MP = VQ",
   "M/V = P/Q",
   "MQ = PV"], ans=1,
   why="The money supply times its velocity equals nominal output, the price level times real output."),
 dict(q="In the equation of exchange, V represents", choices=[
   "the volume of production",
   "the velocity of money, the average number of times a dollar is spent on final goods in a year",
   "the value of exports",
   "the variability of prices",
   "the volume of bank reserves"], ans=1,
   why="Velocity is the turnover rate of the money stock against nominal GDP."),
 dict(q="In the equation of exchange, PQ is equal to", choices=[
   "real GDP",
   "nominal GDP",
   "the money supply",
   "the price level alone",
   "consumption spending"], ans=1,
   why="The price level times real output is nominal output."),
 dict(q="Velocity can be computed as", choices=[
   "the money supply divided by nominal GDP",
   "nominal GDP divided by the money supply",
   "real GDP divided by the price level",
   "the price level times real GDP",
   "the money multiplier"], ans=1,
   why="Rearranging MV = PQ gives V = PQ/M."),
 dict(q="If nominal GDP is $6,000 billion and the money supply is $1,500 billion, velocity equals", choices=[
   "0.25", "2", "4", "6", "9"], ans=2,
   why="V = 6,000/1,500 = 4."),
 dict(q="If nominal GDP is $9,000 billion and the money supply is $1,800 billion, velocity equals", choices=[
   "0.2", "2", "5", "9", "18"], ans=2,
   why="V = 9,000/1,800 = 5."),
 dict(q="If the money supply is $1,000 billion and velocity is 4, nominal GDP equals", choices=[
   "$250 billion", "$1,000 billion", "$2,000 billion", "$4,000 billion", "$40,000 billion"], ans=3,
   why="MV = 1,000 x 4 = $4,000 billion of nominal output."),
 dict(q="If the money supply is $1,000 billion, velocity is 4, and real output is 800 units, the price level is", choices=[
   "0.2", "2", "4", "5", "8"], ans=3,
   why="P = MV/Q = 4,000/800 = 5."),
 dict(q="If M = 500, V = 6, and P = 3, real output Q equals", choices=[
   "250", "500", "900", "1,000", "3,000"], ans=3,
   why="Q = MV/P = 3,000/3 = 1,000."),
 dict(q="Refer to the table. The price level in Year 1 is", table=MVPQ, choices=[
   "0.4", "1", "2", "4", "5"], ans=2,
   why="P = MV/Q = (200 x 5)/500 = 2."),
 dict(q="Refer to the table. The price level in Year 2 is", table=MVPQ, choices=[
   "1", "2", "3", "4", "5"], ans=3,
   why="P = (400 x 5)/500 = 4."),
 dict(q="Refer to the table. Between Year 1 and Year 2, doubling the money supply with velocity and real output constant caused", table=MVPQ, choices=[
   "real output to double",
   "the price level to double",
   "velocity to fall by half",
   "no change in the price level",
   "real output to fall by half"], ans=1,
   why="With MV = PQ and both V and Q fixed, P must rise in proportion to M."),
 dict(q="The quantity theory of money assumes that", choices=[
   "velocity and real output are highly variable in the short run",
   "velocity is relatively stable and real output is determined by real factors, so changes in M chiefly change P",
   "the money supply is fixed",
   "prices never change",
   "the price level determines the money supply"], ans=1,
   why="Stable V and independently determined Q are what make money growth translate into inflation."),
 dict(q="Written in growth rates, the equation of exchange becomes", choices=[
   "%M x %V = %P x %Q",
   "%M + %V = %P + %Q",
   "%M - %V = %P - %Q",
   "%M = %P x %Q",
   "%M + %P = %V + %Q"], ans=1,
   why="Taking growth rates of a product turns multiplication into addition."),
 dict(q="If the money supply grows 8 percent, velocity is constant, and real output grows 3 percent, inflation is about", choices=[
   "3%", "5%", "8%", "11%", "24%"], ans=1,
   why="%P = %M + %V - %Q = 8 + 0 - 3 = 5%."),
 dict(q="If the money supply grows 10 percent, velocity is constant, and real output grows 2 percent, inflation is about", choices=[
   "2%", "5%", "8%", "10%", "12%"], ans=2,
   why="10 + 0 - 2 = 8%."),
 dict(q="If the money supply grows 12 percent, velocity is constant, and real output grows 3 percent, inflation is about", choices=[
   "3%", "4%", "9%", "12%", "15%"], ans=2,
   why="12 + 0 - 3 = 9%."),
 dict(q="If the money supply grows 6 percent and real output grows 6 percent with constant velocity, inflation is about", choices=[
   "0%", "3%", "6%", "12%", "36%"], ans=0,
   why="Money growth exactly matched by output growth leaves the price level unchanged."),
 dict(q="If the money supply grows 4 percent, velocity grows 2 percent, and real output grows 3 percent, inflation is about", choices=[
   "1%", "2%", "3%", "5%", "9%"], ans=2,
   why="4 + 2 - 3 = 3%."),
 dict(q="A central bank that wants zero inflation in the long run should let the money supply grow at", choices=[
   "zero percent",
   "the growth rate of real output, assuming stable velocity",
   "the inflation rate",
   "twice the growth rate of output",
   "the nominal interest rate"], ans=1,
   why="Money growth matching output growth leaves nominal GDP growing at the real rate with no price change."),
 dict(q="Monetary neutrality is the proposition that", choices=[
   "money affects nothing at all",
   "in the long run a change in the money supply changes nominal variables but leaves real variables unchanged",
   "the money supply cannot be changed",
   "money affects only real GDP",
   "velocity is zero"], ans=1,
   why="In the long run, a money supply change alters prices and nominal wages proportionally, leaving real output and employment where they were."),
 dict(q="Which of the following is a real variable?", choices=[
   "the price level",
   "real GDP per person",
   "the nominal wage",
   "the money supply",
   "nominal GDP"], ans=1,
   why="Real variables are measured in units of goods rather than in money."),
 dict(q="The classical dichotomy refers to the idea that", choices=[
   "nominal and real variables are the same",
   "real variables are determined separately from nominal variables in the long run",
   "there are two central banks",
   "inflation causes unemployment",
   "money is a real variable"], ans=1,
   why="It is the theoretical separation that makes monetary neutrality possible."),
 dict(q="A doubling of the money supply in the long run, with velocity and output unchanged, will", choices=[
   "double real GDP",
   "double the price level and the nominal wage, leaving the real wage unchanged",
   "halve the price level",
   "double the real wage",
   "double the unemployment rate"], ans=1,
   why="All nominal magnitudes rise together, so purchasing power is unchanged."),
 dict(q="The inflation tax refers to", choices=[
   "a legislated tax on price increases",
   "the loss of purchasing power suffered by money holders when the government finances spending by printing money",
   "a tariff",
   "the corporate income tax",
   "a progressive income tax"], ans=1,
   why="Printing money to pay bills transfers real resources from holders of currency to the government."),
 dict(q="Hyperinflation is generally caused by", choices=[
   "a small increase in aggregate demand",
   "extremely rapid growth in the money supply, usually to finance government deficits",
   "an increase in real GDP",
   "a fall in velocity",
   "an improvement in technology"], ans=1,
   why="Every well-documented hyperinflation followed explosive money creation to cover a fiscal gap."),
 dict(q="During a hyperinflation, velocity typically", choices=[
   "falls sharply",
   "rises, because people spend money as fast as possible to avoid holding a depreciating asset",
   "stays exactly constant",
   "becomes zero",
   "becomes negative"], ans=1,
   why="Rapidly rising prices make holding money costly, so money changes hands faster."),
 dict(q="Because velocity rises during a hyperinflation, prices tend to rise", choices=[
   "more slowly than the money supply",
   "even faster than the money supply",
   "at exactly the money growth rate",
   "not at all",
   "only after output falls"], ans=1,
   why="With V rising as well as M, nominal spending grows faster than money alone."),
 dict(q="An economy where the money supply is growing 40 percent a year and real output is stagnant will most likely experience", choices=[
   "deflation",
   "roughly 40 percent inflation",
   "stable prices",
   "rapid real growth",
   "falling velocity"], ans=1,
   why="With Q flat and V roughly stable, inflation tracks money growth."),
 dict(q="In the long run, the primary cause of sustained inflation is", choices=[
   "greedy firms",
   "growth of the money supply in excess of the growth of real output",
   "labor unions",
   "high oil prices",
   "trade deficits"], ans=1,
   why="One-off cost shocks raise prices once; only persistent money growth sustains ongoing inflation."),
 dict(q="An adverse supply shock raises the price level but is not usually a source of sustained inflation because", choices=[
   "it never affects prices",
   "it is a one-time increase in the price level unless it is accommodated by continued money growth",
   "it lowers velocity permanently",
   "it raises real output",
   "the central bank cannot respond"], ans=1,
   why="Sustained inflation requires the price level to keep rising, which requires continuing monetary expansion."),
 dict(q="The Fisher effect states that", choices=[
   "the real interest rate rises one for one with inflation",
   "the nominal interest rate rises one for one with expected inflation, leaving the real rate unchanged",
   "inflation lowers nominal rates",
   "money growth lowers nominal rates permanently",
   "velocity equals the interest rate"], ans=1,
   why="Lenders build expected inflation into the nominal rate to protect the real return."),
 dict(q="If the real interest rate is 3 percent and expected inflation is 6 percent, the nominal interest rate is about", choices=[
   "-3%", "2%", "3%", "6%", "9%"], ans=4,
   why="Nominal = real + expected inflation = 3 + 6 = 9%."),
 dict(q="If the nominal interest rate is 7 percent and inflation turns out to be 4 percent, the realized real interest rate is", choices=[
   "-3%", "1.75%", "3%", "4%", "11%"], ans=2,
   why="Real = nominal - inflation = 7 - 4 = 3%."),
 dict(q="Higher long-run money growth raises the nominal interest rate because", choices=[
   "it reduces the supply of loanable funds",
   "it raises expected inflation, which lenders add to the nominal rate",
   "it lowers real output permanently",
   "it raises the real interest rate permanently",
   "it reduces velocity"], ans=1,
   why="This is the Fisher effect operating on expectations of future inflation."),
 dict(q="A short-run increase in the money supply lowers the nominal interest rate, but sustained money growth raises it. This apparent contradiction is resolved by noting that", choices=[
   "the two statements are about the same time horizon",
   "the short-run liquidity effect works through the money market while the long-run effect works through expected inflation",
   "interest rates never change",
   "velocity is zero in the short run",
   "the central bank sets real rates permanently"], ans=1,
   why="A one-time injection is a liquidity effect; a permanent higher growth rate is an expectations effect."),
 dict(q="Shoe-leather costs of inflation refer to", choices=[
   "the cost of changing posted prices",
   "the resources people waste economizing on money holdings, such as making extra trips to the bank",
   "the cost of new shoes",
   "the cost of unemployment",
   "the cost of taxation"], ans=1,
   why="Inflation makes holding cash costly, so people spend real effort holding less of it."),
 dict(q="Menu costs of inflation are", choices=[
   "the costs of eating out",
   "the real resources used in changing prices, reprinting catalogs, and updating price lists",
   "the shoe-leather costs of extra bank trips",
   "the loss on nominal debt",
   "the cost of holding bonds"], ans=1,
   why="Frequent price changes consume real resources."),
 dict(q="Unexpected inflation redistributes wealth from", choices=[
   "borrowers to lenders",
   "lenders to borrowers, because loans are repaid in dollars of lower purchasing power",
   "the government to households",
   "workers to the unemployed",
   "no one to no one"], ans=1,
   why="The real value of a fixed nominal debt falls when prices rise unexpectedly."),
 dict(q="Unexpected deflation redistributes wealth from", choices=[
   "lenders to borrowers",
   "borrowers to lenders, since repayments are worth more in purchasing power",
   "savers to spenders",
   "firms to workers",
   "no one to no one"], ans=1,
   why="Falling prices raise the real burden of a fixed nominal debt."),
 dict(q="Which statement about money and real GDP in the long run is correct?", choices=[
   "Money growth permanently raises real GDP.",
   "Real GDP is determined by productivity and resources, not by the money supply.",
   "Money growth permanently lowers real GDP.",
   "Real GDP equals the money supply times velocity.",
   "Real GDP rises one for one with the price level."],ans=1,
   why="Long-run output depends on real factors, which is exactly what monetary neutrality means."),
 dict(q="If velocity were to fall while the money supply grew at a constant rate, inflation would", choices=[
   "rise",
   "be lower than the money growth rate minus output growth",
   "equal money growth exactly",
   "be unaffected",
   "become infinite"], ans=1,
   why="Falling V subtracts from nominal spending growth, damping the rise in prices."),
 dict(q="The main reason the quantity theory is described as a long-run theory is that", choices=[
   "money never affects output",
   "in the short run prices are sticky and velocity varies, so money growth can affect real output temporarily",
   "velocity is never measurable",
   "real output is fixed forever",
   "the money supply cannot be measured"], ans=1,
   why="Short-run stickiness gives money real effects that disappear once prices adjust."),
 dict(q="A government facing a large deficit that cannot borrow or raise taxes may resort to", choices=[
   "reducing velocity",
   "printing money, which produces seigniorage revenue and inflation",
   "lowering the price level",
   "raising real output instantly",
   "eliminating currency"], ans=1,
   why="Money creation is the residual source of revenue and is the standard route to hyperinflation."),
 dict(q="Seigniorage is", choices=[
   "a tax on imports",
   "the real revenue a government earns by creating money",
   "interest paid on the national debt",
   "the profit of commercial banks",
   "a tariff on exports"], ans=1,
   why="Newly created money buys real goods before prices adjust."),
 dict(q="If the central bank doubles the money supply and the price level eventually doubles, the real money supply M/P", choices=[
   "doubles", "returns to its original level", "halves", "becomes zero", "quadruples"], ans=1,
   why="Both numerator and denominator double, so real money balances are unchanged."),
 dict(q="Country A has money growth of 3 percent and Country B has money growth of 30 percent, with similar real growth. We would expect", choices=[
   "identical inflation rates",
   "Country B to have a much higher inflation rate",
   "Country A to have higher inflation",
   "both to have deflation",
   "Country B to grow faster in real terms permanently"], ans=1,
   why="Across countries and decades, average inflation tracks average money growth."),
 dict(q="Which of the following would break the tight link between money growth and inflation in the short run?", choices=[
   "perfectly flexible prices",
   "a sharp and unpredictable change in velocity",
   "constant velocity",
   "constant real output",
   "monetary neutrality"], ans=1,
   why="MV = PQ still holds, but unstable V means M no longer predicts P reliably."),
 dict(q="An economy has 5 percent inflation, 2 percent real growth, and stable velocity. Its money supply is growing at about", choices=[
   "2%", "3%", "5%", "7%", "10%"], ans=3,
   why="%M = %P + %Q - %V = 5 + 2 - 0 = 7%."),
 dict(q="The claim that inflation is always and everywhere a monetary phenomenon is best understood as a statement about", choices=[
   "the short-run effects of a single supply shock",
   "sustained inflation over long periods, which requires ongoing money growth",
   "the level of real GDP",
   "the unemployment rate",
   "the exchange rate only"], ans=1,
   why="Individual price shocks come and go; only persistent money growth keeps the price level climbing."),
]
