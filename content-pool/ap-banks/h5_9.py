# AP CHEMISTRY 5.9 Pre-Equilibrium Approximation
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.9.A: identify the rate law for a reaction from a
# mechanism in which the first step is not rate limiting. Suggested skill 5.B,
# identify an appropriate theory, definition, or mathematical relationship to
# solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   5.9.A.1  If the first elementary reaction is not rate limiting,
#            approximations (such as pre-equilibrium) must be made to determine
#            a rate law expression.
#
# ONE ESSENTIAL KNOWLEDGE STATEMENT, AND IT IS THE COMPLEMENT OF 5.8.A.1.
# Topic 5.8 licenses reading the rate law straight off the slowest step, but
# only for mechanisms in which each step is irreversible or the FIRST step is
# rate limiting. This topic is what is left: a first step that is fast and
# reversible, whose product is an intermediate, so that the slow step's rate
# expression contains a concentration no experimenter sets. Every mechanism in
# this module has that shape, and the verifier asserts it -- the first step is
# never the slow one, and the slow step always consumes an intermediate.
#
# THE ALGEBRA IS EXACT, SO THE VERIFIER REDOES IT. Writing the fast first step
# as an equilibrium gives the intermediate's concentration in terms of the
# species the experimenter does control, and substituting it into the slow
# step's rate expression produces the powers. That substitution is arithmetic on
# exponents, and verify_h5_9.py performs it from the tabulated steps alone. A
# key with the wrong power fails there rather than reaching a student.
#
# WHAT IS NOT HERE. Reading a rate law off a rate-limiting FIRST step is 5.8,
# and h5_8.py owns those mechanisms; identifying intermediates and catalysts is
# 5.7. Nothing here computes an equilibrium constant, which is unit 7's
# material -- the equilibrium of the fast step is used only to say that the
# intermediate's concentration follows the reactants of that step.
#
# NOTATION. Chemistry is not typeset, so every rate law is a hand-written
# \( ... \) span. Each rate-law choice ends with the overall order it implies,
# written in words, so that no choice is a truncation of another and no slash
# fraction is left outside a span.
TOPIC = ("5.9", "Pre-Equilibrium Approximation", 5)

_FASTEQ = "fast, and reaches equilibrium in both directions"

_M_NO_O2 = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "2 NO gives N2O2", _FASTEQ],
          ["Step 2", "N2O2 + O2 gives 2 NO2", "slow"]])

_M_NOBR = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "NO + Br2 gives NOBr2", _FASTEQ],
          ["Step 2", "NOBr2 + NO gives 2 NOBr", "slow"]])

_M_HI = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "I2 gives 2 I", _FASTEQ],
          ["Step 2", "H2 + 2 I gives 2 HI", "slow"]])

_M_OZONE = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "O3 gives O2 + O", _FASTEQ],
          ["Step 2", "O + O3 gives 2 O2", "slow"]])

_M_CHLORO = dict(
    headers=["Step", "Elementary reaction", "Relative rate"],
    rows=[["Step 1", "Cl2 gives 2 Cl", _FASTEQ],
          ["Step 2", "Cl + CHCl3 gives HCl + CCl3", "slow"],
          ["Step 3", "CCl3 + Cl gives CCl4", "fast"]])

