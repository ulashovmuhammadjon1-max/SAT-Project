# AP PSYCHOLOGY 2.2 Thinking, Problem-Solving, Judgments, and Decision-Making
# — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition. Learning objective 2.2.A.
#
# Essential knowledge relied on: 2.2.A.1 concepts as the basis of thought and
# prototypes as the ideal example of a concept; 2.2.A.2 schemas modified through
# assimilation (taking in new information WITHOUT changing the schema) and
# accommodation (taking it in AND changing the schema); 2.2.A.3 algorithms, which
# try all possible solutions until the correct one is found; 2.2.A.4 heuristics
# as mental shortcuts, with the representativeness heuristic (judging by prior
# expectations or stereotypes) and the availability heuristic (recalling the
# first or most vivid example); 2.2.A.5 mental set, priming, and framing;
# 2.2.A.6 the gambler's fallacy and the sunk-cost fallacy; 2.2.A.7 executive
# functions; 2.2.A.8 creativity, divergent versus convergent thinking, and
# functional fixedness.
#
# This is the topic where every term has a near neighbour it gets confused with,
# so most items are scenarios that fit exactly one of them and the distractors
# are the neighbours: representativeness against availability, gambler's fallacy
# against sunk cost, mental set against functional fixedness, assimilation
# against accommodation, algorithm against heuristic. Each verify_p2_2.py claim
# names which neighbour the item is separating the key from and why the scenario
# excludes it.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
TOPIC = ("2.2", "Thinking, Problem-Solving, Judgments, and Decision-Making", 2)
QUESTIONS = [
 dict(q="In the AP Psychology framework, concepts are best described as", choices=[
   "mental categories that form the basis of thought",
   "step-by-step procedures that guarantee a correct answer",
   "shortcuts that speed up judgment at the cost of accuracy",
   "vivid memories of specific past events"], ans=0,
   why="EK 2.2.A.1 states that concepts form the basis of thought; the other options describe algorithms, heuristics, and memories respectively."),
 dict(q="A prototype is best defined as", choices=[
   "the ideal example of a given concept",
   "a category that has no clear members",
   "a rule that must be applied to every case",
   "a memory of the first time a concept was learned"], ans=0,
   why="EK 2.2.A.1 states that prototypes are the ideal example for any given concept."),
 dict(q="Asked to name a bird, most people say \"robin\" rather than \"penguin.\" This is best explained by", choices=[
   "the robin being closer to most people's prototype of a bird",
   "the penguin belonging to a different concept altogether",
   "the availability of a bird's name in short-term memory",
   "an algorithm producing the fastest possible answer"], ans=0,
   why="EK 2.2.A.1's prototype is the ideal example of a concept, and a robin fits most people's ideal bird more closely than a penguin does, even though both are genuinely birds."),
 dict(q="A child who has a schema for \"dog\" sees a small horse for the first time and calls it a dog, without altering her idea of what a dog is. This is", choices=[
   "assimilation",
   "accommodation",
   "a mental set",
   "convergent thinking"], ans=0,
   why="EK 2.2.A.2 defines assimilation as taking in new information but NOT changing the schema in light of it, which is exactly what fitting the horse into the existing dog schema does."),
 dict(q="The same child is told the animal is a horse and revises her idea of \"dog\" so that four-legged animals of that size are no longer included. This is", choices=[
   "accommodation",
   "assimilation",
   "priming",
   "functional fixedness"], ans=0,
   why="EK 2.2.A.2 defines accommodation as taking in new information AND changing the schema to incorporate it, which is what revising the dog category does."),
 dict(q="Which statement correctly distinguishes assimilation from accommodation?", choices=[
   "assimilation leaves the existing schema unchanged; accommodation revises it",
   "accommodation leaves the existing schema unchanged; assimilation revises it",
   "assimilation applies to children and accommodation to adults",
   "assimilation concerns memory while accommodation concerns perception"], ans=0,
   why="EK 2.2.A.2 defines the pair by whether the schema itself changes, which is the only feature that separates them; the first distractor is that definition reversed."),
 dict(q="An algorithm is best described as a problem-solving approach that", choices=[
   "tries all possible solutions until the correct one is found",
   "uses a mental shortcut to reach a quick judgment",
   "relies on the first example that comes to mind",
   "applies a solution that worked on a previous problem"], ans=0,
   why="EK 2.2.A.3 states that algorithms address problems by attempting all possible solutions until the correct one is found."),
 dict(q="Heuristics differ from algorithms in that heuristics", choices=[
   "use mental shortcuts and so can produce errors in judgment",
   "are guaranteed to reach the correct answer eventually",
   "can only be used on mathematical problems",
   "require more time and effort than algorithms do"], ans=0,
   why="EK 2.2.A.4 states that heuristics address problems by using mental shortcuts to make judgments and that using them can lead to errors in judgment; EK 2.2.A.3's algorithms trade speed for certainty in the opposite direction."),
 dict(q="A person trying to unscramble the letters A, E, L, P, P into a word systematically works through every possible ordering. She is using", choices=[
   "an algorithm",
   "a heuristic",
   "a mental set",
   "divergent thinking"], ans=0,
   why="EK 2.2.A.3's algorithm is defined by attempting all possible solutions until the correct one is found, which is precisely what working through every ordering does."),
 dict(q="Told that a quiet man who loves books is either a librarian or a salesperson, most people guess librarian, even though there are far more salespeople. This judgment reflects", choices=[
   "the representativeness heuristic",
   "the availability heuristic",
   "the gambler's fallacy",
   "the sunk-cost fallacy"], ans=0,
   why="EK 2.2.A.4 describes the representativeness heuristic as making decisions according to prior expectations or stereotypes; the man is judged by how well he matches a stereotype rather than by how common each occupation is."),
 dict(q="After watching several news reports about shark attacks, a swimmer greatly overestimates how likely such an attack is. This judgment reflects", choices=[
   "the availability heuristic",
   "the representativeness heuristic",
   "functional fixedness",
   "a mental set"], ans=0,
   why="EK 2.2.A.4 describes the availability heuristic as recalling the first or most vivid example that comes to mind, which is what vivid news coverage supplies."),
 dict(q="Which statement correctly distinguishes the representativeness heuristic from the availability heuristic?", choices=[
   "representativeness judges by resemblance to a stereotype; availability judges by how easily an example comes to mind",
   "availability judges by resemblance to a stereotype; representativeness judges by how easily an example comes to mind",
   "representativeness applies to people and availability applies to objects",
   "representativeness is always accurate while availability is always mistaken"], ans=0,
   why="EK 2.2.A.4 separates the two by their basis -- prior expectations and stereotypes on one side, the first or most vivid example recalled on the other -- and the first distractor is that separation reversed."),
 dict(q="A coin has landed on heads six times in a row. A gambler concludes that tails is now \"due.\" This reasoning is", choices=[
   "the gambler's fallacy",
   "the sunk-cost fallacy",
   "the availability heuristic",
   "functional fixedness"], ans=0,
   why="EK 2.2.A.6 names the gambler's fallacy among the cognitive processes that hinder good decisions; independent events do not become more likely because they have not occurred recently."),
 dict(q="Two hours into a film she is not enjoying, a viewer stays to the end because she has already paid for the ticket and sat through most of it. This reasoning is", choices=[
   "the sunk-cost fallacy",
   "the gambler's fallacy",
   "the representativeness heuristic",
   "convergent thinking"], ans=0,
   why="EK 2.2.A.6 names the sunk-cost fallacy; the decision is driven by resources already spent and unrecoverable rather than by the value of continuing."),
 dict(q="Which statement correctly distinguishes the gambler's fallacy from the sunk-cost fallacy?", choices=[
   "the gambler's fallacy misjudges the probability of a future event; the sunk-cost fallacy lets unrecoverable past investment drive a present choice",
   "the sunk-cost fallacy misjudges the probability of a future event; the gambler's fallacy lets unrecoverable past investment drive a present choice",
   "both concern probability, but only one applies to money",
   "both concern past investment, but only one applies to gambling"], ans=0,
   why="EK 2.2.A.6 lists the two together as obstacles to good decisions, but one is an error about probability and the other an error about which costs are relevant; the first distractor is that pairing reversed."),
 dict(q="A mental set is best described as", choices=[
   "the tendency to approach a new problem the way a previous problem was successfully solved",
   "the inability to see an object as serving any purpose other than its usual one",
   "a readiness to perceive an ambiguous image in a particular way",
   "the tendency to overestimate an event because vivid examples come to mind"], ans=0,
   why="EK 2.2.A.5 states that decision making can be influenced by prior experiences that were successful, which is what a mental set names; the other options are functional fixedness, a perceptual set from Topic 2.1, and the availability heuristic."),
 dict(q="A person needs to hang a picture and has a wrench but no hammer, and never considers using the wrench to drive the nail. This illustrates", choices=[
   "functional fixedness",
   "a mental set",
   "the representativeness heuristic",
   "convergent thinking"], ans=0,
   why="EK 2.2.A.8 names functional fixedness as an obstacle to creative thinking; it is the failure to see an object as usable for anything but its customary function."),
 dict(q="Which statement correctly distinguishes a mental set from functional fixedness?", choices=[
   "a mental set is fixation on a familiar strategy; functional fixedness is fixation on an object's usual function",
   "functional fixedness is fixation on a familiar strategy; a mental set is fixation on an object's usual function",
   "a mental set aids problem solving while functional fixedness never does",
   "both concern objects, but only one concerns tools"], ans=0,
   why="EK 2.2.A.5 attaches mental set to strategies that previously succeeded and EK 2.2.A.8 attaches functional fixedness to an object's customary use; the two are fixations on different things, and the first distractor swaps them."),
 dict(q="Participants who have just read a list of words about the elderly walk more slowly down the hallway afterward. This effect is best described as", choices=[
   "priming",
   "framing",
   "the gambler's fallacy",
   "an algorithm"], ans=0,
   why="EK 2.2.A.5 lists priming among the circumstances surrounding a decision that influence it; exposure to one stimulus shapes a later response without the person intending it."),
 dict(q="Ground beef labeled \"80 percent lean\" is rated as better than the same product labeled \"20 percent fat.\" This effect is best described as", choices=[
   "framing",
   "priming",
   "the availability heuristic",
   "assimilation"], ans=0,
   why="EK 2.2.A.5 lists framing among the circumstances surrounding a decision; the identical information is evaluated differently depending on how it is presented."),
 dict(q="Which statement correctly distinguishes priming from framing?", choices=[
   "priming is the influence of a prior exposure on a later response; framing is the influence of how the same information is worded",
   "framing is the influence of a prior exposure on a later response; priming is the influence of how the same information is worded",
   "priming applies to decisions and framing applies to perception",
   "both refer to the wording of a question, but only one is deliberate"], ans=0,
   why="EK 2.2.A.5 lists both among the circumstances surrounding a decision, but they operate differently -- one through earlier exposure, one through presentation of the same facts -- and the first distractor reverses them."),
 dict(q="Executive functions are best described as the cognitive processes that allow a person to", choices=[
   "generate, organize, plan, and carry out goal-directed behavior",
   "recognize a familiar face at a glance",
   "detect a faint stimulus at the absolute threshold",
   "store information for a lifetime without rehearsal"], ans=0,
   why="EK 2.2.A.7 states that executive functions are cognitive processes that allow individuals to generate, organize, plan, and carry out goal-directed behaviors and experience critical thinking."),
 dict(q="Divergent thinking is best described as", choices=[
   "generating many different possible ideas or solutions",
   "narrowing many possibilities down to the single best answer",
   "applying a rule that guarantees a correct result",
   "recalling the most vivid example of a category"], ans=0,
   why="EK 2.2.A.8 contrasts divergent thinking with convergent thinking as part of creativity, which it defines as generating novel ideas."),
 dict(q="A student asked to list every possible use for a paper clip is engaging in", choices=[
   "divergent thinking",
   "convergent thinking",
   "an algorithmic search",
   "assimilation"], ans=0,
   why="EK 2.2.A.8 makes divergent thinking the generation of many possibilities, which an open-ended uses task requires; convergent thinking would narrow toward one answer instead."),
 dict(q="A multiple-choice question with one defensible answer calls mainly for", choices=[
   "convergent thinking",
   "divergent thinking",
   "functional fixedness",
   "priming"], ans=0,
   why="EK 2.2.A.8 pairs convergent thinking against divergent thinking; converging on the single best answer is what a single-answer question demands."),
 dict(q="Creativity, in the AP Psychology framework, is defined as a way of thinking that includes", choices=[
   "generating novel ideas and engaging in divergent thinking",
   "reaching the one correct answer as efficiently as possible",
   "applying a well-learned procedure to a familiar problem",
   "recalling stored information without error"], ans=0,
   why="EK 2.2.A.8 states that creativity is a way of thinking that includes generating novel ideas and engaging in divergent versus convergent thinking."),
 dict(q="A chess player who has won many games with one opening keeps using it against an opponent it does not work against. The obstacle here is best described as", choices=[
   "a mental set carried over from prior successes",
   "functional fixedness about the chess pieces",
   "the sunk-cost fallacy about time already spent",
   "the availability of vivid examples of past games"], ans=0,
   why="EK 2.2.A.5 attaches mental set to prior experiences that were successful, and a repeatedly successful opening is exactly such an experience; no object's function and no unrecoverable cost is at issue."),
 dict(q="A researcher wants to test whether framing affects choices. She gives one randomly assigned group a medical option described as having a 90 percent survival rate and the other the same option described as having a 10 percent mortality rate, then records how many in each group choose it. The dependent variable is", choices=[
   "the number of participants in each group who choose the option",
   "the wording used to describe the option",
   "the random assignment procedure",
   "the participants' prior knowledge of medicine"], ans=0,
   why="Science practice 2.B: the dependent variable is the measured outcome, which here is the choice rate; the wording is the manipulated independent variable."),
 dict(q="In the study described above, random assignment matters because it", choices=[
   "makes the two groups comparable so a difference can be attributed to the wording",
   "guarantees that the sample represents the general population",
   "removes the need to define the outcome measure",
   "converts a correlational study into a naturalistic observation"], ans=0,
   why="Random assignment equalizes the groups on everything except the manipulation, which is what licenses a causal conclusion; representing the population is the job of random sampling instead."),
 dict(q="A news outlet reports that people who use a particular puzzle app score higher on tests of planning and organization. Before concluding that the app improves executive functions, a careful reader should note that", choices=[
   "people who already plan well may be the ones who choose to use the app",
   "executive functions cannot be measured at all",
   "the report describes an experiment with a control group",
   "planning and organization are unrelated to executive functions"], ans=0,
   why="Users selected themselves into the app-using group, so the design is correlational and the direction of influence may run the other way; EK 2.2.A.7 does place planning and organization within executive functions, which is what makes the causal reading tempting."),
]
