# MACRO 2.6 Real vs. Nominal GDP — 50 questions
# Table verified (ECON). A two-good economy; base year = 2020.
#   Year   Books P   Books Q   Pens P   Pens Q
#   2020    $10        100      $2.00     200
#   2021    $12        110      $2.50     220
#   2022    $15        120      $3.00     250
#
# NOMINAL GDP (each year's own prices x that year's quantities):
#   2020 = 10(100) + 2.00(200) = 1,000 + 400 = $1,400
#   2021 = 12(110) + 2.50(220) = 1,320 + 550 = $1,870
#   2022 = 15(120) + 3.00(250) = 1,800 + 750 = $2,550
#
# REAL GDP (2020 base-year prices x each year's quantities):
#   2020 = 10(100) + 2.00(200) = 1,000 + 400 = $1,400   (= nominal in base year)
#   2021 = 10(110) + 2.00(220) = 1,100 + 440 = $1,540
#   2022 = 10(120) + 2.00(250) = 1,200 + 500 = $1,700
#
# GDP DEFLATOR = 100 x nominal / real:
#   2020 = 100 x 1,400/1,400 = 100.0
#   2021 = 100 x 1,870/1,540 = 121.4   (1,870/1,540 = 1.21428...)
#   2022 = 100 x 2,550/1,700 = 150.0   (exact)
#
# GROWTH RATES:
#   Real growth 2020->2021 = (1,540 - 1,400)/1,400 = 0.100 = 10.0%
#   Real growth 2021->2022 = (1,700 - 1,540)/1,540 = 160/1,540 = 0.1039 = 10.4%
#   Nominal growth 2020->2021 = (1,870 - 1,400)/1,400 = 470/1,400 = 0.3357 = 33.6%
#   Nominal growth 2021->2022 = (2,550 - 1,870)/1,870 = 680/1,870 = 0.3636 = 36.4%
#   Inflation 2020->2021 by the deflator = (121.4 - 100)/100 = 21.4%
#   Inflation 2021->2022 by the deflator = (150.0 - 121.4)/121.4 = 28.6/121.4 = 23.6%
#
# ALTERNATIVE BASE YEAR CHECK (2021 as base):
#   Real 2022 in 2021 prices = 12(120) + 2.50(250) = 1,440 + 625 = $2,065
TOPIC = ("2.6", "Real vs. Nominal GDP", 2)

ECON = dict(headers=["Year", "Price of books", "Quantity of books", "Price of pens", "Quantity of pens"],
            rows=[["2020", "$10", "100", "$2.00", "200"],
                  ["2021", "$12", "110", "$2.50", "220"],
                  ["2022", "$15", "120", "$3.00", "250"]])

