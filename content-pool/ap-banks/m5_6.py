# MACRO 5.6 Economic Growth — 50 questions
# Every number worked out:
#   Rule of 70: doubling time = 70 / growth rate in percent.
#     70/2 = 35 years. 70/3.5 = 20 years. 70/5 = 14 years. 70/7 = 10 years. 70/10 = 7 years.
#     70/1 = 70 years. 70/14 = 5 years.
#   Real GDP per capita growth = real GDP growth - population growth.
#     Real GDP +4%, population +1% -> per capita +3%.
#     Real GDP +2%, population +3% -> per capita -1% (living standards fall).
#     Real GDP +5%, population +2% -> per capita +3%, doubling in 70/3 ≈ 23 years.
#   Productivity: output 1,200 units from 400 labor hours -> 3 units per hour.
#     Output rises to 1,500 with 500 hours -> 3 units per hour, unchanged productivity.
#     Output 1,800 from 500 hours -> 3.6 units per hour, a 20% rise from 3.0.
#   GROWTH table: real GDP and population, index numbers.
#     Yr1: GDP 1,000, pop 100 -> per capita 10.
#     Yr2: GDP 1,100, pop 105 -> per capita 1,100/105 = 10.476...
#     Yr3: GDP 1,210, pop 110 -> per capita 11.0.
#     Yr4: GDP 1,240, pop 124 -> per capita 10.0, back to the Year 1 level.
#     GDP growth Yr1 to Yr2 = 10%; Yr2 to Yr3 = 10%; Yr3 to Yr4 = 30/1,210 ≈ 2.5%.
TOPIC = ("5.6", "Economic Growth", 5)
GROWTH = dict(
    headers=["Year", "Real GDP", "Population"],
    rows=[["1", "1,000", "100"], ["2", "1,100", "105"], ["3", "1,210", "110"], ["4", "1,240", "124"]],
)
QUESTIONS = [
 dict(q="Long-run economic growth is best defined as", choices=[
   "an increase in the price level over time",
   "a sustained increase in an economy's potential output, usually measured as real GDP per capita",
   "a recovery from a recession",
   "an increase in the money supply",
   "a fall in the unemployment rate"], ans=1,
   why="Growth is about expanding capacity, not about closing a cyclical gap."),
 dict(q="Economic growth is shown in the AD-AS model as", choices=[
   "a rightward shift of aggregate demand",
   "a rightward shift of the long-run aggregate supply curve",
   "a movement along the short-run aggregate supply curve",
   "a leftward shift of SRAS",
   "a fall in the price level"], ans=1,
   why="Potential output rising is exactly an outward move of LRAS."),
 dict(q="Economic growth is shown on the production possibilities curve as", choices=[
   "a movement from inside the curve to a point on it",
   "an outward shift of the entire curve",
   "a movement along the curve",
   "an inward shift of the curve",
   "a point outside the curve that is never attainable"], ans=1,
   why="Growth expands the set of attainable combinations."),
 dict(q="A movement from a point inside the production possibilities curve to a point on the curve represents", choices=[
   "long-run economic growth",
   "a recovery that puts idle resources back to work, not growth in capacity",
   "an increase in potential output",
   "an outward shift of LRAS",
   "an increase in technology"], ans=1,
   why="Using existing resources more fully is a cyclical recovery, not an increase in capacity."),
 dict(q="The main determinant of a country's standard of living over the long run is", choices=[
   "its money supply",
   "its productivity, the output produced per unit of input",
   "its tax rate",
   "its trade balance",
   "its inflation rate"], ans=1,
   why="People can only consume what is produced, so output per worker sets living standards."),
 dict(q="Labor productivity is measured as", choices=[
   "total real GDP",
   "real output per hour worked",
   "the number of workers employed",
   "the wage rate",
   "the labor force participation rate"], ans=1,
   why="Productivity is a ratio of output to labor input."),
 dict(q="An economy produces 1,200 units of output using 400 labor hours. Labor productivity is", choices=[
   "0.33 units per hour", "3 units per hour", "4 units per hour", "300 units per hour", "1,200 units per hour"], ans=1,
   why="1,200/400 = 3 units per hour."),
 dict(q="Output rises from 1,200 units with 400 hours to 1,500 units with 500 hours. Labor productivity has", choices=[
   "risen by 25 percent",
   "remained unchanged at 3 units per hour",
   "fallen",
   "risen to 5 units per hour",
   "doubled"], ans=1,
   why="Both figures give 3 units per hour, so extra output came from extra hours, not from productivity."),
 dict(q="Output rises from 1,200 units with 400 hours to 1,800 units with 500 hours. Labor productivity has risen by", choices=[
   "10%", "20%", "25%", "50%", "60%"], ans=1,
   why="Productivity goes from 3.0 to 3.6 units per hour, a 20 percent increase."),
 dict(q="Physical capital contributes to growth because", choices=[
   "it reduces the labor force",
   "more tools, machines, and structures per worker raise output per worker",
   "it raises the price level",
   "it lowers the saving rate",
   "it reduces technology"], ans=1,
   why="Capital deepening raises the amount each worker can produce."),
 dict(q="Human capital refers to", choices=[
   "the number of people in a country",
   "the knowledge, skills, and health that workers acquire through education, training, and experience",
   "factories and machinery",
   "natural resources",
   "financial assets held by households"], ans=1,
   why="It is productive capacity embodied in people rather than in equipment."),
 dict(q="Technological progress raises growth by", choices=[
   "increasing the number of workers",
   "allowing more output to be produced from the same quantity of inputs",
   "raising the price level",
   "lowering the money supply",
   "raising the natural rate of unemployment"], ans=1,
   why="Better methods shift the whole relationship between inputs and output."),
 dict(q="Which of the following is an institutional factor supporting long-run growth?", choices=[
   "an unpredictable legal system",
   "well-defined and enforced property rights",
   "widespread corruption",
   "frequent expropriation of private assets",
   "unstable currency"], ans=1,
   why="People invest only when they expect to keep the returns."),
 dict(q="Natural resources contribute to growth, but a country with few natural resources can still grow rapidly because", choices=[
   "resources are unimportant to production",
   "human capital, physical capital, technology, and trade can substitute for domestic resource endowments",
   "resources always cause inflation",
   "growth is determined only by population",
   "resources cannot be traded"], ans=1,
   why="Several economies with almost no natural resources are among the richest in the world."),
 dict(q="The rule of 70 states that the number of years for a variable to double is approximately", choices=[
   "70 times the growth rate",
   "70 divided by the annual percentage growth rate",
   "the growth rate divided by 70",
   "70 minus the growth rate",
   "70 plus the growth rate"], ans=1,
   why="It is a convenient approximation to the doubling time of a compounding quantity."),
 dict(q="At a growth rate of 2 percent per year, real GDP per capita will double in about", choices=[
   "7 years", "14 years", "20 years", "35 years", "70 years"], ans=3,
   why="70/2 = 35 years."),
 dict(q="At a growth rate of 5 percent per year, output doubles in about", choices=[
   "5 years", "10 years", "14 years", "35 years", "70 years"], ans=2,
   why="70/5 = 14 years."),
 dict(q="At a growth rate of 7 percent per year, output doubles in about", choices=[
   "5 years", "7 years", "10 years", "14 years", "70 years"], ans=2,
   why="70/7 = 10 years."),
 dict(q="A country growing at 1 percent a year rather than 2 percent a year will take an extra", choices=[
   "5 years to double", "10 years to double", "20 years to double", "35 years to double", "70 years to double"], ans=3,
   why="Doubling takes 70 years at 1 percent and 35 years at 2 percent, a difference of 35 years."),
 dict(q="Real GDP grows 4 percent while population grows 1 percent. Real GDP per capita grows about", choices=[
   "1%", "3%", "4%", "5%", "0.25%"], ans=1,
   why="Per capita growth is roughly output growth minus population growth: 4 - 1 = 3%."),
 dict(q="Real GDP grows 2 percent while population grows 3 percent. Real GDP per capita", choices=[
   "grows 5 percent", "falls about 1 percent", "grows 1 percent", "is unchanged", "grows 2 percent"], ans=1,
   why="Output per person falls when population outpaces output: 2 - 3 = -1%."),
 dict(q="Real GDP grows 5 percent while population grows 2 percent. Real GDP per capita will double in about", choices=[
   "14 years", "23 years", "35 years", "50 years", "70 years"], ans=1,
   why="Per capita growth is 3 percent, and 70/3 is roughly 23 years."),
 dict(q="Refer to the table. Real GDP per capita in Year 1 is", table=GROWTH, choices=[
   "1", "10", "100", "1,000", "10,000"], ans=1,
   why="1,000 divided by 100 is 10."),
 dict(q="Refer to the table. Real GDP per capita in Year 3 is", table=GROWTH, choices=[
   "10.0", "10.5", "11.0", "12.1", "110"], ans=2,
   why="1,210 divided by 110 is 11."),
 dict(q="Refer to the table. Comparing Year 4 with Year 1, real GDP per capita has", table=GROWTH, choices=[
   "risen 24 percent",
   "returned to its Year 1 level despite higher total output",
   "fallen by half",
   "risen 10 percent",
   "risen 30 percent"], ans=1,
   why="1,240/124 = 10, exactly the Year 1 figure, because population grew as fast as output."),
 dict(q="Refer to the table. The growth rate of real GDP from Year 1 to Year 2 is", table=GROWTH, choices=[
   "1%", "5%", "10%", "11%", "20%"], ans=2,
   why="(1,100 - 1,000)/1,000 = 10%."),
 dict(q="Refer to the table. The lesson of Year 3 to Year 4 is that", table=GROWTH, choices=[
   "total output growth always raises living standards",
   "output can grow while output per person falls, if population grows faster",
   "population growth is irrelevant to living standards",
   "real GDP fell",
   "productivity necessarily rose"], ans=1,
   why="Real GDP rose about 2.5 percent while population rose 12.7 percent, so per capita output fell."),
 dict(q="An increase in the saving rate is likely to raise long-run growth because", choices=[
   "saving reduces the interest rate directly with no other effect",
   "greater saving increases the supply of loanable funds, financing more investment and a larger capital stock",
   "saving raises consumption today",
   "saving lowers the labor force",
   "saving raises the price level"], ans=1,
   why="Investment must be financed by saving, and investment builds the capital stock."),
 dict(q="An economy that consumes all of its output and invests nothing will", choices=[
   "grow rapidly",
   "see its capital stock depreciate and its future output capacity stagnate or shrink",
   "have no opportunity cost",
   "experience deflation",
   "eliminate scarcity"], ans=1,
   why="Without replacement investment the capital stock wears out."),
 dict(q="The trade-off at the heart of investment-driven growth is between", choices=[
   "inflation and unemployment",
   "consumption today and higher output in the future",
   "exports and imports",
   "taxes and transfers",
   "money and bonds"], ans=1,
   why="Resources used to build capital cannot also be consumed now."),
 dict(q="Diminishing returns to capital implies that", choices=[
   "additional capital always raises output by the same amount",
   "as capital per worker rises, each additional unit adds less to output than the one before",
   "capital never raises output",
   "output falls as capital rises",
   "growth accelerates without limit"], ans=1,
   why="The marginal product of capital declines as capital accumulates, holding technology fixed."),
 dict(q="Because of diminishing returns to capital, sustained long-run growth in output per worker depends most on", choices=[
   "ever-larger investment in the same technology",
   "continuing technological progress",
   "population growth",
   "increases in the money supply",
   "reductions in the price level"], ans=1,
   why="Only advancing technology can keep raising output per worker indefinitely."),
 dict(q="The catch-up effect predicts that, other things equal, poorer countries tend to", choices=[
   "grow more slowly than rich countries",
   "grow faster than rich countries because the return on their initial capital is high",
   "never grow",
   "have higher output per worker",
   "have more capital per worker"], ans=1,
   why="Where capital is scarce, the marginal product of new capital is large."),
 dict(q="Which of the following would shift long-run aggregate supply to the right?", choices=[
   "an increase in the money supply",
   "an increase in the quantity and quality of the capital stock",
   "an increase in government spending",
   "a fall in the price level",
   "a fall in taxes with no supply-side effect"], ans=1,
   why="LRAS depends on real resources, technology, and institutions, not on demand."),
 dict(q="Which of the following would shift long-run aggregate supply to the left?", choices=[
   "an improvement in technology",
   "a war that destroys a large part of the capital stock",
   "an increase in the labor force",
   "improved education",
   "an increase in aggregate demand"], ans=1,
   why="Fewer productive resources means lower potential output."),
 dict(q="An increase in the labor force participation rate will, other things equal,", choices=[
   "reduce potential output",
   "increase potential output by increasing the quantity of labor available",
   "reduce productivity necessarily",
   "raise the price level in the long run",
   "have no effect on LRAS"], ans=1,
   why="More labor input raises the economy's capacity to produce."),
 dict(q="Investment in infrastructure such as roads, ports, and power grids raises growth because it", choices=[
   "increases consumption today",
   "lowers the cost of production and raises the productivity of private capital and labor",
   "reduces the money supply",
   "raises the price level permanently",
   "reduces human capital"], ans=1,
   why="Public capital makes private inputs more productive."),
 dict(q="Growth accounting attributes increases in output to", choices=[
   "changes in the price level",
   "growth in labor, growth in capital, and improvements in total factor productivity",
   "changes in velocity",
   "changes in the deficit",
   "shifts in aggregate demand"], ans=1,
   why="Output growth is decomposed into input growth and the residual improvement in efficiency."),
 dict(q="Total factor productivity measures", choices=[
   "output per worker only",
   "the efficiency with which all inputs together are converted into output",
   "the capital stock",
   "the number of hours worked",
   "the price level"], ans=1,
   why="It is the part of output growth not explained by measured increases in inputs."),
 dict(q="Two economies begin with the same output. One grows at 2 percent a year and the other at 4 percent. After 35 years,", choices=[
   "they will have the same output",
   "the faster-growing economy will have roughly twice the output of the slower one",
   "the difference will be trivial",
   "the slower one will have caught up",
   "output will be identical per capita"], ans=1,
   why="In 35 years the 2 percent economy doubles once while the 4 percent economy doubles roughly twice."),
 dict(q="Small differences in annual growth rates matter greatly over long periods because", choices=[
   "growth is linear",
   "growth compounds, so a small rate difference produces a large gap in levels over decades",
   "prices adjust",
   "the money supply grows",
   "population is constant"], ans=1,
   why="Compounding turns a fraction of a percentage point into a large difference in living standards."),
 dict(q="Which of the following raises real GDP in the short run but not potential output?", choices=[
   "an increase in the capital stock",
   "an increase in aggregate demand that closes a recessionary gap",
   "technological progress",
   "improved education",
   "better property rights"], ans=1,
   why="Closing a gap puts idle resources to work without expanding capacity."),
 dict(q="Economic growth generally allows an economy to", choices=[
   "eliminate scarcity",
   "produce more of both consumer and capital goods than before",
   "avoid all trade-offs",
   "abolish opportunity cost",
   "guarantee full employment"], ans=1,
   why="An outward shift of the PPC expands the attainable combinations without ending the need to choose."),
 dict(q="Which of the following best measures improvements in a country's standard of living?", choices=[
   "nominal GDP",
   "real GDP per capita",
   "the money supply",
   "total employment",
   "the price level"], ans=1,
   why="Adjusting for both prices and population is what makes the comparison meaningful."),
 dict(q="Depreciation of the capital stock means that", choices=[
   "capital never wears out",
   "some gross investment merely replaces worn-out capital, so net investment is smaller than gross investment",
   "investment always raises the capital stock one for one",
   "capital rises automatically",
   "growth is impossible"], ans=1,
   why="Only net investment adds to the productive capital stock."),
 dict(q="If gross investment is less than depreciation, the capital stock will", choices=[
   "grow", "shrink", "stay constant", "double", "be unaffected"], ans=1,
   why="Replacement falls short of wear and tear, so net investment is negative."),
 dict(q="A country experiencing rapid population growth with little capital accumulation is likely to see", choices=[
   "rising output per person",
   "falling or stagnant output per person even if total output rises",
   "an outward shift of the LRAS in per capita terms",
   "rapid growth in living standards",
   "a rise in productivity"], ans=1,
   why="Spreading a fixed capital stock across more workers lowers capital per worker."),
 dict(q="Which of the following would most directly raise labor productivity?", choices=[
   "an increase in the money supply",
   "widespread adoption of a new production technology",
   "an increase in government transfer payments",
   "a fall in interest rates that has no effect on investment",
   "a rise in the price level"], ans=1,
   why="Productivity is raised by better tools, better skills, or better methods."),
 dict(q="Sustained growth in real GDP with a constant price level would require", choices=[
   "aggregate demand to shift right while LRAS is fixed",
   "aggregate supply and aggregate demand to shift right by similar amounts",
   "aggregate demand to shift left",
   "the money supply to be fixed",
   "LRAS to shift left"], ans=1,
   why="Output can grow without inflation when capacity and spending expand together."),
 dict(q="The most important reason living standards differ so widely across countries is differences in", choices=[
   "population size",
   "productivity, which depends on capital, human capital, technology, and institutions",
   "the money supply",
   "the inflation rate",
   "the size of government budgets"], ans=1,
   why="Cross-country income differences track productivity differences almost exactly."),
]
