# MACRO 2.2 Limitations of GDP — 50 questions
# Table verified (LIV, two hypothetical countries):
#   Country A: nominal GDP = $600 billion, population = 20 million
#     GDP per capita = 600,000 million / 20 million... work in consistent units:
#     $600,000,000,000 / 20,000,000 people = $30,000 per person
#   Country B: nominal GDP = $900 billion, population = 45 million
#     $900,000,000,000 / 45,000,000 people = $20,000 per person
#   So B has the larger total GDP (900 > 600) but the smaller GDP per capita
#     (20,000 < 30,000). Ratio of per capita figures: 30,000 / 20,000 = 1.5
#   If Country A's GDP rose 10% to $660 billion while its population rose 20%
#     to 24 million, per capita GDP = 660,000,000,000 / 24,000,000 = $27,500,
#     a FALL of 2,500 (8.3%) despite total GDP rising.
TOPIC = ("2.2", "Limitations of GDP", 2)

LIV = dict(headers=["Country", "Nominal GDP (billions of $)", "Population (millions)"],
           rows=[["A", "600", "20"],
                 ["B", "900", "45"]])

QUESTIONS = [
 dict(q="GDP is an imperfect measure of a nation's well-being primarily because it", choices=[
   "is measured in nominal rather than real terms",
   "counts only market production and says nothing about how output is distributed or what it costs to produce",
   "is published only once a year",
   "includes transfer payments",
   "double counts intermediate goods"], ans=1,
   why="GDP is a production total, not a welfare index, so it omits both non-market activity and the costs and distribution of output."),
 dict(q="Which of the following is NOT captured in official GDP?", choices=[
   "a restaurant meal",
   "a homeowner mowing their own lawn",
   "a plumber's paid repair",
   "a new tractor purchased by a farm",
   "tuition paid to a private college"], ans=1,
   why="Do-it-yourself household production never passes through a market, so no transaction is recorded."),
 dict(q="Non-market production refers to", choices=[
   "goods sold below cost",
   "useful goods and services produced outside of market transactions, such as housework and volunteer work",
   "government output",
   "exported goods",
   "goods sold in foreign markets"], ans=1,
   why="These activities create real value but generate no market price for statisticians to record."),
 dict(q="Because non-market household production is excluded, official GDP tends to", choices=[
   "overstate the level of economic activity",
   "understate the total amount of useful output produced in the economy",
   "measure welfare precisely",
   "overstate inflation",
   "understate the price level"], ans=1,
   why="Real production is occurring that the accounts never see, so measured output falls short of actual output."),
 dict(q="A country in which a large share of food is grown by families for their own consumption will have GDP figures that", choices=[
   "overstate its material standard of living",
   "understate its material standard of living relative to a country where the same food is bought and sold",
   "be perfectly comparable to any other country",
   "be higher than its true output",
   "include the subsistence farming at market prices"], ans=1,
   why="Subsistence output is real but unmeasured, so cross-country comparisons understate poorer economies."),
 dict(q="The underground economy consists of", choices=[
   "mining and drilling output",
   "transactions that are legal or illegal but go unreported to authorities, such as cash work and black-market sales",
   "government spending that is off budget",
   "foreign trade",
   "output produced by the very poor"], ans=1,
   why="What defines the underground economy is that it is hidden from measurement, not what is being produced."),
 dict(q="A larger underground economy causes measured GDP to", choices=[
   "exceed actual production", "fall short of actual production", "equal actual production", "become negative", "measure only services"], ans=1,
   why="Unreported transactions are real production that never enters the accounts."),
 dict(q="A house painter who is paid $2,000 in cash and does not report the income affects official GDP by", choices=[
   "raising it by $2,000", "leaving it unchanged, even though real services were produced", "lowering it by $2,000", "raising it by $4,000", "raising it only if taxes are paid later"], ans=1,
   why="The service was produced but never recorded, so measured GDP misses it."),
 dict(q="GDP does not account for the value of leisure, which means that a country that produces the same output while working far fewer hours will appear", choices=[
   "better off than it is",
   "no better off than a country working many more hours for the same output",
   "to have higher GDP",
   "to have lower prices",
   "to have more unemployment"], ans=1,
   why="Extra leisure is a genuine gain in well-being that GDP records as nothing at all."),
 dict(q="If the average work week fell from 40 hours to 30 hours and output stayed constant, GDP would", choices=[
   "rise sharply",
   "be unchanged even though people are arguably better off",
   "fall by 25%",
   "fall to zero",
   "rise by the value of the leisure gained"], ans=1,
   why="GDP registers only output, so a gain in free time is invisible to it."),
 dict(q="Environmental degradation caused by production is treated in GDP as", choices=[
   "a subtraction from output",
   "not deducted at all, so GDP overstates the net benefit of that production",
   "an intermediate good",
   "a transfer payment",
   "an addition to investment"], ans=1,
   why="The national accounts have no entry for depleted resources or polluted air, so their cost never reduces GDP."),
 dict(q="A factory that raises output by $10 million while producing air pollution that imposes $4 million in health costs raises measured GDP by", choices=[
   "$0", "$4 million", "$6 million", "$10 million", "$14 million"], ans=3,
   why="The full $10 million of output is counted and the pollution damage is not subtracted anywhere."),
 dict(q="Money spent cleaning up an oil spill", choices=[
   "reduces GDP by the amount spent",
   "increases GDP, even though the country is not better off than if the spill had never happened",
   "has no effect on GDP",
   "is treated as a transfer payment",
   "is treated as an intermediate good"], ans=1,
   why="GDP counts the cleanup as new production without ever counting the damage as a loss."),
 dict(q="Increases in GDP that come from spending on prisons, security systems, and commuting are sometimes called", choices=[
   "transfer payments",
   "defensive or regrettable expenditures, since they offset a problem rather than add to enjoyment",
   "net exports",
   "capital consumption",
   "intermediate consumption"], ans=1,
   why="These are costs of maintaining current living standards that GDP records as gains."),
 dict(q="GDP tells us nothing about", choices=[
   "the total value of final output",
   "how that output is distributed across the population",
   "the size of the investment component",
   "the level of government purchases",
   "the value of exports"], ans=1,
   why="A national total is consistent with any degree of inequality beneath it."),
 dict(q="Two countries have identical GDP per capita, but in one the top 1% receives half of all income. GDP per capita", choices=[
   "correctly signals that living standards are identical",
   "conceals a large difference in how most people actually live",
   "is negative in the unequal country",
   "must be mismeasured",
   "automatically adjusts for inequality"], ans=1,
   why="An average says nothing about the spread around it."),
 dict(q="GDP per capita is calculated as", choices=[
   "GDP × population", "GDP ÷ population", "population ÷ GDP", "GDP ÷ the labor force", "GDP ÷ the number of households"], ans=1,
   why="Dividing total output by the number of people gives output available per person."),
 dict(q="GDP per capita is preferred to total GDP for comparing living standards across countries because", choices=[
   "it is easier to compute",
   "it adjusts for differences in population size, so a large but populous economy is not mistaken for a rich one",
   "it corrects for inflation",
   "it includes the underground economy",
   "it removes the effect of trade"], ans=1,
   why="Total GDP mostly reflects how big a country is, while per capita GDP reflects how much output there is per person."),
 dict(q="Using the table below, GDP per capita in Country A is", table=LIV, choices=[
   "$13,333", "$20,000", "$30,000", "$45,000", "$60,000"], ans=2,
   why="$600 billion divided by 20 million people is $30,000 per person."),
 dict(q="Using the same table, GDP per capita in Country B is", table=LIV, choices=[
   "$15,000", "$20,000", "$25,000", "$30,000", "$45,000"], ans=1,
   why="$900 billion divided by 45 million people is $20,000 per person."),
 dict(q="Using the same table, which conclusion is best supported?", table=LIV, choices=[
   "Country B has both the larger economy and the higher average living standard",
   "Country B has the larger economy, but Country A has the higher output per person",
   "Country A has both the larger economy and the higher output per person",
   "The two countries have identical living standards",
   "Country A must have less inequality"], ans=1,
   why="B's GDP is larger in total ($900b vs $600b) while A's per capita figure is higher ($30,000 vs $20,000)."),
 dict(q="Using the same table, Country A's GDP per capita is what multiple of Country B's?", table=LIV, choices=[
   "0.67", "1.0", "1.5", "2.0", "2.25"], ans=2,
   why="30,000 ÷ 20,000 = 1.5."),
 dict(q="If Country A's GDP rose 10% while its population rose 20%, GDP per capita would", choices=[
   "rise by 10%", "fall, because population grew faster than output", "rise by 30%", "stay the same", "rise by 2%"], ans=1,
   why="Per capita GDP falls to $27,500 because the denominator grew faster than the numerator."),
 dict(q="A country whose real GDP grows 2% a year while population grows 3% a year will experience", choices=[
   "rising output per person", "falling output per person", "constant output per person", "falling total output", "deflation"], ans=1,
   why="Output per person shrinks whenever population outpaces output."),
 dict(q="Comparing GDP per capita across countries also requires converting currencies, and the usual correction for differences in the cost of living is", choices=[
   "the nominal exchange rate",
   "purchasing power parity",
   "the unemployment rate",
   "the trade balance",
   "the GDP deflator of the base country"], ans=1,
   why="PPP adjusts for the fact that a dollar buys different amounts of goods in different countries."),
 dict(q="Which of the following would raise measured GDP without any real improvement in well-being?", choices=[
   "a technological improvement that lowers production costs",
   "a rise in traffic congestion that increases gasoline purchases on longer commutes",
   "an increase in leisure time",
   "a fall in the crime rate",
   "an improvement in air quality"], ans=1,
   why="More fuel bought to sit in traffic is recorded as extra output while making people worse off."),
 dict(q="GDP treats a dollar of spending on cigarettes and a dollar of spending on medical care as", choices=[
   "equal contributions to output, since GDP does not judge the composition of production",
   "unequal, with medical care weighted more heavily",
   "unequal, with cigarettes excluded",
   "transfers rather than production",
   "intermediate goods"], ans=0,
   why="GDP is composition-blind: it adds market values without ranking what is produced."),
 dict(q="The exclusion of illegal activity means measured GDP", choices=[
   "overstates output", "understates output", "is unaffected", "measures welfare correctly", "double counts services"], ans=1,
   why="Real production takes place that is deliberately hidden from the statistical agencies."),
 dict(q="If a country legalized and began taxing an activity that previously took place entirely in the black market, measured GDP would", choices=[
   "fall", "rise, even though actual production might not change at all", "be unchanged", "become negative", "rise only in real terms"], ans=1,
   why="The same activity moves from unmeasured to measured, which is a statistical change rather than a real one."),
 dict(q="Which of the following is a limitation of GDP that adjusting for inflation does NOT fix?", choices=[
   "the difference between nominal and real values",
   "the omission of household production and the underground economy",
   "changes in the general price level",
   "comparing output across years with different prices",
   "the effect of a rising deflator on nominal figures"], ans=1,
   why="Deflating corrects for prices only; it cannot count activity that was never recorded."),
 dict(q="GDP counts government purchases at cost rather than market value because", choices=[
   "governments never produce anything",
   "much government output, such as national defense, is not sold in a market and so has no observable price",
   "governments are exempt from the accounts",
   "government output is an intermediate good",
   "government spending is a transfer"], ans=1,
   why="Without a market price, statisticians value public output by what it costs to provide."),
 dict(q="Improvements in product quality at unchanged prices tend to make GDP growth", choices=[
   "overstate improvements in living standards",
   "understate improvements in living standards",
   "exactly measure them",
   "negative",
   "impossible to calculate"], ans=1,
   why="A better phone at the same price is a real gain in welfare that shows up as no change in output value."),
 dict(q="The Human Development Index differs from GDP per capita by also incorporating", choices=[
   "the money supply and interest rates",
   "life expectancy and education",
   "the trade balance and the deficit",
   "the inflation rate and unemployment rate",
   "the size of the underground economy"], ans=1,
   why="HDI combines income with health and schooling to give a broader picture of development."),
 dict(q="Despite all its limitations, GDP remains the standard measure of economic performance mainly because", choices=[
   "it perfectly measures welfare",
   "it is consistently defined, regularly published, and correlates strongly with things people care about such as health and literacy",
   "no alternative has ever been proposed",
   "it includes non-market production",
   "it is unaffected by inflation"], ans=1,
   why="Its comparability over time and across countries, and its strong correlation with living standards, keep it useful even though it is incomplete."),
 dict(q="A researcher claims Country X is better off than Country Y because X's total GDP is larger. The most important objection is that", choices=[
   "GDP is measured in nominal terms",
   "X may simply have a much larger population, so output per person could be lower",
   "GDP excludes government purchases",
   "GDP double counts intermediate goods",
   "GDP is measured annually"], ans=1,
   why="Total GDP conflates the size of a country with the prosperity of its people."),
 dict(q="Which comparison requires adjusting GDP for BOTH prices and population?", choices=[
   "comparing this quarter's nominal GDP to last quarter's",
   "comparing living standards in one country in 1970 with the same country in 2020",
   "computing net exports",
   "measuring the underground economy",
   "computing the value added of one firm"], ans=1,
   why="Prices and population have both changed over fifty years, so only real GDP per capita is meaningful."),
 dict(q="If real GDP rises 4% and population rises 1%, real GDP per capita rises by approximately", choices=[
   "0.25%", "1%", "3%", "4%", "5%"], ans=2,
   why="Growth in per capita terms is roughly the growth of output minus the growth of population."),
 dict(q="Which of the following costs of production is subtracted somewhere in GDP?", choices=[
   "the depletion of a fishery",
   "the intermediate inputs a firm buys from other firms",
   "the health damage from smog",
   "the loss of leisure time",
   "the stress experienced by workers"], ans=1,
   why="Only purchased intermediate inputs are netted out; environmental and human costs are not."),
 dict(q="A country experiences rising GDP alongside rising pollution, longer working hours, and worsening inequality. The best statement is that", choices=[
   "its people are unambiguously better off",
   "its output is rising, but whether well-being is rising cannot be determined from GDP alone",
   "its GDP must be mismeasured",
   "its GDP must actually be falling",
   "GDP has become a normative statistic"], ans=1,
   why="GDP answers only the question of how much was produced."),
 dict(q="Green GDP attempts to improve on conventional GDP by", choices=[
   "excluding services",
   "subtracting the value of environmental damage and resource depletion",
   "adding the underground economy",
   "adjusting for inflation",
   "including transfer payments"], ans=1,
   why="It nets out environmental costs that standard GDP ignores."),
 dict(q="Compared with a country of similar income, a country with far more of its production occurring within households will show", choices=[
   "unusually high measured GDP per capita",
   "unusually low measured GDP per capita relative to actual living standards",
   "identical measured GDP per capita",
   "higher inflation",
   "a larger trade surplus"], ans=1,
   why="Household production is real output that the accounts do not see."),
 dict(q="Which of the following would cause measured GDP to rise while true economic well-being falls?", choices=[
   "a fall in commuting time",
   "an increase in spending on medical treatment caused by a worsening epidemic",
   "an improvement in workplace safety",
   "a rise in life expectancy",
   "an increase in volunteer work"], ans=1,
   why="Extra treatment spending counts as output, but it responds to a loss the accounts never subtract."),
 dict(q="Volunteer work at a food bank is", choices=[
   "counted in GDP at the market wage for similar work",
   "excluded from GDP because no payment is made",
   "counted as a transfer payment",
   "counted as government purchases",
   "counted as investment"], ans=1,
   why="No market transaction occurs, so nothing is recorded."),
 dict(q="Two economies produce identical output, but one has half its output going to consumption and the other has half going to investment. GDP", choices=[
   "is higher in the investment-heavy economy",
   "is the same in both, though their future growth prospects differ",
   "is higher in the consumption-heavy economy",
   "cannot be computed",
   "must be adjusted for the difference"], ans=1,
   why="GDP totals output regardless of its composition, even though the composition matters greatly for the future."),
 dict(q="The statement 'GDP measures everything except that which makes life worthwhile' is best understood as a criticism that GDP", choices=[
   "is measured in the wrong currency",
   "captures market output while omitting health, leisure, environment, and relationships",
   "double counts",
   "excludes government",
   "is published too infrequently"], ans=1,
   why="It targets the gap between market production and human well-being."),
 dict(q="Which is the strongest argument that GDP per capita is nonetheless a useful welfare proxy?", choices=[
   "it is a normative measure",
   "across countries it correlates closely with literacy, life expectancy, and infant survival",
   "it includes household production",
   "it is unaffected by inequality",
   "it measures leisure directly"], ans=1,
   why="Richer countries systematically do better on the outcomes people care about, so the proxy carries real information."),
 dict(q="If a statistical agency improved its methods and began capturing more of the underground economy, measured GDP growth in that year would", choices=[
   "understate the true change in production",
   "overstate the true change in production",
   "exactly equal it",
   "be unaffected",
   "become negative"], ans=1,
   why="Part of the recorded increase is newly measured activity that was already occurring."),
 dict(q="A country's GDP rises 3% while its population rises 3% and its price level rises 3%. Real GDP per capita has", choices=[
   "risen about 3%", "fallen about 3%", "risen about 6%", "stayed roughly constant", "fallen about 9%"], ans=1,
   why="Nominal growth of 3% is entirely inflation, leaving real growth near zero, and dividing by 3% more people cuts real output per person by about 3%."),
 dict(q="Which of the following best explains why GDP is described as a measure of economic activity rather than a measure of welfare?", choices=[
   "it is reported quarterly",
   "it records the market value of what is produced without evaluating whether that production makes people better or worse off",
   "it is always positive",
   "it excludes investment",
   "it is adjusted for inflation"], ans=1,
   why="Valuation at market prices is a measure of scale, not of benefit."),
 dict(q="A policymaker proposes replacing GDP with a well-being index. The most serious practical objection is that", choices=[
   "well-being cannot possibly be related to income",
   "the components of such an index must be weighted by value judgements, which makes it far less comparable and more contested than a market-value total",
   "GDP already includes leisure",
   "no data on health or education exist",
   "GDP is never revised"], ans=1,
   why="GDP's advantage is that market prices supply objective weights, while any welfare index must choose its weights normatively."),
]
