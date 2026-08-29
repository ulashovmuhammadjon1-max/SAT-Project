# MACRO 4.5 The Money Market — 50 questions
# The money market determines the NOMINAL interest rate.
#   Money demand (MD): downward sloping in the nominal interest rate, because the
#     interest rate is the opportunity cost of holding money instead of bonds.
#   Money supply (MS): a vertical line, since the central bank fixes the quantity
#     and it does not depend on the interest rate.
#   Equilibrium: MD = MS.
# MD shifters (nominal transaction demand): the price level and real GDP.
#   Higher price level  -> MD right -> nominal rate up.
#   Higher real GDP     -> MD right -> nominal rate up.
#   Lower price level or lower real GDP -> MD left -> nominal rate down.
#   A change in the interest rate itself is a MOVEMENT ALONG MD, not a shift.
# MS shifters: central bank actions only (open market operations, reserve
#   requirement, discount rate).
#   MS right -> nominal rate down.  MS left -> nominal rate up.
# Disequilibrium logic, verified:
#   Rate above equilibrium -> quantity of money demanded < quantity supplied ->
#     people hold surplus money, buy bonds -> bond prices rise -> rate falls.
#   Rate below equilibrium -> quantity demanded > supplied -> people sell bonds
#     to get money -> bond prices fall -> rate rises.
TOPIC = ("4.5", "The Money Market", 4)

