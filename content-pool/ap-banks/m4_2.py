# MACRO 4.2 Nominal vs. Real Interest Rates — 50 questions
# Fisher approximation used throughout: real = nominal - inflation.
# Every numeric item worked out:
#   nominal 8, inflation 3  -> real 5
#   nominal 6, inflation 2  -> real 4
#   nominal 5, inflation 5  -> real 0
#   nominal 4, inflation 7  -> real -3
#   nominal 3, inflation 5  -> real -2
#   nominal 12, inflation 9 -> real 3
#   nominal 7, inflation -1 -> real 8   (deflation raises the real rate)
#   real 4, inflation 3     -> nominal 7
#   real 2, inflation 6     -> nominal 8
#   real 5, expected inflation 2 -> nominal 7
#   real -1, inflation 4    -> nominal 3
#   nominal 9, real 4       -> inflation 5
#   nominal 6, real -2      -> inflation 8
#   nominal 10, real 10     -> inflation 0
# Expected vs actual, using nominal 6 set on expected inflation 2 (so expected real 4):
#   actual inflation 5 -> realized real 1: borrower gains, lender loses.
#   actual inflation 0 -> realized real 6: lender gains, borrower loses.
# Exact Fisher check on one item, to confirm the approximation is close:
#   (1.08)/(1.03) - 1 = 0.04854, i.e. 4.85%, which the approximation puts at 5%.
TOPIC = ("4.2", "Nominal vs. Real Interest Rates", 4)

RATES = dict(
    headers=["Year", "Nominal interest rate", "Inflation rate"],
    rows=[
        ["2019", "6%", "2%"],
        ["2020", "5%", "5%"],
        ["2021", "4%", "7%"],
        ["2022", "9%", "4%"],
    ],
)

