# AP HUMAN GEOGRAPHY 2.7 Population Policies -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding SPS-2, "Changes in
# population have long- and short-term effects on a place's economy, culture,
# and politics." Learning objective SPS-2.A, "Explain the intent and effects of
# various population and immigration policies on population size and
# composition."
#
# Essential knowledge -- one statement, and it names three policy types:
#   SPS-2.A.1  Types of population policies include those that promote or
#              discourage population growth, such as pronatalist, antinatalist,
#              and immigration policies.
#
# The learning objective is the part that decides how the items are built: it
# asks for INTENT AND EFFECTS, which are different things and frequently
# diverge. A policy can be well intentioned and ineffective, effective and
# harmful, or produce a composition effect nobody intended. Items 9, 13, 17, 21,
# 24, 26 and 29 all turn on that gap.
#
# The three types, as this module uses them:
#   pronatalist   intended to RAISE births -- cash payments, paid parental
#                 leave, subsidized childcare, tax relief for larger families,
#                 and in some historical cases restrictions on contraception
#                 and abortion
#   antinatalist  intended to LOWER births -- family planning programmes,
#                 contraception access, education campaigns, and in some cases
#                 legal limits on family size with penalties
#   immigration   intended to change population size or composition by
#                 admitting, selecting, restricting, or expelling migrants --
#                 quotas, point systems, guest-worker programmes, family
#                 reunification rules, refugee admissions
#
# Historical cases used here are the standard ones and are named only where the
# fact is not in dispute: China's one-child policy (in force from 1979, relaxed
# to two children in 2016 and three in 2021), Romania's 1966 decree restricting
# contraception and abortion, and India's family planning programme. Where an
# item does not need a named country it does not use one, because an invented
# detail about a real state is exactly the kind of error this bank must not
# ship.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_7.py. FIVE choices (A-E).
TOPIC = ("2.7", "Population Policies", 2)