QUESTIONS = [
 dict(q="Nominal GDP is measured using", choices=[
   "base-year prices and current quantities",
   "current-year prices and current-year quantities",
   "current-year prices and base-year quantities",
   "base-year prices and base-year quantities",
   "the CPI basket"], ans=1,
   why="Nominal GDP values this year's output at this year's prices, so it moves with both output and prices."),
 dict(q="Real GDP is measured using", choices=[
   "current-year prices and current-year quantities",
   "constant base-year prices and current-year quantities",
   "current-year prices and base-year quantities",
   "base-year prices and base-year quantities",
   "the producer price index"], ans=1,
   why="Holding prices fixed at base-year levels means changes in real GDP reflect changes in output alone."),
 dict(q="Real GDP is preferred to nominal GDP for measuring economic growth because it", choices=[
   "is always larger",
   "removes the effect of price changes, so it reflects changes in the quantity of output",
   "includes the underground economy",
   "adjusts for population",
   "uses a fixed market basket of consumer goods"], ans=1,
   why="A rise in nominal GDP could be entirely inflation, which tells us nothing about production."),
 dict(q="In the base year, nominal GDP and real GDP are", choices=[
   "unrelated", "equal", "different by the inflation rate", "both zero", "equal only if inflation is zero"], ans=1,
   why="In the base year the same prices are used for both measures."),
 dict(q="If nominal GDP rises 6% while real GDP rises 2%, the price level has risen by approximately", choices=[
   "2%", "4%", "6%", "8%", "12%"], ans=1,
   why="Nominal growth is roughly real growth plus inflation, so inflation ≈ 6 − 2 = 4%."),
 dict(q="If nominal GDP rises 5% while prices rise 5%, real GDP has", choices=[
   "risen 10%", "stayed roughly constant", "risen 5%", "fallen 5%", "fallen 10%"], ans=1,
   why="The entire nominal increase is accounted for by higher prices, so output is unchanged."),
 dict(q="If nominal GDP falls 1% while prices rise 3%, real GDP has", choices=[
   "risen 2%", "fallen about 4%", "fallen 1%", "risen 3%", "stayed constant"], ans=1,
   why="Real growth ≈ −1 − 3 = −4%, so output fell even faster than spending."),
 dict(q="The GDP deflator is defined as", choices=[
   "100 × real GDP ÷ nominal GDP",
   "100 × nominal GDP ÷ real GDP",
   "nominal GDP − real GDP",
   "real GDP ÷ population",
   "100 × the CPI ÷ nominal GDP"], ans=1,
   why="The deflator is the ratio of output valued at current prices to the same output at base-year prices."),
 dict(q="Real GDP can be recovered from nominal GDP by", choices=[
   "multiplying nominal GDP by the deflator",
   "dividing nominal GDP by the deflator and multiplying by 100",
   "subtracting the inflation rate from nominal GDP",
   "dividing nominal GDP by the population",
   "adding the deflator to nominal GDP"], ans=1,
   why="Deflating converts current-dollar output into constant-dollar output."),
 dict(q="Using the table below, nominal GDP in 2020 is", table=ECON, choices=[
   "$1,200", "$1,400", "$1,540", "$1,700", "$1,870"], ans=1,
   why="$10(100) + $2.00(200) = $1,000 + $400 = $1,400."),
 dict(q="Using the same table, nominal GDP in 2021 is", table=ECON, choices=[
   "$1,400", "$1,540", "$1,700", "$1,870", "$2,065"], ans=3,
   why="$12(110) + $2.50(220) = $1,320 + $550 = $1,870."),
 dict(q="Using the same table, nominal GDP in 2022 is", table=ECON, choices=[
   "$1,700", "$2,065", "$2,300", "$2,550", "$2,750"], ans=3,
   why="$15(120) + $3.00(250) = $1,800 + $750 = $2,550."),
 dict(q="Using the same table with 2020 as the base year, real GDP in 2021 is", table=ECON, choices=[
   "$1,400", "$1,540", "$1,700", "$1,870", "$2,065"], ans=1,
   why="Value 2021's quantities at 2020 prices: $10(110) + $2.00(220) = $1,100 + $440 = $1,540."),
 dict(q="Using the same table with 2020 as the base year, real GDP in 2022 is", table=ECON, choices=[
   "$1,540", "$1,700", "$1,870", "$2,065", "$2,550"], ans=1,
   why="$10(120) + $2.00(250) = $1,200 + $500 = $1,700."),
 dict(q="Using the same table, the GDP deflator in 2020 is", table=ECON, choices=[
   "0", "10", "100", "121.4", "150.0"], ans=2,
   why="2020 is the base year, so nominal and real GDP are both $1,400 and the deflator is 100."),
 dict(q="Using the same table, the GDP deflator in 2021 is closest to", table=ECON, choices=[
   "82.4", "100.0", "110.0", "121.4", "133.6"], ans=3,
   why="100 × $1,870/$1,540 = 121.4."),
 dict(q="Using the same table, the GDP deflator in 2022 is", table=ECON, choices=[
   "66.7", "100.0", "121.4", "136.4", "150.0"], ans=4,
   why="100 × $2,550/$1,700 = 150.0 exactly."),
 dict(q="Using the same table, the growth rate of real GDP from 2020 to 2021 is", table=ECON, choices=[
   "8.0%", "10.0%", "21.4%", "33.6%", "36.4%"], ans=1,
   why="($1,540 − $1,400)/$1,400 = 0.10."),
 dict(q="Using the same table, the growth rate of nominal GDP from 2020 to 2021 is closest to", table=ECON, choices=[
   "10.0%", "21.4%", "25.1%", "33.6%", "47.0%"], ans=3,
   why="($1,870 − $1,400)/$1,400 = 0.336."),
 dict(q="Using the same table, the growth rate of real GDP from 2021 to 2022 is closest to", table=ECON, choices=[
   "9.4%", "10.4%", "16.2%", "23.6%", "36.4%"], ans=1,
   why="($1,700 − $1,540)/$1,540 = 0.1039."),
 dict(q="Using the same table, the inflation rate from 2020 to 2021 as measured by the GDP deflator is closest to", table=ECON, choices=[
   "10.0%", "21.4%", "23.6%", "33.6%", "50.0%"], ans=1,
   why="The deflator rises from 100.0 to 121.4, a 21.4% increase."),
 dict(q="Using the same table, the inflation rate from 2021 to 2022 as measured by the GDP deflator is closest to", table=ECON, choices=[
   "10.4%", "21.4%", "23.6%", "28.6%", "36.4%"], ans=2,
   why="(150.0 − 121.4)/121.4 = 0.236; note that the 28.6 figure is the change in index points, not the percentage change."),
 dict(q="Using the same table but taking 2021 as the base year, real GDP in 2022 would be", table=ECON, choices=[
   "$1,700", "$1,870", "$2,065", "$2,550", "$2,750"], ans=2,
   why="$12(120) + $2.50(250) = $1,440 + $625 = $2,065, which shows that the level of real GDP depends on the chosen base year."),
 dict(q="Using the same table, between 2020 and 2022 the economy's nominal GDP rose about 82% while its real GDP rose about 21%. The difference is explained by", table=ECON, choices=[
   "an increase in population",
   "the rise in the prices of both goods over the period",
   "a change in the base year",
   "an error in the quantity data",
   "the exclusion of imports"], ans=1,
   why="Nominal GDP grew from $1,400 to $2,550 and real GDP from $1,400 to $1,700, with the gap being pure price increase."),
 dict(q="An economy produces exactly the same physical output this year as last year, but every price doubles. Nominal GDP", choices=[
   "is unchanged and real GDP doubles",
   "doubles while real GDP is unchanged",
   "halves",
   "and real GDP both double",
   "and real GDP are both unchanged"], ans=1,
   why="Real GDP tracks quantities, which did not change, while nominal GDP tracks quantities valued at doubled prices."),
 dict(q="Which of the following would raise real GDP?", choices=[
   "a rise in the price level with output unchanged",
   "an increase in the quantity of goods and services produced",
   "a rise in the GDP deflator",
   "an increase in the money supply with output unchanged",
   "a rebasing of the index"], ans=1,
   why="Only more physical output raises real GDP."),
 dict(q="A recession is conventionally identified by a decline in", choices=[
   "nominal GDP", "real GDP", "the GDP deflator", "the CPI", "the money supply"], ans=1,
   why="A downturn is a fall in actual production, which nominal GDP could mask during inflation."),
 dict(q="During a period of rapid inflation, nominal GDP could rise while real GDP falls. This means that", choices=[
   "output rose",
   "the economy produced less even though the dollar value of output rose",
   "prices fell",
   "the deflator fell",
   "the base year changed"], ans=1,
   why="Prices rose enough to more than offset the decline in the quantity of output."),
 dict(q="If nominal GDP is $18 trillion and the GDP deflator is 120, real GDP is", choices=[
   "$12.0 trillion", "$15.0 trillion", "$18.0 trillion", "$21.6 trillion", "$150.0 trillion"], ans=1,
   why="$18 trillion × 100/120 = $15 trillion."),
 dict(q="If real GDP is $16 trillion and the GDP deflator is 125, nominal GDP is", choices=[
   "$12.8 trillion", "$16.0 trillion", "$18.0 trillion", "$20.0 trillion", "$25.0 trillion"], ans=3,
   why="Nominal = real × deflator/100 = 16 × 1.25 = $20 trillion."),
 dict(q="If nominal GDP is $500 billion and real GDP is $400 billion, the GDP deflator is", choices=[
   "80", "100", "110", "120", "125"], ans=4,
   why="100 × 500/400 = 125."),
 dict(q="A price index below 100 for a given year indicates that", choices=[
   "output was lower than in the base year",
   "prices in that year were lower than in the base year",
   "the economy was in recession",
   "nominal GDP exceeded real GDP",
   "the base year was mislabeled"], ans=1,
   why="An index under 100 means the price level was below its base-year value, so nominal GDP is below real GDP that year."),
 dict(q="Real GDP per capita is calculated as", choices=[
   "nominal GDP ÷ population",
   "real GDP ÷ population",
   "real GDP ÷ the labor force",
   "nominal GDP ÷ the deflator",
   "real GDP × population"], ans=1,
   why="It corrects for both prices and the number of people."),
 dict(q="A country's real GDP grows 3% while its population grows 1%. Real GDP per capita grows by approximately", choices=[
   "0.33%", "1%", "2%", "3%", "4%"], ans=2,
   why="Approximately 3 − 1 = 2%."),
 dict(q="Comparing living standards in a country across fifty years requires using", choices=[
   "nominal GDP", "real GDP per capita", "nominal GDP per capita", "the GDP deflator alone", "total employment"], ans=1,
   why="Both the price level and the population change over such a span."),
 dict(q="Chain weighting of real GDP was adopted mainly to address the problem that", choices=[
   "prices are unobservable",
   "a fixed distant base year gives increasingly poor weights as relative prices and output shares change",
   "quantities are unobservable",
   "the deflator cannot be computed",
   "nominal GDP is unreliable"], ans=1,
   why="Chain weighting updates the price weights continuously instead of freezing them in one distant year."),
 dict(q="Which of the following statements about the base year is correct?", choices=[
   "the choice of base year changes the growth rate of nominal GDP",
   "the choice of base year affects the level of real GDP and can slightly affect measured growth rates",
   "the base year must be the current year",
   "the base year has no effect on any calculation",
   "the base year determines the population"], ans=1,
   why="Different base-year prices weight the goods differently, which is why the same data gave real 2022 GDP of $1,700 on a 2020 base and $2,065 on a 2021 base."),
 dict(q="Suppose an economy's output of every good falls 5% while every price rises 5%. Nominal GDP will", choices=[
   "rise by 10%",
   "be roughly unchanged while real GDP falls about 5%",
   "fall by 10%",
   "rise by 5% while real GDP rises 5%",
   "fall by 5% while real GDP is unchanged"], ans=1,
   why="The price rise almost exactly offsets the quantity fall in the dollar total, but production is genuinely lower."),
 dict(q="Which measure would a government use to compute the ratio of the national debt to the size of the economy in current dollars?", choices=[
   "real GDP", "nominal GDP", "real GDP per capita", "the GDP deflator", "the CPI"], ans=1,
   why="Debt is denominated in current dollars, so the comparison should use current-dollar GDP."),
 dict(q="The GDP deflator differs from the CPI in that the deflator", choices=[
   "uses a fixed basket of consumer goods",
   "covers all domestically produced final goods and services, including investment and government purchases",
   "includes imported consumer goods",
   "is always 100",
   "cannot be used to compute inflation"], ans=1,
   why="The deflator's coverage is domestic output rather than the consumer basket."),
 dict(q="If nominal GDP is unchanged from one year to the next while the GDP deflator rises, then real GDP has", choices=[
   "risen", "fallen", "stayed the same", "become negative", "doubled"], ans=1,
   why="With nominal GDP in the numerator fixed and the deflator rising, real GDP = nominal ÷ deflator must fall."),
 dict(q="A journalist reports that GDP hit a record high in dollar terms. The most important caution is that", choices=[
   "GDP is never measured in dollars",
   "a nominal record can occur even in a year when real output fell, because prices rise almost every year",
   "GDP records are never broken",
   "nominal GDP excludes services",
   "the deflator must have fallen"], ans=1,
   why="Persistent inflation makes nominal records routine and uninformative about production."),
 dict(q="An economy's real GDP is $900 billion and potential (full-employment) real GDP is $1,000 billion. The economy is", choices=[
   "above potential",
   "below potential, with a recessionary output gap of $100 billion",
   "at long-run equilibrium",
   "experiencing an inflationary gap",
   "growing at 10%"], ans=1,
   why="Actual output below potential defines a recessionary gap."),
 dict(q="Which of the following would be reflected in a rise in real GDP but not in a rise in nominal GDP alone?", choices=[
   "a doubling of all prices",
   "the opening of new factories that increase physical output",
   "an increase in the deflator",
   "a rise in the CPI",
   "a change in the base year"], ans=1,
   why="Only the change in quantities is a real change."),
 dict(q="If a country's real GDP grew 2% and its deflator rose 3%, nominal GDP grew by approximately", choices=[
   "-1%", "1%", "2%", "3%", "5%"], ans=4,
   why="Nominal growth ≈ real growth + inflation = 2 + 3 = 5%."),
 dict(q="Two countries report identical nominal GDP growth of 8%. Country X had 1% inflation and Country Y had 7%. It follows that", choices=[
   "both grew equally in real terms",
   "Country X grew far faster in real terms, about 7% against about 1%",
   "Country Y grew faster in real terms",
   "neither grew",
   "real growth cannot be compared"], ans=1,
   why="Subtracting each country's inflation from the same nominal growth leaves very different real growth rates."),
 dict(q="Real GDP is sometimes called GDP in constant dollars because", choices=[
   "the quantities are held constant",
   "output in every year is valued using the same set of base-year prices",
   "the population is held constant",
   "the deflator is held at 100",
   "nominal GDP does not change"], ans=1,
   why="Holding the prices constant is exactly what makes the dollars comparable across years."),
 dict(q="Suppose a country's nominal GDP triples over twenty years while its GDP deflator also triples. Real GDP has", choices=[
   "tripled", "remained essentially unchanged", "risen ninefold", "fallen by two-thirds", "risen 200%"], ans=1,
   why="Nominal GDP divided by a deflator that rose in the same proportion leaves real GDP flat, so the country produced no more than before."),
 dict(q="The single most common student error in this topic is", choices=[
   "confusing exports with imports",
   "computing real GDP with current-year prices instead of base-year prices",
   "adding population to output",
   "using the labor force as the denominator",
   "forgetting that GDP is measured annually"], ans=1,
   why="Using current prices produces nominal GDP again, and the whole point of the real measure is to freeze prices."),
 dict(q="A student calculates that because the deflator rose from 121.4 to 150.0, inflation was 28.6%. The error is that", choices=[
   "the deflator cannot be used for inflation",
   "the change of 28.6 index points must be divided by the starting value of 121.4, giving 23.6%",
   "the base year is wrong",
   "the deflator should be divided by 100 first",
   "inflation should be measured only with the CPI"], ans=1,
   why="A change in index points is not a percentage change unless the starting index happens to be 100."),
]
