# 3.2 Short-Run Production Costs — 50 questions
# Table verified: FC=100
#   Q=1 VC=50  TC=150 AFC=100   AVC=50 ATC=150   MC=50
#   Q=2 VC=90  TC=190 AFC=50    AVC=45 ATC=95    MC=40
#   Q=3 VC=150 TC=250 AFC=33.33 AVC=50 ATC=83.33 MC=60
#   Q=4 VC=240 TC=340 AFC=25    AVC=60 ATC=85    MC=90
TOPIC = ("3.2", "Short-Run Production Costs", 3)
COST = dict(headers=["Output", "Fixed cost", "Variable cost"],
            rows=[["1", "100", "50"], ["2", "100", "90"],
                  ["3", "100", "150"], ["4", "100", "240"]])
QUESTIONS = [
 dict(q="A fixed cost is a cost that", choices=[
   "changes as output changes",
   "does not change as output changes in the short run",
   "is zero when output is zero",
   "equals marginal cost",
   "only occurs in the long run"], ans=1,
   why="Fixed costs are incurred regardless of the quantity produced in the short run."),
 dict(q="A variable cost is a cost that", choices=[
   "stays the same at every level of output",
   "rises and falls with the quantity of output produced",
   "is always larger than fixed cost",
   "is paid only when the firm shuts down",
   "equals average total cost"], ans=1,
   why="Variable costs move with output; payments for labor and materials are typical examples."),
 dict(q="Which of the following is most likely a fixed cost for a bakery in the short run?", choices=[
   "flour purchased each week",
   "the monthly lease payment on the bakery building",
   "wages of hourly bakers",
   "electricity used by the ovens",
   "packaging for each loaf sold"], ans=1,
   why="A lease payment is owed whether or not any bread is baked."),
 dict(q="Which of the following is a variable cost for a bakery?", choices=[
   "the annual insurance premium on the building",
   "flour and sugar used to bake each cake",
   "the fixed monthly rent",
   "the purchase price of an oven bought last year",
   "the business license fee"], ans=1,
   why="Ingredient costs rise directly with the number of cakes produced."),
 dict(q="Total cost is equal to", choices=[
   "fixed cost minus variable cost",
   "fixed cost plus variable cost",
   "average cost times fixed cost",
   "marginal cost times fixed cost",
   "variable cost divided by output"], ans=1,
   why="TC = FC + VC by definition."),
 dict(q="Marginal cost is", choices=[
   "total cost divided by output",
   "the change in total cost from producing one more unit of output",
   "fixed cost per unit",
   "the cost of the first unit produced",
   "variable cost divided by output"], ans=1,
   why="MC is the additional cost of one more unit: ΔTC/ΔQ."),
 dict(q="Average total cost is calculated as", choices=[
   "total cost times output",
   "total cost divided by quantity of output",
   "the change in total cost divided by the change in quantity",
   "fixed cost divided by variable cost",
   "total revenue divided by output"], ans=1,
   why="ATC = TC/Q."),
 dict(q="Average fixed cost (AFC) as output increases", choices=[
   "rises continuously",
   "falls continuously, approaching zero but never reaching it",
   "stays constant",
   "first falls then rises",
   "equals marginal cost"], ans=1,
   why="A constant fixed cost spread over more units always shrinks per unit."),
 dict(q="Average variable cost is equal to", choices=[
   "variable cost times output",
   "variable cost divided by quantity of output",
   "total cost minus fixed cost",
   "the change in variable cost",
   "average total cost plus average fixed cost"], ans=1,
   why="AVC = VC/Q."),
 dict(q="ATC can also be written as", choices=[
   "AFC minus AVC",
   "AFC plus AVC",
   "MC plus AFC",
   "TC times Q",
   "AVC minus MC"], ans=1,
   why="Dividing TC = FC + VC through by Q gives ATC = AFC + AVC."),
 dict(q="Using the table, what is total cost when output is 2?", table=COST, choices=[
   "$90", "$100", "$150", "$190", "$240"], ans=3,
   why="TC = FC + VC = 100 + 90 = $190."),
 dict(q="Using the table, what is total cost when output is 4?", table=COST, choices=[
   "$240", "$250", "$300", "$340", "$400"], ans=3,
   why="TC = 100 + 240 = $340."),
 dict(q="Using the table, what is the marginal cost of the second unit?", table=COST, choices=[
   "$20", "$40", "$45", "$50", "$90"], ans=1,
   why="VC rises from 50 to 90, so MC = $40. Fixed cost does not affect MC."),
 dict(q="Using the table, what is the marginal cost of the third unit?", table=COST, choices=[
   "$40", "$50", "$60", "$83", "$150"], ans=2,
   why="TC rises from 190 to 250, so MC = $60."),
 dict(q="Using the table, what is the marginal cost of the fourth unit?", table=COST, choices=[
   "$60", "$70", "$85", "$90", "$240"], ans=3,
   why="TC rises from 250 to 340, so MC = $90."),
 dict(q="Using the table, what is average total cost at an output of 2?", table=COST, choices=[
   "$45", "$50", "$90", "$95", "$190"], ans=3,
   why="ATC = 190/2 = $95."),
 dict(q="Using the table, what is average variable cost at an output of 2?", table=COST, choices=[
   "$40", "$45", "$50", "$90", "$95"], ans=1,
   why="AVC = 90/2 = $45."),
 dict(q="Using the table, what is average fixed cost at an output of 4?", table=COST, choices=[
   "$25", "$33", "$50", "$60", "$100"], ans=0,
   why="AFC = 100/4 = $25."),
 dict(q="Using the table, at which output is average total cost lowest?", table=COST, choices=[
   "1", "2", "3", "4", "ATC is the same at every output"], ans=2,
   why="ATC is 150, 95, about 83.33, and 85, so the minimum occurs at 3 units."),
 dict(q="Using the table, average variable cost at an output of 3 is", table=COST, choices=[
   "$45", "$50", "$60", "$83", "$150"], ans=1,
   why="AVC = 150/3 = $50."),
 dict(q="Marginal cost is not affected by fixed cost because", choices=[
   "fixed cost is always zero",
   "fixed cost does not change when output changes, so it drops out of the change in total cost",
   "fixed cost is paid after production",
   "marginal cost measures only revenue",
   "fixed cost is a long-run concept only"], ans=1,
   why="MC is a change in total cost, and an unchanging component contributes nothing to that change."),
 dict(q="The marginal cost curve is typically U-shaped because of", choices=[
   "rising then falling prices",
   "increasing marginal returns at low output followed by diminishing marginal returns",
   "constant returns to scale",
   "changes in fixed cost",
   "government regulation"], ans=1,
   why="MC falls while marginal product rises and rises once diminishing marginal returns set in."),
 dict(q="When marginal product of labor is rising, marginal cost is", choices=[
   "rising", "falling", "constant", "zero", "negative"], ans=1,
   why="MC and MP move inversely: more added output per worker means a lower cost per added unit."),
 dict(q="When marginal product of labor is falling, marginal cost is", choices=[
   "falling", "rising", "constant", "zero", "undefined"], ans=1,
   why="Diminishing marginal returns raise the cost of each additional unit."),
 dict(q="Marginal cost intersects average total cost", choices=[
   "at the maximum of ATC",
   "at the minimum of ATC",
   "where ATC equals AFC",
   "at zero output",
   "never"], ans=1,
   why="A marginal value pulls an average down while below it and up while above it, so they cross at the average's minimum."),
 dict(q="Marginal cost intersects average variable cost at", choices=[
   "the maximum of AVC",
   "the minimum of AVC",
   "the point where AVC equals ATC",
   "zero output",
   "the minimum of AFC"], ans=1,
   why="The same marginal-average relationship applies to AVC."),
 dict(q="When marginal cost is below average total cost, average total cost is", choices=[
   "rising", "falling", "at its minimum", "constant", "equal to marginal cost"], ans=1,
   why="Adding a unit that costs less than the current average pulls the average down."),
 dict(q="When marginal cost is above average total cost, average total cost is", choices=[
   "falling", "rising", "at its minimum", "constant", "negative"], ans=1,
   why="A unit costing more than the average pulls the average up."),
 dict(q="The vertical distance between the ATC and AVC curves represents", choices=[
   "marginal cost", "average fixed cost", "total fixed cost", "profit", "total variable cost"], ans=1,
   why="ATC − AVC = AFC at every output."),
 dict(q="As output increases, the gap between the ATC and AVC curves", choices=[
   "widens", "narrows", "stays constant", "first narrows then widens", "becomes negative"], ans=1,
   why="That gap is AFC, which shrinks as fixed cost is spread over more units."),
 dict(q="A firm's total fixed cost is $500 and it produces 100 units. Average fixed cost is", choices=[
   "$0.20", "$5", "$50", "$500", "$5,000"], ans=1,
   why="AFC = 500/100 = $5."),
 dict(q="If total cost is $800 at 40 units and $860 at 41 units, marginal cost of the 41st unit is", choices=[
   "$20", "$21", "$60", "$80", "$860"], ans=2,
   why="MC = 860 − 800 = $60."),
 dict(q="A firm produces 20 units at a total cost of $600, of which $200 is fixed. AVC equals", choices=[
   "$10", "$20", "$30", "$40", "$400"], ans=1,
   why="VC = 600 − 200 = $400, so AVC = 400/20 = $20."),
 dict(q="A firm has ATC of $12 and AVC of $9 at 50 units. Total fixed cost is", choices=[
   "$3", "$50", "$150", "$450", "$600"], ans=2,
   why="AFC = 12 − 9 = $3, so TFC = 3 × 50 = $150."),
 dict(q="At an output of zero, total cost equals", choices=[
   "zero", "total fixed cost", "total variable cost", "marginal cost", "average total cost"], ans=1,
   why="With no production, variable cost is zero and only fixed cost remains."),
 dict(q="At an output of zero, average total cost is", choices=[
   "zero", "undefined, because dividing by zero output is not possible", "equal to fixed cost",
   "equal to marginal cost", "at its minimum"], ans=1,
   why="ATC = TC/Q requires a positive Q."),
 dict(q="The total variable cost curve starts at the origin because", choices=[
   "fixed costs are zero",
   "producing zero output requires no variable inputs",
   "marginal cost is zero at low output",
   "average cost is zero",
   "firms always shut down"], ans=1,
   why="With nothing produced, no labor or materials are used."),
 dict(q="An increase in the rent a firm pays for its factory will", choices=[
   "shift the marginal cost curve upward",
   "shift the average total cost curve upward but leave marginal cost unchanged",
   "shift average variable cost upward",
   "lower average fixed cost",
   "have no effect on any cost curve"], ans=1,
   why="Rent is fixed, so it raises ATC through AFC but does not change the cost of an extra unit."),
 dict(q="An increase in the hourly wage a firm pays will", choices=[
   "shift only average fixed cost",
   "shift marginal cost, average variable cost, and average total cost upward",
   "leave marginal cost unchanged",
   "shift average total cost downward",
   "have no effect in the short run"], ans=1,
   why="Wages are a variable cost, so every variable and marginal measure rises."),
 dict(q="An improvement in technology that raises output per worker will", choices=[
   "shift the cost curves upward",
   "shift the marginal and average cost curves downward",
   "raise average fixed cost",
   "leave marginal cost unchanged",
   "reduce total product"], ans=1,
   why="Higher productivity lowers the cost of producing each unit."),
 dict(q="A firm's payment of $3,000 for raw materials this month is an example of", choices=[
   "an implicit cost with no money payment",
   "an explicit cost, since it is an actual monetary payment for an input",
   "a normal profit",
   "a cost never recorded in accounting records",
   "the same thing as marginal cost"], ans=1,
   why="Explicit costs involve an actual payment to an outside party."),
 dict(q="The rent a shop owner gives up by using a building she owns is an example of", choices=[
   "a monetary payment to a supplier",
   "an implicit cost, the opportunity cost of a resource the firm already owns",
   "a variable cost that rises with output",
   "an item recorded on the firm's income statement",
   "a cost that is always zero in the short run"], ans=1,
   why="Forgone rent on an owned resource is an opportunity cost with no cash payment."),
 dict(q="An owner who gives up a $60,000 salary to run her own shop has incurred", choices=[
   "an explicit cost of $60,000",
   "an implicit cost of $60,000",
   "a fixed cost of zero",
   "a marginal cost of $60,000",
   "no cost at all"], ans=1,
   why="The forgone salary is an opportunity cost with no cash payment."),
 dict(q="Which of the following best describes the short run for a firm?", choices=[
   "a period shorter than one year",
   "a period in which at least one input, such as plant size, cannot be changed",
   "a period in which all inputs can be varied",
   "a period in which no costs are incurred",
   "the time it takes to sell inventory"], ans=1,
   why="The short run is defined by the presence of a fixed input, not by calendar length."),
 dict(q="The law of diminishing marginal returns implies that the marginal cost curve eventually", choices=[
   "falls", "rises", "becomes horizontal", "becomes vertical at zero output", "disappears"], ans=1,
   why="Falling marginal product means each additional unit costs more to produce."),
 dict(q="A firm's total cost rises from $1,200 to $1,200 when output rises from 8 to 9 units. Marginal cost of the ninth unit is", choices=[
   "$0", "$1,200", "$133", "$150", "cannot be determined"], ans=0,
   why="MC is the change in total cost, and total cost did not change."),
 dict(q="If AVC is $30 and AFC is $10 at 25 units, total cost equals", choices=[
   "$250", "$400", "$750", "$1,000", "$1,250"], ans=3,
   why="ATC = 30 + 10 = $40, so TC = 40 × 25 = $1,000."),
 dict(q="Sunk costs are best described as costs that", choices=[
   "vary with output",
   "have already been incurred and cannot be recovered",
   "will be paid in the future",
   "equal marginal cost",
   "always equal fixed cost in the long run"], ans=1,
   why="A sunk cost is unrecoverable and therefore irrelevant to a forward-looking decision."),
 dict(q="A rational firm deciding whether to produce one more unit should ignore", choices=[
   "the marginal cost of that unit",
   "sunk costs already paid",
   "the price it can charge",
   "marginal revenue",
   "the additional labor required"], ans=1,
   why="Only costs that change with the decision are relevant."),
 dict(q="In the short run, the shape of a firm's cost curves is determined primarily by", choices=[
   "the market price of output",
   "the productivity of its variable inputs given its fixed inputs",
   "consumer preferences",
   "the number of firms in the industry",
   "government tax policy"], ans=1,
   why="Cost curves are the production function read in dollar terms."),
]
