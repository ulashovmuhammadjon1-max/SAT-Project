# 6.3 Public and Private Goods — 50 questions
TOPIC = ("6.3", "Public and Private Goods", 6)
GOODS = dict(headers=["Good", "Rival in consumption?", "Excludable?"],
             rows=[["P", "yes", "yes"], ["Q", "no", "no"],
                   ["R", "yes", "no"], ["S", "no", "yes"]])
QUESTIONS = [
 dict(q="A good is rival in consumption when", choices=[
   "many people want it",
   "one person's use of it reduces the amount available for others",
   "it is expensive",
   "it is sold in a market",
   "the government provides it"], ans=1,
   why="Rivalry is about whether consumption uses the good up."),
 dict(q="A good is excludable when", choices=[
   "it is scarce",
   "it is possible to prevent people who do not pay from consuming it",
   "it is produced privately",
   "it costs nothing to produce",
   "everyone can use it"], ans=1,
   why="Excludability is about whether non-payers can be kept out."),
 dict(q="A private good is", choices=[
   "non-rival and non-excludable",
   "both rival and excludable",
   "rival but not excludable",
   "excludable but not rival",
   "provided only by government"], ans=1,
   why="A sandwich is used up by one eater and can be withheld from non-payers."),
 dict(q="A public good is", choices=[
   "both rival and excludable",
   "both non-rival and non-excludable",
   "rival but not excludable",
   "non-rival but excludable",
   "any good the government provides"], ans=1,
   why="National defence is the classic case."),
 dict(q="A common resource is", choices=[
   "non-rival and non-excludable",
   "rival but not excludable",
   "rival and excludable",
   "non-rival but excludable",
   "always privately owned"], ans=1,
   why="Ocean fish are used up when caught but no one can be excluded."),
 dict(q="A club good, or artificially scarce good, is", choices=[
   "rival and excludable",
   "non-rival but excludable",
   "rival but not excludable",
   "non-rival and non-excludable",
   "free to everyone"], ans=1,
   why="A subscription streaming service is not used up by an extra viewer but non-payers can be blocked."),
 dict(q="Using the table, Good P is", table=GOODS, choices=[
   "a public good", "a private good", "a common resource", "a club good", "not a good at all"], ans=1,
   why="Rival and excludable is the definition of a private good."),
 dict(q="Using the table, Good Q is", table=GOODS, choices=[
   "a private good", "a public good", "a common resource", "a club good", "a merit good"], ans=1,
   why="Non-rival and non-excludable is the definition of a public good."),
 dict(q="Using the table, Good R is", table=GOODS, choices=[
   "a private good", "a common resource", "a public good", "a club good", "a merit good"], ans=1,
   why="Rival but non-excludable describes a common resource."),
 dict(q="Using the table, Good S is", table=GOODS, choices=[
   "a private good", "a club good", "a public good", "a common resource", "a free good"], ans=1,
   why="Non-rival but excludable describes a club good."),
 dict(q="Using the table, which good is most subject to the free-rider problem?", table=GOODS, choices=[
   "P", "Q", "R", "S", "none of them"], ans=1,
   why="Non-excludability plus non-rivalry means everyone can benefit without paying."),
 dict(q="Using the table, which good is most subject to overuse, as in the tragedy of the commons?", table=GOODS, choices=[
   "P", "Q", "R", "S", "none of them"], ans=2,
   why="Rivalry combined with open access leads each user to take too much."),
 dict(q="The free-rider problem occurs when", choices=[
   "a good is too expensive",
   "people can consume a good without paying, so private markets undersupply it",
   "the government overproduces a good",
   "a firm has market power",
   "a good is rival"], ans=1,
   why="Non-excludability destroys the incentive to pay."),
 dict(q="Public goods tend to be underprovided by private markets because", choices=[
   "they cost too much to produce",
   "producers cannot exclude non-payers, so they cannot capture the value they create",
   "no one wants them",
   "they are rival in consumption",
   "the government forbids private provision"], ans=1,
   why="Without excludability there is no revenue to fund production."),
 dict(q="Which of the following is the best example of a pure public good?", choices=[
   "a cheeseburger", "national defence", "a movie ticket", "a fish in the ocean", "a private garden"], ans=1,
   why="One person's protection does not reduce anyone else's, and no citizen can be excluded."),
 dict(q="Which of the following is the best example of a common resource?", choices=[
   "national defence", "fish in the open ocean", "a cable television subscription", "a bicycle", "a lighthouse"], ans=1,
   why="Each fish caught is unavailable to others, and access cannot be restricted."),
 dict(q="Which of the following is the best example of a club good?", choices=[
   "a public park during a crowd", "a subscription streaming service", "a hamburger", "clean air", "an ocean fishery"], ans=1,
   why="An extra subscriber costs almost nothing to serve but non-subscribers are blocked."),
 dict(q="Which of the following is the best example of a private good?", choices=[
   "street lighting", "a pair of shoes", "national defence", "the atmosphere", "a public radio broadcast"], ans=1,
   why="Shoes are used by one person and can be withheld from non-payers."),
 dict(q="The marginal cost of providing a public good to one more consumer is", choices=[
   "very high", "essentially zero, because the good is non-rival", "equal to the price", "rising", "equal to average cost"], ans=1,
   why="Non-rivalry means the extra user consumes nothing others lose."),
 dict(q="Because the marginal cost of an additional user of a non-rival good is zero, efficiency requires", choices=[
   "a high price", "a price of zero for access, with the fixed cost funded some other way", "excluding some users", "rationing", "a quota"], ans=1,
   why="Charging above marginal cost would exclude users who value the good positively."),
 dict(q="The efficient quantity of a public good is found by", choices=[
   "adding individuals' demand curves horizontally",
   "adding individuals' marginal benefits vertically and setting the sum equal to marginal cost",
   "using one consumer's demand only",
   "setting price equal to zero",
   "maximizing output"], ans=1,
   why="Everyone consumes the same quantity, so their benefits add at each quantity."),
 dict(q="For a private good, the market demand curve is found by", choices=[
   "adding individual demand curves vertically",
   "adding the quantities individuals demand at each price",
   "using the largest buyer's demand",
   "setting price equal to marginal cost",
   "adding marginal benefits vertically"], ans=1,
   why="Different people can consume different quantities of a private good."),
 dict(q="Three residents value a streetlight at $40, $30, and $20 per year. The efficient outcome is to provide it if its cost is", choices=[
   "more than $90", "$90 or less", "more than $40", "$40 or less", "any amount"], ans=1,
   why="The benefits sum to $90 because all three enjoy the same light."),
 dict(q="In the previous scenario, a private market would likely fail to provide the streetlight because", choices=[
   "the cost is too high",
   "each resident hopes the others will pay and no one can be excluded from the light",
   "the light is rival",
   "the government forbids it",
   "residents do not value it"], ans=1,
   why="Free riding leaves the cost uncovered even though the benefits exceed it."),
 dict(q="A cost-benefit analysis of a public good compares", choices=[
   "the price with average cost",
   "the total benefit to all citizens with the total cost of provision",
   "producer surplus with consumer surplus",
   "one person's willingness to pay with the cost",
   "revenue with profit"], ans=1,
   why="Since all consume it jointly, benefits are summed across everyone."),
 dict(q="A difficulty in cost-benefit analysis of public goods is that", choices=[
   "costs are unknowable",
   "people have an incentive to misstate how much they value the good",
   "benefits are always zero",
   "the good is rival",
   "governments cannot tax"], ans=1,
   why="Understating value to reduce one's tax share, or overstating it to get the good, are both tempting."),
 dict(q="Government provision of public goods is usually funded by", choices=[
   "user fees only", "taxation", "voluntary donations only", "profit", "borrowing only"], ans=1,
   why="Compulsory contribution solves the free-rider problem."),
 dict(q="A lighthouse is a classic example of a public good because", choices=[
   "it is expensive",
   "one ship's use of the light does not diminish another's, and passing ships cannot be excluded",
   "governments build lighthouses",
   "it is rival",
   "it serves only one ship"], ans=1,
   why="Both defining conditions hold."),
 dict(q="A crowded public road is best described as", choices=[
   "a pure public good",
   "a common resource, since it is non-excludable but congestion makes it rival",
   "a private good",
   "a club good",
   "not a good"], ans=1,
   why="Congestion is what makes each extra driver reduce what is available to others."),
 dict(q="An uncrowded public road is closest to", choices=[
   "a common resource", "a public good, since one more car does not reduce anyone else's use", "a private good", "a club good", "a merit good"], ans=1,
   why="Without congestion the road is effectively non-rival."),
 dict(q="A toll road is best described as", choices=[
   "a public good", "a club good if uncongested, since tolls make it excludable", "a common resource", "a private good always", "a free good"], ans=1,
   why="The toll supplies excludability that an open road lacks."),
 dict(q="Clean air is usually classified as", choices=[
   "a private good", "a public good, since it is non-rival and non-excludable", "a club good", "a rival good", "an excludable good"], ans=1,
   why="Nobody can be prevented from breathing it and one person's breathing does not deplete it."),
 dict(q="The tragedy of the commons results from", choices=[
   "government ownership",
   "individual users ignoring the cost their use imposes on other users of a rival, non-excludable resource",
   "excludability",
   "non-rivalry",
   "high prices"], ans=1,
   why="Each user's private calculation omits the depletion others suffer."),
 dict(q="Which policy would best address overfishing of a common resource?", choices=[
   "eliminating all regulation",
   "assigning transferable catch quotas that make the fishery excludable",
   "subsidizing fishing boats",
   "increasing the number of fishers",
   "lowering the price of fish"], ans=1,
   why="Creating enforceable rights restores the incentive to conserve."),
 dict(q="Knowledge, once discovered, is largely", choices=[
   "rival and excludable",
   "non-rival, since one person's use does not prevent another's",
   "always excludable",
   "a common resource",
   "a private good"], ans=1,
   why="An idea can be used by many people at once."),
 dict(q="Patents make new knowledge temporarily excludable in order to", choices=[
   "reduce the number of inventions",
   "give inventors a way to earn a return, since without exclusion others could free ride",
   "eliminate market power",
   "lower prices",
   "make knowledge rival"], ans=1,
   why="It trades some deadweight loss for the incentive to innovate."),
 dict(q="A merit good is one that", choices=[
   "is non-rival and non-excludable",
   "society judges people to under-consume relative to what would be good for them",
   "cannot be produced privately",
   "has no cost",
   "is always a public good"], ans=1,
   why="It is a normative category rather than a rivalry-excludability one."),
 dict(q="Which of the following is NOT a characteristic of a pure public good?", choices=[
   "non-rivalry", "non-excludability", "the ability to charge non-payers", "joint consumption", "susceptibility to free riding"], ans=2,
   why="Being unable to charge non-payers is precisely the problem."),
 dict(q="If a good is non-rival but a firm can exclude non-payers, a private market will", choices=[
   "fail entirely",
   "provide it, though charging a positive price excludes some users who value it, creating inefficiency",
   "provide the efficient quantity",
   "provide it free",
   "never provide it"], ans=1,
   why="Provision is possible but pricing above the zero marginal cost is inefficient."),
 dict(q="Public goods are sometimes provided privately through", choices=[
   "impossible arrangements",
   "voluntary contributions, philanthropy, or bundling with an excludable product",
   "taxation only",
   "monopoly pricing",
   "rationing"], ans=1,
   why="Free radio funded by advertising is a familiar example."),
 dict(q="Free radio broadcasting funded by advertisements shows that", choices=[
   "public goods can never be privately provided",
   "a non-excludable good can sometimes be funded by selling an excludable complement",
   "radio is a private good",
   "advertising is a public good",
   "listeners pay directly"], ans=1,
   why="The advertisers, not the listeners, are the paying customers."),
 dict(q="The efficient provision of a public good requires that", choices=[
   "each individual's marginal benefit equals marginal cost",
   "the sum of all individuals' marginal benefits equals the marginal cost",
   "price equals marginal cost",
   "output be maximized",
   "each person pay the same amount"], ans=1,
   why="All consume the same unit, so their benefits add."),
 dict(q="Two neighbours value a shared fence at $200 and $150. The fence costs $300. The efficient outcome is", choices=[
   "not to build it", "to build it, since $350 of total benefit exceeds the $300 cost", "for one neighbour to pay everything", "to build half a fence", "indeterminate"], ans=1,
   why="Summed benefits exceed the cost."),
 dict(q="In that scenario, neither neighbour builds the fence alone because", choices=[
   "they dislike each other",
   "$300 exceeds each individual's own valuation, so each hopes the other will pay",
   "the fence is rival",
   "the cost is unknown",
   "the fence is illegal"], ans=1,
   why="Individual willingness to pay is below cost even though the sum is above it."),
 dict(q="Government provision is one solution to the public goods problem because government can", choices=[
   "produce at zero cost",
   "compel payment through taxation, overcoming free riding",
   "exclude non-payers",
   "make the good rival",
   "eliminate demand"], ans=1,
   why="Compulsion is what a voluntary market lacks."),
 dict(q="A criticism of government provision of public goods is that", choices=[
   "it is always cheaper",
   "government may not know citizens' true valuations and so may provide the wrong quantity",
   "free riding increases",
   "the good becomes rival",
   "taxes cannot be collected"], ans=1,
   why="The preference-revelation problem does not disappear under public provision."),
 dict(q="A national park that becomes crowded shifts from behaving like a public good toward", choices=[
   "a private good", "a common resource, as congestion introduces rivalry", "a club good", "a merit good", "a free good"], ans=1,
   why="Rivalry appears while non-excludability remains."),
 dict(q="Charging an entrance fee to a national park makes it", choices=[
   "non-rival", "excludable, moving it toward a club good or private good", "a public good", "a common resource", "free"], ans=1,
   why="A fee is exactly a mechanism for exclusion."),
 dict(q="The key economic reason public goods require collective action is", choices=[
   "they are expensive",
   "non-excludability means private sellers cannot capture the benefits they create",
   "they are rival",
   "governments prefer to provide them",
   "consumers do not value them"], ans=1,
   why="Without a way to charge, no private producer has a reason to supply."),
 dict(q="Which pair of characteristics defines the four categories of goods?", choices=[
   "price and quantity",
   "rivalry in consumption and excludability",
   "cost and benefit",
   "supply and demand",
   "public and private ownership"], ans=1,
   why="The two-by-two of rival/non-rival and excludable/non-excludable generates all four types."),
]
