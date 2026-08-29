# MACRO 4.6 Monetary Policy — 50 questions
# The full transmission chain, tested forward and backward in this bank:
#   EXPANSIONARY (easy money):
#     buy bonds / cut reserve requirement / cut discount rate / cut interest on reserves
#     -> reserves up -> money supply RIGHT -> nominal interest rate DOWN
#     -> investment and interest-sensitive consumption UP -> AD RIGHT
#     -> real GDP UP, unemployment DOWN, price level UP.
#   CONTRACTIONARY (tight money):
#     sell bonds / raise reserve requirement / raise discount rate / raise interest on reserves
#     -> reserves down -> money supply LEFT -> nominal interest rate UP
#     -> investment DOWN -> AD LEFT
#     -> real GDP DOWN, unemployment UP, price level DOWN (or inflation slows).
#   Long run: money is neutral. A permanent rise in the money supply leaves real
#     GDP at potential and raises the price level proportionally.
# Multiplier figures used, derived here:
#   rr = 0.10 -> money multiplier 10, so a $200 open market purchase can raise
#     the money supply by at most 200 x 10 = $2,000.
#   rr = 0.20 -> multiplier 5, so a $300 open market SALE can cut the money supply
#     by at most 300 x 5 = $1,500.
#   rr = 0.25 -> multiplier 4, so a $1,000 purchase gives at most $4,000.
TOPIC = ("4.6", "Monetary Policy", 4)

