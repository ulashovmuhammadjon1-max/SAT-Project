"""Key audit for AP ENVIRONMENTAL SCIENCE 3.9 Demographic Transition.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-1.D.1  the demographic transition refers to the transition from high to
             lower birth and death rates in a country or region as development
             occurs and that country moves from a pre-industrial to an
             industrialized economic system; this transition is typically
             demonstrated through a four-stage demographic transition model
                 -- items 1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 14, 15, 16, 17, 18,
                    19, 20, 21, 26, 27, 28, 29, 30
  EIN-1.D.2  characteristics of developing countries include higher infant
             mortality rates and more children in the workforce than developed
             countries
                 -- items 8, 9, 12, 22, 23, 24, 25, 29, 30

THE FRAMEWORK DESCRIBES NO STAGE. It names a four stage model and says only
that the transition runs from high to lower birth AND death rates as
development occurs. So no key here states what happens in any stage, gives a
duration for one, or assigns a country to one; item 7 keys that absence
directly and item 28 refuses the reading that all countries move at one pace.
Item 16 reads the order in which the two rates fall in ONE record and its
``why`` says in terms that the framework itself makes no claim about that
order.

THE SWAP IS THE DANGER. High to lower against low to higher (items 1, 10, 11,
13, 30), both rates high against both rates low (items 17, 18, 19), and
developing against developed (items 8, 25) are the reversals a prepared student
falls for, so each anchor on those items carries BOTH clauses -- the direction
and the thing that moves. An anchor of "birth and death rates" alone would
match the swapped distractor as readily as the key.

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run and its control injects a stem that points at one. This matters here more
than in most topics, because the demographic transition model is normally
taught from a picture the bank cannot carry.

DATA ITEMS: 13 to 25 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e3_9

CBR = "Crude birth rate per 1,000 people"
CDR = "Crude death rate per 1,000 people"
INDUSTRY = "Percent of the workforce employed in industry and services"
INFANT = "Infant deaths per 1,000 live births"
WORKING = "Percent of children aged 10 to 14 who are in the workforce"
M = "Country M"
N = "Country N"


def _argmax(values):
    return max(range(len(values)), key=lambda i: values[i])


def _argmin(values):
    return min(range(len(values)), key=lambda i: values[i])


def q13(table, item):
    births = cg.col(table, CBR)
    deaths = cg.col(table, CDR)
    assert births[-1] < births[0] and deaths[-1] < deaths[0], \
        f"both rates must end below where they began; got {births} and {deaths}"
    assert births[-1] < 0.5 * births[0] and deaths[-1] < 0.5 * deaths[0], \
        "both falls must be large enough to be called far lower"
    return (f"the birth rate runs {births} and the death rate {deaths} per thousand, each "
            "ending at well under half its starting value")


def q14(table, item):
    births = cg.col(table, CBR)
    fall = births[0] - births[-1]
    assert abs(fall - 31) < 1e-9, f"the birth rate must fall by 31 per thousand; got {fall}"
    assert fall > 0, "the movement must be a fall rather than a rise"
    return (f"the crude birth rate runs from {births[0]:.0f} to {births[-1]:.0f} per "
            f"thousand, a fall of {fall:.0f}")


def q15(table, item):
    deaths = cg.col(table, CDR)
    fall = deaths[0] - deaths[-1]
    assert abs(fall - 29) < 1e-9, f"the death rate must fall by 29 per thousand; got {fall}"
    assert fall > 0, "the movement must be a fall rather than a rise"
    return (f"the crude death rate runs from {deaths[0]:.0f} to {deaths[-1]:.0f} per "
            f"thousand, a fall of {fall:.0f}")


def q16(table, item):
    births = cg.col(table, CBR)
    deaths = cg.col(table, CDR)
    birth_fall = births[0] - births[1]
    death_fall = deaths[0] - deaths[1]
    assert abs(birth_fall - 1) < 1e-9, \
        f"the birth rate must fall by 1 between the first two periods; got {birth_fall}"
    assert abs(death_fall - 12) < 1e-9, \
        f"the death rate must fall by 12 between the first two periods; got {death_fall}"
    assert death_fall > birth_fall, "the death rate must be the one that falls further"
    return (f"between the first two periods the birth rate falls {birth_fall:.0f} and the "
            f"death rate {death_fall:.0f} per thousand, so the death rate falls further")


def q17(table, item):
    labels = cg.labels(table)
    births = cg.col(table, CBR)
    deaths = cg.col(table, CDR)
    assert len(set(births)) == len(births) and len(set(deaths)) == len(deaths), \
        "no two countries may share a rate, or the record cannot rank them"
    order_b = sorted(range(len(births)), key=lambda i: births[i])
    order_d = sorted(range(len(deaths)), key=lambda i: deaths[i])
    assert order_b == order_d, \
        f"the two rates must rank the countries alike; got {order_b} and {order_d}"
    assert _argmax(births) == _argmax(deaths), \
        "one country must lead on both rates, so 'highest birth with lowest death' is false"
    assert _argmin(births) == _argmin(deaths), \
        "one country must trail on both rates, so 'lowest birth with highest death' is false"
    assert _argmax(births) != _argmin(births), "the leader and the trailer must differ"
    return (f"the birth rates read {births} and the death rates {deaths} per thousand, "
            f"which rank the countries identically, with {labels[_argmax(births)]} leading "
            f"on both and {labels[_argmin(births)]} trailing on both")


def q18(table, item):
    labels = cg.labels(table)
    births = cg.col(table, CBR)
    deaths = cg.col(table, CDR)
    top = _argmax(births)
    assert top == _argmax(deaths), "the highest birth rate and highest death rate must coincide"
    assert labels[top] == "Country 1", \
        f"that country must be Country 1; got {labels[top]}"
    return (f"{labels[top]} carries the highest birth rate, {births[top]:.0f}, and the "
            f"highest death rate, {deaths[top]:.0f}, per thousand, so both are still high")


def q19(table, item):
    labels = cg.labels(table)
    births = cg.col(table, CBR)
    deaths = cg.col(table, CDR)
    bottom = _argmin(births)
    assert bottom == _argmin(deaths), "the lowest birth rate and lowest death rate must coincide"
    assert labels[bottom] == "Country 4", \
        f"that country must be Country 4; got {labels[bottom]}"
    return (f"{labels[bottom]} carries the lowest birth rate, {births[bottom]:.0f}, and the "
            f"lowest death rate, {deaths[bottom]:.0f}, per thousand, so both have reached "
            "the low end")


def q20(table, item):
    for rate in (CBR, CDR):
        pairs = sorted(zip(cg.col(table, INDUSTRY), cg.col(table, rate)))
        assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
            f"sorted by the industry share the {rate!r} must fall strictly; got {pairs}"
    return (f"sorted by the share of the workforce in industry and services, the birth "
            f"rates read {sorted(cg.col(table, CBR), reverse=True)} and the death rates "
            f"{sorted(cg.col(table, CDR), reverse=True)} per thousand, both falling")


def q21(table, item):
    labels = cg.labels(table)
    industry = cg.col(table, INDUSTRY)
    births = cg.col(table, CBR)
    deaths = cg.col(table, CDR)
    least = _argmin(industry)
    assert least == _argmax(births) == _argmax(deaths), \
        "the least industrialized region must also carry the highest of both rates"
    assert labels[least] == "Region 1", f"that region must be Region 1; got {labels[least]}"
    return (f"{labels[least]} records the smallest industry share, {industry[least]:.0f} "
            f"percent, with the largest birth rate, {births[least]:.0f}, and the largest "
            f"death rate, {deaths[least]:.0f}, per thousand")


def q22(table, item):
    pairs = sorted(zip(cg.col(table, INFANT), cg.col(table, WORKING)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"children working must rise with infant deaths; got {pairs}"
    assert len(set(cg.col(table, INFANT))) == len(cg.col(table, INFANT)), \
        "'every country records the same infant mortality' must be false"
    assert len(set(cg.col(table, WORKING))) == len(cg.col(table, WORKING)), \
        "'every country records the same share of children working' must be false"
    return (f"sorted by infant deaths the share of children in the workforce reads "
            f"{[w for _, w in pairs]} percent, rising in step")


def q23(table, item):
    labels = cg.labels(table)
    infant = cg.col(table, INFANT)
    working = cg.col(table, WORKING)
    top = _argmax(infant)
    assert top == _argmax(working), "one country must lead on both columns"
    assert labels[top] == "Country A", f"that country must be Country A; got {labels[top]}"
    assert _argmin(infant) == _argmin(working) != top, \
        "a different country must trail on both columns"
    return (f"{labels[top]} records the largest infant deaths, {infant[top]:.0f} per "
            f"thousand, and the largest share of children working, {working[top]:.0f} "
            "percent")


def q24(table, item):
    infant = cg.col(table, INFANT)
    ratio = max(infant) / min(infant)
    assert abs(ratio - 17) < 1e-9, f"the ratio must be 17; got {ratio}"
    return (f"the largest infant mortality, {max(infant):.0f}, divided by the smallest, "
            f"{min(infant):.0f}, gives {ratio:.0f}")


def q25(table, item):
    labels = cg.labels(table)
    m = cg.col(table, M)
    n = cg.col(table, N)
    assert labels[0] == INFANT, f"the first row must be infant deaths; got {labels[0]!r}"
    assert labels[1] == WORKING, f"the second row must be children working; got {labels[1]!r}"
    higher_on_both = all(a > b for a, b in zip(m, n))
    lower_on_both = all(a < b for a, b in zip(m, n))
    assert higher_on_both, f"Country M must stand higher on both measures; got {m} against {n}"
    assert not lower_on_both, "Country M must not stand lower on both measures"
    # A bare "higher on both" survives almost any corruption of these four cells, so the
    # gap itself is asserted: the two columns must be an order of magnitude apart on each
    # measure, which is what makes the keyed choice unambiguous rather than marginal.
    ratios = [a / b for a, b in zip(m, n)]
    assert all(r >= 10 for r in ratios), \
        f"Country M must stand at least tenfold above Country N on each measure; got {ratios}"
    return (f"Country M records {m} against Country N's {n} on infant deaths and on "
            f"children in the workforce, standing higher on both by factors of "
            f"{[round(r, 1) for r in ratios]}")


CLAIMS = [
 ("from high to lower birth and death rates",
  "EIN-1.D.1, near verbatim: the demographic transition refers to the transition from high to lower birth and death rates in a country or region as development occurs. The anchor carries the direction and both rates, because one rejected option reverses the direction and two others drop one of the rates."),
 ("from a pre-industrial to an industrialized economic system",
  "EIN-1.D.1 places the transition where development occurs and the country moves from a pre-industrial to an industrialized economic system, and names that direction of change and no other."),
 ("four stage demographic transition model",
  "EIN-1.D.1's second sentence states that the transition is typically demonstrated through a four-stage demographic transition model, so the number of stages is the framework's own rather than a convention."),
 ("Four",
  "EIN-1.D.1 calls it a four-stage demographic transition model, so the count is stated outright in the framework."),
 ("Birth rates and death rates together",
  "EIN-1.D.1 names both rates in one movement from high to lower, and mentions neither immigration nor emigration in this statement."),
 ("usual way of showing it, not the only possible way",
  "EIN-1.D.1's hedge TYPICALLY marks the four-stage model as the usual representation rather than the only one, so the framework asserts neither exclusivity nor the absence of stages."),
 ("names the model and describes only the transition as a whole",
  "EIN-1.D.1 names the four-stage model and describes the transition as a movement from high to lower birth and death rates as development occurs. It supplies no rates for a stage, no duration, no country list and no outcome for any stage, so nothing about an individual stage can be keyed here."),
 ("Higher infant mortality rates and more children in the workforce",
  "EIN-1.D.2, near verbatim: characteristics of developing countries include higher infant mortality rates and more children in the workforce than developed countries. The anchor carries both halves, because two rejected options reverse one half each."),
 ("A larger land area than developed countries",
  "EIN-1.D.2 names higher infant mortality rates and more children in the workforce, which the four rejected options restate in one wording or another. Land area appears in neither of this topic's statements."),
 ("both birth rates and death rates moving from high to lower",
  "EIN-1.D.1 puts birth and death rates together in one movement from high to lower as development occurs, so an account that leaves death rates out drops half of the statement."),
 ("running from high rates to lower ones",
  "EIN-1.D.1 gives the direction explicitly, from high to lower birth and death rates, so the reversed reading contradicts the statement rather than restating it."),
 ("Developing countries set against developed countries",
  "EIN-1.D.2 states its two characteristics of developing countries explicitly in comparison with developed countries, which is the only comparison the statement makes."),
 ("end far lower than they began, which is the movement the framework describes",
  "Recomputed in q13 above: each rate ends at well under half its starting value. EIN-1.D.1 describes the transition as a movement from high to lower birth and death rates as development occurs. The anchor carries the direction because the rejected option is that sentence with lower replaced by higher."),
 ("By 31 per thousand people",
  "Recomputed in q14 above: the first and last entries of the crude birth rate column differ by 31 per thousand, downward. EIN-1.D.1 makes the movement of birth rates from high to lower one half of the transition."),
 ("By 29 per thousand people",
  "Recomputed in q15 above: the first and last entries of the crude death rate column differ by 29 per thousand, downward. EIN-1.D.1 makes the movement of death rates from high to lower the other half."),
 ("death rate, which fell by 12 per thousand against the birth rate's 1",
  "Recomputed in q16 above: between the first two periods the birth rate falls by 1 and the death rate by 12 per thousand. This is a reading of the record only; EIN-1.D.1 describes the overall movement of both rates and states nothing about which falls first."),
 ("stand at different points, with both rates highest in one country and both lowest in another",
  "Recomputed in q17 above: the two rate columns rank the four countries identically, one country leading on both and another trailing on both, with no ties. EIN-1.D.1 describes the transition as a movement from high to lower birth and death rates, so countries part way along it stand at different points."),
 ("Country 1, whose birth rate and death rate are both the highest",
  "Recomputed in q18 above: the highest birth rate and the highest death rate belong to the same country. EIN-1.D.1 runs the transition from high to lower rates, so a country still carrying the highest of both has not yet made that movement."),
 ("Country 4, whose birth rate and death rate are both the lowest",
  "Recomputed in q19 above: the lowest birth rate and the lowest death rate belong to the same country. EIN-1.D.1 runs the transition from high to lower rates, so a country carrying the lowest of both stands at the far end of it."),
 ("Both crude rates fall as the share of the workforce in industry and services rises",
  "Recomputed in q20 above: sorting the regions by the industry and services share leaves both crude rates strictly falling. EIN-1.D.1 ties the movement from high to lower birth and death rates to a country moving from a pre-industrial to an industrialized economic system."),
 ("Region 1",
  "Recomputed in q21 above: the smallest industry share and the largest of both rates fall in the same row. EIN-1.D.1 places the movement of the rates alongside the move to an industrialized economic system."),
 ("with higher infant mortality also have more children in the workforce",
  "Recomputed in q22 above: sorting by infant deaths leaves the share of children in the workforce rising in step, with no ties in either column. EIN-1.D.2 names both together as characteristics of developing countries."),
 ("Country A, which leads the record on infant deaths and on children working",
  "Recomputed in q23 above: the largest infant mortality and the largest share of children working belong to one country, and the smallest of each to a different one. EIN-1.D.2 names both as characteristics of developing countries relative to developed ones."),
 ("Seventeen times",
  "Recomputed in q24 above: the largest infant mortality divided by the smallest gives seventeen. EIN-1.D.2 makes higher infant mortality one of the characteristics separating developing from developed countries."),
 ("Country M, which records the higher figure on both measures",
  "Recomputed in q25 above: one column stands above the other on infant deaths and on children in the workforce alike. EIN-1.D.2 attributes both to developing countries, so the anchor names the country and the direction together."),
 ("as a country moves from a pre-industrial to an industrialized economic system",
  "EIN-1.D.1 joins exactly those two things in one sentence: the movement of both rates from high to lower, and the country's move from a pre-industrial to an industrialized economic system."),
 ("both the birth rate and the death rate falling over time as the economy industrializes",
  "EIN-1.D.1 describes a movement of both rates from high to lower as development occurs, so the evidence bearing on it follows both rates over time alongside the change in the economy, rather than either rate on a single occasion."),
 ("makes no claim about pace or about every country",
  "EIN-1.D.1 names the four-stage model as the typical way of demonstrating the transition and states nothing about how fast any country moves through it, nor that every country does."),
 ("hold larger total populations than developed countries",
  "EIN-1.D.1 and EIN-1.D.2 supply the four rejected statements between them, and neither says anything about the total size of a developing country's population, so that comparison is an addition to the framework."),
 ("high to lower birth and death rates as a country develops from a pre-industrial to an industrialized economy",
  "EIN-1.D.1 supplies the direction of the transition, the economic change it accompanies and the four-stage model, and EIN-1.D.2 supplies both characteristics of developing countries. The rejected summaries reverse the direction, cut a rate, change the stage count, or claim stage detail the framework never gives."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19,
                20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25}

if "--selftest" in sys.argv:
    es.selftest(e3_9, CLAIMS, TABLE_CHECKS)

e_check.run(e3_9, CLAIMS, TABLE_CHECKS)
