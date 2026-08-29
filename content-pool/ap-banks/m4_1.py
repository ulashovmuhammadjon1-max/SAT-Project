# MACRO 4.1 Financial Assets — 50 questions
# Bond arithmetic verified line by line:
#   Bond A: face $1,000, fixed coupon $50/yr => coupon rate 5.0%.
#     If market rate rises to 10%, price that yields $50 forever = 50/0.10 = $500.
#     If market rate falls to 4%, price = 50/0.04 = $1,250.
#     If market rate = 5%, price = 50/0.05 = $1,000 (par).
#   Bond B: face $1,000, coupon $80/yr => coupon rate 8.0%.
#     Market rate 8% => 80/0.08 = $1,000 (par).
#     Market rate 16% => 80/0.16 = $500.
#     Market rate 6.4% => 80/0.064 = $1,250.
#   One-year zero-coupon bill paying $1,000 in one year:
#     price $950 => return = 50/950 = 5.263%, rounds to about 5.3%.
#     price $900 => return = 100/900 = 11.11%, rounds to about 11.1%.
#     price $980 => return = 20/980 = 2.04%, rounds to about 2.0%.
#   Current yield of a $1,000-face, $60-coupon bond selling for $1,200:
#     60/1200 = 5.0%, below the 6% coupon rate, as it must be at a premium.
#   Current yield of the same bond selling for $800: 60/800 = 7.5%, above 6%.
# Liquidity ranking used throughout (most to least liquid):
#   cash > checking deposit > savings deposit > publicly traded stock/bond > real estate.
TOPIC = ("4.1", "Financial Assets", 4)

BONDS = dict(
    headers=["Bond", "Face value", "Annual coupon payment", "Coupon rate"],
    rows=[
        ["Bond A", "$1,000", "$50", "5%"],
        ["Bond B", "$1,000", "$80", "8%"],
        ["Bond C", "$1,000", "$100", "10%"],
    ],
)

