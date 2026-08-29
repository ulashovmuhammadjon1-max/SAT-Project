# 3.4 Types of Profit — 50 questions
# Table verified: revenue 200,000; explicit 120,000; implicit (forgone salary 50,000 +
#   forgone interest 5,000) = 55,000
#   accounting profit = 200,000 - 120,000 = 80,000
#   economic profit    = 200,000 - 175,000 = 25,000
TOPIC = ("3.4", "Types of Profit", 3)
PROFIT = dict(headers=["Item", "Amount"],
              rows=[["Total revenue", "$200,000"], ["Wages, rent, materials paid", "$120,000"],
                    ["Salary given up by the owner", "$50,000"],
                    ["Interest given up on the owner's invested savings", "$5,000"]])
QUESTIONS = [
 dict(q="Accounting profit is equal to", choices=[
   "total revenue minus implicit costs",
   "total revenue minus explicit costs",
   "total revenue minus explicit and implicit costs",
   "explicit costs minus implicit costs",
   "total revenue plus implicit costs"], ans=1,
   why="Accounting profit subtracts only the payments the firm actually makes."),
 dict(q="Economic profit is equal to", choices=[
   "total revenue minus explicit costs",
   "total revenue minus the sum of explicit and implicit costs",
   "accounting profit plus implicit costs",
   "implicit costs minus explicit costs",
   "total revenue minus fixed costs"], ans=1,
   why="Economic profit counts every opportunity cost, paid or forgone."),
 dict(q="Explicit costs are", choices=[
   "opportunity costs that involve no money payment",
   "actual monetary payments a firm makes to others for resources",
   "the owner's forgone salary",
   "always zero in the short run",
   "the same as economic profit"], ans=1,
   why="Explicit costs are out-of-pocket payments."),
 dict(q="Implicit costs are", choices=[
   "payments to workers and suppliers",
   "the opportunity costs of resources the owner already owns and supplies to the firm",
   "recorded in the firm's financial statements",
   "always larger than explicit costs",
   "the same as fixed costs"], ans=1,
   why="Implicit costs value owner-supplied resources at their next-best use."),
 dict(q="Because implicit costs are positive, economic profit is generally", choices=[
   "larger than accounting profit",
   "smaller than accounting profit",
   "equal to accounting profit",
   "always negative",
   "always zero"], ans=1,
   why="Economic profit subtracts everything accounting profit subtracts, plus more."),
 dict(q="Using the table, this firm's accounting profit is", table=PROFIT, choices=[
   "$25,000", "$45,000", "$80,000", "$130,000", "$200,000"], ans=2,
   why="200,000 − 120,000 in explicit costs = $80,000."),
 dict(q="Using the table, this firm's total implicit costs are", table=PROFIT, choices=[
   "$5,000", "$50,000", "$55,000", "$120,000", "$175,000"], ans=2,
   why="The forgone salary of $50,000 plus forgone interest of $5,000."),
 dict(q="Using the table, this firm's economic profit is", table=PROFIT, choices=[
   "$0", "$25,000", "$55,000", "$80,000", "$105,000"], ans=1,
   why="200,000 − (120,000 + 55,000) = $25,000."),
 dict(q="Using the table, the owner of this firm should", table=PROFIT, choices=[
   "close the business, since economic profit is negative",
   "continue the business, since economic profit is positive",
   "be indifferent, since economic profit is zero",
   "raise price to eliminate implicit costs",
   "ignore the forgone salary"], ans=1,
   why="A positive economic profit means the business beats the owner's next-best alternative."),
 dict(q="Using the table, the difference between accounting and economic profit here is exactly", table=PROFIT, choices=[
   "total revenue", "explicit costs", "implicit costs", "fixed costs", "marginal cost"], ans=2,
   why="80,000 − 25,000 = 55,000, the implicit costs."),
 dict(q="Normal profit is best defined as", choices=[
   "the maximum profit a firm can earn",
   "the level of accounting profit just equal to the firm's implicit costs, so economic profit is zero",
   "any positive accounting profit",
   "profit before taxes",
   "total revenue minus variable cost"], ans=1,
   why="Normal profit is the return needed to keep resources in their current use."),
 dict(q="When a firm earns zero economic profit, it is earning", choices=[
   "nothing at all",
   "a normal profit, exactly covering all opportunity costs",
   "negative accounting profit",
   "the maximum possible profit",
   "more than its implicit costs"], ans=1,
   why="Zero economic profit means the owner does exactly as well here as in the next-best alternative."),
 dict(q="A firm with zero economic profit should", choices=[
   "shut down immediately",
   "stay in business, since it is doing as well as its next-best alternative",
   "raise price",
   "exit the industry",
   "reduce output to zero"], ans=1,
   why="There is no better use of the resources, so exiting gains nothing."),
 dict(q="Normal profit is treated by economists as", choices=[
   "an explicit cost",
   "a cost of doing business, specifically an implicit cost",
   "pure surplus",
   "revenue",
   "a fixed cost paid in cash"], ans=1,
   why="Keeping the entrepreneur in this line of work has an opportunity cost."),
 dict(q="A firm has revenue of $500,000 and explicit costs of $380,000. Its accounting profit is", choices=[
   "$120,000", "$380,000", "$500,000", "$880,000", "cannot be determined"], ans=0,
   why="500,000 − 380,000 = $120,000."),
 dict(q="A firm has revenue of $500,000, explicit costs of $380,000, and implicit costs of $90,000. Its economic profit is", choices=[
   "$30,000", "$90,000", "$120,000", "$210,000", "$470,000"], ans=0,
   why="500,000 − 380,000 − 90,000 = $30,000."),
 dict(q="A firm has revenue of $300,000, explicit costs of $250,000, and implicit costs of $70,000. Its economic profit is", choices=[
   "$50,000", "−$20,000", "$20,000", "−$70,000", "$120,000"], ans=1,
   why="300,000 − 320,000 = −$20,000, an economic loss."),
 dict(q="A firm with positive accounting profit but negative economic profit is", choices=[
   "clearly thriving",
   "earning less than it could in its owner's next-best alternative",
   "in violation of accounting rules",
   "earning normal profit",
   "certain to be losing cash"], ans=1,
   why="Cash is coming in, but the resources would earn more elsewhere."),
 dict(q="Ana quits a $70,000 job to open a bakery. Revenue is $260,000 and explicit costs are $200,000. Her economic profit is", choices=[
   "$60,000", "−$10,000", "$10,000", "$70,000", "−$70,000"], ans=1,
   why="260,000 − 200,000 − 70,000 = −$10,000."),
 dict(q="In the previous scenario, Ana's accounting profit is", choices=[
   "−$10,000", "$60,000", "$70,000", "$130,000", "$260,000"], ans=1,
   why="Accounting profit ignores the forgone salary: 260,000 − 200,000 = $60,000."),
 dict(q="A shop owner uses a building she owns rather than renting it out for $24,000 a year. The $24,000 is", choices=[
   "an explicit cost",
   "an implicit cost",
   "revenue",
   "accounting profit",
   "not a cost at all"], ans=1,
   why="Forgone rent is an opportunity cost with no cash payment."),
 dict(q="A firm that pays $80,000 in wages has incurred", choices=[
   "an implicit cost",
   "an explicit cost",
   "a normal profit",
   "an economic profit",
   "a sunk revenue"], ans=1,
   why="Wages are an actual money payment."),
 dict(q="Which of the following would appear on an accountant's income statement but not as an implicit cost?", choices=[
   "the owner's forgone salary",
   "the electricity bill",
   "forgone interest on the owner's savings",
   "forgone rent on the owner's building",
   "the value of the owner's time"], ans=1,
   why="Utility bills are explicit payments."),
 dict(q="Economic profit is a better guide than accounting profit for deciding whether to stay in a business because it", choices=[
   "is always larger",
   "accounts for the value of the best alternative use of the owner's resources",
   "excludes wages",
   "is required by tax law",
   "ignores implicit costs"], ans=1,
   why="Only economic profit answers whether this use of resources beats the alternatives."),
 dict(q="If economic profit in an industry is positive, in the long run we expect", choices=[
   "firms to exit",
   "new firms to enter, attracted by returns above the normal level",
   "no change",
   "prices to rise",
   "implicit costs to disappear"], ans=1,
   why="Above-normal returns draw resources into the industry."),
 dict(q="If economic profit in an industry is negative, in the long run we expect", choices=[
   "new firms to enter",
   "firms to exit, since resources earn more elsewhere",
   "no change",
   "accounting profit to become negative immediately",
   "implicit costs to fall to zero"], ans=1,
   why="Below-normal returns push resources out of the industry."),
 dict(q="In long-run equilibrium in a perfectly competitive industry, firms earn", choices=[
   "positive economic profit",
   "zero economic profit, or normal profit",
   "negative economic profit",
   "zero accounting profit",
   "the maximum possible accounting profit"], ans=1,
   why="Free entry and exit competes economic profit away to zero."),
 dict(q="A firm earning zero accounting profit is", choices=[
   "earning normal profit",
   "earning a negative economic profit, since implicit costs are unpaid",
   "in long-run equilibrium",
   "earning positive economic profit",
   "necessarily shutting down today"], ans=1,
   why="With revenue only covering explicit costs, implicit costs are uncovered."),
 dict(q="Total revenue is calculated as", choices=[
   "price times quantity sold",
   "price minus average total cost",
   "quantity divided by price",
   "profit plus implicit cost",
   "marginal revenue times price"], ans=0,
   why="TR = P × Q."),
 dict(q="A firm sells 400 units at $25 each. Total revenue is", choices=[
   "$425", "$1,600", "$10,000", "$16", "$40,000"], ans=2,
   why="25 × 400 = $10,000."),
 dict(q="A firm sells 300 units at $40 each with total costs of $9,000. Its profit is", choices=[
   "$3,000", "$9,000", "$12,000", "$21,000", "$30"], ans=0,
   why="TR = 12,000; 12,000 − 9,000 = $3,000."),
 dict(q="Profit can also be written per unit as", choices=[
   "(price − average total cost) × quantity",
   "price × quantity",
   "average total cost × quantity",
   "price − marginal cost",
   "total revenue − marginal cost"], ans=0,
   why="Per-unit profit times units sold gives total profit."),
 dict(q="A firm sells 200 units at $18 each with an average total cost of $15. Its profit is", choices=[
   "$3", "$600", "$3,000", "$3,600", "$600 loss"], ans=1,
   why="(18 − 15) × 200 = $600."),
 dict(q="A firm sells 150 units at $10 each with an average total cost of $12. It is earning", choices=[
   "a profit of $300", "a loss of $300", "a profit of $2", "zero profit", "a loss of $2"], ans=1,
   why="(10 − 12) × 150 = −$300."),
 dict(q="If price equals average total cost, the firm is earning", choices=[
   "positive economic profit",
   "zero economic profit",
   "an economic loss",
   "negative accounting profit",
   "maximum profit"], ans=1,
   why="Revenue exactly covers total cost including all opportunity costs."),
 dict(q="If price is greater than average total cost, the firm earns", choices=[
   "a loss", "positive economic profit", "zero economic profit", "normal profit only", "no revenue"], ans=1,
   why="Each unit sells for more than it costs on average."),
 dict(q="Entrepreneurial ability is treated as a factor of production whose payment is", choices=[
   "wages", "profit", "rent", "interest", "explicit cost"], ans=1,
   why="Profit is the return to entrepreneurship in the four-factor framework."),
 dict(q="An owner considering whether to keep operating should compare", choices=[
   "accounting profit with zero",
   "economic profit with zero",
   "total revenue with fixed cost",
   "explicit cost with implicit cost",
   "marginal cost with average fixed cost"], ans=1,
   why="Economic profit is the measure that already includes the alternative's value."),
 dict(q="Which of the following is an implicit cost for a self-employed consultant?", choices=[
   "the fee she pays for accounting software",
   "the salary she could earn at a consulting firm",
   "her office internet bill",
   "printing costs for client reports",
   "the taxes she remits"], ans=1,
   why="Forgone earnings elsewhere are an opportunity cost, not a payment."),
 dict(q="A firm's economic profit is zero. Its accounting profit is", choices=[
   "zero", "positive and equal to its implicit costs", "negative", "greater than total revenue", "undefined"], ans=1,
   why="Economic profit = accounting profit − implicit costs, so accounting profit must equal implicit costs."),
 dict(q="Two businesses have identical accounting profits, but one owner gave up a much higher-paying job. That owner's business has", choices=[
   "higher economic profit",
   "lower economic profit",
   "the same economic profit",
   "no implicit costs",
   "higher accounting profit"], ans=1,
   why="A larger forgone salary means larger implicit costs and less economic profit."),
 dict(q="A firm has $600,000 revenue, $400,000 explicit costs, and the owner gave up a $150,000 salary and $20,000 of interest. Economic profit is", choices=[
   "$200,000", "$30,000", "$50,000", "−$30,000", "$170,000"], ans=1,
   why="600,000 − 400,000 − 170,000 = $30,000."),
 dict(q="In the previous scenario, the firm's accounting profit is", choices=[
   "$30,000", "$170,000", "$200,000", "$400,000", "$600,000"], ans=2,
   why="600,000 − 400,000 = $200,000."),
 dict(q="An economist would say a firm earning exactly normal profit is", choices=[
   "failing",
   "doing as well as it could in any alternative use of its resources",
   "earning above-normal returns",
   "certain to exit",
   "earning zero accounting profit"], ans=1,
   why="Normal profit is precisely the break-even point in opportunity-cost terms."),
 dict(q="Which of the following raises a firm's implicit costs without changing its explicit costs?", choices=[
   "an increase in the wage it pays its employees",
   "an increase in the salary the owner could earn elsewhere",
   "an increase in the price of raw materials",
   "a rise in the firm's rent payment",
   "a new tax on inputs"], ans=1,
   why="A better outside option raises the opportunity cost of staying."),
 dict(q="Which of the following raises explicit costs?", choices=[
   "an improvement in the owner's outside job offer",
   "a rise in the market rent the firm pays for its leased warehouse",
   "an increase in the interest the owner could earn on savings",
   "an increase in the resale value of the owner's building",
   "an increase in the owner's leisure value"], ans=1,
   why="A higher rent payment is money actually paid out."),
 dict(q="An entrepreneur values her own unpaid labor in the business at $40,000 a year. Ignoring this in the profit calculation would", choices=[
   "understate accounting profit",
   "overstate economic profit by $40,000",
   "understate economic profit by $40,000",
   "have no effect on either measure",
   "overstate accounting profit"], ans=1,
   why="Omitting an implicit cost makes economic profit look $40,000 larger than it is."),
 dict(q="Economic profit is sometimes called", choices=[
   "gross profit", "above-normal or supernormal profit when positive", "net revenue", "accounting surplus", "operating margin"], ans=1,
   why="Positive economic profit is a return above what is needed to keep resources in place."),
 dict(q="If all firms in an industry earn positive economic profit, resources are", choices=[
   "being drawn away from the industry",
   "earning more in this industry than in their next-best use",
   "earning exactly their opportunity cost",
   "misallocated toward other industries",
   "unpaid"], ans=1,
   why="That is what a positive economic profit means, and it is why entry follows."),
 dict(q="The main reason accounting profit and economic profit differ is that accountants", choices=[
   "use different revenue figures",
   "record only transactions involving actual payments, omitting opportunity costs",
   "always overstate costs",
   "include implicit costs twice",
   "ignore revenue from sales"], ans=1,
   why="Financial statements record payments, not forgone alternatives."),
]
