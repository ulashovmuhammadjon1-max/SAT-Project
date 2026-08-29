# MACRO 2.1 The Circular Flow and GDP — 50 questions
# Table verified (GDP1, billions of dollars):
#   C = 7,000 ; I = 1,800 ; G = 2,200 ; X = 900 ; M = 1,300
#   Net exports  = X - M = 900 - 1,300 = -400
#   GDP = C + I + G + (X - M) = 7,000 + 1,800 + 2,200 - 400 = 10,600
#   Consumption share = 7,000 / 10,600 = 0.6604 = 66.0%
#   Investment share  = 1,800 / 10,600 = 0.1698 = 17.0%
#   If imports rose to 1,500: NX = 900 - 1,500 = -600, GDP = 11,000 - 600 = 10,400
#   If exports rose to 1,400: NX = 1,400 - 1,300 = +100, GDP = 11,000 + 100 = 11,100
#   C + I + G alone = 11,000
TOPIC = ("2.1", "The Circular Flow and GDP", 2)

GDP1 = dict(headers=["Component", "Amount (billions of $)"],
            rows=[["Consumption", "7,000"],
                  ["Investment", "1,800"],
                  ["Government purchases", "2,200"],
                  ["Exports", "900"],
                  ["Imports", "1,300"]])

QUESTIONS = [
 dict(q="Gross domestic product is best defined as", choices=[
   "the total money supply of a nation",
   "the market value of all final goods and services produced within a country in a given period",
   "the total value of everything bought and sold in a country",
   "the sum of all incomes earned by a country's citizens anywhere in the world",
   "the total wealth accumulated by a country"], ans=1,
   why="GDP counts final production inside a country's borders during one period, valued at market prices."),
 dict(q="GDP is measured within a country's borders regardless of who owns the resources, which means output produced in the United States by a Japanese-owned factory is", choices=[
   "excluded from U.S. GDP and included in Japan's GDP",
   "included in U.S. GDP",
   "excluded from both countries' GDP",
   "counted at half its value in each country",
   "included only if the profits stay in the United States"], ans=1,
   why="GDP is a location-based measure, so production physically occurring in the United States is U.S. GDP."),
 dict(q="The expenditure approach calculates GDP as", choices=[
   "wages + rent + interest + profit",
   "C + I + G + (X − M)",
   "C + S + T",
   "consumption + saving",
   "the sum of all business revenues"], ans=1,
   why="The expenditure approach adds up spending on final output by the four sectors, subtracting imports."),
 dict(q="The income approach calculates GDP by summing", choices=[
   "consumption, investment, government spending, and net exports",
   "wages, rents, interest, and profits earned in producing output",
   "taxes and transfer payments",
   "the value of all goods sold, including used goods",
   "household saving and business borrowing"], ans=1,
   why="Every dollar spent on output becomes income to some factor of production, so summing factor incomes gives the same total."),
 dict(q="The reason the expenditure approach and the income approach yield the same GDP figure is that", choices=[
   "both use the same price index",
   "one person's spending on output is another person's income from producing it",
   "governments require the two totals to match",
   "imports are ignored in both",
   "both exclude investment"], ans=1,
   why="Expenditure on final output is distributed entirely as factor income, so the two flows are two sides of one transaction."),
 dict(q="In the circular flow model, households", choices=[
   "purchase factors of production in the resource market",
   "supply factors of production in the resource market and buy goods in the product market",
   "produce all final goods",
   "supply goods in the product market",
   "neither earn nor spend income"], ans=1,
   why="Households own the resources and sell them to firms, then spend the resulting income on output."),
 dict(q="Within the circular flow, a business firm is best described as an economic unit that", choices=[
   "sell labor to households",
   "buy resources in the factor market and sell goods and services in the product market",
   "collect taxes",
   "supply land and labor",
   "are the ultimate owners of the factors of production"], ans=1,
   why="Firms are buyers in factor markets and sellers in product markets."),
 dict(q="In the circular flow model, the flow of wages, rent, interest, and profit from firms to households moves through the", choices=[
   "product market", "resource market", "financial market", "foreign sector", "government sector"], ans=1,
   why="Payments for factors of production flow through the resource (factor) market."),
 dict(q="A leakage from the circular flow is", choices=[
   "investment spending", "household saving", "government purchases", "export sales", "consumption spending"], ans=1,
   why="Saving is income received but not spent on domestic output, so it leaves the spending stream."),
 dict(q="Which of the following is an injection into the circular flow?", choices=[
   "taxes", "investment spending by firms", "saving", "spending on imports", "loan repayments"], ans=1,
   why="Investment adds spending on domestic output that did not come from household consumption."),
 dict(q="In the expenditure approach, the letter C refers to", choices=[
   "corporate profits",
   "household spending on goods and services, including durables, nondurables, and services",
   "capital goods purchased by firms",
   "the capital stock",
   "government consumption"], ans=1,
   why="C is personal consumption expenditure by households."),
 dict(q="In the expenditure approach, investment (I) includes all of the following EXCEPT", choices=[
   "business purchases of new equipment",
   "the purchase of 100 shares of corporate stock",
   "construction of new residential housing",
   "changes in business inventories",
   "construction of a new factory"], ans=1,
   why="Buying stock transfers ownership of an existing asset and produces nothing, so it is a financial transaction rather than investment in the GDP sense."),
 dict(q="Newly built residential housing is counted in GDP as", choices=[
   "consumption", "investment", "government purchases", "net exports", "it is not counted"], ans=1,
   why="New home construction is classified as fixed investment, not consumption."),
 dict(q="Unsold goods that a firm produces this year and adds to its inventory are", choices=[
   "excluded from GDP until they are sold",
   "counted in this year's GDP as inventory investment",
   "counted as consumption",
   "counted as an intermediate good",
   "subtracted from GDP"], ans=1,
   why="GDP measures production, so goods produced but unsold are counted as inventory investment in the year they are made."),
 dict(q="Government purchases (G) in the expenditure approach include", choices=[
   "Social Security payments to retirees",
   "the salary of a public school teacher",
   "unemployment insurance benefits",
   "interest paid on the national debt",
   "welfare payments to low-income families"], ans=1,
   why="G counts government spending that buys currently produced goods and services; the others are transfers that buy no output."),
 dict(q="Transfer payments are excluded from GDP because", choices=[
   "they are illegal",
   "no good or service is produced in exchange for them",
   "they are too small to matter",
   "they are made by state rather than federal government",
   "recipients save all of the money"], ans=1,
   why="A transfer redistributes income without any corresponding production."),
 dict(q="Net exports equal", choices=[
   "exports plus imports", "exports minus imports", "imports minus exports", "total trade volume", "the trade surplus plus the budget deficit"], ans=1,
   why="Net exports are X − M, and they are negative when imports exceed exports."),
 dict(q="Imports are subtracted in the expenditure approach because", choices=[
   "they reduce a nation's welfare",
   "spending on imports is already included in C, I, and G but represents foreign, not domestic, production",
   "they are financial transactions",
   "they are intermediate goods",
   "the government taxes them"], ans=1,
   why="Subtracting M removes foreign-produced output that was captured in the other spending categories."),
 dict(q="A country with exports of $500 billion and imports of $650 billion has net exports of", choices=[
   "-$1,150 billion", "-$150 billion", "$150 billion", "$650 billion", "$1,150 billion"], ans=1,
   why="X − M = 500 − 650 = −150 billion, a trade deficit."),
 dict(q="Which of the following is included in this year's GDP?", choices=[
   "the sale of a house built in 1998",
   "a haircut purchased this year",
   "the sale of a used car",
   "a grandmother's gift of $500 to her grandson",
   "the purchase of a government bond"], ans=1,
   why="The haircut is a final service produced this year; the others involve existing goods or pure transfers of money."),
 dict(q="The sale of a used textbook is excluded from this year's GDP because", choices=[
   "textbooks are intermediate goods",
   "the book was counted in GDP in the year it was produced, and no new production occurs in the resale",
   "students are not consumers",
   "the sale is illegal",
   "the price is too low"], ans=1,
   why="GDP counts current production, and a resale simply transfers an already-counted good."),
 dict(q="An intermediate good is", choices=[
   "a good of average quality",
   "a good purchased for use as an input in producing another good for resale",
   "a good sold to a foreign buyer",
   "any good bought by a firm",
   "a good that is bought and immediately resold unchanged"], ans=1,
   why="Intermediate goods are inputs whose value is embodied in the final good's price."),
 dict(q="Intermediate goods are excluded from GDP to avoid", choices=[
   "understating output", "double counting", "inflation", "measurement of services", "counting government spending twice"], ans=1,
   why="The value of an input is already contained in the price of the final good it becomes part of."),
 dict(q="A tire manufacturer sells tires to an automaker, which installs them on a new car sold to a household. The tires are", choices=[
   "counted separately in GDP at their sale price to the automaker",
   "an intermediate good whose value is captured in the price of the car",
   "excluded from the economy entirely",
   "counted as investment by the household",
   "counted as net exports"], ans=1,
   why="Counting both the tires and the finished car would double count the same production."),
 dict(q="Tires sold directly to a car owner as replacements are", choices=[
   "an intermediate good",
   "a final good counted in consumption",
   "excluded from GDP",
   "counted as investment",
   "counted as government purchases"], ans=1,
   why="Whether a good is intermediate or final depends on the use, and a replacement tire is bought for final use."),
 dict(q="The value-added approach measures GDP by summing", choices=[
   "the sale prices of all goods at every stage of production",
   "the difference between each firm's sales and the cost of the inputs it purchased from other firms",
   "wages only",
   "final consumption spending only",
   "government tax receipts"], ans=1,
   why="Adding value added at each stage totals exactly the value of final output without double counting."),
 dict(q="A farmer sells wheat to a miller for $2, the miller sells flour to a baker for $5, and the baker sells bread to consumers for $9. The contribution to GDP is", choices=[
   "$2", "$7", "$9", "$14", "$16"], ans=2,
   why="Only the $9 final sale counts, which also equals value added of $2 + $3 + $4."),
 dict(q="In the previous chain, the miller's value added is", choices=[
   "$2", "$3", "$5", "$7", "$9"], ans=1,
   why="Value added is the miller's $5 sales minus the $2 of wheat purchased."),
 dict(q="Household production, such as a parent caring for their own children, is excluded from GDP because", choices=[
   "it has no value",
   "no market transaction occurs, so there is no market price to record",
   "it is illegal",
   "it is an intermediate service",
   "children are not consumers"], ans=1,
   why="GDP records output that passes through markets at observable prices."),
 dict(q="If a man who has been paying a housekeeper $20,000 a year marries her and she continues the same work without pay, measured GDP will", choices=[
   "rise by $20,000", "fall by $20,000", "be unchanged", "rise by more than $20,000", "become negative"], ans=1,
   why="The same services now occur outside the market, so the transaction disappears from GDP even though output has not changed."),
 dict(q="Illegal activities such as drug sales are excluded from official GDP mainly because", choices=[
   "they produce nothing of value",
   "the transactions are unreported and therefore unmeasurable",
   "they are intermediate goods",
   "they involve no money",
   "they are counted as transfers"], ans=1,
   why="These transactions are hidden from statistical agencies, not simply judged unworthy of counting."),
 dict(q="The purchase of a newly issued corporate bond is excluded from GDP because", choices=[
   "bonds are imports",
   "it is a financial transaction that transfers funds rather than purchasing current output",
   "the interest is taxed",
   "it is an intermediate good",
   "it counts as a transfer payment by the firm"], ans=1,
   why="No good or service is produced by the exchange of a financial asset for money."),
 dict(q="A real estate agent's commission on the sale of a 40-year-old house is", choices=[
   "excluded from GDP because the house is old",
   "included in GDP because the brokerage service is produced this year",
   "counted as investment in the house",
   "counted as a transfer payment",
   "subtracted from GDP"], ans=1,
   why="The house itself is not counted again, but the current-year service of arranging the sale is."),
 dict(q="Which of the following would be counted in U.S. GDP?", choices=[
   "the pension check received by a retired postal worker",
   "a new commercial airliner built in Washington State and sold to a German airline",
   "the resale of a 2015 pickup truck",
   "a Mexican worker's wages earned in Mexico City for a U.S. firm's subsidiary",
   "shares of stock bought by a U.S. household"], ans=1,
   why="The airliner is current final production inside the United States, and as an export it enters GDP through X."),
 dict(q="A U.S. household buys a $30,000 automobile assembled entirely in South Korea. The effect on U.S. GDP is", choices=[
   "an increase of $30,000",
   "no net change, because consumption rises by $30,000 and imports rise by $30,000",
   "a decrease of $30,000",
   "an increase of $60,000",
   "a decrease of $60,000"], ans=1,
   why="The import subtraction exactly offsets the consumption entry, which is why imports never reduce measured GDP on their own."),
 dict(q="Gross national product (GNP) differs from GDP in that GNP measures output produced by", choices=[
   "domestic firms only, wherever located, but excluding foreign-owned production abroad",
   "a country's residents and firms wherever in the world it is produced",
   "the government sector only",
   "final goods only",
   "the private sector only"], ans=1,
   why="GNP is ownership-based, while GDP is location-based."),
 dict(q="If a country's residents earn a great deal of income abroad while relatively little domestic production is foreign owned, then", choices=[
   "GDP exceeds GNP", "GNP exceeds GDP", "GDP equals GNP", "both must be negative", "neither can be measured"], ans=1,
   why="Adding net factor income received from abroad to GDP gives a larger GNP."),
 dict(q="A country reports the components of aggregate expenditure below. Using the expenditure approach, GDP equals",
   table=GDP1, choices=[
   "$9,600 billion", "$10,600 billion", "$11,000 billion", "$11,400 billion", "$12,200 billion"], ans=1,
   why="GDP = 7,000 + 1,800 + 2,200 + (900 − 1,300) = 10,600 billion."),
 dict(q="Using the same table, net exports equal", table=GDP1, choices=[
   "-$400 billion", "-$100 billion", "$400 billion", "$900 billion", "$2,200 billion"], ans=0,
   why="X − M = 900 − 1,300 = −400 billion."),
 dict(q="Using the same table, consumption as a share of GDP is approximately", table=GDP1, choices=[
   "17%", "44%", "56%", "66%", "77%"], ans=3,
   why="7,000 / 10,600 = 0.66, which matches the usual dominance of consumption in GDP."),
 dict(q="Using the same table, if imports rose to $1,500 billion while everything else stayed the same, GDP would equal", table=GDP1, choices=[
   "$10,200 billion", "$10,400 billion", "$10,600 billion", "$10,800 billion", "$11,000 billion"], ans=1,
   why="Net exports fall to −600, so GDP = 11,000 − 600 = 10,400 billion."),
 dict(q="Using the same table, if exports rose to $1,400 billion with imports unchanged, GDP would equal", table=GDP1, choices=[
   "$10,600 billion", "$10,900 billion", "$11,000 billion", "$11,100 billion", "$11,500 billion"], ans=3,
   why="Net exports become +100, so GDP = 11,000 + 100 = 11,100 billion."),
 dict(q="Using the same table, investment as a share of GDP is closest to", table=GDP1, choices=[
   "7%", "12%", "17%", "22%", "28%"], ans=2,
   why="1,800 / 10,600 = 0.17."),
 dict(q="In most large developed economies, the largest component of GDP by far is", choices=[
   "investment", "consumption", "government purchases", "net exports", "inventory change"], ans=1,
   why="Household consumption typically accounts for roughly two-thirds of GDP."),
 dict(q="The component of GDP that is typically the most volatile over the business cycle is", choices=[
   "consumption of services", "investment", "government purchases", "consumption of nondurables", "transfer payments"], ans=1,
   why="Investment swings sharply with expectations and interest rates, which is why it drives much of the cycle."),
 dict(q="A severe drought destroys a large share of a country's standing timber, but no logging had been scheduled that year. Measured GDP for the year", choices=[
   "falls by the market value of the destroyed timber",
   "is essentially unaffected, because GDP measures production flows rather than changes in the stock of assets",
   "rises because of the cleanup",
   "becomes impossible to compute",
   "falls to zero"], ans=1,
   why="GDP is a flow of newly produced output, so destruction of an existing asset does not enter it directly."),
 dict(q="A hurricane destroys thousands of homes, and $8 billion of rebuilding is done the following year. The rebuilding", choices=[
   "is excluded because it only replaces what existed",
   "raises measured GDP by $8 billion even though the country is not better off than before the storm",
   "reduces GDP by $8 billion",
   "is counted as a transfer payment",
   "is counted as an intermediate good"], ans=1,
   why="GDP counts the new construction as production, which is one reason GDP is not a direct measure of well-being."),
 dict(q="Suppose consumption rises by $50 billion, investment falls by $20 billion, government purchases rise by $10 billion, exports fall by $15 billion, and imports fall by $25 billion. GDP changes by", choices=[
   "-$50 billion", "+$10 billion", "+$50 billion", "+$55 billion", "+$120 billion"], ans=2,
   why="ΔGDP = +50 − 20 + 10 + (−15 − (−25)) = +50 − 20 + 10 + 10 = +50 billion."),
 dict(q="If a firm's inventories fall by $3 billion during a year in which its sales are $40 billion, the firm's contribution to GDP is", choices=[
   "$43 billion", "$37 billion", "$40 billion", "$3 billion", "zero"], ans=1,
   why="Part of what was sold came out of goods produced in an earlier year, so current production is $40 − $3 = $37 billion."),
 dict(q="A student argues that because government purchases are financed by taxes taken from households, counting G in GDP double counts consumption. The best response is that", choices=[
   "the student is correct and G should be excluded",
   "taxes are a transfer of purchasing power, while G measures the government's own purchase of currently produced goods and services",
   "taxes are counted as investment",
   "G is subtracted elsewhere in the accounts",
   "consumption already excludes taxed income"], ans=1,
   why="Household after-tax spending appears in C, and the goods and services government itself buys appear separately in G, so nothing is counted twice."),
]
