"""Key audit for AP HUMAN GEOGRAPHY 2.5 The Demographic Transition Model.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED, AND WHAT CANNOT. IMP-2.B contributes two essential-knowledge
statements to this topic (the third, on Malthus, belongs to 2.6):

    IMP-2.B.1  The demographic transition model can be used to explain
               population change over time.
    IMP-2.B.2  The epidemiological transition explains causes of changing
               death rates.

Both NAME a model and neither DESCRIBES one. So a citation here can support only
two things -- that the demographic model is about population change over time,
and that the epidemiological transition is about causes of changing death rates.
Every key that turns on what a particular stage looks like rests instead on the
model as this course teaches it, set out in full in the module header. Those
claims say which stage description they depend on rather than attaching a code
to content the CED never printed.

Two framings this module is deliberate about:

  * Stage 5 is presented throughout as an EXTENSION of the model rather than as
    one of its original stages, because textbooks differ on whether the model
    has four stages or five and the CED settles nothing. Items 8 and 29 use the
    stage but phrase it as the case of births falling below deaths, which is
    true under either convention.
  * The pivotal structural fact -- mortality falls FIRST and fertility LATER, so
    the gap between the curves is the growth -- carries items 2, 6, 14, 19, 23
    and 27. Getting this backwards is the single most common student error in
    the topic, which is why item 19 asks about it directly.

The model's limitations are examinable content and items 15, 16, 20 and 25 carry
them: it was generalized from European history, it contains no migration term,
and its stages are a sequence rather than a timetable.

The five table items (26-30) are the computational gate, and each is built so
that a single striking column gives the wrong answer:

  26  the country with the HIGHEST birth rate has the LOWEST natural increase
      but one, because its death rate is nearly as high
  27  the interval is identified by which of the two rates falls further, not
      by which rates are lowest
  28  both columns sum to 100 percent, so composition is comparable and totals
      are not
  30  the growth RATE peaks and falls while the POPULATION more than triples

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. Item 26 and item 29 each carry a distractor
whose premise is deliberately false ("its natural increase is the highest",
"none of them, since a population cannot decline"); the recomputes assert those
premises really are false, so a later edit to the tables cannot quietly make a
distractor true.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_5


def q26_stage_two(table):
    """High births with an already-fallen death rate; the highest CBR is a trap."""
    rni, births, deaths = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        b = num(d["Crude birth rate (per 1,000)"])
        m = num(d["Crude death rate (per 1,000)"])
        births[d["Country"]] = b
        deaths[d["Country"]] = m
        rni[d["Country"]] = (b - m) / 10
    assert rni == {"Country A": 3.0, "Country B": 0.4,
                   "Country C": 0.4, "Country D": -0.3}, rni
    fastest = max(rni, key=rni.get)
    assert fastest == "Country A", rni
    # The trap: the highest birth rate is NOT the fastest-growing country,
    # because that country's death rate has not yet fallen.
    top_birth = max(births, key=births.get)
    assert top_birth != fastest, births
    assert deaths[top_birth] > 30, deaths
    # And the key's own figure must hold.
    assert births["Country A"] >= 35 and deaths["Country A"] <= 12, (births, deaths)
    return "3.0 percent"


def q27_stage_crossover(table):
    """The interval where the larger fall switches from deaths to births."""
    rows = sorted((num(rowdict(table, r)["Year"]),
                   num(rowdict(table, r)["Crude birth rate (per 1,000)"]),
                   num(rowdict(table, r)["Crude death rate (per 1,000)"]))
                  for r in table["rows"])
    intervals = []
    for i in range(len(rows) - 1):
        y0, b0, d0 = rows[i]
        y1, b1, d1 = rows[i + 1]
        intervals.append((int(y0), int(y1), b0 - b1, d0 - d1))
    # First interval: mortality falls far more than fertility.
    assert intervals[0][2] == 1 and intervals[0][3] == 15, intervals
    # Second interval: the switch -- fertility now falls far more.
    assert intervals[1][2] == 13 and intervals[1][3] == 4, intervals
    assert intervals[1][2] > intervals[1][3], intervals
    first_switch = next(iv for iv in intervals if iv[2] > iv[3])
    assert (first_switch[0], first_switch[1]) == (1970, 1990), intervals
    return "Between 1970 and 1990"


def q28_cause_composition(table):
    """Two composition columns, both summing to 100, so only shares compare."""
    x = numcol(table, "Country X (% of deaths)")
    y = numcol(table, "Country Y (% of deaths)")
    assert sum(x) == 100 and sum(y) == 100, (sum(x), sum(y))
    causes = column(table, "Cause of death")
    inf = causes.index("Infectious and parasitic disease")
    cardio = causes.index("Cardiovascular disease")
    cancer = causes.index("Cancer")
    assert x[inf] == 48 and y[inf] == 6, (x[inf], y[inf])
    assert x[inf] > 5 * y[inf], (x[inf], y[inf])
    # The chronic-disease distractor's own arithmetic must be right so that only
    # its inference is wrong.
    assert y[cardio] + y[cancer] == 71, (y[cardio], y[cancer])
    return "48 percent of its deaths"


def q29_decline_stage(table):
    """Exactly one country has more deaths than births, and it is the oldest."""
    natural, old = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        natural[d["Country"]] = (num(d["Crude birth rate (per 1,000)"])
                                 - num(d["Crude death rate (per 1,000)"]))
        old[d["Country"]] = num(d["Share aged 65+ (%)"])
    declining = [c for c in natural if natural[c] < 0]
    assert declining == ["Country J"], natural
    assert max(old, key=old.get) == "Country J", old
    assert old["Country J"] == 23, old
    # The distractor claiming no population can decline must be false, which the
    # negative value above already establishes; assert it explicitly.
    assert natural["Country J"] == -3, natural
    return "births fall short of its deaths"


def q30_rate_versus_total(table):
    """The growth rate peaks and falls while the population more than triples."""
    series = sorted((num(rowdict(table, r)["Year"]),
                     num(rowdict(table, r)["Population (millions)"]),
                     num(rowdict(table, r)["Rate of natural increase (%)"]))
                    for r in table["rows"])
    pops = [s[1] for s in series]
    rates = [s[2] for s in series]
    # The rate must rise then fall...
    peak = rates.index(max(rates))
    assert 0 < peak < len(rates) - 1, rates
    assert all(rates[i] < rates[i + 1] for i in range(peak)), rates
    assert all(rates[i] > rates[i + 1] for i in range(peak, len(rates) - 1)), rates
    # ...while the population rises throughout and more than triples.
    assert all(pops[i] < pops[i + 1] for i in range(len(pops) - 1)), pops
    assert pops[-1] > 3 * pops[0], pops
    return "more than tripled"


CLAIMS = [
 ("changing relationship between a population's birth and death rates",
  "EK IMP-2.B.1 states that the demographic transition model can be used to explain population change over time, and the model does so by tracking two rates against each other. Migration, distribution, food supply and urbanization are the subjects of other models in this course."),

 ("death rate has fallen sharply while the birth rate is still high",
  "Natural increase is the gap between the two rates rather than the level of either, and the model's second stage is where that gap is widest. Both rates are high in the first stage, so the gap opens only once mortality has fallen and fertility has not yet followed."),

 ("high fertility is offset by high and unstable mortality",
  "The first stage's signature is not merely a high birth rate but a death rate that is high AND volatile, so growth in good years is cancelled in bad ones. Removing that volatility is precisely what the move into the second stage consists of."),

 ("Clean water, sanitation, improved nutrition",
  "The mortality decline opening the second stage acts on the causes of death that are cheapest to prevent -- infectious and diarrhoeal disease and undernutrition. Every other option acts on fertility or on the old, and neither of those moves the death rate first."),

 ("fertility falls and growth decelerates",
  "The third stage is defined by the second of the two declines: mortality has already fallen and fertility is now following it down. The gap between the curves is narrowing, which is deceleration rather than either maximum growth or stability."),

 ("Urbanization together with expanded education and employment for women",
  "Sanitation and vaccination lower mortality, which is the previous stage's mechanism. The fertility decline is driven by what a child costs and what alternatives adults have, and city living with women's schooling and paid work is the standard pairing."),

 ("both rates are low and natural increase is close to zero",
  "A near-zero natural increase can arise from two high rates or two low ones, and the low pair is the fourth stage. The stem specifies that both rates are low, which is what rules out the first stage despite its similarly small gap."),

 ("birth rate falls below the death rate",
  "The extension of the model to a fifth stage records fertility falling not merely to replacement but below it, so deaths outnumber births in a population that is also aging. The death rate rises there because the population is old, not because conditions have worsened."),

 ("high fertility and recently reduced mortality produce very large young cohorts",
  "A wide base means many births, and each cohort being sharply smaller than the one beneath it means those births are recent and increasing. That combination belongs to the stage in which mortality has already fallen and fertility has not."),

 ("leading causes of death change as a society develops",
  "EK IMP-2.B.2 states that the epidemiological transition explains causes of changing death rates. It is the companion to the demographic model, answering what people die of rather than how many of them die."),

 ("Infectious and parasitic diseases together with famine",
  "EK IMP-2.B.2 makes the epidemiological transition an account of changing causes of death, and its opening stage is the one commonly called pestilence and famine. Chronic disease can dominate only where enough people survive to old age to die of it."),

 ("more people survived to the ages when chronic disease kills",
  "EK IMP-2.B.2's transition is about composition rather than level: removing the causes that kill the young leaves the causes that kill the old as the largest share. Life expectancy rises even as the leading causes come to sound more serious."),

 ("infectious disease re-emerges",
  "The proposed extension of EK IMP-2.B.2's transition covers exactly these mechanisms -- pathogens evolving faster than treatments, and connectivity moving them faster than containment. It is a proposed stage rather than an established one, which is why the key is phrased as a possibility."),

 ("Mortality falls before fertility does",
  "The whole shape of the model follows from the two declines being separated in time, since the interventions that cut deaths are cheaper and faster acting than the social changes that cut births. The population added during that lag does not disappear when fertility finally falls."),

 ("generalized from the European experience and does not account for migration",
  "EK IMP-2.B.1 says the model CAN BE USED to explain population change, which is a claim about usefulness rather than universal law. Its two best-documented limits are its origin in one region's history and its silence about migration, which for many countries is the largest component of change."),

 ("a sequence of changes, not a fixed timetable",
  "EK IMP-2.B.1 offers the model as an explanatory tool rather than a schedule. Countries transitioning later can import medicine and contraception that the earlier ones spent a century developing, so the same sequence runs at very different speeds."),

 ("each new cohort is no larger than the last",
  "A stable total conceals a changing shape: with births flat and survival high, a population accumulates in its older cohorts year after year. Aging is therefore a consequence of the transition rather than a separate process running alongside it."),

 ("describing which causes of death recede",
  "EK IMP-2.B.1 makes the demographic model an account of population change and EK IMP-2.B.2 makes the epidemiological transition an account of causes of changing death rates. One supplies the mechanism sitting behind the other's mortality curve."),

 ("Birth rates are high in both stages",
  "The first two stages share a high birth rate, and the passage between them is entirely a mortality event. Treating the second stage as the high-fertility stage misses that fertility has not yet moved and misidentifies what is causing the growth."),

 ("tracks only births and deaths",
  "EK IMP-2.B.1 makes the model an account of population change through the two rates it plots, and migration is a third component it does not carry. Where migration dominates, the model can describe natural increase correctly and still get the total badly wrong."),

 ("Cardiovascular disease and cancer together account for most deaths",
  "EK IMP-2.B.2's transition is diagnosed from the composition of deaths, and chronic disease can dominate only once enough people survive to the ages at which it kills. High infant mortality, famine, high fertility and rapid growth all point to an earlier stage."),

 ("population has aged so much that a crude death rate rises",
  "A crude rate is deaths divided by the whole population, so a population weighted toward the old ages produces more deaths per thousand regardless of medical improvement. That is why a late-transition country can show a rising death rate meaning the opposite of what it appears to."),

 ("Near-stability, then rapid growth, then decelerating growth",
  "The model's shape follows from the two rates converging, separating and converging again: a small gap in the first stage, a wide one in the second, a narrowing one in the third and a small gap once more in the fourth. The population ends far larger than it began."),

 ("identifies which causes of death dominate",
  "EK IMP-2.B.2 makes the epidemiological transition an account of the CAUSES of changing death rates, which is exactly what a spending decision needs. The demographic model plots the rate itself and is silent about what is producing it."),

 ("policies, epidemics, wars, and migration that the model does not contain",
  "EK IMP-2.B.1 offers the model as something that can be used to explain change, which is a claim about explanatory value rather than inevitability. Its accuracy for any given country depends on whether that country's circumstances resemble the histories it was generalized from."),

 ("3.0 percent",
  "Recomputed from the table: natural increase is 3.0, 0.4, 0.4 and minus 0.3 percent, so the country with the highest birth rate is nowhere near the fastest growing. The verifier confirms that country's death rate is still above 30 per 1,000, which is what places it in the first stage rather than the second.",
  q26_stage_two),

 ("Between 1970 and 1990",
  "Recomputed from the table: the death rate falls 15 points against the birth rate's 1 in the first interval, and the birth rate falls 13 against the death rate's 4 in the second. The verifier locates the first interval in which the larger fall switches from mortality to fertility, which is what marks the passage between the stages.",
  q27_stage_crossover),

 ("48 percent of its deaths",
  "Recomputed from the table: both columns sum to 100 percent, so only composition is comparable and nothing about the number of deaths can be read. Infectious disease causes nearly half of all deaths in one country against one in seventeen in the other, which is the clearest marker of the earlier stage.",
  q28_cause_composition),

 ("births fall short of its deaths",
  "Recomputed from the table: exactly one country records more deaths than births, at 8 against 11 per 1,000, and that same country carries the largest share over 65 at 23 percent. The pairing matters because its rising crude death rate reflects an old age structure rather than worsening health.",
  q29_decline_stage),

 ("more than tripled",
  "Recomputed from the table: the rate rises to 2.6 percent and then falls to 0.6 while the population goes from 20 to 63 million. The verifier asserts the rate genuinely peaks in the middle of the series and that the population rises at every step, since the gap between a rate and a total is the whole point of the item.",
  q30_rate_versus_total),
]

hg_check.check(g2_5, CLAIMS, per_topic=30, n_choices=5)