QUESTIONS = [
 dict(q="The nominal interest rate is", choices=[
   "the interest rate adjusted for inflation",
   "the stated rate of return in current dollars, before adjusting for inflation",
   "always equal to the real rate",
   "the rate charged only by banks",
   "the inflation rate"], ans=1,
   why="The nominal rate is the posted, unadjusted rate."),
 dict(q="The real interest rate measures", choices=[
   "the stated rate on a loan contract",
   "the rate of return in terms of purchasing power, after accounting for inflation",
   "the inflation rate itself",
   "the tax rate on interest income",
   "the rate set by the central bank"], ans=1,
   why="The real rate tells the lender how much more the money will actually buy."),
 dict(q="The approximate relationship known as the Fisher equation states that", choices=[
   "real rate = nominal rate + inflation rate",
   "real rate = nominal rate - inflation rate",
   "nominal rate = real rate - inflation rate",
   "inflation rate = real rate + nominal rate",
   "real rate = inflation rate - nominal rate"], ans=1,
   why="Subtracting inflation from the nominal rate converts a dollar return into a purchasing-power return."),
 dict(q="If the nominal interest rate is 8 percent and inflation is 3 percent, the real interest rate is", choices=[
   "3%", "5%", "8%", "11%", "24%"], ans=1,
   why="8 minus 3 is 5 percent."),
 dict(q="If the nominal interest rate is 6 percent and inflation is 2 percent, the real interest rate is", choices=[
   "2%", "3%", "4%", "6%", "8%"], ans=2,
   why="6 minus 2 is 4 percent."),
 dict(q="If the nominal interest rate is 5 percent and the inflation rate is 5 percent, the real interest rate is", choices=[
   "-5%", "0%", "5%", "10%", "25%"], ans=1,
   why="Interest exactly offsets the loss of purchasing power, so the lender gains nothing in real terms."),
 dict(q="If the nominal interest rate is 4 percent and inflation turns out to be 7 percent, the real interest rate is", choices=[
   "-3%", "0%", "3%", "7%", "11%"], ans=0,
   why="4 minus 7 is negative 3 percent, so the lender loses purchasing power."),
 dict(q="If the nominal interest rate is 3 percent and inflation is 5 percent, the real interest rate is", choices=[
   "-2%", "0%", "2%", "5%", "8%"], ans=0,
   why="Inflation exceeds the nominal rate, making the real return negative."),
 dict(q="If the nominal rate is 12 percent and inflation is 9 percent, the real rate is", choices=[
   "-3%", "0%", "3%", "9%", "21%"], ans=2,
   why="12 minus 9 is 3 percent."),
 dict(q="If the nominal interest rate is 7 percent and prices are falling at 1 percent a year, the real interest rate is", choices=[
   "-8%", "6%", "7%", "8%", "1%"], ans=3,
   why="With inflation of negative 1 percent, 7 minus (-1) equals 8 percent, so deflation raises the real rate."),
 dict(q="A lender wants a real return of 4 percent and expects inflation of 3 percent. The nominal rate the lender should charge is", choices=[
   "1%", "3%", "4%", "7%", "12%"], ans=3,
   why="The nominal rate is the desired real rate plus expected inflation, 4 plus 3."),
 dict(q="A lender requiring a 2 percent real return who expects 6 percent inflation should charge a nominal rate of", choices=[
   "2%", "4%", "6%", "8%", "12%"], ans=3,
   why="2 plus 6 equals 8 percent."),
 dict(q="If savers require a 5 percent real return and expect inflation of 2 percent, the nominal rate on loans will tend toward", choices=[
   "2%", "3%", "5%", "7%", "10%"], ans=3,
   why="Nominal equals real plus expected inflation, 5 plus 2."),
 dict(q="A bank charges a nominal rate of 3 percent when expected inflation is 4 percent. The expected real rate is", choices=[
   "-1%", "0%", "1%", "3%", "7%"], ans=0,
   why="3 minus 4 gives a negative real rate of 1 percent."),
 dict(q="If the nominal rate is 9 percent and the real rate is 4 percent, the inflation rate is", choices=[
   "-5%", "4%", "5%", "9%", "13%"], ans=2,
   why="Inflation equals nominal minus real, 9 minus 4."),
 dict(q="If the nominal rate is 6 percent and the real rate is negative 2 percent, the inflation rate is", choices=[
   "-8%", "2%", "4%", "8%", "12%"], ans=3,
   why="6 minus 8 equals negative 2, so inflation must be 8 percent."),
 dict(q="If the nominal and real interest rates are both 10 percent, the inflation rate must be", choices=[
   "-10%", "0%", "5%", "10%", "20%"], ans=1,
   why="They are equal only when inflation is zero."),
 dict(q="Using the table, the real interest rate in 2019 was", table=RATES, choices=[
   "2%", "4%", "6%", "8%", "12%"], ans=1,
   why="6 percent nominal minus 2 percent inflation is 4 percent."),
 dict(q="Using the table, in which year was the real interest rate equal to zero?", table=RATES, choices=[
   "2019", "2020", "2021", "2022", "in none of these years"], ans=1,
   why="In 2020 the nominal rate of 5 percent exactly matched inflation of 5 percent."),
 dict(q="Using the table, in which year was the real interest rate negative?", table=RATES, choices=[
   "2019", "2020", "2021", "2022", "in no year shown"], ans=2,
   why="In 2021 inflation of 7 percent exceeded the nominal rate of 4 percent, giving a real rate of negative 3 percent."),
 dict(q="Using the table, in which year was the real interest rate highest?", table=RATES, choices=[
   "2019", "2020", "2021", "2022", "2019 and 2022 were tied"], ans=3,
   why="2022's real rate of 5 percent beats 2019's 4 percent, 2020's zero, and 2021's negative 3 percent."),
 dict(q="Using the table, the year with the highest nominal rate", table=RATES, choices=[
   "also had the highest real rate",
   "had the highest real rate as well, but that need not be true in general",
   "had the lowest real rate",
   "had a zero real rate",
   "had a negative real rate"], ans=1,
   why="2022 happens to top both lists, but a high nominal rate paired with high inflation can leave the real rate low."),
 dict(q="When actual inflation turns out to be higher than expected, the group that gains is", choices=[
   "lenders",
   "borrowers, because they repay in dollars worth less than expected",
   "savers holding cash",
   "everyone equally",
   "no one"], ans=1,
   why="Unexpected inflation lowers the realized real rate, transferring purchasing power from lender to borrower."),
 dict(q="When actual inflation turns out to be lower than expected, the group that gains is", choices=[
   "borrowers",
   "lenders, because the dollars they are repaid buy more than expected",
   "workers with fixed wage contracts lose",
   "no one",
   "the government as a debtor"], ans=1,
   why="A lower-than-expected inflation rate raises the realized real return to the lender."),
 dict(q="A bank makes a loan at 6 percent expecting inflation of 2 percent. Inflation turns out to be 5 percent. The realized real interest rate is", choices=[
   "-1%", "1%", "3%", "4%", "6%"], ans=1,
   why="6 minus the actual 5 leaves 1 percent, well below the 4 percent the bank expected."),
 dict(q="A bank makes a loan at 6 percent expecting inflation of 2 percent, but prices end up unchanged. The realized real rate is", choices=[
   "0%", "2%", "4%", "6%", "8%"], ans=3,
   why="With actual inflation at zero, the entire 6 percent nominal return is real, above the expected 4 percent."),
 dict(q="A loan is written at a nominal rate of 6 percent when both parties expect 2 percent inflation, but prices end up unchanged. The party hurt is", choices=[
   "the bank",
   "the borrower, who must repay in dollars worth more than anticipated",
   "neither party",
   "both parties equally",
   "the central bank"], ans=1,
   why="The borrower pays a higher real cost than the contract was designed to impose."),
 dict(q="Nominal interest rates on new loans tend to rise when", choices=[
   "expected inflation falls",
   "expected inflation rises",
   "the real rate falls",
   "the price level is stable",
   "deflation is expected"], ans=1,
   why="Lenders add expected inflation to the real return they require."),
 dict(q="The Fisher effect refers to the tendency for", choices=[
   "real rates to move one for one with inflation",
   "nominal rates to rise roughly one for one with expected inflation, leaving the real rate unchanged",
   "inflation to fall when nominal rates rise",
   "nominal rates to be constant",
   "real rates always to be zero"], ans=1,
   why="Expected inflation is passed through into the nominal rate."),
 dict(q="If expected inflation rises from 2 percent to 6 percent and the required real rate stays at 3 percent, the nominal rate moves from", choices=[
   "5% to 9%", "3% to 6%", "5% to 3%", "2% to 6%", "9% to 5%"], ans=0,
   why="Nominal equals real plus expected inflation, so it goes from 3 plus 2 to 3 plus 6."),
 dict(q="Which rate is the one that actually determines the incentive to save and invest?", choices=[
   "the nominal rate",
   "the real rate",
   "the inflation rate",
   "the discount rate only",
   "the tax rate"], ans=1,
   why="Decisions depend on purchasing power gained or given up, which is the real rate."),
 dict(q="A country with 40 percent nominal interest rates and 45 percent inflation has a real interest rate of", choices=[
   "-5%", "0%", "5%", "40%", "85%"], ans=0,
   why="40 minus 45 is negative 5 percent, so high nominal rates do not mean a high real return."),
 dict(q="A negative real interest rate means that", choices=[
   "borrowers must repay more purchasing power than they borrowed",
   "the purchasing power of the amount repaid is less than that of the amount lent",
   "the nominal rate is negative",
   "no lending occurs",
   "inflation is zero"], ans=1,
   why="Inflation outruns the interest earned, so the lender ends up worse off in real terms."),
 dict(q="Holding cash during a period of inflation earns a real return of", choices=[
   "zero",
   "the negative of the inflation rate",
   "the nominal interest rate",
   "the inflation rate",
   "the real interest rate on bonds"], ans=1,
   why="Cash pays no nominal interest, so its real return is 0 minus inflation."),
 dict(q="A retiree living on a fixed nominal pension is harmed by unexpected inflation because", choices=[
   "the pension payment falls",
   "the same nominal payment buys fewer goods",
   "nominal interest rates fall",
   "the real interest rate rises",
   "taxes fall"], ans=1,
   why="Fixed nominal incomes lose real value when prices rise unexpectedly."),
 dict(q="Unexpected deflation redistributes purchasing power", choices=[
   "from lenders to borrowers",
   "from borrowers to lenders",
   "from workers to firms",
   "from firms to government",
   "not at all"], ans=1,
   why="Falling prices raise the real value of fixed debt repayments, helping the creditor."),
 dict(q="Which of the following would leave the real interest rate unchanged?", choices=[
   "a rise in the nominal rate from 5 to 8 percent while inflation rises from 2 to 5 percent",
   "a rise in the nominal rate from 5 to 8 percent with inflation constant",
   "a fall in inflation with the nominal rate constant",
   "a fall in the nominal rate with inflation constant",
   "a rise in inflation with the nominal rate constant"], ans=0,
   why="Both the nominal rate and inflation rise by 3 points, so the difference stays at 3 percent."),
 dict(q="If a government indexes bond payments to inflation, the bondholder is protected because", choices=[
   "the nominal payment is fixed",
   "the payments adjust with the price level, fixing the real return",
   "inflation is eliminated",
   "the bond never matures",
   "taxes are removed"], ans=1,
   why="Indexing removes the risk that unexpected inflation erodes the real return."),
 dict(q="An economy has a nominal interest rate of 2 percent and inflation of 6 percent. A saver who leaves money in a bank account for a year will find that the money", choices=[
   "buys 8 percent more goods",
   "buys about 4 percent fewer goods",
   "buys 2 percent more goods",
   "buys the same amount of goods",
   "buys 6 percent more goods"], ans=1,
   why="The real return of negative 4 percent is the loss in purchasing power."),
 dict(q="Which of the following is measured in units of purchasing power rather than dollars?", choices=[
   "the nominal wage",
   "the real interest rate",
   "the nominal interest rate",
   "the dollar value of a loan",
   "the face value of a bond"], ans=1,
   why="Real variables are adjusted for the price level."),
 dict(q="A loan contract can only specify the nominal rate because", choices=[
   "real rates are illegal",
   "future inflation is not known when the contract is signed",
   "real rates never change",
   "banks prefer nominal rates",
   "inflation is always zero"], ans=1,
   why="The realized real rate can only be computed after inflation is observed."),
 dict(q="The expected real interest rate differs from the realized real interest rate whenever", choices=[
   "the nominal rate changes",
   "actual inflation differs from expected inflation",
   "the loan is repaid early",
   "the borrower defaults",
   "taxes change"], ans=1,
   why="The gap between the two real rates is exactly the inflation forecast error."),
 dict(q="Suppose everyone correctly anticipates inflation of 10 percent. In that case inflation", choices=[
   "redistributes wealth massively from lenders to borrowers",
   "is built into nominal contracts, so it causes little redistribution between lenders and borrowers",
   "makes real rates negative",
   "raises real output permanently",
   "eliminates the difference between real and nominal rates"], ans=1,
   why="Fully anticipated inflation is priced into the nominal rate ahead of time."),
 dict(q="If nominal interest rates are unchanged but expected inflation rises, the expected real interest rate", choices=[
   "rises", "falls", "is unchanged", "becomes zero", "equals the nominal rate"], ans=1,
   why="A larger amount is subtracted from an unchanged nominal rate."),
 dict(q="A firm deciding whether to borrow to buy machinery should compare the expected return on the machine with", choices=[
   "the inflation rate",
   "the real interest rate on the loan",
   "the nominal wage",
   "the nominal rate without adjustment",
   "the tax rate"], ans=1,
   why="Both the machine's return and the cost of funds must be measured in purchasing power."),
 dict(q="Over a decade in which inflation averaged 3 percent and nominal rates averaged 3 percent, savers", choices=[
   "roughly doubled their purchasing power",
   "earned essentially no gain in purchasing power",
   "lost half their purchasing power",
   "earned a 6 percent real return",
   "earned a 3 percent real return"], ans=1,
   why="A zero real rate means interest just offsets rising prices."),
 dict(q="Which of the following statements is correct?", choices=[
   "The nominal rate can never be below the real rate",
   "The nominal rate is below the real rate whenever there is deflation",
   "The real rate can never be negative",
   "The nominal rate can be negative but the real rate cannot",
   "The two rates are always equal"], ans=1,
   why="Negative inflation means subtracting a negative number, putting the real rate above the nominal rate."),
 dict(q="A borrower with a fixed-rate mortgage benefits most from", choices=[
   "unexpectedly low inflation",
   "unexpectedly high inflation",
   "a fall in the nominal rate on new loans",
   "deflation",
   "an increase in the real rate"], ans=1,
   why="Higher-than-expected inflation shrinks the real burden of the fixed payments."),
 dict(q="Suppose the nominal rate is 7 percent, expected inflation is 3 percent, and actual inflation is 3 percent. Then", choices=[
   "the lender gained at the borrower's expense",
   "the expected and realized real rates are both 4 percent, so no unexpected redistribution occurred",
   "the borrower gained",
   "the real rate was negative",
   "the nominal rate must adjust"], ans=1,
   why="When the forecast is exactly right, the contract delivers the real return both parties planned on."),
 dict(q="Nominal interest rates in a country experiencing hyperinflation are typically very high because", choices=[
   "the real rate is very high",
   "lenders demand compensation for the rapid loss of purchasing power",
   "the central bank forbids lending",
   "the government subsidizes lending",
   "everyone saves more"], ans=1,
   why="Enormous expected inflation is added on top of whatever real return lenders require."),
]
