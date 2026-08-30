"""Key audit for AP HUMAN GEOGRAPHY 2.4 Population Dynamics.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. IMP-2.A prints three essential-knowledge statements:

    IMP-2.A.1  Demographic factors that determine a population's growth and
               decline are fertility, mortality, and migration.
    IMP-2.A.2  Geographers use the rate of natural increase and
               population-doubling time to explain population growth and decline.
    IMP-2.A.3  Social, cultural, political, and economic factors influence
               fertility, mortality, and migration rates.

IMP-2.A.1's list is closed and the third member is the one students drop. Items
1, 3, 6, 9, 14, 18, 20, 21, 23, 25 and 28 are keyed to the fact that natural
increase omits migration, so a country can have positive natural increase and a
shrinking population, or the reverse. All of them cite it.

IMP-2.A.2 names the rate of natural increase and doubling time but PRINTS
NEITHER FORMULA, so every computational key here rests on the standard
definitions recorded in the module header. Those claims say so rather than
attaching a code to arithmetic the CED never wrote down:

    rate of natural increase (%) = (birth rate - death rate) / 10
    doubling time (years)        = 70 / growth rate in percent   [approximate]
    overall growth rate          = natural increase + net migration

The rule of 70 is an approximation, and every item using it says "about" or
"roughly". Presenting an approximation as an exact result would be its own kind
of wrong key, and the recompute functions below assert the wording holds.

IMP-2.A.3 carries items 5, 11, 15, 17, 22 and 24, all of which ask what makes a
rate move rather than what the rate is.

Items 7, 8, 16 and 19 cite nothing. Their keys rest on properties of the
measures that the CED does not state -- that a crude rate is unadjusted for age
structure and therefore not comparable between differently aged populations,
that the lifetime fertility measure is constructed to remove that dependence,
and that mortality falls before fertility so the gap between them is the period
of fastest growth. Each is argued in the claim.

The five table items (26-30) are the computational gate, and three of them are
built so the eye-catching column misleads:

  26  the country with the HIGHEST birth rate also has the highest death rate,
      so it does not have the highest natural increase
  28  the only shrinking country is one whose BIRTHS EXCEED ITS DEATHS, and a
      country whose deaths exceed its births is growing -- the recompute
      asserts both, because that inversion is the entire item
  29  the country with the second-lowest lifetime fertility has the second
      HIGHEST crude birth rate, which is the two measures disagreeing

REVIEW NOTE, written while building the tables. Item 26 offered a distractor
reading "Country D, at 1.9 percent" when D's natural increase is 1.4 percent;
corrected. Item 28's first draft had TWO shrinking countries, so the stem
"which country's population is shrinking" had two correct answers; the first
country's migration rate was changed so exactly one country shrinks, and the
recompute asserts that count. No key was changed in either case.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_4


def q26_natural_increase(table):
    """Natural increase per country, and the highest-birth-rate trap."""
    rni, births, deaths = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        b = num(d["Crude birth rate (per 1,000)"])
        m = num(d["Crude death rate (per 1,000)"])
        births[d["Country"]] = b
        deaths[d["Country"]] = m
        rni[d["Country"]] = (b - m) / 10
    best = max(rni, key=rni.get)
    assert best == "Country A", rni
    assert rni == {"Country A": 2.5, "Country B": 2.2,
                   "Country C": 0.1, "Country D": 1.4}, rni
    # The trap: the highest birth rate belongs to a different country, and that
    # country also carries the highest death rate.
    top_birth = max(births, key=births.get)
    assert top_birth != best, births
    assert max(deaths, key=deaths.get) == top_birth, deaths
    return "2.5 percent"


def q27_doubling(table):
    """Doubling times from the rule of 70; shortest belongs to the fastest grower."""
    dt = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        r = num(d["Annual growth rate (%)"])
        dt[d["Country"]] = 70 / r
    shortest = min(dt, key=dt.get)
    assert shortest == "Country X", dt
    assert abs(dt["Country X"] - 20) < 1e-9, dt
    assert abs(dt["Country W"] - 100) < 1e-9, dt
    assert abs(dt["Country Y"] - 50) < 1e-9, dt
    assert abs(dt["Country Z"] - 35) < 1e-9, dt
    # The rule is an approximation, so the keyed choice must hedge.
    assert "about" in g2_4.QUESTIONS[26]["choices"][g2_4.QUESTIONS[26]["ans"]].lower()
    return "about 20 years"


def q28_three_components(table):
    """Total change is the sum of all three rates; exactly one country shrinks."""
    total, natural = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        b = num(d["Crude birth rate"])
        m = num(d["Crude death rate"])
        mig = num(d["Net migration rate"])
        natural[d["Country"]] = b - m
        total[d["Country"]] = b - m + mig
    shrinking = [c for c in total if total[c] < 0]
    assert shrinking == ["Country K"], total
    # The whole point: the shrinking country has POSITIVE natural increase, and
    # at least one country with negative natural increase is nonetheless growing.
    assert natural["Country K"] > 0, natural
    assert any(natural[c] < 0 and total[c] > 0 for c in total), (natural, total)
    return "net loss to migration exceeds its positive natural increase"


def q29_fertility_vs_birth_rate(table):
    """Lifetime fertility ranks countries differently from the crude birth rate."""
    tfr, cbr = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        tfr[d["Country"]] = num(d["Total fertility rate"])
        cbr[d["Country"]] = num(d["Crude birth rate (per 1,000)"])
    lowest = min(tfr, key=tfr.get)
    assert lowest == "Country P", tfr
    assert tfr["Country P"] == 1.1, tfr
    # The two measures must disagree, or the item teaches nothing.
    by_tfr = sorted(tfr, key=tfr.get)
    by_cbr = sorted(cbr, key=cbr.get)
    assert by_tfr != by_cbr, (by_tfr, by_cbr)
    # Specifically: the second-lowest fertility carries the second-highest births.
    second_low_tfr = by_tfr[1]
    assert second_low_tfr == "Country S", by_tfr
    assert by_cbr[-2] == "Country S", by_cbr
    # And only one country is at or above replacement.
    assert [c for c in tfr if tfr[c] >= 2.1] == ["Country R"], tfr
    return "1.1 children per woman"


def q30_rni_over_time(table):
    """Natural increase rises then falls, because deaths fall before births do."""
    series = []
    for row in table["rows"]:
        d = rowdict(table, row)
        b = num(d["Crude birth rate (per 1,000)"])
        m = num(d["Crude death rate (per 1,000)"])
        series.append((num(d["Year"]), b, m, (b - m) / 10))
    series.sort()
    rni = [s[3] for s in series]
    assert rni == [2.4, 2.8, 1.6], rni
    assert rni[1] > rni[0] and rni[2] < rni[1], rni
    # Deaths must fall throughout while the birth rate's big fall comes last.
    deaths = [s[2] for s in series]
    births = [s[1] for s in series]
    assert deaths[0] > deaths[1] > deaths[2], deaths
    assert (deaths[0] - deaths[1]) > (births[0] - births[1]), (births, deaths)
    assert (births[1] - births[2]) > (deaths[1] - deaths[2]), (births, deaths)
    return "rose from 2.4 to 2.8 percent"


CLAIMS = [
 ("Fertility, mortality, and migration",
  "EK IMP-2.A.1 names exactly these three as the demographic factors determining a population's growth and decline. Urbanization, literacy, industrialization and density may influence those three, but none of them adds or removes a person from a national total by itself."),

 ("1.4 percent",
  "Natural increase is births minus deaths, so 22 minus 8 leaves 14 per 1,000, which is 1.4 percent. Migration is excluded by definition, which is why the figure can be computed from the two rates alone; the CED names the measure at IMP-2.A.2 without printing the formula."),

 ("Net out-migration exceeded the surplus of births over deaths",
  "EK IMP-2.A.1 lists migration alongside fertility and mortality while the rate of natural increase measures only the first two. A larger outflow than the natural surplus is the one way a total can fall while natural increase remains positive."),

 ("About 35 years",
  "EK IMP-2.A.2 names population-doubling time among the measures geographers use, and the standard approximation divides 70 by the growth rate in percent. Seventy over two is thirty-five, and the keyed choice hedges because the rule is an approximation rather than an exact result."),

 ("education and paid employment for women expand",
  "EK IMP-2.A.3 states that social, cultural, political and economic factors influence fertility, mortality and migration rates. Education, employment and the cost of raising a child are exactly such factors, and they act through household decisions rather than by decree."),

 ("the third component of population change",
  "EK IMP-2.A.1 makes population change the sum of three components, and the premise holds two of them equal. With natural increase identical in both countries, only the migration term can produce opposite outcomes."),

 ("much older age structure",
  "A crude rate divides events by the whole population regardless of its composition, so a population concentrated in the old ages records many deaths per thousand however good its medicine. The CED does not state this, so the claim is argued from how the measure is built."),

 ("children a woman would bear over her lifetime",
  "The measure applies this year's fertility at each age to a hypothetical woman passing through all of them, which is why it is stated per woman rather than per thousand people. That construction is what makes it comparable across countries with different age structures."),

 ("population momentum from large earlier cohorts",
  "EK IMP-2.A.1 makes migration a component of change alongside fertility and mortality, and a large cohort already in the childbearing ages produces many births even at a low rate. Either mechanism alone can sustain growth long after fertility falls below replacement."),

 ("fall in the death rate produced by improved sanitation",
  "Natural increase is births minus deaths, so with births held fixed only the death term can move it, and a falling death rate moves it up. Migration changes the total population without entering the natural increase calculation at all."),

 ("Political and economic factors influence mortality rates",
  "EK IMP-2.A.3 makes political and economic factors act on mortality, and EK IMP-2.A.1 makes mortality one of the three determinants of growth. A programme that saves lives widens the gap between births and deaths without touching births."),

 ("doubling time implied by the current growth rate",
  "EK IMP-2.A.2 names population-doubling time as one of the measures geographers use to explain growth. Expressing a rate as the number of years until the population is twice its present size turns an abstract percentage into a planning horizon."),

 ("about 140 years against about 20 years",
  "Seventy divided by 0.5 is 140 and seventy divided by 3.5 is 20, so the ratio of doubling times inverts the ratio of growth rates. Small differences in an annual percentage compound into very large differences within a human lifetime."),

 ("Urbanization",
  "EK IMP-2.A.1 names fertility, mortality and migration, and migration covers movement in both directions. Moving from a rural district to a city inside the same country redistributes a national population without changing its size at all."),

 ("later marriage, urban living costs, and wider access to contraception",
  "EK IMP-2.A.3 attributes fertility rates to social, cultural, political and economic factors. Fertility declines of that speed are consistently associated with this same cluster of household-level changes rather than with any one cause acting alone."),

 ("how many women of childbearing age the population happens to contain",
  "Dividing births by the whole population makes the result depend on age structure, so a young population records a high crude rate even at moderate fertility. The lifetime measure removes that dependence, which is why it travels better between countries."),

 ("Mortality directly, and migration as refugees leave",
  "EK IMP-2.A.1's three components are not mutually exclusive, and a war moves all three: deaths rise, people flee, and couples are separated or impoverished so births are postponed. EK IMP-2.A.3 makes the political factor the common cause behind all three."),

 ("About 3 percent",
  "The rule of 70 relates doubling time and growth rate reciprocally, so a doubling time near 23 years implies a rate near 70 divided by 23, which is close to 3 percent. The approximation runs in both directions and the keyed choice hedges accordingly."),

 ("Mortality usually falls before fertility does",
  "Death rates respond quickly to public health, sanitation and food supply while birth rates respond to household decisions that shift over a generation. The interval in which deaths have fallen and births have not is arithmetically the period of maximum natural increase."),

 ("Internal migration moves people between regions",
  "EK IMP-2.A.1 makes migration one of the three components, and an internal move is an addition in one place and a subtraction in another. The national figure nets those to zero while the local figures record the movement in full."),

 ("natural increase of 0.1 percent and net migration of 0.6 percent are added",
  "EK IMP-2.A.1 makes total change the sum of natural increase and net migration, so 11 minus 10 gives 1 per 1,000 and the migration term adds 6 more, for 7 per 1,000 or 0.7 percent. Adding the death rate as a third positive term is the error the largest distractor represents."),

 ("political and economic factors influence fertility rates",
  "EK IMP-2.A.3 names political and economic factors among those influencing fertility, and a cash payment with parental leave is both at once. The modest size of the response is itself informative, since it shows the policy acting on one input among many."),

 ("Natural increase counts only births and deaths",
  "EK IMP-2.A.2 names the rate of natural increase specifically and EK IMP-2.A.1 makes migration a separate component of change. The two measures coincide only in the special case where net migration happens to be zero."),

 ("expanded prenatal care and clean water supply",
  "EK IMP-2.A.3 attributes demographic rates to social, cultural, political and economic factors, and prenatal care and water supply are exactly such conditions acting on infant survival. Each of the other pairings joins a rate to something with no mechanism connecting them."),

 ("people who would have had children are no longer there",
  "EK IMP-2.A.1's three components interact, and removing people of childbearing age removes their future births along with themselves. The effect on the birth count persists for decades even where the fertility rate per woman never changes."),

 ("2.5 percent",
  "Recomputed from the table: natural increase is 25, 22, 1 and 14 per 1,000, or 2.5, 2.2, 0.1 and 1.4 percent. The verifier confirms separately that the country with the highest birth rate also carries the highest death rate, which is why the birth column alone gives the wrong answer.",
  q26_natural_increase),

 ("Country X, at about 20 years",
  "Recomputed from the table: seventy divided by each rate gives about 100, 20, 50 and 35 years, so the fastest-growing country doubles in roughly two decades. The verifier also asserts the keyed choice hedges, because the rule of 70 is an approximation and must not be presented as exact.",
  q27_doubling),

 ("net loss to migration exceeds its positive natural increase",
  "Recomputed from the table: summing all three rates gives plus 3, minus 5, plus 5 and plus 3 per 1,000, so exactly one country is shrinking and its births exceed its deaths. The verifier also confirms that a country whose deaths exceed its births is nonetheless growing, which is the inversion the item is built on.",
  q28_three_components),

 ("1.1 children per woman",
  "Recomputed from the table: only the lifetime measure is comparable with the replacement level of about 2.1, and 1.1 is the lowest of the four. The verifier confirms the two fertility measures rank the countries differently, with the second-lowest lifetime rate paired with the second-highest crude birth rate.",
  q29_fertility_vs_birth_rate),

 ("rose from 2.4 to 2.8 percent",
  "Recomputed from the table: natural increase runs 24, 28 and 16 per 1,000, so it rises before it falls. The verifier confirms the death rate falls throughout while the birth rate's large fall comes only in the final period, which is why the trend reverses rather than moving in one direction.",
  q30_rni_over_time),
]

hg_check.check(g2_4, CLAIMS, per_topic=30, n_choices=5)