QUESTIONS = [
 dict(q="The money market determines", choices=[
   "the real interest rate",
   "the nominal interest rate",
   "the price level directly",
   "the level of real GDP directly",
   "the exchange rate"], ans=1,
   why="The money market sets the nominal rate; the loanable funds market sets the real rate."),
 dict(q="The money demand curve slopes downward because", choices=[
   "higher interest rates make people wealthier",
   "the interest rate is the opportunity cost of holding money, so a higher rate makes people hold less of it",
   "money is a normal good",
   "the price level falls as rates rise",
   "banks lend more at high rates"], ans=1,
   why="Holding money forgoes the interest that bonds would pay."),
 dict(q="The opportunity cost of holding money is", choices=[
   "the inflation rate",
   "the nominal interest rate forgone on interest-bearing assets",
   "the price level",
   "the reserve requirement",
   "zero"], ans=1,
   why="Every dollar held as money is a dollar not earning the market rate."),
 dict(q="The money supply curve is drawn as a vertical line because", choices=[
   "money demand is fixed",
   "the central bank sets the quantity of money independently of the interest rate",
   "banks refuse to lend",
   "the price level is fixed",
   "the interest rate is fixed"], ans=1,
   why="The quantity supplied is a policy choice and does not respond to the interest rate."),
 dict(q="Equilibrium in the money market occurs where", choices=[
   "money demand is zero",
   "the quantity of money demanded equals the quantity supplied by the central bank",
   "the interest rate is zero",
   "saving equals investment",
   "aggregate demand equals aggregate supply"], ans=1,
   why="The nominal rate adjusts until the public is willing to hold exactly the money that exists."),
 dict(q="If the nominal interest rate is above the money market equilibrium, then", choices=[
   "there is a shortage of money and the rate will rise",
   "there is a surplus of money, people buy bonds, bond prices rise, and the interest rate falls",
   "the central bank must raise the money supply",
   "the rate stays above equilibrium",
   "money demand shifts right"], ans=1,
   why="Unwanted money balances are used to buy bonds, and higher bond prices mean lower rates."),
 dict(q="If the nominal interest rate is below the money market equilibrium, then", choices=[
   "people sell bonds to obtain money, bond prices fall, and the interest rate rises",
   "the surplus of money pushes the rate down further",
   "the central bank must lower the money supply",
   "nothing happens",
   "money demand shifts left"], ans=0,
   why="A shortage of money leads to bond sales, and falling bond prices are a rising interest rate."),
 dict(q="An increase in the money supply by the central bank will, in the money market,", choices=[
   "raise the nominal interest rate",
   "lower the nominal interest rate",
   "shift money demand right",
   "leave the interest rate unchanged",
   "make the money supply curve slope upward"], ans=1,
   why="A rightward shift of a vertical money supply meets money demand at a lower rate."),
 dict(q="A decrease in the money supply will", choices=[
   "lower the nominal interest rate",
   "raise the nominal interest rate",
   "shift money demand left",
   "have no effect on rates",
   "raise real GDP immediately"], ans=1,
   why="Less money available means the public must be induced to hold less, which takes a higher rate."),
 dict(q="An increase in the price level shifts money demand", choices=[
   "left, lowering the nominal interest rate",
   "right, raising the nominal interest rate",
   "not at all",
   "right, lowering the interest rate",
   "left, raising the interest rate"], ans=1,
   why="Higher prices mean more money is needed for the same volume of transactions."),
 dict(q="An increase in real GDP shifts money demand", choices=[
   "left, lowering the interest rate",
   "right, raising the interest rate",
   "not at all",
   "left, raising the interest rate",
   "right, lowering the interest rate"], ans=1,
   why="More transactions require more money at any given interest rate."),
 dict(q="A fall in real GDP will, other things equal, cause the nominal interest rate to", choices=[
   "rise", "fall", "stay the same", "become negative", "equal the inflation rate"], ans=1,
   why="Money demand shifts left, and with a fixed money supply the rate falls."),
 dict(q="A decrease in the price level will cause the nominal interest rate to", choices=[
   "rise", "fall", "stay constant", "become undefined", "rise then fall"], ans=1,
   why="Fewer dollars are needed for transactions, so money demand shifts left."),
 dict(q="A change in the nominal interest rate itself causes", choices=[
   "a shift of the money demand curve",
   "a movement along the money demand curve",
   "a shift of the money supply curve",
   "no change in the quantity of money demanded",
   "the money supply curve to slope downward"], ans=1,
   why="The interest rate is on the vertical axis, so a change in it is a movement along the curve."),
 dict(q="Which of the following shifts the money demand curve?", choices=[
   "a change in the interest rate",
   "a change in the price level",
   "an open market purchase",
   "a cut in the reserve requirement",
   "a change in the discount rate"], ans=1,
   why="The price level is a determinant of nominal money demand; the last three shift money supply."),
 dict(q="Which of the following shifts the money supply curve?", choices=[
   "an increase in real GDP",
   "an open market purchase of bonds by the central bank",
   "an increase in the price level",
   "a fall in the interest rate",
   "an increase in money demand"], ans=1,
   why="Only central bank actions move the vertical money supply line."),
 dict(q="The transactions demand for money arises because", choices=[
   "people fear losses on bonds",
   "money is needed to carry out everyday purchases",
   "money pays interest",
   "the central bank requires it",
   "bonds are illiquid"], ans=1,
   why="Households and firms hold money to bridge the gap between receipts and payments."),
 dict(q="An open market purchase of bonds by the central bank will, in the money market,", choices=[
   "shift money supply left and raise the interest rate",
   "shift money supply right and lower the interest rate",
   "shift money demand right",
   "shift money demand left",
   "leave both curves unchanged"], ans=1,
   why="Buying bonds injects reserves, expanding the money supply and pushing the rate down."),
 dict(q="An open market sale of bonds by the central bank will", choices=[
   "increase the money supply and lower the interest rate",
   "decrease the money supply and raise the interest rate",
   "shift money demand right",
   "have no effect",
   "lower the price level immediately"], ans=1,
   why="Selling bonds drains reserves, contracting the money supply."),
 dict(q="If the central bank wants to lower the nominal interest rate, it should", choices=[
   "sell bonds",
   "buy bonds on the open market",
   "raise the reserve requirement",
   "raise the discount rate",
   "reduce government spending"], ans=1,
   why="Buying bonds increases the money supply, and a rightward shift lowers the rate."),
 dict(q="If the central bank wants to raise the nominal interest rate, it should", choices=[
   "buy bonds",
   "sell bonds on the open market",
   "lower the reserve requirement",
   "lower the discount rate",
   "increase transfer payments"], ans=1,
   why="Selling bonds reduces the money supply, and a leftward shift raises the rate."),
 dict(q="Following an increase in the money supply, the fall in the interest rate is expected to", choices=[
   "reduce investment spending",
   "increase interest-sensitive investment and consumption spending",
   "reduce aggregate demand",
   "raise unemployment immediately",
   "lower the price level"], ans=1,
   why="Cheaper borrowing encourages spending on capital goods and durables."),
 dict(q="An increase in the money supply, working through the money market, will shift aggregate demand", choices=[
   "left, because interest rates rise",
   "right, because interest rates fall and investment rises",
   "not at all",
   "left, because investment rises",
   "right, because interest rates rise"], ans=1,
   why="The chain runs from a lower interest rate to more investment to higher aggregate demand."),
 dict(q="Which of the following correctly describes the effect of a decrease in the money supply?", choices=[
   "interest rate falls, investment rises, AD rises",
   "interest rate rises, investment falls, AD falls",
   "interest rate rises, investment rises, AD rises",
   "interest rate falls, investment falls, AD falls",
   "no effect on any of these"], ans=1,
   why="A smaller money supply raises the rate, discourages investment, and reduces aggregate demand."),
 dict(q="Suppose real GDP rises while the central bank holds the money supply constant. The nominal interest rate will", choices=[
   "fall", "rise", "be unchanged", "become negative", "equal zero"], ans=1,
   why="Money demand shifts right against a fixed vertical supply."),
 dict(q="If both the money supply and money demand increase, the effect on the nominal interest rate is", choices=[
   "definitely an increase",
   "indeterminate without knowing the relative sizes of the shifts",
   "definitely a decrease",
   "definitely zero",
   "definitely unchanged"], ans=1,
   why="The two shifts push the rate in opposite directions, so the net effect depends on magnitudes."),
 dict(q="If the money supply decreases and money demand also decreases, the nominal interest rate", choices=[
   "must rise",
   "may rise or fall depending on which shift is larger",
   "must fall",
   "must be unchanged",
   "must become zero"], ans=1,
   why="A smaller supply raises the rate while weaker demand lowers it, leaving the direction ambiguous."),
 dict(q="The quantity of money on the horizontal axis of the money market diagram is measured in", choices=[
   "real interest rate units",
   "nominal dollars",
   "units of output",
   "percentages",
   "bonds"], ans=1,
   why="The money market is drawn in nominal terms, which is why the price level shifts money demand."),
 dict(q="Money demand is sometimes called liquidity preference because it describes", choices=[
   "how much people wish to borrow",
   "how much of their wealth people wish to hold in the most liquid form rather than in bonds",
   "the supply of loanable funds",
   "the central bank's target",
   "the demand for capital goods"], ans=1,
   why="The choice is between holding money and holding interest-bearing assets."),
 dict(q="A financial innovation such as widespread debit cards that lets people transact with smaller money balances would", choices=[
   "shift money demand right and raise the interest rate",
   "shift money demand left and lower the interest rate",
   "shift money supply right",
   "shift money supply left",
   "have no effect on the money market"], ans=1,
   why="Less money is needed per dollar of transactions at every interest rate."),
 dict(q="Which of the following is held constant when drawing a money demand curve?", choices=[
   "the nominal interest rate",
   "the price level and real GDP",
   "the money supply",
   "bond prices",
   "the quantity of money demanded"], ans=1,
   why="The curve traces the response to the interest rate holding the shifters fixed."),
 dict(q="Bond prices and the nominal interest rate determined in the money market are", choices=[
   "positively related",
   "inversely related",
   "unrelated",
   "always equal",
   "both set by the government"], ans=1,
   why="A higher bond price on a fixed coupon is by definition a lower yield."),
 dict(q="After an open market purchase, bond prices", choices=[
   "fall, and interest rates rise",
   "rise, and interest rates fall",
   "are unchanged",
   "fall, and interest rates fall",
   "rise, and interest rates rise"], ans=1,
   why="The central bank's buying bids up bond prices, which is the same as pushing the rate down."),
 dict(q="A central bank that fixes the money supply and then experiences an unexpected surge in money demand will see", choices=[
   "the interest rate fall",
   "the interest rate rise",
   "the money supply rise automatically",
   "no change in the interest rate",
   "the money demand curve become vertical"], ans=1,
   why="With supply fixed, all the adjustment falls on the interest rate."),
 dict(q="A central bank that instead targets a specific interest rate must, when money demand rises,", choices=[
   "let the rate rise",
   "increase the money supply to hold the rate at target",
   "decrease the money supply",
   "raise the reserve requirement",
   "do nothing"], ans=1,
   why="Accommodating the extra demand with more money keeps the rate where the bank wants it."),
 dict(q="An increase in the price level raises the nominal quantity of money demanded because", choices=[
   "people expect higher interest rates",
   "the same basket of purchases now requires more dollars",
   "bonds become riskier",
   "the central bank prints more money",
   "real GDP falls"], ans=1,
   why="Nominal transactions demand scales with the price level."),
 dict(q="Which of the following is NOT a determinant of money demand?", choices=[
   "the price level",
   "real GDP",
   "the reserve requirement set by the central bank",
   "the ease of making transactions",
   "the level of nominal spending"], ans=2,
   why="The reserve requirement affects the money supply, not the public's desire to hold money."),
 dict(q="In the short run, an expansionary monetary policy will most likely", choices=[
   "lower output and raise unemployment",
   "raise output, lower unemployment, and raise the price level",
   "lower the price level",
   "leave output unchanged",
   "raise interest rates"], ans=1,
   why="A lower rate raises investment, aggregate demand, output, and prices while cutting unemployment."),
 dict(q="If the central bank increases the money supply and interest rates barely fall, the most likely explanation is that", choices=[
   "money supply is downward sloping",
   "money demand is very flat, so a large change in quantity requires only a small change in the rate",
   "money demand is vertical",
   "the price level is fixed",
   "bond prices are fixed"], ans=1,
   why="A highly interest-elastic money demand absorbs new money with little rate movement."),
 dict(q="The nominal interest rate determined in the money market affects real output primarily through", choices=[
   "changes in government spending",
   "changes in interest-sensitive investment and consumption spending",
   "changes in taxes",
   "changes in the reserve requirement",
   "changes in net exports only"], ans=1,
   why="Investment is the main channel from interest rates to aggregate demand."),
 dict(q="Which pair of events would unambiguously lower the nominal interest rate?", choices=[
   "an increase in the money supply and an increase in real GDP",
   "an increase in the money supply and a fall in the price level",
   "a decrease in the money supply and a fall in real GDP",
   "a decrease in the money supply and a rise in the price level",
   "an increase in money demand and a decrease in money supply"], ans=1,
   why="More money supply and weaker money demand both push the rate down."),
 dict(q="Which pair of events would unambiguously raise the nominal interest rate?", choices=[
   "an increase in the money supply and a rise in real GDP",
   "a decrease in the money supply and a rise in the price level",
   "an increase in the money supply and a fall in the price level",
   "a decrease in the money supply and a fall in real GDP",
   "no change in either curve"], ans=1,
   why="Less money supplied and more money demanded both push the rate up."),
 dict(q="Holding wealth in bonds rather than money has the advantage of", choices=[
   "greater liquidity",
   "earning interest",
   "being usable for everyday purchases",
   "having no risk",
   "being counted in M1"], ans=1,
   why="The return on bonds is precisely what is given up by holding money."),
 dict(q="At very low nominal interest rates, money demand tends to become", choices=[
   "very steep, because people hold little money",
   "very flat, because the cost of holding money is small and people are willing to hold large balances",
   "vertical",
   "upward sloping",
   "irrelevant"], ans=1,
   why="With almost no interest forgone, people are close to indifferent between money and bonds."),
 dict(q="A student claims that when the central bank buys bonds, interest rates rise because the central bank is demanding funds. The error is that", choices=[
   "the central bank never buys bonds",
   "buying bonds pays reserves into the banking system, increasing the money supply and lowering the rate",
   "bond prices fall when the central bank buys",
   "the money supply curve slopes upward",
   "money demand shifts left"], ans=1,
   why="The central bank is supplying money, not demanding funds."),
 dict(q="If the central bank doubles the money supply and the price level eventually doubles as well, the nominal interest rate in the long run will", choices=[
   "be permanently lower",
   "return toward its original level, since money demand also doubles",
   "be permanently higher",
   "fall to zero",
   "be indeterminate"], ans=1,
   why="A proportional rise in the price level shifts money demand right by the same amount."),
 dict(q="The immediate effect of an expansionary open market operation on the interest rate is called the", choices=[
   "wealth effect",
   "liquidity effect",
   "crowding out effect",
   "multiplier effect",
   "Fisher effect"], ans=1,
   why="The liquidity effect is the initial fall in the rate as more money is supplied."),
 dict(q="Money demand shifting right while the money supply is held fixed will", choices=[
   "lower the interest rate and raise investment",
   "raise the interest rate and reduce investment",
   "leave investment unchanged",
   "shift the money supply right",
   "lower the price level"], ans=1,
   why="A higher rate makes borrowing to invest less attractive."),
 dict(q="Which statement about the money market and the loanable funds market is correct?", choices=[
   "Both determine the real interest rate",
   "The money market determines the nominal rate, while the loanable funds market determines the real rate",
   "Both determine the nominal rate",
   "Neither is affected by central bank policy",
   "The money market determines the real rate and loanable funds the nominal rate"], ans=1,
   why="Keeping the two rates straight is essential, because students routinely swap them."),
 dict(q="Suppose the economy is in a recession with a large output gap and the central bank expands the money supply. The most likely short-run outcome is", choices=[
   "a higher interest rate and less investment",
   "a lower interest rate, more investment, and a rise in real GDP with only a modest increase in the price level",
   "no change in real GDP and a large rise in the price level",
   "a fall in real GDP",
   "a fall in the price level"], ans=1,
   why="With substantial slack, the extra aggregate demand mostly raises output rather than prices."),
]