QUESTIONS = [
 dict(q="A government offers a cash payment at the birth of a second child, eighteen months of paid parental leave, and subsidized childcare. What kind of policy is this?",
   choices=[
     "Pronatalist, since its measures are designed to raise the birth rate",
     "Antinatalist, since it regulates family size",
     "An immigration policy, since it affects population size",
     "Neither, since payments to families are welfare rather than population policy",
     "Antinatalist, since childcare allows women to work"],
   ans=0,
   why="EK SPS-2.A.1 lists pronatalist policies among the types that promote population growth. Every instrument named lowers the cost of having an additional child, which is the mechanism through which a state tries to raise fertility."),

 dict(q="A government funds free contraception, trains community health workers to provide family planning advice, and runs a campaign promoting smaller families. This is",
   choices=[
     "An antinatalist policy, since it is intended to reduce the birth rate",
     "A pronatalist policy, since it improves health services",
     "An immigration policy, since it changes population size",
     "Not a population policy, since it is voluntary",
     "A pronatalist policy, since healthier mothers have more children"],
   ans=0,
   why="EK SPS-2.A.1 names antinatalist policies among the types that discourage population growth. Being voluntary changes the instrument used, not the intent, and the stated intent here is a smaller average family."),

 dict(q="Which of the following is an immigration policy in the framework's sense?",
   choices=[
     "A points system that admits applicants according to age, language, and occupation",
     "A cash bonus paid on the birth of a third child",
     "Free provision of contraception in rural clinics",
     "A campaign encouraging couples to marry later",
     "A tax deduction for each dependent child"],
   ans=0,
   why="EK SPS-2.A.1 lists immigration policies alongside pronatalist and antinatalist ones as a way of changing population size and composition. A points system changes both how many people enter and who they are, which is the composition half of the learning objective."),

 dict(q="China's one-child policy, in force from 1979, is the standard example of which type?",
   choices=[
     "An antinatalist policy enforced by penalties as well as by persuasion",
     "A pronatalist policy",
     "An immigration policy",
     "A policy with no measurable effect on the birth rate",
     "A policy that promoted population growth"],
   ans=0,
   why="EK SPS-2.A.1's antinatalist category covers policies intended to discourage population growth, and a legal limit on family size backed by fines and administrative sanctions is its strongest form. The policy was relaxed to two children in 2016 and three in 2021."),

 dict(q="Beyond lowering the birth rate, what unintended composition effect is the one-child policy most associated with?",
   choices=[
     "A sex ratio skewed toward males, produced by a strong preference for sons interacting with a strict limit on births",
     "A rise in the number of children per family",
     "A fall in the share of the population over 65",
     "An increase in immigration",
     "A rise in the total fertility rate"],
   ans=0,
   why="The learning objective asks for effects on population size AND composition, and this is the clearest case of the two diverging. A binding limit on births turns an existing preference for sons into a measurable imbalance in the sex ratio at birth."),

 dict(q="A country with a total fertility rate of 1.3 introduces generous family benefits and its fertility rises to 1.5 over a decade. What does this outcome illustrate?",
   choices=[
     "Pronatalist policies can raise fertility but usually by modest amounts, because the decision to have a child depends on much more than cost",
     "Pronatalist policies always restore fertility to replacement level",
     "Pronatalist policies have no effect whatsoever",
     "The country's policy was antinatalist",
     "Fertility rose because of immigration"],
   ans=0,
   why="The learning objective asks for intent and effects together, and the honest reading of the evidence is that these policies work in the intended direction and do not close the gap to replacement. Housing, careers, partnership and expectations are inputs no subsidy controls."),

 dict(q="Why do many countries facing population decline turn to immigration policy rather than relying on pronatalist measures alone?",
   choices=[
     "Immigration adds working-age people immediately, while a rise in births takes about two decades to reach the labour force",
     "Immigration is cheaper than any pronatalist measure",
     "Pronatalist policies always fail completely",
     "Immigration policies reduce the birth rate",
     "Immigrants are not counted in the population"],
   ans=0,
   why="EK SPS-2.A.1 groups the three policy types because they are alternative levers on the same problem, and they differ mainly in how quickly they act. A newborn is a dependent for two decades, while an admitted adult worker is in the labour force at once."),

 dict(q="Romania's 1966 decree restricting access to contraception and abortion was followed by a sharp one-year spike in births and then a return toward the previous level. What does this pattern show?",
   choices=[
     "A coercive pronatalist policy can move births sharply in the short run without changing the underlying desire for smaller families",
     "The decree was an antinatalist policy",
     "The decree had no effect at all",
     "Births continued to rise for decades afterward",
     "The policy raised fertility permanently to replacement level"],
   ans=0,
   why="The learning objective asks for intent and effects, and the effect here separates cleanly into a large immediate response and a much smaller lasting one. Removing a means of avoiding birth changes behaviour faster than it changes intentions."),

 dict(q="Which is the strongest reason a state's population policy can produce an effect its authors did not intend?",
   choices=[
     "Households respond to the rule in whatever way best serves their own goals, which may differ from the state's",
     "Population policies are never written down clearly",
     "Population data are always inaccurate",
     "Governments cannot measure birth rates",
     "Unintended effects occur only in immigration policy"],
   ans=0,
   why="A policy sets the terms on which families decide but does not decide for them, so the aggregate outcome is the sum of household responses to a new constraint. That gap between rule and response is where the composition effects the learning objective asks about arise."),

 dict(q="A country admits large numbers of temporary workers on contracts that do not permit families to accompany them. What effect on composition should be expected?",
   choices=[
     "A working-age, male-weighted population with few children, since the policy admits workers rather than households",
     "A population with a very wide pyramid base",
     "A rapid rise in the share of the population over 65",
     "A fall in the sex ratio below 100",
     "No change in composition, only in total size"],
   ans=0,
   why="EK SPS-2.A.1 makes immigration policy one of the instruments acting on population, and the learning objective asks about composition as well as size. A rule admitting workers without dependents selects a narrow slice of the age and sex distribution."),

 dict(q="Which of these is an antinatalist measure that operates through incentives rather than penalties?",
   choices=[
     "Offering priority in housing and schooling to families who have fewer children",
     "Fining families who exceed a legal limit on children",
     "Requiring a permit before a couple may have a child",
     "Restricting the sale of contraception",
     "Paying a bonus for each additional child"],
   ans=0,
   why="EK SPS-2.A.1's antinatalist category covers policies discouraging growth without specifying the instrument. A reward for compliance and a punishment for non-compliance both discourage births, but only the first leaves the household's legal freedom intact."),

 dict(q="A state relaxes a long-standing limit on family size, but fertility barely rises. What is the most likely explanation?",
   choices=[
     "Decades of small families, high urban living costs, and women's employment have changed what couples want, and the rule was no longer the binding constraint",
     "The relaxation was never announced",
     "Fertility cannot rise once it has fallen",
     "The relaxation was actually an antinatalist policy",
     "The country's population was already growing rapidly"],
   ans=0,
   why="The learning objective asks for effects rather than intentions, and a rule only binds while it is what prevents the behaviour. Once the cost of children and the alternatives available to women have moved, removing the legal ceiling changes very little."),

 dict(q="Which pairing of policy type with its likely long-run effect on age structure is correct?",
   choices=[
     "A sustained antinatalist policy leads to an older age structure and a rising share of dependents who are elderly",
     "A sustained antinatalist policy leads to a younger age structure",
     "A sustained pronatalist policy leads to an older age structure",
     "Immigration of young workers leads to an older age structure",
     "Neither type of policy affects age structure"],
   ans=0,
   why="EK SPS-2.A.1's antinatalist policies act on births, and fewer births now means a smaller cohort at every age later. The effect on structure is delayed but arithmetically certain, which is why the learning objective distinguishes short-term from long-term effects."),

 dict(q="A country introduces a family-reunification provision allowing admitted migrants to bring spouses, children, and parents. What is the most likely effect on composition?",
   choices=[
     "The admitted population becomes broader in age and closer to balanced by sex than a worker-only programme would produce",
     "The admitted population becomes overwhelmingly male",
     "The admitted population becomes entirely elderly",
     "Composition is unaffected, since the total is what matters",
     "The admitted population contains no children"],
   ans=0,
   why="EK SPS-2.A.1 treats immigration policy as an instrument acting on population, and the learning objective asks about composition. Admitting households rather than individual workers imports a cross-section of ages and both sexes rather than a single slice."),

 dict(q="A government wishing to slow population growth invests in girls' secondary education rather than in a birth limit. What is the strongest justification?",
   choices=[
     "Extended schooling delays marriage and childbearing and raises the opportunity cost of a large family, so fertility falls without coercion",
     "Education has no relationship to fertility",
     "Education raises fertility, which is the intended goal",
     "Coercive limits are more effective in every case",
     "Schooling changes the death rate rather than the birth rate"],
   ans=0,
   why="EK SPS-2.A.1's antinatalist category is defined by intent rather than by instrument, and schooling acts on the same outcome through the household's own decisions. The mechanism is well documented and it produces a durable change rather than a suppressed one."),

 dict(q="Which statement about the INTENT and the EFFECT of a population policy is most accurate?",
   choices=[
     "They must be evaluated separately, because a policy can be intended to raise births and instead alter only their timing",
     "Intent and effect are always the same",
     "Only intent can be evaluated, since effects are unmeasurable",
     "Only effects matter, since intent is unknowable",
     "A policy's effect is always larger than its intent"],
   ans=0,
   why="The learning objective for this topic asks for the intent AND effects of population policies, which is a deliberate pairing. A bonus paid for a birth before a deadline can move births earlier without adding any over a lifetime, which is intent and effect coming apart entirely."),

 dict(q="A country restricts immigration sharply while its fertility remains at 1.4. What should it expect over the following decades?",
   choices=[
     "Population decline and accelerated aging, since neither of the two sources of growth is operating",
     "Rapid population growth from natural increase",
     "A younger population, since fewer migrants arrive",
     "No change, since immigration policy affects only composition",
     "A rise in the birth rate caused by the restriction"],
   ans=0,
   why="Population changes only through births, deaths and migration, so closing one source while fertility sits well below replacement leaves nothing to offset mortality. EK SPS-2.A.1 puts immigration policy alongside natalist policy precisely because they are alternative levers on the same total."),

 dict(q="Which is the clearest example of a population policy whose effects fell mainly on composition rather than on total size?",
   choices=[
     "A selective admission system that changed the languages, skills, and origins of a country's immigrants without changing how many were admitted",
     "A cash bonus paid for every birth",
     "A national campaign to lower the birth rate",
     "A general increase in the annual immigration quota",
     "A ban on emigration"],
   ans=0,
   why="The learning objective distinguishes effects on size from effects on composition. Holding the number admitted constant while changing the selection criteria alters who the population is made of without altering how many people it contains."),

 dict(q="A pronatalist government provides childcare and protects the jobs of women who take parental leave, rather than simply paying a bonus. What is the reasoning?",
   choices=[
     "The obstacle to a further child is often the career cost of having one, so reducing that cost addresses the actual constraint",
     "Bonuses are illegal in most countries",
     "Childcare lowers the birth rate",
     "Job protection is an antinatalist measure",
     "Parental leave has no effect on fertility decisions"],
   ans=0,
   why="A one-off payment addresses the direct cost of a birth while the larger cost is often years of forgone earnings and advancement. Policies aimed at the binding constraint are the ones that show the larger measured effect, which is what the learning objective's focus on effects asks students to notice."),

 dict(q="Which of the following would count as a population policy under the framework even though it does not mention births?",
   choices=[
     "An annual quota setting how many permanent residents may be admitted",
     "A national curriculum reform",
     "A change in the corporate tax rate",
     "A new highway construction programme",
     "A revision of the electoral map"],
   ans=0,
   why="EK SPS-2.A.1 explicitly names immigration policies as one of the types of population policy. An admission quota changes the size and composition of the resident population directly, which is what makes it a population policy whatever its stated purpose."),

 dict(q="A government's antinatalist campaign succeeds and fertility falls quickly to 1.2. Forty years later the same government adopts pronatalist measures. What does the sequence illustrate?",
   choices=[
     "Population policy can overshoot, and reversing a fertility decline is far harder than causing one",
     "Antinatalist and pronatalist policies are the same thing",
     "Fertility always returns to its previous level",
     "The first policy must have failed",
     "Governments cannot influence fertility in either direction"],
   ans=0,
   why="The learning objective asks about long-term as well as short-term effects, and this pair of policies is the standard demonstration that they are asymmetric. Lowering fertility removes a constraint, while raising it requires persuading households to want something they have stopped wanting."),

 dict(q="Which is a legitimate criticism of coercive antinatalist policies, judged on the framework's own terms of intent and effects?",
   choices=[
     "They can achieve the intended fall in births while producing serious unintended effects on sex ratio, aging, and individual rights",
     "They never lower the birth rate",
     "They always raise the birth rate",
     "They are indistinguishable from immigration policy",
     "They affect only the total population and never its composition"],
   ans=0,
   why="The learning objective requires both intent and effects to be explained, and an honest account here concedes the intended effect while naming the unintended ones. Denying that such policies lower births would be as inaccurate as ignoring what else they do."),

 dict(q="Two neighbouring countries have the same fertility rate, but one is growing and the other is shrinking. Which policy difference best explains this?",
   choices=[
     "One admits substantial numbers of immigrants and the other does not",
     "One has a pronatalist policy and the other does not",
     "One has an antinatalist policy and the other does not",
     "One counts its population more accurately",
     "One has a larger land area"],
   ans=0,
   why="Fertility is held constant by the premise, so the natalist policies cannot be doing the work whatever either country has adopted. EK SPS-2.A.1's third type is the only lever left that can move a total in opposite directions."),

 dict(q="Why is the SHORT-TERM effect of a pronatalist bonus often larger than its long-term effect?",
   choices=[
     "Couples who intended to have a child anyway move the birth forward to qualify, which raises this year's births without raising completed family size",
     "Bonuses are usually cancelled after one year",
     "Bonuses cause a permanent rise in fertility",
     "Short-term and long-term effects are always identical",
     "Bonuses reduce births in the year they are introduced"],
   ans=0,
   why="A timing response and a quantum response look identical in a single year's birth count and are entirely different over a lifetime. Distinguishing them is the clearest case of the intent-and-effects analysis the learning objective calls for."),

 dict(q="A country's population policy explicitly aims to increase the share of residents holding advanced technical qualifications. Which instrument fits that aim most directly?",
   choices=[
     "A skills-selective immigration system",
     "A birth bonus for third children",
     "A campaign encouraging later marriage",
     "Free contraception in rural areas",
     "A ban on emigration by graduates"],
   ans=0,
   why="EK SPS-2.A.1 names immigration policy as an instrument acting on population, and a selection rule acts on composition by construction. Natalist measures change how many people are born and cannot change what qualifications the population holds for at least two decades."),

 dict(q="Birth rates before and after a country's antinatalist programme are shown. Using the table, what was the programme's measured effect?",
   table=dict(
     headers=["Year", "Crude birth rate (per 1,000)"],
     rows=[
       ["Year 0 (programme begins)", "38"],
       ["Year 5", "33"],
       ["Year 10", "27"],
       ["Year 15", "22"],
       ["Year 20", "19"]]),
   choices=[
     "The birth rate fell by 19 points, exactly halving over twenty years",
     "The birth rate fell by 19 percent over twenty years",
     "The birth rate was unchanged",
     "The birth rate fell fastest in the first five years",
     "The birth rate rose after Year 10"],
   ans=0,
   why="From 38 to 19 is a fall of 19 points, and 19 is exactly half of 38, so the proportional fall is 50 percent rather than 19. The largest five-year drop is the 6 points between Year 5 and Year 10, not the 5 points in the first interval."),

 dict(q="Sex ratios at birth are shown for a country before and during a strict birth limit. Using the table, what effect on composition is visible?",
   table=dict(
     headers=["Period", "Males per 100 female births"],
     rows=[
       ["Before the limit", "106"],
       ["First decade of the limit", "111"],
       ["Second decade of the limit", "118"],
       ["Third decade of the limit", "117"]]),
   choices=[
     "The ratio rose 12 points above its pre-policy level, an imbalance that a normal biological range cannot explain",
     "The ratio fell steadily under the policy",
     "The ratio remained within its pre-policy level throughout",
     "The ratio rose by 118 points",
     "The ratio was highest before the limit was introduced"],
   ans=0,
   why="The ratio moves from 106 to a peak of 118, a rise of 12 points, and stays near that level. A sex ratio at birth around 105 or 106 is the ordinary range, so a sustained value near 118 is evidence of a behavioural response to the limit rather than of biology."),

 dict(q="Four states report all three components of population change, in rates per 1,000. Using the table, which state would be losing people if it admitted no migrants at all?",
   table=dict(
     headers=["Country", "Crude birth rate", "Crude death rate", "Net migration rate"],
     rows=[
       ["Country A", "9", "12", "+8"],
       ["Country B", "17", "7", "+2"],
       ["Country C", "12", "9", "0"],
       ["Country D", "8", "13", "-1"]]),
   choices=[
     "Country A, which would shrink at 3 per 1,000 without migration but grows at 5 per 1,000 with it",
     "Country B, whose natural increase is the highest in the table",
     "Country C, whose net migration is zero",
     "Country D, which is losing people through both channels",
     "None of them, since migration never determines growth"],
   ans=0,
   why="Natural increase is minus 3, plus 10, plus 3 and minus 5 per 1,000, so only one country combines a natural deficit with a total that is nonetheless positive. Its entire growth is imported, which is what makes its immigration settings decisive."),

 dict(q="Fertility before and after a pronatalist package is shown for four countries. Using the table, which country's policy had the largest measured effect?",
   table=dict(
     headers=["Country", "Fertility before policy", "Fertility after ten years"],
     rows=[
       ["Country P", "1.30", "1.55"],
       ["Country Q", "1.90", "1.98"],
       ["Country R", "1.45", "1.52"],
       ["Country S", "1.60", "1.58"]]),
   choices=[
     "Country P, with a rise of 0.25 children per woman, though still well below replacement",
     "Country Q, which reached the highest fertility of the four",
     "Country R, with a rise of 0.07 children per woman",
     "Country S, whose fertility fell slightly",
     "All four had the same effect, since all adopted a policy"],
   ans=0,
   why="Differences of plus 0.25, plus 0.08, plus 0.07 and minus 0.02 make one country's change three times the next largest, and the country ending highest is not the one that moved most. Even the largest rise leaves fertility far short of the replacement level of about 2.1."),

 dict(q="Two immigration systems admitting the same number of people are compared. Using the table, what is the main difference between them?",
   table=dict(
     headers=["Characteristic of those admitted", "System 1 (%)", "System 2 (%)"],
     rows=[
       ["Aged 20-44 on arrival", "82", "46"],
       ["Holding a tertiary qualification", "71", "24"],
       ["Arriving with dependent children", "9", "48"],
       ["Arriving as part of a family group", "12", "63"]]),
   choices=[
     "System 1 selects working-age qualified individuals while System 2 admits families, so they change composition very differently even at the same total",
     "System 1 admits more people than System 2",
     "System 2 admits more working-age people than System 1",
     "The two systems produce identical populations",
     "Neither system affects the composition of the population"],
   ans=0,
   why="The stem holds the number admitted equal, so every difference in the table is a difference in composition rather than in size. One system takes 82 percent from a single age band and 71 percent with degrees; the other takes 63 percent as family groups and nearly half with children."),
]
