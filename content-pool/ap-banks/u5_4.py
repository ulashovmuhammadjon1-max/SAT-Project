# 5.4 Monopsonistic Markets — 50 questions
# Table verified: upward-sloping labor supply facing a single buyer.
#   L=1 W=10 TFC=10  MFC=10
#   L=2 W=12 TFC=24  MFC=14
#   L=3 W=14 TFC=42  MFC=18
#   L=4 W=16 TFC=64  MFC=22
#   L=5 W=18 TFC=90  MFC=26
#   With MRP = $22 at L=4, the monopsonist hires 4 workers and pays a wage of $16.
TOPIC = ("5.4", "Monopsonistic Markets", 5)
MONOP = dict(headers=["Workers", "Wage required"],
             rows=[["1", "$10"], ["2", "$12"], ["3", "$14"], ["4", "$16"], ["5", "$18"]])
QUESTIONS = [
 dict(q="A monopsony is a market with", choices=[
   "a single seller", "a single buyer", "many buyers and sellers", "two buyers", "no buyers"], ans=1,
   why="Monopsony is buyer-side market power, the mirror image of monopoly."),
 dict(q="In a labor market monopsony, the single buyer is", choices=[
   "the worker", "the employer", "the government always", "the consumer", "the union"], ans=1,
   why="One firm is the only significant purchaser of that labor."),
 dict(q="A monopsonist in a labor market faces a labor supply curve that is", choices=[
   "horizontal at the market wage",
   "upward sloping, because it must raise the wage to attract more workers",
   "downward sloping",
   "vertical",
   "perfectly elastic"], ans=1,
   why="Being the whole market, it faces the market supply curve."),
 dict(q="For a monopsonist, marginal factor cost is", choices=[
   "equal to the wage",
   "greater than the wage, because raising the wage to hire one more worker also raises the wage paid to everyone",
   "less than the wage",
   "zero",
   "equal to the marginal revenue product"], ans=1,
   why="The wage increase applies to all workers already employed, not just the new one."),
 dict(q="Using the table, the total labor cost of hiring 3 workers is", table=MONOP, choices=[
   "$14", "$36", "$42", "$18", "$24"], ans=2,
   why="All three are paid $14, so 3 × $14 = $42."),
 dict(q="Using the table, the total labor cost of hiring 4 workers is", table=MONOP, choices=[
   "$16", "$42", "$52", "$64", "$90"], ans=3,
   why="Four workers at $16 each is $64."),
 dict(q="Using the table, the marginal factor cost of the third worker is", table=MONOP, choices=[
   "$2", "$14", "$18", "$42", "$24"], ans=2,
   why="Total labor cost rises from $24 to $42, so MFC = $18."),
 dict(q="Using the table, the marginal factor cost of the fourth worker is", table=MONOP, choices=[
   "$16", "$18", "$22", "$26", "$64"], ans=2,
   why="Total labor cost rises from $42 to $64, so MFC = $22."),
 dict(q="Using the table, the marginal factor cost of the fifth worker is", table=MONOP, choices=[
   "$18", "$22", "$26", "$30", "$90"], ans=2,
   why="Total labor cost rises from $64 to $90, so MFC = $26."),
 dict(q="Using the table, the marginal factor cost of the fourth worker exceeds that worker's $16 wage because", table=MONOP, choices=[
   "the worker is less productive",
   "hiring the fourth worker requires raising the wage of the three already employed from $14 to $16",
   "of a payroll tax",
   "the firm pays overtime",
   "marginal revenue product is falling"], ans=1,
   why="MFC of $22 is the $16 wage plus $6 of raises to existing workers."),
 dict(q="Using the table, if marginal revenue product is $22 at the fourth worker, the monopsonist hires", table=MONOP, choices=[
   "2 workers", "3 workers", "4 workers", "5 workers", "1 worker"], ans=2,
   why="MFC equals MRP at the fourth worker."),
 dict(q="Using the table, having decided to hire 4 workers, the monopsonist pays a wage of", table=MONOP, choices=[
   "$14", "$16", "$18", "$22", "$26"], ans=1,
   why="The supply curve shows $16 is the wage needed to attract four workers."),
 dict(q="Using the table, the monopsonist's wage of $16 is below the $22 marginal revenue product because", table=MONOP, choices=[
   "workers are underqualified",
   "the firm hires where MRP equals marginal factor cost, and reads the wage off the lower supply curve",
   "the government caps wages",
   "the firm is losing money",
   "labor supply is perfectly elastic"], ans=1,
   why="Hiring is set by MFC while pay is set by supply, and the two differ."),
 dict(q="A monopsonist hires labor up to the point where", choices=[
   "the wage equals marginal revenue product",
   "marginal factor cost equals marginal revenue product",
   "the wage equals marginal factor cost",
   "total product is maximized",
   "marginal product is maximized"], ans=1,
   why="The general rule is MFC = MRP; only in competition does MFC equal the wage."),
 dict(q="After choosing its employment level, a monopsonist sets the wage by reading", choices=[
   "the marginal factor cost curve at that employment",
   "the labor supply curve at that employment",
   "the marginal revenue product curve",
   "the product demand curve",
   "the average product curve"], ans=1,
   why="Supply shows the lowest wage that attracts that many workers."),
 dict(q="Compared with a perfectly competitive labor market, a monopsonist hires", choices=[
   "more workers at a higher wage",
   "fewer workers at a lower wage",
   "the same number at the same wage",
   "more workers at a lower wage",
   "fewer workers at a higher wage"], ans=1,
   why="Restricting hiring is how it holds the wage down."),
 dict(q="Under monopsony, workers are paid", choices=[
   "more than their marginal revenue product",
   "less than their marginal revenue product",
   "exactly their marginal revenue product",
   "nothing",
   "the marginal factor cost"], ans=1,
   why="The wage comes off the supply curve, below the MRP at that employment."),
 dict(q="The gap between marginal revenue product and the wage under monopsony is sometimes called", choices=[
   "producer surplus", "monopsonistic exploitation", "deadweight loss", "economic rent to workers", "compensating differential"], ans=1,
   why="It is the value workers produce that they do not receive."),
 dict(q="Monopsony creates a deadweight loss because", choices=[
   "workers are paid too much",
   "employment is below the level at which the wage would equal marginal revenue product",
   "the firm earns no profit",
   "the wage is too high",
   "too many workers are hired"], ans=1,
   why="Mutually beneficial employment matches go unmade."),
 dict(q="A monopsonist's marginal factor cost curve lies", choices=[
   "below its labor supply curve",
   "above its labor supply curve",
   "on its labor supply curve",
   "horizontally at the wage",
   "below the MRP curve everywhere"], ans=1,
   why="Each additional hire costs the new wage plus raises for existing workers."),
 dict(q="Which of the following is the closest real-world example of monopsony?", choices=[
   "a supermarket hiring cashiers in a large city",
   "the only large hospital in a remote town hiring nurses",
   "a restaurant hiring servers downtown",
   "a national retailer hiring in many cities",
   "a farm hiring seasonal workers where many farms compete"], ans=1,
   why="Workers with that specialization have essentially one local employer."),
 dict(q="Monopsony power is more likely when", choices=[
   "workers can easily move to other employers",
   "workers are geographically immobile and have few alternative employers",
   "there are many firms in the area",
   "skills are general and transferable",
   "information is perfect"], ans=1,
   why="Limited alternatives is what gives the buyer power."),
 dict(q="A minimum wage set between the monopsony wage and the competitive wage will", choices=[
   "reduce employment",
   "raise both the wage and employment",
   "raise the wage but reduce employment",
   "have no effect",
   "cause a labor surplus"], ans=1,
   why="It flattens the effective supply curve, so MFC equals the wage over that range."),
 dict(q="The reason a minimum wage can raise employment under monopsony but not under perfect competition is that", choices=[
   "monopsonists are more generous",
   "it removes the monopsonist's incentive to restrict hiring to hold the wage down",
   "competitive firms ignore wages",
   "monopsonists have no marginal cost",
   "labor supply is vertical under monopsony"], ans=1,
   why="With the wage fixed by law, hiring one more worker no longer raises everyone's pay."),
 dict(q="A minimum wage set above the competitive wage in a monopsonistic market will", choices=[
   "always raise employment",
   "reduce employment below the competitive level, as in a competitive market",
   "have no effect",
   "eliminate the deadweight loss entirely",
   "lower the wage"], ans=1,
   why="Beyond the competitive wage the ordinary price-floor effect takes over."),
 dict(q="A labor union facing a monopsonist creates a situation called", choices=[
   "perfect competition", "bilateral monopoly", "a cartel", "monopolistic competition", "a price floor"], ans=1,
   why="Market power on both sides of the market is bilateral monopoly."),
 dict(q="In a bilateral monopoly, the wage is", choices=[
   "determined precisely by supply and demand",
   "determined by bargaining between the two sides, within a range",
   "always the competitive wage",
   "always the monopsony wage",
   "zero"], ans=1,
   why="Economic theory bounds the outcome but does not pin down a single point."),
 dict(q="A union in a monopsonistic labor market can potentially raise", choices=[
   "only the wage, at the cost of employment",
   "both the wage and employment toward the competitive level",
   "neither wages nor employment",
   "only employment",
   "the deadweight loss"], ans=1,
   why="Countervailing power can offset the monopsonist's output restriction."),
 dict(q="Compared with monopoly, monopsony involves market power on the", choices=[
   "selling side of the product market",
   "buying side of a market",
   "government side",
   "consumer side of the product market",
   "supply side of the product market"], ans=1,
   why="Monopoly is a single seller; monopsony is a single buyer."),
 dict(q="A monopsonist's total labor cost rises faster than the wage bill would in a competitive market because", choices=[
   "it pays a higher wage",
   "each additional hire requires raising the wage of all workers already employed",
   "it hires more workers",
   "it faces higher taxes",
   "its workers are more productive"], ans=1,
   why="The raise applies across the whole workforce."),
 dict(q="If a monopsonist could perfectly wage discriminate, paying each worker exactly their reservation wage, employment would", choices=[
   "fall further",
   "rise to the competitive level, since MFC would equal the supply curve",
   "stay the same",
   "fall to zero",
   "become undefined"], ans=1,
   why="With no need to raise everyone's pay, the extra worker costs only their own wage."),
 dict(q="Under a perfectly wage-discriminating monopsonist, worker surplus is", choices=[
   "maximized", "zero, since each worker is paid exactly their reservation wage", "unchanged", "negative", "equal to producer surplus"], ans=1,
   why="The firm captures the entire surplus while reaching efficient employment."),
 dict(q="A monopsonist with an MRP of $30 at its chosen employment and a wage of $20 is", choices=[
   "losing money on the marginal worker",
   "capturing $10 per worker of the value that worker produces",
   "paying above the competitive wage",
   "hiring too many workers",
   "earning zero profit"], ans=1,
   why="The gap between MRP and the wage accrues to the employer."),
 dict(q="Which curve does a monopsonist NOT use to determine its employment level?", choices=[
   "the marginal revenue product curve",
   "the marginal factor cost curve",
   "the labor supply curve, which it uses only to set the wage",
   "any of them",
   "the product demand curve"], ans=2,
   why="Supply sets the wage after MFC = MRP has set the quantity."),
 dict(q="The monopsonist's wage is determined by the", choices=[
   "marginal factor cost curve at the chosen employment",
   "labor supply curve at the chosen employment",
   "marginal revenue product at the chosen employment",
   "average factor cost of the last worker only",
   "market equilibrium wage"], ans=1,
   why="Supply gives the minimum wage that attracts that number of workers."),
 dict(q="In a competitive labor market, marginal factor cost and the labor supply curve are", choices=[
   "different, with MFC above supply",
   "the same, both horizontal at the market wage",
   "different, with MFC below supply",
   "both upward sloping",
   "both vertical"], ans=1,
   why="A wage taker's cost of an extra worker is exactly the wage."),
 dict(q="Monopsony power reduces", choices=[
   "the firm's profit", "both employment and the wage relative to the competitive outcome", "only the wage",
   "only employment", "neither"], ans=1,
   why="Restricting hiring is the mechanism for holding the wage down."),
 dict(q="A firm that is the only employer in a company town has monopsony power mainly because", choices=[
   "it produces a unique product",
   "local workers have few alternative employers without relocating",
   "it has a patent",
   "it faces inelastic product demand",
   "it pays high wages"], ans=1,
   why="Immobility limits workers' outside options."),
 dict(q="Which policy is most directly aimed at countering monopsony power in labor markets?", choices=[
   "a tax on output",
   "a legally enforced wage floor at or near the competitive wage",
   "a subsidy to the employer",
   "a tariff on imports",
   "deregulation of product markets"], ans=1,
   why="A properly set floor removes the incentive to restrict hiring."),
 dict(q="A monopsonist that faces a perfectly elastic labor supply curve", choices=[
   "still restricts employment",
   "behaves exactly like a competitive employer, paying the market wage",
   "pays below the competitive wage",
   "hires no workers",
   "has MFC above the wage"], ans=1,
   why="With a horizontal supply curve, MFC equals the wage and the power vanishes."),
 dict(q="The more elastic the labor supply facing a monopsonist, the", choices=[
   "greater its monopsony power",
   "smaller the gap between the wage it pays and the competitive wage",
   "lower the wage it pays",
   "fewer workers it hires",
   "larger the deadweight loss"], ans=1,
   why="Workers with more alternatives are harder to underpay."),
 dict(q="A monopsonist's MFC curve for an upward-sloping supply curve W = a + bL is", choices=[
   "a + bL", "a + 2bL, rising twice as steeply", "a − bL", "constant at a", "b alone"], ans=1,
   why="The same doubling of the slope that gives a monopolist's MR applies here."),
 dict(q="A firm faces labor supply W = 5 + L. Its marginal factor cost is", choices=[
   "5 + L", "5 + 2L", "10 + L", "5", "L"], ans=1,
   why="Total factor cost is 5L + L², so MFC = 5 + 2L."),
 dict(q="For that firm, if MRP = 25 − L, the profit-maximizing employment is", choices=[
   "5", "20/3", "10", "15", "25"], ans=1,
   why="Setting 5 + 2L = 25 − L gives 3L = 20, so L = 20/3."),
 dict(q="Monopsony is inefficient because at its chosen employment", choices=[
   "the wage exceeds marginal revenue product",
   "marginal revenue product exceeds the wage, so additional mutually beneficial hires are not made",
   "marginal factor cost is below the wage",
   "the wage is too high",
   "the firm earns no profit"], ans=1,
   why="Workers would accept the job at a wage below what they would produce."),
 dict(q="Which of the following is true of both monopoly and monopsony?", choices=[
   "both involve a single seller",
   "both restrict quantity below the competitive level and create deadweight loss",
   "both raise the price paid by buyers",
   "both benefit consumers",
   "both eliminate profit"], ans=1,
   why="Market power on either side reduces the quantity traded."),
 dict(q="Under monopsony, the firm's demand for labor curve", choices=[
   "is its MRP curve, as under competition",
   "does not exist as a conventional demand curve, since employment depends on both MRP and the supply curve",
   "is horizontal",
   "is its MFC curve",
   "is the labor supply curve"], ans=1,
   why="Like a monopolist's supply curve, it is not well defined."),
 dict(q="If a monopsonist's MRP curve shifts rightward, its employment and wage will", choices=[
   "both fall", "both rise", "employment rise and wage fall", "employment fall and wage rise", "be unchanged"], ans=1,
   why="Hiring more workers requires moving up the supply curve to a higher wage."),
 dict(q="A monopsonist compared with a competitive employer with identical MRP will have a total wage bill that is", choices=[
   "necessarily larger",
   "smaller, since it hires fewer workers at a lower wage",
   "identical",
   "zero",
   "equal to marginal factor cost"], ans=1,
   why="Both the wage and the number of workers are lower."),
 dict(q="The core insight of monopsony is that a large buyer", choices=[
   "must pay the market price",
   "can pay less than the value of what it buys by choosing to buy less of it",
   "always pays more",
   "has no effect on price",
   "faces a horizontal supply curve"], ans=1,
   why="Restricting purchases moves down the supply curve to a lower price."),
]