QUESTIONS = [

 dict(q="What does the framework say must be done if the first elementary "
        "reaction of a mechanism is not rate limiting?",
      choices=[
        "Approximations such as pre-equilibrium must be made to determine a rate "
        "law expression",
        "The rate law is read directly off the molecularity of the first step",
        "The rate law is taken from the coefficients of the overall equation",
        "The mechanism must be rejected as impossible",
        "The slowest step must be rewritten until it comes first"],
      ans=0,
      why="EK 5.9.A.1, near verbatim: if the first elementary reaction is not "
          "rate limiting, approximations such as pre-equilibrium must be made to "
          "determine a rate law expression."),

 dict(q="Which condition sends a mechanism to this topic rather than to the "
        "direct reading of the slowest step?",
      choices=[
        "A first step that is fast and reversible, so that it is not the rate-"
        "limiting step",
        "A mechanism with more than two elementary steps",
        "A mechanism that forms no intermediate at any stage",
        "A mechanism in which every step is irreversible",
        "A mechanism whose overall equation has fractional coefficients"],
      ans=0,
      why="EK 5.8.A.1 licenses the direct reading for mechanisms in which each "
          "step is irreversible or the first step is rate limiting, and EK "
          "5.9.A.1 takes over exactly when the first elementary reaction is not "
          "rate limiting."),

 dict(q="If the first step of a mechanism IS the rate-limiting one, what does "
        "the framework allow instead?",
      choices=[
        "The rate law is set by the molecularity of that slowest step",
        "The rate law still requires a pre-equilibrium approximation",
        "The rate law is set by the molecularity of the fastest step",
        "The rate law must be measured, since no step can be identified",
        "The rate law is the product of the molecularities of all the steps"],
      ans=0,
      why="EK 5.8.A.1 states that for mechanisms in which the first step is rate "
          "limiting the rate law is set by the molecularity of the slowest "
          "elementary step, which is why EK 5.9.A.1 is written for the other "
          "case."),

 dict(q="The table gives a mechanism whose first step is fast and reversible. "
        "What rate law does the pre-equilibrium approximation give?",
      table=_M_NO_O2,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{O_2}] \), overall order "
        "three",
        r"\( \mathrm{rate} = k[\mathrm{N_2O_2}][\mathrm{O_2}] \), overall order "
        "two",
        r"\( \mathrm{rate} = k[\mathrm{NO}][\mathrm{O_2}] \), overall order two",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2} \), overall order two",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{O_2}]^{2} \), overall "
        "order four"],
      ans=0,
      why="EK 5.9.A.1 requires an approximation because the slow step's rate "
          "expression contains an intermediate. Treating the fast first step as "
          "an equilibrium makes that intermediate's concentration follow the "
          "square of the reactant's, which substitution then carries into the "
          "rate law."),

 dict(q="For that same tabulated mechanism, what happens to the rate when the "
        "concentration of nitrogen monoxide is doubled at constant oxygen "
        "concentration?",
      table=_M_NO_O2,
      choices=[
        "It becomes four times as large",
        "It becomes twice as large",
        "It is unchanged",
        "It becomes eight times as large",
        "It becomes half as large"],
      ans=0,
      why="EK 5.9.A.1's approximation gives a rate law second order in that "
          "reactant, because two of its particles are needed to form the "
          "intermediate, and EK 5.2.A.2 makes the rate proportional to the "
          "concentration raised to its power."),

 dict(q="Why does the intermediate formed in the first step not appear in the "
        "final rate law of that mechanism?",
      table=_M_NO_O2,
      choices=[
        "Because the equilibrium of the fast step lets its concentration be "
        "replaced by the concentrations of species the experimenter controls",
        "Because an intermediate has no concentration while a reaction runs",
        "Because the intermediate is a product rather than a reactant of the "
        "slow step",
        "Because intermediates are always present in negligible amounts",
        "Because the rate law may contain at most two concentration factors"],
      ans=0,
      why="EK 5.9.A.1 calls for an approximation such as pre-equilibrium "
          "precisely so that a rate law expression can be determined, and EK "
          "5.7.A.3 makes the intermediate a species present only while the "
          "reaction is occurring."),

 dict(q="The table gives a mechanism for the reaction of nitrogen monoxide with "
        "bromine. What rate law follows from the pre-equilibrium approximation?",
      table=_M_NOBR,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2}[\mathrm{Br_2}] \), overall order "
        "three",
        r"\( \mathrm{rate} = k[\mathrm{NOBr_2}][\mathrm{NO}] \), overall order "
        "two",
        r"\( \mathrm{rate} = k[\mathrm{NO}][\mathrm{Br_2}] \), overall order two",
        r"\( \mathrm{rate} = k[\mathrm{NO}]^{2} \), overall order two",
        r"\( \mathrm{rate} = k[\mathrm{NO}][\mathrm{Br_2}]^{2} \), overall order "
        "three"],
      ans=0,
      why="EK 5.9.A.1's approximation replaces the intermediate's concentration "
          "with the product of the concentrations that form it in the fast "
          "step, so the second molecule of the reactant entering at the slow "
          "step raises that reactant to the second power."),

 dict(q="For that bromine mechanism, what happens to the rate when the bromine "
        "concentration is doubled at constant nitrogen monoxide concentration?",
      table=_M_NOBR,
      choices=[
        "It becomes twice as large",
        "It becomes four times as large",
        "It is unchanged",
        "It becomes eight times as large",
        "It becomes half as large"],
      ans=0,
      why="EK 5.9.A.1's approximation leaves the derived rate law first order in "
          "bromine, since one bromine molecule enters the fast step, and EK "
          "5.2.A.2 makes the rate proportional to that concentration."),

 dict(q="The table gives a mechanism for the formation of hydrogen iodide. What "
        "rate law follows from the pre-equilibrium approximation?",
      table=_M_HI,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{I_2}][\mathrm{H_2}] \), overall order two",
        r"\( \mathrm{rate} = k[\mathrm{H_2}][\mathrm{I}]^{2} \), overall order "
        "three",
        r"\( \mathrm{rate} = k[\mathrm{I_2}]^{2}[\mathrm{H_2}] \), overall order "
        "three",
        r"\( \mathrm{rate} = k[\mathrm{I_2}] \), overall order one",
        r"\( \mathrm{rate} = k[\mathrm{H_2}] \), overall order one"],
      ans=0,
      why="EK 5.9.A.1's approximation replaces the square of the iodine atom "
          "concentration, which the fast step ties to a single molecule of "
          "iodine, so the two powers of the atom collapse into one power of the "
          "molecule."),

 dict(q="A mechanism with a fast equilibrium first step turns out to predict "
        "exactly the rate law that a single two-particle elementary step would "
        "predict. What does that show?",
      choices=[
        "A multistep mechanism can predict the same rate law that a single "
        "elementary step would, so the law alone does not settle the mechanism",
        "A multistep mechanism always predicts a higher overall order than a "
        "single step would",
        "A multistep mechanism can never predict a second order rate law",
        "The rate law of a multistep mechanism always contains an intermediate",
        "A pre-equilibrium approximation always raises the overall order by one"],
      ans=0,
      why="EK 5.9.A.1's approximation produced a law identical to the one EK "
          "5.4.A.1 would give a single two-particle step, and EK 5.7.A.4 makes "
          "detection of an intermediate the further evidence that distinguishes "
          "such proposals."),

 dict(q="The table gives a mechanism for the decomposition of ozone in which the "
        "first step is a fast equilibrium. What rate law follows?",
      table=_M_OZONE,
      choices=[
        r"\( \mathrm{rate} = \frac{k[\mathrm{O_3}]^{2}}{[\mathrm{O_2}]} \), "
        "overall order one",
        r"\( \mathrm{rate} = k[\mathrm{O_3}]^{2}[\mathrm{O_2}] \), overall order "
        "three",
        r"\( \mathrm{rate} = k[\mathrm{O_3}][\mathrm{O}] \), overall order two",
        r"\( \mathrm{rate} = k[\mathrm{O_3}] \), overall order one",
        r"\( \mathrm{rate} = k[\mathrm{O_3}]^{2} \), overall order two"],
      ans=0,
      why="EK 5.9.A.1's approximation replaces the oxygen atom's concentration "
          "using the fast equilibrium, in which the atom appears alongside a "
          "molecule of dioxygen; that molecule therefore enters the derived law "
          "as a divisor."),

 dict(q="In that ozone mechanism, what is predicted to happen to the rate when "
        "dioxygen is added to the mixture at constant ozone concentration?",
      table=_M_OZONE,
      choices=[
        "The rate falls, because dioxygen appears as a divisor in the derived "
        "rate law",
        "The rate rises, because dioxygen appears as a factor in the derived "
        "rate law",
        "The rate is unchanged, because dioxygen is a product",
        "The rate falls to zero, because the first step stops",
        "The rate rises, because more collisions occur"],
      ans=0,
      why="EK 5.9.A.1's approximation puts the concentration of the species "
          "formed alongside the intermediate into the denominator of the derived "
          "law, and EK 5.2.A.2 makes the rate follow the law as written."),

 dict(q="The table gives a three-step mechanism for the chlorination of "
        "chloroform, with a fast reversible first step. What rate law follows?",
      table=_M_CHLORO,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{Cl_2}]^{1/2}[\mathrm{CHCl_3}] \), overall "
        "order three halves",
        r"\( \mathrm{rate} = k[\mathrm{Cl_2}][\mathrm{CHCl_3}] \), overall order "
        "two",
        r"\( \mathrm{rate} = k[\mathrm{Cl}][\mathrm{CHCl_3}] \), overall order "
        "two",
        r"\( \mathrm{rate} = k[\mathrm{Cl_2}]^{2}[\mathrm{CHCl_3}] \), overall "
        "order three",
        r"\( \mathrm{rate} = k[\mathrm{CHCl_3}] \), overall order one"],
      ans=0,
      why="EK 5.9.A.1's approximation ties the chlorine atom's concentration to "
          "the equilibrium in which one molecule gives two atoms, so replacing "
          "one atom brings in the square root of the molecule's concentration."),

 dict(q="What does a power of one half in a derived rate law indicate about the "
        "fast first step?",
      choices=[
        "That the intermediate is formed by splitting one particle into two, so "
        "replacing one of them brings in a square root",
        "That the rate law was measured rather than derived",
        "That two particles of the reactant must collide in the slow step",
        "That the reaction is half complete when the rate is measured",
        "That the mechanism is impossible and must be rejected"],
      ans=0,
      why="EK 5.9.A.1's approximation writes the intermediate's concentration "
          "from the equilibrium of the first step, and an equilibrium producing "
          "two particles from one leaves the intermediate proportional to the "
          "square root of that reactant's concentration."),

 dict(q="Why is a rate law containing the concentration of an intermediate "
        "unsatisfactory as the rate law of the overall reaction?",
      choices=[
        "Because the intermediate is present only while the reaction runs, so "
        "its concentration is not a quantity the experimenter fixes",
        "Because an intermediate never takes part in a collision",
        "Because such a rate law would have too many terms",
        "Because an intermediate has no concentration at any time",
        "Because a rate law may only contain products"],
      ans=0,
      why="EK 5.7.A.3 makes an intermediate present only while a reaction is "
          "occurring, which is why EK 5.9.A.1 requires an approximation to "
          "determine a rate law expression in terms of measurable "
          "concentrations."),

 dict(q="Under the pre-equilibrium approximation, what does the concentration of "
        "the intermediate depend on?",
      choices=[
        "The concentrations of the species on both sides of the fast first step",
        "The concentration of the catalyst alone",
        "The temperature alone",
        "The concentrations of the products of the overall reaction alone",
        "Nothing, since it is treated as constant"],
      ans=0,
      why="EK 5.9.A.1 names pre-equilibrium as the approximation, and treating "
          "the first step as an equilibrium relates the intermediate's "
          "concentration to those of the species it stands between in that step."),

 dict(q="A mechanism has a fast reversible first step and a slow second step. "
        "Which step is rate limiting?",
      choices=[
        "The second, because it is the slower of the two",
        "The first, because it comes first in the sequence",
        "Both equally, because the sequence cannot run without either",
        "Neither, because a reversible step has no rate",
        "It cannot be determined without the rate constants"],
      ans=0,
      why="EK 5.8.A.1 identifies the rate-limiting step as the slowest "
          "elementary step, and EK 5.9.A.1 is written for the case in which that "
          "step is not the first."),

 dict(q="Before any substitution is made, what does the rate expression of the "
        "slow step contain?",
      choices=[
        "The concentrations of the particles that collide in that step, "
        "including the intermediate",
        "The concentrations of the overall reaction's reactants only",
        "The concentration of the catalyst only",
        "No concentrations at all, only the rate constant",
        "The concentrations of the products of the slow step"],
      ans=0,
      why="EK 5.4.A.1 infers an elementary step's rate law from the "
          "stoichiometry of the particles participating in its collision, and "
          "for these mechanisms one of those particles is the intermediate, "
          "which is why EK 5.9.A.1's approximation is needed."),

 dict(q="Two mechanisms are proposed for one overall reaction: in the first the "
        "opening step is slow, and in the second it is a fast equilibrium "
        "followed by a slow step. What does the framework say about their rate "
        "laws?",
      choices=[
        "The first is read off its slow step directly, while the second needs an "
        "approximation, and the two laws will generally differ",
        "Both are read off their slow steps directly",
        "Both require the pre-equilibrium approximation",
        "The two must give the same rate law, since the overall reaction is the "
        "same",
        "Neither mechanism predicts a rate law at all"],
      ans=0,
      why="EK 5.8.A.1 covers the first case and EK 5.9.A.1 the second, and the "
          "substitution the second requires generally introduces powers the slow "
          "step alone does not carry."),

 dict(q="How can a derived rate law come out with a power HIGHER than the number "
        "of particles colliding in the slow step?",
      choices=[
        "Because the intermediate consumed in the slow step is itself made from "
        "several particles in the fast step",
        "Because the fast step is counted twice in the derivation",
        "Because a rate constant may be raised to a power",
        "Because the products of the slow step are added to the law",
        "It cannot; a derived law never exceeds the slow step's molecularity"],
      ans=0,
      why="EK 5.9.A.1's approximation replaces the intermediate's concentration "
          "with the concentrations that form it, and EK 5.4.A.1 makes those "
          "counts the powers, so an intermediate built from two particles brings "
          "two powers in with it."),

 dict(q="In the ozone mechanism whose first step is a fast equilibrium, what "
        "happens to the rate when the ozone concentration is doubled at constant "
        "dioxygen concentration?",
      table=_M_OZONE,
      choices=[
        "It becomes four times as large",
        "It becomes twice as large",
        "It is unchanged",
        "It becomes eight times as large",
        "It becomes half as large"],
      ans=0,
      why="EK 5.9.A.1's approximation gives a derived law with ozone raised to "
          "the second power, one from the slow step and one from the "
          "substitution, and EK 5.2.A.2 makes the rate proportional to that "
          "square."),

 dict(q="Why does the framework call pre-equilibrium an approximation rather "
        "than an exact treatment?",
      choices=[
        "Because it assumes the fast step stays at equilibrium while the slow "
        "step steadily removes the intermediate",
        "Because the concentrations used in it are never measured accurately",
        "Because the rate constants involved are only estimates",
        "Because it applies only at a single temperature",
        "Because the framework regards every rate law as approximate"],
      ans=0,
      why="EK 5.9.A.1 says approximations SUCH AS pre-equilibrium must be made "
          "to determine a rate law expression, so the equilibrium treatment of a "
          "step that is being drained by the next one is the assumption the "
          "framework flags."),

 dict(q="A rate law derived by a pre-equilibrium approximation disagrees with "
        "the measured rate law. What follows?",
      choices=[
        "The proposed mechanism is not consistent with the measurement and must "
        "be revised or rejected",
        "The approximation must be applied a second time",
        "The measured rate law must be discarded in favor of the derived one",
        "The overall balanced equation must be wrong",
        "Nothing follows, since a derived rate law is only a guide"],
      ans=0,
      why="EK 5.2.A.1 and EK 5.2.A.5 make the measured rate law the authority, "
          "and EK 5.9.A.1 makes the approximation a way of predicting one, so a "
          "disagreement counts against the proposal."),

 dict(q="In a mechanism whose first step is a fast equilibrium, which "
        "concentrations replace the intermediate's in the derived rate law?",
      choices=[
        "Those of the species that appear with it in that first step",
        "Those of the products of the overall reaction",
        "Those of every species named anywhere in the mechanism",
        "Those of the species in the last step of the mechanism",
        "Those of the catalyst only"],
      ans=0,
      why="EK 5.9.A.1's pre-equilibrium approximation relates the intermediate's "
          "concentration to the other species in the equilibrium it takes part "
          "in, which are the species of the first step."),

 dict(q="A derived rate law has a reactant's concentration in the denominator. "
        "What does that predict about the reaction?",
      choices=[
        "Adding that substance slows the reaction down",
        "Adding that substance speeds the reaction up",
        "Adding that substance has no effect on the rate",
        "The reaction stops as soon as that substance is present",
        "The rate law must have been derived incorrectly"],
      ans=0,
      why="EK 5.9.A.1's approximation puts a species formed alongside the "
          "intermediate into the denominator, and EK 5.2.A.2's proportionality "
          "then makes a larger concentration of it correspond to a smaller rate."),

 dict(q="How is the overall order of a rate law derived by this approximation "
        "found?",
      choices=[
        "By adding the powers of every concentration in the law, counting a "
        "denominator power as negative",
        "By counting the number of steps in the mechanism",
        "By taking the largest single power that appears",
        "By counting the particles colliding in the fast step only",
        "By adding the coefficients of the overall balanced equation"],
      ans=0,
      why="EK 5.2.A.3 makes the overall order the sum of the powers in the rate "
          "law, and EK 5.9.A.1's approximation is what supplies those powers "
          "when the first step is not rate limiting."),

 dict(q="What becomes of the equilibrium constant of the fast first step when "
        "the substitution is carried out?",
      choices=[
        "It is absorbed into the single rate constant written in front of the "
        "derived law",
        "It appears in the derived law as a separate concentration factor",
        "It cancels and has no effect on the derived law's form",
        "It becomes the overall order of the derived law",
        "It replaces the rate constant of the slow step entirely"],
      ans=0,
      why="EK 5.9.A.1's approximation multiplies the slow step's rate constant "
          "by the equilibrium expression, and the product of two constants is "
          "one constant, which is what the derived law's coefficient stands for."),

 dict(q="A mechanism has a fast equilibrium first step, a slow second step, and "
        "a fast third step. Which step's rate expression is the starting point "
        "of the derivation?",
      choices=[
        "The second, because it is the slowest and therefore rate limiting",
        "The first, because it comes first in the sequence",
        "The third, because it completes the reaction",
        "All three, added together",
        "Whichever step contains the intermediate as a product"],
      ans=0,
      why="EK 5.8.A.1 makes the slowest step the rate-limiting one, and EK "
          "5.9.A.1's approximation is applied to the intermediate appearing in "
          "that step's rate expression rather than to any other step."),

 dict(q="A reaction is found to obey a rate law that is second order in A and "
        "first order in B. Which proposed mechanism could give that law by a "
        "pre-equilibrium argument?",
      choices=[
        "A fast equilibrium in which two particles of A form an intermediate, "
        "followed by a slow step in which that intermediate meets one B",
        "A slow first step in which one A meets one B, followed by a fast step "
        "consuming a second A",
        "A fast equilibrium forming an intermediate from one A, followed by a "
        "slow step in which the intermediate meets one B",
        "A single elementary step in which one A meets one B",
        "A slow first step in which one particle of A falls apart"],
      ans=0,
      why="EK 5.9.A.1's approximation replaces the intermediate's concentration "
          "with the concentrations that form it, so an intermediate built from "
          "two particles of A carries two powers of A into a slow step that "
          "already contributes one power of B."),

 dict(q="Why does the framework write approximations SUCH AS pre-equilibrium "
        "rather than naming pre-equilibrium alone?",
      choices=[
        "Because pre-equilibrium is offered as one example of the "
        "approximations that may be required",
        "Because pre-equilibrium applies only to reactions in the gas phase",
        "Because pre-equilibrium is the only approximation that ever works",
        "Because the framework has not decided which approximation is correct",
        "Because approximations are never actually needed in practice"],
      ans=0,
      why="EK 5.9.A.1's own wording is that approximations (such as "
          "pre-equilibrium) must be made to determine a rate law expression, "
          "which presents the method as an instance rather than as the whole "
          "class."),
]
