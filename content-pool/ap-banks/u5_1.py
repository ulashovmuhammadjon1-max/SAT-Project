# 5.1 Introduction to Factor Markets — 50 questions
# Table verified: output price $5 (competitive product market)
#   L=1 TP=12 MP=12 MRP=60
#   L=2 TP=22 MP=10 MRP=50
#   L=3 TP=30 MP=8  MRP=40
#   L=4 TP=36 MP=6  MRP=30
#   L=5 TP=40 MP=4  MRP=20
#   At a wage of $40 the firm hires 3 workers (MRP = wage).
TOPIC = ("5.1", "Introduction to Factor Markets", 5)
MRP = dict(headers=["Workers", "Total product"],
           rows=[["1", "12"], ["2", "22"], ["3", "30"], ["4", "36"], ["5", "40"]])
QUESTIONS = [
 dict(q="A factor market is a market for", choices=[
   "finished consumer goods",
   "the resources used to produce goods and services, such as labor, land, and capital",
   "government bonds",
   "imports and exports",
   "money"], ans=1,
   why="Factor markets trade inputs rather than outputs."),
 dict(q="In a factor market, the roles are reversed relative to a product market: firms are", choices=[
   "sellers and households are buyers",
   "buyers and households are sellers",
   "both buyers and sellers",
   "neither buyers nor sellers",
   "regulators"], ans=1,
   why="Households supply labor and firms demand it."),
 dict(q="The demand for a factor of production is called a derived demand because it depends on", choices=[
   "the price of the factor alone",
   "the demand for the product the factor helps produce",
   "government policy",
   "the number of workers",
   "the firm's fixed costs"], ans=1,
   why="No one wants labor for its own sake; it is wanted for what it produces."),
 dict(q="If demand for a firm's product rises, its demand for labor will", choices=[
   "fall", "rise", "stay the same", "become perfectly inelastic", "disappear"], ans=1,
   why="Derived demand moves with product demand."),
 dict(q="Marginal product of labor is", choices=[
   "total output divided by the number of workers",
   "the additional output produced by hiring one more worker",
   "the wage paid to the last worker",
   "output times the product price",
   "the cost of hiring one more worker"], ans=1,
   why="MP is the change in total product from one more unit of labor."),
 dict(q="Marginal revenue product of labor (MRP) is", choices=[
   "the marginal product of labor",
   "the additional revenue a firm earns from hiring one more worker",
   "the wage rate",
   "total revenue divided by workers",
   "the marginal cost of output"], ans=1,
   why="MRP measures a worker's contribution to revenue."),
 dict(q="For a firm selling in a perfectly competitive product market, MRP equals", choices=[
   "marginal product times the wage",
   "marginal product times the product price",
   "the wage rate",
   "total revenue divided by output",
   "marginal cost times price"], ans=1,
   why="Each extra unit of output sells at the market price, so MRP = MP × P."),
 dict(q="Using the table, if the product sells for $5, the marginal product of the second worker is", table=MRP, choices=[
   "8", "10", "11", "12", "22"], ans=1,
   why="Total product rises from 12 to 22."),
 dict(q="Using the table, if the product sells for $5, the marginal revenue product of the second worker is", table=MRP, choices=[
   "$10", "$40", "$50", "$60", "$110"], ans=2,
   why="MRP = 10 × $5 = $50."),
 dict(q="Using the table, the marginal revenue product of the third worker at a $5 price is", table=MRP, choices=[
   "$8", "$30", "$40", "$50", "$150"], ans=2,
   why="MP is 8, so MRP = 8 × $5 = $40."),
 dict(q="Using the table, the marginal revenue product of the fourth worker at a $5 price is", table=MRP, choices=[
   "$6", "$20", "$30", "$36", "$40"], ans=2,
   why="MP is 6, so MRP = 6 × $5 = $30."),
 dict(q="Using the table with a $5 product price and a wage of $40, the firm should hire", table=MRP, choices=[
   "1 worker", "2 workers", "3 workers", "4 workers", "5 workers"], ans=2,
   why="The third worker's MRP of $40 exactly equals the wage; the fourth's $30 falls short."),
 dict(q="Using the table with a $5 product price and a wage of $50, the firm should hire", table=MRP, choices=[
   "1 worker", "2 workers", "3 workers", "4 workers", "5 workers"], ans=1,
   why="The second worker's MRP is $50; the third's $40 is below the wage."),
 dict(q="Using the table with a $5 product price and a wage of $20, the firm should hire", table=MRP, choices=[
   "2 workers", "3 workers", "4 workers", "5 workers", "1 worker"], ans=3,
   why="The fifth worker's MRP is $20, matching the wage."),
 dict(q="Using the table, marginal revenue product declines as more workers are hired because", table=MRP, choices=[
   "the product price falls",
   "the marginal product of labor falls under diminishing marginal returns",
   "wages rise",
   "workers become less skilled",
   "total product falls"], ans=1,
   why="Total product rises by 12, 10, 8, 6, 4, a falling sequence."),
 dict(q="A profit-maximizing firm hires labor up to the point where", choices=[
   "marginal product equals the wage",
   "marginal revenue product equals the wage rate",
   "total product is maximized",
   "average product is maximized",
   "the wage equals the product price"], ans=1,
   why="Hire while a worker adds more to revenue than to cost."),
 dict(q="If a worker's marginal revenue product exceeds the wage, the firm should", choices=[
   "hire fewer workers", "hire more workers", "keep employment unchanged", "lower the wage", "shut down"], ans=1,
   why="That worker adds more revenue than cost."),
 dict(q="If a worker's marginal revenue product is below the wage, the firm should", choices=[
   "hire more workers", "hire fewer workers", "raise the wage", "keep employment unchanged", "raise its price"], ans=1,
   why="That worker costs more than they contribute."),
 dict(q="In a perfectly competitive labor market, an individual firm faces a labor supply curve that is", choices=[
   "upward sloping",
   "horizontal at the market wage",
   "downward sloping",
   "vertical",
   "identical to market labor supply"], ans=1,
   why="The firm is a wage taker and can hire any number of workers at the going wage."),
 dict(q="For a firm in a perfectly competitive labor market, the marginal factor cost of labor equals", choices=[
   "the marginal revenue product", "the market wage rate", "zero", "the product price", "average product"], ans=1,
   why="Each extra worker costs exactly the going wage."),
 dict(q="A firm's demand curve for labor is", choices=[
   "its marginal product curve",
   "its marginal revenue product curve",
   "its total product curve",
   "horizontal",
   "the market labor supply curve"], ans=1,
   why="At any wage, the firm hires where MRP equals that wage."),
 dict(q="The labor demand curve slopes downward because", choices=[
   "wages fall over time",
   "the marginal product of labor declines as more workers are added",
   "workers become lazy",
   "product prices rise",
   "firms dislike hiring"], ans=1,
   why="Diminishing marginal returns lower each additional worker's contribution."),
 dict(q="The market supply curve of labor generally slopes", choices=[
   "downward", "upward, because higher wages draw more workers into the market", "horizontally", "vertically", "backward at all wages"], ans=1,
   why="A higher wage raises the opportunity cost of leisure and of other occupations."),
 dict(q="The equilibrium wage in a competitive labor market is determined by", choices=[
   "the government",
   "the intersection of market labor demand and market labor supply",
   "the largest employer",
   "each individual firm",
   "the marginal product of the first worker"], ans=1,
   why="It is an ordinary market equilibrium."),
 dict(q="A worker whose marginal product is 6 units and whose output sells for $9 has a marginal revenue product of", choices=[
   "$15", "$54", "$6", "$9", "$1.50"], ans=1,
   why="MRP = 6 × $9 = $54."),
 dict(q="A worker with a marginal revenue product of $22 an hour will be hired if the wage is", choices=[
   "$25", "$22 or less", "$30", "any wage at all", "no wage"], ans=1,
   why="Hiring is profitable while MRP is at least the wage."),
 dict(q="If the price of a firm's output rises, its labor demand curve", choices=[
   "shifts leftward", "shifts rightward, since each worker's MRP is now higher", "does not move", "becomes vertical", "becomes horizontal"], ans=1,
   why="MRP = MP × P, so a higher price raises MRP at every level of employment."),
 dict(q="If the price of a firm's output falls, its demand for labor", choices=[
   "rises", "falls", "stays the same", "becomes perfectly elastic", "becomes vertical"], ans=1,
   why="Lower product price means lower MRP at every employment level."),
 dict(q="An improvement in worker productivity will shift labor demand", choices=[
   "leftward", "rightward", "not at all", "downward along the same curve", "vertically"], ans=1,
   why="A higher marginal product raises MRP."),
 dict(q="The four factors of production are", choices=[
   "money, goods, services, and taxes",
   "land, labor, capital, and entrepreneurship",
   "supply, demand, price, and quantity",
   "wages, rent, interest, and taxes",
   "consumers, firms, government, and trade"], ans=1,
   why="These are the standard categories of productive resources."),
 dict(q="The payment to labor is called", choices=[
   "rent", "wages", "interest", "profit", "revenue"], ans=1,
   why="Each factor has its own income category."),
 dict(q="The payment to capital is called", choices=[
   "wages", "interest", "rent", "profit", "dividends only"], ans=1,
   why="Interest is the return to capital in the four-factor framework."),
 dict(q="The payment to land is called", choices=[
   "wages", "rent", "interest", "profit", "tax"], ans=1,
   why="Rent is the return to land."),
 dict(q="The payment to entrepreneurship is called", choices=[
   "wages", "profit", "rent", "interest", "salary"], ans=1,
   why="Profit is the return to bearing risk and organizing production."),
 dict(q="In the circular flow model, households supply factors of production and receive", choices=[
   "goods and services", "factor payments such as wages and rent", "taxes", "subsidies", "nothing"], ans=1,
   why="Factor income flows from firms to households."),
 dict(q="A firm in a competitive labor market that tried to pay below the market wage would", choices=[
   "attract more workers", "lose its workers to other employers", "raise its profit", "face no consequence", "face rising MRP"], ans=1,
   why="Workers have alternatives at the going wage."),
 dict(q="A firm in a competitive labor market has no reason to pay above the market wage because", choices=[
   "it is illegal",
   "it can already hire as many workers as it wants at the market wage",
   "workers would refuse",
   "MRP would fall",
   "the government caps wages"], ans=1,
   why="Its labor supply curve is horizontal at that wage."),
 dict(q="The least-cost combination of two inputs requires that", choices=[
   "the same amount is spent on each input",
   "the marginal product per dollar spent is equal across all inputs",
   "the same quantity of each input is used",
   "the cheaper input is used exclusively",
   "marginal products are equal"], ans=1,
   why="Otherwise a dollar could be shifted to the input yielding more output."),
 dict(q="If MP of labor divided by the wage exceeds MP of capital divided by the rental rate, the firm should", choices=[
   "use more capital and less labor",
   "use more labor and less capital",
   "use equal amounts of each",
   "shut down",
   "keep its input mix unchanged"], ans=1,
   why="Labor currently delivers more output per dollar."),
 dict(q="The profit-maximizing combination of inputs requires that", choices=[
   "marginal products are equal",
   "the marginal revenue product per dollar of each input equals one",
   "input prices are equal",
   "output is maximized",
   "the firm uses only one input"], ans=1,
   why="Each input is used up to the point where its last dollar returns exactly a dollar of revenue."),
 dict(q="Labor demand is more elastic when", choices=[
   "labor is a small share of total cost",
   "it is easy to substitute machines for workers",
   "the product's demand is inelastic",
   "there are no substitutes for labor",
   "the time horizon is short"], ans=1,
   why="Easy substitution means employment responds strongly to a wage change."),
 dict(q="Labor demand is less elastic when", choices=[
   "the product's demand is highly elastic",
   "labor accounts for a small share of the firm's total costs",
   "machines are close substitutes for workers",
   "the time horizon is long",
   "many substitutes exist"], ans=1,
   why="A wage rise then has little effect on total cost and so on output and hiring."),
 dict(q="An increase in the market wage causes a competitive firm to", choices=[
   "hire more workers",
   "move up along its labor demand curve and hire fewer workers",
   "shift its labor demand curve rightward",
   "shift its labor demand curve leftward",
   "hire the same number of workers"], ans=1,
   why="A price change is a movement along the curve, not a shift."),
 dict(q="A firm's demand for labor shifts rather than moving along the curve when", choices=[
   "the wage changes",
   "the product price or worker productivity changes",
   "employment changes",
   "the firm hires an extra worker",
   "the labor supply curve shifts"], ans=1,
   why="Anything that changes MRP at a given employment level shifts the curve."),
 dict(q="In a competitive labor market, a worker is paid", choices=[
   "less than their marginal revenue product",
   "a wage equal to the marginal revenue product of the last worker hired",
   "more than their marginal revenue product",
   "the average product of labor",
   "the total product divided by output"], ans=1,
   why="Firms hire until MRP equals the wage."),
 dict(q="A firm selling its output in an imperfectly competitive market has an MRP equal to", choices=[
   "marginal product times price",
   "marginal product times marginal revenue",
   "the wage rate",
   "average product times price",
   "marginal product alone"], ans=1,
   why="With MR below price, the correct multiplier is marginal revenue."),
 dict(q="A firm with market power in its product market will, all else equal, hire", choices=[
   "more labor than a competitive firm with the same MP schedule",
   "less labor than a competitive firm with the same MP schedule",
   "the same amount of labor",
   "no labor",
   "labor only up to where MP is maximized"], ans=1,
   why="Its MRP is lower because marginal revenue is below price."),
 dict(q="A competitive firm's labor demand curve is downward sloping only in the range where", choices=[
   "marginal product is rising",
   "marginal product is falling",
   "total product is falling",
   "average product is rising",
   "output is zero"], ans=1,
   why="Diminishing marginal returns are what make MRP fall."),
 dict(q="If both the wage and the product price double, a competitive firm's optimal employment will", choices=[
   "double", "stay the same, since MRP and the wage both double", "halve", "fall to zero", "be undefined"], ans=1,
   why="The MRP = wage condition is unchanged by scaling both sides."),
 dict(q="The main reason wages differ across occupations in competitive labor markets is differences in", choices=[
   "the number of hours worked",
   "workers' marginal revenue products and the supply of workers with those skills",
   "government wage schedules",
   "firm size alone",
   "the length of the workweek"], ans=1,
   why="Both sides of the market matter: productivity and scarcity."),
]
