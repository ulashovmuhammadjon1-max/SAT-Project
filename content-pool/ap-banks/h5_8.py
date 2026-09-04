# AP CHEMISTRY 5.8 Reaction Mechanism and Rate Law
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.8.A: identify the rate law for a reaction from a
# mechanism in which the first step is rate limiting. Suggested skill 5.B,
# identify an appropriate theory, definition, or mathematical relationship to
# solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   5.8.A.1  For reaction mechanisms in which each elementary step is
#            irreversible, or in which the first step is rate limiting, the rate
#            law of the reaction is set by the molecularity of the slowest
#            elementary step (i.e., the rate-limiting step).
#            Exclusion statement: collection of data pertaining to detection of
#            a reaction intermediate will not be assessed on the AP Exam.
#
# THE CONDITION IS PART OF THE CLAIM, AND THIS MODULE KEEPS IT THERE. 5.8.A.1
# does not say the slowest step always sets the rate law; it says so FOR
# MECHANISMS IN WHICH EACH ELEMENTARY STEP IS IRREVERSIBLE, OR IN WHICH THE
# FIRST STEP IS RATE LIMITING. Every mechanism in this module labels its FIRST
# step slow, and the verifier asserts that -- because a slow step that is not
# the first is 5.9's pre-equilibrium case and its rate law is not read off in
# this way. Two items ask about the condition itself rather than about a rate
# law, which is where the distinction is taught.
#
# WHERE THE POWERS COME FROM. 5.8.A.1 says the rate law is set by the
# MOLECULARITY of the slowest step, and EK 5.4.A.1 makes the rate law of an
# elementary reaction follow from the stoichiometry of the particles colliding.
# So the powers are counted off the reactant side of the slow step, which is
# arithmetic the verifier redoes for every mechanism here.
#
# WHAT IS NOT HERE. Identifying intermediates and catalysts is 5.7, and h5_7.py
# owns those mechanisms; the ones here carry a rate column that h5_7's do not.
# Measuring a rate law from concentration data is 5.2. Energy profiles for
# several steps are 5.10.
#
# NOTATION. Chemistry is not typeset, so every rate law is a hand-written
# \( ... \) span, and each rate-law choice states the overall order it implies
# so that no choice is a truncation of another.
TOPIC = ("5.8", "Reaction Mechanism and Rate Law", 5)

_M_NO2CO = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "NO2 + NO2 gives NO3 + NO", "slow"],
          ["Step 2", "NO3 + CO gives NO2 + CO2", "fast"]])

_M_NO2F2 = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "NO2 + F2 gives NO2F + F", "slow"],
          ["Step 2", "F + NO2 gives NO2F", "fast"]])

_M_IODIDE = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "H2O2 + I- gives H2O + IO-", "slow"],
          ["Step 2", "H2O2 + IO- gives H2O + O2 + I-", "fast"]])

_M_OZONE = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "O3 gives O2 + O", "slow"],
          ["Step 2", "O + O3 gives 2 O2", "fast"]])

_M_NOBR = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "NO + Br2 gives NOBr2", "slow"],
          ["Step 2", "NOBr2 + NO gives 2 NOBr", "fast"]])

_M_CHLORO = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "Cl2 gives 2 Cl", "slow"],
          ["Step 2", "Cl + CHCl3 gives HCl + CCl3", "fast"],
          ["Step 3", "CCl3 + Cl gives CCl4", "fast"]])

_M_NO_O2 = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "2 NO gives N2O2", "slow"],
          ["Step 2", "N2O2 + O2 gives 2 NO2", "fast"]])

