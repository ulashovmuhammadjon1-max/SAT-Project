# MACRO 4.7 The Loanable Funds Market — 50 questions
# The loanable funds market determines the REAL interest rate.
#   SUPPLY of loanable funds = saving (households, firms, government surpluses,
#     and foreign lending). Upward sloping: a higher real rate rewards saving.
#   DEMAND for loanable funds = borrowing, mostly for investment. Downward
#     sloping: a lower real rate makes more projects worth financing.
#   Equilibrium real rate where saving = borrowing.
# SUPPLY shifters:
#   more private saving, a government budget surplus, capital inflows from abroad
#     -> supply RIGHT -> real rate DOWN, quantity of funds UP.
#   less saving, capital outflows -> supply LEFT -> real rate UP, quantity DOWN.
# DEMAND shifters:
#   better investment opportunities/new technology, business optimism, an
#     investment tax credit, GOVERNMENT DEFICIT BORROWING
#     -> demand RIGHT -> real rate UP, quantity UP.
#   pessimism, fewer profitable projects -> demand LEFT -> real rate DOWN.
# CROWDING OUT, worked through:
#   deficit-financed government spending -> demand for loanable funds RIGHT
#   -> real rate UP -> private investment DOWN. The quantity of funds traded
#   rises, but private investment specifically falls. In the long run, less
#   capital accumulation means slower growth of potential output.
# Expected inflation raises the NOMINAL rate one for one (Fisher) while the
#   loanable funds market pins down the REAL rate; the two markets must not be
#   confused, and several items here corner that error directly.
TOPIC = ("4.7", "The Loanable Funds Market", 4)

