"""Key audit for AP HUMAN GEOGRAPHY 2.9 Aging Populations.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. SPS-2.C prints two essential-knowledge statements:

    SPS-2.C.1  Population aging is determined by birth and death rates and life
               expectancy.
    SPS-2.C.2  An aging population has political, social, and economic
               consequences, including the dependency ratio.

SPS-2.C.1 names THREE determinants, and BIRTH RATES comes first. That ordering
matters, because the popular account of aging is that people live longer, and
the larger driver in most countries is that fewer are born: a proportion rises
when its denominator shrinks just as surely as when its numerator grows. Items
1, 2, 11, 14, 16, 21, 23 and 29 are keyed to that and cite it.

SPS-2.C.2 names three consequence domains -- political, social, economic -- and
one measure. Items 6, 7, 8, 10, 19, 25 and 30 are keyed to the domains and cite
it; item 7 asks for the SOCIAL one specifically and item 8 for the POLITICAL
one, because a module that only ever asks about budgets teaches one third of the
statement.

WHAT THE CITATION CANNOT SUPPORT. The CED names the dependency ratio and does
not print its formula, so every computational key rests on the standard
construction recorded in the module header:

    total   = (under 15 + 65 and over) / (15-64) x 100
    youth   = (under 15)               / (15-64) x 100
    elderly = (65 and over)            / (15-64) x 100

Two consequences of that construction carry items on their own and are argued
rather than cited. Items 5, 17, 24 and 27 turn on the fact that the TOTAL ratio
adds two unlike groups, so an identical value can describe a very young country
and a very old one -- item 27's table is built to make that undeniable by giving
two countries the same ratio of 70 with opposite compositions. Items 13 and 22
turn on the fixed age cut-offs, which count a working 70-year-old as dependent
and a full-time student of 22 as a worker.

The five table items (26-30) are the computational gate:

  26  the ratio, against four distractors that each compute something else --
      the raw count, a share of the total, the reciprocal, one component alone
  27  two countries, one ratio, opposite compositions
  28  the elderly ratio TRIPLES because both terms move in the raising direction
  29  the largest fertility COLLAPSE belongs to a country whose elderly share is
      still small, which is aging that has been committed to but not yet arrived
  30  both budget columns sum to 100, so only composition is comparable

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. Item 17 is a NOT question -- which
conclusion is not safe -- and its claim says so explicitly, since a negative
stem is where a hurried reader mis-keys.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_9


def _bands(table, label_col, value_cols):
    """Read a three-band age table into {band: {column: value}}."""
    out = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        out[d[label_col]] = {c: num(d[c]) for c in value_cols}
    return out


def q26_total_ratio(table):
    """Total dependency ratio, and the four things it is not."""
    pop = {rowdict(table, r)["Age group"]:
           num(rowdict(table, r)["Population (millions)"]) for r in table["rows"]}
    young, work, old = pop["Under 15"], pop["15-64"], pop["65 and over"]
    ratio = 100 * (young + old) / work
    assert ratio == 50, ratio
    assert young + old == 20 and work == 40, (young, old, work)
    # Each distractor must compute a genuinely different number.
    share_of_total = 100 * (young + old) / (young + work + old)
    reciprocal = 100 * work / (young + old)
    elderly_only = 100 * old / work
    for other in (share_of_total, reciprocal, elderly_only):
        assert abs(other - ratio) > 1, (ratio, other)
    return "50, since 20 million dependents"


def q27_same_ratio_opposite_shape(table):
    """Identical total ratios built from opposite compositions."""
    b = _bands(table, "Age group", ["Country A (millions)", "Country B (millions)"])
    ratios, comps = {}, {}
    for col in ("Country A (millions)", "Country B (millions)"):
        young = b["Under 15"][col]
        work = b["15-64"][col]
        old = b["65 and over"][col]
        ratios[col] = 100 * (young + old) / work
        comps[col] = young / old
    vals = list(ratios.values())
    assert vals[0] == vals[1] == 70, ratios
    # ...and the compositions must be opposite, not merely different.
    a, bb = comps["Country A (millions)"], comps["Country B (millions)"]
    assert a > 1 > bb, comps
    assert a > 5 and bb < 0.5, comps
    return "total dependency ratio of 70"


def q28_elderly_ratio_rising(table):
    """Both terms move in the raising direction, so the ratio triples."""
    series = sorted((num(rowdict(table, r)["Year"]),
                     num(rowdict(table, r)["Population 15-64 (millions)"]),
                     num(rowdict(table, r)["Population 65 and over (millions)"]))
                    for r in table["rows"])
    ratios = [round(100 * old / work) for _, work, old in series]
    assert ratios == [20, 33, 60], ratios
    works = [w for _, w, _ in series]
    olds = [o for _, _, o in series]
    assert all(works[i] > works[i + 1] for i in range(len(works) - 1)), works
    assert all(olds[i] < olds[i + 1] for i in range(len(olds) - 1)), olds
    assert ratios[-1] == 3 * ratios[0], ratios
    # The elderly population alone grows far less than the ratio does.
    assert olds[-1] / olds[0] < ratios[-1] / ratios[0], (olds, ratios)
    return "from 20 to 60 per hundred workers"


def q29_fastest_aging(table):
    """The largest fertility collapse, held against the largest elderly share."""
    fall, old = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        fall[d["Country"]] = round(num(d["Fertility 25 years ago"])
                                   - num(d["Fertility now"]), 2)
        old[d["Country"]] = num(d["Share 65 and over now (%)"])
    steepest = max(fall, key=fall.get)
    assert steepest == "Country Q", fall
    assert fall["Country Q"] == 4.5, fall
    ranked = sorted(fall.values(), reverse=True)
    assert ranked[0] > 5 * ranked[1], ranked
    # The country aging fastest must NOT be the one with the largest elderly
    # share, or the item has no point.
    assert max(old, key=old.get) != steepest, old
    assert old[steepest] < 10, old
    return "fell by 4.5 children per woman"


def q30_budget_composition(table):
    """Two budget columns, both summing to 100; the age-related share decides."""
    x = numcol(table, "Country X (% of budget)")
    y = numcol(table, "Country Y (% of budget)")
    assert sum(x) == 100 and sum(y) == 100, (sum(x), sum(y))
    cats = column(table, "Spending category")
    pens = cats.index("Pensions")
    health = cats.index("Health care for those over 65")
    edu = cats.index("Primary and secondary education")
    x_age = x[pens] + x[health]
    y_age = y[pens] + y[health]
    assert y_age == 53 and x_age == 12, (x_age, y_age)
    assert y_age > 4 * x_age, (x_age, y_age)
    # The younger country must spend more on schooling, or the contrast is muddy.
    assert x[edu] > y[edu], (x[edu], y[edu])
    return "53 percent of its budget"


CLAIMS = [
 ("Birth rates, death rates, and life expectancy",
  "EK SPS-2.C.1 names exactly these three determinants of population aging. Aging is a change in the SHARE of a population that is old, so it depends on how many people are added at the bottom as much as on how long those already alive survive."),

 ("smaller cohort at the bottom raises every older cohort's share",
  "EK SPS-2.C.1 lists birth rates first among the determinants of aging. A proportion rises either because its numerator grows or because its denominator shrinks, and sustained low fertility shrinks the denominator every single year."),

 ("divided by the population aged 15 to 64",
  "EK SPS-2.C.2 names the dependency ratio as a consequence measure without printing its formula, and the standard construction places both dependent age groups over the working ages. Using total population as the denominator would give a share rather than a ratio of dependents to workers."),

 ("40 million dependents are supported by 60 million",
  "Adding the two dependent bands gives 40 million against 60 million of working age, which is about 67 per hundred workers. The distractors compute a share of the total population, one component ratio alone, and the reciprocal of the ratio asked for."),

 ("one ratio implies schools and the other implies pensions",
  "The total ratio adds two very different groups into one figure, so an identical value is compatible with opposite compositions. EK SPS-2.C.2 names the ratio among the consequences of aging, and reading it without decomposing it is how a young country and an old one get confused."),

 ("working-age population that is not growing",
  "EK SPS-2.C.2 names economic consequences among the effects of an aging population. Pension and health systems transfer resources from workers to the retired, so a rising elderly share against a flat working-age population raises the transfer each worker must make."),

 ("adult child provides daily care for an aging parent",
  "EK SPS-2.C.2 lists political, social and economic consequences as three separate domains. Budgets, tax revenue and labour shortages are economic and the electorate's composition is political, while the reorganization of family life around care is the social case."),

 ("older voters turn out in large numbers",
  "EK SPS-2.C.2 names political consequences separately from social and economic ones. Where an age group is both large and reliably participating, the policies serving it acquire a constituency that makes reform electorally costly."),

 ("moves people from the dependent group into the working-age group",
  "The ratio's denominator is the population counted as of working age, so redefining where that band ends adds to the denominator and subtracts from the numerator simultaneously. Larger pensions, more care places and longer schooling change costs or the numerator instead."),

 ("enter the working-age population immediately",
  "Both instruments act on the working-age population but on completely different timescales, and an aging country's shortage is present rather than future. EK SPS-2.C.2's economic consequences are what the country is trying to relieve, and only one lever relieves them now."),

 ("even though no one lives longer",
  "EK SPS-2.C.1 makes birth rates a determinant of aging in their own right. A shrinking base raises the share held by every cohort above it, so a population can age rapidly with no change at all in how long its members live."),

 ("relates the population 65 and over to the population aged 15 to 64",
  "EK SPS-2.C.2 names the dependency ratio, and the elderly component is the part isolating the group in question. The total ratio mixes in children, whose costs fall on different budgets and end at a known age."),

 ("age cut-offs are fixed",
  "The construction assumes everyone between two ages works and nobody outside them does, which is an approximation rather than a measurement. Where labour force participation departs from that assumption, the measured ratio and the real burden move apart."),

 ("Sustained low fertility together with rising life expectancy",
  "EK SPS-2.C.1 names birth rates, death rates and life expectancy as the determinants, and only one combination of them raises median age while holding the total steady. Fewer entrants at the bottom and more survivors at the top both push the median upward."),

 ("working-age population can shrink even while total population is stable",
  "The working-age band is fed at one end and drained at the other, so its size depends on the relative sizes of the entering and exiting cohorts rather than on the total. A large cohort leaving against a small one arriving shrinks it whatever the total does."),

 ("takes their future children with them",
  "At the subnational scale migration reshapes age structure faster than fertility or mortality can, and it is strongly selective by age. The district loses the cohort that would have had children as well as the cohort itself, which ages it twice over."),

 ("has an older population",
  "This is a NOT question: the key is the inference that cannot safely be drawn. A high total ratio can arise from many children or many elderly, so the total alone does not identify which, and EK SPS-2.C.2's measure has to be decomposed before it can support a claim about age."),

 ("Admitting a large number of working-age immigrants",
  "The ratio compares two age groups, so adding people to the working-age band lowers it directly. Raising births adds to the numerator now, extending life expectancy adds to it later, and better care or larger pensions change costs without changing any count."),

 ("Current workers' contributions fund current pensions",
  "EK SPS-2.C.2 names economic consequences including the dependency ratio, and a pay-as-you-go system makes that ratio the system's own arithmetic. When each pensioner is supported by fewer workers, contributions, benefits or the retirement age has to move."),

 ("still under 10 percent but its fertility has been below replacement",
  "EK SPS-2.C.1 makes low fertility a determinant of aging that acts with a long lag, so the commitment to an older future is made years before the older population appears. A small elderly share with entrenched low fertility is that early stage exactly."),

 ("determined by birth rates as well as by death rates",
  "EK SPS-2.C.1 lists birth rates among the determinants of aging alongside death rates and life expectancy. The remark compresses the first determinant into a sentence, and it is worth making because the popular account of aging omits it."),

 ("provided older workers can actually find and keep work",
  "Moving the age boundary is an arithmetic change to the ratio, and whether it changes the underlying economics depends on employment at those ages. Stating that condition is what separates an honest answer from one confusing a definition with an outcome."),

 ("both began at different levels and moved at different times",
  "EK SPS-2.C.1's three determinants have all moved in the aging direction across most of the world, so the differences between regions are of timing and starting point rather than of direction. That is why the process is nearly universal but nowhere synchronized."),

 ("pressure on schools rather than on pensions",
  "Decomposing the total ratio identifies the source of the burden, and a youth component nearly six times the elderly one places the country firmly at the young end. EK SPS-2.C.2 names the ratio as the measure, and reading its parts is what makes it informative."),

 ("Raising the retirement age, funding home care",
  "EK SPS-2.C.2 names political, social and economic consequences, and the three measures listed address one of each: labour supply, the burden carried by families, and legislated entitlement. A response confined to one domain leaves the other two untouched."),

 ("50, since 20 million dependents",
  "Recomputed from the table: nine plus eleven million dependents against forty million of working age is 50 per hundred workers. The verifier confirms that the share of total population, the reciprocal and the elderly component alone each give a materially different number, so no distractor is accidentally right.",
  q26_total_ratio),

 ("total dependency ratio of 70",
  "Recomputed from the table: both countries carry 21 million dependents against 30 million of working age, so both ratios are exactly 70, yet one has six children per elderly person and the other has the reverse. The verifier asserts the compositions are opposite rather than merely different.",
  q27_same_ratio_opposite_shape),

 ("from 20 to 60 per hundred workers",
  "Recomputed from the table: the elderly ratio runs 20, 33 and 60 per hundred, tripling over forty years, because the working-age population falls at every step while the elderly population rises at every step. The verifier confirms the elderly population alone grows by less than the ratio does.",
  q28_elderly_ratio_rising),

 ("fell by 4.5 children per woman",
  "Recomputed from the table: fertility falls of 0.1, 4.5, 0.1 and 0.8 make one country's collapse more than five times any other's, while its elderly share is still under ten percent. EK SPS-2.C.1 makes birth rates a determinant of aging, so a fall of that size commits the country to a rapid rise ahead of it.",
  q29_fastest_aging),

 ("53 percent of its budget",
  "Recomputed from the table: both columns sum to 100 percent, so only composition is comparable, and pensions plus elderly health care come to 53 percent against 12 in the other country. The verifier also confirms the younger country spends more on schooling, which is the same contrast seen from the other end.",
  q30_budget_composition),
]

hg_check.check(g2_9, CLAIMS, per_topic=30, n_choices=5)
