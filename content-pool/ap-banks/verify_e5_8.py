"""Key audit for AP ENVIRONMENTAL SCIENCE 5.8 Impacts of Overfishing.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.J.1 is the topic's only statement: overfishing has led to the extreme
scarcity of SOME fish species, which can lessen biodiversity in aquatic systems
and harm people who depend on fishing for food and commerce.

  scarcity of some species  -- items 1, 3, 4, 5, 6, 15, 16, 17, 18, 24, 25, 30
  lessened biodiversity     -- items 2, 7, 8, 20, 21, 27
  harm to dependent people  -- items 9, 10, 19, 26, 28

The learning objective also asks for CAUSES, which EIN-2.J.1 does not supply,
so every causal item chains to a statement that does, and the chain is named in
the claim:

  STB-1.A.2  sustainable yield is the amount of a renewable resource that can be
             taken WITHOUT REDUCING THE AVAILABLE SUPPLY -- items 11, 12, 13,
             22, 23
  EIN-2.A.1  individuals use shared resources in their own self-interest rather
             than in keeping with the common good, thereby depleting them
                                                          -- item 14

No key names a fish species, a gear, a fishery or a country, because the
framework names none. Item 18 turns on the framework's word SOME.

DATA ITEMS: 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 21, 24, 25 and 28 carry
tables, recomputed below from those tables alone and anchored to named rows.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_8

STOCK = "Adult fish remaining in the stock (thousand tonnes)"
CATCH = "Fish landed by the fleet in the decade (thousand tonnes)"
DAYS = "Days at sea worked by the fleet (thousands)"
LANDED = "Fish landed (thousand tonnes)"
PRESSURE = "Fishing pressure applied over twenty years (relative units)"
SPP = "Fish species recorded in the survey"
PORT_LAND = "Fish landed at the port (thousand tonnes)"
JOBS = "People employed in fishing and processing at the port"
TAKE = "Fish taken each year (thousand tonnes)"
LEFT = "Stock remaining after twelve years (thousand tonnes)"
RECOVER = "Adult fish in the stock (thousand tonnes)"

SUSTAINABLE = "Take held at the amount the stock replaces"
OVER = "Take set above the amount the stock replaces"


def q3(table, item):
    s = cg.col(table, STOCK)
    c = cg.col(table, CATCH)
    assert cg.cell(table, "First", STOCK) == max(s), "the first decade must hold the largest stock"
    assert all(s[i] > s[i + 1] for i in range(len(s) - 1)), f"the stock must fall; got {s}"
    assert c[-1] > s[-1], f"the final catch {c[-1]} must exceed the final stock {s[-1]}"
    return (f"the stock runs {s} thousand tonnes while the catch runs {c}, so the stock falls "
            "without a reversal and the last catch exceeds what is left")


def q4(table, item):
    d = cg.cell(table, "First", STOCK) - cg.cell(table, "Fourth", STOCK)
    assert d == 840, f"the loss recomputes to {d}, not 840"
    for wrong in (900, 590, 250, 960):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"900 minus 60 is {d:.0f} thousand tonnes of stock lost"


def q5(table, item):
    e = cg.col(table, DAYS)
    l = cg.col(table, LANDED)
    assert cg.cell(table, "Year 1", DAYS) == min(e), "the first year must carry the least effort"
    assert all(e[i] < e[i + 1] for i in range(len(e) - 1)), f"effort must rise; got {e}"
    assert max(l) > l[0], "landings must rise before they fall"
    assert l[-1] < l[0], f"landings must end below their starting value; got {l}"
    return (f"days at sea run {e} thousand while landings run {l} thousand tonnes, effort "
            "rising throughout and landings peaking then falling below their start")


def q6(table, item):
    first = cg.cell(table, "Year 1", LANDED) / cg.cell(table, "Year 1", DAYS)
    last = cg.cell(table, "Year 24", LANDED) / cg.cell(table, "Year 24", DAYS)
    assert first == 5, f"the opening return recomputes to {first}, not 5"
    assert last == 0.5, f"the closing return recomputes to {last}, not 0.5"
    assert last < first, "the return per unit effort must fall across the record"
    return (f"100 over 20 is {first:.1f} and 40 over 80 is {last:.1f} thousand tonnes per "
            "thousand days, a fall of a factor of ten")


def q7(table, item):
    pairs = sorted(zip(cg.col(table, PRESSURE), cg.col(table, SPP)))
    assert cg.cell(table, "Area 1", PRESSURE) == min(cg.col(table, PRESSURE)), \
        "Area 1 must carry the lightest fishing pressure"
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"species recorded must fall as pressure rises; got {pairs}"
    assert len(set(cg.col(table, SPP))) > 1, "'the same number of species' must be false"
    return (f"sorted by pressure the species counts are {[s for _, s in pairs]}, falling "
            "without exception")


def q8(table, item):
    spp = dict(zip(cg.labels(table), cg.col(table, SPP)))
    press = dict(zip(cg.labels(table), cg.col(table, PRESSURE)))
    light, heavy = min(press, key=press.get), max(press, key=press.get)
    d = spp[light] - spp[heavy]
    assert d == 36, f"the difference recomputes to {d}, not 36"
    for wrong in (44, 27, 9, 52):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"44 minus 8 is {d:.0f} more species in the least fished area"


def q9(table, item):
    l = cg.col(table, PORT_LAND)
    j = cg.col(table, JOBS)
    assert cg.cell(table, "Before the decline", PORT_LAND) == max(l), \
        "the earliest period must carry the largest landings"
    assert all(l[i] > l[i + 1] for i in range(len(l) - 1)), f"landings must fall; got {l}"
    assert all(j[i] > j[i + 1] for i in range(len(j) - 1)), f"employment must fall; got {j}"
    return (f"landings run {l} thousand tonnes while employment runs {j} people, both falling "
            "without a reversal")


def q10(table, item):
    d = (cg.cell(table, "Before the decline", JOBS)
         - cg.cell(table, "Twenty years into the decline", JOBS))
    assert d == 2100, f"the loss recomputes to {d}, not 2,100"
    for wrong in (2400, 1300, 800, 2700):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"2,400 minus 300 is {d:.0f} jobs lost across the twenty years"


def q12(table, item):
    assert cg.cell(table, SUSTAINABLE, TAKE) < cg.cell(table, OVER, TAKE), \
        "the sustainable rule must take the smaller annual catch"
    assert cg.cell(table, SUSTAINABLE, LEFT) > cg.cell(table, OVER, LEFT), \
        "the sustainable rule must leave the larger stock"
    assert cg.cell(table, OVER, LEFT) > 0, "'both stocks reduced to nothing' must be false"
    assert cg.cell(table, OVER, TAKE) > 0, "'yielded no fish at all' must be false"
    return (f"the sustainable rule takes {cg.cell(table, SUSTAINABLE, TAKE):.0f} thousand "
            f"tonnes a year and leaves {cg.cell(table, SUSTAINABLE, LEFT):.0f}, against "
            f"{cg.cell(table, OVER, TAKE):.0f} and {cg.cell(table, OVER, LEFT):.0f}")


def q13(table, item):
    d = cg.cell(table, SUSTAINABLE, LEFT) - cg.cell(table, OVER, LEFT)
    assert d == 430, f"the difference recomputes to {d}, not 430"
    for wrong in (500, 70, 50, 570):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"500 minus 70 is {d:.0f} thousand tonnes more stock left under the sustainable rule"


def q15(table, item):
    v = cg.col(table, RECOVER)
    assert cg.cell(table, "At closure", RECOVER) == min(v), \
        "the closure row must hold the smallest stock"
    assert all(v[i] < v[i + 1] for i in range(len(v) - 1)), f"the stock must grow; got {v}"
    assert v[1] < v[-1], "the five-year value must remain below the fifteen-year value"
    return f"the stock runs {v} thousand tonnes from closure onward, rising without a reversal"


def q16(table, item):
    base = cg.cell(table, "At closure", RECOVER)
    assert base > 0, "the closure stock must be non-zero for a ratio to exist"
    r = cg.cell(table, "Fifteen", RECOVER) / base
    assert abs(r - 8) < 1, f"the ratio recomputes to {r}, which is not about eight"
    for wrong in (2, 5, 15, 1):
        assert abs(r - wrong) > 1, f"the {wrong} distractor equals the key"
    return f"460 divided by 60 is {r:.1f}, which rounds to about eight times the stock at closure"


def q21(table, item):
    spp = dict(zip(cg.labels(table), cg.col(table, SPP)))
    press = dict(zip(cg.labels(table), cg.col(table, PRESSURE)))
    light, heavy = min(press, key=press.get), max(press, key=press.get)
    assert spp[light] == 44 and spp[heavy] == 8, \
        f"the two counts recompute to {spp[light]} and {spp[heavy]}"
    assert abs(spp[light] / spp[heavy] - 11.0 / 2.0) < 1e-9, \
        f"the ratio recomputes to {spp[light] / spp[heavy]}, not eleven to two"
    return f"44 to 8 reduces to 11 to 2 between the least and most heavily fished areas"


def q24(table, item):
    labs = cg.labels(table)
    s = cg.col(table, STOCK)
    c = cg.col(table, CATCH)
    over = [labs[i] for i in range(len(labs)) if c[i] > s[i]]
    assert over == ["Fourth"], f"the catch exceeds the stock left only in {over}"
    assert c[-1] == 70 and s[-1] == 60, f"the final decade reads {c[-1]} and {s[-1]}"
    return (f"comparing the two columns decade by decade, the catch first exceeds the stock "
            f"remaining in the fourth decade, {c[-1]:.0f} against {s[-1]:.0f} thousand tonnes")


def q25(table, item):
    e = cg.col(table, DAYS)
    l = cg.col(table, LANDED)
    assert e[-1] / e[0] == 4, f"effort rose by a factor of {e[-1] / e[0]}, not four"
    assert l[-1] < l[0], f"landings must end below their start; got {l}"
    return (f"days at sea rise from {e[0]:.0f} to {e[-1]:.0f} thousand while landings fall "
            f"from {l[0]:.0f} to {l[-1]:.0f} thousand tonnes")


def q28(table, item):
    start = cg.cell(table, "Before the decline", JOBS)
    assert start > 0, "the opening employment must be non-zero for a fraction to exist"
    frac = cg.cell(table, "Twenty years into the decline", JOBS) / start
    assert abs(frac - 0.125) < 1e-9, f"the fraction recomputes to {frac}, not one eighth"
    for wrong in (0.5, 0.25, 0.75, 1.0):
        assert abs(frac - wrong) > 1e-9, "a rejected fraction equals the key"
    return f"300 over 2,400 is {frac:.3f}, which is one eighth of the original employment"


CLAIMS = [
 ("extreme scarcity of some fish species",
  "EIN-2.J.1, near verbatim: overfishing has led to the extreme scarcity of SOME fish species. The framework's word is some rather than all, and it claims scarcity rather than global extinction."),
 ("lessen biodiversity in aquatic systems and harm people",
  "EIN-2.J.1 states that the extreme scarcity can lessen biodiversity in aquatic systems and harm people who depend on fishing for food and commerce. Each rejected option reverses one or both directions."),
 ("catch was larger than what was left",
  "Recomputed in q3 above: the stock falls from 900 to 60 thousand tonnes and the final catch of 70 exceeds the 60 remaining. EIN-2.J.1 records the extreme scarcity of some fish species as the result of overfishing."),
 ("840 thousand tonnes",
  "Recomputed in q4 above: 900 minus 60 thousand tonnes. The rejected values quote the opening stock alone, pair the wrong decades, or add the two."),
 ("more work was producing less fish",
  "Recomputed in q5 above: days at sea rise from 20 to 80 thousand while landings peak and then fall from 100 to 40 thousand tonnes. EIN-2.J.1 records the extreme scarcity of some fish species as the result of overfishing."),
 ("to 0.5 thousand tonnes per thousand days",
  "Recomputed in q6 above: 100 over 20 at the start and 40 over 80 at the end, a fall of a factor of ten in the return for the same work. That is the scarcity of EIN-2.J.1 measured against effort."),
 ("heavier fishing pressure recorded fewer fish species",
  "Recomputed in q7 above: pressures of 1, 4, 9 and 16 relative units against species counts of 44, 31, 17 and 8. EIN-2.J.1 states that the extreme scarcity of some fish species can lessen biodiversity in aquatic systems."),
 ("36 more species",
  "Recomputed in q8 above: 44 minus 8 species. The rejected values quote the largest count alone, pair the wrong areas, or add the two."),
 ("which is the harm to people dependent on fishing",
  "Recomputed in q9 above: landings of 58, 26 and 7 thousand tonnes against employment of 2,400, 1,100 and 300. EIN-2.J.1 states that the scarcity can harm people who depend on fishing for food and commerce."),
 ("2,100 jobs",
  "Recomputed in q10 above: 2,400 minus 300 jobs. The rejected values quote the opening count alone, pair the wrong periods, or add the two."),
 ("without reducing the available supply",
  "STB-1.A.2 defines sustainable yield as the amount of a renewable resource that can be taken WITHOUT REDUCING THE AVAILABLE SUPPLY, so a catch that reduces the supply is above it. The rejected statements are STB-1.F.1, STB-3.F.1, ENG-2.B.2 and EIN-2.M.3."),
 ("fished at the amount it replaces was left far larger",
  "Recomputed in q12 above: 500 thousand tonnes remaining against 70, on annual takes of 40 and 90. STB-1.A.2 makes the sustainable yield the amount that can be taken without reducing the available supply."),
 ("Larger by 430 thousand tonnes",
  "Recomputed in q13 above: 500 minus 70 thousand tonnes. The rejected values quote one remaining stock alone, use the difference in annual takes, or add the two."),
 ("cost of the reduced stock falls on every boat",
  "EIN-2.A.1 states that individuals will use shared resources in their own self-interest rather than in keeping with the common good, thereby depleting the resources, and the division of the cost across all users is what makes that so. The rejected options concentrate the cost on one user or replace the incentive with ignorance."),
 ("grew in every interval after the closure",
  "Recomputed in q15 above: 60, 140, 290 and 460 thousand tonnes at closure and after five, ten and fifteen years. EIN-2.J.1 records the scarcity that follows overfishing, and this is what removing the pressure does to it."),
 ("About eight times as large",
  "Recomputed in q16 above: 460 divided by 60, which is about 7.7. The rejected values come from earlier points in the record or from the number of years."),
 ("lands less fish year after year while the stock keeps falling",
  "EIN-2.J.1 ties overfishing to the extreme scarcity of some fish species and STB-1.A.2 makes the sustainable amount the one that does not reduce the available supply, so a falling stock beside a falling return for the same work is the diagnostic pair. Fish farming is STB-1.F, a different topic."),
 ("scarcity of SOME fish species rather than all",
  "EIN-2.J.1 says overfishing has led to the extreme scarcity of SOME fish species, so a mixed picture across a bay is what the framework describes rather than evidence against it."),
 ("harm to people who depend on fishing for food and commerce",
  "EIN-2.J.1 names harm to people who depend on fishing FOR FOOD AND COMMERCE, and the described town depends on the fishery for both. The other options name the framework's other consequences or belong to STB-1.A.2 and STB-1.F.1."),
 ("number of fish species recorded in repeated surveys",
  "EIN-2.J.1 says the scarcity can LESSEN BIODIVERSITY IN AQUATIC SYSTEMS, and a count of species present in repeated surveys measures that directly. Landings, price, effort and boat size measure the fishery rather than the diversity of the system."),
 ("About eleven to two",
  "Recomputed in q21 above: 44 species against 8, which reduces to 11 to 2. The rejected values invert the ratio or use the fishing pressure column."),
 ("Limit the annual catch to an amount the stock can replace",
  "STB-1.A.2 defines sustainable yield as the amount that can be taken without reducing the available supply, so holding the catch at that amount is what the definition prescribes. Each rejected option raises the take, moves it, or leaves it to the self-interested choice EIN-2.A.1 describes."),
 ("mass of the stock remaining at the end of each year",
  "STB-1.A.2 defines the sustainable amount as the one that does not reduce the available supply, so the test compares what is taken with what remains from year to year. The rejected pairs leave one side of that comparison unmeasured."),
 ("fourth decade, when 70 thousand tonnes were landed",
  "Recomputed in q24 above: the catch stays below the stock remaining in the first three decades and exceeds it only in the fourth. EIN-2.J.1 records extreme scarcity as the outcome of overfishing."),
 ("effort quadrupled while landings ended below",
  "Recomputed in q25 above: effort rises by a factor of four while landings fall from 100 to 40 thousand tonnes. That falling return for rising effort is the scarcity EIN-2.J.1 describes, which a raw landings total conceals."),
 ("harmed in both its food supply and its commerce",
  "EIN-2.J.1 names harm to people who depend on fishing FOR FOOD AND COMMERCE, which covers both. The framework does not restrict the harm to one of the two nor confine the consequences to the ecosystem."),
 ("ecological consequence is lessened biodiversity",
  "EIN-2.J.1 puts lessened biodiversity in aquatic systems and harm to people who depend on fishing side by side, one about the system and one about the people. The rejected options swap them or collapse the pair."),
 ("One eighth of it",
  "Recomputed in q28 above: 300 over 2,400 jobs. The rejected fractions correspond to other pairs of periods or deny that employment changed."),
 ("neighbouring area where no fishing was permitted",
  "If an unfished area declined by the same amount, the fishing is not doing the work the claim assigns it. The other observations are consistent with EIN-2.J.1's links between overfishing, scarcity, lessened biodiversity and harm to dependent people."),
 ("made some fish species extremely scarce, which can lessen aquatic",
  "EIN-2.J.1 states that overfishing has led to the extreme scarcity of some fish species, which can lessen biodiversity in aquatic systems and harm people who depend on fishing for food and commerce. Each rejected summary reverses a direction, drops a consequence, or strengthens scarcity into extinction."),
]

TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 12: q12,
                13: q13, 15: q15, 16: q16, 21: q21, 24: q24, 25: q25, 28: q28}

e_check.run(e5_8, CLAIMS, TABLE_CHECKS)