QUESTIONS = [
 dict(q="The loanable funds market determines", choices=[
   "the nominal interest rate",
   "the real interest rate",
   "the price level",
   "the money supply",
   "the exchange rate"], ans=1,
   why="Loanable funds set the real rate, while the money market sets the nominal rate."),
 dict(q="In the loanable funds market, the supply of loanable funds comes from", choices=[
   "firms borrowing to invest",
   "saving by households, firms, and government",
   "the central bank alone",
   "consumption spending",
   "imports"], ans=1,
   why="Funds available to lend originate in saving."),
 dict(q="In the loanable funds market, the demand for loanable funds comes from", choices=[
   "household saving",
   "borrowers, principally firms financing investment and governments financing deficits",
   "the central bank",
   "exports",
   "tax revenue"], ans=1,
   why="Demand for funds is demand to borrow."),
 dict(q="The supply of loanable funds slopes upward because", choices=[
   "a higher real interest rate discourages saving",
   "a higher real interest rate rewards saving, so more funds are made available",
   "saving does not respond to interest rates",
   "the central bank fixes the quantity",
   "borrowing rises with the rate"], ans=1,
   why="A better return on saving induces people to postpone consumption."),
 dict(q="The demand for loanable funds slopes downward because", choices=[
   "higher rates make more investment projects profitable",
   "a lower real interest rate makes more investment projects worth undertaking",
   "saving falls as rates rise",
   "the government borrows more when rates are high",
   "money demand is downward sloping"], ans=1,
   why="The real rate is the cost of financing capital projects."),
 dict(q="Equilibrium in the loanable funds market occurs where", choices=[
   "the money supply equals money demand",
   "the quantity of funds saved equals the quantity of funds borrowed",
   "the budget is balanced",
   "the nominal rate equals zero",
   "aggregate demand equals aggregate supply"], ans=1,
   why="The real rate adjusts until saving and borrowing are equal."),
 dict(q="An increase in household saving shifts the supply of loanable funds", choices=[
   "left, raising the real interest rate",
   "right, lowering the real interest rate",
   "right, raising the real interest rate",
   "left, lowering the real interest rate",
   "not at all"], ans=1,
   why="More funds available drives down their price, which is the real rate."),
 dict(q="A fall in household saving will cause the real interest rate to", choices=[
   "fall", "rise", "stay constant", "become zero", "equal the inflation rate"], ans=1,
   why="A leftward shift of supply means less is available to lend, so the price of funds rises."),
 dict(q="An increase in government borrowing to finance a budget deficit shifts", choices=[
   "the supply of loanable funds right, lowering the real rate",
   "the demand for loanable funds right, raising the real rate",
   "the demand for loanable funds left, lowering the real rate",
   "the supply of loanable funds left, lowering the real rate",
   "neither curve"], ans=1,
   why="The government adds itself to the pool of borrowers, increasing demand for funds."),
 dict(q="Crowding out refers to", choices=[
   "the central bank raising interest rates",
   "the reduction in private investment caused by higher real interest rates when the government borrows",
   "a fall in government spending",
   "an increase in the money supply",
   "a decline in imports"], ans=1,
   why="Government borrowing bids up the real rate and squeezes private borrowers out of the market."),
 dict(q="When government deficit borrowing crowds out private investment, the total quantity of loanable funds traded", choices=[
   "falls",
   "rises, even though private investment specifically falls",
   "is unchanged",
   "falls to zero",
   "cannot be determined"], ans=1,
   why="The higher rate draws out more saving, so total lending rises while the private share shrinks."),
 dict(q="A government budget surplus, other things equal, will", choices=[
   "shift demand for loanable funds right and raise the real rate",
   "shift supply of loanable funds right and lower the real rate",
   "shift supply left and raise the real rate",
   "have no effect on the loanable funds market",
   "shift demand left and raise the real rate"], ans=1,
   why="Public saving adds to the pool of funds available to lend."),
 dict(q="The long-run consequence of persistent crowding out is", choices=[
   "faster growth of potential output",
   "a smaller capital stock and slower growth of potential output",
   "lower prices",
   "higher saving",
   "no effect on growth"], ans=1,
   why="Less private investment today means less capital available to produce with tomorrow."),
 dict(q="An investment tax credit that makes new capital cheaper for firms will", choices=[
   "shift the supply of loanable funds right",
   "shift the demand for loanable funds right, raising the real interest rate",
   "shift the demand for loanable funds left",
   "lower the real interest rate",
   "leave the market unchanged"], ans=1,
   why="More projects become worth financing at every rate, which is an increase in demand for funds."),
 dict(q="A technological breakthrough that creates many profitable investment opportunities will cause the real interest rate to", choices=[
   "fall", "rise", "stay the same", "become negative", "be indeterminate"], ans=1,
   why="Demand for loanable funds shifts right against a given supply."),
 dict(q="A wave of business pessimism about future profits will shift", choices=[
   "supply of loanable funds left",
   "demand for loanable funds left, lowering the real interest rate",
   "demand for loanable funds right",
   "supply right, raising the rate",
   "neither curve"], ans=1,
   why="Fewer firms wish to borrow at any rate, so demand falls and the rate falls with it."),
 dict(q="An inflow of foreign financial capital into a country will", choices=[
   "shift the supply of loanable funds right and lower the real interest rate",
   "shift the demand for loanable funds right",
   "shift supply left and raise the rate",
   "have no effect",
   "lower the money supply"], ans=0,
   why="Foreign lending adds to the funds available domestically."),
 dict(q="A large outflow of financial capital to other countries will cause the domestic real interest rate to", choices=[
   "fall", "rise", "stay constant", "become zero", "fall then rise"], ans=1,
   why="Fewer funds are available at home, so supply shifts left."),
 dict(q="Which of the following distinguishes the loanable funds market from the money market?", choices=[
   "Both determine the nominal rate",
   "Loanable funds determines the real rate through saving and borrowing, while the money market determines the nominal rate through money supply and money demand",
   "The money market has an upward-sloping supply curve",
   "Loanable funds has a vertical supply curve",
   "The two markets are identical"], ans=1,
   why="The axis variable and the curves are different, and confusing them is the most common error in this unit."),
 dict(q="The supply curve in the loanable funds market differs from the money supply curve in that the loanable funds supply is", choices=[
   "vertical",
   "upward sloping, because saving responds to the real interest rate",
   "downward sloping",
   "horizontal",
   "set by the central bank"], ans=1,
   why="Money supply is fixed by the central bank; saving genuinely responds to the rate."),
 dict(q="An increase in expected inflation, holding the real loanable funds equilibrium unchanged, will", choices=[
   "lower the nominal interest rate",
   "raise the nominal interest rate while leaving the real rate unchanged",
   "lower the real interest rate",
   "raise the real interest rate",
   "have no effect on any rate"], ans=1,
   why="Expected inflation is added to the real rate to give the nominal rate."),
 dict(q="Government deficit spending financed by borrowing raises the real interest rate. The effect on private investment is that it", choices=[
   "rises", "falls", "is unchanged", "becomes zero", "cannot be determined"], ans=1,
   why="A higher cost of funds makes fewer private projects worth undertaking."),
 dict(q="If the government runs a deficit and the central bank simultaneously buys bonds, the effect on the real interest rate is", choices=[
   "certainly an increase",
   "less clear, since one action raises demand for funds while the other adds to lendable reserves",
   "certainly a decrease",
   "certainly zero",
   "the same as the deficit alone"], ans=1,
   why="The two forces push in opposite directions, so the net effect depends on their sizes."),
 dict(q="Which of the following would shift the supply of loanable funds to the right?", choices=[
   "an increase in government borrowing",
   "a rise in the household saving rate",
   "an investment tax credit",
   "a wave of business optimism",
   "an outflow of financial capital"], ans=1,
   why="More saving is directly more funds supplied; the others affect demand or reduce supply."),
 dict(q="Which of the following would shift the demand for loanable funds to the right?", choices=[
   "an increase in household saving",
   "an increase in the government budget deficit",
   "a foreign capital inflow",
   "a budget surplus",
   "an increase in retained earnings held idle"], ans=1,
   why="Deficit borrowing adds the government to the demand side of the market."),
 dict(q="At a real interest rate above the loanable funds equilibrium, there is", choices=[
   "a shortage of funds and the rate will rise",
   "a surplus of funds, and competition among lenders pushes the rate down",
   "no adjustment",
   "an increase in borrowing",
   "a leftward shift of supply"], ans=1,
   why="Saving exceeds borrowing, so lenders bid the rate down to place their funds."),
 dict(q="At a real interest rate below equilibrium there is", choices=[
   "a surplus of funds and the rate falls",
   "a shortage of funds, and competition among borrowers pushes the rate up",
   "no adjustment",
   "a rightward shift of demand",
   "an increase in saving"], ans=1,
   why="Borrowers want more than savers will provide, which bids the rate up."),
 dict(q="Which of the following pairs correctly matches a market with the rate it determines?", choices=[
   "money market and the real rate; loanable funds and the nominal rate",
   "money market and the nominal rate; loanable funds and the real rate",
   "both markets and the nominal rate",
   "both markets and the real rate",
   "neither market determines an interest rate"], ans=1,
   why="This pairing is tested directly and often reversed by students."),
 dict(q="An increase in the real interest rate causes", choices=[
   "a rightward shift of the supply of loanable funds",
   "a movement along the supply and demand curves, not a shift of either",
   "a leftward shift of demand",
   "a rightward shift of demand",
   "the supply curve to become vertical"], ans=1,
   why="The rate is the variable on the axis, so a change in it moves along the curves."),
 dict(q="If saving increases and investment demand also increases, the real interest rate", choices=[
   "must rise",
   "may rise or fall, but the quantity of loanable funds will definitely rise",
   "must fall",
   "will be unchanged",
   "will fall to zero"], ans=1,
   why="Both shifts raise the quantity traded, but they push the rate in opposite directions."),
 dict(q="If saving decreases and investment demand also decreases, the quantity of loanable funds traded", choices=[
   "definitely rises",
   "definitely falls, while the effect on the real rate is ambiguous",
   "is unchanged",
   "cannot be determined",
   "definitely falls along with the real rate"], ans=1,
   why="Both curves shift left, which certainly reduces quantity but leaves the rate indeterminate."),
 dict(q="A country that runs a large budget deficit year after year is likely to experience", choices=[
   "lower real interest rates and more private investment",
   "higher real interest rates and less private investment",
   "no change in interest rates",
   "higher saving with no change in rates",
   "a permanent increase in potential output"], ans=1,
   why="Persistent public borrowing keeps demand for funds elevated and crowds out private borrowers."),
 dict(q="One reason crowding out may be small in a deep recession is that", choices=[
   "the government does not borrow in a recession",
   "there is little private investment demand competing for funds, so the rate rises little",
   "saving is zero",
   "the central bank raises rates",
   "the demand curve is vertical"], ans=1,
   why="With few firms wanting to borrow, additional government borrowing meets slack in the market."),
 dict(q="National saving in a closed economy consists of", choices=[
   "private saving only",
   "private saving plus public saving",
   "public saving only",
   "investment only",
   "consumption plus investment"], ans=1,
   why="Households and government both contribute to the pool of funds available."),
 dict(q="Public saving is", choices=[
   "household saving deposited in banks",
   "tax revenue minus government spending, so it is negative when the budget is in deficit",
   "always positive",
   "the same as investment",
   "the money supply"], ans=1,
   why="A deficit is negative public saving, which reduces national saving."),
 dict(q="In a closed economy, in equilibrium, national saving equals", choices=[
   "consumption", "investment", "government spending", "the money supply", "taxes"], ans=1,
   why="Everything saved is borrowed and used for investment, which is exactly the loanable funds equilibrium."),
 dict(q="A policy that successfully encourages households to save more will, in the loanable funds market,", choices=[
   "raise the real interest rate and reduce investment",
   "lower the real interest rate and raise investment",
   "leave the rate unchanged",
   "shift demand right",
   "reduce the quantity of funds traded"], ans=1,
   why="More supply means a lower price of funds and a larger quantity of investment financed."),
 dict(q="An aging population that begins to draw down its accumulated savings would tend to", choices=[
   "shift the supply of loanable funds right and lower the real rate",
   "shift the supply of loanable funds left and raise the real rate",
   "shift demand left",
   "shift demand right",
   "have no effect"], ans=1,
   why="Dissaving reduces the funds available at every real rate."),
 dict(q="The real interest rate is the appropriate rate for the loanable funds diagram because", choices=[
   "it is the rate quoted on loan contracts",
   "saving and investment decisions depend on purchasing power gained or given up, not on nominal dollars",
   "it is always higher than the nominal rate",
   "it never changes",
   "the central bank sets it"], ans=1,
   why="Real decisions respond to real returns and real costs."),
 dict(q="Suppose the government cuts taxes without cutting spending, financing the gap by borrowing. In the loanable funds market this will", choices=[
   "shift supply right and lower the real rate",
   "shift demand right and raise the real rate, crowding out private investment",
   "shift demand left",
   "leave the market unchanged",
   "lower the quantity of funds traded"], ans=1,
   why="A larger deficit means more government borrowing, which is more demand for funds."),
 dict(q="Which of the following is a source of the supply of loanable funds in an open economy?", choices=[
   "domestic firms borrowing",
   "financial capital flowing in from abroad",
   "government deficits",
   "consumption spending",
   "an investment tax credit"], ans=1,
   why="Foreign savers can lend into the domestic market, adding to supply."),
 dict(q="If the real interest rate in a country rises above rates abroad, we would expect", choices=[
   "capital to flow out, shifting supply left",
   "capital to flow in, shifting the supply of loanable funds right",
   "no capital movement",
   "demand for loanable funds to fall",
   "the nominal rate to fall"], ans=1,
   why="Higher returns attract foreign lenders, which then pushes the rate back down."),
 dict(q="A student says that when the government borrows more, the supply of loanable funds increases because the government has more money. The error is that", choices=[
   "government borrowing does not affect the market",
   "borrowing places the government on the demand side of the market, not the supply side",
   "the government is a saver",
   "supply and demand are the same curve",
   "the rate is fixed"], ans=1,
   why="A borrower demands funds; only a budget surplus would put the government on the supply side."),
 dict(q="A student says that an increase in the money supply lowers the real interest rate permanently. The more accurate statement is that it", choices=[
   "lowers the nominal rate in the short run, but in the long run the real rate is determined by saving and investment",
   "lowers the real rate permanently",
   "raises the real rate permanently",
   "has no effect on any rate",
   "raises the nominal rate immediately"], ans=0,
   why="Monetary expansion moves the nominal rate in the short run; real fundamentals anchor the real rate."),
 dict(q="The quantity of loanable funds on the horizontal axis measures", choices=[
   "the money supply",
   "the dollar volume of funds saved and borrowed per period",
   "the price level",
   "real GDP",
   "the interest rate"], ans=1,
   why="It is a flow of funds through the market, not a stock of money."),
 dict(q="A decrease in the government budget deficit, other things equal, will cause private investment to", choices=[
   "fall", "rise", "stay the same", "fall to zero", "become indeterminate"], ans=1,
   why="Less public borrowing lowers the real rate, which is crowding out working in reverse."),
 dict(q="If a country simultaneously experiences a large capital inflow and a large increase in government borrowing, the effect on the real interest rate is", choices=[
   "definitely an increase",
   "ambiguous, since supply and demand both shift right",
   "definitely a decrease",
   "definitely zero",
   "definitely unchanged"], ans=1,
   why="Both shifts raise the quantity of funds traded but move the rate in opposite directions."),
 dict(q="Which combination would unambiguously lower the real interest rate?", choices=[
   "an increase in government borrowing and a fall in saving",
   "an increase in private saving and a fall in investment demand",
   "an investment tax credit and a capital outflow",
   "a budget deficit and business optimism",
   "a fall in saving and an increase in investment demand"], ans=1,
   why="More supply and less demand both push the price of funds down."),
 dict(q="Which combination would unambiguously raise the real interest rate?", choices=[
   "an increase in saving and a fall in investment demand",
   "a larger budget deficit and a decline in private saving",
   "a capital inflow and business pessimism",
   "a budget surplus and an investment tax credit",
   "a capital inflow and a budget surplus"], ans=1,
   why="More demand for funds and less supply of them both push the rate up."),
 dict(q="Deficit-financed government spending during a period of full employment is most likely to", choices=[
   "raise real output permanently with no side effects",
   "raise the real interest rate and reduce private investment, limiting future growth in potential output",
   "lower the real interest rate",
   "increase private saving enough to offset all effects",
   "leave the loanable funds market unchanged"], ans=1,
   why="With no slack, the extra public borrowing competes directly with private borrowers for a fixed pool of saving."),
]