QUESTIONS = [
 dict(q="A financial asset is best described as", choices=[
   "a physical good used in production",
   "a claim on the future income or wealth of the issuer",
   "a natural resource owned by a household",
   "any good that is durable",
   "the money value of a factory"], ans=1,
   why="Financial assets such as stocks and bonds are paper claims, not physical capital."),
 dict(q="When a household buys a corporate bond, the household becomes", choices=[
   "a part owner of the corporation",
   "a lender to the corporation",
   "an employee of the corporation",
   "a customer of the corporation",
   "a director of the corporation"], ans=1,
   why="A bond is debt, so the buyer is a creditor entitled to interest and repayment of principal."),
 dict(q="When a household buys shares of stock, the household becomes", choices=[
   "a creditor of the firm",
   "a part owner of the firm with a claim on its profits",
   "a guaranteed recipient of fixed interest",
   "legally responsible for the firm's debts",
   "a bondholder"], ans=1,
   why="Stock is equity: an ownership share whose return depends on the firm's profits."),
 dict(q="Which of the following is the most important difference between a stock and a bond?", choices=[
   "Bonds can be sold and stocks cannot",
   "A bond represents debt with a promised payment, while a stock represents ownership with no promised payment",
   "Stocks are issued by governments and bonds by firms",
   "Bonds are always riskier than stocks",
   "Stocks pay interest and bonds pay dividends"], ans=1,
   why="Debt carries a contractual payment; equity carries a residual claim on profits."),
 dict(q="If a bond's market price rises, its interest rate, or yield,", choices=[
   "rises", "falls", "is unchanged", "becomes zero", "becomes negative"], ans=1,
   why="The fixed coupon is divided by a larger price, so the yield falls; price and yield move in opposite directions."),
 dict(q="A rise in market interest rates causes the prices of previously issued bonds to", choices=[
   "rise", "fall", "stay the same", "rise then fall to the original level", "become undefined"], ans=1,
   why="Old bonds with lower fixed coupons are only attractive at a lower price once new bonds pay more."),
 dict(q="Bond A has a face value of $1,000 and pays a fixed coupon of $50 per year. If the market interest rate on comparable bonds is 10 percent, Bond A will sell for approximately", choices=[
   "$400", "$500", "$1,000", "$1,250", "$2,000"], ans=1,
   why="A price of $500 makes the $50 coupon a 10 percent return, matching the market rate."),
 dict(q="A bond paying a fixed $50 coupon each year on a face value of $1,000 is outstanding. If the market interest rate falls to 4 percent, Bond A will sell for approximately", choices=[
   "$500", "$800", "$1,000", "$1,250", "$1,500"], ans=3,
   why="At $1,250 the $50 coupon is a 4 percent return, so the price must rise until the yield matches the market."),
 dict(q="A bond with a face value of $1,000 and a coupon of $80 per year sells at par when the market interest rate equals", choices=[
   "4%", "5%", "6%", "8%", "10%"], ans=3,
   why="A bond sells at face value exactly when its coupon rate equals the market rate, here 80/1,000 = 8 percent."),
 dict(q="A one-year bill promises to pay $1,000 in one year and currently sells for $950. Its rate of return is approximately", choices=[
   "2.0%", "5.0%", "5.3%", "9.5%", "10.5%"], ans=2,
   why="The $50 gain divided by the $950 paid is 5.26 percent."),
 dict(q="A one-year bill promising $1,000 sells for $900. Its rate of return is approximately", choices=[
   "5.0%", "9.0%", "10.0%", "11.1%", "20.0%"], ans=3,
   why="A $100 gain on a $900 outlay is 11.1 percent."),
 dict(q="A one-year bill promising $1,000 in one year sells for $980. Compared with a similar bill selling for $950, the $980 bill offers", choices=[
   "a higher rate of return",
   "a lower rate of return",
   "the same rate of return",
   "a return that cannot be compared",
   "a negative return"], ans=1,
   why="Paying more for the same $1,000 payoff means a smaller percentage gain."),
 dict(q="A $1,000-face bond paying a $60 annual coupon currently sells for $1,200. Its current yield is", choices=[
   "3.0%", "5.0%", "6.0%", "7.5%", "12.0%"], ans=1,
   why="The current yield is the coupon divided by the price, 60/1,200 = 5 percent."),
 dict(q="A $1,000-face bond paying a $60 annual coupon currently sells for $800. Its current yield is", choices=[
   "4.8%", "6.0%", "7.5%", "8.0%", "13.3%"], ans=2,
   why="60 divided by 800 is 7.5 percent, above the coupon rate because the bond sells at a discount."),
 dict(q="A bond selling above its face value is said to sell at a premium. This happens when the market interest rate is", choices=[
   "above the bond's coupon rate",
   "below the bond's coupon rate",
   "equal to the bond's coupon rate",
   "zero",
   "negative"], ans=1,
   why="A coupon that is generous relative to current rates bids the price above par."),
 dict(q="A bond selling below its face value sells at a discount, which occurs when the market interest rate is", choices=[
   "below the coupon rate",
   "above the coupon rate",
   "equal to the coupon rate",
   "irrelevant to the price",
   "fixed by the issuer"], ans=1,
   why="A coupon that is stingy relative to current rates pushes the price below par."),
 dict(q="Using the table, if the market interest rate is 10 percent, which bond sells at par?", table=BONDS, choices=[
   "Bond A", "Bond B", "Bond C", "all three", "none of them"], ans=2,
   why="Bond C's coupon rate of 10 percent equals the market rate, so its price equals face value."),
 dict(q="Using the table, if the market interest rate is 10 percent, Bond A and Bond B will both sell", table=BONDS, choices=[
   "at par", "at a discount", "at a premium", "at zero", "above face value"], ans=1,
   why="Their coupon rates of 5 and 8 percent are below the market rate, so both must sell below face value."),
 dict(q="Using the table, if the market interest rate falls to 3 percent, all three bonds will sell", table=BONDS, choices=[
   "below face value",
   "above face value",
   "at exactly face value",
   "at prices that cannot be determined",
   "at zero"], ans=1,
   why="Every coupon rate in the table exceeds 3 percent, so all three bonds trade at a premium."),
 dict(q="Liquidity refers to", choices=[
   "the profitability of an asset",
   "how quickly and cheaply an asset can be converted into cash without losing value",
   "the riskiness of an asset",
   "the length of time until an asset matures",
   "the interest an asset pays"], ans=1,
   why="Liquidity is about ease of conversion into a means of payment, not about return."),
 dict(q="Which of the following assets is the most liquid?", choices=[
   "a house",
   "currency in a wallet",
   "a share of stock",
   "a certificate of deposit with a three-year term",
   "a small business owned by a household"], ans=1,
   why="Cash is already the medium of exchange, so no conversion is needed."),
 dict(q="Which of the following assets is the least liquid?", choices=[
   "a checking deposit",
   "an apartment building",
   "a savings deposit",
   "a Treasury bill",
   "a widely traded corporate stock"], ans=1,
   why="Real estate takes months to sell and involves large transaction costs."),
 dict(q="Compared with a savings account, a share of stock is generally", choices=[
   "less risky and lower yielding",
   "riskier with a higher expected return",
   "equally risky",
   "guaranteed by the government",
   "more liquid"], ans=1,
   why="Investors require compensation for bearing greater risk, which is the risk-return trade-off."),
 dict(q="The risk-return trade-off states that assets with higher expected returns generally", choices=[
   "are safer",
   "carry greater risk",
   "are more liquid",
   "are issued by governments",
   "have shorter maturities"], ans=1,
   why="Savers must be paid a premium to hold assets whose payoffs are uncertain."),
 dict(q="Government bonds of a stable country typically pay lower interest rates than corporate bonds because they", choices=[
   "have longer maturities",
   "carry less default risk",
   "are less liquid",
   "pay no coupon",
   "are exempt from all markets"], ans=1,
   why="Lower default risk means lenders accept a lower return."),
 dict(q="If investors suddenly regard a company as more likely to default, the interest rate on its newly issued bonds will", choices=[
   "fall", "rise", "stay the same", "become zero", "be set by the government"], ans=1,
   why="Greater default risk requires a higher promised return to attract lenders."),
 dict(q="A bank deposit differs from a stock in that a bank deposit", choices=[
   "offers ownership of the bank",
   "has a fixed nominal value and is typically insured, making it far less risky",
   "pays a higher expected return",
   "cannot be withdrawn",
   "is less liquid"], ans=1,
   why="A deposit is a safe, liquid, low-return claim; a stock is a risky ownership claim."),
 dict(q="The present value of a future payment falls when", choices=[
   "the interest rate falls",
   "the interest rate rises",
   "the payment is received sooner",
   "inflation is zero",
   "the payment increases"], ans=1,
   why="A higher discount rate means less must be set aside today to reach the same future sum."),
 dict(q="Interest rates and bond prices are said to be inversely related. The reason is that", choices=[
   "bond issuers change the coupon when rates change",
   "the coupon payment is fixed, so only the price can adjust to bring the yield in line with the market",
   "governments regulate bond prices",
   "bonds are riskier than stocks",
   "bond buyers are irrational"], ans=1,
   why="With the payment stream contractually fixed, the price is the only variable left to move."),
 dict(q="An investor holding long-term bonds will suffer a capital loss if", choices=[
   "interest rates fall",
   "interest rates rise",
   "inflation is zero",
   "the issuer repays on time",
   "the coupon is paid"], ans=1,
   why="Rising rates push down the market price of bonds already held."),
 dict(q="Diversification reduces risk because", choices=[
   "it raises the expected return of every asset",
   "losses on some assets tend to be offset by gains on others",
   "it eliminates all risk",
   "it makes assets more liquid",
   "governments insure diversified portfolios"], ans=1,
   why="Holding many imperfectly correlated assets smooths the portfolio's overall return."),
 dict(q="Which statement about diversification is correct?", choices=[
   "It eliminates all risk from a portfolio",
   "It reduces risk that is specific to individual firms but not risk affecting the whole economy",
   "It raises risk",
   "It applies only to bonds",
   "It guarantees a positive return"], ans=1,
   why="Economy-wide shocks hit every asset, so they cannot be diversified away."),
 dict(q="A dividend is", choices=[
   "the interest paid on a bond",
   "a share of a corporation's profits paid out to its shareholders",
   "the face value of a bond",
   "a tax on financial assets",
   "the price of a share"], ans=1,
   why="Dividends are the equity holder's share of profits, and they are not contractually guaranteed."),
 dict(q="The face value of a bond is", choices=[
   "the price the bond sells for today",
   "the amount the issuer repays at maturity",
   "the annual coupon payment",
   "the yield on the bond",
   "the market interest rate"], ans=1,
   why="Face value, or par value, is the principal returned at maturity, which does not change with market prices."),
 dict(q="An increase in the overall demand for bonds, holding the supply of bonds constant, will", choices=[
   "raise bond prices and lower interest rates",
   "lower bond prices and raise interest rates",
   "raise both bond prices and interest rates",
   "lower both",
   "leave both unchanged"], ans=0,
   why="More buyers bid prices up, and a higher price on a fixed coupon means a lower yield."),
 dict(q="If firms and governments issue a much larger volume of new bonds while demand is unchanged, bond prices will", choices=[
   "rise and interest rates will fall",
   "fall and interest rates will rise",
   "stay constant",
   "rise along with interest rates",
   "become indeterminate"], ans=1,
   why="A greater supply of bonds lowers their price, which is the same thing as a higher interest rate."),
 dict(q="Which of the following is a financial asset rather than a physical asset?", choices=[
   "a delivery truck",
   "a corporate bond",
   "an office building",
   "a stock of raw materials",
   "a factory machine"], ans=1,
   why="A bond is a paper claim on future payments, not a productive good."),
 dict(q="A certificate of deposit typically pays a higher interest rate than a checking account because", choices=[
   "it is riskier in terms of default",
   "the depositor gives up liquidity by committing the funds for a fixed term",
   "it is not insured",
   "banks are required to pay more on it",
   "it is a form of equity"], ans=1,
   why="Savers must be compensated for tying money up, which is a liquidity premium."),
 dict(q="A firm that wants to raise funds without taking on an obligation to make fixed payments would prefer to", choices=[
   "issue bonds",
   "issue new shares of stock",
   "borrow from a bank",
   "issue commercial paper",
   "take out a mortgage"], ans=1,
   why="Equity carries no contractual repayment, so it does not create fixed financial obligations."),
 dict(q="Which of the following best explains why a 30-year bond's price is more sensitive to interest rate changes than a 1-year bond's price?", choices=[
   "long bonds pay no coupon",
   "the fixed payments on a long bond are locked in for many more years, so a change in rates affects a longer stream",
   "long bonds are riskier borrowers",
   "short bonds are illiquid",
   "long bonds have larger face values"], ans=1,
   why="More years of mispriced payments means a larger price adjustment."),
 dict(q="If a saver expects interest rates to fall sharply next year, the saver would most want to hold", choices=[
   "cash",
   "long-term bonds purchased today",
   "a short-term bill",
   "a checking deposit",
   "no assets at all"], ans=1,
   why="Falling rates raise bond prices, producing a capital gain for someone holding long bonds."),
 dict(q="The interest rate on a bond can be thought of as", choices=[
   "the price of the bond",
   "the return a lender earns for giving up the use of funds and bearing risk",
   "the face value of the bond",
   "the coupon payment in dollars",
   "the tax on the transaction"], ans=1,
   why="Interest is the payment for the use of funds over time plus compensation for risk."),
 dict(q="Which of the following would most likely raise the interest rate a firm must offer on new bonds?", choices=[
   "a credit rating upgrade",
   "a downgrade of the firm's credit rating",
   "a fall in economy-wide interest rates",
   "an increase in the firm's profits",
   "greater liquidity in the market for its bonds"], ans=1,
   why="A downgrade signals higher default risk, so lenders demand more."),
 dict(q="Two bonds are identical except that one is far more actively traded. The actively traded bond will generally offer", choices=[
   "a higher interest rate",
   "a lower interest rate",
   "the same interest rate",
   "no interest",
   "a variable coupon"], ans=1,
   why="Greater liquidity is valuable to holders, so they accept a lower yield for it."),
 dict(q="Suppose you own a bond paying $50 a year and market interest rates jump from 5 percent to 10 percent. The most accurate description of your position is that", choices=[
   "your coupon payments will double",
   "your coupon payments are unchanged but the resale price of your bond has fallen by roughly half",
   "your bond is now worthless",
   "the issuer must repay you immediately",
   "your bond now pays 10 percent"], ans=1,
   why="The contract fixes the payment, so the entire adjustment shows up in the market price."),
 dict(q="Which of the following pairs correctly ranks assets from most to least liquid?", choices=[
   "real estate, cash, checking deposit",
   "cash, checking deposit, real estate",
   "checking deposit, real estate, cash",
   "real estate, checking deposit, cash",
   "cash, real estate, checking deposit"], ans=1,
   why="Cash is the medium of exchange, deposits convert instantly, and property takes months to sell."),
 dict(q="A saver who most values safety of principal and immediate access to funds should choose", choices=[
   "shares of a start-up company",
   "an insured savings deposit",
   "a long-term corporate bond",
   "a rental property",
   "a collection of art"], ans=1,
   why="An insured deposit combines low risk with high liquidity, at the cost of a low return."),
 dict(q="Financial markets contribute to economic growth mainly because they", choices=[
   "print money",
   "channel the savings of households into productive investment by firms",
   "eliminate risk",
   "set the price level",
   "guarantee full employment"], ans=1,
   why="Intermediation moves funds from savers to the investors who can use them productively."),
 dict(q="If the price of a $1,000-face bond with a $50 coupon rises from $1,000 to $1,250, the yield on the bond has moved from", choices=[
   "4% to 5%", "5% to 4%", "5% to 6.25%", "6.25% to 5%", "5% to 5%"], ans=1,
   why="50/1,000 is 5 percent and 50/1,250 is 4 percent, so the higher price means the lower yield."),
 dict(q="A student claims that when interest rates rise, bondholders are better off because their bonds now pay more. This reasoning is wrong because", choices=[
   "interest rates never rise",
   "the coupon on an existing bond is fixed, so higher rates only reduce the bond's market value",
   "bondholders receive dividends instead",
   "issuers must raise the coupon by law",
   "the face value falls"], ans=1,
   why="Only newly issued bonds carry the higher rate; existing holders take a capital loss."),
]
