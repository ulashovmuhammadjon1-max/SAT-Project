# MACRO 4.3 Definition, Measurement, and Functions of Money — 50 questions
# Aggregate classification used throughout (standard AP convention):
#   M1 = currency in circulation + checkable (demand) deposits + traveler's checks
#        + (since the 2020 redefinition) savings deposits.
#   For AP purposes the exam still tests the traditional split, so this bank uses:
#        M1 = currency + checkable deposits + traveler's checks
#        M2 = M1 + savings deposits + small time deposits (under $100,000)
#             + retail money market mutual fund shares.
#   NOT in M1 or M2: large time deposits, stocks, bonds, credit cards (not money at all),
#        gold, real estate.
# ASSETS table arithmetic, verified line by line (billions of dollars):
#   Currency in circulation            400
#   Checkable deposits                 600
#   Traveler's checks                   10
#   Savings deposits                 1,200
#   Small time deposits                500
#   Retail money market mutual funds   300
#   Large time deposits                800   <- excluded from both M1 and M2
#   M1 = 400 + 600 + 10                    = 1,010
#   M2 = 1,010 + 1,200 + 500 + 300         = 3,010
#   M2 - M1 = 1,200 + 500 + 300            = 2,000
#   Note 800 of large time deposits is in neither aggregate.
TOPIC = ("4.3", "Definition, Measurement, and Functions of Money", 4)

ASSETS = dict(
    headers=["Asset", "Amount (billions of dollars)"],
    rows=[
        ["Currency in circulation", "400"],
        ["Checkable deposits", "600"],
        ["Traveler's checks", "10"],
        ["Savings deposits", "1,200"],
        ["Small time deposits", "500"],
        ["Retail money market mutual fund shares", "300"],
        ["Large time deposits", "800"],
    ],
)