QUESTIONS = [

 dict(q="According to the framework, what sets the rate law of a reaction whose "
        "first elementary step is rate limiting?",
      choices=[
        "The molecularity of the slowest elementary step",
        "The coefficients of the overall balanced equation",
        "The molecularity of the fastest elementary step",
        "The total number of elementary steps in the mechanism",
        "The concentration of the intermediate that forms"],
      ans=0,
      why="EK 5.8.A.1, near verbatim: the rate law of the reaction is set by the "
          "molecularity of the slowest elementary step. EK 5.2.A.1 keeps the "
          "overall equation's coefficients out of a rate law."),

 dict(q="Under which conditions does the framework say the slowest step sets the "
        "rate law?",
      choices=[
        "When each elementary step is irreversible, or when the first step is "
        "rate limiting",
        "Under all conditions, without exception",
        "Only when every step has the same molecularity",
        "Only when the mechanism has exactly two steps",
        "Only when no intermediate is formed at any stage"],
      ans=0,
      why="EK 5.8.A.1 states the rule FOR reaction mechanisms in which each "
          "elementary step is irreversible, or in which the first step is rate "
          "limiting. EK 5.9.A.1 covers the case the condition excludes."),

 dict(q="What does the framework call the slowest elementary step of a "
        "mechanism?",
      choices=[
        "The rate-limiting step",
        "The elementary step",
        "The pre-equilibrium step",
        "The transition state",
        "The termination step"],
      ans=0,
      why="EK 5.8.A.1 names it in its own parenthesis: the slowest elementary "
          "step, that is, the rate-limiting step. A transition state is a point "
          "on EK 5.6.A.3's energy profile, not a step."),

 dict(q="The table gives a two-step mechanism with the relative rate of each "
        "step. What is the rate law of the overall reaction?",
      table=_M_NO2CO,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}][\mathrm{CO}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_3}][\mathrm{CO}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{2}[\mathrm{CO}] \), third order "
        "overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "and EK 5.4.A.1 reads that molecularity off the particles colliding in "
          "it. Two molecules of the same reactant must meet in the tabulated "
          "slow step."),

 dict(q="In that same tabulated mechanism, why does carbon monoxide not appear "
        "in the rate law even though it is a reactant of the overall reaction?",
      table=_M_NO2CO,
      choices=[
        "Because it is consumed only in a step that is not rate limiting",
        "Because it is an intermediate rather than a reactant",
        "Because it is present in a much larger amount than the other reactant",
        "Because gases never appear in a rate law",
        "Because it appears on both sides of the overall equation"],
      ans=0,
      why="EK 5.8.A.1 makes the rate law depend on the molecularity of the "
          "slowest step alone, so a species entering only in a faster step "
          "contributes no power; EK 5.2.A.1 leaves the overall equation out of "
          "the matter."),

 dict(q="The table gives a two-step mechanism for the reaction of nitrogen "
        "dioxide with fluorine. What is the rate law?",
      table=_M_NO2F2,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO_2}][\mathrm{F_2}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{2}[\mathrm{F_2}] \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{F_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO_2}]^{2} \), second order overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "and EK 5.4.A.1 makes one particle of each reactant in that step "
          "contribute one power of its own concentration."),

 dict(q="Which statement about the overall balanced equation and the rate law is "
        "correct for a mechanism whose first step is rate limiting?",
      choices=[
        "The rate law follows the slow step, so its powers need not match the "
        "coefficients of the overall equation",
        "The rate law always matches the coefficients of the overall equation",
        "The overall equation is derived from the rate law rather than the "
        "reverse",
        "The rate law and the overall equation carry no information about the "
        "same reaction",
        "The rate law follows whichever step is written last"],
      ans=0,
      why="EK 5.8.A.1 ties the rate law to the slowest step, and EK 5.2.A.1 "
          "makes an overall reaction's powers a matter for measurement rather "
          "than for reading off coefficients, so the two need not agree."),

 dict(q="The table gives a two-step mechanism for the decomposition of hydrogen "
        "peroxide catalyzed by iodide ion. What is the rate law?",
      table=_M_IODIDE,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{H_2O_2}][\mathrm{I^-}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{H_2O_2}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{H_2O_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{I^-}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{H_2O_2}]^{2}[\mathrm{I^-}] \), third "
        "order overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "and EK 5.4.A.1 gives one power to each particle taking part in that "
          "collision, one peroxide molecule and one iodide ion."),

 dict(q="The iodide ion in that mechanism is regenerated by the second step, so "
        "its net amount does not change. Why does it still appear in the rate "
        "law?",
      table=_M_IODIDE,
      choices=[
        "Because it is one of the particles that must collide in the rate-"
        "limiting step",
        "Because every species in a mechanism appears in the rate law",
        "Because a species that is regenerated must always be first order",
        "Because it is an intermediate of the mechanism",
        "Because it appears in the overall balanced equation"],
      ans=0,
      why="EK 5.8.A.1 makes the molecularity of the slowest step the source of "
          "the powers, and EK 5.4.A.1 counts the particles participating in that "
          "collision; EK 5.11.A.2's regeneration concerns the net amount, not "
          "the collision."),

 dict(q="The table gives a two-step mechanism for the decomposition of ozone. "
        "What is the rate law?",
      table=_M_OZONE,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{O_3}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{O_3}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{O_3}][\mathrm{O}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{O_2}][\mathrm{O}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k \), zero order overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "which here is a single ozone molecule falling apart, and EK 5.4.A.1 "
          "gives that one particle one power of its concentration."),

 dict(q="The table gives a two-step mechanism for the reaction of nitrogen "
        "monoxide with bromine. What is the rate law?",
      table=_M_NOBR,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO}][\mathrm{Br_2}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{Br_2}] \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{Br_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{NOBr_2}][\mathrm{NO}] \), second order "
        "overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "and EK 5.4.A.1 gives one power to each of the two different particles "
          "that must collide in it."),

 dict(q="The table gives a three-step mechanism for the chlorination of "
        "chloroform. What is the rate law?",
      table=_M_CHLORO,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{Cl_2}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{Cl_2}][\mathrm{CHCl_3}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{Cl}][\mathrm{CHCl_3}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{Cl_2}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{CHCl_3}] \), first order overall"],
      ans=0,
      why="EK 5.8.A.1 makes the slowest step decisive however many steps follow "
          "it, and EK 5.4.A.1 reads one power off the single particle that falls "
          "apart in that step."),

 dict(q="For that same three-step mechanism, what happens to the rate if the "
        "concentration of chloroform is doubled while everything else is held "
        "constant?",
      table=_M_CHLORO,
      choices=[
        "It is unchanged, because chloroform enters only after the rate-"
        "limiting step",
        "It doubles, because chloroform is a reactant of the overall reaction",
        "It quadruples, because chloroform appears in two of the three steps",
        "It halves, because chloroform competes with chlorine",
        "It cannot be predicted from a mechanism"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step "
          "alone, so a species absent from that step carries no power, and EK "
          "5.2.A.2 makes the rate depend only on the concentrations that appear "
          "in the rate law."),

 dict(q="The table gives a two-step mechanism for the formation of nitrogen "
        "dioxide from nitrogen monoxide and oxygen. What is the rate law?",
      table=_M_NO_O2,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{O_2}] \), third order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}][\mathrm{O_2}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{N_2O_2}][\mathrm{O_2}] \), second order "
        "overall",
        r"\( \mathrm{rate} = k[\mathrm{NO}] \), first order overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "and EK 5.4.A.1 makes two particles of the same species contribute two "
          "powers of its concentration."),

 dict(q="For that same mechanism, what happens to the rate if the concentration "
        "of nitrogen monoxide is doubled while the oxygen concentration is held "
        "constant?",
      table=_M_NO_O2,
      choices=[
        "It becomes four times as large",
        "It becomes twice as large",
        "It is unchanged",
        "It becomes eight times as large",
        "It becomes half as large"],
      ans=0,
      why="EK 5.8.A.1 gives the reaction the rate law of its slow step, which EK "
          "5.4.A.1 makes second order in that reactant, and EK 5.2.A.2 makes the "
          "rate proportional to that concentration squared."),

 dict(q="A mechanism has a slow first step in which one particle of A and one "
        "of B collide, followed by a fast step consuming a particle of C. What "
        "is the overall order of the reaction?",
      choices=[
        "Two, the sum of the powers the slow step contributes",
        "Three, since three different substances take part in the mechanism",
        "One, since only one step controls the rate",
        "Two, since there are two steps in the mechanism",
        "It cannot be found without measuring the rate"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "EK 5.4.A.1 gives one power to each colliding particle in it, and EK "
          "5.2.A.3 makes the overall order the sum of the powers."),

 dict(q="Why does a fast step that follows the rate-limiting step not change the "
        "rate law?",
      choices=[
        "Because the reaction can proceed no faster than its slowest step, which "
        "is where the framework locates the rate law",
        "Because a fast step involves no collisions at all",
        "Because a fast step always consumes an intermediate",
        "Because the rate constant of a fast step is zero",
        "Because only the last step of a mechanism matters"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law of the reaction by the molecularity of "
          "the SLOWEST elementary step, which is the framework's own way of "
          "saying that the steps downstream of it do not limit the rate."),

 dict(q="A measured rate law disagrees with the rate law predicted from a "
        "proposed mechanism whose first step is rate limiting. What follows?",
      choices=[
        "The proposed mechanism is not consistent with the measurement and must "
        "be revised or rejected",
        "The measurement must be repeated until it agrees with the mechanism",
        "The overall balanced equation must be wrong",
        "The mechanism is still acceptable, since a rate law is only a "
        "prediction",
        "The reaction must proceed by a single elementary step instead"],
      ans=0,
      why="EK 5.2.A.1 and EK 5.2.A.5 make the measured rate law the authority, "
          "and EK 5.8.A.1 makes a first-step-limited mechanism predict one, so a "
          "disagreement counts against the proposal."),

 dict(q="Two mechanisms are proposed for the same reaction and both align with "
        "the overall balanced equation, but they predict different rate laws. "
        "How can they be told apart?",
      choices=[
        "By measuring the rate law, since the framework has the slowest step set "
        "it",
        "By counting which mechanism has fewer steps",
        "By checking which mechanism forms an intermediate",
        "By comparing the coefficients in the overall equation",
        "They cannot be told apart by any experiment"],
      ans=0,
      why="EK 5.8.A.1 makes the rate law a consequence of the slowest step, so "
          "two mechanisms with different slow steps predict different rate laws, "
          "and EK 5.2.A.5 makes the rate law measurable."),

 dict(q="In a mechanism whose first step is rate limiting, which species may "
        "appear in the rate law?",
      choices=[
        "Only the species that collide in the first step",
        "Every species that appears anywhere in the mechanism",
        "Only the species written in the overall balanced equation",
        "Only the products of the first step",
        "Only species that are not regenerated later"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "which when the first step is rate limiting means the particles "
          "colliding in it, as EK 5.4.A.1 counts them."),

 dict(q="A mechanism's slow first step is written as a single molecule of X "
        "breaking apart. What is the rate law, and what is the overall order?",
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{X}] \), first order overall",
        r"\( \mathrm{rate} = k[\mathrm{X}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k \), zero order overall",
        r"\( \mathrm{rate} = k[\mathrm{X}]^{1/2} \), half order overall",
        r"\( \mathrm{rate} = k[\mathrm{X}]^{3} \), third order overall"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step "
          "and EK 5.4.A.1 gives a single participating particle a single power "
          "of its own concentration, so EK 5.2.A.3 makes the overall order one."),

 dict(q="Why does the framework attach a condition to its rule about the slowest "
        "step rather than stating the rule outright?",
      choices=[
        "Because a mechanism whose first step is reversible and not rate "
        "limiting needs an approximation instead",
        "Because some reactions have no slowest step",
        "Because the rule fails whenever a catalyst is present",
        "Because the rule applies only to reactions in solution",
        "Because the rule applies only to two-step mechanisms"],
      ans=0,
      why="EK 5.8.A.1 states its rule for mechanisms in which each step is "
          "irreversible or the first step is rate limiting, and EK 5.9.A.1 says "
          "that if the first elementary reaction is not rate limiting, "
          "approximations such as pre-equilibrium must be made instead."),

 dict(q="A two-step mechanism has a slow first step involving two particles of "
        "the same reactant. What happens to the rate when that reactant's "
        "concentration is tripled?",
      choices=[
        "It becomes nine times as large",
        "It becomes three times as large",
        "It becomes six times as large",
        "It is unchanged",
        "It becomes twenty seven times as large"],
      ans=0,
      why="EK 5.8.A.1 gives the reaction the rate law of its slow step, EK "
          "5.4.A.1 makes two colliding particles of one species give a squared "
          "concentration, and EK 5.2.A.2 makes the rate proportional to that."),

 dict(q="What does the word molecularity refer to in the framework's statement "
        "about the rate-limiting step?",
      choices=[
        "How many particles must come together for that single step to occur",
        "How many molecules of product the step forms",
        "How many steps the mechanism contains",
        "How large the molecules taking part in the step are",
        "How many times the step repeats before the reaction is complete"],
      ans=0,
      why="EK 5.8.A.1 sets the rate law by the molecularity of the slowest step, "
          "and EK 5.4.A.1 infers an elementary reaction's rate law from the "
          "stoichiometry of the particles participating in a collision, which is "
          "what that count is."),

 dict(q="A student writes a rate law containing the concentration of a reaction "
        "intermediate. Why is that unacceptable as the rate law of the overall "
        "reaction?",
      choices=[
        "Because an intermediate is present only while the reaction runs, so its "
        "concentration is not a quantity the experimenter sets",
        "Because an intermediate never takes part in any collision",
        "Because a rate law may contain at most two concentration factors",
        "Because an intermediate has no concentration at any time",
        "Because intermediates always appear in the overall balanced equation"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate present only while a reaction is "
          "occurring, and EK 5.2.A.1 writes a rate law in the concentrations of "
          "the reactants, so a mechanism producing such a law needs EK 5.9.A.1's "
          "approximation rather than EK 5.8.A.1's direct reading."),

 dict(q="A proposed mechanism has three elementary steps, the second of which is "
        "the slowest. Why can its rate law not be read off in the way this topic "
        "describes?",
      choices=[
        "Because the framework's rule requires each step to be irreversible or "
        "the FIRST step to be rate limiting",
        "Because a mechanism may never have three steps",
        "Because the second step of any mechanism has no molecularity",
        "Because only the first step of a mechanism affects the rate",
        "Because a slow step in the middle makes the reaction stop"],
      ans=0,
      why="EK 5.8.A.1 attaches exactly that condition, and EK 5.9.A.1 sends the "
          "remaining case to an approximation such as pre-equilibrium."),

 dict(q="For a mechanism in which every elementary step is irreversible, what "
        "does the framework allow?",
      choices=[
        "The rate law is still set by the molecularity of the slowest step, "
        "wherever that step falls",
        "The rate law must be measured, since no step can be identified as "
        "limiting",
        "The rate law is set by the molecularity of the first step, slow or not",
        "The rate law is set by the sum of the molecularities of every step",
        "The rate law cannot be written at all"],
      ans=0,
      why="EK 5.8.A.1 offers two conditions, either of which suffices: each "
          "elementary step is irreversible, OR the first step is rate limiting, "
          "and under either the rate law is set by the molecularity of the "
          "slowest step."),

 dict(q="Two elementary steps are proposed for the slow step of a mechanism, one "
        "in which a single particle of A decomposes and one in which two "
        "particles of A collide. How would a measurement distinguish them?",
      choices=[
        "Doubling the concentration of A would double the rate in the first case "
        "and quadruple it in the second",
        "Doubling the concentration of A would leave the rate unchanged in "
        "either case",
        "Doubling the concentration of A would quadruple the rate in the first "
        "case and double it in the second",
        "The two cannot be distinguished, since both are first order",
        "Only a change in temperature would distinguish them"],
      ans=0,
      why="EK 5.8.A.1 makes each candidate slow step predict its own rate law "
          "through EK 5.4.A.1's particle counts, and EK 5.2.A.2 turns those "
          "different powers into different responses to a doubling."),

 dict(q="What does a rate law tell a chemist about a mechanism whose first step "
        "is rate limiting?",
      choices=[
        "Which particles must collide in the rate-limiting step, and how many of "
        "each",
        "How many elementary steps the mechanism contains",
        "Which step forms the intermediate",
        "How much energy the reaction releases",
        "The order in which the products appear"],
      ans=0,
      why="EK 5.8.A.1 makes the rate law the molecularity of the slow step, and "
          "EK 5.4.A.1 makes that molecularity the count of particles "
          "participating in the collision, so the law reports exactly that "
          "count."),

 dict(q="Why is a mechanism never established by a rate law alone?",
      choices=[
        "Because more than one mechanism can have a slowest step of the same "
        "molecularity, so further evidence such as a detected intermediate is "
        "needed",
        "Because a rate law is not measurable with any accuracy",
        "Because rate laws describe only reactions in the gas phase",
        "Because the framework treats every mechanism as unprovable in "
        "principle",
        "Because a rate law describes the fastest step rather than the slowest"],
      ans=0,
      why="EK 5.8.A.1 fixes the rate law from the slow step's molecularity but "
          "not the converse, and EK 5.7.A.4 makes detection of an intermediate a "
          "common way to build evidence for one mechanism over an alternative."),
]
