# 3.1 The Production Function — 50 questions
# Table verified: L 1-5, TP 10,25,35,40,42 -> MP 10,15,10,5,2 ; AP 10,12.5,11.67,10,8.4
TOPIC = ("3.1", "The Production Function", 3)
PROD = dict(headers=["Labor", "Total product"],
            rows=[["1", "10"], ["2", "25"], ["3", "35"], ["4", "40"], ["5", "42"]])
QUESTIONS = [
 dict(q="A production function shows the relationship between", choices=[
   "price and quantity demanded",
   "quantities of inputs used and the maximum output produced",
   "total revenue and total cost",
   "wages and profits",
   "supply and demand"], ans=1,
   why="The production function maps inputs to maximum attainable output."),
 dict(q="Total product (TP) is", choices=[
   "the extra output from one more worker",
   "the total quantity of output produced with a given quantity of inputs",
   "output per worker",
   "the cost of production",
   "revenue from output"], ans=1,
   why="Total product is the whole quantity produced."),
 dict(q="Marginal product of labor (MPL) is", choices=[
   "total output divided by workers",
   "the additional output produced by hiring one more worker",
   "the wage paid to the last worker",
   "total product times price",
   "the cost of an extra worker"], ans=1,
   why="MP is the change in total product from one additional unit of input."),
 dict(q="Average product of labor (APL) is calculated as", choices=[
   "change in TP ÷ change in labor",
   "total product ÷ quantity of labor",
   "total cost ÷ output",
   "marginal product × wage",
   "output × price"], ans=1,
   why="Average product is output per unit of input: TP/L."),
 dict(q="The law of diminishing marginal returns states that", choices=[
   "total product eventually falls to zero",
   "as more of a variable input is added to a fixed input, marginal product eventually declines",
   "average product always rises",
   "costs always fall as output rises",
   "all inputs are variable in the short run"], ans=1,
   why="Adding a variable input to fixed inputs eventually yields smaller output gains."),
 dict(q="Diminishing marginal returns occurs because", choices=[
   "workers become lazy",
   "additional variable inputs have less and less of the fixed input to work with",
   "wages rise",
   "prices fall",
   "technology worsens"], ans=1,
   why="A fixed factor spread across more workers reduces each worker's added output."),
 dict(q="The short run in production is defined as a period in which", choices=[
   "all inputs are variable",
   "at least one input is fixed",
   "no production occurs",
   "prices are constant",
   "firms cannot change output"], ans=1,
   why="At least one fixed input defines the short run."),
 dict(q="The long run in production is defined as a period in which", choices=[
   "at least one input is fixed",
   "all inputs, including plant size, are variable",
   "output is fixed",
   "only labor can change",
   "prices are fixed"], ans=1,
   why="In the long run every input can be adjusted."),
 dict(table=PROD, q="Using the table, the marginal product of the SECOND worker is", choices=[
   "10 units", "15 units", "25 units", "12.5 units", "35 units"], ans=1,
   why="TP rises from 10 to 25, so MP = 15."),
 dict(table=PROD, q="Using the table, the marginal product of the FOURTH worker is", choices=[
   "40 units", "10 units", "5 units", "2 units", "35 units"], ans=2,
   why="TP rises from 35 to 40, so MP = 5."),
 dict(table=PROD, q="Using the table, the average product when 2 workers are employed is", choices=[
   "10", "12.5", "15", "25", "35"], ans=1,
   why="AP = TP/L = 25/2 = 12.5."),
 dict(table=PROD, q="Using the table, diminishing marginal returns begin with the", choices=[
   "first worker", "second worker", "third worker", "fourth worker", "fifth worker"], ans=2,
   why="MP rises to 15 with the second worker, then falls to 10 with the third."),
 dict(table=PROD, q="Using the table, total product at 5 workers is", choices=[
   "2 units", "8.4 units", "40 units", "42 units", "35 units"], ans=3,
   why="The table reports TP of 42 at five workers."),
 dict(q="When marginal product is greater than average product, average product is", choices=[
   "falling", "rising", "constant", "at its maximum", "zero"], ans=1,
   why="A marginal value above the average pulls the average up."),
 dict(q="When marginal product is less than average product, average product is", choices=[
   "rising", "falling", "constant", "at its minimum", "negative"], ans=1,
   why="A marginal value below the average drags the average down."),
 dict(q="Marginal product intersects average product at", choices=[
   "the minimum of average product",
   "the maximum of average product",
   "the origin",
   "the point where MP is zero",
   "the point where TP is zero"], ans=1,
   why="MP cuts AP at AP's maximum, the standard marginal-average relationship."),
 dict(q="Total product is at its MAXIMUM when marginal product is", choices=[
   "at its maximum", "equal to average product", "zero", "negative", "rising"], ans=2,
   why="Output stops growing when the next worker adds nothing."),
 dict(q="If marginal product becomes NEGATIVE, total product is", choices=[
   "rising", "falling", "at a maximum", "constant", "zero"], ans=1,
   why="A negative marginal contribution reduces total output."),
 dict(q="In the range of increasing marginal returns, each additional worker adds", choices=[
   "less output than the previous worker",
   "more output than the previous worker",
   "exactly the same output",
   "no output",
   "negative output"], ans=1,
   why="Increasing marginal returns means MP is rising."),
 dict(q="Increasing marginal returns early in production often occurs because of", choices=[
   "diminishing returns",
   "gains from specialization and division of labor",
   "rising wages",
   "fixed costs",
   "falling prices"], ans=1,
   why="Early workers can specialize, raising each additional worker's contribution."),
 dict(q="Returns to scale describe what happens to output when", choices=[
   "only labor changes",
   "all inputs are increased proportionally in the long run",
   "prices change",
   "one input is fixed",
   "technology is fixed"], ans=1,
   why="Returns to scale is a long-run concept: all inputs scaled together."),
 dict(q="If a firm doubles all inputs and output MORE than doubles, the firm experiences", choices=[
   "constant returns to scale",
   "increasing returns to scale",
   "decreasing returns to scale",
   "diminishing marginal returns",
   "negative returns"], ans=1,
   why="Output rising proportionally more than inputs is increasing returns to scale."),
 dict(q="If a firm doubles all inputs and output exactly doubles, the firm experiences", choices=[
   "increasing returns to scale",
   "constant returns to scale",
   "decreasing returns to scale",
   "diminishing returns",
   "economies of scope"], ans=1,
   why="Proportional output growth is constant returns to scale."),
 dict(q="If a firm doubles all inputs and output LESS than doubles, the firm experiences", choices=[
   "increasing returns to scale",
   "constant returns to scale",
   "decreasing returns to scale",
   "increasing marginal returns",
   "perfect competition"], ans=2,
   why="Output rising proportionally less than inputs is decreasing returns to scale."),
 dict(q="Diminishing marginal returns differs from decreasing returns to scale because diminishing returns", choices=[
   "is a long-run concept",
   "occurs in the short run when one input is fixed",
   "means output falls",
   "applies only to capital",
   "requires all inputs to change"], ans=1,
   why="Diminishing returns is short-run (a fixed input); returns to scale is long-run."),
 dict(q="The factors of production in a firm's production function typically include", choices=[
   "revenue and profit",
   "land, labor, and capital",
   "price and quantity",
   "supply and demand",
   "taxes and subsidies"], ans=1,
   why="Production combines land, labor, capital (and entrepreneurship)."),
 dict(q="A firm using a fixed factory with an increasing number of workers is operating in", choices=[
   "the long run", "the short run", "a market period only", "perfect competition only", "the very long run"], ans=1,
   why="A fixed plant with variable labor is the definition of the short run."),
 dict(q="If total product is 120 with 10 workers, average product equals", choices=[
   "1,200", "120", "12", "10", "cannot be determined"], ans=2,
   why="AP = 120/10 = 12 units per worker."),
 dict(q="A firm's total product rises from 200 to 215 when the 21st worker is hired. The marginal product of that worker is", choices=[
   "215", "200", "15", "10.2", "21"], ans=2,
   why="MP = 215 − 200 = 15 units."),
 dict(q="Marginal product and marginal cost are inversely related because", choices=[
   "they are unrelated",
   "when a worker adds more output, the cost of each extra unit of output falls",
   "wages rise with output",
   "fixed costs vary",
   "prices determine costs"], ans=1,
   why="Higher productivity spreads the wage over more units, lowering MC."),
 dict(q="If marginal product is falling, marginal cost is most likely", choices=[
   "falling", "rising", "constant", "zero", "negative"], ans=1,
   why="Diminishing returns raise the cost of producing each additional unit."),
 dict(q="Which of the following would shift a firm's entire production function upward?", choices=[
   "Hiring more workers",
   "An improvement in technology",
   "A fall in the wage rate",
   "An increase in output price",
   "A rise in demand"], ans=1,
   why="Better technology raises output attainable from the same inputs."),
 dict(q="A firm experiencing negative marginal product should", choices=[
   "hire more workers",
   "reduce the number of workers, since output would rise",
   "raise prices",
   "increase fixed costs",
   "shut down permanently"], ans=1,
   why="If extra workers reduce output, cutting back raises total product."),
 dict(q="Which statement about the three stages of production is correct?", choices=[
   "Firms should always produce where MP is negative",
   "Rational production occurs where marginal product is positive but diminishing",
   "Firms maximize AP always",
   "Stage of production is irrelevant",
   "Firms should produce where TP is zero"], ans=1,
   why="Rational short-run production lies in the diminishing-but-positive MP range."),
 dict(q="Specialization of labor within a firm tends to", choices=[
   "reduce total product",
   "raise marginal product in the early range of hiring",
   "eliminate diminishing returns entirely",
   "raise fixed costs",
   "lower output per worker immediately"], ans=1,
   why="Division of labor boosts productivity while there is capital to work with."),
 dict(q="Human capital improvements raise a firm's output because they", choices=[
   "reduce the number of workers",
   "increase the productivity of each worker",
   "lower output prices",
   "raise fixed costs",
   "eliminate the need for capital"], ans=1,
   why="Better skills mean more output from the same labor input."),
 dict(q="A restaurant kitchen of fixed size hires more cooks. Eventually output per additional cook falls because", choices=[
   "cooks become unskilled",
   "the fixed kitchen space and equipment must be shared among more cooks",
   "wages fall",
   "demand falls",
   "prices rise"], ans=1,
   why="The fixed input becomes the bottleneck — classic diminishing returns."),
 dict(q="If a firm's average product of labor is rising, then marginal product must be", choices=[
   "falling below average product",
   "above average product",
   "zero",
   "negative",
   "equal to average product"], ans=1,
   why="Only a marginal value above the average can pull the average up."),
 dict(q="Total product, marginal product, and average product are all measured in units of", choices=[
   "dollars", "output", "labor hours only", "prices", "revenue"], ans=1,
   why="All three are physical output measures, not monetary values."),
 dict(q="Which of the following is a FIXED input for a bakery in the short run?", choices=[
   "Flour", "Hourly bakers", "The oven and building", "Electricity used per loaf", "Packaging"], ans=2,
   why="Plant and major equipment cannot be varied in the short run."),
 dict(q="Which of the following is a VARIABLE input for a bakery in the short run?", choices=[
   "The building lease", "The number of ovens", "Hours of baker labor", "Property taxes", "The mortgage"], ans=2,
   why="Labor hours can be adjusted quickly."),
 dict(q="A production function exhibiting constant returns to scale means that doubling inputs", choices=[
   "triples output", "doubles output", "halves output", "leaves output unchanged", "eliminates costs"], ans=1,
   why="Constant returns: output scales exactly with inputs."),
 dict(q="If a firm's marginal product of labor is 8 units and the wage is $16, the marginal cost of output is", choices=[
   "$128", "$24", "$8", "$2", "$16"], ans=3,
   why="MC = wage / MPL = 16/8 = $2 per unit."),
 dict(q="A firm with MPL of 4 and a wage of $20 has a marginal cost per unit of", choices=[
   "$80", "$24", "$16", "$5", "$4"], ans=3,
   why="MC = 20/4 = $5 per unit of output."),
 dict(q="Which of the following best explains why marginal product eventually declines but total product may still rise?", choices=[
   "Total product falls whenever MP falls",
   "Each worker still adds some output, just less than the previous one",
   "MP and TP are unrelated",
   "TP is always constant",
   "MP is always negative"], ans=1,
   why="Positive but shrinking additions still increase the total."),
 dict(q="Returns to scale become relevant only in the long run because", choices=[
   "output is fixed in the short run",
   "all inputs must be variable to scale them proportionally",
   "prices change only in the long run",
   "labor is fixed",
   "technology changes"], ans=1,
   why="Scaling every input requires the long run."),
 dict(q="Decreasing returns to scale often arise from", choices=[
   "specialization gains",
   "coordination and management difficulties as the firm grows very large",
   "falling input prices",
   "improved technology",
   "diminishing marginal returns to a fixed input"], ans=1,
   why="Large organizations face rising coordination costs."),
 dict(q="If a firm hires a 6th worker and total product remains unchanged at 42 units, the marginal product of that worker is", choices=[
   "42", "7", "1", "0", "−42"], ans=3,
   why="No change in total product means MP = 0."),
 dict(q="Which change would allow a firm to escape diminishing marginal returns?", choices=[
   "Hiring even more workers",
   "Expanding the fixed input, such as building a larger plant, in the long run",
   "Lowering wages",
   "Raising output price",
   "Reducing output"], ans=1,
   why="Only relaxing the fixed constraint removes the short-run bottleneck."),
 dict(q="The primary reason economists study the production function is to", choices=[
   "measure consumer utility",
   "derive the firm's cost structure and ultimately its supply decisions",
   "set market prices",
   "calculate taxes",
   "measure inflation"], ans=1,
   why="Productivity determines costs, which determine supply."),
]
assert len(QUESTIONS) == 50, len(QUESTIONS)