QUESTIONS = [
 dict(q="Monetary policy refers to actions taken by", choices=[
   "the legislature to change taxes and spending",
   "the central bank to change the money supply and interest rates",
   "firms to change investment",
   "households to change saving",
   "foreign governments to change exchange rates"], ans=1,
   why="Monetary policy is the central bank's tool set; taxes and spending are fiscal policy."),
 dict(q="The three traditional tools of monetary policy are", choices=[
   "taxes, spending, and transfers",
   "open market operations, the reserve requirement, and the discount rate",
   "the money multiplier, the spending multiplier, and the tax multiplier",
   "inflation, unemployment, and growth",
   "M1, M2, and reserves"], ans=1,
   why="These three are the standard tools listed in the AP course."),
 dict(q="Open market operations involve the central bank", choices=[
   "setting the interest rate banks charge each other by law",
   "buying and selling government bonds to change bank reserves",
   "lending directly to households",
   "changing tax rates",
   "printing currency for the government to spend"], ans=1,
   why="Bond purchases and sales are the day-to-day instrument for adjusting reserves."),
 dict(q="An open market purchase of government bonds by the central bank is", choices=[
   "contractionary, because it drains reserves",
   "expansionary, because it adds reserves and increases the money supply",
   "neutral",
   "a fiscal policy action",
   "an increase in the reserve requirement"], ans=1,
   why="Paying for the bonds credits reserves to banks, which supports more lending."),
 dict(q="An open market sale of government bonds is", choices=[
   "expansionary",
   "contractionary, because banks pay for the bonds with reserves",
   "neutral",
   "fiscal policy",
   "a cut in the discount rate"], ans=1,
   why="Selling bonds absorbs reserves and shrinks the money supply."),
 dict(q="The discount rate is", choices=[
   "the rate banks charge their best customers",
   "the rate the central bank charges commercial banks that borrow reserves from it",
   "the rate on government bonds",
   "the inflation rate",
   "the rate banks pay depositors"], ans=1,
   why="It is the cost of borrowing reserves directly from the central bank."),
 dict(q="Lowering the discount rate is", choices=[
   "contractionary",
   "expansionary, because borrowing reserves becomes cheaper and banks lend more",
   "neutral",
   "a fiscal action",
   "the same as selling bonds"], ans=1,
   why="Cheaper access to reserves encourages banks to expand lending."),
 dict(q="Raising the discount rate will tend to", choices=[
   "increase the money supply and lower interest rates",
   "decrease the money supply and raise interest rates",
   "leave the money supply unchanged",
   "raise investment",
   "raise aggregate demand"], ans=1,
   why="Costlier reserves discourage borrowing and lending by banks."),
 dict(q="Raising the reserve requirement is", choices=[
   "expansionary, because banks hold more reserves",
   "contractionary, because it reduces excess reserves and lowers the money multiplier",
   "neutral",
   "a fiscal policy tool",
   "the same as buying bonds"], ans=1,
   why="Banks must hold more of each deposit idle, so lending and the multiplier both shrink."),
 dict(q="Lowering the reserve requirement will", choices=[
   "reduce the money multiplier",
   "increase excess reserves and expand the money supply",
   "raise interest rates",
   "reduce lending",
   "have no effect"], ans=1,
   why="Freeing reserves lets banks lend more, and each round of the multiplier leaks less."),
 dict(q="In modern practice, central banks conduct policy mainly by", choices=[
   "frequently changing the reserve requirement",
   "steering a short-term policy interest rate, using open market operations and the interest paid on reserves",
   "printing currency",
   "changing taxes",
   "setting the exchange rate"], ans=1,
   why="The reserve requirement is a blunt tool that is rarely adjusted; the policy rate is the working instrument."),
 dict(q="Paying a higher rate of interest on bank reserves tends to be", choices=[
   "expansionary, because banks have more income",
   "contractionary, because holding reserves becomes more attractive than lending them out",
   "neutral",
   "a fiscal policy",
   "a way to lower market interest rates"], ans=1,
   why="A higher return on idle reserves raises the floor under market rates and discourages lending."),
 dict(q="Lowering the interest rate paid on reserves would be expected to", choices=[
   "reduce lending",
   "encourage banks to lend rather than hold reserves, expanding the money supply",
   "raise the policy rate",
   "raise the reserve requirement",
   "have no effect on the money supply"], ans=1,
   why="A smaller reward for holding reserves pushes banks toward making loans."),
 dict(q="Expansionary monetary policy is appropriate when the economy is", choices=[
   "producing above potential with high inflation",
   "in a recession with a negative output gap and high unemployment",
   "at long-run equilibrium",
   "experiencing a trade surplus",
   "growing at its potential rate"], ans=1,
   why="Easy money raises aggregate demand, which is what a demand-deficient recession needs."),
 dict(q="Contractionary monetary policy is appropriate when the economy is", choices=[
   "in a deep recession",
   "producing beyond potential output with rising inflation",
   "at full employment with stable prices",
   "experiencing deflation",
   "growing slowly"], ans=1,
   why="Tight money restrains aggregate demand and slows inflation."),
 dict(q="The correct sequence for expansionary monetary policy is", choices=[
   "money supply up, interest rate up, investment down, AD left",
   "money supply up, interest rate down, investment up, AD right",
   "money supply down, interest rate down, investment up, AD right",
   "money supply up, interest rate down, investment down, AD left",
   "money supply down, interest rate up, investment up, AD right"], ans=1,
   why="Each link runs in the same direction: more money, cheaper credit, more investment, higher demand."),
 dict(q="The correct sequence for contractionary monetary policy is", choices=[
   "money supply down, interest rate up, investment down, AD left",
   "money supply down, interest rate down, investment down, AD left",
   "money supply up, interest rate up, investment down, AD left",
   "money supply down, interest rate up, investment up, AD right",
   "money supply up, interest rate down, investment up, AD right"], ans=0,
   why="Less money raises the rate, which cuts investment and pulls aggregate demand back."),
 dict(q="Expansionary monetary policy will, in the short run, cause real GDP to", choices=[
   "fall and the price level to fall",
   "rise and the price level to rise",
   "rise and the price level to fall",
   "fall and the price level to rise",
   "stay constant"], ans=1,
   why="A rightward shift of AD along an upward-sloping short-run aggregate supply raises both."),
 dict(q="Contractionary monetary policy will, in the short run, cause real GDP to", choices=[
   "rise and the price level to rise",
   "fall and the price level to fall",
   "rise and the price level to fall",
   "stay the same",
   "fall and the price level to rise"], ans=1,
   why="AD shifts left along short-run aggregate supply, reducing output and easing prices."),
 dict(q="Expansionary monetary policy is expected to move the unemployment rate", choices=[
   "up", "down", "to zero", "to the natural rate exactly", "unpredictably in every case"], ans=1,
   why="Higher output requires more labor, so cyclical unemployment falls."),
 dict(q="To fight high inflation, the central bank should", choices=[
   "buy bonds and lower the discount rate",
   "sell bonds, raise the discount rate, or raise the reserve requirement",
   "increase government spending",
   "cut taxes",
   "lower the interest paid on reserves"], ans=1,
   why="Every one of these actions reduces the money supply and restrains aggregate demand."),
 dict(q="To fight a recession, the central bank should", choices=[
   "sell bonds and raise the reserve requirement",
   "buy bonds, lower the discount rate, or lower the reserve requirement",
   "raise taxes",
   "cut government spending",
   "raise the interest paid on reserves"], ans=1,
   why="These actions expand the money supply, lower rates, and raise aggregate demand."),
 dict(q="If the reserve requirement is 10 percent, a $200 open market purchase can raise the money supply by at most", choices=[
   "$20", "$200", "$1,800", "$2,000", "$20,000"], ans=3,
   why="$200 of new reserves times a money multiplier of 10."),
 dict(q="If the reserve requirement is 20 percent, a $300 open market sale can reduce the money supply by at most", choices=[
   "$60", "$300", "$1,200", "$1,500", "$6,000"], ans=3,
   why="$300 times a multiplier of 5, and the sale drains reserves so the change is negative."),
 dict(q="With a 25 percent reserve requirement, a $1,000 open market purchase can expand the money supply by at most", choices=[
   "$250", "$1,000", "$2,500", "$4,000", "$25,000"], ans=3,
   why="$1,000 times a multiplier of 4."),
 dict(q="In the long run, an increase in the money supply is generally believed to", choices=[
   "permanently raise real GDP",
   "raise the price level while leaving real output at potential",
   "permanently lower unemployment",
   "lower the price level",
   "raise real wages permanently"], ans=1,
   why="This is the neutrality of money: nominal variables adjust, real ones return to potential."),
 dict(q="The idea that monetary policy cannot change real output in the long run is called", choices=[
   "the liquidity trap",
   "the neutrality of money",
   "crowding out",
   "the Fisher effect",
   "the multiplier effect"], ans=1,
   why="Prices and wages eventually adjust fully, leaving real variables where they started."),
 dict(q="A liquidity trap describes a situation in which", choices=[
   "the money supply cannot be increased",
   "nominal interest rates are near zero, so further increases in the money supply do little to lower rates or raise spending",
   "banks refuse deposits",
   "inflation is very high",
   "the reserve requirement is 100 percent"], ans=1,
   why="With rates already at the floor, the usual transmission channel is blocked."),
 dict(q="Monetary policy may be weak in a deep recession if", choices=[
   "interest rates are very high",
   "banks hold new reserves as excess reserves and firms are unwilling to borrow at any rate",
   "the reserve requirement is low",
   "inflation is high",
   "the central bank buys too many bonds"], ans=1,
   why="Reserves that are never lent, and borrowers who will not borrow, break the chain to spending."),
 dict(q="One advantage of monetary policy over fiscal policy is that monetary policy", choices=[
   "has no effect on inflation",
   "can be implemented quickly without a lengthy legislative process",
   "always works with no lag",
   "raises output permanently",
   "requires no forecasting"], ans=1,
   why="The central bank can act at a scheduled meeting rather than waiting for a budget to pass."),
 dict(q="A disadvantage of monetary policy is that", choices=[
   "it is decided by legislators",
   "it works through interest rates and investment, so its effects come with a substantial and variable lag",
   "it cannot change the money supply",
   "it has no effect on interest rates",
   "it directly changes taxes"], ans=1,
   why="Investment plans take time to respond, so the policy may act after conditions have changed."),
 dict(q="Suppose the central bank buys bonds and the interest rate falls, but investment barely changes. The most likely explanation is that", choices=[
   "the money multiplier is too large",
   "investment demand is quite insensitive to the interest rate, perhaps because business confidence is low",
   "the reserve requirement rose",
   "money demand shifted left",
   "the price level fell"], ans=1,
   why="A steep investment demand curve breaks the link between cheaper credit and more spending."),
 dict(q="If the central bank sells bonds during a recession, the likely result is", choices=[
   "a faster recovery",
   "a deeper recession, since rates rise and investment falls",
   "no change in output",
   "lower unemployment",
   "higher investment"], ans=1,
   why="This is contractionary policy applied at exactly the wrong time."),
 dict(q="Which combination is contractionary?", choices=[
   "buying bonds and lowering the discount rate",
   "selling bonds and raising the reserve requirement",
   "buying bonds and lowering the reserve requirement",
   "lowering the discount rate and lowering the reserve requirement",
   "buying bonds and lowering interest on reserves"], ans=1,
   why="Both actions drain reserves and shrink the money supply."),
 dict(q="Which combination is expansionary?", choices=[
   "selling bonds and raising the discount rate",
   "buying bonds and lowering the reserve requirement",
   "raising the reserve requirement and raising interest on reserves",
   "selling bonds and raising the reserve requirement",
   "raising the discount rate and selling bonds"], ans=1,
   why="Both actions add to reserves and lending capacity."),
 dict(q="Expansionary monetary policy affects net exports because a lower domestic interest rate", choices=[
   "attracts foreign financial investment and strengthens the currency",
   "discourages foreign financial investment, weakens the currency, and raises net exports",
   "has no effect on the exchange rate",
   "raises the price of exports abroad",
   "reduces exports"], ans=1,
   why="Less demand for the domestic currency depreciates it, making exports cheaper abroad."),
 dict(q="Contractionary monetary policy tends to affect the exchange rate by", choices=[
   "depreciating the domestic currency",
   "appreciating the domestic currency as higher rates attract financial inflows",
   "leaving it unchanged",
   "raising net exports",
   "reducing capital inflows"], ans=1,
   why="Higher returns draw in foreign funds, raising demand for the currency."),
 dict(q="The federal funds rate is best described as", choices=[
   "the rate the central bank charges banks",
   "the interest rate banks charge one another for overnight loans of reserves",
   "the rate on government bonds",
   "the rate banks charge households",
   "the inflation rate"], ans=1,
   why="It is the interbank market rate for reserves and serves as the policy rate."),
 dict(q="If the central bank wants to lower the policy rate, it will typically", choices=[
   "sell securities to drain reserves",
   "buy securities to add reserves to the banking system",
   "raise the reserve requirement",
   "raise the discount rate",
   "reduce government spending"], ans=1,
   why="More reserves available in the interbank market pushes the overnight rate down."),
 dict(q="An economy has an inflation rate of 9 percent and output above potential. The appropriate monetary policy and its effect is", choices=[
   "expansionary policy, raising output further",
   "contractionary policy, raising interest rates and reducing aggregate demand",
   "expansionary policy, lowering the price level",
   "no policy change",
   "contractionary policy, lowering interest rates"], ans=1,
   why="An inflationary gap calls for tighter money, which works by raising rates and cutting spending."),
 dict(q="An economy has 11 percent unemployment and output well below potential. The appropriate policy and effect is", choices=[
   "contractionary policy, lowering the price level",
   "expansionary policy, lowering interest rates and raising aggregate demand",
   "contractionary policy, raising output",
   "no policy change",
   "expansionary policy, raising interest rates"], ans=1,
   why="A recessionary gap calls for easier money working through lower rates."),
 dict(q="A student writes that an open market purchase raises interest rates and therefore raises investment. Two things are wrong. The correct chain is that an open market purchase", choices=[
   "raises rates and lowers investment",
   "lowers rates and raises investment",
   "lowers rates and lowers investment",
   "raises rates and raises investment",
   "leaves rates and investment unchanged"], ans=1,
   why="Buying bonds expands the money supply, which lowers the rate and encourages investment."),
 dict(q="A student writes that raising the reserve requirement increases the money supply. The error is that a higher reserve requirement", choices=[
   "raises the money multiplier",
   "forces banks to hold more of each deposit idle, reducing lending and the money supply",
   "has no effect on lending",
   "is a fiscal policy",
   "lowers the discount rate"], ans=1,
   why="Higher required reserves mean fewer excess reserves and a smaller multiplier."),
 dict(q="If the central bank increases the money supply while the government simultaneously raises taxes sharply, the effect on real GDP is", choices=[
   "certainly an increase",
   "ambiguous, because the two policies push aggregate demand in opposite directions",
   "certainly a decrease",
   "certainly zero",
   "certainly a fall in the price level with no output change"], ans=1,
   why="Expansionary monetary policy and contractionary fiscal policy offset one another to an unknown degree."),
 dict(q="Monetary policy influences aggregate demand mainly through", choices=[
   "changes in government purchases",
   "changes in interest-sensitive investment and consumption, and through the exchange rate",
   "changes in tax rates",
   "changes in the natural rate of unemployment",
   "changes in long-run aggregate supply"], ans=1,
   why="Interest rates and the exchange rate are the two channels the AP course emphasizes."),
 dict(q="The central bank's dual mandate is usually described as", choices=[
   "balancing the budget and reducing debt",
   "promoting maximum employment and stable prices",
   "setting exchange rates and tariffs",
   "raising tax revenue and cutting spending",
   "controlling wages and profits"], ans=1,
   why="Price stability and full employment are the two statutory objectives."),
 dict(q="If a central bank pursues expansionary policy when the economy is already at full employment, the most likely long-run result is", choices=[
   "permanently higher real GDP",
   "a higher price level with real GDP back at potential",
   "permanently lower unemployment",
   "deflation",
   "a permanent fall in interest rates"], ans=1,
   why="With no slack, the extra demand is absorbed by prices once wages adjust."),
 dict(q="Which of the following would most directly increase bank reserves?", choices=[
   "an increase in the reserve requirement",
   "a central bank purchase of securities from banks",
   "a central bank sale of securities to banks",
   "an increase in the discount rate",
   "an increase in the interest paid on reserves"], ans=1,
   why="The central bank pays for the securities by crediting the banks' reserve accounts."),
 dict(q="Monetary and fiscal policy are said to be complementary when", choices=[
   "one expands while the other contracts",
   "both are expansionary during a recession or both are contractionary during inflation",
   "neither is used",
   "monetary policy alone is used",
   "the central bank sets tax rates"], ans=1,
   why="Policies pointing the same direction reinforce rather than offset each other."),
 dict(q="Trace the full effect of a large open market sale on an economy at full employment. In the short run it will", choices=[
   "raise money supply, lower rates, raise investment, raise output and prices",
   "lower money supply, raise rates, lower investment, lower output and the price level, and raise unemployment",
   "lower money supply, lower rates, lower investment, raise output",
   "raise money supply, raise rates, lower output",
   "leave every variable unchanged"], ans=1,
   why="Every link of the contractionary chain runs in the same direction, ending in a recessionary gap."),
]