QUESTIONS = [
 dict(q="Money is best defined as", choices=[
   "currency issued by the government only",
   "any asset generally accepted in exchange for goods and services",
   "a household's total wealth",
   "income earned in a year",
   "gold and silver"], ans=1,
   why="General acceptability in exchange, not physical form, is what makes something money."),
 dict(q="The three functions of money are", choices=[
   "saving, spending, and lending",
   "medium of exchange, store of value, and unit of account",
   "currency, deposits, and credit",
   "liquidity, risk, and return",
   "M1, M2, and M3"], ans=1,
   why="These three functions define money in every AP treatment."),
 dict(q="Money serves as a medium of exchange when it", choices=[
   "measures the value of goods",
   "is accepted by sellers as payment, removing the need for barter",
   "holds purchasing power over time",
   "is deposited in a bank",
   "earns interest"], ans=1,
   why="The medium-of-exchange function is about being accepted in transactions."),
 dict(q="Money serves as a unit of account when it", choices=[
   "is used to buy goods",
   "provides a common measure in which prices and debts are quoted",
   "retains value over time",
   "is held as savings",
   "is printed by the government"], ans=1,
   why="A unit of account is the yardstick in which values are expressed."),
 dict(q="Money serves as a store of value when it", choices=[
   "is spent immediately",
   "can be held now and used to buy goods later",
   "measures prices",
   "is accepted in trade",
   "is backed by gold"], ans=1,
   why="Storing value means purchasing power carries forward through time."),
 dict(q="Which function of money is most damaged by high inflation?", choices=[
   "medium of exchange",
   "store of value",
   "unit of account only",
   "none of them",
   "all three equally"], ans=1,
   why="Rapidly rising prices destroy the purchasing power of money held over time."),
 dict(q="Posting a price of $30 on a jacket is an example of money acting as a", choices=[
   "medium of exchange", "unit of account", "store of value", "commodity money", "reserve asset"], ans=1,
   why="The price is expressed in a common measuring unit."),
 dict(q="Handing a cashier a $20 bill for groceries illustrates money as a", choices=[
   "unit of account", "medium of exchange", "store of value", "fiat backing", "financial asset only"], ans=1,
   why="Money is being used to complete the transaction itself."),
 dict(q="Keeping $500 in a drawer for an emergency next year illustrates money as a", choices=[
   "unit of account", "store of value", "medium of exchange", "barter good", "commodity"], ans=1,
   why="Purchasing power is being carried forward in time."),
 dict(q="Barter requires", choices=[
   "a common unit of account",
   "a double coincidence of wants between the two traders",
   "a central bank",
   "fiat money",
   "commercial banks"], ans=1,
   why="Without money each trader must want exactly what the other offers."),
 dict(q="The main advantage of money over barter is that money", choices=[
   "eliminates scarcity",
   "greatly lowers the transaction costs of exchange",
   "raises real output automatically",
   "prevents inflation",
   "removes the need for saving"], ans=1,
   why="Money removes the need for a double coincidence of wants, so trade is far cheaper to arrange."),
 dict(q="Commodity money is money that", choices=[
   "has value only because the government declares it legal tender",
   "consists of a good that has intrinsic value in an alternative use, such as gold",
   "is issued by commercial banks",
   "exists only as bank deposits",
   "is backed by other currencies"], ans=1,
   why="Commodity money would be valuable even if it were not used as money."),
 dict(q="Fiat money is money that", choices=[
   "is backed by a fixed quantity of gold",
   "has no intrinsic value and is money because government declares it legal tender and people accept it",
   "is made of a valuable metal",
   "is issued only by banks",
   "cannot be used for payment"], ans=1,
   why="Fiat money's value rests on acceptance and legal status, not on the material itself."),
 dict(q="A country's paper currency today is best classified as", choices=[
   "commodity money", "fiat money", "barter", "a commodity-backed money", "a financial derivative"], ans=1,
   why="Modern currencies are not redeemable for any commodity."),
 dict(q="Which of the following is an example of commodity money?", choices=[
   "a modern dollar bill",
   "cigarettes used as payment in a prison camp",
   "a checking deposit",
   "a credit card",
   "a government bond"], ans=1,
   why="The cigarettes have value in their own use apart from serving as money."),
 dict(q="Which of the following is NOT counted as money in any monetary aggregate?", choices=[
   "currency in circulation",
   "a credit card",
   "a checking deposit",
   "a savings deposit",
   "a traveler's check"], ans=1,
   why="A credit card is a way of borrowing, not an asset that can be spent."),
 dict(q="M1 consists of", choices=[
   "currency plus all bank deposits of any kind",
   "the most liquid forms of money, chiefly currency in circulation, checkable deposits, and traveler's checks",
   "savings and time deposits only",
   "government bonds",
   "the total wealth of households"], ans=1,
   why="M1 is the narrow, transaction-ready measure of money."),
 dict(q="M2 consists of", choices=[
   "only currency",
   "M1 plus savings deposits, small time deposits, and retail money market mutual fund shares",
   "M1 minus currency",
   "all financial assets including stocks",
   "government debt"], ans=1,
   why="M2 adds near-monies that are slightly less liquid than M1."),
 dict(q="Which of the following is true of M1 and M2?", choices=[
   "M1 is larger than M2",
   "Every dollar in M1 is also counted in M2",
   "They are entirely separate categories",
   "M2 excludes currency",
   "M1 includes stocks"], ans=1,
   why="M2 is defined as M1 plus additional assets, so M1 is contained in M2."),
 dict(q="Using the table, M1 equals", table=ASSETS, choices=[
   "$400 billion", "$1,000 billion", "$1,010 billion", "$2,010 billion", "$3,010 billion"], ans=2,
   why="Currency 400 plus checkable deposits 600 plus traveler's checks 10 is 1,010."),
 dict(q="Using the table, M2 equals", table=ASSETS, choices=[
   "$1,010 billion", "$2,000 billion", "$3,010 billion", "$3,810 billion", "$3,000 billion"], ans=2,
   why="M1 of 1,010 plus savings 1,200, small time deposits 500, and money market funds 300 is 3,010."),
 dict(q="Using the table, the difference between M2 and M1 is", table=ASSETS, choices=[
   "$1,000 billion", "$1,200 billion", "$2,000 billion", "$2,800 billion", "$3,010 billion"], ans=2,
   why="Savings 1,200 plus small time 500 plus money market funds 300 equals 2,000."),
 dict(q="Using the table, which item is excluded from both M1 and M2?", table=ASSETS, choices=[
   "traveler's checks",
   "large time deposits",
   "savings deposits",
   "checkable deposits",
   "retail money market mutual fund shares"], ans=1,
   why="Large time deposits are held mainly by institutions and fall outside both aggregates."),
 dict(q="Using the table, if $100 billion is shifted from checkable deposits into savings deposits, then", table=ASSETS, choices=[
   "both M1 and M2 fall",
   "M1 falls by $100 billion and M2 is unchanged",
   "M1 is unchanged and M2 falls",
   "both rise",
   "M1 rises and M2 falls"], ans=1,
   why="The funds leave the narrow aggregate but stay inside the broad one."),
 dict(q="If a household withdraws $500 in cash from its checking account, M1", choices=[
   "rises by $500",
   "is unchanged, because currency rises by the same amount checkable deposits fall",
   "falls by $500",
   "rises by $1,000",
   "falls to zero"], ans=1,
   why="Both currency and checkable deposits are inside M1, so the composition changes but not the total."),
 dict(q="If a household moves $2,000 from a savings account into a checking account, then", choices=[
   "M1 and M2 both rise",
   "M1 rises by $2,000 and M2 is unchanged",
   "M1 is unchanged and M2 rises",
   "both fall",
   "neither changes"], ans=1,
   why="The funds become part of the narrow aggregate while remaining inside the broad one."),
 dict(q="Which list ranks assets from most liquid to least liquid?", choices=[
   "a savings deposit, currency, a house",
   "currency, a savings deposit, a house",
   "a house, currency, a savings deposit",
   "a savings deposit, a house, currency",
   "a house, a savings deposit, currency"], ans=1,
   why="Cash is already spendable, savings converts quickly, and property takes months to sell."),
 dict(q="Which of the following belongs in M2 but not M1?", choices=[
   "currency in circulation",
   "a small time deposit",
   "a checkable deposit",
   "a traveler's check",
   "a corporate bond"], ans=1,
   why="Small time deposits are near-money counted only in the broader aggregate."),
 dict(q="Which of the following belongs in M1?", choices=[
   "a savings deposit under the traditional definition",
   "a checkable deposit",
   "a share of stock",
   "a large time deposit",
   "a Treasury bond"], ans=1,
   why="Checkable deposits can be spent directly and are the core of M1 besides currency."),
 dict(q="A share of corporate stock is", choices=[
   "part of M1",
   "not counted in the money supply at all",
   "part of M2 only",
   "the same as a checking deposit",
   "commodity money"], ans=1,
   why="Stocks are financial assets but not means of payment, so they are outside the aggregates."),
 dict(q="Liquidity of an asset means", choices=[
   "its rate of return",
   "the ease with which it can be converted into a medium of exchange without loss of value",
   "its riskiness",
   "the government's guarantee of it",
   "the length of time it is held"], ans=1,
   why="Money is the most liquid asset because it already is the medium of exchange."),
 dict(q="The reason M1 assets typically pay little or no interest is that", choices=[
   "the government forbids interest",
   "holders are compensated by liquidity rather than by return",
   "they are risky",
   "they are illegal to hold in quantity",
   "banks make no profit on them"], ans=1,
   why="The convenience of instant spendability is itself the return on holding money."),
 dict(q="If the public loses confidence in a fiat currency and refuses to accept it, that currency", choices=[
   "retains its value because of legal tender laws",
   "ceases to function as money regardless of its legal status",
   "becomes commodity money",
   "enters M2",
   "gains purchasing power"], ans=1,
   why="Money works only as long as people will take it in exchange."),
 dict(q="During a hyperinflation people often begin quoting prices in a foreign currency. This shows that the domestic money has lost its function as a", choices=[
   "medium of exchange only",
   "unit of account",
   "legal tender",
   "commodity money",
   "financial asset"], ans=1,
   why="When values are no longer quoted in the domestic money, its measuring function has failed."),
 dict(q="A debit card is best described as", choices=[
   "money itself",
   "a means of accessing money already in a checkable deposit",
   "a loan from the bank",
   "part of M2 but not M1",
   "commodity money"], ans=1,
   why="The card is a payment instrument; the money is the deposit balance it draws on."),
 dict(q="Which of the following would increase M1 with no change in M2?", choices=[
   "a transfer from a savings deposit to a checking deposit",
   "a new bank loan credited to a borrower's checking account",
   "a household buying a bond",
   "a shift from checking to savings",
   "a purchase of stock"], ans=0,
   why="Both accounts sit inside M2, so only the narrow measure changes."),
 dict(q="The value of fiat money ultimately rests on", choices=[
   "the gold held by the central bank",
   "confidence that others will accept it and on limited supply",
   "the paper it is printed on",
   "the interest it pays",
   "the size of the government's budget"], ans=1,
   why="Acceptance plus a controlled supply is what keeps fiat money valuable."),
 dict(q="A large and sustained increase in the money supply relative to output tends to", choices=[
   "raise the value of money",
   "reduce the purchasing power of money by raising the price level",
   "leave prices unchanged",
   "cause deflation",
   "raise real output permanently"], ans=1,
   why="More money chasing the same goods raises prices, which is the same as money buying less."),
 dict(q="The purchasing power of money is", choices=[
   "the same as the nominal money supply",
   "inversely related to the price level",
   "directly related to the price level",
   "fixed by law",
   "unrelated to inflation"], ans=1,
   why="When prices double, a unit of money buys half as much."),
 dict(q="Which of the following is the best example of near-money?", choices=[
   "a $10 bill",
   "a savings deposit",
   "a checking deposit",
   "a share of stock",
   "a house"], ans=1,
   why="A savings deposit is highly liquid but cannot be spent directly, which is what near-money means."),
 dict(q="Gold is not used as money in modern economies mainly because", choices=[
   "it has no value",
   "its supply cannot be adjusted to the needs of a growing economy and it is inconvenient to carry",
   "governments do not own any",
   "it is not durable",
   "it is not divisible"], ans=1,
   why="A commodity standard ties the money supply to the supply of the commodity."),
 dict(q="The characteristics that make a good suitable as money include", choices=[
   "high value in alternative uses only",
   "durability, portability, divisibility, uniformity, and limited supply",
   "unlimited supply",
   "perishability",
   "government ownership"], ans=1,
   why="These properties let a good circulate reliably as a means of payment."),
 dict(q="A government that prints money without limit will most likely destroy money's usefulness because", choices=[
   "money becomes too heavy",
   "the resulting inflation destroys its value as a store of value and unit of account",
   "the central bank closes",
   "banks refuse deposits",
   "output rises too quickly"], ans=1,
   why="Limited supply is essential to money retaining purchasing power."),
 dict(q="If a country's M2 is $2,000 billion and its M1 is $700 billion, then M2 minus M1 is", choices=[
   "$0", "$700 billion", "$1,300 billion", "$2,000 billion", "$2,700 billion"], ans=2,
   why="Subtracting M1 of 700 from M2 of 2,000 leaves 1,300 in near-monies."),
 dict(q="Which change would leave both M1 and M2 unchanged?", choices=[
   "a bank makes a new loan",
   "a household uses currency to buy a bond from another household",
   "a household moves funds from savings to checking",
   "the central bank buys bonds from a bank",
   "a household deposits cash in a savings account"], ans=1,
   why="The cash simply changes hands between members of the public, so no aggregate changes."),
 dict(q="Money makes specialization possible because", choices=[
   "it eliminates opportunity cost",
   "workers can sell what they produce for money and use it to buy everything else they need",
   "it raises wages",
   "it eliminates scarcity",
   "it prevents unemployment"], ans=1,
   why="Without money, a specialist would have to barter directly for every good consumed."),
 dict(q="Compared with M1, M2 is", choices=[
   "smaller and more liquid",
   "larger and, on average, less liquid",
   "identical in size",
   "smaller and less liquid",
   "larger and more liquid"], ans=1,
   why="M2 adds assets that are one step removed from being spendable."),
 dict(q="A household that keeps its wealth entirely in stocks and real estate", choices=[
   "holds a large amount of money",
   "holds almost no money, since neither asset is counted in the monetary aggregates",
   "holds only M2",
   "holds only M1",
   "holds commodity money"], ans=1,
   why="Neither asset is a means of payment, so neither is in M1 or M2."),
 dict(q="When a bank customer converts $1,000 from a checking account into a small time deposit, M2", choices=[
   "falls by $1,000",
   "is unchanged while M1 falls by $1,000",
   "rises by $1,000",
   "falls by $2,000",
   "rises while M1 rises"], ans=1,
   why="Both accounts are inside M2, so only the narrow aggregate is affected."),
 dict(q="The statement that money is whatever is generally accepted in payment implies that", choices=[
   "only government-issued paper can be money",
   "in principle a wide range of items, including cigarettes or shells, can serve as money if people accept them",
   "money must be backed by gold",
   "credit cards are money",
   "money must pay interest"], ans=1,
   why="Acceptance, not any particular physical form or legal decree, is the defining test."),
]
