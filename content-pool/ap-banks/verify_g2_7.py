"""Key audit for AP HUMAN GEOGRAPHY 2.7 Population Policies.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic has one essential-knowledge statement, and the
learning objective above it does as much work as the statement does:

    SPS-2.A    Explain the INTENT AND EFFECTS of various population and
               immigration policies on population size and composition.
    SPS-2.A.1  Types of population policies include those that promote or
               discourage population growth, such as pronatalist, antinatalist,
               and immigration policies.

Two things follow, and between them they shape every item:

  1. The statement lists THREE types, and immigration is one of them. Items 3,
     7, 10, 14, 17, 20, 23, 25, 28 and 30 are keyed to that inclusion, which
     students routinely forget because "population policy" sounds like it should
     mean birth policy.
  2. The objective pairs INTENT with EFFECTS, and on SIZE with on COMPOSITION.
     Those are two independent splits and both are examinable. Items 5, 6, 8, 9,
     12, 16, 18, 21, 22, 24, 27 and 30 are built on a case where the two halves
     of one of those pairs come apart -- a policy that works in the intended
     direction but only slightly, one that shifts the timing of births without
     changing their number, one that achieves its target and produces a sex-ratio
     imbalance nobody legislated for.

NAMED COUNTRIES, AND THE LIMIT ON THEM. Only three real cases appear -- China's
one-child policy, Romania's 1966 decree, and India's family planning programme
-- and only for facts that are not in dispute: that the Chinese policy began in
1979 and was relaxed to two children in 2016 and three in 2021, and that the
Romanian decree was followed by a one-year spike and then a decline. No item
asserts a statistic about a named country that is not printed in its own table.
That restraint is deliberate: SOCIAL_BRIEF.md's rule is that an uncertain claim
is cut rather than guessed, and a fabricated national figure is the easiest
possible way to ship a lie.

The five table items (26-30) are the computational gate:

  26  a fall of 19 POINTS is a fall of 50 PERCENT, and the largest five-year
      drop is not the first one -- both distractors are arithmetic traps
  27  the sex ratio at birth rises 12 points above a normal range and stays
      there, which is a composition effect of a size policy
  28  the only country whose growth is entirely imported is the one with a
      NEGATIVE natural increase and a positive total
  29  the largest rise is more than three times the next largest, and the
      country ending highest is not the country that moved most
  30  the two systems admit the same number, so every difference in the table
      is composition rather than size

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_7


def q26_points_versus_percent(table):
    """A 19-point fall is a 50 percent fall, and the first interval is not the steepest."""
    rates = numcol(table, "Crude birth rate (per 1,000)")
    drop_points = rates[0] - rates[-1]
    drop_share = 100 * drop_points / rates[0]
    assert drop_points == 19, drop_points
    assert abs(drop_share - 50) < 1e-9, drop_share
    # The two arithmetic traps must both be genuinely wrong.
    assert abs(drop_share - drop_points) > 20, (drop_points, drop_share)
    steps = [rates[i] - rates[i + 1] for i in range(len(rates) - 1)]
    assert steps[0] != max(steps), steps
    assert all(s > 0 for s in steps), steps
    return "fell by 19 points"


def q27_sex_ratio_shift(table):
    """The ratio rises well above the ordinary biological range and stays there."""
    ratios = numcol(table, "Males per 100 female births")
    base = ratios[0]
    peak = max(ratios)
    assert base == 106, base
    assert peak == 118, peak
    assert peak - base == 12, (base, peak)
    # It must not be a single spike: the last period stays near the peak.
    assert ratios[-1] >= peak - 2, ratios
    # And the pre-policy value must sit inside the ordinary range.
    assert 103 <= base <= 107, base
    return "rose 12 points above its pre-policy level"


def q28_growth_from_migration(table):
    """Exactly one country has a natural deficit and a positive total."""
    natural, total = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        b = num(d["Crude birth rate"])
        m = num(d["Crude death rate"])
        mig = num(d["Net migration rate"])
        natural[d["Country"]] = b - m
        total[d["Country"]] = b - m + mig
    imported = [c for c in total if natural[c] < 0 < total[c]]
    assert imported == ["Country A"], (natural, total)
    assert natural["Country A"] == -3 and total["Country A"] == 5, (natural, total)
    # The highest natural increase belongs to a different country, which is the
    # distractor's true-but-irrelevant premise.
    assert max(natural, key=natural.get) != "Country A", natural
    return "shrink at 3 per 1,000 without migration"


def q29_policy_effect(table):
    """The largest fertility gain, against the highest final level."""
    change, after = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        b = num(d["Fertility before policy"])
        a = num(d["Fertility after ten years"])
        change[d["Country"]] = round(a - b, 2)
        after[d["Country"]] = a
    biggest = max(change, key=change.get)
    assert biggest == "Country P", change
    assert change["Country P"] == 0.25, change
    ranked = sorted(change.values(), reverse=True)
    assert ranked[0] > 3 * ranked[1], ranked
    # The country ending highest must NOT be the one that moved most.
    assert max(after, key=after.get) != biggest, after
    # And even the winner stays well below replacement.
    assert after[biggest] < 2.1, after
    # One country must have gone the wrong way, or the spread is uninteresting.
    assert any(v < 0 for v in change.values()), change
    return "rise of 0.25 children per woman"


def q30_composition_not_size(table):
    """Same number admitted, so every row is a composition difference."""
    for row in table["rows"]:
        d = rowdict(table, row)
        s1 = num(d["System 1 (%)"])
        s2 = num(d["System 2 (%)"])
        assert 0 <= s1 <= 100 and 0 <= s2 <= 100, (s1, s2)
        assert abs(s1 - s2) >= 20, (d["Characteristic of those admitted"], s1, s2)
    rows = {rowdict(table, r)["Characteristic of those admitted"]: rowdict(table, r)
            for r in table["rows"]}
    assert num(rows["Aged 20-44 on arrival"]["System 1 (%)"]) == 82
    assert num(rows["Holding a tertiary qualification"]["System 1 (%)"]) == 71
    assert num(rows["Arriving as part of a family group"]["System 2 (%)"]) == 63
    # System 1 must be the working-age-selective one, or the key is reversed.
    assert (num(rows["Aged 20-44 on arrival"]["System 1 (%)"])
            > num(rows["Aged 20-44 on arrival"]["System 2 (%)"]))
    return "selects working-age qualified individuals"


CLAIMS = [
 ("designed to raise the birth rate",
  "EK SPS-2.A.1 lists pronatalist policies among the types that promote population growth. Every instrument named in the stem lowers the cost of an additional child, which is the mechanism by which a state attempts to raise fertility."),

 ("intended to reduce the birth rate",
  "EK SPS-2.A.1 names antinatalist policies among the types that discourage population growth. Being voluntary changes the instrument rather than the intent, and the stated intent here is a smaller average family size."),

 ("points system that admits applicants according to age, language, and occupation",
  "EK SPS-2.A.1 lists immigration policies alongside pronatalist and antinatalist ones as population policies. A points system changes both how many people enter and who they are, which is the composition half of what SPS-2.A asks students to explain."),

 ("enforced by penalties as well as by persuasion",
  "EK SPS-2.A.1's antinatalist category covers policies intended to discourage population growth, and a legal limit on family size backed by fines is its strongest form. The undisputed dates are that it began in 1979 and was relaxed to two children in 2016 and three in 2021."),

 ("sex ratio skewed toward males",
  "SPS-2.A asks for effects on size AND composition, and this is the clearest case of the two diverging. A binding limit on births turns an existing preference for sons into a measurable imbalance in the sex ratio at birth, which no legislator wrote into the policy."),

 ("usually by modest amounts",
  "SPS-2.A pairs intent with effects, and the honest reading of the evidence is that pronatalist measures move fertility in the intended direction without closing the gap to replacement. Housing, careers, partnership and expectations are inputs no subsidy controls."),

 ("adds working-age people immediately",
  "EK SPS-2.A.1 groups the three policy types because they are alternative levers on the same problem, and they differ mainly in how fast they act. A newborn is a dependent for two decades while an admitted adult worker joins the labour force at once."),

 ("without changing the underlying desire for smaller families",
  "SPS-2.A asks for intent and effects, and the effect here separates cleanly into a large immediate response and a much smaller lasting one. Removing a means of avoiding a birth changes behaviour faster than it changes intentions."),

 ("in whatever way best serves their own goals",
  "A policy sets the terms on which families decide without deciding for them, so the aggregate outcome is the sum of household responses to a new constraint. That gap between rule and response is where the composition effects SPS-2.A asks about arise."),

 ("working-age, male-weighted population with few children",
  "EK SPS-2.A.1 makes immigration policy one of the instruments acting on population, and SPS-2.A asks about composition as well as size. A rule admitting workers without dependents selects a narrow slice of the age and sex distribution by construction."),

 ("priority in housing and schooling to families who have fewer children",
  "EK SPS-2.A.1's antinatalist category covers policies discouraging growth without specifying an instrument. A reward for compliance and a penalty for non-compliance both discourage births, but only the first leaves the household's legal freedom intact."),

 ("the rule was no longer the binding constraint",
  "SPS-2.A asks for effects rather than intentions, and a rule binds only while it is what prevents the behaviour. Once the cost of children and the alternatives open to women have moved, removing the legal ceiling changes very little."),

 ("older age structure and a rising share of dependents who are elderly",
  "EK SPS-2.A.1's antinatalist policies act on births, and fewer births now means a smaller cohort at every age later on. The effect on structure is delayed but arithmetically certain, which is why SPS-2.A distinguishes short-term from long-term effects."),

 ("broader in age and closer to balanced by sex",
  "EK SPS-2.A.1 treats immigration policy as an instrument acting on population and SPS-2.A asks about composition. Admitting households rather than individual workers imports a cross-section of ages and both sexes instead of a single slice."),

 ("raises the opportunity cost of a large family",
  "EK SPS-2.A.1's antinatalist category is defined by intent rather than by instrument, and schooling acts on the same outcome through households' own decisions. The mechanism is well documented and produces a durable change rather than a suppressed one."),

 ("intended to raise births and instead alter only their timing",
  "SPS-2.A asks for the intent AND effects of population policies, which is a deliberate pairing. A bonus paid for a birth before a deadline can move births earlier without adding any over a lifetime, which is intent and effect coming apart completely."),

 ("neither of the two sources of growth is operating",
  "Population changes only through births, deaths and migration, so closing one source while fertility sits well below replacement leaves nothing to offset mortality. EK SPS-2.A.1 places immigration policy alongside natalist policy precisely because they are alternative levers on the same total."),

 ("changed the languages, skills, and origins",
  "SPS-2.A distinguishes effects on size from effects on composition. Holding the number admitted constant while changing the selection criteria alters who the population is made of without altering how many people it contains."),

 ("career cost of having one",
  "A one-off payment addresses the direct cost of a birth while the larger cost is often years of forgone earnings and advancement. Policies aimed at the binding constraint show the larger measured effect, which is what SPS-2.A's focus on effects asks students to notice."),

 ("quota setting how many permanent residents may be admitted",
  "EK SPS-2.A.1 explicitly names immigration policies as one of the types of population policy. An admission quota changes the size and composition of the resident population directly, which makes it a population policy whatever its stated purpose."),

 ("reversing a fertility decline is far harder than causing one",
  "SPS-2.A asks about long-term as well as short-term effects, and this pair of policies is the standard demonstration that the two directions are asymmetric. Lowering fertility removes a constraint, while raising it means persuading households to want something they have stopped wanting."),

 ("serious unintended effects on sex ratio, aging, and individual rights",
  "SPS-2.A requires both intent and effects to be explained, and an honest account concedes the intended effect while naming the unintended ones. Denying that such policies lower births would be as inaccurate as ignoring what else they do."),

 ("admits substantial numbers of immigrants and the other does not",
  "Fertility is held equal by the premise, so no natalist policy either country has adopted can be doing the work. EK SPS-2.A.1's third type is the only lever left that can move two totals in opposite directions."),

 ("move the birth forward to qualify",
  "A timing response and a quantum response are indistinguishable in a single year's birth count and completely different over a lifetime. Separating them is the clearest case of the intent-and-effects analysis SPS-2.A calls for."),

 ("skills-selective immigration system",
  "EK SPS-2.A.1 names immigration policy as an instrument acting on population, and a selection rule acts on composition by construction. Natalist measures change how many people are born and cannot change what qualifications a population holds for at least two decades."),

 ("fell by 19 points",
  "Recomputed from the table: 38 to 19 is a fall of 19 points and exactly 50 percent, so the two distractors confusing points with percent are both wrong. The verifier also confirms the largest five-year drop is not the first interval, which disposes of a third distractor.",
  q26_points_versus_percent),

 ("rose 12 points above its pre-policy level",
  "Recomputed from the table: the ratio moves from 106 to a peak of 118 and stays near it, a rise of 12 points. A sex ratio at birth around 105 or 106 is the ordinary range, so a sustained value near 118 evidences a behavioural response rather than biology.",
  q27_sex_ratio_shift),

 ("shrink at 3 per 1,000 without migration",
  "Recomputed from the table: natural increase is minus 3, plus 10, plus 3 and minus 5 per 1,000, so exactly one country combines a natural deficit with a positive total. Its entire growth is imported, which is what makes its immigration settings decisive rather than incidental.",
  q28_growth_from_migration),

 ("rise of 0.25 children per woman",
  "Recomputed from the table: the changes are plus 0.25, plus 0.08, plus 0.07 and minus 0.02, so the largest is more than three times the next. The verifier confirms the country ending highest is not the one that moved most, and that even the largest rise leaves fertility well below replacement.",
  q29_policy_effect),

 ("selects working-age qualified individuals",
  "Recomputed from the table: the stem holds the number admitted equal, so every row is a difference in composition rather than in size, and every row differs by at least twenty points. One system draws 82 percent from a single age band and 71 percent with degrees, the other 63 percent as family groups.",
  q30_composition_not_size),
]

hg_check.check(g2_7, CLAIMS, per_topic=30, n_choices=5)
