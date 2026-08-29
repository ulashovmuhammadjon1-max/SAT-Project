# 5.3 Profit-Maximizing Behavior in Perfectly Competitive Factor Markets — 50 questions
# Table verified: product price $4 (competitive product market), wage $24
#   L=1 TP=15 MP=15 MRP=60
#   L=2 TP=27 MP=12 MRP=48
#   L=3 TP=36 MP=9  MRP=36
#   L=4 TP=42 MP=6  MRP=24  <- hire here at a wage of $24
#   L=5 TP=45 MP=3  MRP=12
TOPIC = ("5.3", "Profit-Maximizing Behavior in Perfectly Competitive Factor Markets", 5)
HIRE = dict(headers=["Workers", "Total product"],
            rows=[["1", "15"], ["2", "27"], ["3", "36"], ["4", "42"], ["5", "45"]])
QUESTIONS = [
 dict(q="A perfectly competitive factor market is one in which", choices=[
   "a single firm hires all the workers",
   "many firms hire many workers and no single participant can affect the wage",
   "the government sets the wage",
   "workers have no alternatives",
   "there is only one buyer of labor"], ans=1,
   why="Large numbers on both sides make everyone a wage taker."),
 dict(q="In a perfectly competitive factor market, an individual firm's labor supply curve is", choices=[
   "upward sloping", "horizontal at the market wage", "downward sloping", "vertical", "backward bending"], ans=1,
   why="The firm can hire any quantity at the going wage."),
 dict(q="Marginal factor cost (MFC) is", choices=[
   "the total cost of all factors",
   "the additional cost of hiring one more unit of a factor",
   "the wage divided by output",
   "the marginal product of the factor",
   "the average cost of labor"], ans=1,
   why="MFC is the change in total factor cost from one more unit."),
 dict(q="In a perfectly competitive labor market, marginal factor cost equals", choices=[
   "the marginal revenue product", "the market wage", "zero", "the product price", "average product"], ans=1,
   why="Because the firm is a wage taker, each extra worker costs exactly the wage."),
 dict(q="A firm hires labor up to the point where", choices=[
   "marginal product equals marginal factor cost",
   "marginal revenue product equals marginal factor cost",
   "total product is maximized",
   "the wage equals the product price",
   "average product is maximized"], ans=1,
   why="Hire while the revenue a worker adds exceeds the cost of employing them."),
 dict(q="Using the table with a product price of $4, the marginal revenue product of the third worker is", table=HIRE, choices=[
   "$9", "$24", "$36", "$48", "$144"], ans=2,
   why="MP is 9, so MRP = 9 × $4 = $36."),
 dict(q="Using the table with a product price of $4, the marginal revenue product of the fourth worker is", table=HIRE, choices=[
   "$6", "$12", "$24", "$36", "$42"], ans=2,
   why="MP is 6, so MRP = 6 × $4 = $24."),
 dict(q="Using the table with a product price of $4 and a wage of $24, the firm should hire", table=HIRE, choices=[
   "1 worker", "2 workers", "3 workers", "4 workers", "5 workers"], ans=3,
   why="The fourth worker's MRP of $24 exactly equals the wage; the fifth's $12 does not."),
 dict(q="Using the table with a product price of $4 and a wage of $36, the firm should hire", table=HIRE, choices=[
   "1 worker", "2 workers", "3 workers", "4 workers", "5 workers"], ans=2,
   why="MRP reaches $36 at the third worker."),
 dict(q="Using the table with a product price of $4 and a wage of $48, the firm should hire", table=HIRE, choices=[
   "1 worker", "2 workers", "3 workers", "4 workers", "no workers"], ans=1,
   why="The second worker's MRP is $48; the third's $36 is below the wage."),
 dict(q="Using the table, if the product price rises to $8 and the wage stays at $24, the firm should hire", table=HIRE, choices=[
   "3 workers", "4 workers", "5 workers", "2 workers", "1 worker"], ans=2,
   why="At $8 the fifth worker's MRP is 3 × $8 = $24, matching the wage."),
 dict(q="Using the table, the fall in marginal revenue product as employment rises reflects", table=HIRE, choices=[
   "a falling product price",
   "diminishing marginal returns to labor",
   "a rising wage",
   "declining worker effort",
   "falling total product"], ans=1,
   why="Total product rises by 15, 12, 9, 6, 3 — a falling marginal product."),
 dict(q="Using the table, total product at 5 workers is", table=HIRE, choices=[
   "3", "42", "45", "48", "60"], ans=2,
   why="The table gives 45 units at five workers."),
 dict(q="If a firm's MRP of labor is $30 and the market wage is $22, the firm should", choices=[
   "hire fewer workers", "hire more workers", "keep employment unchanged", "lower the wage", "exit"], ans=1,
   why="The next worker adds more revenue than cost."),
 dict(q="If a firm's MRP of labor is $18 and the market wage is $25, the firm should", choices=[
   "hire more workers", "reduce employment", "keep employment unchanged", "raise its price", "raise the wage"], ans=1,
   why="The last worker costs more than they add."),
 dict(q="A firm in a competitive labor market that maximizes profit will find that the wage equals", choices=[
   "the marginal product of labor",
   "the marginal revenue product of the last worker hired",
   "the average revenue product",
   "total revenue divided by workers",
   "the product price"], ans=1,
   why="That is exactly the hiring condition."),
 dict(q="A firm's labor demand curve in a competitive labor market is its", choices=[
   "marginal product curve",
   "marginal revenue product curve",
   "average product curve",
   "total product curve",
   "marginal factor cost curve"], ans=1,
   why="MRP maps each wage to the profit-maximizing number of workers."),
 dict(q="The market labor demand curve is obtained by", choices=[
   "adding firms' MRP curves vertically",
   "summing the quantities of labor all firms demand at each wage",
   "using the largest firm's curve",
   "averaging wages",
   "adding labor supply curves"], ans=1,
   why="It is a horizontal summation, like any market demand curve."),
 dict(q="In a competitive labor market, the equilibrium wage is $20. A firm hiring 40 workers pays a total wage bill of", choices=[
   "$60", "$200", "$800", "$2", "$8,000"], ans=2,
   why="40 × $20 = $800."),
 dict(q="A firm hires the quantity of every input where the marginal revenue product per dollar spent", choices=[
   "is largest for one input",
   "is equal across all inputs and equal to one",
   "is zero",
   "equals the output price",
   "equals total cost"], ans=1,
   why="Otherwise the firm could raise profit by reallocating a dollar between inputs."),
 dict(q="The least-cost rule for producing a given output requires", choices=[
   "spending equally on each input",
   "MP of labor divided by the wage to equal MP of capital divided by the rental rate",
   "using only the cheaper input",
   "equal marginal products",
   "equal quantities of each input"], ans=1,
   why="Each dollar must buy the same amount of extra output wherever it is spent."),
 dict(q="A firm finds MP of labor is 20 and the wage is $10, while MP of capital is 24 and the rental rate is $16. It should", choices=[
   "use more capital and less labor",
   "use more labor and less capital",
   "leave its input mix unchanged",
   "shut down",
   "hire equal amounts of each"], ans=1,
   why="Labor delivers 2 units per dollar against capital's 1.5."),
 dict(q="A firm finds MP of labor is 12 and the wage is $6, while MP of capital is 30 and the rental rate is $15. Its input mix is", choices=[
   "not cost minimizing; it should use more labor",
   "cost minimizing, since both give 2 units of output per dollar",
   "not cost minimizing; it should use more capital",
   "impossible to evaluate",
   "profit maximizing but not cost minimizing"], ans=1,
   why="12/6 = 30/15 = 2, so the least-cost rule holds."),
 dict(q="An increase in the market wage causes a competitive firm to", choices=[
   "shift its labor demand curve left",
   "move up along its labor demand curve, hiring fewer workers",
   "shift its labor demand curve right",
   "hire more workers",
   "leave employment unchanged"], ans=1,
   why="A change in the factor's own price is a movement along its demand curve."),
 dict(q="An increase in the price of the firm's output causes its labor demand curve to", choices=[
   "shift leftward", "shift rightward", "stay put", "become vertical", "become horizontal"], ans=1,
   why="MRP = MP × P rises at every level of employment."),
 dict(q="In a competitive labor market, the supply curve facing the market as a whole is", choices=[
   "horizontal", "upward sloping", "vertical", "downward sloping", "the same as a single firm's"], ans=1,
   why="A higher wage draws more workers into the market even though each firm faces a flat curve."),
 dict(q="The difference between the market labor supply curve and a single firm's labor supply curve in perfect competition is that", choices=[
   "they are identical",
   "the market curve slopes upward while the individual firm's is horizontal at the market wage",
   "the firm's slopes upward and the market's is horizontal",
   "both are vertical",
   "the firm's is downward sloping"], ans=1,
   why="One firm is too small to have to raise the wage to hire more."),
 dict(q="Total labor cost for a firm in a competitive labor market equals", choices=[
   "the wage divided by the number of workers",
   "the wage times the number of workers",
   "marginal factor cost",
   "the marginal revenue product",
   "output times the wage"], ans=1,
   why="Every worker is paid the same market wage."),
 dict(q="In a competitive labor market, average factor cost equals", choices=[
   "marginal factor cost, both equal to the wage",
   "half of marginal factor cost",
   "the marginal revenue product",
   "zero",
   "the product price"], ans=0,
   why="With a constant wage, average and marginal cost of labor coincide."),
 dict(q="A firm whose output price is $6 and whose fourth worker raises output by 5 units should hire that worker if the wage is", choices=[
   "$40", "$30 or less", "$35", "any wage", "$60"], ans=1,
   why="MRP = 5 × $6 = $30, so the worker is worth hiring at a wage up to $30."),
 dict(q="A firm whose output price is $12 and whose next worker raises output by 3 units has an MRP of", choices=[
   "$15", "$36", "$4", "$12", "$3"], ans=1,
   why="3 × $12 = $36."),
 dict(q="For a firm that sells output in a competitive market, MRP declines because", choices=[
   "the product price falls as output rises",
   "the marginal product of labor declines",
   "wages rise as more workers are hired",
   "revenue falls",
   "fixed costs rise"], ans=1,
   why="The price is constant for a price taker, so only MP can fall."),
 dict(q="For a firm with market power in its product market, MRP declines for two reasons:", choices=[
   "rising wages and rising fixed costs",
   "falling marginal product and falling marginal revenue as output expands",
   "falling wages and rising output",
   "rising marginal product and falling price",
   "government regulation and taxes"], ans=1,
   why="Both terms in MP × MR fall as employment rises."),
 dict(q="Compared with a competitive product seller facing the same production function, a firm with product-market power will hire", choices=[
   "more labor", "less labor", "the same amount of labor", "no labor", "labor only in the long run"], ans=1,
   why="Its MRP curve lies below, since marginal revenue is below price."),
 dict(q="A firm's demand for labor is more elastic when", choices=[
   "labor is a tiny share of total cost",
   "capital can easily be substituted for labor",
   "the product's demand is inelastic",
   "there are no substitutes",
   "the adjustment period is very short"], ans=1,
   why="Easy substitution means employment responds sharply to a wage change."),
 dict(q="The elasticity of labor demand is greater in the long run because", choices=[
   "wages fall over time",
   "firms have more time to substitute other inputs and adjust their production methods",
   "workers become more productive",
   "product demand becomes inelastic",
   "marginal product rises"], ans=1,
   why="Adjustment possibilities widen with time."),
 dict(q="If the wage rises and a firm cannot substitute capital for labor at all, employment will", choices=[
   "not change at all",
   "fall by less than it would if substitution were easy",
   "fall by more than if substitution were easy",
   "rise",
   "become undefined"], ans=1,
   why="Only the output effect operates, so labor demand is less elastic."),
 dict(q="Producer surplus in a competitive labor market accrues to", choices=[
   "workers only",
   "employers, as the area between the labor demand curve and the wage",
   "the government",
   "no one",
   "consumers of the product"], ans=1,
   why="It is the value of workers' output above what the firm paid for it."),
 dict(q="Worker surplus in a competitive labor market is the area", choices=[
   "above the demand curve",
   "between the wage and the labor supply curve",
   "under the supply curve",
   "above the wage and under demand",
   "equal to total wages"], ans=1,
   why="It is the wage above workers' reservation wages."),
 dict(q="A competitive labor market at equilibrium", choices=[
   "creates a deadweight loss",
   "maximizes the combined surplus of workers and employers",
   "leaves workers unpaid",
   "always has unemployment",
   "pays workers more than their MRP"], ans=1,
   why="Every mutually beneficial employment match is made."),
 dict(q="A firm operating where MRP exceeds the wage is", choices=[
   "maximizing profit",
   "not maximizing profit, because expanding employment would raise profit",
   "shutting down",
   "hiring too many workers",
   "paying above the market wage"], ans=1,
   why="There are still profitable hires to be made."),
 dict(q="A firm operating where MRP is below the wage is", choices=[
   "maximizing profit",
   "hiring too many workers and could raise profit by hiring fewer",
   "hiring too few workers",
   "at the shutdown point",
   "in long-run equilibrium"], ans=1,
   why="The marginal worker costs more than they contribute."),
 dict(q="If a competitive firm's product price doubles while the wage is unchanged, the firm will", choices=[
   "hire the same number of workers",
   "hire more workers, since MRP has doubled at every level of employment",
   "hire fewer workers",
   "shut down",
   "raise the wage"], ans=1,
   why="The labor demand curve shifts right."),
 dict(q="A firm's derived demand for labor ultimately depends on", choices=[
   "the wage alone",
   "the value consumers place on the product the labor helps produce",
   "the number of workers available",
   "the firm's fixed costs",
   "the length of the workday"], ans=1,
   why="Labor is valued for what it produces and what that product is worth."),
 dict(q="In equilibrium in a competitive labor market, workers as a group are paid", choices=[
   "more than the value of their contribution",
   "a wage equal to the marginal revenue product of the last worker hired",
   "exactly total revenue",
   "nothing above their reservation wage",
   "the average product of labor"], ans=1,
   why="The market wage is set where the marginal worker's contribution equals their cost."),
 dict(q="Two identical firms face the same competitive wage but one has a higher product price. That firm will", choices=[
   "hire fewer workers", "hire more workers", "hire the same number", "pay a lower wage", "pay a higher wage"], ans=1,
   why="Its MRP is higher at every level of employment."),
 dict(q="If a competitive firm's workers become 50% more productive, its labor demand curve", choices=[
   "shifts leftward", "shifts rightward", "does not move", "becomes vertical", "becomes horizontal"], ans=1,
   why="Higher marginal product raises MRP throughout."),
 dict(q="A competitive firm cannot raise its profit by paying below the market wage because", choices=[
   "the government forbids it",
   "workers would leave for other employers paying the market wage",
   "its MRP would fall",
   "output would rise",
   "the wage is fixed by contract"], ans=1,
   why="A competitive labor market gives workers alternatives at the going wage."),
 dict(q="The profit-maximizing employment rule and the profit-maximizing output rule are", choices=[
   "unrelated",
   "two views of the same decision, since choosing how much labor to hire determines how much output to produce",
   "in conflict with each other",
   "used only by monopolies",
   "applicable only in the long run"], ans=1,
   why="MRP = wage and MR = MC describe the same optimum from the input and output sides."),
 dict(q="The single condition that summarizes profit-maximizing input use in a competitive factor market is", choices=[
   "MP = wage", "MRP = MFC = the market wage", "MP = product price", "total revenue = total cost", "MRP = MP"], ans=1,
   why="Hire each input until its revenue contribution equals its cost."),
]
