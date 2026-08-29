# 4.5 Oligopoly and Game Theory — 50 questions
# Payoff matrix verified (first number is Firm A's profit, second is Firm B's):
#   Both High: (10, 10) | A High, B Low: (4, 14)
#   A Low, B High: (14, 4) | Both Low: (6, 6)
# For A: B plays High -> 14 > 10 so Low; B plays Low -> 6 > 4 so Low. Low is dominant.
# Symmetric for B. Nash equilibrium is (Low, Low) at (6, 6), which both firms
# prefer less than the (10, 10) cooperative outcome. A prisoner's dilemma.
TOPIC = ("4.5", "Oligopoly and Game Theory", 4)
GAME = dict(headers=["", "Firm B: High price", "Firm B: Low price"],
            rows=[["Firm A: High price", "(10, 10)", "(4, 14)"],
                  ["Firm A: Low price", "(14, 4)", "(6, 6)"]])
QUESTIONS = [
 dict(q="An oligopoly is a market structure with", choices=[
   "one seller", "a small number of interdependent firms", "many firms selling identical products",
   "many firms selling differentiated products", "a single buyer"], ans=1,
   why="Few firms, each affected by the others' decisions, defines oligopoly."),
 dict(q="Mutual interdependence in oligopoly means that", choices=[
   "firms have identical costs",
   "each firm's best decision depends on what it expects its rivals to do",
   "firms must charge the same price",
   "entry is free",
   "products are identical"], ans=1,
   why="With few rivals, one firm's move materially changes the others' payoffs."),
 dict(q="Oligopolies typically arise because of", choices=[
   "free entry",
   "barriers to entry such as economies of scale, high startup costs, or patents",
   "identical products",
   "government requirements to have many firms",
   "perfectly elastic demand"], ans=1,
   why="Barriers keep the number of firms small."),
 dict(q="In game theory, a dominant strategy is one that", choices=[
   "gives the highest payoff only if rivals cooperate",
   "gives a player a better payoff than any alternative regardless of what rivals do",
   "is chosen at random",
   "maximizes the rivals' payoff",
   "is always illegal"], ans=1,
   why="It is best against every possible rival choice."),
 dict(q="A Nash equilibrium is an outcome in which", choices=[
   "every player earns the maximum possible payoff",
   "no player can improve their payoff by unilaterally changing strategy",
   "firms always cooperate",
   "profits are equal",
   "the game ends"], ans=1,
   why="Each player's choice is a best response to the others'."),
 dict(q="Using the payoff matrix, Firm A's payoff if both firms choose the high price is", table=GAME, choices=[
   "$4", "$6", "$10", "$14", "$20"], ans=2,
   why="The first number in the (10, 10) cell is Firm A's."),
 dict(q="Using the payoff matrix, if Firm B chooses the high price, Firm A's best response is", table=GAME, choices=[
   "the high price, earning 10", "the low price, earning 14", "either, since payoffs are equal",
   "to exit the market", "to raise price further"], ans=1,
   why="14 from undercutting beats 10 from matching."),
 dict(q="Using the payoff matrix, if Firm B chooses the low price, Firm A's best response is", table=GAME, choices=[
   "the high price, earning 4", "the low price, earning 6", "either, since payoffs are equal",
   "to exit", "to collude"], ans=1,
   why="6 beats 4."),
 dict(q="Using the payoff matrix, Firm A's dominant strategy is", table=GAME, choices=[
   "the high price", "the low price", "there is no dominant strategy", "to alternate", "to exit"], ans=1,
   why="The low price is better whichever price Firm B chooses."),
 dict(q="Using the payoff matrix, the Nash equilibrium is", table=GAME, choices=[
   "both firms choose the high price",
   "both firms choose the low price",
   "A high and B low",
   "A low and B high",
   "there is no Nash equilibrium"], ans=1,
   why="Low is dominant for both, so neither can gain by deviating from (Low, Low)."),
 dict(q="Using the payoff matrix, the payoffs at the Nash equilibrium are", table=GAME, choices=[
   "(10, 10)", "(6, 6)", "(14, 4)", "(4, 14)", "(0, 0)"], ans=1,
   why="Both firms choosing the low price yields 6 each."),
 dict(q="Using the payoff matrix, the outcome both firms would prefer to the Nash equilibrium is", table=GAME, choices=[
   "both choose the low price", "both choose the high price", "A low and B high", "A high and B low", "no outcome is better"], ans=1,
   why="(10, 10) beats (6, 6) for both, but it is not individually stable."),
 dict(q="Using the payoff matrix, this game is an example of", table=GAME, choices=[
   "a game with no equilibrium",
   "a prisoner's dilemma, where individually rational choices produce a jointly worse outcome",
   "perfect competition",
   "a game with no dominant strategies",
   "a monopoly"], ans=1,
   why="Both defect despite mutual cooperation being better for both."),
 dict(q="Using the payoff matrix, the reason the firms do not settle on the high price is that", table=GAME, choices=[
   "high prices are illegal",
   "each firm can gain by undercutting while the other holds its price high",
   "the low price is more profitable jointly",
   "consumers refuse to pay high prices",
   "costs are too high"], ans=1,
   why="14 beats 10, so cooperating leaves each firm exposed to the other's defection."),
 dict(q="Collusion occurs when firms", choices=[
   "compete aggressively on price",
   "agree, openly or tacitly, to restrict output or fix prices",
   "produce where P = MC",
   "enter a new market",
   "advertise heavily"], ans=1,
   why="Cooperating on price is what collusion means."),
 dict(q="A cartel is a group of firms that", choices=[
   "compete independently",
   "formally agree to act as a single monopolist by limiting output and raising price",
   "sell at marginal cost",
   "are owned by the government",
   "produce different products"], ans=1,
   why="It attempts to capture monopoly profit collectively."),
 dict(q="The main instability in a cartel comes from", choices=[
   "consumers refusing to buy",
   "each member's incentive to cheat by selling more than its quota at the high price",
   "low fixed costs",
   "government subsidies",
   "identical products"], ans=1,
   why="At the cartel price, an individual member's extra unit is highly profitable."),
 dict(q="Tacit collusion refers to", choices=[
   "a written contract to fix prices",
   "firms coordinating on high prices without any explicit agreement",
   "price competition",
   "government price setting",
   "advertising jointly"], ans=1,
   why="Repeated interaction can sustain cooperation without a formal deal."),
 dict(q="Price leadership in an oligopoly occurs when", choices=[
   "the government sets a price",
   "one firm sets its price and the others follow",
   "all firms set price equal to marginal cost",
   "prices are chosen at random",
   "firms merge"], ans=1,
   why="It is a way of coordinating without an explicit agreement."),
 dict(q="A price war in an oligopoly typically results in", choices=[
   "higher prices and higher profits",
   "lower prices and lower profits for the firms, and gains for consumers",
   "no change in prices",
   "immediate collusion",
   "a monopoly"], ans=1,
   why="Successive undercutting drives price toward cost."),
 dict(q="In a repeated game, cooperation is easier to sustain than in a one-shot game because", choices=[
   "payoffs are larger",
   "a firm that cheats can be punished by rivals in later rounds",
   "the dominant strategy disappears",
   "there are more players",
   "collusion becomes legal"], ans=1,
   why="The threat of future punishment can outweigh the one-time gain from cheating."),
 dict(q="A game in which players move simultaneously and cannot observe each other's choice first is called", choices=[
   "a sequential game", "a simultaneous game", "a repeated game", "a zero-sum game", "a dominant game"], ans=1,
   why="Neither player knows the other's move when choosing."),
 dict(q="In a sequential game, the second mover has the advantage of", choices=[
   "moving first", "observing the first player's choice before deciding", "larger payoffs always",
   "a dominant strategy always", "no information"], ans=1,
   why="Information about the earlier move can be used."),
 dict(q="A player has no dominant strategy when", choices=[
   "one strategy is best regardless of the rival's move",
   "the best choice depends on what the rival does",
   "payoffs are all equal",
   "the game is repeated",
   "there are only two players"], ans=1,
   why="Dominance requires one strategy to win against every rival choice."),
 dict(q="A game can have", choices=[
   "exactly one Nash equilibrium always",
   "one Nash equilibrium, more than one, or none in pure strategies",
   "no equilibrium ever",
   "a Nash equilibrium only if there is a dominant strategy",
   "at most two players"], ans=1,
   why="Existence and uniqueness depend on the payoff structure."),
 dict(q="If both players in a two-player game have a dominant strategy, the Nash equilibrium is", choices=[
   "impossible to determine",
   "the outcome in which each plays their dominant strategy",
   "the cooperative outcome",
   "the outcome with the highest joint payoff",
   "random"], ans=1,
   why="Neither can gain by deviating from a strategy that is best against everything."),
 dict(q="The prisoner's dilemma illustrates that", choices=[
   "cooperation always occurs",
   "individually rational choices can lead to an outcome worse for everyone",
   "dominant strategies never exist",
   "collusion is always stable",
   "payoffs are always equal"], ans=1,
   why="Both defect and both end up worse than if both had cooperated."),
 dict(q="Oligopolists that successfully collude produce a quantity closest to that of", choices=[
   "perfect competition", "a monopoly", "monopolistic competition", "a factor market", "zero output"], ans=1,
   why="A cartel behaves like a single monopolist."),
 dict(q="Oligopolists that compete aggressively on price produce a quantity closest to that of", choices=[
   "a monopoly", "perfect competition", "a cartel", "monopolistic competition", "zero output"], ans=1,
   why="Undercutting drives price toward marginal cost."),
 dict(q="The kinked demand curve model attempts to explain", choices=[
   "why oligopoly prices are often sticky",
   "why prices change constantly",
   "why entry is free",
   "why firms merge",
   "why demand is perfectly elastic"], ans=0,
   why="Rivals match price cuts but not increases, so a firm gains little from moving either way."),
 dict(q="In the kinked demand curve model, a firm believes that if it raises its price, rivals will", choices=[
   "match the increase", "not follow, so it loses many customers", "exit", "collude", "lower output"], ans=1,
   why="Its demand is elastic above the kink."),
 dict(q="In the kinked demand curve model, a firm believes that if it lowers its price, rivals will", choices=[
   "not follow", "match the cut, so it gains few customers", "exit the market", "raise their prices", "merge"], ans=1,
   why="Its demand is inelastic below the kink."),
 dict(q="Non-price competition is common in oligopoly because", choices=[
   "price cuts are illegal",
   "price cuts are easily matched by rivals, while advertising and product features are harder to copy quickly",
   "firms have no market power",
   "costs are zero",
   "demand is perfectly elastic"], ans=1,
   why="Competing where rivals cannot instantly respond is more durable."),
 dict(q="Which of the following industries is best described as an oligopoly?", choices=[
   "wheat farming", "commercial airliner manufacturing", "hair salons", "local restaurants", "street vendors"], ans=1,
   why="A handful of manufacturers accounts for essentially all global output."),
 dict(q="A four-firm concentration ratio of 90% indicates", choices=[
   "perfect competition", "a highly concentrated oligopoly", "monopolistic competition", "free entry", "a monopsony"], ans=1,
   why="Four firms accounting for nearly all sales is a concentrated market."),
 dict(q="Antitrust laws generally prohibit", choices=[
   "advertising",
   "explicit agreements among competitors to fix prices or divide markets",
   "profit maximization",
   "product differentiation",
   "entering a new market"], ans=1,
   why="Price fixing directly harms consumers by suppressing competition."),
 dict(q="Compared with perfect competition, an oligopoly generally produces", choices=[
   "more output at a lower price",
   "less output at a higher price",
   "the same output",
   "no output",
   "output at minimum average cost"], ans=1,
   why="Market power allows a markup over marginal cost."),
 dict(q="A dominant strategy equilibrium is", choices=[
   "always the outcome with the highest joint payoff",
   "a Nash equilibrium, though not necessarily the jointly best outcome",
   "never a Nash equilibrium",
   "impossible in a two-player game",
   "the same as collusion"], ans=1,
   why="The prisoner's dilemma is exactly a case where they differ."),
 dict(q="In a game where each firm's best response is to match the other's choice, there may be", choices=[
   "no equilibrium",
   "more than one Nash equilibrium",
   "a dominant strategy for each firm",
   "zero payoffs",
   "only one player"], ans=1,
   why="Coordination games commonly have multiple equilibria."),
 dict(q="Two firms choosing output levels simultaneously, each taking the other's output as given, describes", choices=[
   "a price-leadership model", "a quantity-setting oligopoly model", "perfect competition", "a monopoly", "a monopsony"], ans=1,
   why="Each firm picks its best output given a belief about the rival's."),
 dict(q="A firm considering cheating on a cartel agreement compares", choices=[
   "its fixed and variable costs",
   "the immediate gain from undercutting against the future losses if rivals retaliate",
   "price and average total cost only",
   "revenue and output",
   "its costs with the government's"], ans=1,
   why="Cheating pays now and costs later."),
 dict(q="Collusion is harder to sustain when", choices=[
   "there are only two firms",
   "there are many firms, products differ, and cheating is hard to detect",
   "firms meet frequently",
   "costs are identical",
   "the market is stable"], ans=1,
   why="More parties and less transparency make agreements fragile."),
 dict(q="Collusion is easier to sustain when", choices=[
   "there are many firms",
   "there are few firms with similar costs and prices are easily observed",
   "products are highly differentiated",
   "demand fluctuates wildly",
   "entry is free"], ans=1,
   why="Transparency and small numbers make deviations easy to spot and punish."),
 dict(q="In the prisoner's dilemma applied to advertising, both firms advertise heavily because", choices=[
   "advertising is costless",
   "each gains by advertising whatever the rival does, even though both would be better off spending less",
   "consumers demand it",
   "the government requires it",
   "advertising lowers costs"], ans=1,
   why="Advertising is the dominant strategy despite the joint waste."),
 dict(q="If a game has a unique Nash equilibrium that is not the jointly best outcome, the firms", choices=[
   "will always reach the jointly best outcome",
   "would both prefer to cooperate but cannot do so credibly without some enforcement",
   "have no dominant strategy",
   "earn identical payoffs to the cooperative outcome",
   "face no strategic interaction"], ans=1,
   why="Individual incentives pull them away from the cooperative point."),
 dict(q="Which of the following would most likely destabilize an existing cartel?", choices=[
   "a fall in the number of members",
   "the entry of a new producer outside the agreement",
   "increased price transparency",
   "identical costs across members",
   "a long-standing relationship among members"], ans=1,
   why="An outsider undercutting the cartel price takes sales the members cannot retaliate against."),
 dict(q="Compared with a monopoly, an oligopoly that does not collude will typically produce", choices=[
   "less output at a higher price",
   "more output at a lower price",
   "exactly the monopoly output",
   "no output",
   "output where P = MC"], ans=1,
   why="Competition among the few pushes output above the monopoly level."),
 dict(q="The reason oligopoly outcomes are hard to predict is that", choices=[
   "firms have no costs",
   "the result depends on how firms expect their rivals to behave, which can vary",
   "demand does not exist",
   "there is only one firm",
   "entry is always free"], ans=1,
   why="Outcomes range from near-monopoly under collusion to near-competitive in a price war."),
 dict(q="A firm in an oligopoly that credibly commits to matching any rival's price cut is trying to", choices=[
   "start a price war",
   "deter rivals from cutting price in the first place",
   "raise its own costs",
   "exit the market",
   "achieve allocative efficiency"], ans=1,
   why="If cutting price wins no customers, no rival has a reason to try it."),
 dict(q="Which best describes the welfare effect of successful collusion in an oligopoly?", choices=[
   "consumers gain and total surplus rises",
   "consumers lose, firms gain, and total surplus falls because output is restricted",
   "no one is affected",
   "firms lose and consumers gain",
   "total surplus is maximized"], ans=1,
   why="It reproduces the monopoly outcome, transfer and deadweight loss alike."),
]
