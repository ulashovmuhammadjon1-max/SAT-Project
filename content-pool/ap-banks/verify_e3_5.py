"""Key audit for AP ENVIRONMENTAL SCIENCE 3.5 Population Growth and Resource
Availability.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-3.F.1  Population growth is limited by environmental factors, especially by
           the available resources and space.
                   -- items 1, 2, 21, 22, 26, 29, 30
ERT-3.F.2  Resource availability and the total resource base are limited and
           finite over all scales of time.
                   -- items 3, 4, 23, 24, 29, 30
ERT-3.F.3  When the resources needed by a population for growth are abundant,
           population growth usually accelerates.
                   -- items 5, 6, 13, 14, 15, 25, 29, 30
ERT-3.F.4  When the resource base of a population shrinks, the increased
           potential for unequal distribution of resources will ultimately
           result in increased mortality, decreased fecundity, or both,
           resulting in population growth declining to, or below, carrying
           capacity.
                   -- items 7, 8, 9, 10, 11, 16, 17, 18, 19, 20, 27, 28, 29, 30

THE TWO HEDGES ARE KEYED AS HEDGES. ERT-3.F.3 says growth USUALLY accelerates
(item 6) and ERT-3.F.4 says increased mortality, decreased fecundity, OR BOTH
(item 10) and growth declining TO, OR BELOW, carrying capacity (item 11). No key
anywhere in the module hardens either one into a promise.

TWO ITEMS TURN ON A SWAP, so their anchors carry BOTH clauses rather than one.
Item 12 is the boundary against topic 3.4 and its rejected option is this topic's
own claim exchanged with 3.4's; item 16 and item 27 each have a distractor that
reverses one of two co-varying directions. An anchor naming only the first clause
would match the swap as well as the key -- the defect already found once in
verify_e2_1.py.

BOUNDARY WITH 3.4. Overshoot (ERT-3.D.1) and the dieback that follows it
(ERT-3.E.1) belong to topic 3.4 Carrying Capacity. Nothing here keys either; item
12 states the line rather than crossing it, and item 19's key speaks of growth
declining to or below capacity in ERT-3.F.4's own words, not of a dieback.

DATA ITEMS: 13 to 27 carry tables, fifteen of them, because the suggested skill
for this topic is 6.B, apply appropriate mathematical relationships. Every keyed
gain, difference, percentage, density and running total is recomputed below from
that table alone, and each check also falsifies the distractors it can.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Several checks here read a
co-varying gradient that a column reversal preserves -- reversing every numeric
column at once leaves "resources up, growth up" intact -- so for those e_check
flattens the table next and the check fails, because a flat column has no
gradient at all. ``python3 verify_e3_5.py --selftest`` is the same run; the
controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e3_5

SUPPLY = "Resource supply (index)"
START = "Population at the start of the period"
END = "Population at the end of the period"
BASE = "Resource base (index)"
DEATHS = "Deaths per thousand individuals"
OFFSPRING = "Offspring per female per year"
POP = "Population"
K = "Carrying capacity (K)"
AREA = "Floor area available (square metres)"
REACHED = "Population the colony reached"
STOCK = "Stock of the resource at the start (thousand tonnes)"
USED = "Amount used during the decade (thousand tonnes)"
RELNEED = "Resource supply relative to need (percent)"
GROWTH = "Annual growth rate (percent)"
SHARE = "Share of the food taken by the largest quarter of the herd (percent)"
DEATHS2 = "Deaths per thousand individuals"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    """Every named column, reordered so ``key_header`` ascends."""
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def _gains(table):
    return [e - s for s, e in zip(cg.col(table, START), cg.col(table, END))]


def q13(table, item):
    supply = cg.col(table, SUPPLY)
    gains = _gains(table)
    order = sorted(range(len(supply)), key=lambda i: supply[i])
    g = [gains[i] for i in order]
    assert _rises(g), f"the gain must rise with the resource supply; got {g}"
    assert min(g) > 0, f"no period may lose individuals; got {g}"
    assert len(set(g)) == len(g), "'the same number in every period' must be false"
    return (f"ordered by resource supply the four periods add {g} individuals, "
            "strictly increasing and never negative")


def q14(table, item):
    labs = cg.labels(table)
    start = cg.col(table, START)
    end = cg.col(table, END)
    pct = [(e - s) / s * 100 for s, e in zip(start, end)]
    j = labs.index("Period 4")
    assert 75 <= pct[j] <= 85, f"the fourth period must grow about 80 percent; got {pct[j]}"
    others = [p for i, p in enumerate(pct) if i != j]
    assert all(abs(p - pct[j]) > 10 for p in others), \
        f"no other period may grow by nearly as much; got {pct}"
    return (f"the fourth period runs {start[j]:.0f} to {end[j]:.0f}, a gain of "
            f"{end[j] - start[j]:.0f}, which is {pct[j]:.0f} percent of the starting count")


def q15(table, item):
    labs = cg.labels(table)
    gains = _gains(table)
    fewest = labs[min(range(len(gains)), key=lambda i: gains[i])]
    assert fewest == "Period 1", f"the smallest gain must belong to Period 1; got {fewest}"
    assert list(gains).count(min(gains)) == 1, \
        "'all four periods added the same number' must be false"
    return (f"the four periods add {gains} individuals and the smallest belongs "
            f"to {fewest}")


def q16(table, item):
    deaths, offspring = _by(table, BASE, DEATHS, OFFSPRING)
    # Named booleans, not indexes into parallel tuples: the two directions are
    # opposite and a swapped comparison would read as parallel and not be.
    deaths_rise_as_base_shrinks = _falls(deaths)
    offspring_fall_as_base_shrinks = _rises(offspring)
    assert deaths_rise_as_base_shrinks, \
        f"sorted by a rising resource base, deaths must fall; got {deaths}"
    assert offspring_fall_as_base_shrinks, \
        f"sorted by a rising resource base, offspring must rise; got {offspring}"
    return (f"ordered by a rising resource base the deaths read {deaths} per thousand "
            f"and the offspring per female {offspring}, so as the base SHRANK deaths "
            "rose and offspring fell")


def q17(table, item):
    deaths = cg.col(table, DEATHS)
    change = deaths[-1] - deaths[0]
    assert change == 140, f"the death rate must rise by 140 per thousand; got {change}"
    assert change != deaths[-1] and change != deaths[0], \
        "the change must not coincide with either endpoint"
    return (f"deaths per thousand run {deaths[0]:.0f} to {deaths[-1]:.0f}, a rise of "
            f"{change:.0f}")


def q18(table, item):
    off = cg.col(table, OFFSPRING)
    change = off[0] - off[-1]
    assert abs(change - 2.6) < 1e-9, f"offspring per female must fall by 2.6; got {change}"
    assert change != off[0] and change != off[-1], \
        "the fall must not coincide with either endpoint"
    return (f"offspring per female run {off[0]} to {off[-1]}, a fall of {change:.1f}")


def q19(table, item):
    pop = cg.col(table, POP)
    cap = cg.col(table, K)
    assert len(set(cap)) == 1, f"one carrying capacity must apply throughout; got {cap}"
    rose_above = max(pop) > cap[0]
    ended_below_capacity = pop[-1] < cap[0]
    ended_below_start = pop[-1] < pop[0]
    assert rose_above, f"the population must exceed the capacity at some point; got {pop}"
    assert ended_below_capacity, f"the population must end below the capacity; got {pop[-1]}"
    assert ended_below_start, \
        f"the population must end below where it began; got {pop[0]} then {pop[-1]}"
    return (f"the population runs {pop} against a constant capacity of {cap[0]:.0f}, "
            f"passing above it and finishing at {pop[-1]:.0f}, below both the capacity "
            f"and its own starting {pop[0]:.0f}")


def q20(table, item):
    labs = cg.labels(table)
    short = [k - p for p, k in zip(cg.col(table, POP), cg.col(table, K))]
    worst = labs[max(range(len(short)), key=lambda i: short[i])]
    assert worst == "Year 13", \
        f"the largest shortfall must belong to the thirteenth year; got {worst}"
    assert short.count(max(short)) == 1, "the largest shortfall must be unique"
    assert max(short) > 0, "'never below the carrying capacity' must be false"
    return (f"the shortfalls against the capacity are {short} individuals, negative "
            f"where the population stood above it, and the largest belongs to {worst}")


def q21(table, item):
    (reached,) = _by(table, AREA, REACHED)
    assert _rises(reached), f"the population reached must rise with floor area; got {reached}"
    assert len(set(reached)) == len(reached), "'every colony reached the same population' must be false"
    return (f"ordered by floor area the colonies reach {reached} individuals, "
            "strictly increasing")


def q22(table, item):
    area = cg.col(table, AREA)
    reached = cg.col(table, REACHED)
    density = [r / a for a, r in zip(area, reached)]
    assert all(19 <= d <= 21 for d in density), \
        f"every density must be about twenty per square metre; got {density}"
    assert max(density) - min(density) < 1, f"the densities must be nearly equal; got {density}"
    assert len(set(reached)) == len(reached), "the populations reached must differ"
    assert len(set(area)) == len(area), "the floor areas must differ"
    return (f"dividing each population reached by its floor area gives "
            f"{[round(d, 1) for d in density]} individuals per square metre, near twenty "
            "in every enclosure while both the areas and the populations differ")


def q23(table, item):
    stock = cg.col(table, STOCK)
    used = cg.col(table, USED)
    for i in range(len(stock) - 1):
        assert abs(stock[i] - used[i] - stock[i + 1]) < 1e-9, \
            f"decade {i + 1}: {stock[i]} less {used[i]} must leave {stock[i + 1]}"
    assert _falls(stock), f"the stock must fall in every decade; got {stock}"
    assert abs(stock[-1] - used[-1]) < 1e-9, \
        f"the last decade's use must exhaust the stock; {stock[-1]} against {used[-1]}"
    return (f"the stock runs {stock} thousand tonnes while {used} are used, each decade's "
            "use accounting exactly for the fall to the next, and the last exhausting it")


def q24(table, item):
    stock = cg.col(table, STOCK)
    used = cg.col(table, USED)
    total = sum(used)
    assert abs(total - stock[0]) < 1e-9, \
        f"the total used must equal the opening stock; {total} against {stock[0]}"
    assert total != 2 * stock[0] and total != used[-1], \
        "the total must not coincide with twice the opening stock or one decade's use"
    return (f"the four decades use {used}, which sum to {total:.0f} thousand tonnes, "
            f"exactly the opening stock of {stock[0]:.0f}")


def q25(table, item):
    (growth,) = _by(table, RELNEED, GROWTH)
    assert _rises(growth), \
        f"growth must rise with the resources available relative to need; got {growth}"
    assert len(set(growth)) == len(growth), "'all four grew at the same rate' must be false"
    return (f"ordered by resources relative to need the growth rates read {growth} percent "
            "a year, strictly increasing")


def q26(table, item):
    labs = cg.labels(table)
    growth = cg.col(table, GROWTH)
    relneed = cg.col(table, RELNEED)
    shrinking = [lab for lab, g in zip(labs, growth) if g < 0]
    assert shrinking == ["Population 4"], \
        f"exactly the fourth population must be shrinking; got {shrinking}"
    poorest = labs[min(range(len(relneed)), key=lambda i: relneed[i])]
    assert poorest == shrinking[0], \
        f"the shrinking population must also be the worst supplied; got {poorest}"
    return (f"the growth rates are {growth} percent a year, negative in exactly one case, "
            f"{shrinking[0]}, which is also the population whose resources fall furthest "
            "short of its needs")


def q27(table, item):
    share = cg.col(table, SHARE)
    deaths = cg.col(table, DEATHS2)
    # Named booleans rather than a comparison between parallel tuples.
    sharing_grew_more_unequal = _rises(share)
    death_rate_rose = _rises(deaths)
    assert sharing_grew_more_unequal, \
        f"the share taken by the largest quarter must rise through the shortage; got {share}"
    assert death_rate_rose, f"the death rate must rise through the shortage; got {deaths}"
    return (f"through the shortage the largest quarter takes {share} percent of the food "
            f"while deaths run {deaths} per thousand, so the sharing grew more unequal AND "
            "the death rate rose")


CLAIMS = [
 ("especially the available resources and space",
  "ERT-3.F.1, near verbatim: population growth is limited by environmental factors, especially by the available resources and space. Each rejected option names a single limit the statement does not single out, or denies that growth is limited at all."),
 ("available resources and space",
  "ERT-3.F.1 names environmental factors in general and then singles out two of them with the word especially. The rejected pairs are conditions the course treats elsewhere but that this statement does not name."),
 ("limited and finite over all scales of time",
  "ERT-3.F.2, near verbatim: resource availability and the total resource base are limited and finite over all scales of time. Each rejected option exempts one timescale or all of them."),
 ("however long or short",
  "ERT-3.F.2 applies limited and finite OVER ALL SCALES OF TIME, so no interval is exempted. The statement says nothing about measurement intervals, comparisons between resources, renewal or spatial variation."),
 ("usually accelerates",
  "ERT-3.F.3, near verbatim: when the resources needed by a population for growth are abundant, population growth usually accelerates. Acceleration is the direction the statement gives and each rejected option reverses or replaces it."),
 ("the usual result rather than one guaranteed",
  "ERT-3.F.3 is written with USUALLY, which commits the framework to the direction of the effect while stopping short of a rule without exceptions. Hardening it into every case is stronger than the statement."),
 ("potential for unequal distribution",
  "ERT-3.F.4 states that when the resource base of a population shrinks, it is the increased POTENTIAL FOR UNEQUAL DISTRIBUTION of resources that will ultimately have consequences. Every rejected option names a quantity the statement has fall, or does not mention."),
 ("Increased mortality, decreased fecundity, or both",
  "ERT-3.F.4, near verbatim: the increased potential for unequal distribution will ultimately result in increased mortality, decreased fecundity, or both. Both named changes work against the population and each rejected option reverses at least one direction."),
 ("declining to, or below, carrying capacity",
  "ERT-3.F.4 ends by stating that the result is population growth declining to, or below, carrying capacity. Growth is what declines and the carrying capacity is what it is measured against."),
 ("Either change alone",
  "ERT-3.F.4's phrase increased mortality, decreased fecundity, OR BOTH admits each change on its own and admits the two together, and fixes no order between them."),
 ("may end up under the carrying capacity",
  "ERT-3.F.4 writes declining TO, OR BELOW, carrying capacity, which admits both landing points. A promise of settling exactly at the capacity is stronger than the statement and the other options reverse it."),
 # Both clauses, in order: the rejected option is this topic's claim and 3.4's
 # exchanged with one another, so an anchor naming one clause matches both.
 ("how resource availability changes the rate of population growth, while that statement is about what follows",
  "ERT-3.F.1 to ERT-3.F.4 concern what limits growth and what abundance or shortage does to its rate. ERT-3.D.1 and ERT-3.E.1, in the carrying capacity topic, concern a population exceeding its capacity and the dieback that follows. The two statements begin at different points."),
 ("added more individuals in each successive period",
  "Recomputed in q13 above: ordered by resource supply the four periods add 40, 120, 330 and 790 individuals, strictly increasing. ERT-3.F.3 states that when the resources needed for growth are abundant, population growth usually accelerates."),
 ("About 80 percent",
  "Recomputed in q14 above: 1,780 less 990 is 790, and 790 divided by 990 is about 0.80. The rejected values are the growth rates of the other three periods, each more than ten points away."),
 ("Period 1",
  "Recomputed in q15 above: the four gains are 40, 120, 330 and 790 individuals and the smallest is unique and belongs to the period of lowest resource supply, which is what ERT-3.F.3 connects to the slowest growth."),
 # Both clauses: a distractor reverses each direction, so either half alone matches it.
 ("Deaths rose and offspring per female fell",
  "Recomputed in q16 above: ordered by a rising resource base the deaths fall and the offspring rise, so as the base SHRANK the deaths rose and the offspring fell. ERT-3.F.4 states that a shrinking resource base ultimately results in increased mortality, decreased fecundity, or both, and here it is both."),
 ("rose by 140 per thousand",
  "Recomputed in q17 above: deaths per thousand run 40 to 180, a rise of 140, which is neither endpoint. ERT-3.F.4 names increased mortality among the results of a shrinking resource base."),
 ("fell by 2.6",
  "Recomputed in q18 above: offspring per female run 3.2 to 0.6, a fall of 2.6, which is neither endpoint. ERT-3.F.4 names decreased fecundity as the other result of a shrinking resource base."),
 ("rose above the carrying capacity and then declined to below it",
  "Recomputed in q19 above: against a constant capacity of 1,400 the population passes above it and finishes below both the capacity and its own starting count. ERT-3.F.4 ends with population growth declining to, or below, carrying capacity."),
 ("The thirteenth year",
  "Recomputed in q20 above: the shortfalls against the capacity are 200, minus 100, 50 and 220 individuals, and the largest is unique and belongs to the last year recorded. That is the case ERT-3.F.4's phrase declining to, or BELOW, carrying capacity allows."),
 ("larger enclosures reached larger populations",
  "Recomputed in q21 above: ordered by floor area the populations reached run 40, 118, 352 and 1,060, strictly increasing. ERT-3.F.1 names SPACE alongside the available resources among the environmental factors that limit population growth."),
 ("each square metre of floor, at about twenty",
  "Recomputed in q22 above: dividing each population reached by its floor area gives about twenty individuals per square metre in all four enclosures, while both the areas and the populations differ. A constant density is what a limit set by space looks like in numbers, which is the limit ERT-3.F.1 names."),
 ("exhausted by the end of the record",
  "Recomputed in q23 above: each decade's use accounts exactly for the fall in the stock to the next decade, and the last decade's use equals what remained. ERT-3.F.2 states that resource availability and the total resource base are limited and finite over all scales of time."),
 ("the whole of the opening stock",
  "Recomputed in q24 above: 150, 220, 310 and 220 sum to 900 thousand tonnes, exactly the stock standing at the start of the first decade. ERT-3.F.2 describes the total resource base as limited and finite."),
 ("more resources relative to need grew faster",
  "Recomputed in q25 above: ordered by resources relative to need the growth rates run minus 2.3, 0.7, 4.1 and 6.4 percent a year, strictly increasing. ERT-3.F.3 states that abundant resources usually accelerate population growth."),
 ("Population 4 alone",
  "Recomputed in q26 above: exactly one of the four records a negative growth rate, and it is also the population whose resources fall furthest short of its needs. ERT-3.F.1 makes the available resources a limit on population growth."),
 # Both clauses: one distractor reverses the death rate and another reverses the
 # sharing, so either half alone would match a distractor as well as the key.
 ("shared more unequally, the death rate rose",
  "Recomputed in q27 above: the share taken by the largest quarter rises through the shortage and so does the death rate. ERT-3.F.4 states that a shrinking resource base brings an increased potential for unequal distribution of resources, which ultimately results in increased mortality, decreased fecundity, or both."),
 ("how evenly it is shared",
  "ERT-3.F.4 runs from a shrinking resource base, through the potential for unequal distribution, to increased mortality or decreased fecundity, to growth declining to or below carrying capacity. Only the keyed set measures every link of that chain; each rejected option measures at most one quantity, or something the statement never connects."),
 ("grows to match a population",
  "ERT-3.F.1 to ERT-3.F.4 supply the four rejected statements in the framework's own words. None of them offers a resource base that grows to meet demand, and ERT-3.F.2 rules it out by calling the base limited and finite over all scales of time."),
 ("raises the potential for unequal distribution",
  "ERT-3.F.1 supplies the limit and the two factors it singles out, ERT-3.F.2 the finiteness over all scales of time, ERT-3.F.3 the hedged acceleration, and ERT-3.F.4 the whole chain ending in growth declining to or below carrying capacity. Each rejected summary removes a limit, reverses a direction, exempts a timescale, or forbids the population to fall below the capacity."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19,
                20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26,
                27: q27}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e3_5, CLAIMS, TABLE_CHECKS)
