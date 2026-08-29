# 4.1 Introduction to Imperfectly Competitive Markets — 50 questions
TOPIC = ("4.1", "Introduction to Imperfectly Competitive Markets", 4)
STRUCT = dict(headers=["Market", "Number of firms", "Product"],
              rows=[["W", "very many", "identical"], ["X", "one", "unique, no close substitutes"],
                    ["Y", "many", "differentiated"], ["Z", "a few", "identical or differentiated"]])
QUESTIONS = [
 dict(q="An imperfectly competitive market is one in which", choices=[
   "all firms are price takers",
   "at least one firm has some ability to influence the price of its product",
   "there is no product to sell",
   "entry is always free",
   "products are always identical"], ans=1,
   why="Market power, the ability to affect price, is what makes a market imperfectly competitive."),
 dict(q="Market power is best defined as a firm's ability to", choices=[
   "produce at the lowest cost",
   "raise its price above marginal cost without losing all of its customers",
   "hire any number of workers",
   "eliminate its fixed costs",
   "predict consumer demand"], ans=1,
   why="A price taker loses all sales if it raises price; a firm with market power does not."),
 dict(q="A firm with market power faces a demand curve that is", choices=[
   "horizontal", "downward sloping", "vertical", "upward sloping", "perfectly elastic"], ans=1,
   why="To sell more it must lower its price, which is what a downward-sloping curve means."),
 dict(q="Which of the following is NOT one of the four basic market structures?", choices=[
   "perfect competition", "monopoly", "monopolistic competition", "comparative advantage", "oligopoly"], ans=3,
   why="Comparative advantage is a trade concept, not a market structure."),
 dict(q="Using the table, Market W is best described as", table=STRUCT, choices=[
   "monopoly", "perfect competition", "oligopoly", "monopolistic competition", "monopsony"], ans=1,
   why="Very many firms selling an identical product is the definition of perfect competition."),
 dict(q="Using the table, Market X is best described as", table=STRUCT, choices=[
   "perfect competition", "monopoly", "oligopoly", "monopolistic competition", "a factor market"], ans=1,
   why="A single seller of a product with no close substitutes is a monopoly."),
 dict(q="Using the table, Market Y is best described as", table=STRUCT, choices=[
   "monopoly", "monopolistic competition", "perfect competition", "oligopoly", "monopsony"], ans=1,
   why="Many firms selling differentiated products describes monopolistic competition."),
 dict(q="Using the table, Market Z is best described as", table=STRUCT, choices=[
   "perfect competition", "oligopoly", "monopoly", "monopolistic competition", "a competitive factor market"], ans=1,
   why="A few interdependent firms is an oligopoly, whether or not the product is differentiated."),
 dict(q="Using the table, which markets are imperfectly competitive?", table=STRUCT, choices=[
   "W only", "X, Y, and Z", "W and Y", "X only", "none of them"], ans=1,
   why="Only Market W is perfectly competitive; the other three all involve some market power."),
 dict(q="For any firm with market power, marginal revenue is", choices=[
   "equal to price", "less than price", "greater than price", "always zero", "equal to marginal cost"], ans=1,
   why="Selling one more unit requires cutting the price on all units, so MR falls below P."),
 dict(q="For a price taker, marginal revenue equals price because", choices=[
   "the firm sets its own price",
   "the firm can sell additional units without lowering the price on units it already sells",
   "marginal cost is constant",
   "demand is downward sloping",
   "there are no fixed costs"], ans=1,
   why="No price cut is needed, so the extra unit adds exactly its price to revenue."),
 dict(q="A barrier to entry is", choices=[
   "anything that makes it difficult for new firms to enter a market",
   "a cost paid by every firm equally",
   "the same as a fixed cost",
   "a legal requirement to produce",
   "a limit on how much a firm may sell"], ans=0,
   why="Barriers are what allow market power to persist in the long run."),
 dict(q="Which of the following is a barrier to entry?", choices=[
   "many potential competitors",
   "a patent granting exclusive rights to produce a product",
   "low startup costs",
   "widely available technology",
   "identical products"], ans=1,
   why="A patent legally excludes rivals for a period of time."),
 dict(q="Economies of scale can act as a barrier to entry because", choices=[
   "large firms have higher costs",
   "a new small entrant would face higher average costs than the established large firm",
   "they raise marginal revenue",
   "they eliminate fixed costs",
   "they make products identical"], ans=1,
   why="An entrant cannot match the incumbent's price without matching its scale."),
 dict(q="Control of a key scarce resource creates market power because", choices=[
   "it lowers the firm's costs to zero",
   "rivals cannot obtain the input needed to compete",
   "consumers prefer that firm",
   "the government requires it",
   "it raises marginal revenue above price"], ans=1,
   why="Without the input, no competitor can produce at all."),
 dict(q="Which of the following is a legal barrier to entry?", choices=[
   "brand loyalty",
   "a government-issued exclusive licence",
   "high transportation costs",
   "a large advertising budget",
   "a network of loyal suppliers"], ans=1,
   why="A licence excludes competitors by law rather than by economics."),
 dict(q="Product differentiation means that", choices=[
   "all firms sell an identical good",
   "firms sell products consumers perceive as distinct from one another",
   "there is only one seller",
   "products are sold at the same price",
   "entry is blocked"], ans=1,
   why="Perceived differences give each firm a small amount of pricing discretion."),
 dict(q="Compared with a perfectly competitive firm, a firm with market power generally produces", choices=[
   "more output at a lower price",
   "less output at a higher price",
   "the same output at the same price",
   "more output at a higher price",
   "no output"], ans=1,
   why="Restricting output is how the firm sustains a price above marginal cost."),
 dict(q="A market with market power typically generates", choices=[
   "maximum total surplus",
   "deadweight loss, because price exceeds marginal cost",
   "no consumer surplus at all",
   "zero producer surplus",
   "allocative efficiency"], ans=1,
   why="Units worth more to buyers than they cost to make go unproduced."),
 dict(q="Every profit-maximizing firm, regardless of market structure, produces where", choices=[
   "price equals average total cost",
   "marginal revenue equals marginal cost",
   "price equals marginal cost",
   "total revenue is maximized",
   "average total cost is minimized"], ans=1,
   why="MR = MC is the general rule; only the shape of MR differs across structures."),
 dict(q="The key difference between perfect competition and imperfect competition in the profit-maximizing condition is that under imperfect competition", choices=[
   "MR = MC no longer applies",
   "price exceeds marginal revenue, so price also exceeds marginal cost at the chosen output",
   "marginal cost is negative",
   "output is always zero",
   "average cost is minimized"], ans=1,
   why="Since MR < P, setting MR = MC leaves P above MC."),
 dict(q="Concentration in a market refers to", choices=[
   "the share of total output produced by the largest firms",
   "the level of fixed costs",
   "the number of consumers",
   "the elasticity of demand",
   "the size of the deadweight loss"], ans=0,
   why="Concentration measures how much of the market the biggest sellers account for."),
 dict(q="A four-firm concentration ratio of 85% suggests a market that is", choices=[
   "perfectly competitive", "highly concentrated, likely an oligopoly", "a monopsony", "unregulated by definition", "in long-run equilibrium"], ans=1,
   why="A few firms accounting for most sales is the hallmark of oligopoly."),
 dict(q="A four-firm concentration ratio close to 0% suggests", choices=[
   "a monopoly", "a market with many small sellers, close to perfect competition", "an oligopoly", "a cartel", "high barriers to entry"], ans=1,
   why="No firm accounts for a meaningful share of sales."),
 dict(q="In which market structure do firms most clearly take account of rivals' likely reactions?", choices=[
   "perfect competition", "oligopoly", "monopoly", "monopolistic competition", "a competitive factor market"], ans=1,
   why="With only a few firms, each one's decision materially affects the others."),
 dict(q="Interdependence among firms is a defining feature of", choices=[
   "perfect competition", "oligopoly", "monopoly", "monopolistic competition", "perfectly competitive factor markets"], ans=1,
   why="A small number of rivals makes strategic reaction unavoidable."),
 dict(q="Which market structure has the greatest degree of market power?", choices=[
   "perfect competition", "monopoly", "monopolistic competition", "oligopoly", "all are equal"], ans=1,
   why="A single seller with no close substitutes faces the whole market demand curve."),
 dict(q="Which market structure has the least market power?", choices=[
   "monopoly", "perfect competition", "oligopoly", "monopolistic competition", "a cartel"], ans=1,
   why="A price taker has none at all."),
 dict(q="In the long run, firms in monopolistic competition earn", choices=[
   "positive economic profit", "zero economic profit, because entry is free", "large losses", "the same profit as a monopoly", "zero accounting profit"], ans=1,
   why="Free entry competes profits away despite the differentiated product."),
 dict(q="A monopoly can earn positive economic profit in the long run because", choices=[
   "its costs are always lower",
   "barriers to entry prevent competitors from arriving to compete the profit away",
   "it faces a horizontal demand curve",
   "it produces where P = MC",
   "consumers are irrational"], ans=1,
   why="Without entry, nothing erodes the profit."),
 dict(q="Which of the following markets is closest to monopolistic competition?", choices=[
   "wheat farming", "local restaurants", "municipal tap water", "commercial airliners", "electricity transmission"], ans=1,
   why="Many restaurants compete, each offering a distinguishable experience."),
 dict(q="Which of the following markets is closest to oligopoly?", choices=[
   "corn farming", "commercial airliner manufacturing", "hair salons", "residential water service", "street food vendors"], ans=1,
   why="A very small number of manufacturers accounts for essentially all output."),
 dict(q="Which of the following markets is closest to monopoly?", choices=[
   "clothing retail", "a town's only piped water utility", "coffee shops", "used-car dealerships", "soybean farming"], ans=1,
   why="One provider serves the whole market with no close substitute."),
 dict(q="An imperfectly competitive firm chooses", choices=[
   "only its quantity, taking price as given",
   "a point on its demand curve, so choosing quantity determines its price",
   "price and quantity independently of each other",
   "neither price nor quantity",
   "only its price, with quantity fixed"], ans=1,
   why="Demand ties the two together: setting one determines the other."),
 dict(q="A firm with market power that raises its price will", choices=[
   "lose all of its customers",
   "lose some but not all of its customers",
   "gain customers",
   "keep exactly the same customers",
   "be forced to exit"], ans=1,
   why="Its demand curve slopes downward rather than being horizontal."),
 dict(q="Which of the following increases a firm's market power?", choices=[
   "the arrival of a close substitute",
   "a successful advertising campaign that strengthens brand loyalty",
   "the expiry of its patent",
   "a fall in barriers to entry",
   "standardization of the product"], ans=1,
   why="Stronger loyalty makes the firm's demand less sensitive to its price."),
 dict(q="Which of the following reduces a firm's market power?", choices=[
   "a new patent",
   "the entry of firms selling close substitutes",
   "control of a scarce input",
   "increased brand loyalty",
   "a government-granted monopoly"], ans=1,
   why="More substitutes make the firm's demand more elastic."),
 dict(q="A natural monopoly exists when", choices=[
   "the government owns the firm",
   "one firm can supply the entire market at a lower average cost than two or more could",
   "there are no fixed costs",
   "the product is a natural resource",
   "many firms produce identical goods"], ans=1,
   why="Economies of scale over the whole range of demand make a single producer cheapest."),
 dict(q="Under imperfect competition, price is generally", choices=[
   "equal to marginal cost", "above marginal cost", "below marginal cost", "equal to marginal revenue", "zero"], ans=1,
   why="A markup over marginal cost is the visible sign of market power."),
 dict(q="Allocative inefficiency under imperfect competition arises because", choices=[
   "firms produce at minimum average cost",
   "the price buyers pay for the last unit exceeds what it cost to produce",
   "firms earn zero profit",
   "there are too many firms",
   "marginal revenue equals price"], ans=1,
   why="Some mutually beneficial trades do not happen."),
 dict(q="A cartel is", choices=[
   "a single firm with a patent",
   "a group of firms that agree to act together to restrict output and raise price",
   "a government agency",
   "a firm that sells at marginal cost",
   "a competitive industry association"], ans=1,
   why="Colluding firms attempt to behave like a single monopolist."),
 dict(q="The main problem facing a cartel is that", choices=[
   "consumers refuse to buy",
   "each member has an incentive to cheat by producing more than its quota",
   "prices fall below marginal cost",
   "governments always subsidize entry",
   "marginal revenue exceeds price"], ans=1,
   why="At the cartel price, an individual member's extra output is highly profitable."),
 dict(q="Which of the following is true of both perfect competition and monopolistic competition in the long run?", choices=[
   "price equals marginal cost",
   "economic profit is driven to zero by entry",
   "firms produce at minimum average total cost",
   "products are identical",
   "firms are price takers"], ans=1,
   why="Free entry is common to both, though only perfect competition also gives P = MC."),
 dict(q="Which of the following distinguishes monopolistic competition from perfect competition?", choices=[
   "the number of firms is small",
   "products are differentiated, so each firm faces a downward-sloping demand curve",
   "entry is blocked",
   "firms earn long-run profit",
   "there is a single seller"], ans=1,
   why="Differentiation is the sole essential difference."),
 dict(q="Which of the following distinguishes oligopoly from monopolistic competition?", choices=[
   "products may be differentiated",
   "the small number of firms makes each one's decisions depend on its rivals' expected responses",
   "firms maximize profit",
   "demand slopes downward",
   "firms may advertise"], ans=1,
   why="Strategic interdependence is what makes oligopoly distinct."),
 dict(q="A firm in an imperfectly competitive market that produces where P = MC would", choices=[
   "maximize its profit",
   "produce more than the profit-maximizing quantity and earn less profit",
   "produce nothing",
   "earn maximum revenue",
   "minimize average cost"], ans=1,
   why="Beyond MR = MC the extra units cost more than they add to revenue."),
 dict(q="For a firm with a downward-sloping demand curve, marginal revenue is zero when total revenue is", choices=[
   "zero", "at its maximum", "at its minimum", "equal to total cost", "negative"], ans=1,
   why="Revenue stops rising exactly when an extra unit adds nothing to it."),
 dict(q="A profit-maximizing firm with market power will never operate on the portion of its demand curve where demand is", choices=[
   "elastic", "inelastic", "unit elastic", "downward sloping", "linear"], ans=1,
   why="Where demand is inelastic, MR is negative and cutting output raises revenue while lowering cost."),
 dict(q="Imperfect competition is common in the real world mainly because", choices=[
   "governments require it",
   "differentiated products, scale economies, and barriers to entry are widespread",
   "consumers dislike low prices",
   "firms cannot compute marginal cost",
   "perfect information is illegal"], ans=1,
   why="The conditions for perfect competition are demanding and rarely all hold."),
 dict(q="The efficiency case against market power rests on the fact that firms with market power", choices=[
   "earn accounting profit",
   "restrict output below the level at which price would equal marginal cost",
   "employ workers",
   "advertise their products",
   "have downward-sloping demand curves"], ans=1,
   why="The lost output is the deadweight loss."),
]
